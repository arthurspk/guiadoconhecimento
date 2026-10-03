#!/usr/bin/env python3
"""Gera o repositório navegável a partir de data/, em todos os idiomas de base.IDIOMAS:
README, areas/, trilhas/, ia/ (português na raiz; os outros em README.<idioma>.md e i18n/<idioma>/),
mais docs/07-fontes-e-licencas.md e data/links.csv.

Só usa a stdlib. Rodar de novo produz os mesmos arquivos (saída determinística).
Uso: python3 scripts/gerar.py [--idiomas pt,en]
"""
import argparse, collections, csv, json, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import (CODIGOS, IDIOMAS, J, TIPO_EMOJI, TIPOS_COM_ROTULO, Ctx, carregar, emoji_topico, esc, escrever, gh_anchor,
                  limpa, textos_pt)
from gerar_ia import pagina_ia, paginas_profissoes
from selecionar import chave

CFG = carregar('config.json')
TAX = carregar('taxonomia.json')
TRI = carregar('trilhas.json')['trilhas']
LINKS = [json.loads(l) for l in open(J('data', 'links.jsonl'), encoding='utf-8')]
FONTES = carregar('fontes.json') + carregar('fontes-guias.json')
ARQ_REPOS = J('data', 'repos-ia.jsonl')
REPOS = [json.loads(l) for l in open(ARQ_REPOS, encoding='utf-8')] if os.path.exists(ARQ_REPOS) else []

AREA = {a['slug']: dict(a, setor=s['slug']) for s in TAX['setores'] for a in s['areas']}
SETOR = {s['slug']: s for s in TAX['setores']}
POR_AREA = collections.defaultdict(list)
for x in LINKS:
    POR_AREA[x['area']].append(x)
MIN_TOPICO = 6    # tópicos com menos itens vão para "Mais links"
MAX_TOPICOS = 15  # no máximo 15 seções de tópico por página (o resto vai para "Mais links")
SEM_IA_PROPRIA = ('ia-generativa', 'ferramentas-ia')
DADOS = {'TAX': TAX, 'TRI': TRI, 'AREA': AREA, 'POR_AREA': POR_AREA, 'REPOS': REPOS, 'SEM_IA_PROPRIA': SEM_IA_PROPRIA}


def item_md(c: Ctx, x: dict) -> str:
    d = c.d(limpa(x['descricao']))
    extra = []
    if x.get('tipo') in TIPOS_COM_ROTULO:
        extra.append(f"{TIPO_EMOJI[x['tipo']]} {c.t('tipo.' + x['tipo'])}")
    if x.get('idioma') == 'pt':
        extra.append('🇧🇷 pt-BR')
    sufixo = f" <sub>{' · '.join(extra)}</sub>" if extra else ''
    return f"- [{esc(x['nome'])}]({x['url']})" + (f" - {d}" if d else '') + sufixo


def nome_area(c: Ctx, slug: str) -> str:
    return c.t(f'area.{slug}.nome')


def titulo_ia(c: Ctx, slug: str) -> str:
    return c.t('ia_area.titulo', area=nome_area(c, slug))


def ancora_ia(c: Ctx, slug: str) -> str:
    return gh_anchor(titulo_ia(c, slug), set())


def link_area(c: Ctx, de: str, slug: str) -> str:
    return c.rel(de, f"areas/{AREA[slug]['setor']}/{slug}.md")


