#!/usr/bin/env python3
"""Gera o repositório navegável a partir de data/: README.md, areas/, trilhas/,
docs/07-fontes-e-licencas.md e data/links.csv.

Só usa a stdlib. Rodar de novo produz os mesmos arquivos (saída determinística).
Uso: python3 scripts/gerar.py
"""
import collections, csv, json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from selecionar import chave
from urllib.parse import urlsplit

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
CFG = json.load(open(J('data', 'config.json'), encoding='utf-8'))
TAX = json.load(open(J('data', 'taxonomia.json'), encoding='utf-8'))
TRI = json.load(open(J('data', 'trilhas.json'), encoding='utf-8'))['trilhas']
LINKS = [json.loads(l) for l in open(J('data', 'links.jsonl'), encoding='utf-8')]
FONTES = json.load(open(J('data', 'fontes.json'), encoding='utf-8')) + json.load(open(J('data', 'fontes-guias.json'), encoding='utf-8'))

AREA = {a['slug']: dict(a, setor=s['slug']) for s in TAX['setores'] for a in s['areas']}
SETOR = {s['slug']: s for s in TAX['setores']}
POR_AREA = collections.defaultdict(list)
for x in LINKS:
    POR_AREA[x['area']].append(x)
TIPO_ROTULO = {'site': 'site', 'repositorio': 'repositório', 'awesome': 'lista awesome', 'curso': 'curso', 'canal': 'canal',
               'video': 'vídeo', 'livro': 'livro', 'comunidade': 'comunidade', 'documentacao': 'documentação',
               'ferramenta': 'ferramenta', 'app': 'app', 'artigo': 'artigo científico'}
MIN_TOPICO = 6  # tópicos com menos itens vão para "Mais links"
MAX_TOPICOS = 15  # no máximo 15 seções de tópico por página (o resto vai para "Mais links")

def gh_anchor(texto, usados):
    """Âncora no formato do GitHub (emoji some, espaço vira hífen)."""
    t = texto.strip().lower()
    t = ''.join(c for c in t if c in ' -_' or unicodedata.category(c)[0] in 'LMN' or unicodedata.category(c) == 'Pc')
    t = t.replace(' ', '-')
    base, n = t, 1
    while t in usados:
        t = f'{base}-{n}'; n += 1
    usados.add(t)
    return t

def esc(s):
    return s.replace('[', '(').replace(']', ')').replace('|', '/').strip()

def item_md(x):
    d = x['descricao'].strip()
    extra = []
    if x.get('idioma') == 'pt':
        extra.append('pt-BR')
    if x.get('tipo') in ('curso', 'canal', 'livro', 'awesome', 'comunidade', 'app', 'artigo'):
        extra.append(TIPO_ROTULO[x['tipo']])
    sufixo = f" <sub>{' · '.join(extra)}</sub>" if extra else ''
    return f"- [{esc(x['nome'])}]({x['url']})" + (f" - {d}" if d else '') + sufixo

def rel(de, para):
    return os.path.relpath(J(para), os.path.dirname(J(de))).replace(os.sep, '/')

def escrever(caminho, texto):
    os.makedirs(os.path.dirname(J(caminho)), exist_ok=True)
    open(J(caminho), 'w', encoding='utf-8').write(texto.rstrip() + '\n')

def titulo_ia(slug):
    return f"🤖 IA para {AREA[slug]['nome']}"

def ancora_ia(slug):
    return gh_anchor(titulo_ia(slug), set())

