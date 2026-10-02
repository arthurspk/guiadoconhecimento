#!/usr/bin/env python3
"""Coleta os links das fontes curadas (listas awesome e afins) listadas em data/fontes.json.

Para cada fonte baixa os arquivos markdown/rst indicados e extrai cada item de lista com
nome, URL, descrição e o tópico (o cabeçalho sob o qual o item aparece).

Download: Scrapling (Fetcher) em raw.githubusercontent.com; se o Scrapling não estiver
instalado ou falhar, cai para `git` (clone raso, sem checkout, lendo só os arquivos pedidos).

Uso:
    python3 scripts/coletar.py                 # todas as fontes
    python3 scripts/coletar.py --area seo      # só uma área
    python3 scripts/coletar.py --sem-scrapling # força o git
Saída: data/brutos.jsonl.gz (um item por linha, versionado para o selecionar.py rodar num clone novo).
"""
import argparse, concurrent.futures as cf, gzip, json, os, re, subprocess, sys, time
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(RAIZ, '.cache', 'fontes')
os.makedirs(CACHE, exist_ok=True)

# ---------------- download ----------------
try:
    from scrapling.fetchers import Fetcher  # type: ignore
    import logging
    logging.getLogger('scrapling').setLevel(logging.ERROR)
except Exception:  # Scrapling é opcional
    Fetcher = None

def baixar_scrapling(repo, arquivo):
    url = f'https://raw.githubusercontent.com/{repo}/HEAD/{arquivo}'
    p = Fetcher.get(url, timeout=30, retries=2)
    if p.status != 200:
        raise RuntimeError(f'HTTP {p.status}')
    body = p.body
    return body.decode('utf-8', 'replace') if isinstance(body, bytes) else str(body)

def baixar_git(repo, arquivo):
    d = os.path.join(CACHE, repo.replace('/', '__'))
    if not os.path.isdir(d):
        subprocess.run(['git', 'clone', '-q', '--depth', '1', '--filter=blob:none', '--no-checkout',
                        f'https://github.com/{repo}', d], check=True, timeout=300,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    r = subprocess.run(['git', '-C', d, 'show', f'HEAD:{arquivo}'], capture_output=True, timeout=300)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode()[:200])
    return r.stdout.decode('utf-8', 'replace')

def baixar(repo, arquivo, usar_scrapling):
    cache = os.path.join(CACHE, 'raw', repo.replace('/', '__'), arquivo)
    if os.path.exists(cache):
        return open(cache, encoding='utf-8').read(), 'cache'
    erros = []
    metodos = ([('scrapling', baixar_scrapling)] if (usar_scrapling and Fetcher) else []) + [('git', baixar_git)]
    for nome, fn in metodos:
        try:
            txt = fn(repo, arquivo)
            os.makedirs(os.path.dirname(cache), exist_ok=True)
            open(cache, 'w', encoding='utf-8').write(txt)
            return txt, nome
        except Exception as e:  # tenta o próximo método
            erros.append(f'{nome}: {e}')
    raise RuntimeError('; '.join(erros))

# ---------------- parser ----------------
SECOES_IGNORADAS = re.compile(r'^(contribut\w*|license|licen[cç]a|'
                              r'footnotes|sponsors?|patrocinadores|backers|credits|créditos|acknowledg\w*|related( lists)?|'
                              r'awesome lists?|code of conduct|how to (contribute|use)|navega[cç][aã]o|meta|star history|'
                              r'support|doa[cç][oõ]es|donat\w*|e-book|authors?|maintainers?)$', re.I)
RE_HEAD = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')
RE_HTML_HEAD = re.compile(r'<h([1-6])[^>]*>(.*?)</h\1>', re.I)
RE_ITEM = re.compile(r'^\s*(?:[-*+]|\d+[.)])\s+(.*)$')
RE_MDLINK = re.compile(r'(?<!!)\[((?:[^\[\]]|\[[^\]]*\])+)\]\((<?https?://(?:[^()\s>]|\([^()\s]*\))+>?)(?:\s+"[^"]*")?\)')
RE_REFLINK = re.compile(r'(?<!!)\[([^\]]+)\]\[([^\]]*)\]')
RE_REFDEF = re.compile(r'^\s*\[([^\]]+)\]:\s*<?(https?://\S+?)>?(?:\s+"[^"]*")?\s*$')
RE_AHREF = re.compile(r'<a\s+[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', re.I | re.S)
RE_RST = re.compile(r'`([^`<]+?)\s*<(https?://[^>]+)>`_{1,2}')
RE_RAW = re.compile(r'(https?://[^\s<>)\]"\'`]+)')
RE_TAGS = re.compile(r'<[^>]+>')
RE_LINHA_CRUA = re.compile(r'^[^:\[\]()]{2,80}:\s*https?://\S+\s*$')
RE_IMG = re.compile(r'!\[[^\]]*\]\([^)]*\)')
RE_EMOJI = re.compile('[\U0001F000-\U0001FAFF☀-➿️‍]|:[a-z0-9_+-]+:')

