<p align="center">
  <img src="images/logo.svg" alt="Guia do Conhecimento" width="160" height="160">
</p>

<h1 align="center">Guia do Conhecimento</h1>

## 🎯 목적

> **Guia do Conhecimento**는 개방형 무료 지식 지도입니다. **9개 부문**, **72개 영역**, **38개 직업**에 걸쳐 **55357개 링크**를 정리하여, **누구나** 자기 분야의 가장 좋은 사이트, 강좌, 도구, 저장소, awesome 리스트, 커뮤니티, 유틸리티를 찾을 수 있게 합니다. 개발, 데이터, 보안, 디자인, 영상 편집, 영화, 사진, 음악, 마케팅, 유료 트래픽, 영업, 금융, 법률, 보건, 과학, 교육, 외국어 등 폭넓은 분야를 다룹니다. 각 영역은 **엄선한 필수 링크**로 시작하여 **해당 직업에 적용한 인공지능** 섹션을 두고, 커뮤니티가 큐레이션한 최고의 목록에서 모은 링크로 이어집니다. 직업마다 **AI 저장소 1000개**도 있습니다. 모든 링크에는 설명이 있으며, 가이드 전체가 **12개 언어**로 제공됩니다.

- 🗂️ [영역 카탈로그](i18n/ko/areas/CATALOGO.md): 72개 영역 전체를 부문별로, 링크 수와 함께 보여줍니다.
- 🧭 [직업별 학습 경로](i18n/ko/trilhas/README.md): 프런트엔드 개발자부터 영상 제작자, 트래픽 매니저, 교사까지 38개의 학습 경로.
- 🧠 [직업별 AI 저장소](i18n/ko/ia/profissoes/README.md): AI 저장소 38000개, 직업당 1000개.

## 💡 이 가이드의 구성

