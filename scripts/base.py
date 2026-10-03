#!/usr/bin/env python3
"""Base comum dos geradores: caminhos, idiomas, textos da interface, traduções e emojis.

O guia é gerado em 12 idiomas. O português fica na raiz (README.md, areas/, trilhas/, ia/);
os outros ficam em README.<idioma>.md e i18n/<idioma>/. docs/, data/ e scripts/ são únicos.
"""
import gzip, hashlib, json, os, re, unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)

# código, bandeira, nome do idioma, texto do link, código do pacote Argos
IDIOMAS = [
    ('pt', '🇧🇷', 'Português (Brasil)', 'este arquivo', 'pb'),
    ('en', '🇺🇸', 'English', 'Click Here', 'en'),
    ('es', '🇪🇸', 'Español', 'Clic aquí', 'es'),
    ('zh', '🇨🇳', '中文', '点击这里', 'zh'),
    ('hi', '🇮🇳', 'हिन्दी', 'यहाँ क्लिक करें', 'hi'),
    ('ar', '🇸🇦', 'العربية', 'اضغط هنا', 'ar'),
    ('fr', '🇫🇷', 'Français', 'Cliquez ici', 'fr'),
    ('it', '🇮🇹', 'Italiano', 'Clicca qui', 'it'),
    ('ko', '🇰🇷', '한국어', '여기 클릭', 'ko'),
    ('ru', '🇷🇺', 'Русский', 'Нажмите здесь', 'ru'),
    ('de', '🇩🇪', 'Deutsch', 'Hier klicken', 'de'),
    ('ja', '🇯🇵', '日本語', 'こちらをクリック', 'ja'),
]
CODIGOS = [i[0] for i in IDIOMAS]
UNICOS = ('docs/', 'data/', 'scripts/', 'tests/', 'images/', 'prompts/', 'LICENSE', 'CONTRIBUTING.md')

EMOJI = re.compile('[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U00002B00-\U00002BFF\U0001F1E6-\U0001F1FF️‍⃣]+')
PT = re.compile(r'\b(de|da|do|das|dos|para|com|que|em|uma|um|os|as|ou|não|sobre|você|seu|sua|mais|como|são|é|pelo|pela|aos|às|entre|e|o|ao|na|nas|nos|se|por|sem)\b|[ãõçáéíóúâêô]', re.I)
EN = re.compile(r'\b(the|for|and|with|of|to|an|in|is|your|that|from|on|by|are|using|this|it|as|at|be|or)\b', re.I)


def carregar(nome: str):
    return json.load(open(J('data', nome), encoding='utf-8'))


def limpa(texto: str) -> str:
    """Descrição pronta para a página: sem emoji, sem HTML, sem restos de tabela, uma linha, até 200 caracteres."""
    t = re.sub(r':[a-z0-9_+-]{2,30}:', ' ', texto or '')
    t = EMOJI.sub(' ', re.sub(r'<[^>]*>', ' ', t))
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'\s+', ' ', t.replace('|', '/').replace('[', '(').replace(']', ')').replace('`', '')).strip(' -–—:·•,/')
    if len(t) > 200:
        t = t[:200].rsplit(' ', 1)[0].rstrip(' ,;:-') + '…'
    return t


def idioma_de(texto: str) -> str:
    """'pt' ou 'en' (o que não parece português é tratado como inglês para a tradução)."""
    return 'pt' if len(PT.findall(texto)) > len(EN.findall(texto)) else 'en'


def h(texto: str) -> str:
    return hashlib.sha1(texto.encode('utf-8')).hexdigest()[:14]


def gh_anchor(texto: str, usados: set) -> str:
    """Âncora no formato do GitHub (emoji some, espaço vira hífen)."""
    t = texto.strip().lower()
    t = ''.join(c for c in t if c in ' -_' or unicodedata.category(c)[0] in 'LMN' or unicodedata.category(c) == 'Pc')
    t = t.replace(' ', '-')
    base, n = t, 1
    while t in usados:
        t = f'{base}-{n}'; n += 1
    usados.add(t)
    return t


def esc(s: str) -> str:
    return s.replace('[', '(').replace(']', ')').replace('|', '/').strip()


def escrever(caminho: str, texto: str) -> None:
    os.makedirs(os.path.dirname(J(caminho)) or RAIZ, exist_ok=True)
    open(J(caminho), 'w', encoding='utf-8').write(texto.rstrip() + '\n')


