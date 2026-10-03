#!/usr/bin/env python3
"""Transforma data/brutos.jsonl.gz na base final data/links.jsonl.

Etapas: normaliza URLs, descarta itens ruins, define o tópico, classifica tipo e idioma,
remove duplicados dentro de cada área, aplica a política de licenças das descrições e
seleciona os itens de cada área com teto e rodízio entre fontes (diversidade).
Os essenciais (data/essenciais.json) entram sempre e primeiro.

Uso: python3 scripts/selecionar.py [--teto 200] [--teto-grande 300] [--teto-linguagens 1500]
"""
import argparse, collections, gzip, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coletar import normalizar_url
from urllib.parse import urlsplit

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(RAIZ, 'data', *p)

AREAS_GRANDES = {'recursos-audiovisuais', 'front-end', 'back-end', 'devops-cloud', 'ia-generativa', 'ciberseguranca', 'apps-sistemas', 'self-hosted',
                 'ferramentas-online', 'ferramentas-ia', 'recursos-gratuitos', 'ciencia-de-dados-ml', 'datasets', 'apis-publicas',
                 'ferramentas-dev', 'mobile', 'sistemas-linux', 'qa-testes'}

LINGUAGEM_DA_FONTE = {
    'vinta/awesome-python': 'Python', 'sorrycc/awesome-javascript': 'JavaScript', 'dzharii/awesome-typescript': 'TypeScript',
    'akullpp/awesome-java': 'Java', 'avelino/awesome-go': 'Go', 'rust-unofficial/awesome-rust': 'Rust', 'fffaraz/awesome-cpp': 'C++',
    'oz123/awesome-c': 'C', 'quozd/awesome-dotnet': 'C# e .NET', 'ziadoz/awesome-php': 'PHP', 'mcxiaoke/awesome-kotlin': 'Kotlin',
    'matteocrippa/awesome-swift': 'Swift', 'markets/awesome-ruby': 'Ruby', 'h4cc/awesome-elixir': 'Elixir', 'yissachar/awesome-dart': 'Dart',
    'EbookFoundation/free-programming-books': 'Livros e cursos gratuitos em português'}
NOME_LINGUAGEM = {'c#': 'C# e .NET', 'golang': 'Go', 'go': 'Go'}

