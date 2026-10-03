#!/usr/bin/env python3
"""Coleta repositórios de IA por profissão na busca do GitHub (via `gh api`).

Lê data/repos-ia-consultas.json (temas e consultas de cada trilha) e grava
data/repos-ia.jsonl com exatamente ALVO repositórios por trilha, cada um com a
descrição pública do próprio repositório. Quando os temas da profissão não
chegam a ALVO, completa com o tema "geral" (IA e automação de uso geral).

Cada resposta da API fica em .cache/repos-ia/, então rodar de novo é barato.
Uso: python3 scripts/coletar_repos_ia.py [--trilha <slug>] [--alvo 1000]
"""
import argparse, hashlib, json, os, re, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
CACHE = J('.cache', 'repos-ia')
ALVO = 1000
MIN_ESTRELAS = 3
PAGINAS_1, PAGINAS_2 = 3, 10   # 1ª passada: até 300 por consulta; 2ª: até o limite da API (1000)
INTERVALO = 2.1                # a busca do GitHub aceita 30 requisições por minuto: uma a cada 2,1 s
_trava, _proxima = threading.Lock(), [0.0]

SINAL_IA = re.compile(
    r"(?<![a-z])(ai|a\.i\.|llms?|gpt\w*|chatgpt|agents?|agentic|ml|mlops|llmops|aiops|automl|tinyml|nlp|rag|mcp|tts|stt|asr|ocr|"
    r"bots?|chatbots?|copilot|claude|gemini|openai|ollama|llama\w*|whisper|yolo\w*|nerf|bert|lora|gguf|"
    r"neural|diffusion|transformers?|embeddings?|generative|genai|autonomous|assistant|"
    r"machine[- ]learning|deep[- ]learning|reinforcement[- ]learning|computer[- ]vision|language[- ]models?|"
    r"text[- ]to[- ]\w+|speech|voice|predict\w*|forecast\w*|detect\w*|recogni\w*|segment\w*|recommend\w*|"
    r"automat\w*|intelligen\w*|prompts?|fine[- ]?tun\w*|inference|models?)(?![a-z])", re.I)
BLOQUEIO = re.compile(
    r"nsfw|porn|hentai|undress|deepnude|nude|onlyfans|sex|crack(ed|s)?\b|keygen|aimbot|wallhack|cheat(s|er)?\b|"
    r"free[- ]api[- ]key|leaked|account[- ]generator|casino|gambling|betting|unlimited[- ]free|"
    r"bypass (paywall|license|detection)|stealer|\brat\b|ransomware builder", re.I)


def latino(texto: str) -> bool:
    """Descrição em alfabeto latino (dá para traduzir com segurança)."""
    letras = [c for c in texto if c.isalpha()]
    return bool(letras) and sum(c < 'ɐ' for c in letras) / len(letras) >= 0.9


def esperar_vez() -> None:
    """Espaça o início das requisições (vale para todas as threads)."""
    with _trava:
        agora = time.time()
        vez = max(agora, _proxima[0])
        _proxima[0] = vez + INTERVALO
    time.sleep(max(0.0, vez - agora))


def prebuscar(consultas: list, paginas: range) -> None:
    """Enche o cache em paralelo: uma página por vez, só para as consultas que ainda têm resultados."""
    with ThreadPoolExecutor(max_workers=2) as pool:
        for p in paginas:
            pendentes = [c for c in consultas if p == 1 or len(buscar(c, p - 1)['itens']) == 100 and (p - 1) * 100 < min(buscar(c, p - 1)['total'], 1000)]
            list(pool.map(lambda c: buscar(c, p), pendentes))


def buscar(consulta: str, pagina: int) -> dict:
    """Uma página (100 itens) da busca de repositórios, com cache em disco."""
    q = f"{consulta} stars:>={MIN_ESTRELAS} archived:false fork:false"
    arq = os.path.join(CACHE, hashlib.sha1(f"{q}|{pagina}".encode()).hexdigest() + '.json')
    if os.path.exists(arq):
        return json.load(open(arq, encoding='utf-8'))
    cmd = ['gh', 'api', '-X', 'GET', 'search/repositories', '-f', f'q={q}', '-f', 'sort=stars',
           '-f', 'order=desc', '-f', 'per_page=100', '-f', f'page={pagina}']
    for tentativa in range(8):
        esperar_vez()
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            bruto = json.loads(r.stdout)
            dados = {'total': bruto.get('total_count', 0), 'itens': [resumir(i) for i in bruto.get('items', [])]}
            json.dump(dados, open(arq, 'w', encoding='utf-8'), ensure_ascii=False)
            return dados
        if 'rate limit' in (r.stdout + r.stderr).lower():
            time.sleep(35)
            continue
        print(f"  FALHA em '{consulta}' p{pagina}: {(r.stderr or r.stdout)[:160]}", file=sys.stderr)
        time.sleep(5 * (tentativa + 1))
    return {'total': 0, 'itens': []}


