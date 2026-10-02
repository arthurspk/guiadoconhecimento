<p align="center">
  <img src="./images/logo.svg" alt="Guia do Conhecimento" width="160" height="160">
</p>

<h1 align="center">Guia do Conhecimento</h1>

## :dart: A proposta

> O **Guia do Conhecimento** é um mapa de conhecimento aberto e gratuito: **17017 links** (15298 URLs únicas) organizados em **9 setores**, **71 áreas** e centenas de tópicos, para que **qualquer pessoa** encontre os melhores sites, cursos, ferramentas, repositórios, listas awesome, comunidades e utilitários da sua área: desenvolvimento, dados, segurança, design, edição de vídeo, cinema, fotografia, música, marketing, tráfego pago, vendas, finanças, direito, saúde, ciência, educação, idiomas e muito mais. Cada área começa com **essenciais escolhidos a dedo e descritos em português**, traz uma seção de **inteligência artificial aplicada àquela profissão** e segue com os links reunidos das melhores listas curadas da comunidade, com crédito a cada uma.

- 🗂️ [Catálogo de áreas](areas/CATALOGO.md): todas as 71 áreas, por setor, com a contagem de links.
- 🧭 [Trilhas por profissão](trilhas/README.md): 38 trilhas, de desenvolvedor(a) front-end a filmmaker, de gestor(a) de tráfego a professor(a).

## 💡 Como este guia é organizado