TRAD = {  # tópicos comuns traduzidos; o resto mantém o nome da lista de origem
    'tools': 'Ferramentas', 'tooling': 'Ferramentas', 'books': 'Livros', 'courses': 'Cursos', 'online courses': 'Cursos online',
    'tutorials': 'Tutoriais', 'articles': 'Artigos', 'videos': 'Vídeos', 'video': 'Vídeos', 'podcasts': 'Podcasts',
    'communities': 'Comunidades', 'community': 'Comunidade', 'libraries': 'Bibliotecas', 'libs': 'Bibliotecas',
    'frameworks': 'Frameworks', 'resources': 'Recursos', 'blogs': 'Blogs', 'newsletters': 'Newsletters', 'learning': 'Aprendizado',
    'learning resources': 'Recursos de aprendizado', 'documentation': 'Documentação', 'websites': 'Sites', 'apps': 'Aplicativos',
    'applications': 'Aplicativos', 'games': 'Jogos', 'testing': 'Testes', 'security': 'Segurança', 'miscellaneous': 'Diversos',
    'misc': 'Diversos', 'other': 'Outros', 'others': 'Outros', 'utilities': 'Utilitários', 'extensions': 'Extensões',
    'templates': 'Templates', 'icons': 'Ícones', 'fonts': 'Fontes', 'people': 'Pessoas', 'companies': 'Empresas', 'youtube': 'YouTube',
    'youtube channels': 'Canais do YouTube', 'channels': 'Canais', 'cheatsheets': 'Cheatsheets', 'cheat sheets': 'Cheatsheets',
    'guides': 'Guias', 'papers': 'Artigos científicos', 'research papers': 'Artigos científicos', 'datasets': 'Datasets',
    'data': 'Dados', 'database': 'Banco de dados', 'databases': 'Bancos de dados', 'education': 'Educação', 'games and fun': 'Jogos',
    'news': 'Notícias', 'conferences': 'Conferências', 'events': 'Eventos', 'jobs': 'Vagas', 'job boards': 'Sites de vagas',
    'productivity': 'Produtividade', 'design': 'Design', 'development': 'Desenvolvimento', 'developer tools': 'Ferramentas de desenvolvimento',
    'development tools': 'Ferramentas de desenvolvimento', 'networking': 'Redes', 'monitoring': 'Monitoramento', 'logging': 'Logs',
    'editors': 'Editores', 'text editors': 'Editores de texto', 'plugins': 'Plugins', 'software': 'Software', 'services': 'Serviços',
    'platforms': 'Plataformas', 'general': 'Geral', 'getting started': 'Primeiros passos', 'basics': 'Fundamentos',
    'interactive learning': 'Aprendizado interativo', 'free courses': 'Cursos gratuitos', 'mobile': 'Mobile', 'audio': 'Áudio',
    'music': 'Música', 'images': 'Imagens', 'photos': 'Fotos', 'stock photos': 'Bancos de imagens', 'illustrations': 'Ilustrações',
    'colors': 'Cores', 'color': 'Cores', 'typography': 'Tipografia', 'inspiration': 'Inspiração', 'marketplaces': 'Marketplaces',
    'analytics': 'Analytics', 'email': 'E-mail', 'email marketing': 'E-mail marketing', 'social media': 'Redes sociais',
    'writing': 'Escrita', 'research': 'Pesquisa', 'statistics': 'Estatística', 'mathematics': 'Matemática', 'physics': 'Física',
    'chemistry': 'Química', 'biology': 'Biologia', 'history': 'História', 'philosophy': 'Filosofia', 'economics': 'Economia',
    'finance': 'Finanças', 'accounting': 'Contabilidade', 'legal': 'Jurídico', 'health': 'Saúde', 'medicine': 'Medicina',
    'psychology': 'Psicologia', 'languages': 'Idiomas', 'apis': 'APIs', 'api': 'API', 'automation': 'Automação',
    'cloud': 'Cloud', 'hosting': 'Hospedagem', 'deployment': 'Deploy', 'authentication': 'Autenticação', 'payments': 'Pagamentos',
    'e-commerce': 'E-commerce', 'ecommerce': 'E-commerce', 'seo': 'SEO', 'marketing': 'Marketing', 'sales': 'Vendas',
    'project management': 'Gestão de projetos', 'communication': 'Comunicação', 'collaboration': 'Colaboração',
    'note taking': 'Notas', 'notes': 'Notas', 'task management': 'Tarefas', 'file sharing': 'Compartilhamento de arquivos',
    'media streaming': 'Streaming de mídia', 'backup': 'Backup', 'privacy': 'Privacidade', 'browsers': 'Navegadores',
    'browser extensions': 'Extensões de navegador', 'terminal': 'Terminal', 'shell': 'Shell', 'command line': 'Linha de comando',
    'cli': 'Linha de comando', 'blender': 'Blender', 'tutorials and courses': 'Tutoriais e cursos', 'communities and forums': 'Comunidades e fóruns',
    'forums': 'Fóruns', 'magazines': 'Revistas', 'newsletter': 'Newsletter', 'organizations': 'Organizações', 'awesome lists': 'Listas awesome',
    'related lists': 'Listas relacionadas', 'related': 'Relacionados', 'free': 'Gratuitos', 'open source': 'Open source',
}
WRAPPERS = re.compile(r'^(index|contents?|table of contents|geral|all categories|chapters?|the book of secret knowledge.*|'
                      r'[–\-\s]*apps?[–\-\s]*|\d{4}|awesome .*|list|lista|categories|categorias|sections?|summary|overview)$', re.I)
NOMES_RUINS = re.compile(r'^(\(?paper\)?|\(?pdf\)?|project page|code|arxiv|official introductory video|video demo|github repo|link|here|aqui|website|site|source|\[?source\]?|demo|github|homepage|home|docs?|download|'
                         r'official|official site|read more|more|video|playlist|pdf|book|website link|url|\d+)$', re.I)
FRAGMENTO = re.compile(r'^(?:or|and|by|see|via|also|ou|e|&)\b|^(?i:great list|thanks)')
RE_IA = re.compile(r'\b(AI|IA|A\.I\.|GPT-?\d*|LLMs?|ChatGPT|Claude|Gemini|Copilot|OpenAI|Anthropic|Midjourney|Stable Diffusion|'
                   r'generative|gen ?AI|machine learning|deep learning|neural|inteligência artificial|AI-powered|agentes? de IA|MCP)\b')
AREAS_SO_IA = {'ia-generativa', 'ferramentas-ia'}  # a página inteira já é de IA: só os essenciais de IA
PT = re.compile(r'(ção|ções|ões\b| você | não | é | para o | para a | uma | com o | sobre o | aprenda | gratuito| em português)', re.I)

