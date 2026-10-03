#!/usr/bin/env python3
"""Páginas de IA: ia/README.md (IA em todas as áreas) e ia/profissoes/ (repositórios de IA por profissão).

Usado por gerar.py, que passa o contexto do idioma (base.Ctx) e os dados já carregados.
"""
import collections
from base import Ctx, carregar, esc, gh_anchor, limpa

CONSULTAS = carregar('repos-ia-consultas.json')


def estrelas(n: int) -> str:
    return f'{n / 1000:.1f}k' if n >= 1000 else str(n)


def repo_md(c: Ctx, r: dict) -> str:
    extra = [f"⭐ {estrelas(r['estrelas'])}"] + ([r['linguagem']] if r['linguagem'] else [])
    return f"- [{esc(r['nome'])}]({r['url']}) - {c.d(limpa(r['descricao']))} <sub>{' · '.join(extra)}</sub>"


def pagina_ia(c: Ctx, D: dict, item_md) -> None:
    cam = 'ia/README.md'
    TAX, AREA, POR_AREA, pular = D['TAX'], D['AREA'], D['POR_AREA'], D['SEM_IA_PROPRIA']
    links = [x for its in POR_AREA.values() for x in its]
    n_ia = sum(1 for x in links if x.get('ia')); n_ess = sum(1 for x in links if x.get('ia') and x['essencial'])
    area_md = lambda slug: c.rel(cam, f"areas/{AREA[slug]['setor']}/{slug}.md")
    tit_ia = lambda slug: c.t('ia_area.titulo', area=c.t(f'area.{slug}.nome'))
    L = [f"# 🤖 {c.t('nav.ia')}\n", '> ' + c.t('ia.intro', ia=n_ia, ess=n_ess) + '\n',
         f"[🏠 {c.t('nav.inicio')}]({c.rel(cam, 'README.md')}) · [🗂️ {c.t('nav.catalogo')}]({c.rel(cam, 'areas/CATALOGO.md')}) · "
         f"[🧠 {c.t('nav.profissoes')}]({c.rel(cam, 'ia/profissoes/README.md')}) · [📖 {c.t('ia.responsavel')}]({c.rel(cam, 'docs/09-ia-em-todas-as-areas.md')})\n",
         c.seletor(cam), f"## {c.t('indice.titulo')}\n", f"> {c.t('indice.desc')}\n"]
    usados = set(); gh_anchor(c.t('indice.titulo'), usados)
    L.append(f"[{c.t('ia.comecar.titulo')}](#{gh_anchor(c.t('ia.comecar.titulo'), usados)}) <br>")
    for s in TAX['setores']:
        tit = f"{s['emoji']} {c.t(f'setor.{s['slug']}.nome')}"
        L.append(f"[{tit}](#{gh_anchor(tit, usados)}) <br>")
    L += ['', f"## {c.t('ia.comecar.titulo')}\n", f"> {c.t('ia.comecar.desc')}\n"]
    for slug in pular:
        L += [item_md(c, x) for x in POR_AREA.get(slug, []) if x.get('ia') and x['essencial']]
    L.append('\n' + c.t('ia.fundo') + ' ' + ' · '.join(f"[{AREA[s_]['emoji']} {c.t(f'area.{s_}.nome')}]({area_md(s_)})" for s_ in pular) + '\n')
    for s in TAX['setores']:
        L += [f"## {s['emoji']} {c.t(f'setor.{s['slug']}.nome')}\n", '> ' + c.t('ia.setor.desc', setor=c.t(f'setor.{s['slug']}.nome')) + '\n',
              f"| {c.t('tab.area')} | 🤖 {c.t('tab.links_ia')} | {c.t('tab.secao')} |", '|---|:--:|---|']
        areas = [a for a in s['areas'] if a['slug'] not in pular]
        for a in areas:
            n = sum(1 for x in POR_AREA.get(a['slug'], []) if x.get('ia'))
            L.append(f"| {a['emoji']} {c.t(f'area.{a['slug']}.nome')} | {n} | [{tit_ia(a['slug'])}]({area_md(a['slug'])}#{gh_anchor(tit_ia(a['slug']), set())}) |")
        L.append(f"\n<details><summary>📌 {c.t('ia.tres')}</summary>\n")
        for a in areas:
            top = [x for x in POR_AREA.get(a['slug'], []) if x.get('ia') and x['essencial']][:3]
            if top:
                L += [f"**{a['emoji']} {c.t(f'area.{a['slug']}.nome')}**\n"] + [item_md(c, x) for x in top] + ['']
        L.append('</details>\n')
    c.escrever(cam, L)