def textos_derivados() -> dict:
    """Textos da interface que vêm dos dados (setores, áreas, trilhas e temas de IA), em português."""
    tax, tri, cons = carregar('taxonomia.json'), carregar('trilhas.json')['trilhas'], carregar('repos-ia-consultas.json')
    d = {}
    for s in tax['setores']:
        d[f"setor.{s['slug']}.nome"], d[f"setor.{s['slug']}.descricao"] = s['nome'], s['descricao']
        for a in s['areas']:
            d[f"area.{a['slug']}.nome"], d[f"area.{a['slug']}.descricao"] = a['nome'], a['descricao']
    for t in tri:
        d[f"trilha.{t['slug']}.nome"], d[f"trilha.{t['slug']}.resumo"] = t['nome'], t['resumo']
        for n, (_, nome, desc, _) in enumerate(cons['trilhas'].get(t['slug'], [])):
            d[f"tema.{t['slug']}.{n}.nome"], d[f"tema.{t['slug']}.{n}.descricao"] = nome, desc
    d['tema.geral.nome'], d['tema.geral.descricao'] = cons['geral']['nome'], cons['geral']['descricao']
    return d


def textos_pt() -> dict:
    return {**carregar('i18n/textos.pt.json'), **textos_derivados()}


class Ctx:
    """Contexto de um idioma: caminhos de saída, textos da interface e traduções das descrições."""

    def __init__(self, lang: str, pt: dict):
        self.lang, self.pt = lang, pt
        arq = J('data', 'i18n', f'textos.{lang}.json')
        self.ui = pt if lang == 'pt' else (json.load(open(arq, encoding='utf-8')) if os.path.exists(arq) else {})
        arq = J('data', 'i18n', f'desc.{lang}.json.gz')
        self.td = json.load(gzip.open(arq, 'rt', encoding='utf-8')) if os.path.exists(arq) else {}

    def p(self, caminho: str) -> str:
        """Caminho real de uma página lógica neste idioma."""
        if self.lang == 'pt' or caminho.startswith(UNICOS):
            return caminho
        return f'README.{self.lang}.md' if caminho == 'README.md' else f'i18n/{self.lang}/{caminho}'

    def rel(self, de: str, para: str) -> str:
        return os.path.relpath(J(self.p(para)), os.path.dirname(J(self.p(de)))).replace(os.sep, '/')

    def t(self, chave: str, **kw) -> str:
        s = self.ui.get(chave) or self.pt[chave]
        try:
            return s.format(**kw) if kw else s
        except (KeyError, IndexError, ValueError):   # tradução que perdeu um marcador: cai para o português
            return self.pt[chave].format(**kw)

    def d(self, texto: str) -> str:
        """Descrição (ou nome de tópico) no idioma da página; sem tradução, fica o original."""
        return self.td.get(h(texto), texto) if texto else texto

    def escrever(self, caminho: str, linhas: list) -> None:
        escrever(self.p(caminho), '\n'.join(linhas))

    def seletor(self, caminho: str) -> str:
        """Linha com o mesmo documento nos outros idiomas."""
        partes = []
        for cod, band, nome, _, _ in IDIOMAS:
            if cod == self.lang:
                partes.append(f'{band} **{nome}**')
            else:
                alvo = os.path.relpath(J(Ctx.p_de(cod, caminho)), os.path.dirname(J(self.p(caminho)))).replace(os.sep, '/')
                partes.append(f'{band} [{nome}]({alvo})')
        return '🌍 ' + ' · '.join(partes) + '\n'

    @staticmethod
    def p_de(lang: str, caminho: str) -> str:
        if lang == 'pt':
            return caminho
        return f'README.{lang}.md' if caminho == 'README.md' else f'i18n/{lang}/{caminho}'


# ---------- emojis ----------
TIPO_EMOJI = {'site': '🌐', 'repositorio': '📦', 'awesome': '📋', 'curso': '🎓', 'canal': '📺', 'video': '🎬', 'livro': '📚',
              'comunidade': '👥', 'documentacao': '📖', 'ferramenta': '🛠️', 'app': '📱', 'artigo': '📄'}
TIPOS_COM_ROTULO = ('curso', 'canal', 'livro', 'awesome', 'comunidade', 'app', 'artigo', 'video', 'documentacao')