def pagina_area(c: Ctx, slug: str) -> None:
    a = AREA[slug]; s = SETOR[a['setor']]
    cam = f"areas/{s['slug']}/{slug}.md"
    nome, nome_setor = nome_area(c, slug), c.t(f"setor.{s['slug']}.nome")
    itens = POR_AREA.get(slug, [])
    ess = [x for x in itens if x['essencial'] and not x.get('ia')]
    ess_inicio = [x for x in ess if x['topico'] == 'Comece por aqui']
    ess_tema = collections.OrderedDict()   # essenciais com tópico próprio viram seções da curadoria
    for x in ess:
        if x['topico'] != 'Comece por aqui':
            ess_tema.setdefault(x['topico'], []).append(x)
    ia_ess = [x for x in itens if x['essencial'] and x.get('ia')]
    ia_col = [x for x in itens if not x['essencial'] and x.get('ia')]
    resto = [x for x in itens if not x['essencial'] and not x.get('ia')]
    fontes = sorted({x['fonte'] for x in resto + ia_col})
    titulo = f"{a['emoji']} {nome}"
    L = [f"# {titulo}\n",
         '> ' + c.t(f'area.{slug}.descricao') + ' ' + c.t('area.resumo', n=len(itens), ess=len(ess), ia=len(ia_ess) + len(ia_col),
                                                         resto=len(resto), fontes=len(fontes)) + '\n',
         f"[← {s['emoji']} {nome_setor}]({c.rel(cam, f'areas/{s['slug']}/README.md')}) · "
         f"[🗂️ {c.t('nav.catalogo')}]({c.rel(cam, 'areas/CATALOGO.md')}) · [🏠 {c.t('nav.inicio')}]({c.rel(cam, 'README.md')})\n",
         c.seletor(cam)]
    blocos = []  # (titulo, descricao, itens, tipo)
    if ess_inicio:
        blocos.append((c.t('comece.titulo'), c.t('comece.desc', area=nome), ess_inicio, 'lista'))
    for t, its in ess_tema.items():
        nt = c.d(t)
        blocos.append((f'{emoji_topico(t)} {nt}', c.t('curado.desc', topico=nt, area=nome), its, 'lista'))
    if ia_ess or ia_col:
        blocos.append((titulo_ia(c, slug), c.t('ia_area.desc', area=nome, link=c.rel(cam, 'ia/README.md')), ia_ess + ia_col, 'ia'))
    if slug == 'linguagens':
        por_grupo = collections.defaultdict(list)
        for x in resto:
            por_grupo[x['grupo'] or 'Geral'].append(x)
        for g in sorted(por_grupo, key=lambda g: (-len(por_grupo[g]), g)):
            blocos.append((f'🔤 {g}', c.t('linguagem.desc', n=len(por_grupo[g]), linguagem=g), por_grupo[g], 'grupo'))
    else:
        por_top = collections.defaultdict(list)
        for x in resto:
            por_top[x['topico']].append(x)
        grandes = sorted([t for t in por_top if len(por_top[t]) >= MIN_TOPICO and t not in ('Geral', 'Outros', 'Diversos')],
                         key=lambda t: (-len(por_top[t]), t.lower()))[:MAX_TOPICOS - len(ess_tema)]
        miudos = [x for t in por_top if t not in grandes for x in por_top[t]]
        for t in grandes:
            nt = c.d(t)
            blocos.append((f'{emoji_topico(t)} {nt}', c.t('topico.desc', n=len(por_top[t]), topico=nt, area=nome), por_top[t], 'lista'))
        if miudos:
            blocos.append((c.t('mais.titulo'), c.t('mais.desc', area=nome), miudos, 'lista'))
    usados = set(); gh_anchor(titulo, usados); gh_anchor(c.t('indice.titulo'), usados)
    L += [f"## {c.t('indice.titulo')}\n", f"> {c.t('indice.desc')}\n"]
    for tit, _, its, _ in blocos:
        L.append(f"[{tit}](#{gh_anchor(tit, usados)}) <sub>{len(its)}</sub> <br>")
    L.append(f"[{c.t('fontes_area.titulo')}](#{gh_anchor(c.t('fontes_area.titulo'), usados)})\n")
    for tit, desc, its, tipo in blocos:
        L += [f"## {tit}\n", f"> {desc}\n"]
        if tipo == 'ia':
            for sub, grupo in ((c.t('ia_area.essenciais'), [x for x in its if x['essencial']]),
                               (c.t('ia_area.mais'), [x for x in its if not x['essencial']])):
                if grupo:
                    L += [f"### {sub}\n"] + [item_md(c, x) for x in grupo] + ['']
        elif tipo == 'grupo':
            sub = collections.defaultdict(list)
            for x in its:
                sub[x['topico']].append(x)
            ordem = sorted(sub, key=lambda t: (-len(sub[t]), t.lower()))
            outros = [x for t in ordem if len(sub[t]) < MIN_TOPICO for x in sub[t]]
            for t in [t for t in ordem if len(sub[t]) >= MIN_TOPICO]:
                L += [f"### {emoji_topico(t)} {c.d(t)}\n"] + [item_md(c, x) for x in sub[t]] + ['']
            if outros:
                L += [f"### {c.t('mais.titulo')}\n"] + [item_md(c, x) for x in outros] + ['']
        else:
            L += [item_md(c, x) for x in its] + ['']
    L += [f"## {c.t('fontes_area.titulo')}\n", f"> {c.t('fontes_area.desc')}\n"]
    lic = {(f['repo'], f['area']): f for f in FONTES}
    for f in fontes:
        meta = lic.get((f, slug)) or next((v for (r, _), v in lic.items() if r == f), {})
        n = sum(1 for x in resto + ia_col if x['fonte'] == f)
        L.append(f"- [{f}](https://github.com/{f}) <sub>🔗 {n} · ⚖️ {meta.get('licenca', '?')}</sub>")
    L.append(f"\n---\n[⬆️ {c.t('nav.topo')}](#{gh_anchor(titulo, set())}) · [← {nome_setor}]({c.rel(cam, f'areas/{s['slug']}/README.md')})")
    c.escrever(cam, L)