> 일반에서 구체로 가는 세 단계입니다. **부문**(예: 디자인과 창작) → **영역**(예: 영상 편집) → **주제**(예: 비선형 편집기). 각 영역은 목차, **⭐ 여기서 시작하세요** 섹션, **🤖 AI** 섹션, 그리고 큰 주제부터 작은 주제 순으로 정렬되고 각각 설명이 달린 주제들로 이루어진 하나의 페이지입니다. 모든 내용은 공개 데이터베이스(`data/links.jsonl`)에서 나오며 Python 스크립트로 생성되므로, 가이드 전체를 다시 생성하고 검증하고 확장할 수 있습니다. 구성 방식은 [guiadevbrasil](https://github.com/arthurspk/guiadevbrasil)과 [guiadomaestri](https://github.com/arthurspk/guiadomaestri) 가이드를 따릅니다.

## 🌍 번역

> 이 가이드를 다른 언어로 보려면 아래에서 선택하세요. 각 언어에서 페이지, 섹션, 링크별 설명이 해당 언어로 표시됩니다. 설명은 자동 번역이므로 오류를 바로잡는 데 참여해 주시면 커뮤니티에 큰 도움이 됩니다. `docs/`의 상세 문서는 포르투갈어로 되어 있습니다.

🇧🇷・**Português (Brasil) —** [este arquivo](README.md)<br>
🇺🇸・**English —** [Click Here](README.en.md)<br>
🇪🇸・**Español —** [Clic aquí](README.es.md)<br>
🇨🇳・**中文 —** [点击这里](README.zh.md)<br>
🇮🇳・**हिन्दी —** [यहाँ क्लिक करें](README.hi.md)<br>
🇸🇦・**العربية —** [اضغط هنا](README.ar.md)<br>
🇫🇷・**Français —** [Cliquez ici](README.fr.md)<br>
🇮🇹・**Italiano —** [Clicca qui](README.it.md)<br>
🇰🇷・**한국어 —** [이 파일](README.ko.md)<br>
🇷🇺・**Русский —** [Нажмите здесь](README.ru.md)<br>
🇩🇪・**Deutsch —** [Hier klicken](README.de.md)<br>
🇯🇵・**日本語 —** [こちらをクリック](README.ja.md)<br>

## 📚 목차

> 이 페이지의 섹션을 나타나는 순서대로 나열했습니다.

[⭐ 여기서 시작하세요](#-여기서-시작하세요) — 찾는 것에 가장 빨리 다가가는 길. <br>
[📖 문서](#-문서) — 사용법, 구성, 기여 방법. <br>
[🗂️ 부문과 영역](#️-부문과-영역) — 부문과 모든 영역. <br>
[🧭 직업별 학습 경로](#-직업별-학습-경로) — 커리어를 어디서 시작할지. <br>
[🤖 모든 영역의 AI](#-모든-영역의-ai) — 각 직업에 적용한 인공지능. <br>
[🧠 직업별 AI 저장소 1000개](#-직업별-ai-저장소-1000개) — 각 직업의 AI 저장소, 새로운 도구, 자동화. <br>
[🔢 숫자로 보는 가이드](#-숫자로-보는-가이드) — 링크 수, 유형, 출처. <br>
[📜 제공되는 스크립트](#-제공되는-스크립트) — Python으로 작성한 수집기, 번역기, 생성기, 검증기. <br>
[🛠️ 재생성과 검증](#️-재생성과-검증) — 전체를 다시 빌드하고 확인하기. <br>
[🤝 기여](#-기여) — 링크, 영역, 번역을 제안하는 방법. <br>
[⚖️ 라이선스와 크레딧](#️-라이선스와-크레딧) — 각 링크의 출처. <br>
[⚠️ 안내](#️-안내) — 외부 링크에 대하여. <br>
[🌟 Star History](#-star-history) — 저장소의 스타 그래프. <br>

## ⭐ 여기서 시작하세요

> 생각하고 있는 바에 따른 일곱 가지 바로가기입니다.

- [🧭 **내 직업을 알고 있어요**](i18n/ko/trilhas/README.md): 해당 학습 경로를 열고 영역을 순서대로 따라가세요.
- [🗂️ **주제를 알고 있어요**](i18n/ko/areas/CATALOGO.md): 카탈로그를 열어 바로 해당 영역으로 가세요.
- [🤖 **업무에 AI를 쓰고 싶어요**](i18n/ko/ia/README.md): 모든 직업의 AI 섹션을 한곳에서.
- [🧠 **내 직업을 위한 AI 저장소가 필요해요**](i18n/ko/ia/profissoes/README.md): 직업당 저장소 1000개, 주제별로 정리.
- [🎬 **영상·음향 분야에서 일해요**](i18n/ko/areas/criacao/recursos-audiovisuais.md): LUTs, 이펙트, 트랜지션, 프리셋, 폰트, 효과음, 무료 음악, stock footage.
- [🧰 **좋은 도구만 보고 싶어요**](i18n/ko/areas/ferramentas/README.md): 온라인 도구, 시스템별 앱, 확장 프로그램, API, 무료 자료.
- 🔎 **특정한 것을 찾고 있나요?** 영역 페이지에서 `Ctrl+F`를 쓰거나 이 저장소에서 GitHub 검색을 사용하세요. 전체 데이터베이스는 [`data/links.csv`](data/links.csv)에 있어 어떤 스프레드시트로든 열 수 있습니다.

## 📖 문서

> 가이드의 문서들입니다. 처음이라면 01부터 시작하세요.

- [🧭 01 · **이 가이드 사용법**](docs/01-como-usar.md) — 탐색 방법, 기호, 이 가이드로 공부하는 방법.
- [🗺️ 02 · **구성과 분류 체계**](docs/02-organizacao-e-taxonomia.md) — 부문, 영역, 주제와 그렇게 나눈 이유.
- [🥾 03 · **직업별 학습 경로**](docs/03-trilhas-por-profissao.md) — 학습 경로를 사용하고 만드는 방법.
- [📐 04 · **데이터 형식**](docs/04-formato-dos-dados.md) — `data/`의 각 파일에 있는 필드.
- [🕷️ 05 · **Scrapling으로 수집하기**](docs/05-coleta-com-scrapling.md) — 링크를 수집, 검증, 업데이트하는 방법.
- [🔍 06 · **큐레이션과 품질**](docs/06-curadoria-e-qualidade.md) — 포함·제외 기준, 중복 제거, 영역별 상한.
- [⚖️ 07 · **출처와 라이선스**](docs/07-fontes-e-licencas.md) — 모든 출처와 크레딧, 라이선스.
- [🤝 08 · **기여 방법**](docs/08-como-contribuir.md) — 링크, 영역, 학습 경로, 번역 제안하기.
- [🤖 09 · **모든 영역의 AI**](docs/09-ia-em-todas-as-areas.md) — AI 계층이 구성되는 방식과 AI를 책임감 있게 사용하는 방법.

## 🗂️ 부문과 영역

> 9개 부문과 72개 영역. 각 부문에는 영역 요약과 영역별 첫 필수 링크를 담은 페이지가 있습니다.

- [💻 **기술과 개발**](i18n/ko/areas/tecnologia/README.md) — 🔗 5051
  - [🧮 컴퓨터 과학 기초](i18n/ko/areas/tecnologia/fundamentos-computacao.md) — 알고리즘, 자료구조, 운영체제, 컴파일러, 이론.
  - [🔤 프로그래밍 언어](i18n/ko/areas/tecnologia/linguagens.md) — Python, JavaScript, Java, Go, Rust, C#, PHP, Kotlin, Swift 등 수십 가지 언어.
  - [🎨 프런트엔드](i18n/ko/areas/tecnologia/front-end.md) — HTML, CSS, JavaScript, 프레임워크, 접근성, 웹 성능.
  - [⚙️ 백엔드](i18n/ko/areas/tecnologia/back-end.md) — API, 서버 프레임워크, 인증, 큐, 마이크로서비스.
  - [📱 모바일](i18n/ko/areas/tecnologia/mobile.md) — Android, iOS, Flutter, React Native, 스토어 배포.
  - [🎮 게임 개발](i18n/ko/areas/tecnologia/games.md) — 엔진, 그래픽, 게임 디자인, 에셋, 게임 프로그래밍.
  - [☁️ DevOps와 클라우드](i18n/ko/areas/tecnologia/devops-cloud.md) — CI/CD, 컨테이너, Kubernetes, IaC, AWS, Azure, GCP, SRE.
  - [🗄️ 데이터베이스](i18n/ko/areas/tecnologia/bancos-de-dados.md) — SQL, NoSQL, 모델링, 최적화, 관리.
  - [✅ QA와 테스트](i18n/ko/areas/tecnologia/qa-testes.md) — 자동화 테스트, 수동 테스트, 성능, 모바일, 소프트웨어 품질.
  - [🏛️ 소프트웨어 아키텍처와 엔지니어링](i18n/ko/areas/tecnologia/arquitetura-software.md) — 시스템 설계, 패턴, 클린 코드, DDD, 확장성.
  - [🐧 Linux, 시스템, 터미널](i18n/ko/areas/tecnologia/sistemas-linux.md) — Linux, 셸, 시스템 관리, 커맨드 라인.
  - [🌐 네트워크와 통신](i18n/ko/areas/tecnologia/redes.md) — 프로토콜, 네트워크 인프라, SDN, 통신.
  - [🔌 임베디드, IoT, 하드웨어](i18n/ko/areas/tecnologia/embarcados-iot.md) — Arduino, Raspberry Pi, 전자공학, 로보틱스, 펌웨어.
  - [⛓️ 블록체인과 Web3](i18n/ko/areas/tecnologia/blockchain-web3.md) — 스마트 컨트랙트, Ethereum, 응용 암호학, 분산 시스템.
  - [🛠️ 개발자 도구](i18n/ko/areas/tecnologia/ferramentas-dev.md) — 에디터, Git, 터미널, 생산성, 개발 유틸리티.
  - [🌱 오픈 소스](i18n/ko/areas/tecnologia/open-source.md) — 기여하는 방법, 프로젝트 찾기, 자유 소프트웨어 유지 관리.
- [🤖 **데이터와 인공지능**](i18n/ko/areas/dados-ia/README.md) — 🔗 1289
  - [📊 데이터 분석과 BI](i18n/ko/areas/dados-ia/analise-de-dados.md) — Excel, 분석용 SQL, 대시보드, 시각화, 비즈니스 인텔리전스.
  - [🔀 데이터 엔지니어링](i18n/ko/areas/dados-ia/engenharia-de-dados.md) — 파이프라인, ETL, 데이터 레이크, 스트리밍, 오케스트레이션.
  - [🧠 데이터 과학과 machine learning](i18n/ko/areas/dados-ia/ciencia-de-dados-ml.md) — 통계, 전통적 ML, 딥러닝, 컴퓨터 비전, NLP.
  - [✨ 생성형 AI와 LLM](i18n/ko/areas/dados-ia/ia-generativa.md) — LLM, 에이전트, 프롬프트, RAG, MCP, AI 도구.
  - [🗃️ 데이터셋과 공공 데이터](i18n/ko/areas/dados-ia/datasets.md) — 공개 데이터, 정부 공공 데이터, 학습용 데이터셋.
- [🔒 **보안과 개인정보 보호**](i18n/ko/areas/seguranca/README.md) — 🔗 722
  - [🛡️ 사이버 보안](i18n/ko/areas/seguranca/ciberseguranca.md) — 침투 테스트, 블루팀, CTF, 악성코드, 포렌식, 버그 바운티.
  - [🔎 OSINT와 조사](i18n/ko/areas/seguranca/osint.md) — 공개 출처 정보 수집과 조사 기법.
  - [🕶️ 개인정보 보호](i18n/ko/areas/seguranca/privacidade.md) — 디지털 프라이버시, LGPD/GDPR, 보호 도구.
- [🎬 **디자인과 창작**](i18n/ko/areas/criacao/README.md) — 🔗 1895
  - [🖌️ UI/UX 디자인](i18n/ko/areas/criacao/design-ui-ux.md) — 인터페이스 디자인, UX 리서치, 디자인 시스템, 프로토타이핑.
  - [🖍️ 그래픽 디자인과 일러스트](i18n/ko/areas/criacao/design-grafico.md) — 타이포그래피, 색상, 브랜드 아이덴티티, 일러스트, 그래픽 소스.
  - [🎞️ 영상 편집](i18n/ko/areas/criacao/edicao-de-video.md) — 편집 소프트웨어, color grading, 자막, 코덱, 후반 작업 워크플로.
  - [🎥 영화 제작](i18n/ko/areas/criacao/filmmaking.md) — 시나리오, 연출, 영화 촬영, 제작, 배급.
  - [🪄 영상·음향 소스](i18n/ko/areas/criacao/recursos-audiovisuais.md) — LUTs, 이펙트, 트랜지션, 프리셋, 오버레이, 폰트, 효과음, 무료 음악, stock footage.
  - [📷 사진](i18n/ko/areas/criacao/fotografia.md) — 기법, 편집, 장비, 이미지 스톡 사이트.
  - [🧊 모션 디자인, 3D, 애니메이션](i18n/ko/areas/criacao/motion-3d.md) — Blender, 모션 그래픽, 2D/3D 애니메이션, 시각 효과.
  - [🎧 오디오, 음악, 팟캐스트](i18n/ko/areas/criacao/audio-musica.md) — 음악 제작, DAW, 플러그인, 믹싱, 팟캐스트.
  - [✍️ 글쓰기](i18n/ko/areas/criacao/escrita.md) — 작문, 카피라이팅, 기술 문서 작성, 교정, 출판.
- [📈 **마케팅과 영업**](i18n/ko/areas/marketing-vendas/README.md) — 🔗 1170
  - [📣 디지털 마케팅](i18n/ko/areas/marketing-vendas/marketing-digital.md) — 전략, 퍼널, 이메일 마케팅, 자동화, 그로스.
  - [🎯 유료 트래픽](i18n/ko/areas/marketing-vendas/trafego-pago.md) — Google Ads, Meta Ads, TikTok Ads, LinkedIn Ads, 성과 측정, 광고 소재.
  - [🔍 SEO](i18n/ko/areas/marketing-vendas/seo.md) — 기술적 SEO, 콘텐츠, 링크 빌딩, 분석 도구.
  - [📲 소셜 미디어와 콘텐츠](i18n/ko/areas/marketing-vendas/social-media.md) — 소셜 미디어, 콘텐츠 제작, 크리에이터, 예약 게시.
  - [🤝 영업과 CRM](i18n/ko/areas/marketing-vendas/vendas.md) — 고객 발굴, 협상, CRM, 영업 운영.
  - [🛒 이커머스](i18n/ko/areas/marketing-vendas/e-commerce.md) — 온라인 쇼핑몰, 플랫폼, 결제, 물류, 마켓플레이스.
- [💼 **비즈니스와 경영**](i18n/ko/areas/negocios/README.md) — 🔗 1622
  - [🚀 창업과 스타트업](i18n/ko/areas/negocios/empreendedorismo.md) — 사업 시작과 확장, 투자 유치, 비즈니스 모델, SaaS.
  - [📦 프로덕트 매니지먼트](i18n/ko/areas/negocios/produto.md) — 디스커버리, 로드맵, 지표, 프로덕트 매니지먼트 실무.
  - [🗂️ 프로젝트 관리와 애자일](i18n/ko/areas/negocios/gestao-de-projetos.md) — Scrum, Kanban, PMBOK, 도구, 팀 리더십.
  - [💰 금융과 투자](i18n/ko/areas/negocios/financas.md) — 개인 재무, 투자, 금융 시장, 기업 재무.
  - [🧾 회계와 세무](i18n/ko/areas/negocios/contabilidade.md) — 회계, 세금, MEI, 세무 업무.
  - [👥 인사와 피플 매니지먼트](i18n/ko/areas/negocios/rh-pessoas.md) — 채용, 조직 문화, 온보딩, 보상, 리더십.
  - [⚖️ 법률](i18n/ko/areas/negocios/juridico.md) — 법령, 디지털 법, 계약, 리걸테크.
  - [🛟 고객 지원과 Customer Success](i18n/ko/areas/negocios/atendimento-suporte.md) — 지원, 고객 성공, 헬프 데스크, 지식 베이스.
- [🔬 **과학, 보건, 교육**](i18n/ko/areas/ciencia-educacao/README.md) — 🔗 2238
  - [➗ 수학과 통계](i18n/ko/areas/ciencia-educacao/matematica.md) — 기초부터 고급까지, 통계, 미적분, 선형대수.
  - [🔭 물리학과 천문학](i18n/ko/areas/ciencia-educacao/fisica-astronomia.md) — 물리학, 천문학, 천체물리학, 우주 과학.
  - [⚗️ 화학](i18n/ko/areas/ciencia-educacao/quimica.md) — 일반 화학, 계산 화학, 실험실 도구.
  - [🧬 생물학과 생물정보학](i18n/ko/areas/ciencia-educacao/biologia.md) — 생물학, 유전학, 생물정보학, 생명과학.
  - [🩺 의학과 보건](i18n/ko/areas/ciencia-educacao/saude.md) — 의학, 공중보건, 디지털 헬스, 웰빙.
  - [🧠 심리학과 신경과학](i18n/ko/areas/ciencia-educacao/psicologia.md) — 심리학, 신경과학, 행동, 정신 건강.
  - [📉 경제학](i18n/ko/areas/ciencia-educacao/economia.md) — 경제학, 계량경제학, 공공 정책.
  - [🏛️ 인문학](i18n/ko/areas/ciencia-educacao/humanidades.md) — 역사, 철학, 사회학, 지리학, 예술.
  - [🗣️ 외국어](i18n/ko/areas/ciencia-educacao/idiomas.md) — 영어, 스페인어 등 여러 언어의 강좌, 앱, 연습.
  - [🎓 교육](i18n/ko/areas/ciencia-educacao/educacao.md) — 플랫폼, 무료 강좌, MOOC, 교사를 위한 자료.
  - [📚 학술 연구](i18n/ko/areas/ciencia-educacao/pesquisa-academica.md) — 논문, 학술 데이터베이스, LaTeX, 참고문헌 관리, 오픈 사이언스.
- [🧭 **커리어와 생산성**](i18n/ko/areas/carreira/README.md) — 🔗 997
  - [💼 커리어와 채용](i18n/ko/areas/carreira/carreira-vagas.md) — 채용 공고, 이력서, 면접, 커리어 로드맵, 연봉.
  - [🏝️ 원격 근무와 프리랜서](i18n/ko/areas/carreira/trabalho-remoto-freela.md) — 원격 채용, 프리랜서 플랫폼, 디지털 노마드, 스스로 일 관리하기.
  - [⏱️ 생산성과 정리](i18n/ko/areas/carreira/produtividade.md) — 방법론, 노트 앱, 할 일 관리, 집중, 세컨드 브레인.
  - [👋 커뮤니티, 이벤트, 콘텐츠](i18n/ko/areas/carreira/comunidades.md) — 커뮤니티, 이벤트, 뉴스레터, 팟캐스트, 채널.
  - [♿ 접근성](i18n/ko/areas/carreira/acessibilidade.md) — 디지털 접근성, 보조 기술, 포용.
- [🧰 **도구와 유틸리티**](i18n/ko/areas/ferramentas/README.md) — 🔗 2373
  - [🌍 온라인 도구](i18n/ko/areas/ferramentas/ferramentas-online.md) — 브라우저에서 쓰는 변환기, 생성기, 에디터, 유틸리티.
  - [🪄 AI 도구](i18n/ko/areas/ferramentas/ferramentas-ia.md) — 텍스트, 이미지, 영상, 오디오, 생산성을 위한 AI 앱.
  - [🏠 Self-hosted](i18n/ko/areas/ferramentas/self-hosted.md) — 직접 호스팅하는 소프트웨어: 개인 클라우드, 미디어, 자동화.
  - [🖥️ macOS, Windows, Linux 앱](i18n/ko/areas/ferramentas/apps-sistemas.md) — 운영체제별 최고의 애플리케이션.
  - [📲 Android와 iOS 앱](i18n/ko/areas/ferramentas/apps-celular.md) — 유용한 모바일 앱과 오픈 소스 앱.
  - [🧩 브라우저 확장 프로그램](i18n/ko/areas/ferramentas/extensoes-navegador.md) — Chrome, Firefox 등 브라우저용 확장 프로그램.
  - [🔗 공개 API](i18n/ko/areas/ferramentas/apis-publicas.md) — 프로젝트, 학습, 프로토타입에 쓸 수 있는 무료 API.
  - [🎁 무료 자료](i18n/ko/areas/ferramentas/recursos-gratuitos.md) — 이미지 스톡, 아이콘, 폰트, 팔레트, 목업, 템플릿.
  - [⚡ 자동화와 노코드](i18n/ko/areas/ferramentas/automacao.md) — 워크플로 자동화, 노코드, 로우코드, 연동.

## 🧭 직업별 학습 경로

> 각 학습 경로는 한 직업에 중요한 영역을 공부할 만한 순서대로 묶어 줍니다.

- [🎨 프런트엔드 개발자](i18n/ko/trilhas/README.md#-프런트엔드-개발자) — 사람들이 브라우저에서 사용하는 인터페이스를 만듭니다.
- [⚙️ 백엔드 개발자](i18n/ko/trilhas/README.md#️-백엔드-개발자) — API, 비즈니스 로직, 연동, 서버에서 돌아가는 모든 것을 만듭니다.
- [📱 모바일 개발자](i18n/ko/trilhas/README.md#-모바일-개발자) — Android와 iOS 앱을 만듭니다.
- [🎮 게임 개발자](i18n/ko/trilhas/README.md#-게임-개발자) — 게임을 프로그래밍하고 디자인하고 출시합니다.
- [☁️ DevOps, SRE, 클라우드](i18n/ko/trilhas/README.md#️-devops-sre-클라우드) — 배포를 자동화하고, 인프라를 운영하고, 시스템이 계속 돌아가게 합니다.
- [✅ QA와 테스트 분석가](i18n/ko/trilhas/README.md#-qa와-테스트-분석가) — 수동, 자동화, 성능 테스트로 품질을 보장합니다.
- [📊 데이터 분석가와 BI](i18n/ko/trilhas/README.md#-데이터-분석가와-bi) — 데이터를 답, 대시보드, 의사결정으로 바꿉니다.
- [🔀 데이터 엔지니어](i18n/ko/trilhas/README.md#-데이터-엔지니어) — 신뢰할 수 있는 데이터 파이프라인과 플랫폼을 구축합니다.
- [🧠 데이터 과학자와 ML 엔지니어](i18n/ko/trilhas/README.md#-데이터-과학자와-ml-엔지니어) — 통계와 machine learning으로 데이터를 모델링합니다.
- [✨ AI와 LLM 엔지니어](i18n/ko/trilhas/README.md#-ai와-llm-엔지니어) — 언어 모델, 에이전트, RAG로 제품을 만듭니다.
- [🛡️ 보안 전문가](i18n/ko/trilhas/README.md#️-보안-전문가) — 시스템을 보호하고, 방어를 테스트하고, 사고를 조사합니다.
- [🖌️ UI/UX 디자이너](i18n/ko/trilhas/README.md#️-uiux-디자이너) — 사람 중심의 경험과 인터페이스를 디자인합니다.
- [🖍️ 그래픽 디자이너와 일러스트레이터](i18n/ko/trilhas/README.md#️-그래픽-디자이너와-일러스트레이터) — 아이덴티티, 시각 결과물, 일러스트를 만듭니다.
- [🎞️ 영상 편집자](i18n/ko/trilhas/README.md#️-영상-편집자) — 영상을 편집하고, 색과 소리를 다듬고, 마무리합니다.
- [🎥 영화 제작자와 감독](i18n/ko/trilhas/README.md#-영화-제작자와-감독) — 영화와 영상을 쓰고, 찍고, 연출하고, 배급합니다.
- [📷 사진가](i18n/ko/trilhas/README.md#-사진가) — 사진을 찍고, 편집하고, 판매합니다.
- [🧊 모션 디자이너와 3D 아티스트](i18n/ko/trilhas/README.md#-모션-디자이너와-3d-아티스트) — 애니메이션, 모델링, 시각 효과를 만듭니다.
- [🎧 음악 프로듀서와 팟캐스터](i18n/ko/trilhas/README.md#-음악-프로듀서와-팟캐스터) — 음악과 팟캐스트를 녹음하고, 믹싱하고, 공개합니다.
- [✍️ 작가, 카피라이터, 콘텐츠 라이터](i18n/ko/trilhas/README.md#️-작가-카피라이터-콘텐츠-라이터) — 알리고, 설득하고, 판매하는 글을 씁니다.
- [🎯 트래픽 매니저](i18n/ko/trilhas/README.md#-트래픽-매니저) — 유료 미디어를 기획하고, 구매하고, 최적화합니다.
- [📣 디지털 마케터](i18n/ko/trilhas/README.md#-디지털-마케터) — 온라인에서 고객을 끌어들이고, 전환시키고, 유지합니다.
- [📲 소셜 미디어 담당자와 콘텐츠 크리에이터](i18n/ko/trilhas/README.md#-소셜-미디어-담당자와-콘텐츠-크리에이터) — 소셜 미디어 콘텐츠를 기획하고 제작합니다.
- [🤝 영업과 SDR](i18n/ko/trilhas/README.md#-영업과-sdr) — 고객을 발굴하고, 협상하고, 계약을 성사시킵니다.
- [🛒 셀러와 이커머스 매니저](i18n/ko/trilhas/README.md#-셀러와-이커머스-매니저) — 온라인으로 판매하고 쇼핑몰을 운영합니다.
- [🚀 창업가](i18n/ko/trilhas/README.md#-창업가) — 사업을 만들고 키웁니다.
- [📦 프로덕트 매니저](i18n/ko/trilhas/README.md#-프로덕트-매니저) — 무엇을, 왜 만들지 결정합니다.
- [🗂️ 프로젝트 매니저와 애자일 코치](i18n/ko/trilhas/README.md#️-프로젝트-매니저와-애자일-코치) — 사람, 일정, 산출물을 조직합니다.
- [💰 금융, 투자, 회계 전문가](i18n/ko/trilhas/README.md#-금융-투자-회계-전문가) — 개인과 기업의 돈을 관리합니다.
- [👥 인사와 채용](i18n/ko/trilhas/README.md#-인사와-채용) — 사람을 영입하고, 성장시키고, 돌봅니다.
- [⚖️ 변호사와 법률 전문가](i18n/ko/trilhas/README.md#️-변호사와-법률-전문가) — 법, 계약, 컴플라이언스를 다룹니다.
- [🛟 고객 지원과 Customer Success](i18n/ko/trilhas/README.md#-고객-지원과-customer-success) — 문제를 해결하고 고객의 성공을 돕습니다.
- [🎓 교사와 교육자](i18n/ko/trilhas/README.md#-교사와-교육자) — 가르치고 학습 자료를 만듭니다.
- [📚 학생 (입시, 대학, 독학)](i18n/ko/trilhas/README.md#-학생-입시-대학-독학) — 스스로, 무료로, 방법을 갖추고 배웁니다.
- [🔬 연구자와 과학자](i18n/ko/trilhas/README.md#-연구자와-과학자) — 과학 지식을 생산하고 발표합니다.
- [🩺 보건 전문가](i18n/ko/trilhas/README.md#-보건-전문가) — 사람을 돌보고 보건 분야에서 데이터와 기술을 활용합니다.
- [🔌 메이커, 전자공학, 로보틱스](i18n/ko/trilhas/README.md#-메이커-전자공학-로보틱스) — 하드웨어, 센서, 마이크로컨트롤러로 프로젝트를 만듭니다.
- [🏝️ 프리랜서와 원격 근무자](i18n/ko/trilhas/README.md#️-프리랜서와-원격-근무자) — 독립적으로 또는 원격으로 일합니다.
- [🧰 누구나: 디지털 일상의 필수 도구](i18n/ko/trilhas/README.md#-누구나-디지털-일상의-필수-도구) — 모두에게 쓸모 있는 도구, 앱, 주의 사항.

## 🤖 모든 영역의 AI

> 모든 영역 페이지에는 AI 섹션이 있습니다. AI 링크는 총 2465개이며, 그중 734개가 엄선한 필수 링크입니다. 직업별 도구, 에이전트용 skills, 플러그인, MCP, 무료 강좌, 프롬프트 가이드, 규제와 책임 있는 활용을 다룹니다.

- [🤖 **모든 영역을 위한 AI**](i18n/ko/ia/README.md): 각 영역의 AI 섹션을 부문별로 한곳에서.
- 💡 예시: [영상 편집](i18n/ko/areas/criacao/edicao-de-video.md#-영상-편집를-위한-ai) · [유료 트래픽](i18n/ko/areas/marketing-vendas/trafego-pago.md#-유료-트래픽를-위한-ai) · [법률](i18n/ko/areas/negocios/juridico.md#-법률를-위한-ai) · [의학과 보건](i18n/ko/areas/ciencia-educacao/saude.md#-의학과-보건를-위한-ai) · [교육](i18n/ko/areas/ciencia-educacao/educacao.md#-교육를-위한-ai) · [QA와 테스트](i18n/ko/areas/tecnologia/qa-testes.md#-qa와-테스트를-위한-ai) · [회계와 세무](i18n/ko/areas/negocios/contabilidade.md#-회계와-세무를-위한-ai) · [UI/UX 디자인](i18n/ko/areas/criacao/design-ui-ux.md#-uiux-디자인를-위한-ai).

## 🧠 직업별 AI 저장소 1000개

> **38000개 저장소**(고유 26307개), 38개 직업마다 1000개씩이며, 모두 AI, 새로운 도구, AI 자동화에 집중했습니다. 주제별로 나누고 스타 수 순으로 정렬했으며 각 저장소에 설명이 있습니다.

- [🎨 프런트엔드 개발자](i18n/ko/ia/profissoes/desenvolvedor-front-end.md)
- [⚙️ 백엔드 개발자](i18n/ko/ia/profissoes/desenvolvedor-back-end.md)
- [📱 모바일 개발자](i18n/ko/ia/profissoes/desenvolvedor-mobile.md)
- [🎮 게임 개발자](i18n/ko/ia/profissoes/desenvolvedor-de-jogos.md)
- [☁️ DevOps, SRE, 클라우드](i18n/ko/ia/profissoes/devops-sre.md)
- [✅ QA와 테스트 분석가](i18n/ko/ia/profissoes/qa.md)
- [📊 데이터 분석가와 BI](i18n/ko/ia/profissoes/analista-de-dados.md)
- [🔀 데이터 엔지니어](i18n/ko/ia/profissoes/engenheiro-de-dados.md)
- [🧠 데이터 과학자와 ML 엔지니어](i18n/ko/ia/profissoes/cientista-de-dados.md)
- [✨ AI와 LLM 엔지니어](i18n/ko/ia/profissoes/engenheiro-de-ia.md)
- [🛡️ 보안 전문가](i18n/ko/ia/profissoes/seguranca.md)
- [🖌️ UI/UX 디자이너](i18n/ko/ia/profissoes/designer-ui-ux.md)
- [🖍️ 그래픽 디자이너와 일러스트레이터](i18n/ko/ia/profissoes/designer-grafico.md)
- [🎞️ 영상 편집자](i18n/ko/ia/profissoes/editor-de-video.md)
- [🎥 영화 제작자와 감독](i18n/ko/ia/profissoes/filmmaker.md)
- [📷 사진가](i18n/ko/ia/profissoes/fotografo.md)
- [🧊 모션 디자이너와 3D 아티스트](i18n/ko/ia/profissoes/motion-3d.md)
- [🎧 음악 프로듀서와 팟캐스터](i18n/ko/ia/profissoes/produtor-musical.md)
- [✍️ 작가, 카피라이터, 콘텐츠 라이터](i18n/ko/ia/profissoes/redator.md)
- [🎯 트래픽 매니저](i18n/ko/ia/profissoes/gestor-de-trafego.md)
- [📣 디지털 마케터](i18n/ko/ia/profissoes/profissional-de-marketing.md)
- [📲 소셜 미디어 담당자와 콘텐츠 크리에이터](i18n/ko/ia/profissoes/social-media.md)
- [🤝 영업과 SDR](i18n/ko/ia/profissoes/vendedor.md)
- [🛒 셀러와 이커머스 매니저](i18n/ko/ia/profissoes/e-commerce.md)
- [🚀 창업가](i18n/ko/ia/profissoes/empreendedor.md)
- [📦 프로덕트 매니저](i18n/ko/ia/profissoes/product-manager.md)
- [🗂️ 프로젝트 매니저와 애자일 코치](i18n/ko/ia/profissoes/gerente-de-projetos.md)
- [💰 금융, 투자, 회계 전문가](i18n/ko/ia/profissoes/financas.md)
- [👥 인사와 채용](i18n/ko/ia/profissoes/rh.md)
- [⚖️ 변호사와 법률 전문가](i18n/ko/ia/profissoes/advogado.md)
- [🛟 고객 지원과 Customer Success](i18n/ko/ia/profissoes/atendimento.md)
- [🎓 교사와 교육자](i18n/ko/ia/profissoes/professor.md)
- [📚 학생 (입시, 대학, 독학)](i18n/ko/ia/profissoes/estudante.md)
- [🔬 연구자와 과학자](i18n/ko/ia/profissoes/pesquisador.md)
- [🩺 보건 전문가](i18n/ko/ia/profissoes/saude.md)
- [🔌 메이커, 전자공학, 로보틱스](i18n/ko/ia/profissoes/maker.md)
- [🏝️ 프리랜서와 원격 근무자](i18n/ko/ia/profissoes/freelancer.md)
- [🧰 누구나: 디지털 일상의 필수 도구](i18n/ko/ia/profissoes/usuario.md)

## 🔢 숫자로 보는 가이드

> 수치는 생성기가 실행될 때마다 계산됩니다.

| 지표 | 값 |
|---|---|
| 🔗 영역 카탈로그의 링크 | 17357 |
| 🧬 카탈로그의 고유 URL | 15493 |
| 🗂️ 부문 / 영역 | 9 / 72 |
| ⭐ 엄선한 필수 링크 | 1998 |
| 🤖 영역별 AI 링크 | 2465 |
| 🧠 직업별 AI 저장소(고유) | 38000 (26307) |
| 📋 출처로 사용한 큐레이션 목록 | 397 |
| 🌍 가이드 언어 | 12 |
| 🧾 유형별 | 🌐 사이트 8638 · 📦 저장소 6084 · 🛠️ 도구 661 · 📖 문서 616 · 🎓 강좌 281 · 📋 awesome 리스트 224 · 👥 커뮤니티 183 · 🎬 동영상 174 · 📚 도서 150 · 📱 앱 137 · 📺 채널 118 · 📄 학술 논문 91 |

| 부문 | 다루는 내용 | 영역 | 🔗 링크 |
|---|---|:--:|:--:|
| [💻 기술과 개발](i18n/ko/areas/tecnologia/README.md) | 프로그래밍, 웹, 모바일, 게임, 인프라, 테스트 등 소프트웨어를 만드는 일. | 16 | 5051 |
| [🤖 데이터와 인공지능](i18n/ko/areas/dados-ia/README.md) | 데이터 분석, 엔지니어링, 데이터 과학, machine learning, 생성형 AI. | 5 | 1289 |
| [🔒 보안과 개인정보 보호](i18n/ko/areas/seguranca/README.md) | 공격형·방어형 사이버 보안, OSINT, 개인정보 보호, 컴플라이언스. | 3 | 722 |
| [🎬 디자인과 창작](i18n/ko/areas/criacao/README.md) | 디자인, 영상, 영화, 영상·음향 소스, 사진, 애니메이션, 오디오, 글쓰기. | 9 | 1895 |
| [📈 마케팅과 영업](i18n/ko/areas/marketing-vendas/README.md) | 디지털 마케팅, 유료 트래픽, SEO, 소셜 미디어, 영업, 이커머스. | 6 | 1170 |
| [💼 비즈니스와 경영](i18n/ko/areas/negocios/README.md) | 창업, 제품, 프로젝트, 재무, 인사, 법무. | 8 | 1622 |
| [🔬 과학, 보건, 교육](i18n/ko/areas/ciencia-educacao/README.md) | 자연과학과 생명과학, 보건, 인문학, 외국어, 교육. | 11 | 2238 |
| [🧭 커리어와 생산성](i18n/ko/areas/carreira/README.md) | 채용 공고, 원격 근무, 프리랜서, 생산성, 커뮤니티, 접근성. | 5 | 997 |
| [🧰 도구와 유틸리티](i18n/ko/areas/ferramentas/README.md) | 온라인 도구, 시스템별 앱, 셀프 호스팅, API, 무료 자료. | 9 | 2373 |

## 📜 제공되는 스크립트

> 모든 것은 Python으로 생성됩니다. 손으로 편집하는 페이지는 없습니다.

| 스크립트 | 기능 |
|---|---|
| [`scripts/coletar.py`](scripts/coletar.py) | 큐레이션된 목록을 내려받아(Scrapling 사용, 대체 수단은 git) 각 링크의 이름, 설명, 주제를 추출합니다. |
| [`scripts/selecionar.py`](scripts/selecionar.py) | 정규화하고 중복을 제거하며 라이선스 정책을 적용하고 설명을 필수로 요구하며, 상한과 출처 간 순환 방식으로 영역별 링크를 고릅니다. |
| [`scripts/coletar_repos_ia.py`](scripts/coletar_repos_ia.py) | GitHub에서 직업별 AI 저장소를 직업당 1000개씩 검색합니다. |
| [`scripts/descrever.py`](scripts/descrever.py) | 설명이 없는 저장소의 공개 설명을 가져옵니다. |
| [`scripts/traduzir.py`](scripts/traduzir.py) | 공개 모델을 사용해 오프라인으로 설명과 주제를 가이드의 여러 언어로 번역합니다. |
| [`scripts/gerar.py`](scripts/gerar.py) | 모든 언어로 README, 부문·영역·학습 경로·AI 페이지, 카탈로그, CSV를 생성합니다. |
| [`scripts/checar_links.py`](scripts/checar_links.py) | 링크가 응답하는지 확인하고 깨진 링크를 표시합니다. |
| [`tests/validar.py`](tests/validar.py) | 데이터, 페이지, 앵커, 설명, 언어, 개수를 검증합니다. |

## 🛠️ 재생성과 검증

> 생성과 검증에는 Python 3 표준 라이브러리만 있으면 됩니다. Scrapling은 수집을 개선하고, Argos Translate는 번역을 담당합니다.

```bash
python3 scripts/coletar.py            # → data/brutos.jsonl.gz
python3 scripts/descrever.py          # → data/descricoes.json
python3 scripts/selecionar.py         # → data/links.jsonl
python3 scripts/coletar_repos_ia.py   # → data/repos-ia.jsonl
python3 scripts/traduzir.py           # → data/i18n/desc.<idioma>.json.gz
python3 scripts/gerar.py              # → README*, areas/, trilhas/, ia/, i18n/
python3 tests/validar.py              # → "OK"
```

## 🤝 기여

> 제안은 언제나 환영합니다. 빠진 링크, 새 영역, 학습 경로, 더 나은 번역 무엇이든 좋습니다.

- **새 링크:** `data/essenciais.json`에 추가하거나(해당 영역의 필수 링크라면), `data/fontes.json`에 **큐레이션 목록**을 제안하세요. 그다음 생성기를 실행하세요.
- **깨진 링크나 어색한 번역:** 페이지 주소와 링크를 적어 이슈를 열어 주세요.
- 단계별 안내는 [docs/08 · 기여 방법](docs/08-como-contribuir.md)과 [CONTRIBUTING.md](CONTRIBUTING.md)에 있습니다.

## ⚖️ 라이선스와 크레딧

> 링크는 커뮤니티가 관리하는 **큐레이션 목록 397곳**에서 가져왔으며, 라이선스와 함께 [docs/07](docs/07-fontes-e-licencas.md)과 각 영역 하단에 나열되어 있습니다. 이 가이드의 콘텐츠는 **CC BY-SA 4.0**, 스크립트는 **MIT**입니다([LICENSE](LICENSE) 참조). 라이선스가 없거나 GPL 또는 비상업 라이선스인 목록의 텍스트는 복사하지 않았습니다.

## ⚠️ 안내

> 이 가이드는 제3자의 사이트와 저장소를 가리킵니다. 이들과는 아무 제휴 관계가 없으며, 각 콘텐츠의 책임은 운영하는 쪽에 있습니다. 링크는 바뀌므로 깨진 링크를 발견하면 알려 주세요. 공격형 보안 콘텐츠는 학습용이며 **허가된 범위 안에서만** 사용해야 합니다.

## 🌟 Star History

> 가이드가 도움이 되었다면 스타를 눌러 주세요. 더 많은 사람에게 닿는 힘이 됩니다.

[![Star History Chart](https://api.star-history.com/svg?repos=arthurspk/guiadoconhecimento&type=Date)](https://star-history.com/#arthurspk/guiadoconhecimento&Date)
