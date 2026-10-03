#!/usr/bin/env python3
"""Valida a base e as páginas geradas. Sai com código 1 se algo estiver errado.

Confere: JSONs válidos; toda área da taxonomia tem página e links; nenhum link repetido
dentro da mesma área; todo link tem descrição; cada profissão tem exatamente 1000 repositórios
de IA, todos com descrição; cada idioma tem o mesmo conjunto de páginas e todos os textos da
interface; toda seção (##) das páginas geradas tem uma descrição; todas as âncoras e links
internos apontam para algo que existe; contagem total dentro da meta.
"""
import collections, json, os, re, sys, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))
from base import CODIGOS, Ctx, textos_pt
from conferir_textos import problemas

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
erros = []
def erro(m): erros.append(m)

tax = json.load(open(J('data', 'taxonomia.json'), encoding='utf-8'))
areas = {a['slug']: s['slug'] for s in tax['setores'] for a in s['areas']}
links = [json.loads(l) for l in open(J('data', 'links.jsonl'), encoding='utf-8')]
for f in ('fontes.json', 'fontes-guias.json', 'essenciais.json', 'trilhas.json', 'config.json'):
    json.load(open(J('data', f), encoding='utf-8'))
for t in json.load(open(J('data', 'trilhas.json'), encoding='utf-8'))['trilhas']:
    for a in t['areas']:
        if a not in areas: erro(f"trilha {t['slug']} cita área inexistente {a}")

campos = {'nome', 'url', 'descricao', 'topico', 'area', 'fonte', 'tipo', 'essencial'}
vistos = collections.defaultdict(set)
for i, x in enumerate(links):
    if not campos <= set(x): erro(f'links.jsonl linha {i+1}: campos faltando {campos - set(x)}')
    if x['area'] not in areas: erro(f"área desconhecida {x['area']}")
    if not x['url'].startswith(('http://', 'https://')): erro(f"URL inválida {x['url']}")
    k = x['url'].rstrip('/').lower()
    if k in vistos[x['area']]: erro(f"duplicado em {x['area']}: {x['url']}")
    vistos[x['area']].add(k)
    if len(x['descricao'].strip()) < 12: erro(f"link sem descrição: {x['nome']} ({x['area']})")
    if x['url'].count('(') != x['url'].count(')'): erro(f"URL com parênteses desbalanceados: {x['url']}")
    if re.search(r'[<>\\]|\]\(|href=', x['nome']): erro(f"nome com resto de markup: {x['nome']}")
    if re.search(r'\]\[|\]\(', x['descricao']): erro(f"descrição com resto de markdown: {x['descricao'][:60]}")
for a in areas:
    if not vistos[a]: erro(f'área sem links: {a}')
    pag = J('areas', areas[a], a + '.md')
    if a != 'linguagens' and os.path.exists(pag) and len(re.findall(r'^## ', open(pag, encoding='utf-8').read(), re.M)) > 25:
        erro(f'página de área com seções demais (>25): {a}')
    if not os.path.exists(J('areas', areas[a], a + '.md')): erro(f'página faltando: {a}')
ia_por_area = collections.Counter(x['area'] for x in links if x.get('ia'))
for a in areas:
    if ia_por_area[a] < 7: erro(f'área com seção de IA pequena demais (<7): {a} ({ia_por_area[a]})')
if not os.path.exists(J('ia', 'README.md')): erro('página central de IA faltando: ia/README.md')
total = len(links)
if not 10000 <= total <= 20000: erro(f'total fora da meta 10.000–20.000: {total}')

# repositórios de IA por profissão: exatamente 1000 por trilha, sem repetição, todos com descrição
REPOS_POR_TRILHA = 1000
trilhas = [t['slug'] for t in json.load(open(J('data', 'trilhas.json'), encoding='utf-8'))['trilhas']]
repos = collections.defaultdict(list)
if os.path.exists(J('data', 'repos-ia.jsonl')):
    for l in open(J('data', 'repos-ia.jsonl'), encoding='utf-8'):
        r = json.loads(l); repos[r['trilha']].append(r)