URL_RUIM = re.compile(r'(shields\.io|badge|travis-ci|circleci\.com/gh|codecov\.io|twitter\.com/intent|'
                      r'facebook\.com/sharer|\.(png|jpe?g|gif|svg|webp)(\?|$)|github\.com/[^/]+/[^/]+/(blob|tree)/[^/]+/'
                      r'(CONTRIBUTING|LICENSE|CODE_OF_CONDUCT)|creativecommons\.org/(licenses|publicdomain)|'
                      r'github\.com/sindresorhus/awesome/?$|awesome\.re|opensource\.org/licenses|'
                      r'github\.com/[^/]+/[^/]+/(issues|pulls|graphs|stargazers|network|fork|compare)\b)', re.I)

def limpar(txt):
    txt = RE_IMG.sub('', txt)
    txt = RE_TAGS.sub('', txt)
    txt = RE_EMOJI.sub('', txt)
    txt = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', txt)
    txt = re.sub(r'\\([\\`*_{}\[\]()#+\-.!|])', r'\1', txt)          # escapes de markdown: \_ \- \!
    txt = re.sub(r'[*`]{1,3}', '', txt)
    txt = re.sub(r'(?<![\w])_{1,3}|_{1,3}(?![\w])', '', txt)        # _ênfase_, mas preserva nome_com_underscore
    return re.sub(r'\s+', ' ', txt).strip()

def limpar_desc(txt):
    txt = re.sub(r'\[!\[[^\]]*\](?:\[[^\]]*\]|\([^)]*\))\]\([^)]*\)', '', txt)   # [![ícone][ref]](url)
    txt = re.sub(r'!\[[^\]]*\](?:\[[^\]]*\]|\([^)]*\))', '', txt)                  # ![ícone][ref] / ![img](url)
    txt = re.sub(r'\[\[([^\]]*)\]\]\([^)]*\)', '', txt)                              # [[more info]](url)
    txt = limpar(txt)
    txt = re.sub(r'\]\([^)]*\)|\]\[[^\]]*\]', '', txt)                               # restos ](url) e ][ref]
    txt = re.sub(r'\s*!\s*$|\s+!\s+', ' ', txt)
    txt = re.sub(r'^[\s\-–—:|•·]+', '', txt)
    txt = re.sub(r'\s*\|\s*$', '', txt)
    txt = re.sub(r'\[[^\]]*\]\[[^\]]*\]', '', txt)                   # [MIT][MIT]
    txt = re.sub(r'\((?:⭐|★)[^)]*\)', '', txt).strip()                # (⭐ 110 · updated 2025-09)
    if len(txt) > 300:
        txt = txt[:297].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    return txt.strip()

def normalizar_url(u):
    u = u.strip().strip('<>').rstrip('.,;')
    s = urlsplit(u)
    afiliado = ('utm_', 'ref', 'fbclid', 'gclid', 'aff', 'affiliate', 'partner')
    q = [(k, v) for k, v in parse_qsl(s.query) if not k.lower().startswith(afiliado)
         and not (k.lower() in ('tag', 'linkcode', 'camp', 'creative') and 'amazon.' in s.netloc.lower())]
    path = s.path or '/'
    return urlunsplit((s.scheme.lower(), s.netloc.lower(), path, urlencode(q), ''))

def chave_url(u):
    s = urlsplit(u)
    host = s.netloc.lower()
    host = host[4:] if host.startswith('www.') else host
    path = s.path.rstrip('/').lower() or ''
    if host == 'github.com':
        path = '/'.join(path.split('/')[:3])  # dono/repo
    return host + path + (('?' + s.query) if s.query and host in ('youtube.com', 'm.youtube.com') else '')

