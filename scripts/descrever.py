#!/usr/bin/env python3
"""Busca a descrição pública (campo "About") dos repositórios do GitHub que ficaram sem descrição.

Um link fica sem descrição quando a lista de origem não tem uma ou quando a licença da lista não
permite copiar o texto (sem licença, GPL, NC). Para repositórios do GitHub, a descrição que o próprio
projeto publica resolve isso. O resultado vai para data/descricoes.json ({url: descrição}), que o
selecionar.py usa. Links que continuam sem descrição não entram no guia.

Uso: python3 scripts/descrever.py   (precisa do `gh` autenticado; consulta 100 repositórios por chamada)
"""
import gzip, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import J, limpa
from coletar_repos_ia import latino
from selecionar import normalizar_url

SAIDA = J('data', 'descricoes.json')
SEM = J('.cache', 'descrever-sem.json')   # repositórios já consultados que não têm descrição aproveitável
REPO = re.compile(r'^https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/?$')
LOTE = 100


def precisa(it: dict) -> bool:
    lic = it.get('licenca', '')
    return not it.get('descricao', '').strip() or lic == 'sem-licenca' or lic.startswith(('CC-BY-NC', 'GPL'))


def consultar(lote: list) -> dict:
    """lote: [(url, dono, repo)] → {url: descrição ou ''} numa única chamada GraphQL."""
    campos = ' '.join(f'r{i}: repository(owner: {json.dumps(d)}, name: {json.dumps(r)}) {{ description isArchived }}'
                      for i, (_, d, r) in enumerate(lote))
    res = subprocess.run(['gh', 'api', 'graphql', '-f', f'query={{ {campos} }}'], capture_output=True, text=True)
    try:
        dados = json.loads(res.stdout).get('data') or {}   # repositório inexistente vem como erro parcial: o resto vale
    except json.JSONDecodeError:
        print(f'  FALHA no lote: {(res.stderr or res.stdout)[:160]}', file=sys.stderr)
        return {}
    return {url: ((dados.get(f'r{i}') or {}).get('description') or '') for i, (url, _, _) in enumerate(lote)}


def main() -> None:
    feitas = json.load(open(SAIDA, encoding='utf-8')) if os.path.exists(SAIDA) else {}
    sem = set(json.load(open(SEM, encoding='utf-8'))) if os.path.exists(SEM) else set()
    pendentes = {}
    for linha in gzip.open(J('data', 'brutos.jsonl.gz'), 'rt', encoding='utf-8'):
        it = json.loads(linha)
        if not precisa(it):
            continue
        url = normalizar_url(it['url'])
        m = REPO.match(url)
        if m and url not in feitas and url not in sem:
            pendentes[url] = (url, m.group(1), m.group(2).removesuffix('.git'))
    fila = sorted(pendentes.values())
    print(f'{len(fila)} repositórios a consultar ({len(feitas)} já descritos)', flush=True)
    for i in range(0, len(fila), LOTE):
        for url, desc in consultar(fila[i:i + LOTE]).items():
            d = limpa(desc)
            if len(d) >= 15 and latino(d):
                feitas[url] = d
            else:
                sem.add(url)
        if i // LOTE % 10 == 9:
            print(f'  {i + LOTE} consultados', flush=True)
    json.dump(dict(sorted(feitas.items())), open(SAIDA, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    os.makedirs(os.path.dirname(SEM), exist_ok=True)
    json.dump(sorted(sem), open(SEM, 'w', encoding='utf-8'))
    print(f'{len(feitas)} descrições em data/descricoes.json; {len(sem)} repositórios sem descrição aproveitável')


if __name__ == '__main__':
    main()