def pagina_setor(c: Ctx, s: dict) -> None:
    cam = f"areas/{s['slug']}/README.md"
    L = [f"# {s['emoji']} {c.t(f'setor.{s['slug']}.nome')}\n", f"> {c.t(f'setor.{s['slug']}.descricao')}\n",
         f"[🗂️ {c.t('nav.catalogo')}]({c.rel(cam, 'areas/CATALOGO.md')}) · [🏠 {c.t('nav.inicio')}]({c.rel(cam, 'README.md')})\n", c.seletor(cam),
         f"| {c.t('tab.area')} | {c.t('tab.cobre')} | 🔗 {c.t('tab.links')} | ⭐ {c.t('tab.essenciais')} |", '|---|---|:--:|:--:|']
    for a in s['areas']:
        its = POR_AREA.get(a['slug'], [])
        L.append(f"| [{a['emoji']} **{nome_area(c, a['slug'])}**](./{a['slug']}.md) | {c.t(f'area.{a['slug']}.descricao')} | {len(its)} | {sum(x['essencial'] for x in its)} |")
    L += [f"\n## {c.t('gostinho.titulo')}\n", f"> {c.t('gostinho.desc')}\n"]
    for a in s['areas']:
        ess = [x for x in POR_AREA.get(a['slug'], []) if x['essencial']][:5]
        if not ess:
            continue
        L += [f"### {a['emoji']} {nome_area(c, a['slug'])}\n"] + [item_md(c, x) for x in ess]
        L.append(f"\n→ [{c.t('gostinho.ver', n=len(POR_AREA[a['slug']]), area=nome_area(c, a['slug']))}](./{a['slug']}.md)\n")
    c.escrever(cam, L)


def catalogo(c: Ctx) -> None:
    cam = 'areas/CATALOGO.md'
    total = len(LINKS); unicos = len({chave(x['url']) for x in LINKS})
    L = [f"# 🗂️ {c.t('nav.catalogo')}\n", '> ' + c.t('catalogo.resumo', total=total, unicos=unicos, areas=len(AREA), setores=len(SETOR)) + '\n',
         f"[🏠 {c.t('nav.inicio')}]({c.rel(cam, 'README.md')}) · [🧭 {c.t('nav.trilhas')}]({c.rel(cam, 'trilhas/README.md')}) · "
         f"[🤖 {c.t('nav.ia')}]({c.rel(cam, 'ia/README.md')})\n", c.seletor(cam)]
    for s in TAX['setores']:
        n = sum(len(POR_AREA.get(a['slug'], [])) for a in s['areas'])
        L += [f"## {s['emoji']} {c.t(f'setor.{s['slug']}.nome')}\n",
              f"> {c.t(f'setor.{s['slug']}.descricao')} **🔗 {n}** · [{c.t('catalogo.abrir')}](./{s['slug']}/README.md)\n",
              f"| {c.t('tab.area')} | {c.t('tab.cobre')} | 🔗 {c.t('tab.links')} | ⭐ {c.t('tab.essenciais')} |", '|---|---|:--:|:--:|']
        for a in s['areas']:
            its = POR_AREA.get(a['slug'], [])
            L.append(f"| [{a['emoji']} {nome_area(c, a['slug'])}](./{s['slug']}/{a['slug']}.md) | {c.t(f'area.{a['slug']}.descricao')} | {len(its)} | {sum(x['essencial'] for x in its)} |")
        L.append('')
    c.escrever(cam, L)