def pagina_area(slug):
    a = AREA[slug]; s = SETOR[a['setor']]
    cam = f"areas/{s['slug']}/{slug}.md"
    itens = POR_AREA.get(slug, [])
    ess = [x for x in itens if x['essencial'] and not x.get('ia')]
    ia_ess = [x for x in itens if x['essencial'] and x.get('ia')]
    ia_col = [x for x in itens if not x['essencial'] and x.get('ia')]
    resto = [x for x in itens if not x['essencial'] and not x.get('ia')]
    fontes = sorted({x['fonte'] for x in resto + ia_col})
    usados = set(); L = []
    L.append(f"# {a['emoji']} {a['nome']}\n")
    L.append(f"> {a['descricao']} **{len(itens)} links** nesta área: {len(ess)} essenciais escolhidos a dedo, "
             f"{len(ia_ess) + len(ia_col)} de inteligência artificial e {len(resto)} reunidos de {len(fontes)} listas curadas.\n")
    L.append(f"[← {s['emoji']} {s['nome']}]({rel(cam, f'areas/{s['slug']}/README.md')}) · "
             f"[🗂️ Catálogo completo]({rel(cam, 'areas/CATALOGO.md')}) · [🏠 Início]({rel(cam, 'README.md')})\n")
    blocos = []  # (titulo, nivel, itens)
    if ess:
        blocos.append(('⭐ Comece por aqui', 2, ess))
    if ia_ess or ia_col:
        blocos.append((titulo_ia(slug), 2, ia_ess + ia_col))
    if slug == 'linguagens':
        por_grupo = collections.defaultdict(list)
        for x in resto:
            por_grupo[x['grupo'] or 'Geral'].append(x)
        for g in sorted(por_grupo, key=lambda g: (-len(por_grupo[g]), g)):
            blocos.append((f'🔤 {g}', 2, por_grupo[g]))
    else:
        por_top = collections.defaultdict(list)
        for x in resto:
            por_top[x['topico']].append(x)
        grandes = sorted([t for t in por_top if len(por_top[t]) >= MIN_TOPICO and t not in ('Geral', 'Outros', 'Diversos')],
                         key=lambda t: (-len(por_top[t]), t.lower()))[:MAX_TOPICOS]
        miudos = [x for t in por_top if t not in grandes for x in por_top[t]]
        for t in sorted(grandes, key=lambda t: (-len(por_top[t]), t.lower())):
            blocos.append((f'◾ {t}', 2, por_top[t]))
        if miudos:
            blocos.append(('◾ Mais links', 2, miudos))
    L.append('## 📚 Índice\n')
    ancoras = []
    for titulo, _, its in blocos:
        anc = gh_anchor(titulo, usados)
        ancoras.append(anc)
        L.append(f"[{titulo}](#{anc}) <sub>{len(its)}</sub> <br>")
    L.append(f"[🧾 Fontes desta área](#{gh_anchor('🧾 Fontes desta área', set(usados))})\n")
    for (titulo, nivel, its) in blocos:
        L.append(f"{'#' * nivel} {titulo}\n")
        if titulo.startswith('🤖'):
            L.append(f"> Ferramentas, skills, MCPs, cursos, guias de prompt e uso responsável de IA para quem trabalha com {a['nome'].lower()}. "
                     f"Veja também [🤖 IA para todas as áreas]({rel(cam, 'ia/README.md')}).\n")
            ie = [x for x in its if x['essencial']]; ic = [x for x in its if not x['essencial']]
            if ie:
                L.append('### Essenciais de IA\n'); L += [item_md(x) for x in ie]; L.append('')
            if ic:
                L.append('### Mais ferramentas e recursos de IA\n'); L += [item_md(x) for x in ic]; L.append('')
        elif slug == 'linguagens' and titulo.startswith('🔤'):
            sub = collections.defaultdict(list)
            for x in its: sub[x['topico']].append(x)
            ordem = sorted(sub, key=lambda t: (-len(sub[t]), t.lower()))
            outros = [x for t in ordem if len(sub[t]) < MIN_TOPICO for x in sub[t]]
            for t in [t for t in ordem if len(sub[t]) >= MIN_TOPICO]:
                L.append(f"### {t}\n")
                L += [item_md(x) for x in sub[t]]; L.append('')
            if outros:
                L.append("### Mais links\n"); L += [item_md(x) for x in outros]; L.append('')
        else:
            L += [item_md(x) for x in its]; L.append('')
    L.append('## 🧾 Fontes desta área\n')
    L.append('Os links acima (fora os essenciais) foram reunidos destas listas curadas. Obrigado a quem as mantém.\n')
    lic = {(f['repo'], f['area']): f for f in FONTES}
    for f in fontes:
        meta = lic.get((f, slug)) or next((v for (r, _), v in lic.items() if r == f), {})
        n = sum(1 for x in resto if x['fonte'] == f)
        L.append(f"- [{f}](https://github.com/{f}) <sub>{n} links · licença {meta.get('licenca', '?')}</sub>")
    L.append(f"\n---\n[⬆️ Voltar ao topo](#{gh_anchor(L[0][2:].strip(), set())}) · [← {s['nome']}]({rel(cam, f'areas/{s['slug']}/README.md')})")
    escrever(cam, '\n'.join(L))
    return cam