def paginas_profissoes(c: Ctx, D: dict) -> None:
    """Uma página por trilha com os repositórios de IA daquela profissão, por tema, e o índice ia/profissoes/README.md."""
    if not D['REPOS']:
        return
    por_trilha = collections.defaultdict(list)
    for r in D['REPOS']:
        por_trilha[r['trilha']].append(r)
    total, unicos = len(D['REPOS']), len({r['url'] for r in D['REPOS']})
    idx = 'ia/profissoes/README.md'
    I = [f"# 🧠 {c.t('nav.profissoes')}\n", '> ' + c.t('prof.indice.intro', total=total, unicos=unicos, trilhas=len(por_trilha)) + '\n',
         f"[🏠 {c.t('nav.inicio')}]({c.rel(idx, 'README.md')}) · [🤖 {c.t('nav.ia')}]({c.rel(idx, 'ia/README.md')}) · "
         f"[🧭 {c.t('nav.trilhas')}]({c.rel(idx, 'trilhas/README.md')})\n", c.seletor(idx),
         f"## {c.t('prof.lista.titulo')}\n", f"> {c.t('prof.lista.desc')}\n",
         f"| {c.t('tab.profissao')} | 🧠 {c.t('tab.repos')} | 🎯 {c.t('tab.oficio')} | 🧰 {c.t('tab.gerais')} |", '|---|:--:|:--:|:--:|']
    for t in D['TRI']:
        repos = por_trilha.get(t['slug'], [])
        if not repos:
            continue
        nome = c.t(f"trilha.{t['slug']}.nome")
        proprios = sum(1 for r in repos if r['tema'] >= 0)
        I.append(f"| [{t['emoji']} **{nome}**](./{t['slug']}.md) | {len(repos)} | {proprios} | {len(repos) - proprios} |")
        pagina_profissao(c, t, repos, nome)
    I += [f"\n## {c.t('prof.como.titulo')}\n", f"> {c.t('prof.como.desc')}\n"]
    I += [f"- {c.t(f'prof.como.{n}')}" for n in (1, 2, 3, 4)]
    c.escrever(idx, I)


def pagina_profissao(c: Ctx, t: dict, repos: list, nome: str) -> None:
    slug = t['slug']; cam = f'ia/profissoes/{slug}.md'
    temas = CONSULTAS['trilhas'][slug]
    titulo = f"{t['emoji']} {c.t('prof.titulo', profissao=nome)}"
    blocos = []
    for n, (emoji, _, _, _) in enumerate(temas):
        its = [r for r in repos if r['tema'] == n]
        if its:
            blocos.append((f"{emoji} {c.t(f'tema.{slug}.{n}.nome')}", c.t(f'tema.{slug}.{n}.descricao'), its))
    gerais = [r for r in repos if r['tema'] < 0]
    if gerais:
        blocos.append((f"{CONSULTAS['geral']['emoji']} {c.t('tema.geral.nome')}", c.t('tema.geral.descricao'), gerais))
    L = [f"# {titulo}\n", '> ' + c.t(f'trilha.{slug}.resumo') + ' ' + c.t('prof.resumo', n=len(repos), temas=len(blocos)) + '\n',
         f"[← 🧠 {c.t('nav.profissoes')}](./README.md) · [🧭 {c.t('prof.trilha')}]({c.rel(cam, 'trilhas/README.md')}#{gh_anchor(t['emoji'] + ' ' + nome, set())}) · "
         f"[🏠 {c.t('nav.inicio')}]({c.rel(cam, 'README.md')})\n", c.seletor(cam),
         f"## {c.t('indice.titulo')}\n", f"> {c.t('indice.desc')}\n"]
    usados = set(); gh_anchor(titulo, usados); gh_anchor(c.t('indice.titulo'), usados)
    for tit, _, its in blocos:
        L.append(f"[{tit}](#{gh_anchor(tit, usados)}) <sub>{len(its)}</sub> <br>")
    L.append('')
    for tit, desc, its in blocos:
        L += [f"## {tit}\n", f"> {desc}\n"] + [repo_md(c, r) for r in its] + ['']
    L.append(f"---\n[⬆️ {c.t('nav.topo')}](#{gh_anchor(titulo, set())}) · [← {c.t('nav.profissoes')}](./README.md)")
    c.escrever(cam, L)