# palavra (em inglês ou português, no nome do tópico) → emoji; a primeira que casar vence
TOPICO_EMOJI = [
    (r'smart contract|blockchain|web3|ethereum|bitcoin|solidity|nft|defi', '⛓️'),
    (r'ia\b|ai\b|artificial|machine learning|deep learning|llm|gpt|neural', '🤖'), (r'font|tipograf|typograph', '🔤'),
    (r'luts?\b|color|cor(es)?\b|grading|palette|paleta', '🎨'), (r'sfx|sound|som\b|sonor', '🔊'), (r'v[ií]deo|film|cinema|movie|youtube', '🎞️'),
    (r'music|música|audio|áudio|song', '🎵'), (r'podcast', '🎙️'), (r'photo|foto|image|imagem|imagens|picture', '📷'),
    (r'icon|ícone|emoji', '🔣'), (r'illustrat|ilustra|draw|desenh|art\b|arte', '🖍️'), (r'3d|blender|render|model', '🧊'),
    (r'animat|anima|motion|effect|efeito|transi|overlay|vfx', '✨'), (r'template|preset|mockup|boilerplate|starter', '🧩'),
    (r'book|livro|ebook|reading|leitura', '📚'), (r'course|curso|mooc|class|aula|bootcamp|learn|aprend|tutori|training|treinamento', '🎓'),
    (r'channel|canal|canais|talk|palestra|conference|conferência|evento|event|meetup', '📺'), (r'newsletter|blog|article|artigo|post|news|notícia|magazine|revista', '📰'),
    (r'communit|comunidade|forum|fórum|discord|slack|telegram|grupo', '👥'), (r'job|vaga|career|carreira|hiring|interview|entrevista|resume|currículo', '💼'),
    (r'secur|segur|pentest|hack|malware|exploit|vulnerab|crypto(graphy)?|criptograf|privac', '🔒'), (r'test|qa\b|quality|qualidade|debug|lint', '✅'),
    (r'database|banco|sql|data ?base|storage|armazen', '🗄️'), (r'data|dado|analytic|análise|statistic|estatíst|visualiz|chart|gráfico|dashboard', '📊'),
    (r'cloud|nuvem|aws|azure|gcp|kubernetes|docker|container|deploy|devops|infra|server|servidor|hosting|hosped', '☁️'),
    (r'network|rede|http|dns|vpn|proxy|protocol', '🌐'), (r'api|sdk|integration|integra|webhook', '🔌'),
    (r'mobile|android|ios|iphone|app\b|apps\b|aplicativ', '📱'), (r'game|jogo|gaming|unity|unreal|godot', '🎮'),
    (r'web|frontend|front-end|html|css|javascript|react|vue|browser|navegador|extension|extens', '🕸️'),
    (r'linux|unix|shell|terminal|cli\b|command|bash|system|sistema|kernel|windows|macos', '🖥️'),
    (r'hardware|iot|arduino|raspberry|embedded|embarcad|robot|electron|eletrôn|sensor', '🔧'),
    (r'framework|librar|bibliotec|package|pacote|plugin|module|módulo|component', '🧱'), (r'tool|ferrament|utilit|generator|gerador|editor|ide\b', '🛠️'),
    (r'design|ui\b|ux\b|interface|layout|prototyp|wirefram', '🖌️'), (r'market|seo|ads?\b|anúncio|campaign|campanha|growth|social|email', '📣'),
    (r'sale|venda|crm|customer|cliente|support|suporte|atendimento', '🤝'), (r'financ|money|dinheiro|invest|payment|pagamento|bank|banco|tax|imposto|contab|account', '💰'),
    (r'legal|law|lei\b|leis|juríd|direito|contract|contrato|licen|compliance', '⚖️'), (r'health|saúde|medic|médic|clinic|clínic|bio|genom|nutri', '🩺'),
    (r'math|matemát|physic|físic|chem|quím|science|ciência|astro|research|pesquisa|paper|academic|acadêm', '🔬'),
    (r'language|idioma|língua|english|inglês|translat|tradu|grammar|gramát|dictionar|dicionár|writing|escrita|redação', '🗣️'),
    (r'education|educa|school|escola|teach|ensin|student|estud|universit', '🏫'), (r'product|produto|project|projeto|manage|gest|agile|ágil|scrum|kanban|planning', '🗂️'),
    (r'startup|business|negóc|entrepreneur|empreend|company|empresa', '🚀'), (r'productiv|produtiv|note|nota|todo|task|tarefa|calendar|time|tempo', '⏱️'),
    (r'automat|workflow|bot\b|bots\b|script|scrap', '⚙️'), (r'free|grát|gratuit|open source|código aberto|resource|recurso|stock', '🎁'),
    (r'docs?\b|documenta|reference|referência|guide|guia|cheat ?sheet|handbook|manual|roadmap', '📖'), (r'dataset|corpus|benchmark', '🧮'),
    (r'self-?host|homelab|backup|monitor|log', '🏠'), (r'access|acessib|a11y|inclus', '♿'), (r'remote|remoto|freelanc|nomad', '🏝️'),
    (r'blockchain|web3|ethereum|bitcoin|solidity|nft|defi', '⛓️'), (r'history|histór|philosoph|filosof|sociolog|geograf|politic|polític|human', '🏛️'),
    (r'psycholog|psicolog|mental|mind|mente|cognit', '🧠'), (r'econom', '📈'), (r'compiler|algorithm|algoritm|structure|estrutura|theory|teoria|architecture|arquitetura|pattern|padr', '🧮'),
]
TOPICO_EMOJI = [(re.compile(rf'\b(?:{rx})', re.I), e) for rx, e in TOPICO_EMOJI]   # casa só no começo de palavra
RESERVA = ['🔹', '🔸', '🟢', '🟣', '🟠', '🔷', '🔶', '🟡', '🟤', '🔵']


def emoji_topico(nome: str) -> str:
    for rx, e in TOPICO_EMOJI:
        if rx.search(nome):
            return e
    return RESERVA[int(h(nome), 16) % len(RESERVA)]