def pagina_setor(s):
    cam = f"areas/{s['slug']}/README.md"
    L = [f"# {s['emoji']} {s['nome']}\n", f"> {s['descricao']}\n",
         f"[🗂️ Catálogo completo]({rel(cam, 'areas/CATALOGO.md')}) · [🏠 Início]({rel(cam, 'README.md')})\n",
         '| Área | O que cobre | Links | Essenciais |', '|---|---|:--:|:--:|']
    for a in s['areas']:
        its = POR_AREA.get(a['slug'], [])
        L.append(f"| [{a['emoji']} **{a['nome']}**](./{a['slug']}.md) | {a['descricao']} | {len(its)} | {sum(x['essencial'] for x in its)} |")
    L.append('\n## ⭐ Um gostinho de cada área\n')
    for a in s['areas']:
        ess = [x for x in POR_AREA.get(a['slug'], []) if x['essencial']][:5]
        if not ess: continue
        L.append(f"### {a['emoji']} {a['nome']}\n")
        L += [item_md(x) for x in ess]
        L.append(f"\n→ [Ver todos os {len(POR_AREA[a['slug']])} links de {a['nome']}](./{a['slug']}.md)\n")
    escrever(cam, '\n'.join(L))

def pagina_ia():
    cam = 'ia/README.md'
    n_ia = sum(1 for x in LINKS if x.get('ia'))
    n_ess = sum(1 for x in LINKS if x.get('ia') and x['essencial'])
    L = ['# 🤖 IA para todas as áreas\n',
         f"> A inteligência artificial já mudou o trabalho em quase toda profissão. Este guia tem **{n_ia} links de IA**, sendo **{n_ess} essenciais escolhidos a dedo** "
         "com descrição em português, distribuídos pelas áreas: cada página de área tem uma seção **🤖 IA para <área>** com ferramentas, skills, MCPs, cursos, "
         "guias de prompt e páginas de uso responsável daquela profissão.\n",
         f"[🏠 Início]({rel(cam, 'README.md')}) · [🗂️ Catálogo de áreas]({rel(cam, 'areas/CATALOGO.md')}) · [📖 Como usar IA com responsabilidade]({rel(cam, 'docs/09-ia-em-todas-as-areas.md')})\n",
         '## 📚 Índice\n', '[⭐ Por onde começar](#-por-onde-começar) <br>']
    usados = set(); gh_anchor('⭐ Por onde começar', usados)
    for s in TAX['setores']:
        L.append(f"[{s['emoji']} {s['nome']}](#{gh_anchor(s['emoji'] + ' ' + s['nome'], usados)}) <br>")
    L.append('')
    L.append('## ⭐ Por onde começar\n')
    L.append('> Primeiros passos com IA, para qualquer pessoa: guias oficiais, cursos gratuitos e ferramentas gerais.\n')
    for slug in ('ia-generativa', 'ferramentas-ia'):
        L += [item_md(x) for x in POR_AREA.get(slug, []) if x.get('ia') and x['essencial']]
    L.append(f"\nPara ir fundo: [✨ IA Generativa e LLMs]({rel(cam, 'areas/dados-ia/ia-generativa.md')}) e [🪄 Ferramentas de IA]({rel(cam, 'areas/ferramentas/ferramentas-ia.md')}).\n")
    for s in TAX['setores']:
        L.append(f"## {s['emoji']} {s['nome']}\n")
        L.append('| Área | Links de IA | Ver a seção |'); L.append('|---|:--:|---|')
        for ar in s['areas']:
            if ar['slug'] in ('ia-generativa', 'ferramentas-ia'): continue
            n = sum(1 for x in POR_AREA.get(ar['slug'], []) if x.get('ia'))
            L.append(f"| {ar['emoji']} {ar['nome']} | {n} | [{titulo_ia(ar['slug'])}]({rel(cam, f'areas/{s['slug']}/{ar['slug']}.md')}#{ancora_ia(ar['slug'])}) |")
        L.append('\n<details><summary>Os 3 primeiros de cada área</summary>\n')
        for ar in s['areas']:
            if ar['slug'] in ('ia-generativa', 'ferramentas-ia'): continue
            top = [x for x in POR_AREA.get(ar['slug'], []) if x.get('ia') and x['essencial']][:3]
            if top:
                L.append(f"**{ar['emoji']} {ar['nome']}**\n"); L += [item_md(x) for x in top]; L.append('')
        L.append('</details>\n')
    escrever(cam, '\n'.join(L))