for t in trilhas:
    rs = repos.get(t, [])
    if len(rs) != REPOS_POR_TRILHA: erro(f'trilha {t}: {len(rs)} repositórios de IA (esperado {REPOS_POR_TRILHA})')
    if len({r['url'].lower() for r in rs}) != len(rs): erro(f'trilha {t}: repositório de IA repetido')
    for r in rs:
        if len(r['descricao'].strip()) < 15: erro(f"trilha {t}: repositório sem descrição {r['nome']}")
        if not r['url'].startswith('https://github.com/'): erro(f"trilha {t}: URL inesperada {r['url']}")

# idiomas: textos da interface completos e o mesmo conjunto de páginas em todos
pt = textos_pt()
for lang in CODIGOS:
    if lang != 'pt':
        for e in problemas(lang, pt): erro(e)
logicas = ['README.md', 'areas/CATALOGO.md', 'trilhas/README.md', 'ia/README.md', 'ia/profissoes/README.md']
logicas += [f'areas/{s}/README.md' for s in {v for v in areas.values()}] + [f'areas/{s}/{a}.md' for a, s in areas.items()]
logicas += [f'ia/profissoes/{t}.md' for t in trilhas]
geradas = set()
for lang in CODIGOS:
    for pag in logicas:
        real = Ctx.p_de(lang, pag)
        geradas.add(J(real))
        if not os.path.exists(J(real)): erro(f'página faltando em {lang}: {real}')

def anchors(md):
    usados, res = set(), set()
    for m in re.finditer(r'^#{1,6}\s+(.*)$', md, re.M):
        t = m.group(1).strip().lower()
        t = ''.join(c for c in t if c in ' -_' or unicodedata.category(c)[0] in 'LMN' or unicodedata.category(c) == 'Pc').replace(' ', '-')
        b, n = t, 1
        while t in usados: t = f'{b}-{n}'; n += 1
        usados.add(t); res.add(t)
    return res

paginas = [os.path.join(r, f) for r, _, fs in os.walk(RAIZ) if '/.' not in r and '/.cache' not in r for f in fs if f.endswith('.md')]
cache = {}
for p in paginas:
    md = open(p, encoding='utf-8').read()
    cache[p] = (md, anchors(md))
for p in geradas:   # toda seção das páginas geradas começa com uma descrição (> ...)
    if p not in cache: continue
    linhas = cache[p][0].split('\n')
    for i, l in enumerate(linhas):
        if l.startswith('## '):
            prox = next((x for x in linhas[i + 1:i + 4] if x.strip()), '')
            if not prox.startswith('> '): erro(f'{os.path.relpath(p, RAIZ)}: seção sem descrição: {l[3:40]}')
internos = 0
for p, (md, anc) in cache.items():
    sem_codigo = re.sub(r'```.*?```', '', re.sub(r'`[^`\n]*`', '', md), flags=re.S)
    for m in re.finditer(r'\]\(([^)\s]+)\)', sem_codigo):
        alvo = m.group(1)
        if alvo.startswith(('http://', 'https://', 'mailto:')): continue
        internos += 1
        caminho, _, frag = alvo.partition('#')
        dest = os.path.normpath(os.path.join(os.path.dirname(p), caminho)) if caminho else p
        if not os.path.exists(dest):
            erro(f'{os.path.relpath(p, RAIZ)}: link interno quebrado {alvo}'); continue
        if frag and dest.endswith('.md'):
            if dest not in cache:
                cache[dest] = (open(dest, encoding='utf-8').read(), None); cache[dest] = (cache[dest][0], anchors(cache[dest][0]))
            if frag not in cache[dest][1]:
                erro(f'{os.path.relpath(p, RAIZ)}: âncora inexistente #{frag} em {os.path.relpath(dest, RAIZ)}')

if erros:
    print(f'{len(erros)} problema(s):'); [print(' -', e) for e in erros[:50]]
    sys.exit(1)
print(f'OK: {total} links, {sum(len(v) for v in repos.values())} repositórios de IA em {len(trilhas)} profissões, {len(areas)} áreas, '
      f'{len(CODIGOS)} idiomas, {len(paginas)} páginas, {internos} links internos conferidos.')