def extrair(texto, fonte):
    """Devolve itens {nome,url,descricao,topico,subtopico} de um markdown/rst."""
    linhas = texto.splitlines()
    refs = {}
    for ln in linhas:
        m = RE_REFDEF.match(ln)
        if m:
            refs[m.group(1).lower()] = m.group(2)
    itens, h2, h3, ignorar, nivel_ign = [], '', '', False, 9
    em_codigo = False
    rst_prev = ''
    for i, ln in enumerate(linhas):
        if ln.strip().startswith('```'):
            em_codigo = not em_codigo
            continue
        if em_codigo:
            continue
        # cabeçalhos rst (texto sublinhado com === ou ---)
        if fonte.get('_rst') and re.match(r'^[=\-~^]{3,}\s*$', ln) and rst_prev.strip():
            nivel = {'=': 2, '-': 3, '~': 4, '^': 4}[ln.strip()[0]]
            titulo = limpar(rst_prev)
            if nivel <= 2: h2, h3 = titulo, ''
            else: h3 = titulo
            ignorar = bool(SECOES_IGNORADAS.match(titulo))
            rst_prev = ln
            continue
        rst_prev = ln
        m = RE_HEAD.match(ln) or None
        if not m:
            mh = RE_HTML_HEAD.search(ln)
            if mh and ln.strip().startswith('<h'):
                m = ('#' * int(mh.group(1)), mh.group(2))
        if m:
            nivel = len(m[0]) if isinstance(m, tuple) else len(m.group(1))
            titulo = limpar(m[1] if isinstance(m, tuple) else m.group(2))
            if nivel <= 1:
                continue
            if ignorar and nivel > nivel_ign:
                continue
            ignorar = bool(SECOES_IGNORADAS.match(titulo))
            nivel_ign = nivel
            if nivel == 2: h2, h3 = titulo, ''
            else: h3 = titulo
            continue
        if ignorar:
            continue
        mi = RE_ITEM.match(ln)
        st = ln.lstrip()
        if mi:
            corpo = mi.group(1)
        elif st.startswith('|'):
            corpo = ln
        elif st.startswith('>') and '](http' in st:            # > **[nome](url)** ... <br>descrição
            corpo = st.lstrip('> ').replace('<br>', ' - ')
        elif st.startswith('[') and '](http' in st:            # [**nome**](url) \  (listas em blocos)
            corpo = st.rstrip('\\ ')
        elif st.startswith(('&nbsp;', '<a href', '<p><a href')) and 'href="http' in st:   # <a href=...>nome</a> - descrição
            corpo = st.replace('&nbsp;', ' ').strip()
        elif '](http' in st and '|' in st:                        # tabela sem | inicial
            corpo = '|' + st.split('|', 1)[1] if not st.startswith('[') else st
        elif RE_LINHA_CRUA.match(st):                          # Nome: https://...
            corpo = st
        else:
            continue
        corpo = re.sub(r'<kbd>.*?</kbd>', '', corpo)
        achou = None
        for mm in RE_MDLINK.finditer(corpo):
            if mm.group(1).lstrip().startswith('!['):  # selo/ícone antes do nome: pula para o próximo link
                continue
            achou = (limpar(mm.group(1)), mm.group(2), corpo[mm.end():]); break
        if not achou:
            mm = RE_REFLINK.search(corpo)
            if mm:
                u = refs.get((mm.group(2) or mm.group(1)).lower())
                if u: achou = (limpar(mm.group(1)), u, corpo[mm.end():])
        if not achou:
            mm = re.match(r'\s*\[([^\]]+)\](?![\[(])', corpo)  # referência curta: [Nome] + [Nome]: url
            if mm and mm.group(1).lower() in refs:
                achou = (limpar(mm.group(1)), refs[mm.group(1).lower()], corpo[mm.end():])
        if not achou:
            mm = RE_AHREF.search(corpo)
            if mm: achou = (limpar(mm.group(2)), mm.group(1), RE_TAGS.sub('', corpo[mm.end():]))
        if not achou:
            mm = RE_RST.search(corpo)
            if mm: achou = (limpar(mm.group(1)), mm.group(2), corpo[mm.end():])
        if not achou:
            mm = RE_RAW.search(corpo)
            if mm:
                antes = limpar(corpo[:mm.start()]).rstrip(' :-–—')
                achou = (antes or mm.group(1), mm.group(1), corpo[mm.end():])
        if not achou:
            continue
        nome, url, resto = achou
        if corpo.lstrip().startswith('|'):
            cols = [c.strip() for c in corpo.strip().strip('|').split('|')]
            resto = next((c for c in cols[1:] if c and 'http' not in c and len(c) > 8), '')
        url = normalizar_url(url)
        if URL_RUIM.search(url) or not nome or len(nome) > 120:
            continue
        if f"github.com/{fonte['repo'].lower()}" in url.lower():
            continue
        itens.append({'nome': nome, 'url': url, 'descricao': limpar_desc(resto),
                      'topico': h2 or 'Geral', 'subtopico': h3})
    return itens

