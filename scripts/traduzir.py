#!/usr/bin/env python3
"""Traduz as descrições e os nomes de tópico para os idiomas do guia, offline.

Usa os modelos abertos do Argos Translate direto no CTranslate2, em lote. Cada texto é tratado como
português ou inglês; o inglês é o pivô (pt → en → outros). Só traduz o que ainda não está em
data/i18n/desc.<idioma>.json.gz ({hash do texto: tradução}), então rodar de novo é incremental.

Uso: python3 scripts/traduzir.py [--idiomas es,fr]     (pip install argostranslate)
"""
import argparse, gzip, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import CODIGOS, IDIOMAS, J, h, idioma_de, limpa

ARGOS = {cod: argos for cod, _, _, _, argos in IDIOMAS}
LOTE = 64


def textos_do_guia() -> list:
    """Tudo o que aparece nas páginas e não é texto da interface: descrições e nomes de tópico."""
    textos = set()
    for linha in open(J('data', 'links.jsonl'), encoding='utf-8'):
        x = json.loads(linha)
        textos.add(limpa(x['descricao']))
        if not x.get('grupo'):
            textos.add(x['topico'])
        elif x['topico']:
            textos.add(x['topico'])
    arq = J('data', 'repos-ia.jsonl')
    if os.path.exists(arq):
        for linha in open(arq, encoding='utf-8'):
            textos.add(limpa(json.loads(linha)['descricao']))
    return sorted(t for t in textos if t and any(ch.isalpha() for ch in t))


class Modelo:
    """Um par de idiomas do Argos, carregado no CTranslate2."""

    def __init__(self, de: str, para: str):
        import argostranslate.package as pacotes
        import ctranslate2, sentencepiece
        pk = next((p for p in pacotes.get_installed_packages() if p.from_code == de and p.to_code == para), None)
        if pk is None:
            pacotes.update_package_index()
            novo = next(p for p in pacotes.get_available_packages() if p.from_code == de and p.to_code == para)
            pacotes.install_from_path(novo.download())
            pk = next(p for p in pacotes.get_installed_packages() if p.from_code == de and p.to_code == para)
        pasta = str(pk.package_path)
        self.sp = sentencepiece.SentencePieceProcessor(os.path.join(pasta, 'sentencepiece.model'))
        self.tr = ctranslate2.Translator(os.path.join(pasta, 'model'), device='cpu', inter_threads=4, intra_threads=3)

    def traduzir(self, frases: list) -> list:
        tokens = [self.sp.encode(f, out_type=str) for f in frases]
        res = self.tr.translate_batch(tokens, max_batch_size=LOTE, batch_type='examples', beam_size=2,
                                      max_decoding_length=256, repetition_penalty=1.2)
        return [''.join(r.hypotheses[0]).replace('▁', ' ').strip() for r in res]   # peças do SentencePiece → texto


def caminho(lang: str) -> str:
    return J('data', 'i18n', f'desc.{lang}.json.gz')


def ler(lang: str) -> dict:
    return json.load(gzip.open(caminho(lang), 'rt', encoding='utf-8')) if os.path.exists(caminho(lang)) else {}


def gravar(lang: str, dados: dict) -> None:
    os.makedirs(os.path.dirname(caminho(lang)), exist_ok=True)
    with open(caminho(lang), 'wb') as f, gzip.GzipFile(fileobj=f, mode='wb', mtime=0) as g:   # mtime fixo: saída determinística
        g.write(json.dumps(dict(sorted(dados.items())), ensure_ascii=False, separators=(',', ':')).encode('utf-8'))


def completar(lang: str, de: str, para: str, pares: list, dados: dict) -> None:
    """pares: [(texto original, texto de entrada do modelo)]; grava a tradução sob o hash do original."""
    pares = [(o, e) for o, e in pares if h(o) not in dados]
    if not pares:
        return
    t0 = time.time()
    modelo = Modelo(de, para)
    saidas = modelo.traduzir([e for _, e in pares])
    for (o, e), s in zip(pares, saidas):
        if s and len(s) <= 4 * len(e) + 20:   # tradução vazia ou que disparou em repetição: fica o original
            dados[h(o)] = limpa(s)
    gravar(lang, dados)
    print(f'  {lang}: {len(pares)} textos ({de}→{para}) em {time.time() - t0:.0f}s', flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--idiomas', default=','.join(CODIGOS))
    idiomas = [i for i in ap.parse_args().idiomas.split(',') if i in CODIGOS]
    textos = textos_do_guia()
    em_pt = [t for t in textos if idioma_de(t) == 'pt']
    em_en = [t for t in textos if idioma_de(t) == 'en']
    print(f'{len(textos)} textos: {len(em_pt)} em português, {len(em_en)} em inglês', flush=True)

    ingles = ler('en')                                  # pivô: os textos em português, em inglês
    completar('en', ARGOS['pt'], 'en', [(t, t) for t in em_pt], ingles)
    pivo = [(t, ingles[h(t)]) for t in em_pt if h(t) in ingles] + [(t, t) for t in em_en]
    for lang in idiomas:
        if lang == 'en':
            continue
        pares = [(t, t) for t in em_en] if lang == 'pt' else pivo
        completar(lang, 'en', ARGOS[lang], pares, ler(lang))
    print('pronto')


if __name__ == '__main__':
    main()
