# 🔎 OSINT와 조사

> 공개 출처 정보 수집과 조사 기법. 이 영역에는 **205개 링크**가 있습니다. 엄선한 필수 링크 20개, 인공지능 링크 35개, 그리고 큐레이션된 목록 4곳에서 모은 150개입니다.

[← 🔒 보안과 개인정보 보호](README.md) · [🗂️ 영역 카탈로그](../CATALOGO.md) · [🏠 홈](../../../../README.ko.md)

🌍 🇧🇷 [Português (Brasil)](../../../../areas/seguranca/osint.md) · 🇺🇸 [English](../../../en/areas/seguranca/osint.md) · 🇪🇸 [Español](../../../es/areas/seguranca/osint.md) · 🇨🇳 [中文](../../../zh/areas/seguranca/osint.md) · 🇮🇳 [हिन्दी](../../../hi/areas/seguranca/osint.md) · 🇸🇦 [العربية](../../../ar/areas/seguranca/osint.md) · 🇫🇷 [Français](../../../fr/areas/seguranca/osint.md) · 🇮🇹 [Italiano](../../../it/areas/seguranca/osint.md) · 🇰🇷 **한국어** · 🇷🇺 [Русский](../../../ru/areas/seguranca/osint.md) · 🇩🇪 [Deutsch](../../../de/areas/seguranca/osint.md) · 🇯🇵 [日本語](../../../ja/areas/seguranca/osint.md)

## 📚 목차

> 필요한 섹션으로 바로 이동하세요. 옆의 숫자는 링크 수입니다.

