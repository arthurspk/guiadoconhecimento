#!/usr/bin/env python3
"""Confere se os links da base respondem e grava data/status-links.json.

Usa o Scrapling (Fetcher, com impersonação de navegador e retentativas) quando instalado;
senão, urllib da stdlib. O selecionar.py tira da base os links que falharam em duas rodadas seguidas (essenciais nunca).

Uso:
    python3 scripts/checar_links.py                  # todos (demora: ~15 mil URLs)
    python3 scripts/checar_links.py --area seo       # uma área
    python3 scripts/checar_links.py --limite 300     # amostra
"""
import argparse, concurrent.futures as cf, json, os, random, time, urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(RAIZ, 'data', *p)
try:
    from scrapling.fetchers import Fetcher  # type: ignore
    import logging
    logging.getLogger('scrapling').setLevel(logging.CRITICAL)
except Exception:
    Fetcher = None

OK_MESMO_COM_ERRO = {401, 403, 405, 429, 999}  # sites que barram robôs mas estão no ar

def checar(url):
    try:
        if Fetcher:
            r = Fetcher.get(url, timeout=20, retries=1, follow_redirects=True)
            code = r.status
        else:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (guia; verificador de links)'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                code = resp.status
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:
        return {'status': 'erro', 'detalhe': type(e).__name__}
    if 200 <= code < 400 or code in OK_MESMO_COM_ERRO:
        return {'status': 'ok', 'codigo': code}
    return {'status': 'quebrado', 'codigo': code}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--area'); ap.add_argument('--limite', type=int); ap.add_argument('--workers', type=int, default=16)
    a = ap.parse_args()
    links = [json.loads(l) for l in open(D('links.jsonl'), encoding='utf-8')]
    estado = json.load(open(D('status-links.json'), encoding='utf-8')) if os.path.exists(D('status-links.json')) else {}
    urls = sorted({x['url'] for x in links if not a.area or x['area'] == a.area})
    if a.limite:
        random.seed(42); urls = random.sample(urls, min(a.limite, len(urls)))
    t0 = time.time(); cont = {'ok': 0, 'quebrado': 0, 'erro': 0}
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for url, res in zip(urls, ex.map(checar, urls)):
            ant = estado.get(url, {})
            falhas = ant.get('falhas', 0) + 1 if res['status'] != 'ok' else 0
            estado[url] = dict(res, falhas=falhas, quando=time.strftime('%Y-%m-%d'))
            cont[res['status']] += 1
    json.dump(estado, open(D('status-links.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    print(f"{len(urls)} URLs em {time.time() - t0:.0f}s via {'Scrapling' if Fetcher else 'urllib'}: {cont}")

if __name__ == '__main__':
    main()