def chave(u):
    s = urlsplit(u)
    h = s.netloc.lower()
    h = h[4:] if h.startswith('www.') else h
    p = s.path.rstrip('/').lower()
    if h == 'github.com':
        p = '/'.join(p.split('/')[:3]) if p.count('/') <= 2 or '/blob/' not in p and '/tree/' not in p else p
    q = ('?' + s.query) if s.query and ('youtube' in h or 'watch' in p) else ''
    return h + p + q

def tipo(u, nome):
    s = urlsplit(u); h = s.netloc.lower().replace('www.', ''); p = s.path.lower()
    if h == 'github.com' and p.count('/') >= 2:
        return 'awesome' if 'awesome' in p or 'awesome' in nome.lower() else 'repositorio'
    if h in ('youtube.com', 'm.youtube.com', 'youtu.be'):
        return 'canal' if re.match(r'^/(c/|channel/|user/|@)', p) else 'video'
    if re.search(r'(coursera|edx|udemy|udacity|khanacademy|alura|freecodecamp|codecademy|dio\.me|fundacao-bradesco|cursoemvideo|mooc)', h):
        return 'curso'
    if re.search(r'(discord\.(gg|com)|reddit\.com|t\.me|telegram|slack\.com|meetup\.com|forum)', h + p):
        return 'comunidade'
    if 'arxiv.org' in h or re.search(r'(doi\.org|aclanthology|openreview\.net|semanticscholar)', h):
        return 'artigo'
    if re.search(r'(amazon\.|goodreads|oreilly\.com/library|leanpub)', h + p):
        return 'livro'
    if re.search(r'(apps\.apple|play\.google|chrome\.google\.com/webstore|chromewebstore|addons\.mozilla|f-droid)', h + p):
        return 'app'
    if re.search(r'(^docs\.|/docs?/|developer\.|developers\.)', h + p):
        return 'documentacao'
    return 'site'

def idioma(it):
    h = urlsplit(it['url']).netloc.lower()
    if h.endswith('.br') or 'pt_BR' in it.get('arquivo', '') or PT.search(' ' + it.get('descricao', '') + ' '):
        return 'pt'
    return ''

def limpa_topico(t):
    t = re.sub(r'\(\d+\)|\[\d+\]|\d+ projects?', '', t or '')
    t = re.sub(r'[^\w\s&/.,+#()\'-]', '', t).strip(' -–—:^|')
    t = re.sub(r'^\([A-Z]{1,3}\)\s*', '', t)                 # "(QA) Mathematics" -> "Mathematics"
    if t.isupper() and len(t) > 3:
        t = t.capitalize()
    t = re.sub(r'\s+', ' ', t)
    return TRAD.get(t.lower(), t) or 'Geral'

BLOCO_TOPICO = 6