> Três níveis, do geral ao específico: **setor** (ex.: Design e Criação) → **área** (ex.: Edição de Vídeo) → **tópico** (ex.: Non-Linear Editors). Cada área é uma página com índice, uma seção **⭐ Comece por aqui** e os tópicos ordenados do maior para o menor. Tudo vem de uma base de dados aberta (`data/links.jsonl`) e é gerado por scripts em Python, então o guia inteiro pode ser regenerado, validado e ampliado. A organização segue a dos guias [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) e [guiadomaestri](https://github.com/arthurspk/guiadomaestri). Detalhes em [docs/02](docs/02-organizacao-e-taxonomia.md).

## 🌍 Tradução

> O guia está em **português (Brasil)**. As descrições dos essenciais e dos guias de origem brasileira estão em pt-BR; boa parte das demais vem das listas originais, em inglês. Quer traduzir o guia ou as descrições? Veja [docs/08 · Como contribuir](docs/08-como-contribuir.md).

🇧🇷・**Português (Brasil) —** [este arquivo](README.md)<br>

## 📚 Índice

[⭐ Comece por aqui](#-comece-por-aqui) — o caminho mais curto até o que você procura. <br>
[📖 Documentação](#-documentação) — como usar, como é organizado, como contribuir. <br>
[🗂️ Setores e áreas](#️-setores-e-áreas) — os 9 setores e todas as áreas. <br>
[🧭 Trilhas por profissão](#-trilhas-por-profissão) — por onde começar na sua carreira. <br>
[🤖 IA em todas as áreas](#-ia-em-todas-as-áreas) — inteligência artificial aplicada a cada profissão. <br>
[🔢 O guia em números](#-o-guia-em-números) — quantos links, de que tipo, de onde. <br>
[📜 Scripts disponíveis](#-scripts-disponíveis) — coletores, gerador e validadores em Python. <br>
[🛠️ Regenerar e validar](#️-regenerar-e-validar) — reconstruir e conferir tudo. <br>
[🤝 Contribuição](#-contribuição) — como sugerir links, áreas e traduções. <br>
[⚖️ Licenças e créditos](#️-licenças-e-créditos) — de onde vem cada link. <br>
[⚠️ Aviso](#️-aviso) — sobre links externos. <br>
[⭐ Star History](#-star-history) — o gráfico de estrelas do repositório. <br>

## ⭐ Comece por aqui

> Cinco atalhos, conforme o que você tem em mente.

- [🧭 **Sei a minha profissão**](trilhas/README.md): abra a trilha dela e siga as áreas na ordem.
- [🗂️ **Sei o assunto**](areas/CATALOGO.md): abra o catálogo e vá direto à área.
- [🤖 **Quero usar IA no meu trabalho**](ia/README.md): a seção de IA de cada profissão, num lugar só.
- [🧰 **Quero só boas ferramentas**](areas/ferramentas/README.md): ferramentas online, apps por sistema, extensões, APIs e recursos gratuitos.
- 🔎 **Procurando algo específico?** Use `Ctrl+F` na página da área, ou a busca do GitHub neste repositório. A base completa está em [`data/links.csv`](data/links.csv) para abrir em qualquer planilha.

## 📖 Documentação

> Os documentos do guia. Comece pelo 01 se é a sua primeira vez aqui.

- [🧭 01 · **Como usar este guia**](docs/01-como-usar.md) — navegação, símbolos e como estudar com ele.
- [🗺️ 02 · **Organização e taxonomia**](docs/02-organizacao-e-taxonomia.md) — setores, áreas, tópicos e por que estão assim.
- [🧭 03 · **Trilhas por profissão**](docs/03-trilhas-por-profissao.md) — como usar e criar trilhas; a lista está em [trilhas/](trilhas/README.md).
- [📐 04 · **Formato dos dados**](docs/04-formato-dos-dados.md) — os campos de `links.jsonl`, `fontes.json` e `essenciais.json`.
- [🕷️ 05 · **Coleta com Scrapling**](docs/05-coleta-com-scrapling.md) — como os links são coletados, verificados e atualizados.
- [🔍 06 · **Curadoria e qualidade**](docs/06-curadoria-e-qualidade.md) — critérios de entrada, saída, deduplicação e tetos por área.
- [⚖️ 07 · **Fontes e licenças**](docs/07-fontes-e-licencas.md) — todas as fontes, com crédito e licença.
- [🤝 08 · **Como contribuir**](docs/08-como-contribuir.md) — sugerir links, áreas, trilhas e traduções.
- [🤖 09 · **IA em todas as áreas**](docs/09-ia-em-todas-as-areas.md) — como a camada de IA é montada e como usar IA com responsabilidade.

## 🗂️ Setores e áreas

> 9 setores e 71 áreas. Cada setor tem uma página com o resumo das áreas e os primeiros essenciais de cada uma.

- [💻 **Tecnologia e Desenvolvimento**](areas/tecnologia/README.md) — 5024 links · [Fundamentos da Computação](areas/tecnologia/fundamentos-computacao.md) · [Linguagens de Programação](areas/tecnologia/linguagens.md) · [Front-end](areas/tecnologia/front-end.md) · [Back-end](areas/tecnologia/back-end.md) · [Mobile](areas/tecnologia/mobile.md) · [Desenvolvimento de Jogos](areas/tecnologia/games.md) · [DevOps e Cloud](areas/tecnologia/devops-cloud.md) · [Bancos de Dados](areas/tecnologia/bancos-de-dados.md) · [QA e Testes](areas/tecnologia/qa-testes.md) · [Arquitetura e Engenharia de Software](areas/tecnologia/arquitetura-software.md) · [Linux, Sistemas e Terminal](areas/tecnologia/sistemas-linux.md) · [Redes e Telecom](areas/tecnologia/redes.md) · [Embarcados, IoT e Hardware](areas/tecnologia/embarcados-iot.md) · [Blockchain e Web3](areas/tecnologia/blockchain-web3.md) · [Ferramentas para Desenvolvedores](areas/tecnologia/ferramentas-dev.md) · [Open Source](areas/tecnologia/open-source.md).
- [🤖 **Dados e Inteligência Artificial**](areas/dados-ia/README.md) — 1289 links · [Análise de Dados e BI](areas/dados-ia/analise-de-dados.md) · [Engenharia de Dados](areas/dados-ia/engenharia-de-dados.md) · [Ciência de Dados e Machine Learning](areas/dados-ia/ciencia-de-dados-ml.md) · [IA Generativa e LLMs](areas/dados-ia/ia-generativa.md) · [Datasets e Dados Abertos](areas/dados-ia/datasets.md).
- [🔒 **Segurança e Privacidade**](areas/seguranca/README.md) — 721 links · [Cibersegurança](areas/seguranca/ciberseguranca.md) · [OSINT e Investigação](areas/seguranca/osint.md) · [Privacidade e Proteção de Dados](areas/seguranca/privacidade.md).
- [🎬 **Design e Criação**](areas/criacao/README.md) — 1633 links · [Design UI/UX](areas/criacao/design-ui-ux.md) · [Design Gráfico e Ilustração](areas/criacao/design-grafico.md) · [Edição de Vídeo](areas/criacao/edicao-de-video.md) · [Filmmaking e Cinema](areas/criacao/filmmaking.md) · [Fotografia](areas/criacao/fotografia.md) · [Motion Design, 3D e Animação](areas/criacao/motion-3d.md) · [Áudio, Música e Podcast](areas/criacao/audio-musica.md) · [Escrita e Redação](areas/criacao/escrita.md).
- [📈 **Marketing e Vendas**](areas/marketing-vendas/README.md) — 1157 links · [Marketing Digital](areas/marketing-vendas/marketing-digital.md) · [Tráfego Pago](areas/marketing-vendas/trafego-pago.md) · [SEO](areas/marketing-vendas/seo.md) · [Social Media e Conteúdo](areas/marketing-vendas/social-media.md) · [Vendas e CRM](areas/marketing-vendas/vendas.md) · [E-commerce](areas/marketing-vendas/e-commerce.md).
- [💼 **Negócios e Gestão**](areas/negocios/README.md) — 1620 links · [Empreendedorismo e Startups](areas/negocios/empreendedorismo.md) · [Gestão de Produto](areas/negocios/produto.md) · [Gestão de Projetos e Agilidade](areas/negocios/gestao-de-projetos.md) · [Finanças e Investimentos](areas/negocios/financas.md) · [Contabilidade e Fiscal](areas/negocios/contabilidade.md) · [RH e Gestão de Pessoas](areas/negocios/rh-pessoas.md) · [Jurídico e Direito](areas/negocios/juridico.md) · [Atendimento e Customer Success](areas/negocios/atendimento-suporte.md).
- [🔬 **Ciência, Saúde e Educação**](areas/ciencia-educacao/README.md) — 2203 links · [Matemática e Estatística](areas/ciencia-educacao/matematica.md) · [Física e Astronomia](areas/ciencia-educacao/fisica-astronomia.md) · [Química](areas/ciencia-educacao/quimica.md) · [Biologia e Bioinformática](areas/ciencia-educacao/biologia.md) · [Medicina e Saúde](areas/ciencia-educacao/saude.md) · [Psicologia e Neurociência](areas/ciencia-educacao/psicologia.md) · [Economia](areas/ciencia-educacao/economia.md) · [Humanidades](areas/ciencia-educacao/humanidades.md) · [Idiomas](areas/ciencia-educacao/idiomas.md) · [Educação e Ensino](areas/ciencia-educacao/educacao.md) · [Pesquisa Acadêmica](areas/ciencia-educacao/pesquisa-academica.md).
- [🧭 **Carreira e Produtividade**](areas/carreira/README.md) — 997 links · [Carreira e Vagas](areas/carreira/carreira-vagas.md) · [Trabalho Remoto e Freelancer](areas/carreira/trabalho-remoto-freela.md) · [Produtividade e Organização](areas/carreira/produtividade.md) · [Comunidades, Eventos e Conteúdo](areas/carreira/comunidades.md) · [Acessibilidade](areas/carreira/acessibilidade.md).
- [🧰 **Ferramentas e Utilitários**](areas/ferramentas/README.md) — 2373 links · [Ferramentas Online](areas/ferramentas/ferramentas-online.md) · [Ferramentas de IA](areas/ferramentas/ferramentas-ia.md) · [Self-hosted](areas/ferramentas/self-hosted.md) · [Apps para macOS, Windows e Linux](areas/ferramentas/apps-sistemas.md) · [Apps para Android e iOS](areas/ferramentas/apps-celular.md) · [Extensões de Navegador](areas/ferramentas/extensoes-navegador.md) · [APIs Públicas](areas/ferramentas/apis-publicas.md) · [Recursos Gratuitos](areas/ferramentas/recursos-gratuitos.md) · [Automação e No-code](areas/ferramentas/automacao.md).

## 🧭 Trilhas por profissão

> Cada trilha junta as áreas que importam para uma profissão, na ordem em que vale a pena estudar.

[🎨 Desenvolvedor(a) Front-end](trilhas/README.md#-desenvolvedora-front-end) · [⚙️ Desenvolvedor(a) Back-end](trilhas/README.md#️-desenvolvedora-back-end) · [📱 Desenvolvedor(a) Mobile](trilhas/README.md#-desenvolvedora-mobile) · [🎮 Desenvolvedor(a) de Jogos](trilhas/README.md#-desenvolvedora-de-jogos) · [☁️ DevOps, SRE e Cloud](trilhas/README.md#️-devops-sre-e-cloud) · [✅ QA e Analista de Testes](trilhas/README.md#-qa-e-analista-de-testes) · [📊 Analista de Dados e BI](trilhas/README.md#-analista-de-dados-e-bi) · [🔀 Engenheiro(a) de Dados](trilhas/README.md#-engenheiroa-de-dados) · [🧠 Cientista de Dados e Engenheiro(a) de ML](trilhas/README.md#-cientista-de-dados-e-engenheiroa-de-ml) · [✨ Engenheiro(a) de IA e LLMs](trilhas/README.md#-engenheiroa-de-ia-e-llms) · [🛡️ Profissional de Segurança](trilhas/README.md#️-profissional-de-segurança) · [🖌️ Designer UI/UX](trilhas/README.md#️-designer-uiux) · [🖍️ Designer Gráfico e Ilustrador(a)](trilhas/README.md#️-designer-gráfico-e-ilustradora) · [🎞️ Editor(a) de Vídeo](trilhas/README.md#️-editora-de-vídeo) · [🎥 Filmmaker e Cineasta](trilhas/README.md#-filmmaker-e-cineasta) · [📷 Fotógrafo(a)](trilhas/README.md#-fotógrafoa) · [🧊 Motion Designer e Artista 3D](trilhas/README.md#-motion-designer-e-artista-3d) · [🎧 Produtor(a) Musical e Podcaster](trilhas/README.md#-produtora-musical-e-podcaster) · [✍️ Redator(a), Copywriter e Escritor(a)](trilhas/README.md#️-redatora-copywriter-e-escritora) · [🎯 Gestor(a) de Tráfego](trilhas/README.md#-gestora-de-tráfego) · [📣 Profissional de Marketing Digital](trilhas/README.md#-profissional-de-marketing-digital) · [📲 Social Media e Criador(a) de Conteúdo](trilhas/README.md#-social-media-e-criadora-de-conteúdo) · [🤝 Vendas e SDR](trilhas/README.md#-vendas-e-sdr) · [🛒 Lojista e Gestor(a) de E-commerce](trilhas/README.md#-lojista-e-gestora-de-e-commerce) · [🚀 Empreendedor(a)](trilhas/README.md#-empreendedora) · [📦 Product Manager](trilhas/README.md#-product-manager) · [🗂️ Gerente de Projetos e Agilista](trilhas/README.md#️-gerente-de-projetos-e-agilista) · [💰 Finanças, Investimentos e Contabilidade](trilhas/README.md#-finanças-investimentos-e-contabilidade) · [👥 RH e Recrutamento](trilhas/README.md#-rh-e-recrutamento) · [⚖️ Advogado(a) e Profissional Jurídico](trilhas/README.md#️-advogadoa-e-profissional-jurídico) · [🛟 Atendimento e Customer Success](trilhas/README.md#-atendimento-e-customer-success) · [🎓 Professor(a) e Educador(a)](trilhas/README.md#-professora-e-educadora) · [📚 Estudante (vestibular, faculdade, autodidata)](trilhas/README.md#-estudante-vestibular-faculdade-autodidata) · [🔬 Pesquisador(a) e Cientista](trilhas/README.md#-pesquisadora-e-cientista) · [🩺 Profissional de Saúde](trilhas/README.md#-profissional-de-saúde) · [🔌 Maker, Eletrônica e Robótica](trilhas/README.md#-maker-eletrônica-e-robótica) · [🏝️ Freelancer e Trabalhador(a) Remoto](trilhas/README.md#️-freelancer-e-trabalhadora-remoto) · [🧰 Qualquer pessoa: o essencial do dia a dia digital](trilhas/README.md#-qualquer-pessoa-o-essencial-do-dia-a-dia-digital)

## 🤖 IA em todas as áreas

> Toda página de área tem uma seção **🤖 IA para <área>**: 2327 links de IA no total, 718 deles essenciais escolhidos a dedo e descritos em português. Ferramentas da profissão, skills, plugins e MCPs para agentes (Claude, ChatGPT, Codex), cursos gratuitos, guias de prompt, regulação e uso responsável.

- [🤖 **IA para todas as áreas**](ia/README.md): a seção de IA de cada área, por setor, num lugar só.
- Exemplos: [Edição de Vídeo](areas/criacao/edicao-de-video.md#-ia-para-edição-de-vídeo) · [Tráfego Pago](areas/marketing-vendas/trafego-pago.md#-ia-para-tráfego-pago) · [Jurídico e Direito](areas/negocios/juridico.md#-ia-para-jurídico-e-direito) · [Medicina e Saúde](areas/ciencia-educacao/saude.md#-ia-para-medicina-e-saúde) · [Educação e Ensino](areas/ciencia-educacao/educacao.md#-ia-para-educação-e-ensino) · [QA e Testes](areas/tecnologia/qa-testes.md#-ia-para-qa-e-testes) · [Contabilidade e Fiscal](areas/negocios/contabilidade.md#-ia-para-contabilidade-e-fiscal) · [Design UI/UX](areas/criacao/design-ui-ux.md#-ia-para-design-uiux).

## 🔢 O guia em números

| Indicador | Valor |
|---|---|
| Links no total | 17017 |
| URLs únicas | 15298 |
| Setores / áreas | 9 / 71 |
| Essenciais escolhidos a dedo (pt-BR) | 1898 |
| Links de IA (seções 🤖 nas áreas) | 2327 |
| Listas curadas usadas como fonte | 397 |
| Links marcados como conteúdo em português | 1042 |
| Por tipo | site 9637 · repositório 4360 · documentação 662 · ferramenta 642 · vídeo 449 · curso 306 · comunidade 222 · app 180 · livro 178 · lista awesome 139 · canal 138 · artigo científico 104 |

| Setor | Áreas | Links |
|---|:--:|:--:|
| 💻 Tecnologia e Desenvolvimento | 16 | 5024 |
| 🤖 Dados e Inteligência Artificial | 5 | 1289 |
| 🔒 Segurança e Privacidade | 3 | 721 |
| 🎬 Design e Criação | 8 | 1633 |
| 📈 Marketing e Vendas | 6 | 1157 |
| 💼 Negócios e Gestão | 8 | 1620 |
| 🔬 Ciência, Saúde e Educação | 11 | 2203 |
| 🧭 Carreira e Produtividade | 5 | 997 |
| 🧰 Ferramentas e Utilitários | 9 | 2373 |

## 📜 Scripts disponíveis

> Tudo é gerado por Python. Detalhes em [`scripts/README.md`](scripts/README.md).

| Script | Tipo | O que faz |
|---|---|---|
| [`scripts/coletar.py`](scripts/coletar.py) | coletor | Baixa as listas curadas (Scrapling, com git como reserva) e extrai cada link com nome, descrição e tópico. |
| [`scripts/selecionar.py`](scripts/selecionar.py) | curadoria | Normaliza, deduplica, aplica a política de licenças e escolhe os links de cada área com teto e rodízio entre fontes. |
| [`scripts/gerar.py`](scripts/gerar.py) | gerador | Gera este README, as páginas de setor e de área, as trilhas, o catálogo e o CSV. |
| [`scripts/checar_links.py`](scripts/checar_links.py) | verificação | Confere se os links respondem (Scrapling ou urllib) e marca os quebrados. |
| [`tests/validar.py`](tests/validar.py) | validação | Confere dados, páginas, âncoras, duplicados e contagens. |

## 🛠️ Regenerar e validar

> Só a stdlib do Python 3 é obrigatória. O Scrapling (`pip install "scrapling[fetchers]"`) deixa a coleta e a checagem de links mais robustas.

```bash
python3 scripts/coletar.py        # → data/brutos.jsonl.gz (todas as fontes)
python3 scripts/selecionar.py     # → data/links.jsonl (base final)
python3 scripts/gerar.py          # → README, areas/, trilhas/, docs/07, data/links.csv
python3 scripts/checar_links.py   # → data/status-links.json (opcional, demora)
python3 tests/validar.py          # → "OK" se tudo estiver consistente
```

## 🤝 Contribuição

> Sugestões são muito bem-vindas: um link que faltou, uma área nova, uma trilha, uma tradução.

- **Link novo:** adicione em `data/essenciais.json` (se é essencial da área) ou sugira uma **lista curada** em `data/fontes.json`. Depois rode o gerador.
- **Link quebrado ou ruim:** abra uma issue com o endereço da página e o link.
- Passo a passo em [docs/08 · Como contribuir](docs/08-como-contribuir.md) e em [CONTRIBUTING.md](CONTRIBUTING.md).

## ⚖️ Licenças e créditos

> Os links vêm de **397 listas curadas** mantidas pela comunidade, listadas com licença em [docs/07](docs/07-fontes-e-licencas.md) e no rodapé de cada área. O conteúdo deste guia é **CC BY-SA 4.0** e os scripts são **MIT** (veja [LICENSE](LICENSE)). Descrições de fontes sem licença, GPL ou não comerciais não foram copiadas.

## ⚠️ Aviso

> Este guia aponta para sites de terceiros. Não há afiliação com nenhum deles, e o conteúdo de cada site é responsabilidade de quem o mantém. Links mudam: se encontrar um quebrado, avise. Conteúdo de segurança ofensiva é para estudo e uso **somente em escopo autorizado**.

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=arthurspk/guiadoconhecimento&type=Date)](https://star-history.com/#arthurspk/guiadoconhecimento&Date)