def titulo_trilha(c: Ctx, t: dict) -> str:
    return f"{t['emoji']} {c.t(f'trilha.{t['slug']}.nome')}"


def trilhas(c: Ctx) -> None:
    cam = 'trilhas/README.md'
    L = [f"# 🧭 {c.t('nav.trilhas')}\n", f"> {c.t('trilhas.intro')}\n",
         f"[🏠 {c.t('nav.inicio')}]({c.rel(cam, 'README.md')}) · [🗂️ {c.t('nav.catalogo')}]({c.rel(cam, 'areas/CATALOGO.md')}) · "
         f"[🧠 {c.t('nav.profissoes')}]({c.rel(cam, 'ia/profissoes/README.md')})\n", c.seletor(cam),
         f"## {c.t('indice.titulo')}\n", f"> {c.t('trilhas.indice')}\n"]
    usados = set(); gh_anchor(c.t('indice.titulo'), usados)
    for t in TRI:
        L.append(f"[{titulo_trilha(c, t)}](#{gh_anchor(titulo_trilha(c, t), usados)}) <br>")
    L.append('')
    for t in TRI:
        L += [f"## {titulo_trilha(c, t)}\n", f"> {c.t(f'trilha.{t['slug']}.resumo')}\n"]
        for i, slug in enumerate(t['areas'], 1):
            L.append(f"{i}. **[{AREA[slug]['emoji']} {nome_area(c, slug)}]({link_area(c, cam, slug)})**: {c.t(f'area.{slug}.descricao')}")
        L.append(f"\n🤖 **{c.t('trilhas.ia')}**\n")
        L += [f"- [{nome_area(c, s_)}]({link_area(c, cam, s_)}#{ancora_ia(c, s_)})" for s_ in t['areas'] if s_ not in SEM_IA_PROPRIA]
        if REPOS:
            n = sum(1 for r in REPOS if r['trilha'] == t['slug'])
            L.append(f"\n🧠 **[{c.t('trilhas.repos', n=n)}]({c.rel(cam, f'ia/profissoes/{t['slug']}.md')})**")
        L.append(f"\n<details><summary>📌 {c.t('trilhas.primeiros')}</summary>\n")
        for slug in t['areas'][:4]:
            L += [item_md(c, x) for x in [x for x in POR_AREA.get(slug, []) if x['essencial'] and not x.get('ia')][:3]]
        L.append('\n</details>\n')
    c.escrever(cam, L)


def fontes_doc() -> None:
    usadas = collections.Counter((x['fonte'], x['area']) for x in LINKS if not x['essencial'])
    lic = collections.Counter()
    L = ['# 07 · Fontes e licenças\n',
         '> Este guia existe porque milhares de pessoas mantêm listas curadas no GitHub. Esta página dá o crédito a cada uma e explica como as licenças foram respeitadas.\n',
         '## ⚖️ Como as licenças foram tratadas\n',
         '> As regras que decidem o que entra de cada fonte e com que texto.\n',
         '- **Links e nomes** são fatos: entram de qualquer fonte, sempre com crédito.',
         '- **Descrições** são texto autoral: só foram reaproveitadas de fontes com licença que permite (CC0, CC-BY, CC-BY-SA, MIT, Unlicense e afins). '
         'De fontes **sem licença**, **GPL** ou **não comerciais (NC)**, o texto da lista não é copiado.',
         '- **Todo link tem descrição.** Quando a descrição da lista não pode ser usada, entra a descrição pública que o próprio projeto publica '
         '(o campo "About" do repositório no GitHub) ou uma descrição escrita pela curadoria deste guia, guardada em `data/descricoes.json`. Link sem descrição não entra.',
         '- **Repositórios de IA por profissão** (`data/repos-ia.jsonl`) vêm da busca pública do GitHub; a descrição é a que o próprio repositório publica.',
         '- **Traduções** das descrições são automáticas (Argos Translate, modelos abertos, rodando offline) e ficam em `data/i18n/`. Correções são bem-vindas.',
         '- Por incluir material CC-BY-SA, o **conteúdo** deste guia é distribuído sob **CC BY-SA 4.0**. Os **scripts** são MIT.',
         '- Os **essenciais** ("Comece por aqui") foram escolhidos e descritos pela curadoria deste guia.\n',
         '## 🧾 Fontes usadas\n', '> Cada lista curada, a área em que foi usada, quantos links entraram e a licença.\n',
         '| Fonte | Área | Links usados | Licença |', '|---|---|:--:|---|']
    for f in sorted(FONTES, key=lambda f: (f['area'], f['repo'])):
        if f['area'] == '_mapa':
            n = sum(v for (r, _), v in usadas.items() if r == f['repo']); area = 'várias'
        else:
            n = usadas.get((f['repo'], f['area']), 0); area = AREA[f['area']]['nome']
        lic[f.get('licenca', '?')] += 1
        L.append(f"| [{f['repo']}](https://github.com/{f['repo']}) | {area} | {n} | {f.get('licenca', '?')} |")
    L += ['\n## 📊 Resumo das licenças das fontes\n', '> Quantas fontes há em cada licença.\n']
    L += [f"- {k}: {v} fontes" for k, v in lic.most_common()]
    escrever('docs/07-fontes-e-licencas.md', '\n'.join(L))