def catalogo():
    cam = 'areas/CATALOGO.md'
    total = len(LINKS); unicos = len({chave(x['url']) for x in LINKS})
    L = [f"# 🗂️ Catálogo de áreas\n",
         f"> **{total} links** ({unicos} URLs únicas) em **{len(AREA)} áreas** de **{len(SETOR)} setores**. Clique numa área para abrir a página dela.\n",
         f"[🏠 Início]({rel(cam, 'README.md')}) · [🧭 Trilhas por profissão]({rel(cam, 'trilhas/README.md')})\n"]
    for s in TAX['setores']:
        n = sum(len(POR_AREA.get(a['slug'], [])) for a in s['areas'])
        L.append(f"## {s['emoji']} {s['nome']}\n")
        L.append(f"{s['descricao']} **{n} links.** [Abrir o setor](./{s['slug']}/README.md)\n")
        L.append('| Área | Links | Essenciais |'); L.append('|---|:--:|:--:|')
        for a in s['areas']:
            its = POR_AREA.get(a['slug'], [])
            L.append(f"| [{a['emoji']} {a['nome']}](./{s['slug']}/{a['slug']}.md) | {len(its)} | {sum(x['essencial'] for x in its)} |")
        L.append('')
    escrever(cam, '\n'.join(L))

def trilhas():
    cam = 'trilhas/README.md'
    L = ['# 🧭 Trilhas por profissão\n',
         '> Não sabe por onde começar? Escolha a sua profissão (ou a que você quer ter). Cada trilha junta as áreas que importam, na ordem em que vale a pena estudar, e mostra os primeiros links de cada uma.\n',
         f"[🏠 Início]({rel(cam, 'README.md')}) · [🗂️ Catálogo de áreas]({rel(cam, 'areas/CATALOGO.md')})\n", '## 📚 Índice\n']
    usados = set()
    for t in TRI:
        L.append(f"[{t['emoji']} {t['nome']}](#{gh_anchor(t['emoji'] + ' ' + t['nome'], usados)}) <br>")
    L.append('')
    for t in TRI:
        L.append(f"## {t['emoji']} {t['nome']}\n")
        L.append(f"> {t['resumo']}\n")
        for i, slug in enumerate(t['areas'], 1):
            a = AREA[slug]
            L.append(f"{i}. **[{a['emoji']} {a['nome']}]({rel(cam, f'areas/{a['setor']}/{slug}.md')})**: {a['descricao']}")
        ia_links = ' · '.join(f"[{AREA[s_]['nome']}]({rel(cam, f'areas/{AREA[s_]['setor']}/{s_}.md')}#{ancora_ia(s_)})" for s_ in t['areas'] if s_ not in ('ia-generativa', 'ferramentas-ia'))
        L.append(f"\n🤖 **IA nesta trilha:** {ia_links}")
        L.append('\n<details><summary>Primeiros links desta trilha</summary>\n')
        for slug in t['areas'][:4]:
            ess = [x for x in POR_AREA.get(slug, []) if x['essencial'] and not x.get('ia')][:3]
            L += [item_md(x) for x in ess]
        L.append('\n</details>\n')
    escrever(cam, '\n'.join(L))