# ---------------- principal ----------------
def processar(fonte, usar_scrapling):
    out, metodos = [], set()
    for arq in fonte['arquivos']:
        txt, metodo = baixar(fonte['repo'], arq, usar_scrapling)
        metodos.add(metodo)
        f2 = dict(fonte, _rst=arq.lower().endswith('.rst'))
        mapa = [(re.compile(rx, re.I), ar) for rx, ar in fonte.get('mapa', [])]
        for it in extrair(txt, f2):
            it['topico'] = re.sub(r'^Sites e cursos para aprender\s+', '', it['topico']).rstrip(' :')
            area = fonte['area']
            if mapa:  # fonte que cobre várias áreas: o cabeçalho decide a área
                orig = it['topico']
                sub = it.get('subtopico') or ''
                area = next((ar for rx, ar in mapa if sub and rx.search(sub)), None) or \
                       next((ar for rx, ar in mapa if rx.search(orig) or rx.search('Sites e cursos para aprender ' + orig)), None)
                if not area:
                    continue
            it.update(area=area, fonte=fonte['repo'], arquivo=arq, licenca=fonte.get('licenca', 'sem-licenca'), ia=bool(fonte.get('ia')))
            out.append(it)
    return out, metodos

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--area', help='recoleta só esta área e mescla com o resto da base')
    ap.add_argument('--sem-scrapling', action='store_true')
    ap.add_argument('--workers', type=int, default=12)
    a = ap.parse_args()
    fontes = json.load(open(os.path.join(RAIZ, 'data', 'fontes.json'), encoding='utf-8'))
    extras = os.path.join(RAIZ, 'data', 'fontes-guias.json')
    if os.path.exists(extras):
        fontes += json.load(open(extras, encoding='utf-8'))
    if a.area:  # fontes "_mapa" cobrem várias áreas: entram sempre, e os itens são filtrados pela área
        fontes = [f for f in fontes if f['area'] in (a.area, '_mapa')]
    t0 = time.time(); falhas = []; usos = {}; resultados = {}
    with cf.ThreadPoolExecutor(a.workers) as ex:
        futs = {ex.submit(processar, f, not a.sem_scrapling): i for i, f in enumerate(fontes)}
        for fut in cf.as_completed(futs):
            i = futs[fut]; f = fontes[i]
            try:
                itens, metodos = fut.result()
            except Exception as e:
                falhas.append(f"{f['repo']} ({f['area']}): {str(e)[:160]}"); continue
            for m in metodos: usos[m] = usos.get(m, 0) + 1
            resultados[i] = [it for it in itens if not a.area or it['area'] == a.area]
    novos = [it for i in sorted(resultados) for it in resultados[i]]  # ordem de fontes.json: saída determinística
    caminho = os.path.join(RAIZ, 'data', 'brutos.jsonl.gz')
    if a.area and os.path.exists(caminho):
        antigos = [json.loads(l) for l in gzip.open(caminho, 'rt', encoding='utf-8')]
        novos = [it for it in antigos if it['area'] != a.area] + novos
    with gzip.GzipFile(caminho, 'wb', mtime=0) as gz:
        for it in novos:
            gz.write((json.dumps(it, ensure_ascii=False) + '\n').encode('utf-8'))
    print(f'{len(fontes)} fontes, {sum(len(v) for v in resultados.values())} itens coletados em {time.time()-t0:.0f}s '
          f'(base bruta: {len(novos)}); métodos: {usos}')
    for x in falhas:
        print('FALHA', x)
    return 1 if len(falhas) > len(fontes) * 0.1 else 0

if __name__ == '__main__':
    sys.exit(main())