def intercalar(itens):
    """Rodízio entre tópicos (para cobrir a lista inteira, não só o começo), com descrição primeiro."""
    out = []
    for passo in (lambda x: len(x['descricao']) >= 12, lambda x: len(x['descricao']) < 12):
        por_top = collections.OrderedDict()
        for x in itens:
            if passo(x): por_top.setdefault(x['topico'], collections.deque()).append(x)
        while por_top:
            for t in list(por_top):
                for _ in range(BLOCO_TOPICO):  # pega até 3 por tópico a cada volta, para o tópico render uma seção
                    if por_top[t]: out.append(por_top[t].popleft())
                if not por_top[t]: del por_top[t]
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--teto', type=int, default=170)
    ap.add_argument('--teto-grande', type=int, default=260)
    ap.add_argument('--teto-linguagens', type=int, default=1300)
    ap.add_argument('--teto-ia', type=int, default=30, help='links de IA coletados por área, além dos essenciais de IA')
    a = ap.parse_args()

    tax = json.load(open(D('taxonomia.json'), encoding='utf-8'))
    areas = [ar['slug'] for s in tax['setores'] for ar in s['areas']]
    brutos = [json.loads(l) for l in gzip.open(D('brutos.jsonl.gz'), 'rt', encoding='utf-8')]
    fontes_cfg = json.load(open(D('fontes.json'), encoding='utf-8')) + json.load(open(D('fontes-guias.json'), encoding='utf-8'))
    validas = {(f['repo'], f['area']) for f in fontes_cfg}
    excluir = {(f['repo'], f['area']): re.compile(f['excluir_topicos'], re.I) for f in fontes_cfg if f.get('excluir_topicos')}
    essenciais = json.load(open(D('essenciais.json'), encoding='utf-8'))
    # descrições próprias dos projetos (scripts/descrever.py), para links cuja lista de origem não pode ser citada
    descricoes = json.load(open(D('descricoes.json'), encoding='utf-8')) if os.path.exists(D('descricoes.json')) else {}
    st = D('status-links.json')
    quebrados = set()
    if os.path.exists(st):  # gerado por checar_links.py: fora os links que falharam 2 vezes seguidas
        quebrados = {u for u, v in json.load(open(st, encoding='utf-8')).items() if v.get('status') != 'ok' and v.get('falhas', 0) >= 2}

    # tópico efetivo: se o H2 é só um "invólucro" com vários H3, o H3 vira o tópico
    h3_por_h2 = collections.defaultdict(set)
    for it in brutos:
        if it['subtopico']:
            h3_por_h2[(it['fonte'], it['arquivo'], it['topico'])].add(it['subtopico'])
    stats = collections.Counter()
    por_area = collections.defaultdict(lambda: collections.defaultdict(list))  # area -> fonte -> itens
    for it in brutos:
        stats['brutos'] += 1
        if (it['fonte'], it['area']) not in validas and (it['fonte'], '_mapa') not in validas:
            stats['fonte_removida'] += 1; continue
        rx = excluir.get((it['fonte'], it['area']))
        if rx and (rx.search(it['topico'] or '') or rx.search(it['subtopico'] or '')):
            stats['topico_excluido'] += 1; continue
        it['url'] = normalizar_url(it['url'])
        u = it['url']
        if u in quebrados:
            stats['quebrado_removido'] += 1; continue
        if not u.startswith(('http://', 'https://')) or len(u) > 400:
            stats['url_invalida'] += 1; continue
        nome = html.unescape(re.sub(r'<[^>]*>?|"?>', '', it['nome'])).strip(' -–—:*')
        if nome.count('"') % 2:
            nome = nome.replace('"', '')
        if '](' in nome:
            nome = re.sub(r'^\[?([^\]]*)\]\(.*$', r'\1', nome).strip()
        if nome.startswith(('http://', 'https://')):
            nome = re.sub(r'^https?://(www\.)?', '', nome).rstrip('/')
        if 'href' in nome or '="' in nome or not re.search(r'\w', nome):
            stats['nome_ruim'] += 1; continue
        if NOMES_RUINS.match(nome) or len(nome) < 2 or '![' in nome or nome.startswith('!') or 'randomrepoimg' in u:
            stats['nome_ruim'] += 1; continue
        h2, h3 = it['topico'], it['subtopico']
        usa_h3 = h3 and (WRAPPERS.match(h2 or '') or len(h3_por_h2[(it['fonte'], it['arquivo'], h2)]) >= 3)
        topico = limpa_topico(h3 if usa_h3 else h2)
        if WRAPPERS.match(topico):
            topico = 'Geral'
        desc = html.unescape(re.sub(r'<[^>]*>', '', it['descricao']))
        desc = re.sub(r'^[\s)\]\-–—:|,.]+', '', desc).strip()
        if desc.lower() == nome.lower() or FRAGMENTO.match(desc): desc = ''
        lic = it.get('licenca', '')
        if lic in ('sem-licenca',) or lic.startswith(('CC-BY-NC', 'GPL')):
            desc = ''  # sem licença compatível: o texto da lista não é copiado
            stats['desc_omitida_licenca'] += 1
        if ' | ' in desc:
            desc = ''  # resto de tabela, não é descrição
        if len(desc) < 12 and u in descricoes:
            desc = descricoes[u]; stats['desc_do_proprio_projeto'] += 1
        if len(desc) < 12:
            stats['sem_descricao'] += 1; continue  # todo link do guia tem descrição
        grupo = ''
        if it['area'] == 'linguagens':
            grupo = LINGUAGEM_DA_FONTE.get(it['fonte']) or NOME_LINGUAGEM.get(topico.lower(), topico)
        por_area[it['area']][it['fonte']].append({
            'nome': nome[:120], 'url': u, 'descricao': desc, 'topico': topico, 'grupo': grupo,
            'area': it['area'], 'fonte': it['fonte'], 'licenca_fonte': lic, 'tipo': tipo(u, nome),
            'idioma': idioma(it), 'essencial': False,
            'ia_fonte': bool(it.get('ia')), 'ia': bool(it.get('ia')) or bool(RE_IA.search(nome + ' ' + desc))})

    # tópicos equivalentes viram um só por área (Dictionary/Dictionaries, Keyword Research/Keywords Research)
    def chave_topico(t):
        k = re.sub(r'[^a-z0-9áéíóúãõâêôç]', '', t.lower())
        return re.sub(r'(ies|es|s)$', '', k)
    for area, fontes_area in por_area.items():
        nomes = collections.defaultdict(collections.Counter)
        for its in fontes_area.values():
            for x in its: nomes[chave_topico(x['topico'])][x['topico']] += 1
        canon = {k: c.most_common(1)[0][0] for k, c in nomes.items()}
        for its in fontes_area.values():
            for x in its: x['topico'] = canon[chave_topico(x['topico'])]

    saida = []
    for area in areas:
        teto = a.teto_linguagens if area == 'linguagens' else (a.teto_grande if area in AREAS_GRANDES else a.teto)
        vistos = set(); escolhidos = []
        for e in [x for x in essenciais if x['area'] == area]:
            k = chave(e['url'])
            if k in vistos: continue
            vistos.add(k)
            escolhidos.append({'nome': e['nome'], 'url': e['url'], 'descricao': e['descricao'],
                               'topico': 'IA' if e.get('ia') else e.get('topico', 'Comece por aqui'),
                               'grupo': '', 'area': area, 'fonte': 'curadoria', 'licenca_fonte': 'CC-BY-SA-4.0',
                               'tipo': e.get('tipo', 'site'), 'idioma': e.get('idioma', ''), 'gratuito': e.get('gratuito'),
                               'essencial': True, 'ia': bool(e.get('ia'))})
        # IA para a área: listas de IA do domínio + categorias das listas gerais de IA + itens de IA das listas da área
        if area not in AREAS_SO_IA:
            filas_ia = {f: collections.deque(intercalar([x for x in its if x['ia'] and len(x['descricao']) >= 12]))  # IA: só itens com descrição
                        for f, its in por_area.get(area, {}).items()}
            filas_ia = {f: q for f, q in filas_ia.items() if q}
            ordem_ia = sorted(filas_ia, key=lambda f: (not any(x['ia_fonte'] for x in filas_ia[f]), f))
            n_ia = 0
            while n_ia < a.teto_ia and any(filas_ia.values()):
                for f in ordem_ia:
                    q = filas_ia[f]
                    while q:
                        x = q.popleft(); k = chave(x['url'])
                        if k in vistos: continue
                        vistos.add(k); escolhidos.append(dict(x, topico='IA', ia=True)); n_ia += 1; break
                    if n_ia >= a.teto_ia: break
            stats['links_ia_coletados'] += n_ia
        fontes = por_area.get(area, {})
        # filas: com descrição primeiro (mantendo a ordem da lista original), depois sem descrição
        filas = {}
        for f, its in fontes.items():
            normais = [x for x in its if not x['ia_fonte']]
            if normais: filas[f] = collections.deque(intercalar(normais))
        if area == 'linguagens':  # rodízio por linguagem, para todas aparecerem
            grupos = collections.defaultdict(list)
            for f, q in filas.items():
                for x in q: grupos[x['grupo']].append(x)
            filas = {g: collections.deque(intercalar(v)) for g, v in grupos.items()}
        # fontes do autor (arthurspk) e em português na frente do rodízio
        ordem = sorted(filas, key=lambda f: (not f.startswith('arthurspk/'), f))
        teto += len(escolhidos) - sum(1 for x in escolhidos if x['essencial'] and not x['ia'])  # a seção de IA não come o teto
        while len(escolhidos) < teto and any(filas.values()):
            for f in ordem:
                q = filas[f]
                while q:
                    x = q.popleft(); k = chave(x['url'])
                    if k in vistos:
                        stats['duplicado_na_area'] += 1; continue
                    vistos.add(k); escolhidos.append(x); break
                if len(escolhidos) >= teto: break
        stats['cortado_pelo_teto'] += sum(len(q) for q in filas.values())
        for x in escolhidos:
            x.pop('ia_fonte', None)
            x.setdefault('ia', False)
            if x['topico'] != 'IA': x['ia'] = False  # o selo de IA vale para a seção de IA
        saida += escolhidos

    with open(D('links.jsonl'), 'w', encoding='utf-8') as fo:
        for x in saida:
            fo.write(json.dumps(x, ensure_ascii=False) + '\n')
    unicos = len({chave(x['url']) for x in saida})
    print(f"{len(saida)} entradas ({unicos} URLs únicas) em {len(areas)} áreas")
    for k, v in stats.items():
        print(f'  {k}: {v}')

if __name__ == '__main__':
    main()