[⭐ 여기서 시작하세요](#-여기서-시작하세요) <sub>20</sub> <br>
[🤖 OSINT와 조사를 위한 AI](#-osint와-조사를-위한-ai) <sub>35</sub> <br>
[🟠 Nickname 검색](#-nickname-검색) <sub>12</sub> <br>
[🟢 서브도메인](#-서브도메인) <sub>10</sub> <br>
[🔸 URL을](#-url을) <sub>8</sub> <br>
[📊 다크 웹에서 크롤러 데이터 도구](#-다크-웹에서-크롤러-데이터-도구) <sub>7</sub> <br>
[📊 Data Breach 검색 엔진](#-data-breach-검색-엔진) <sub>6</sub> <br>
[🔹 파일 검색](#-파일-검색) <sub>6</sub> <br>
[🔶 일반 검색](#-일반-검색) <sub>6</sub> <br>
[🎞️ 이미지 및 비디오 분석](#️-이미지-및-비디오-분석) <sub>6</sub> <br>
[🔵 사이버 위협 지도](#-사이버-위협-지도) <sub>6</sub> <br>
[🟢 파킨스](#-파킨스) <sub>6</sub> <br>
[🔒 Privacy Focused 검색 엔진](#-privacy-focused-검색-엔진) <sub>6</sub> <br>
[🟤 특수 검색 엔진](#-특수-검색-엔진) <sub>6</sub> <br>
[🔵 Threat Actor 검색](#-threat-actor-검색) <sub>6</sub> <br>
[🧺 더 많은 링크](#-더-많은-링크) <sub>59</sub> <br>
[🧾 이 영역의 출처](#-이-영역의-출처)

## ⭐ 여기서 시작하세요

> 큐레이션에서 엄선한 OSINT와 조사의 필수 링크입니다. 시간이 많지 않다면 이것만 보세요.

- [OSINT Framework](https://github.com/lockfale/osint-framework) - OSINT 도구의 상호 맵은 데이터 조사 유형에 의해 조직.
- [Bellingcat](https://www.bellingcat.com/) - 조사에 대한 세계 참고 자료인 연구 기관.
- [Bellingcat Online Investigation Toolkit](https://bellingcat.gitbook.io/toolkit) - 연구 도구의 검토 카탈로그, 사용 가이드.
- [Guias da Bellingcat](https://www.bellingcat.com/category/resources/how-tos/) - Practical geolocation 튜토리얼, 위성 이미지 및 검증.
- [Abraji](https://abraji.org.br/) - Investigative Journalism의 브라질 협회, 과정 및 평가 가이드. <sub>👥 커뮤니티 · 🇧🇷 pt-BR</sub>
- [IntelTechniques](https://inteltechniques.com/) - Michael Bazzlell의 웹 사이트 OSINT 도서, 교육 및 기능 및 개인 정보 보호.
- [Trace Labs](https://www.tracelabs.org/) - 협력 OSINT 조사 및 CTFs를 조직하는 NGO는 누락 된 사람을 찾을 수 있습니다. <sub>👥 커뮤니티</sub>
- [Sector035 - Week in OSINT](https://sector035.nl/) - OSINT 도구, 기술 및 기사의 주간 요약.
- [OSINTCurio.us](https://osintcurio.us/) - 튜토리얼과 연구 기법을 가진 OSINT Curious 프로젝트의 아카이브 (2023).
- [Sherlock](https://github.com/sherlock-project/sherlock) - 수백 개의 소셜 네트워크에서 사용자 이름을 찾는 도구.
- [Maigret](https://github.com/soxoj/maigret) - 수천 개의 웹 사이트에서 사용자로부터 정보를 수집합니다.
- [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) - 데이터베이스 및 도구는 다양한 웹 사이트에 사용자 이름을 삽입합니다.
- [theHarvester](https://github.com/laramies/theHarvester) - 이메일, 하위 도메인 및 호스트를 공공 소스에서 수집합니다.
- [SpiderFoot](https://github.com/smicallef/spiderfoot) - IP, 도메인, 이메일 및 사람들에 200 개 이상의 모듈을 갖춘 OSINT 컬렉션을 자동화합니다.
- [Shodan](https://www.shodan.io/) - 인터넷에 연결된 기기 및 서비스에 대한 검색.
- [Epieos](https://epieos.com/) - 관련 계좌를 공개하는 이메일 및 전화의 역 검색.
- [InVID Verification Plugin](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) - 소셜 네트워크에서 비디오 및 이미지를 확인하는 무료 확장.
- [Wayback Machine](https://web.archive.org/) - 오래된 버전의 페이지에 대한 역사적인 웹 아카이브.
- [SunCalc](https://www.suncalc.org/) - 태양과 그림자 크기의 위치를 계산, geolocating 및 데이트 사진에 유용합니다.
- [TinEye](https://tineye.com/) - 사진의 소스와 버전을 찾을 수 있는 반전 이미지 검색.

## 🤖 OSINT와 조사를 위한 AI

> OSINT와 조사 분야에서 일하는 분들을 위한 AI 도구, skills, MCP, 강좌, 프롬프트 가이드, 책임 있는 AI 활용 자료입니다. [🤖 모든 영역을 위한 AI](../../ia/README.md)도 함께 보세요.

### 💎 AI 필수 링크

- [Have LLMs Finally Mastered Geolocation? (Bellingcat)](https://www.bellingcat.com/resources/how-tos/2025/06/06/have-llms-finally-mastered-geolocation/) - Bellingcat 테스트 20 사진 지 위치에 AI 모델, 표시 안타, 복고증과 Google 렌즈에 대한 제한.
- [Pinpoint (Google Journalist Studio)](https://journaliststudio.google.com/pinpoint/about) - AI를 가진 문서, 오디오 및 비디오의 대형 컬렉션을 검색하고 transcribe에 대한 Google 도구.
- [Hive AI-Generated Content Detection](https://hivemoderation.com/ai-generated-content-detection) - 이미지, 비디오 및 오디오의 발견은 AI에 의해 생성되고 무료 웹 도구와 Chrome 연장을 가진 deepfakes.
- [Content Credentials Verify](https://verify.contentauthenticity.org/) - 무료 콘텐츠 자격 증명 (C2PA) 검수원은 AI의 사용을 포함하여 이미지 소스 및 편집 역사를 보여주는.
- [SynthID Detector (Google DeepMind)](https://deepmind.google/models/synthid/) - SynthID 페이지, AI에 의해 생성 된 콘텐츠의 Google 's 워터 마크 및 Journalist Check Portal (오른쪽 목록으로 액세스).
- [Picarta](https://picarta.ai) - 시각 요소에서 AI로 사진의 위치, 심지어 EXIF 메타 데이터없이; 유료 전체 리소스.
- [Fátima (Aos Fatos)](https://www.aosfatos.org/fatima/) - Tos Fact check robot that help tofirm if information is true, in Portuguese and via message apps. <sub>🇧🇷 pt-BR</sub>
- [The Essential AI Toolkit (Journalists on HF)](https://huggingface.co/spaces/JournalistsonHF/ai-toolkit) - 기자를위한 AI 도구의 무료 및 개방 컬렉션 : transcription, 비디오 처리 및 데이터 추출.
- [Whisper](https://github.com/openai/whisper) - OpenAi 음성 인식 오픈 모델 transcribe 및 번역 오디오와 비디오를 로컬로, 포르투갈어 포함.
- [Robin](https://github.com/apurvsinghgautam/robin) - OSINT 도구 AI 검색 및 Tor를 통해 어두운 웹 콘텐츠를 요약; 윤리적 및 법적 사용.

### 🧪 더 많은 AI 도구와 자료

- [Perplexity](https://www.perplexity.ai/) - 소스 인용을 가진 AI 전원 검색 엔진.
- [SubGPT](https://github.com/s0md3v/SubGPT) - GPT로 하위 도메인을 찾기, 무료로
- [Phind](https://phindai.org/) - AI 검색 엔진은 개발자와 기술적인 질문에 최적화되어 있습니다.
- [YOU](https://you.com/) - AI 검색 엔진.
- [DorkGenius](https://dorkgenius.com/) - DorkGenius는 Google, Bing 및 DuckDuckGo에 대한 사용자 정의 검색 쿼리 생성을위한 궁극적 인 도구입니다. - 우리의 최첨단 응용 프로그램은 AI의 힘을 사용하여 고급 검색 쿼리를 만들 수 있습니다 ...
- [DorkGPT](https://www.dorkgpt.com/) - AI로 Google Dorks 생성.
- [SearchDorks](https://kriztalz.sh/search-dorks/) - 검색 엔진 생성 (Google, FOFA, Shodan, Censys, ZoomEye) AI를 사용하여 도크.
- [OSINTNova](https://app.osintnova.com/) - 고급 디지털 조사 및 지능 분석을위한 AI-powered OSINT 플랫폼
- [NEUROAUTOSEARCH](https://t.me/noblackAuto_bot) - 자동차 DB 검색 + 신경 네트워크. <sub>👥 커뮤니티</sub>
- [Trace](https://trace.manus.space/) - Real-time OSINT 플랫폼에서 사용자 이름, 이메일, 전화 번호 및 breach detection와 AI 위험 점수를 가진 600+ 플랫폼을 통해 전체 이름을 검색할 수 있습니다.
- [Offendersearch](https://offendersearch.app/) - 무료. 모든 검색 58 미국 상태, 영토와 tribal 성-offender 등록 한 쿼리; 점수를 매기고, 각 경기 뒤에 공식 레지스트리 레코드에 대한 링크가 포함 된 결과. 공개 API + 오픈 ...
- [VerifiedHer](https://verifiedher.com/) - 온라인 제작자 및 영향력의 무료 등록은 "그녀가 진짜?"에 응답합니다. - 소스 된 verdict (real / AI persona / unverified)가있는 개인 페이지, 공식 계정 및 알려진 문서 ...
- [WhiteIntel](https://whiteintel.dev/) - 무료 기업 및 해외 소유권 그래프 : 31 공공 등록 (Companies House, GLEIF, ICIJ Offshore Leaks, OpenSanctions, SEC EDGAR)의 유리 소유자에 회사를 추적합니다.
- [HoneyLabs](https://honeylabs.net/) - 분산 된 허니팟 네트워크의 무료 per-IP 보고서: 어떤 IP 스캔, 일치 CVE 악용 경로, JA4/JA4H / HASSH 클라이언트 지문, 캡처된 페이로드 및 VirusTotal 인증 악성 코드 그것은...
- [IntoDNS.ai](https://intodns.ai/) - SPF, DKIM, DMARC, DNSSEC 검사 및 수정 제안을 가진 AI 전원 DNS 및 이메일 보안 스캐너.
- [GeoSpyer](https://github.com/atiilla/geospy) - Graylark의 AI-powered geo-location 서비스를 사용하여 Python 도구는 사진이 찍은 위치를 발견하지 못했습니다.
- [GeoSpy](https://geospy.web.app/) - AI 기반 이미지 osint 도구
- [ReverseImageLocation](https://reverseimagelocation.com/) - 이미지에서 위치를 식별하는 AI-powered geolocation 도구.
- [Nodebox](https://www.nodebox.net/) - 도구의 가족은 당신이 원하는 방법을 생성 디자인을 만들 수있는 레버리지를 제공합니다.
- [Amass](https://github.com/owasp-amass/amass) - amass 도구 인터넷 데이터 소스 검색, brute force subdomain enumeration 수행, 웹 아카이브를 검색하고 추가 하위 도메인 이름 추측을 생성하는 기계 학습을 사용합니다. DNS 이름...
- [ArkhamMirror](https://github.com/mantisfury/ArkhamMirror) - 오프라인 RAG, 금전 탐지, 지식 그래프 및 비전 AI 테이블 추출과 현지 최초의 AI 문서 인텔리전스.
- [IntellyWeave](https://github.com/vericle/intellyweave) - GLiNER 법인 추출, Mapbox 3D geospatial 시각화 및 30 + 국제 아카이브에 걸쳐 멀티 시약 아카이브 연구와 AI 기반 OSINT 플랫폼.
- [OpenGraph Intel (OGI)](https://github.com/khashashin/ogi) - 오픈 소스 링크 분석 및 OSINT Framework. AI 기반 조사 도구
- [Pharos AI](https://conflicts.app/) - 상호 작용하는 geospatial 시각화, 다중 자원 RSS 모니터링 및 배우 dossiers와 충돌 추적을위한 실시간 오픈 소스 인텔리전스 대시보드.
- [Taranis AI](https://github.com/taranis-ai/taranis-ai) - 웹, RSS, 이메일 및 AI / NLP 보조 워크플로우를 사용하여 웹, RSS, 전자 메일 및 기타 소스에서 수집, 풍부하고 분석 및 게시 인텔리전스 플랫폼.

## 🟠 Nickname 검색

> OSINT와 조사의 Nickname 검색 링크 12개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Social analyzer](https://github.com/qeeqbox/social-analyzer) - API, CLI 및 웹 앱을 분석하고 1000 소셜 미디어의 사람 프로필을 발견
- [nexfil](https://github.com/thewhiteh4t/nexfil) - OSINT Tool for Profiles by 사용자 이름
- [userrecon](https://github.com/wishihab/userrecon) - 75개 이상의 소셜 네트워크에서 사용자를 찾습니다.
- [NicknameFinder](https://github.com/restanse/NicknameFinder) - OSINT 도구로 검색 별명
- [gideon](https://github.com/YouVBeenHacked/gideon) - 검색 및 수집 정보의 간단한 도구
- [Arina-OSINT](https://github.com/AlexC-ux/Arina-OSINT) - OSINT 도구는 오래된 페이지에 대한 정보를 찾을 수 있습니다.
- [netizenship](https://github.com/rahulrajpl/netizenship) - commandline #OSINT 도구는 Facebook, Instagram, Twitter 등과 같은 인기있는 소셜 미디어 웹 사이트에서 사용자의 온라인 존재를 찾을 수 있습니다.
- [Search4](https://github.com/0xknown/Search4) - 인터넷에서 사람들을 검색합니다.
- [socialscan](https://github.com/iojw/socialscan) - 온라인 플랫폼에서 사용자 이름과 이메일 사용을 정확하게 쿼리하는 Python 라이브러리
- [Sherlock](https://github.com/mesuutt/sherlock) - 소셜 네트워크에서 사용자 이름 찾기
- [recon-ng](https://github.com/lanmaster53/recon-ng/) - Open Source Intelligence 모임 도구는 오픈 소스에서 수확 정보를 감소시키는 시간을 단축합니다.
- [SocialPath](https://github.com/woj-ciech/SocialPath) - 소셜 미디어 플랫폼에서 사용자를 추적

## 🟢 서브도메인

> OSINT와 조사의 서브도메인 링크 10개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Bbot](https://github.com/blacklanternsecurity/bbot) - 해커를위한 재큐브 인터넷 스캐너.
- [Subdominator](https://github.com/RevoltSecurities/Subdominator) - SubDominator는 타겟 도메인과 관련된 하위 도메인을 효율적으로 발견하고 Bug Bounty에 대한 최소 충격
- [sub.Monitor](https://github.com/e1abrador/sub.Monitor) - Self-hosted 수동 subdomain 연속 모니터링 도구.
- [Sudomy](https://github.com/screetsec/Sudomy) - Sudomy는 벌레 사냥 / pentesting에 대한 자동화 된 reconnaissance (recon)를 수행하는 하위 도메인 및 분석 영역을 수집하기 위해 서브도메인 감소 도구입니다.
- [Amass](https://github.com/OWASP/Amass) - 심층적 공격 표면 매핑 및 자산 발견
- [subchase](https://github.com/tokiakasu/subchase) - Chase subdomains Google 및 Yandex 검색 결과 파싱
- [GooFuzz](https://github.com/m3n0sd0n4ld/GooFuzz) - GooFuzz는 OSINT 접근 방식과 함께 fuzzing을 수행 할 수있는 도구이며, 감독, 파일, 하위 도메인 또는 매개 변수를 enumerate 관리하여 대상 서버의 증거를 떠나지 않고 ...
- [alterx](https://github.com/projectdiscovery/alterx) - DSL를 사용하는 빠르고 customizable subdomain wordlist 발전기
- [Photon](https://github.com/s0md3v/Photon) - OSINT용으로 설계된 빠른 크롤러.
- [subdomain-enum](https://github.com/chaitanyakrishna/subdomain-enum) - Securitytrails API를 사용하여 하위 도메인 Enumeration

## 🔸 URL을

> OSINT와 조사의 URL을 링크 8개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Gau](https://github.com/lc/gau) - AlienVault의 Open Threat Exchange, Wayback Machine 및 Common Crawl에서 알려진 URL을 Fetch에 붙여 넣으십시오.
- [Xurlfind3r](https://github.com/hueristiq/xurlfind3r) - 간단한, 효율적인 방법으로 주어진 도메인에 대한 URL을 발견하도록 설계된 명령행 유틸리티. 그것은 다양한 수동 소스에서 정보를 수집하여 작동하며 상호 작용하지 않습니다 ...
- [Unja](https://github.com/ninjhacks/unja) - Fetch & 필터 알기 URL
- [Urlfinder](https://github.com/projectdiscovery/urlfinder) - 수동으로 URL을 수집하는 고속 도구는 활성 스캔없이 효율적이고 포괄적 인 웹 자산 발견에 최적화되어 있습니다.
- [urlhunter](https://github.com/utkusen/urlhunter) - 단축 서비스를 통해 노출되는 URL에 검색 할 수있는 재구성 도구
- [Waymore](https://github.com/xnl-h4ck3r/waymore) - Wayback Machine, Common Crawl, Alien Vault OTX, URLScan, VirusTotal, GhostArchive & Intelligence X에서 더 많은 방법을 찾으십시오!
- [Uscrapper](https://github.com/z0m31en7/Uscrapper) - Uscrapper Vanta :이 강력한 오픈 소스 도구로 웹에 깊은 깊이. 표면과 깊은 웹 소스에서 쉽고 효율을 가진 귀중한 통찰력을 추출하십시오. 데이터 마이닝 및 ...
- [Ominis-Osint](https://github.com/AnonCatalyst/Ominis-Osint) - 이 파이썬 응용 프로그램은 OSINT (Open Source Intelligence) 도구는 "Ominis OSINT - Web Hunter"라고합니다. 그것은 구글에 대한 검색 결과와 관련된 검색 결과를 쿼리하여 온라인 정보 수집을 수행 ...

## 📊 다크 웹에서 크롤러 데이터 도구

> OSINT와 조사의 다크 웹에서 크롤러 데이터 도구 링크 7개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [github.com/DedSecInside/TorBot](https://github.com/DedSecInside/TorBot) - 다크 웹 OSINT 도구
- [github.com/MikeMeliz/TorCrawl.py](https://github.com/MikeMeliz/TorCrawl.py) - 크롤 및 추출 (일반 또는 양파) TOR 네트워크를 통해 웹 페이지
- [github.com/andreyglauzer/VigilantOnion](https://github.com/andreyglauzer/VigilantOnion) - tor 네트워크 사이트에 크롤러, 키워드 검색.
- [github.com/danieleperera/OnionIngestor](https://github.com/danieleperera/OnionIngestor) - 수집, 크롤 및 모니터링 onion 사이트 tor 네트워크와 인덱스 Elasticsearch에 대한 정보를 수집하는 확장 도구
- [github.com/JarryShaw/darc](https://github.com/JarryShaw/darc) - Darkweb 크롤러 프로젝트
- [github.com/RicYaben/midnight_sea](https://github.com/RicYaben/midnight_sea) - Midnight Sea : 어두운 웹 시장의 물에 항해
- [github.com/iudicium/pryingdeep](https://github.com/iudicium/pryingdeep) - Prying Deep - 어두운 웹에 대한 인텔리전스를 수집하는 OSINT 도구.

## 📊 Data Breach 검색 엔진

> OSINT와 조사의 Data Breach 검색 엔진 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [CheckLeaked](https://checkleaked.cc/) - 이메일, 사용자 이름 또는 전화가 데이터 침해에 나타나면 소스를 표시; 무료 검색, 개발자 API 및 채팅 봇.
- [CredenShow](https://credenshow.com/) - 다른 사람의 앞에 손상된 credentials를 식별하십시오.
- [HIB Ransomed](https://haveibeenransom.com/) - 그 데이터가 유출되었는지 알고 있는 것이 옳다고 합니다.
- [HEROIC.NOW](https://heroic.com/) - 어두운 웹에 데이터를 유출 했습니까? 무료로 식별 할 수 있습니다.
- [IKnowYour.Dad](https://iknowyour.dad/) - 데이터 Breach 검색 엔진.
- [Leaker](https://github.com/vflame6/leaker) - 수동 누출은 10 breach 데이터베이스를 동시에 검색하는 CLI 도구입니다.

## 🔹 파일 검색

> OSINT와 조사의 파일 검색 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [eyedex](https://www.eyedex.org/) - 디렉토리 검색 엔진을 엽니다.
- [de digger](https://www.dedigger.com/) - Google Drive에서 공개적으로 사용할 수있는 모든 종류의 파일을 찾을 수 있도록하는 웹 사이트입니다.
- [Filesec.io](https://filesec.io/) - 중앙 자원은 악의적인 파일 확장, 위험, OS 및 완화를 카탈로그.
- [Find Security Contacts](https://findsecuritycontacts.com/) - Public index listing security contacts (emails, policy 등) 보안 도메인에서 추출.txt 파일.
- [Meawfy](https://meawfy.com/) - 고급 Mega.nz 파일 검색 엔진. 우리의 지능형 크롤러 기술로 Mega.nz에서 파일을 검색하고 발견하십시오. 즉시 9 백만 개 이상의 색인 된 파일에 액세스하십시오.
- [ODCrawler](https://odcrawler.xyz/) - 오픈 디렉터리 검색 엔진. 수백만의 공공 가능한 파일을 찾습니다

## 🔶 일반 검색

> OSINT와 조사의 일반 검색 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Aol](https://search.aol.com/) - 미국 웹.
- [Bing](https://www.bing.com/) - Microsoft의 검색 엔진.
- [Brave](https://search.brave.com/) - 개인, 독립적 인 및 투명 검색 엔진.
- [Goodsearch](https://www.goodsearch.com/) - 온라인 쇼핑 거래를위한 검색 엔진.
- [Google Search](https://www.google.com/) - 가장 인기있는 검색 엔진.
- [Instya](https://www.instya.com/) - 당신은 쇼핑 사이트, 사전, 답변 사이트, 뉴스, 이미지, 비디오 등을 검색 할 수 있습니다.

## 🎞️ 이미지 및 비디오 분석

> OSINT와 조사의 이미지 및 비디오 분석 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Google Images](https://images.google.com/) - 반전 이미지 검색.
- [Yandex Images](https://yandex.com/images/) - 강력한 얼굴 인식 기능으로 대체 역 이미지 검색.
- [Surfface](https://surfface.com/) - Face search and people finder that indexes social profiles 과 다른 공공 미디어.
- [ExifTool](https://exiftool.org/) - 사진과 비디오에서 metadata (EXIF, GPS, 타임스탬프)를 추출하십시오.
- [Jimpl EXIF Viewer](https://jimpl.com/) - 이미지 메타데이터 검사를 위한 간단한 온라인 도구 (설치 필요 없음).
- [FFmpeg](https://ffmpeg.org/) - 비디오 / 오디오 추출 및 처리를위한 멀티미디어 프레임 워크.

## 🔵 사이버 위협 지도

> OSINT와 조사의 사이버 위협 지도 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Bitdefender Threat Map](https://threatmap.bitdefender.com/) - Cyberthreat Real Time 지도 Bitdefender.
- [BunkerWeb Live Cyber Attack Threat Map](https://threatmap.bunkerweb.io/) - BunkerWeb, 오픈 소스 및 차세대 웹 애플리케이션 방화벽에 의해 차단된 사이버 공격.
- [Check Point Live Cyber Threat Map](https://threatmap.checkpoint.com/) - ransomware, infostealers 및 클라우드 취약점을 포함하여 2025의 최고 사이버 위협을 탐험하십시오.
- [Fortiguard Labs](https://fortiguard.fortinet.com/threat-map) - FortiGuard Outbreak Alerts는 다양한 기업, 단체 및 산업에 영향을 미치는 중요한 램화와 사이버 보안 공격에 대한 주요 정보를 제공합니다.
- [HCL Threat Map](https://www.hcltech.com/hcl-threat-map) - Cyber Threat 지도 HCLTech.
- [Imperva Live Threat Map](https://www.imperva.com/cyber-threat-attack-map/) - DDoS 공격의 실시간 글로벌 전망, 해킹 시도, 그리고 봇은 Imperva 보안 서비스에 의해 미량화.

## 🟢 파킨스

> OSINT와 조사의 파킨스 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [BeanPaste](https://beanpaste.fun/) - 텍스트를 공유하는 작은 방법.
- [bpaste](https://bpa.st/) - bpaste에 오신 것을 환영합니다,이 사이트는 풀빈입니다. 그것은 당신이 다른 사람들과 코드를 공유 할 수 있습니다.
- [CentOS Pastebin Service](https://paste.centos.org/) - Stikked는 오픈 소스 PHP Pastebin이며, 사용자 인터페이스를 사용하기 쉽고 간단하게 유지하는 것을 목표로합니다.
- [cl1p](https://cl1p.net/) - 인터넷 클립보드.
- [commie](https://commie.io/) - commie는 라인 논평 지원과 풀빈 스크립트입니다.
- [Context](https://ctxt.io/) - 몇 초 안에 다른 사람들과 공유하십시오.

## 🔒 Privacy Focused 검색 엔진

> OSINT와 조사의 Privacy Focused 검색 엔진 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [DuckDuckGo](https://duckduckgo.com/) - 검색자의 개인 정보 보호를 강조하는 인터넷 검색 엔진.
- [Disconnect Search](https://search.disconnect.me/) - 검색 엔진을 추적하여 검색합니다. <sub>👥 커뮤니티</sub>
- [Gibiru](https://gibiru.com/) - Gibiru는 로깅 사용자의 IP 주소 또는 검색 쿼리와 같은 개인 데이터를 수집하지 않고 "uncensored search results"를 제공합니다.
- [Kagi Search](https://kagi.com/) - 검색을 Liberate. 광고를 무료로. 감시의 무료. 당신의 시간 존경. 당신은 고객, 결코 제품입니다.
- [Mojeek](https://www.mojeek.com/) - Mojeek는 당신을 추적하지 않는 독립적 인 검색 엔진입니다.
- [Presearch](https://presearch.com/) - Presearch는 당신이 검색 할 때 개인 정보 보호 및 보상을 보호하기 위해 분산 된 커뮤니티 중심의 검색 엔진입니다.

## 🟤 특수 검색 엔진

> OSINT와 조사의 특수 검색 엔진 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Abusech](https://hunting.abuse.ch/) - 모든 남용.ch 플랫폼에서 한 가지 간단한 쿼리를 통해 사냥
- [Abuseipdb](https://www.abuseipdb.com/) - IP, 도메인 및 하위넷에 대한 시스템 관리자가보고 한 학대의 저장소
- [BeVigil](https://bevigil.com/search) - Subdomains, URL, 모바일 애플리케이션의 매개 변수와 같은 자산 검색
- [BGP.tools](https://bgp.tools/) - 네트워크 reconnaissance 및 분석을위한 현대 BGP 툴킷.
- [BGP.he.net](https://bgp.he.net/) - 무료 BGP 및 네트워크 인텔리전트 툴킷
- [BrightCloud](https://brightcloud.com/tools/url-ip-lookup.php) - URL 또는 IP 주소와 관련된 명성, 범주 및 잠재적 위협을 확인합니다.

## 🔵 Threat Actor 검색

> OSINT와 조사의 Threat Actor 검색 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [APT Groups and Operations](https://docs.google.com/spreadsheets/u/0/d/1H9_xaxQHpWaa4O_Son4Gx0YOIzlcBWMsdvePFX68EKU/pubhtml?pli=1) - Threat Actors, 스폰서 국가, 도구, 방법 등에 대해 알아보십시오. <sub>📖 문서</sub>
- [Bi.Zone](https://gti.bi.zone/) - 148 상세한 TTP를 가진 위협 그룹.
- [BreachHQ](https://breach-hq.com/threat-actors) - 모든 알려진 사이버 위협 행위자의 목록을 제공 또한 악의적인 배우로 언급, APT 그룹 또는 해커.
- [Dark Web Informer](https://darkwebinformer.com/threat-actor-database/) - 추적 854 5 월 29 일 위협 행위자 2025.
- [ETDA](https://apt.etda.or.th/cgi-bin/listgroups.cgi) - Threat Actor 그룹 및 도구 검색.
- [FortiGuard Labs](https://www.fortiguard.com/threat-actor) - FortiGuard Labs에 의해 구동, 우리의 Threat Actor Encyclopedia는 행동 가능한 통찰력을 제공합니다, 보안 팀을 준비하고 유선 고급 위협 사냥 및 응답.

## 🧺 더 많은 링크

> 별도 섹션을 두기에는 너무 작은 주제에서 나온 OSINT와 조사 링크입니다.

- [github.com/adnane-X-tebbaa/Katana](https://github.com/adnane-X-tebbaa/Katana) - 고급 Google 쿼리를 실행할 수있는 기능을 제공하는 파이썬 도구 (Google Dorks로 Known - Google Dorking)
- [github.com/megadose/OnionSearch](https://github.com/megadose/OnionSearch) - OnionSearch는 다른 .onion 검색 엔진에서 URL을 스크랩하는 스크립트입니다.
- [github.com/josh0xA/darkdump](https://github.com/josh0xA/darkdump) - 딥 웹 스크램핑을위한 오픈 소스 인텔리전스 인터페이스
- [github.com/Lucksi/Darkus](https://github.com/Lucksi/Darkus) - A Onion 웹사이트 검색
- [github.com/aryanguenthner/darkfox](https://github.com/aryanguenthner/darkfox) - CTI 사이버 위협 인텔리전스 OSINT 다크 웹 딥 웹 연구. Ransomware 갱 정보 수집 도구.
- [Open-source intelligence (OSINT)](https://en.wikipedia.org/wiki/Open-source_intelligence) - 공개적으로 사용할 수 있는 소스에서 수집된 정보입니다.
- [Buster](https://github.com/sham00n/buster) - 이메일 reconnaissance에 대 한 고급 도구.
- [Have I Been Pwned](https://haveibeenpwned.com/) - 이메일 주소가 데이터 침해에 노출되었는지 확인하십시오.
- [Eyes](https://github.com/N0rz3/Eyes) - 이메일 osint 도구
- [Poastal](https://github.com/jakecreps/poastal) - Poastal - 이메일 OSINT 도구
- [h8mail](https://github.com/khast3x/h8mail) - 이메일 OSINT & Password breach hunting tool, 로컬 또는 프리미엄 서비스를 사용하여. 관련 이메일을 chasing 지원
- [EmailFinder](https://github.com/Josue87/EmailFinder) - 검색 엔진을 통해 도메인에서 이메일 찾기
- [ronin-recon](https://github.com/ronin-rb/ronin-recon) - reconnaissance를 수행하기위한 마이크로 프레임 워크 및 도구.
- [Maltego](https://www.maltego.com/) - OSINT discovery에 대한 변형 라이브러리를 제공하고 링크 분석을위한 그래프 형식으로 정보를 시각화합니다.
- [WhatsMyName](https://whatsmyname.app/) - 수백 개의 웹 사이트에서 사용자를 검색합니다.
- [Forensic OSINT Full Page Screen Capture](https://chromewebstore.google.com/detail/forensic-osint-full-page/jojaomahhndmeienhjihojidkddkahcn) - 전체 웹 페이지 화면과 비디오를 캡처하는 브라우저 확장 <sub>📱 앱</sub>
- [github.com/s-rah/onionscan](https://github.com/s-rah/onionscan) - OnionScan은 다크 웹을 조사하기위한 무료 및 오픈 소스 도구입니다.
- [github.com/k4m4/onioff](https://github.com/k4m4/onioff) - 깊은 웹 링크 검사를 위한 양파 url 조사관.
- [github.com/milesrichardson/docker-onion-nmap](https://github.com/milesrichardson/docker-onion-nmap) - Scan .onion은 최소 알파인 도커 컨테이너에서 Tor, 프록시 체인 및 dnsmasq를 사용하여 nmap과 숨겨진 서비스를 제공합니다.
- [Instaloader](https://instaloader.github.io/) - Instagram 사진, 비디오, 캡션 및 메타 데이터를 다운로드하십시오.
- [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) - 전화 번호에 대한 정보 수집 프레임 워크.
- [Truecaller](https://www.truecaller.com/) - Caller ID 및 스팸 조회 서비스 (상업).
- [BuscaPaginasBlancas](https://github.com/GeiserX/BuscaPaginasBlancas) - 스페인어 흰색 페이지 (Paginas Blancas)의 연락처 정보를 추출하기위한 OSINT 도구
- [GhostTrack](https://github.com/HunxByts/GhostTrack) - 위치 또는 모바일 번호를 추적하는 유용한 도구
- [AtDork](https://github.com/amnottdevv/atdork) - 적합한 지연, 회로 차단기 및 IP 금지와 비율 제한을 피하기 위해 자동 백엔드 낙하를 특징으로하는 전문 OSINT dorking 도구.
- [DorkCraft](https://github.com/juandresrodca/DorkCraft) - OSINT 및 reconnaissance에 대한 고급 검색 쿼리를 구축하는 Google 도크 발전기.
- [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database) - GHDB는 공개적으로 유효한 정보를 찾아내기 위하여 이용된 수색 (우리는 그(것)들을 칭합니다)의 색인입니다, pentesters와 안전 연구원을 위해 예정했습니다.
- [Alleba (Philippines)](https://www.alleba.com/) - 필리핀 검색 엔진
- [Baidu (China)](https://www.baidu.com/) - 중국에서 사용되는 주요 검색 엔진
- [Qwant](https://www.qwant.com/) - Microsoft Bing에 의존하는 프랑스어 검색 엔진.
- [SearXNG](https://searxng.org/) - 개인 정보 보호, 오픈 소스 metasearch 엔진.
- [github.com/fastfire/deepdarkCTI](https://github.com/fastfire/deepdarkCTI) - 사이버 위협 인텔리전스 소스의 깊은 어두운 웹
- [GoWitness](https://github.com/sensepost/gowitness) - CLI 도구는 증거 수집을위한 웹 페이지의 스크린 샷을 취할.
- [Wayback Machine](https://archive.org/web/) - 웹 사이트의 역사적인 스냅 샷을 검색합니다.
- [Google Maps](https://maps.google.com/) - 스트리트 뷰 및 위성 이미지.
- [Mapillary](https://www.mapillary.com/) - Crowdsourced 거리 수준 이미지.
- [Web-check](https://github.com/Lissy93/web-check) - 모든 웹 사이트 분석을위한 All-in-one OSINT 도구
- [Smap](https://github.com/s0md3v/Smap) - shodan.io에 의해 구동 Nmap의 드롭 인 교체
- [Nmap-censys](https://github.com/censys/nmap-censys) - Censys Search API를 수동 데이터 수집에 활용한 NSE 스크립트
- [Censys](https://censys.com/) - Internet-wide 스캐닝 및 인텔리전스 플랫폼.
- [WiGLE](https://wigle.net/) - 무선 네트워크 매핑 데이터베이스.
- [ExchangeFinder](https://github.com/mhaskar/ExchangeFinder) - 주어진 도메인에 대한 Microsoft Exchange 인스턴스를 찾아 정확한 버전을 확인합니다.
- [Translate Shell](https://github.com/soimort/translate-shell) - Google, Bing, Yandex 및 기타에 의해 구동되는 명령 줄 번역기.
- [DeepL](https://www.deepl.com/) - 유럽과 아시아 언어에 대한 강력한 지원으로 고품질의 번역 서비스.
- [Telepathy](https://github.com/jordanwildon/Telepathy) - Telepathy의 공개 릴리스, 텔레그램 채팅을 투자하기위한 OSINT 툴킷.
- [Pagodo](https://github.com/opsdisk/pagodo) - pagodo (Passive Google Dork) - Automate 구글 해킹 데이터베이스 스크랩 및 검색
- [Gasmask](https://github.com/twelvesec/gasmask) - 정보 수집 도구 - OSINT
- [Th3inspector](https://github.com/Moham3dRiahi/Th3inspector) - Th3Inspector 정보 수집을위한 최고의 도구
- [WhereToGo](https://github.com/valeriyshevchenko90/WhereToGo) - WhereToGo - 조직에서 사용될 수있는 인기있는 서비스 목록입니다. 사용자의 계정이있을 때 - 당신은 조직 데이터에 항목 점수를 찾을 수 있습니다.
- [Cloud OSINT](https://github.com/7WaySecurity/cloud_osint) - 큐레이트 클라우드 OSINT 리소스 — AWS, Azure, GCP, Oracle Cloud 및 기타 주요 공급자 reconnaissance에 대한 도크, 도구 및 기술
- [Information Disclosure Write-Ups And PoCs](https://github.com/soxoj/information-disclosure-writeups-and-pocs) - 글쓰기 업, 기사 및 OSINT의 상황에 다양한 흥미로운 PoC 목록
- [Carrot2](https://search.carrot2.org/) - 검색 결과를 주제로 구성합니다.
- [SimilarSites](https://www.similarsites.com/) - 서로 유사한 웹 사이트 발견
- [SitesLike](https://www.siteslike.com/) - 비슷한 웹 사이트 범주
- [DocumentCloud](https://www.documentcloud.org/) - 분석, 주석 및 출판 문서의 플랫폼.
- [Epstein Exposed](https://epsteinexposed.com/) - 2M+ DOJ Epstein 케이스 문서, 1,700+ 사람, 비행 기록, 이메일 및 네트워크 그래프 시각화의 종합 검색 데이터베이스.
- [RECAP Archive](https://www.courtlistener.com/recap/) - PACER 법정 문서의 공개 아카이브.
- [AnalyzeID](https://analyzeid.com/) - 다른 웹 사이트를 찾기에 의해 소유 된 동일한 사람
- [Code Finder](https://codefinder.dev/) - GitHub 저장소를 찾는 최고의 검색 엔진

## 🧾 이 영역의 출처

> 위의 링크 중 필수 링크를 제외한 나머지는 아래의 큐레이션 목록에서 모았습니다. 목록을 관리해 주시는 분들께 감사드립니다.

- [apurvsinghgautam/dark-web-osint-tools](https://github.com/apurvsinghgautam/dark-web-osint-tools) <sub>🔗 16 · ⚖️ sem-licenca</sub>
- [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) <sub>🔗 88 · ⚖️ CC-BY-SA-4.0</sub>
- [tracelabs/awesome-osint](https://github.com/tracelabs/awesome-osint) <sub>🔗 22 · ⚖️ MPL-2.0</sub>
- [wddadk/Offensive-OSINT-Tools](https://github.com/wddadk/Offensive-OSINT-Tools) <sub>🔗 49 · ⚖️ sem-licenca</sub>

---
[⬆️ 맨 위로](#-osint와-조사) · [← 보안과 개인정보 보호](README.md)