def readme(c: Ctx) -> None:
    cam = 'README.md'
    total = len(LINKS); unicos = len({chave(x['url']) for x in LINKS}); ness = sum(x['essencial'] for x in LINKS)
    nfontes = len({x['fonte'] for x in LINKS if not x['essencial']})
    tipos = collections.Counter(x['tipo'] for x in LINKS)
    n_ia = sum(1 for x in LINKS if x.get('ia')); n_ia_ess = sum(1 for x in LINKS if x.get('ia') and x['essencial'])
    n_repos, n_repos_unicos = len(REPOS), len({r['url'] for r in REPOS})
    nome, repo = CFG['nome'], CFG['repo']
    doc = lambda n: c.rel(cam, f'docs/{n}.md')
    v = dict(nome=nome, total=total, unicos=unicos, setores=len(SETOR), areas=len(AREA), trilhas=len(TRI), ia=n_ia, ia_ess=n_ia_ess,
             repos=n_repos, repos_unicos=n_repos_unicos, fontes=nfontes, idiomas=len(IDIOMAS), tudo=total + n_repos)
    secoes = ['comece', 'docs', 'setores', 'trilhas', 'ia', 'repos', 'numeros', 'scripts', 'regenerar', 'contribuir', 'licencas', 'aviso', 'stars']
    usados = set()
    anc = {k: gh_anchor(c.t(f'readme.{k}.titulo'), usados) for k in ['proposta', 'organizacao', 'traducao', 'indice'] + secoes}
    sec = lambda k: [f"## {c.t(f'readme.{k}.titulo')}\n", '> ' + c.t(f'readme.{k}.desc', **v) + '\n']
    L = [f'<p align="center">\n  <img src="{c.rel(cam, "images/logo.svg")}" alt="{nome}" width="160" height="160">\n</p>\n',
         f'<h1 align="center">{nome}</h1>\n', f"## {c.t('readme.proposta.titulo')}\n", '> ' + c.t('readme.proposta.desc', **v) + '\n',
         f"- 🗂️ [{c.t('nav.catalogo')}]({c.rel(cam, 'areas/CATALOGO.md')}): {c.t('readme.atalho.catalogo', **v)}",
         f"- 🧭 [{c.t('nav.trilhas')}]({c.rel(cam, 'trilhas/README.md')}): {c.t('readme.atalho.trilhas', **v)}",
         f"- 🧠 [{c.t('nav.profissoes')}]({c.rel(cam, 'ia/profissoes/README.md')}): {c.t('readme.atalho.profissoes', **v)}\n"]
    L += sec('organizacao') + sec('traducao')
    for cod, band, nome_id, clique, _ in IDIOMAS:
        alvo = os.path.relpath(J(Ctx.p_de(cod, cam)), os.path.dirname(J(c.p(cam)))).replace(os.sep, '/')
        L.append(f"{band}・**{nome_id} —** [{c.t('readme.traducao.este') if cod == c.lang else clique}]({alvo})<br>")
    L += ['', f"## {c.t('readme.indice.titulo')}\n", '> ' + c.t('readme.indice.desc') + '\n']
    L += [f"[{c.t(f'readme.{k}.titulo')}](#{anc[k]}) — {c.t(f'readme.{k}.indice')} <br>" for k in secoes]
    L += [''] + sec('comece')
    L += [f"- [🧭 **{c.t('readme.comece.profissao')}**]({c.rel(cam, 'trilhas/README.md')}): {c.t('readme.comece.profissao.desc')}",
          f"- [🗂️ **{c.t('readme.comece.assunto')}**]({c.rel(cam, 'areas/CATALOGO.md')}): {c.t('readme.comece.assunto.desc')}",
          f"- [🤖 **{c.t('readme.comece.ia')}**]({c.rel(cam, 'ia/README.md')}): {c.t('readme.comece.ia.desc')}",
          f"- [🧠 **{c.t('readme.comece.repos')}**]({c.rel(cam, 'ia/profissoes/README.md')}): {c.t('readme.comece.repos.desc')}",
          f"- [🎬 **{c.t('readme.comece.audiovisual')}**]({c.rel(cam, 'areas/criacao/recursos-audiovisuais.md')}): {c.t('readme.comece.audiovisual.desc')}",
          f"- [🧰 **{c.t('readme.comece.ferramentas')}**]({c.rel(cam, 'areas/ferramentas/README.md')}): {c.t('readme.comece.ferramentas.desc')}",
          f"- 🔎 {c.t('readme.comece.busca', csv=c.rel(cam, 'data/links.csv'))}\n"]
    L += sec('docs')
    for emoji, n, arq in (('🧭', '01', '01-como-usar'), ('🗺️', '02', '02-organizacao-e-taxonomia'), ('🥾', '03', '03-trilhas-por-profissao'),
                          ('📐', '04', '04-formato-dos-dados'), ('🕷️', '05', '05-coleta-com-scrapling'), ('🔍', '06', '06-curadoria-e-qualidade'),
                          ('⚖️', '07', '07-fontes-e-licencas'), ('🤝', '08', '08-como-contribuir'), ('🤖', '09', '09-ia-em-todas-as-areas')):
        L.append(f"- [{emoji} {n} · **{c.t(f'readme.doc.{n}')}**]({doc(arq)}) — {c.t(f'readme.doc.{n}.desc')}")
    L += [''] + sec('setores')
    for s in TAX['setores']:
        n = sum(len(POR_AREA.get(a['slug'], [])) for a in s['areas'])
        L.append(f"- [{s['emoji']} **{c.t(f'setor.{s['slug']}.nome')}**]({c.rel(cam, f'areas/{s['slug']}/README.md')}) — 🔗 {n}")
        L += [f"  - [{a['emoji']} {nome_area(c, a['slug'])}]({c.rel(cam, f'areas/{s['slug']}/{a['slug']}.md')}) — {c.t(f'area.{a['slug']}.descricao')}"
              for a in s['areas']]
    L += [''] + sec('trilhas')
    L += [f"- [{titulo_trilha(c, t)}]({c.rel(cam, 'trilhas/README.md')}#{gh_anchor(titulo_trilha(c, t), set())}) — {c.t(f'trilha.{t['slug']}.resumo')}" for t in TRI]
    L += [''] + sec('ia')
    L += [f"- [🤖 **{c.t('nav.ia')}**]({c.rel(cam, 'ia/README.md')}): {c.t('readme.ia.central')}",
          f"- 💡 {c.t('readme.ia.exemplos')} " + ' · '.join(f"[{nome_area(c, s_)}]({link_area(c, cam, s_)}#{ancora_ia(c, s_)})" for s_ in
                                                           ('edicao-de-video', 'trafego-pago', 'juridico', 'saude', 'educacao', 'qa-testes', 'contabilidade', 'design-ui-ux')) + '.\n']
    L += sec('repos')
    L += [f"- [{t['emoji']} {c.t(f'trilha.{t['slug']}.nome')}]({c.rel(cam, f'ia/profissoes/{t['slug']}.md')})" for t in TRI if REPOS]
    L += [''] + sec('numeros')
    L += [f"| {c.t('num.indicador')} | {c.t('num.valor')} |", '|---|---|',
          f"| 🔗 {c.t('num.total')} | {total} |", f"| 🧬 {c.t('num.unicos')} | {unicos} |", f"| 🗂️ {c.t('num.setores')} | {len(SETOR)} / {len(AREA)} |",
          f"| ⭐ {c.t('num.essenciais')} | {ness} |", f"| 🤖 {c.t('num.ia')} | {n_ia} |", f"| 🧠 {c.t('num.repos')} | {n_repos} ({n_repos_unicos}) |",
          f"| 📋 {c.t('num.fontes')} | {nfontes} |", f"| 🌍 {c.t('num.idiomas')} | {len(IDIOMAS)} |",
          f"| 🧾 {c.t('num.tipos')} | " + ' · '.join(f"{TIPO_EMOJI.get(k, '🔗')} {c.t('tipo.' + k)} {n}" for k, n in tipos.most_common()) + ' |', '',
          f"| {c.t('tab.setor')} | {c.t('tab.cobre')} | {c.t('tab.areas')} | 🔗 {c.t('tab.links')} |", '|---|---|:--:|:--:|']
    for s in TAX['setores']:
        L.append(f"| [{s['emoji']} {c.t(f'setor.{s['slug']}.nome')}]({c.rel(cam, f'areas/{s['slug']}/README.md')}) | {c.t(f'setor.{s['slug']}.descricao')} | "
                 f"{len(s['areas'])} | {sum(len(POR_AREA.get(a['slug'], [])) for a in s['areas'])} |")
    L += [''] + sec('scripts')
    L += [f"| {c.t('tab.script')} | {c.t('tab.faz')} |", '|---|---|']
    for sc in ('coletar', 'selecionar', 'coletar_repos_ia', 'descrever', 'traduzir', 'gerar', 'checar_links', 'validar'):
        arq = 'tests/validar.py' if sc == 'validar' else f'scripts/{sc}.py'
        L.append(f"| [`{arq}`]({c.rel(cam, arq)}) | {c.t(f'readme.script.{sc}')} |")
    L += [''] + sec('regenerar')
    L += ['```bash', 'python3 scripts/coletar.py            # → data/brutos.jsonl.gz', 'python3 scripts/descrever.py          # → data/descricoes.json',
          'python3 scripts/selecionar.py         # → data/links.jsonl', 'python3 scripts/coletar_repos_ia.py   # → data/repos-ia.jsonl',
          'python3 scripts/traduzir.py           # → data/i18n/desc.<idioma>.json.gz', 'python3 scripts/gerar.py              # → README*, areas/, trilhas/, ia/, i18n/',
          'python3 tests/validar.py              # → "OK"', '```\n']
    L += sec('contribuir')
    L += [f"- {c.t('readme.contribuir.novo')}", f"- {c.t('readme.contribuir.quebrado')}",
          f"- {c.t('readme.contribuir.passo', doc=doc('08-como-contribuir'), contributing=c.rel(cam, 'CONTRIBUTING.md'))}\n"]
    L += [f"## {c.t('readme.licencas.titulo')}\n", '> ' + c.t('readme.licencas.desc', doc=doc('07-fontes-e-licencas'), licenca=c.rel(cam, 'LICENSE'), **v) + '\n']
    L += sec('aviso') + sec('stars')
    L.append(f"[![Star History Chart](https://api.star-history.com/svg?repos={repo}&type=Date)](https://star-history.com/#{repo}&Date)")
    c.escrever(cam, L)