def fontes_doc():
    cam = 'docs/07-fontes-e-licencas.md'
    usadas = collections.Counter((x['fonte'], x['area']) for x in LINKS if not x['essencial'])
    lic = collections.Counter()
    L = ['# 07 · Fontes e licenças\n',
         '> Este guia existe porque milhares de pessoas mantêm listas curadas no GitHub. Esta página dá o crédito a cada uma e explica como as licenças foram respeitadas.\n',
         '## Como as licenças foram tratadas\n',
         '- **Links e nomes** são fatos: entram de qualquer fonte, sempre com crédito.',
         '- **Descrições** são texto autoral: só foram reaproveitadas de fontes com licença que permite (CC0, CC-BY, CC-BY-SA, MIT, Unlicense e afins). '
         'De fontes **sem licença**, **GPL** ou **não comerciais (NC)**, entram só nome e link, sem a descrição.',
         '- Por incluir material CC-BY-SA, o **conteúdo** deste guia é distribuído sob **CC BY-SA 4.0**. Os **scripts** são MIT.',
         '- Os **essenciais** ("Comece por aqui") foram escolhidos e descritos pela curadoria deste guia.\n',
         '## Fontes usadas\n', '| Fonte | Área | Links usados | Licença |', '|---|---|:--:|---|']
    for f in sorted(FONTES, key=lambda f: (f['area'], f['repo'])):
        if f['area'] == '_mapa':
            n = sum(v for (r, _), v in usadas.items() if r == f['repo']); area = 'várias'
        else:
            n = usadas.get((f['repo'], f['area']), 0); area = AREA[f['area']]['nome']
        lic[f.get('licenca', '?')] += 1
        L.append(f"| [{f['repo']}](https://github.com/{f['repo']}) | {area} | {n} | {f.get('licenca', '?')} |")
    L.append('\n## Resumo das licenças das fontes\n')
    L += [f"- {k}: {v} fontes" for k, v in lic.most_common()]
    escrever(cam, '\n'.join(L))