def resumir(i: dict) -> dict:
    return {'nome': i['full_name'], 'url': i['html_url'], 'descricao': (i.get('description') or '').strip(),
            'estrelas': i.get('stargazers_count', 0), 'linguagem': i.get('language') or '',
            'licenca': (i.get('license') or {}).get('spdx_id') or '', 'atualizado': (i.get('pushed_at') or '')[:10],
            'topicos': i.get('topics') or []}


def serve(r: dict) -> bool:
    d = r['descricao']
    texto = f"{r['nome']} {d} {' '.join(r['topicos'])}"
    return len(d) >= 15 and latino(d) and not BLOQUEIO.search(texto) and bool(SINAL_IA.search(texto))


def coletar_consultas(consultas: list, paginas: range, achados: dict, tema: int) -> None:
    """Soma em `achados` (nome → repo) o que cada consulta devolve nas páginas pedidas."""
    for c in consultas:
        for p in paginas:
            res = buscar(c, p)
            for r in res['itens']:
                if serve(r) and r['nome'].lower() not in achados:
                    achados[r['nome'].lower()] = dict(r, tema=tema)
            if len(res['itens']) < 100 or p * 100 >= min(res['total'], 1000):
                break


def coletar_trilha(temas: list, gerais: list, alvo: int) -> list:
    achados: dict = {}
    todas = [c for _, _, _, consultas in temas for c in consultas]
    prebuscar(todas, range(1, PAGINAS_1 + 1))
    for n, (_, _, _, consultas) in enumerate(temas):
        coletar_consultas(consultas, range(1, PAGINAS_1 + 1), achados, n)
    if len(achados) < alvo:
        prebuscar(todas, range(PAGINAS_1 + 1, PAGINAS_2 + 1))
        for n, (_, _, _, consultas) in enumerate(temas):
            coletar_consultas(consultas, range(PAGINAS_1 + 1, PAGINAS_2 + 1), achados, n)
    escolhidos = sorted(achados.values(), key=lambda r: (-r['estrelas'], r['nome'].lower()))[:alvo]
    usados = {r['nome'].lower() for r in escolhidos}
    for r in gerais:
        if len(escolhidos) >= alvo:
            break
        if r['nome'].lower() not in usados:
            escolhidos.append(dict(r, tema=-1)); usados.add(r['nome'].lower())
    return escolhidos


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--trilha', help='recoleta só esta trilha e mescla com o que já existe')
    ap.add_argument('--alvo', type=int, default=ALVO)
    args = ap.parse_args()
    os.makedirs(CACHE, exist_ok=True)
    cfg = json.load(open(J('data', 'repos-ia-consultas.json'), encoding='utf-8'))
    saida = J('data', 'repos-ia.jsonl')
    antigos = [json.loads(l) for l in open(saida, encoding='utf-8')] if args.trilha and os.path.exists(saida) else []

    base_geral: dict = {}
    prebuscar(cfg['geral']['consultas'], range(1, PAGINAS_2 + 1))
    coletar_consultas(cfg['geral']['consultas'], range(1, PAGINAS_2 + 1), base_geral, -1)
    gerais = sorted(base_geral.values(), key=lambda r: (-r['estrelas'], r['nome'].lower()))
    print(f"tema geral: {len(gerais)} repositórios", flush=True)

    linhas, resumo = [], {}
    for slug, temas in cfg['trilhas'].items():
        if args.trilha and slug != args.trilha:
            linhas += [x for x in antigos if x['trilha'] == slug]
            continue
        repos = coletar_trilha(temas, gerais, args.alvo)
        proprios = sum(1 for r in repos if r['tema'] >= 0)
        resumo[slug] = {'total': len(repos), 'do_oficio': proprios, 'gerais': len(repos) - proprios}
        print(f"{slug}: {len(repos)} ({proprios} do ofício, {len(repos) - proprios} gerais)", flush=True)
        linhas += [{'trilha': slug, **{k: r[k] for k in ('tema', 'nome', 'url', 'descricao', 'estrelas', 'linguagem', 'licenca', 'atualizado')}}
                   for r in repos]
    with open(saida, 'w', encoding='utf-8') as f:
        for x in linhas:
            f.write(json.dumps(x, ensure_ascii=False) + '\n')
    meta_arq = J('data', 'repos-ia-meta.json')
    meta = json.load(open(meta_arq, encoding='utf-8')) if args.trilha and os.path.exists(meta_arq) else {'trilhas': {}}
    meta['coletado_em'] = time.strftime('%Y-%m-%d')
    meta['trilhas'].update(resumo)
    json.dump(meta, open(meta_arq, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"{len(linhas)} linhas em data/repos-ia.jsonl ({len({x['url'] for x in linhas})} repositórios únicos)")


if __name__ == '__main__':
    main()