def csv_out() -> None:
    with open(J('data', 'links.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['setor', 'area', 'topico', 'nome', 'url', 'descricao', 'tipo', 'idioma', 'essencial', 'fonte'])
        for x in LINKS:
            w.writerow([AREA[x['area']]['setor'], x['area'], x['grupo'] or x['topico'], x['nome'], x['url'], x['descricao'],
                        x['tipo'], x.get('idioma', ''), 'sim' if x['essencial'] else '', x['fonte']])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--idiomas', default=','.join(CODIGOS), help='códigos separados por vírgula (padrão: todos)')
    idiomas = [i for i in ap.parse_args().idiomas.split(',') if i in CODIGOS]
    pt = textos_pt()
    for lang in idiomas:
        if lang != 'pt':
            shutil.rmtree(J('i18n', lang), ignore_errors=True)
        c = Ctx(lang, pt)
        for s in TAX['setores']:
            for a in s['areas']:
                pagina_area(c, a['slug'])
            pagina_setor(c, s)
        catalogo(c); trilhas(c); pagina_ia(c, DADOS, item_md); paginas_profissoes(c, DADOS); readme(c)
    fontes_doc(); csv_out()
    print(f"Gerado em {len(idiomas)} idioma(s): {len(AREA)} páginas de área, {len(SETOR)} setores, {len(TRI)} trilhas, "
          f"{len(LINKS)} links, {len(REPOS)} repositórios de IA por profissão.")


if __name__ == '__main__':
    main()