def readme():
    cam = 'README.md'
    total = len(LINKS); unicos = len({chave(x['url']) for x in LINKS}); ness = sum(x['essencial'] for x in LINKS)
    nfontes = len({x['fonte'] for x in LINKS if not x['essencial']})
    tipos = collections.Counter(x['tipo'] for x in LINKS)
    pt = sum(1 for x in LINKS if x.get('idioma') == 'pt')
    nome, repo = CFG['nome'], CFG['repo']
    L = ['<p align="center">\n  <img src="./images/logo.svg" alt="' + nome + '" width="160" height="160">\n</p>\n',
         f'<h1 align="center">{nome}</h1>\n', '## :dart: A proposta\n',
         f"> O **{nome}** é um mapa de conhecimento aberto e gratuito: **{total} links** ({unicos} URLs únicas) organizados em **{len(SETOR)} setores**, "
         f"**{len(AREA)} áreas** e centenas de tópicos, para que **qualquer pessoa** encontre os melhores sites, cursos, ferramentas, repositórios, listas awesome, "
         "comunidades e utilitários da sua área: desenvolvimento, dados, segurança, design, edição de vídeo, cinema, fotografia, música, marketing, tráfego pago, "
         "vendas, finanças, direito, saúde, ciência, educação, idiomas e muito mais. Cada área começa com **essenciais escolhidos a dedo e descritos em português**, traz uma seção de **inteligência artificial aplicada àquela profissão** "
         "e segue com os links reunidos das melhores listas curadas da comunidade, com crédito a cada uma.\n",
         f"- 🗂️ [Catálogo de áreas](areas/CATALOGO.md): todas as {len(AREA)} áreas, por setor, com a contagem de links.",
         f"- 🧭 [Trilhas por profissão](trilhas/README.md): {len(TRI)} trilhas, de desenvolvedor(a) front-end a filmmaker, de gestor(a) de tráfego a professor(a).\n",
         '## 💡 Como este guia é organizado\n',
         '> Três níveis, do geral ao específico: **setor** (ex.: Design e Criação) → **área** (ex.: Edição de Vídeo) → **tópico** (ex.: Non-Linear Editors). '
         'Cada área é uma página com índice, uma seção **⭐ Comece por aqui** e os tópicos ordenados do maior para o menor. Tudo vem de uma base de dados aberta '
         '(`data/links.jsonl`) e é gerado por scripts em Python, então o guia inteiro pode ser regenerado, validado e ampliado. A organização segue a dos guias '
         '[guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) e [guiadomaestri](https://github.com/arthurspk/guiadomaestri). Detalhes em [docs/02](docs/02-organizacao-e-taxonomia.md).\n',
         '## 🌍 Tradução\n',
         '> O guia está em **português (Brasil)**. As descrições dos essenciais e dos guias de origem brasileira estão em pt-BR; boa parte das demais vem das listas originais, em inglês. '
         'Quer traduzir o guia ou as descrições? Veja [docs/08 · Como contribuir](docs/08-como-contribuir.md).\n',
         '🇧🇷・**Português (Brasil) —** [este arquivo](README.md)<br>\n',
         '## 📚 Índice\n',
         '[⭐ Comece por aqui](#-comece-por-aqui) — o caminho mais curto até o que você procura. <br>',
         '[📖 Documentação](#-documentação) — como usar, como é organizado, como contribuir. <br>',
         '[🗂️ Setores e áreas](#️-setores-e-áreas) — os 9 setores e todas as áreas. <br>',
         '[🧭 Trilhas por profissão](#-trilhas-por-profissão) — por onde começar na sua carreira. <br>',
         '[🤖 IA em todas as áreas](#-ia-em-todas-as-áreas) — inteligência artificial aplicada a cada profissão. <br>',
         '[🔢 O guia em números](#-o-guia-em-números) — quantos links, de que tipo, de onde. <br>',
         '[📜 Scripts disponíveis](#-scripts-disponíveis) — coletores, gerador e validadores em Python. <br>',
         '[🛠️ Regenerar e validar](#️-regenerar-e-validar) — reconstruir e conferir tudo. <br>',
         '[🤝 Contribuição](#-contribuição) — como sugerir links, áreas e traduções. <br>',
         '[⚖️ Licenças e créditos](#️-licenças-e-créditos) — de onde vem cada link. <br>',
         '[⚠️ Aviso](#️-aviso) — sobre links externos. <br>',
         '[⭐ Star History](#-star-history) — o gráfico de estrelas do repositório. <br>\n',
         '## ⭐ Comece por aqui\n',
         '> Cinco atalhos, conforme o que você tem em mente.\n',
         '- [🧭 **Sei a minha profissão**](trilhas/README.md): abra a trilha dela e siga as áreas na ordem.',
         '- [🗂️ **Sei o assunto**](areas/CATALOGO.md): abra o catálogo e vá direto à área.',
         '- [🤖 **Quero usar IA no meu trabalho**](ia/README.md): a seção de IA de cada profissão, num lugar só.',
         '- [🧰 **Quero só boas ferramentas**](areas/ferramentas/README.md): ferramentas online, apps por sistema, extensões, APIs e recursos gratuitos.',
         '- 🔎 **Procurando algo específico?** Use `Ctrl+F` na página da área, ou a busca do GitHub neste repositório. A base completa está em [`data/links.csv`](data/links.csv) para abrir em qualquer planilha.\n',
         '## 📖 Documentação\n',
         '> Os documentos do guia. Comece pelo 01 se é a sua primeira vez aqui.\n',
         '- [🧭 01 · **Como usar este guia**](docs/01-como-usar.md) — navegação, símbolos e como estudar com ele.',
         '- [🗺️ 02 · **Organização e taxonomia**](docs/02-organizacao-e-taxonomia.md) — setores, áreas, tópicos e por que estão assim.',
         '- [🧭 03 · **Trilhas por profissão**](docs/03-trilhas-por-profissao.md) — como usar e criar trilhas; a lista está em [trilhas/](trilhas/README.md).',
         '- [📐 04 · **Formato dos dados**](docs/04-formato-dos-dados.md) — os campos de `links.jsonl`, `fontes.json` e `essenciais.json`.',
         '- [🕷️ 05 · **Coleta com Scrapling**](docs/05-coleta-com-scrapling.md) — como os links são coletados, verificados e atualizados.',
         '- [🔍 06 · **Curadoria e qualidade**](docs/06-curadoria-e-qualidade.md) — critérios de entrada, saída, deduplicação e tetos por área.',
         '- [⚖️ 07 · **Fontes e licenças**](docs/07-fontes-e-licencas.md) — todas as fontes, com crédito e licença.',
         '- [🤝 08 · **Como contribuir**](docs/08-como-contribuir.md) — sugerir links, áreas, trilhas e traduções.',
         '- [🤖 09 · **IA em todas as áreas**](docs/09-ia-em-todas-as-areas.md) — como a camada de IA é montada e como usar IA com responsabilidade.\n',
         '## 🗂️ Setores e áreas\n',
         f"> {len(SETOR)} setores e {len(AREA)} áreas. Cada setor tem uma página com o resumo das áreas e os primeiros essenciais de cada uma.\n"]
    for s in TAX['setores']:
        n = sum(len(POR_AREA.get(a['slug'], [])) for a in s['areas'])
        areas = ' · '.join(f"[{a['nome']}](areas/{s['slug']}/{a['slug']}.md)" for a in s['areas'])
        L.append(f"- [{s['emoji']} **{s['nome']}**](areas/{s['slug']}/README.md) — {n} links · {areas}.")
    L += ['', '## 🧭 Trilhas por profissão\n',
          '> Cada trilha junta as áreas que importam para uma profissão, na ordem em que vale a pena estudar.\n']
    L.append(' · '.join(f"[{t['emoji']} {t['nome']}](trilhas/README.md#{gh_anchor(t['emoji'] + ' ' + t['nome'], set())})" for t in TRI) + '\n')
    n_ia = sum(1 for x in LINKS if x.get('ia')); n_ia_ess = sum(1 for x in LINKS if x.get('ia') and x['essencial'])
    L += ['## 🤖 IA em todas as áreas\n',
          f"> Toda página de área tem uma seção **🤖 IA para <área>**: {n_ia} links de IA no total, {n_ia_ess} deles essenciais escolhidos a dedo e descritos em português. "
          "Ferramentas da profissão, skills, plugins e MCPs para agentes (Claude, ChatGPT, Codex), cursos gratuitos, guias de prompt, regulação e uso responsável.\n",
          '- [🤖 **IA para todas as áreas**](ia/README.md): a seção de IA de cada área, por setor, num lugar só.',
          '- Exemplos: ' + ' · '.join(f"[{AREA[s_]['nome']}](areas/{AREA[s_]['setor']}/{s_}.md#{ancora_ia(s_)})" for s_ in
                                      ('edicao-de-video', 'trafego-pago', 'juridico', 'saude', 'educacao', 'qa-testes', 'contabilidade', 'design-ui-ux')) + '.\n']
    L += ['## 🔢 O guia em números\n', '| Indicador | Valor |', '|---|---|',
          f'| Links no total | {total} |', f'| URLs únicas | {unicos} |', f'| Setores / áreas | {len(SETOR)} / {len(AREA)} |',
          f'| Essenciais escolhidos a dedo (pt-BR) | {ness} |', f"| Links de IA (seções 🤖 nas áreas) | {sum(1 for x in LINKS if x.get('ia'))} |", f'| Listas curadas usadas como fonte | {nfontes} |',
          f'| Links marcados como conteúdo em português | {pt} |',
          '| Por tipo | ' + ' · '.join(f"{TIPO_ROTULO.get(k, k)} {v}" for k, v in tipos.most_common()) + ' |', '',
          '| Setor | Áreas | Links |', '|---|:--:|:--:|']
    for s in TAX['setores']:
        L.append(f"| {s['emoji']} {s['nome']} | {len(s['areas'])} | {sum(len(POR_AREA.get(a['slug'], [])) for a in s['areas'])} |")
    L += ['', '## 📜 Scripts disponíveis\n', '> Tudo é gerado por Python. Detalhes em [`scripts/README.md`](scripts/README.md).\n',
          '| Script | Tipo | O que faz |', '|---|---|---|',
          '| [`scripts/coletar.py`](scripts/coletar.py) | coletor | Baixa as listas curadas (Scrapling, com git como reserva) e extrai cada link com nome, descrição e tópico. |',
          '| [`scripts/selecionar.py`](scripts/selecionar.py) | curadoria | Normaliza, deduplica, aplica a política de licenças e escolhe os links de cada área com teto e rodízio entre fontes. |',
          '| [`scripts/gerar.py`](scripts/gerar.py) | gerador | Gera este README, as páginas de setor e de área, as trilhas, o catálogo e o CSV. |',
          '| [`scripts/checar_links.py`](scripts/checar_links.py) | verificação | Confere se os links respondem (Scrapling ou urllib) e marca os quebrados. |',
          '| [`tests/validar.py`](tests/validar.py) | validação | Confere dados, páginas, âncoras, duplicados e contagens. |', '',
          '## 🛠️ Regenerar e validar\n',
          '> Só a stdlib do Python 3 é obrigatória. O Scrapling (`pip install "scrapling[fetchers]"`) deixa a coleta e a checagem de links mais robustas.\n',
          '```bash', 'python3 scripts/coletar.py        # → data/brutos.jsonl.gz (todas as fontes)',
          'python3 scripts/selecionar.py     # → data/links.jsonl (base final)', 'python3 scripts/gerar.py          # → README, areas/, trilhas/, docs/07, data/links.csv',
          'python3 scripts/checar_links.py   # → data/status-links.json (opcional, demora)', 'python3 tests/validar.py          # → "OK" se tudo estiver consistente', '```\n',
          '## 🤝 Contribuição\n',
          '> Sugestões são muito bem-vindas: um link que faltou, uma área nova, uma trilha, uma tradução.\n',
          '- **Link novo:** adicione em `data/essenciais.json` (se é essencial da área) ou sugira uma **lista curada** em `data/fontes.json`. Depois rode o gerador.',
          '- **Link quebrado ou ruim:** abra uma issue com o endereço da página e o link.',
          '- Passo a passo em [docs/08 · Como contribuir](docs/08-como-contribuir.md) e em [CONTRIBUTING.md](CONTRIBUTING.md).\n',
          '## ⚖️ Licenças e créditos\n',
          f"> Os links vêm de **{nfontes} listas curadas** mantidas pela comunidade, listadas com licença em [docs/07](docs/07-fontes-e-licencas.md) e no rodapé de cada área. "
          'O conteúdo deste guia é **CC BY-SA 4.0** e os scripts são **MIT** (veja [LICENSE](LICENSE)). Descrições de fontes sem licença, GPL ou não comerciais não foram copiadas.\n',
          '## ⚠️ Aviso\n',
          '> Este guia aponta para sites de terceiros. Não há afiliação com nenhum deles, e o conteúdo de cada site é responsabilidade de quem o mantém. '
          'Links mudam: se encontrar um quebrado, avise. Conteúdo de segurança ofensiva é para estudo e uso **somente em escopo autorizado**.\n',
          '## ⭐ Star History\n',
          f"[![Star History Chart](https://api.star-history.com/svg?repos={repo}&type=Date)](https://star-history.com/#{repo}&Date)"]
    escrever(cam, '\n'.join(L))

def csv_out():
    with open(J('data', 'links.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['setor', 'area', 'topico', 'nome', 'url', 'descricao', 'tipo', 'idioma', 'essencial', 'fonte'])
        for x in LINKS:
            w.writerow([AREA[x['area']]['setor'], x['area'], x['grupo'] or x['topico'], x['nome'], x['url'], x['descricao'],
                        x['tipo'], x.get('idioma', ''), 'sim' if x['essencial'] else '', x['fonte']])

def main():
    for s in TAX['setores']:
        for a in s['areas']:
            pagina_area(a['slug'])
        pagina_setor(s)
    catalogo(); trilhas(); pagina_ia(); fontes_doc(); readme(); csv_out()
    print(f"Gerado: {len(AREA)} páginas de área, {len(SETOR)} setores, {len(TRI)} trilhas, {len(LINKS)} links.")

if __name__ == '__main__':
    main()
