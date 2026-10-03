# 🔀 데이터 엔지니어링

> 파이프라인, ETL, 데이터 레이크, 스트리밍, 오케스트레이션. 이 영역에는 **210개 링크**가 있습니다. 엄선한 필수 링크 20개, 인공지능 링크 40개, 그리고 큐레이션된 목록 5곳에서 모은 150개입니다.

[← 🤖 데이터와 인공지능](README.md) · [🗂️ 영역 카탈로그](../CATALOGO.md) · [🏠 홈](../../../../README.ko.md)

🌍 🇧🇷 [Português (Brasil)](../../../../areas/dados-ia/engenharia-de-dados.md) · 🇺🇸 [English](../../../en/areas/dados-ia/engenharia-de-dados.md) · 🇪🇸 [Español](../../../es/areas/dados-ia/engenharia-de-dados.md) · 🇨🇳 [中文](../../../zh/areas/dados-ia/engenharia-de-dados.md) · 🇮🇳 [हिन्दी](../../../hi/areas/dados-ia/engenharia-de-dados.md) · 🇸🇦 [العربية](../../../ar/areas/dados-ia/engenharia-de-dados.md) · 🇫🇷 [Français](../../../fr/areas/dados-ia/engenharia-de-dados.md) · 🇮🇹 [Italiano](../../../it/areas/dados-ia/engenharia-de-dados.md) · 🇰🇷 **한국어** · 🇷🇺 [Русский](../../../ru/areas/dados-ia/engenharia-de-dados.md) · 🇩🇪 [Deutsch](../../../de/areas/dados-ia/engenharia-de-dados.md) · 🇯🇵 [日本語](../../../ja/areas/dados-ia/engenharia-de-dados.md)

## 📚 목차

> 필요한 섹션으로 바로 이동하세요. 옆의 숫자는 링크 수입니다.

[⭐ 여기서 시작하세요](#-여기서-시작하세요) <sub>20</sub> <br>
[🤖 데이터 엔지니어링를 위한 AI](#-데이터-엔지니어링를-위한-ai) <sub>40</sub> <br>
[🔹 엔진 및 플랫폼](#-엔진-및-플랫폼) <sub>15</sub> <br>
[🛠️ 응용 및 도구](#️-응용-및-도구) <sub>12</sub> <br>
[📊 데이터 통합 및 Pipelines](#-데이터-통합-및-pipelines) <sub>10</sub> <br>
[🧊 라이브러리, SDK 및 프로그래밍 모델](#-라이브러리-sdk-및-프로그래밍-모델) <sub>9</sub> <br>
[🗄️ 관련 기사](#️-관련-기사) <sub>6</sub> <br>
[🔵 일괄 처리](#-일괄-처리) <sub>6</sub> <br>
[🔹 인증현황](#-인증현황) <sub>6</sub> <br>
[📊 차트 및 대시보드](#-차트-및-대시보드) <sub>6</sub> <br>
[📊 자료 Ingestion](#-자료-ingestion) <sub>6</sub> <br>
[🖥️ 파일 시스템](#️-파일-시스템) <sub>6</sub> <br>
[🔹 Stream 처리](#-stream-처리) <sub>6</sub> <br>
[🧺 더 많은 링크](#-더-많은-링크) <sub>62</sub> <br>
[🧾 이 영역의 출처](#-이-영역의-출처)

## ⭐ 여기서 시작하세요

> 큐레이션에서 엄선한 데이터 엔지니어링의 필수 링크입니다. 시간이 많지 않다면 이것만 보세요.

- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) - 무료 및 오픈 코스는 Docker, Terraform, dbt, Spark 및 Kafka와 완벽한 파이프라인을 구축합니다. <sub>🎓 강좌</sub>
- [roadmap.sh - Data Engineer](https://roadmap.sh/data-engineer) - 데이터 엔지니어가되기 위해 공부하는 것보다 대화 형 스크립트.
- [Microsoft Learn - Engenheiro de Dados](https://learn.microsoft.com/pt-br/training/career-paths/data-engineer) - Azure의 데이터 엔지니어링 모듈과 공식 및 무료 포르투갈어 트레일. <sub>🎓 강좌 · 🇧🇷 pt-BR</sub>
- [Designing Data-Intensive Applications](https://dataintensive.net/) - Martin Kleppmann의 분산 데이터 시스템, 스토리지 및 스트리밍의 기본 책. <sub>📚 도서</sub>
- [Big Book of Data Engineering](https://www.databricks.com/resources/ebook/big-book-of-data-engineering) - Databricks 자유 전자 책 패턴과 파이프라인 및 호수의 실용적인 사례. <sub>📚 도서</sub>
- [Documentação do Apache Airflow](https://airflow.apache.org/docs/) - 시장에서 가장 많이 사용되는 파이프라인 오케스트라의 공식 문서. <sub>📖 문서</sub>
- [Documentação do Apache Spark](https://spark.apache.org/docs/latest/) - PySpark 및 Spark SQL을 포함한 분산 처리 엔진의 공식 문서. <sub>📖 문서</sub>
- [Documentação do Apache Kafka](https://kafka.apache.org/documentation/) - Kafka Connect 및 Kafka Streams와 함께 이벤트 스트리밍 플랫폼의 공식 문서. <sub>📖 문서</sub>
- [dbt Developer Hub](https://docs.getdbt.com/) - 문서, 가이드 및 SQL으로 데이터 변환을위한 dbt의 좋은 관행. <sub>📖 문서</sub>
- [DuckDB](https://duckdb.org/) - 내장 분석 데이터베이스는 Parquet 및 CSV 로컬에서 SQL, 클러스터없이.
- [Apache Iceberg](https://iceberg.apache.org/) - 계획 진화와 시간 여행과 데이터 호수를위한 테이블 형식을 엽니 다.
- [Delta Lake](https://delta.io/) - ACID 거래 및 데이터 호수에 버전화되는 오픈 소스 프레임 워크.
- [Dagster](https://dagster.io/) - 현대 오케스트라는 데이터 자산, 선량 및 관측 가능성에 중점을 둡니다.
- [Prefect](https://www.prefect.io/) - Python 워크플로우 오케스트라는 스케줄링, 유지 및 모니터링을 제공합니다.
- [Airbyte](https://airbyte.com/) - 수백 개의 커넥터가있는 데이터 입력 (ELT) 플랫폼.
- [Start Data Engineering](https://www.startdataengineering.com/) - 파이프라인 디자인, SQL, Airflow, dbt 및 좋은 연습에 대한 실제 기사.
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) - 주간 뉴스 레터 작성 및 데이터 엔지니어링 뉴스.
- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/) - 은행, 파이프라인 및 데이터 인프라에 대한 인터뷰와 주간 팟 캐스트. <sub>📺 채널</sub>
- [Programação Dinâmica](https://www.youtube.com/@pgdinamica) - 프로그래밍, 데이터 및 AI에 대한 브라질 채널, 파이썬 콘텐츠와 파이프라인. <sub>📺 채널 · 🇧🇷 pt-BR</sub>
- [Seattle Data Guy](https://www.youtube.com/@SeattleDataGuy) - 데이터 아키텍처, 현대 데이터 스택 도구 및 경력에 대한 채널. <sub>📺 채널</sub>

## 🤖 데이터 엔지니어링를 위한 AI

> 데이터 엔지니어링 분야에서 일하는 분들을 위한 AI 도구, skills, MCP, 강좌, 프롬프트 가이드, 책임 있는 AI 활용 자료입니다. [🤖 모든 영역을 위한 AI](../../ia/README.md)도 함께 보세요.

### 💎 AI 필수 링크

- [Genie Code (Databricks)](https://docs.databricks.com/aws/pt/notebooks/databricks-assistant-faq) - Databricks AI 마법사 문서는 코드를 생성하고, 파이프라인과 대쉬보드를 구축하며 작업 공간 오류를 디버그합니다. <sub>📖 문서 · 🇧🇷 pt-BR</sub>
- [Gemini no BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview?hl=pt-br) - 공식 BigQuery AI 문서: SQL 생성, 데이터 준비 및 대화 분석. <sub>📖 문서 · 🇧🇷 pt-BR</sub>
- [Copilot no Data Factory (Microsoft Fabric)](https://learn.microsoft.com/pt-br/fabric/data-factory/copilot-fabric-data-factory) - 공식 Copilot 문서는 Fabric의 자연 언어에서 데이터 통합 및 Dataflow Gen2를 만들 수 있습니다. <sub>📖 문서 · 🇧🇷 pt-BR</sub>
- [Snowflake Cortex AI](https://docs.snowflake.com/en/guides-overview-ai-features) - Snowflake AI 기능 개요 (Cortex Agents, AI Functions, Analyst, Search)는 창고 둘레 내에서 수행했습니다. <sub>📖 문서</sub>
- [dbt Wizard (antigo dbt Copilot)](https://docs.getdbt.com/docs/cloud/dbt-copilot) - 프로젝트의 맥락에서 모델, 테스트, 문서 및 메트릭을 생성하는 dbt 플랫폼의 AI 에이전트; 테스트와 함께 지불. <sub>📖 문서</sub>
- [dbt MCP Server](https://github.com/dbt-labs/dbt-mcp) - AI 에이전트에 대한 프로젝트, 선량, 메트릭 및 dbt 명령을 노출하는 공식 Dbt Labs MCP 서버; 오픈 소스.
- [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) - Google Open source MCP 서버는 Postgres, MySQL, BigQuery 및 Spanner와 같은 은행에 에이전트를 연결하고 안전하게 풀 연결을 연결합니다.
- [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) - 데이터베이스 건강 분석, 계획 및 인덱스 권장 설명과 함께 PostgreSQL에 대한 MCP 서버; 오픈 소스.
- [Airflow AI SDK](https://github.com/astronomer/airflow-ai-sdk) - Astronomer SDK는 Apache Airflow DAG 작업으로 LLM 및 에이전트를 호출합니다. 오픈 소스.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - RAG 및 LLMs의 데이터를 준비하는 통합 문서 (PDF, HTML, Word)를 위한 ETL 라이브러리; 오픈 소스.

### 🧪 더 많은 AI 도구와 자료

- [Weaviate](https://github.com/weaviate/weaviate) - (저녁 식사 안내)
- [Dingo](https://github.com/MigoXLab/dingo) - Dingo : 종합 AI 데이터, 모델 및 응용 품질 평가 도구
- [DeepLearning.AI — Introduction to Data Engineering](https://www.deeplearning.ai/courses/introduction-to-data-engineering) - 데이터 엔지니어링 수명주기의 기초에 짧은 및 무료 과정. <sub>🇧🇷 pt-BR</sub>
- [Rivestack](https://rivestack.io/) - AI 워크로드에 대한 pgvector와 함께 관리 된 PostgreSQL. HNSW 지수, 하위 4ms 대기 시간 및 자동 embedding 세대를 가진 내장 SQL 편집기.
- [ArkFlow](https://github.com/arkflow-rs/arkflow) - 높은 성능 Rust 스트림 처리 엔진을 원활히 통합 AI 기능, 강력한 실시간 데이터 처리 및 지능형 분석 제공.
- [txtai](https://github.com/neuml/txtai) - 검색, LLM 관현 및 언어 모델 워크플로우를 위한 올인원 AI 프레임워크
- [AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) - AdalFlow : LLM 응용 프로그램을 구축하고 자동 최적화하는 라이브러리.
- [Didática Tech](https://www.youtube.com/@didaticatech) - 데이터, 기계 학습 및 프로그래밍에 포르투갈어의 무료 과정과 설명. <sub>📺 채널 · 🇧🇷 pt-BR</sub>
- [zvec](https://github.com/alibaba/zvec) - 임베디드 벡터 데이터베이스 on-device RAG 및 Edge AI, 벡터 데이터베이스의 SQLite.
- [RisingWave](https://github.com/risingwavelabs/risingwave) - Event Streaming platform for Agentic AI. 지속적으로 ingest, transform 및 이벤트 스트림을 실시간으로 제공합니다.
- [marqo](https://github.com/marqo-ai/marqo) - 전자 상거래 검색 및 발견 - marqo.ai
- [LlamaIndex](https://github.com/run-llama/llama_index) - LlamaIndex는 AI를 위한 문서 처리 플랫폼입니다.
- [Monte Carlo](https://montecarlo.ai/) - Data Observability platform (date + AI 관측), 최종 사용자의 앞에 파이프라인을 감지합니다.
- [pdfmux](https://github.com/NameetP/pdfmux) - Python PDF-to-Markdown Orchestrator. 각 페이지를 분류하고 최적의 백엔드 (PyMuPDF, Docling, RapidOCR, Gemini Flash)로 변환하여 Markdown을 방출하며 페이지 신뢰 점수를 매기합니다.
- [CapyMOA](https://github.com/adaptive-machine-learning/CapyMOA) - CapyMOA는 Python의 데이터 스트림에 대한 효율적인 기계 학습을합니다. CapyMOA는 다음과 같은 방법 및 증발기의 도구 상자입니다: 분류, 회귀, 클러스터링, anomaly detection, 반 감독 ...
- [SuperDuperDB](https://github.com/SuperDuperDB/superduperdb) - Superduper: 주문 AI 신청 및 대리인을 건축하는 끝 최후 기구.
- [GitHub Copilot](https://github.com/features/copilot) - Cursor 및 Claude Code는 DAGs, dbt 모델과 품질 테스트의 쓰기를 가속화합니다. 그러나 항상 생산 라인에 적용하기 전에 시험 환경에서 실행됩니다. <sub>🇧🇷 pt-BR</sub>
- [Xquik](https://xquik.com/) - REST API (76 엔드포인트), 20 대량 추출 도구, 계정 모니터링, HMAC 서명 웹훅 및 AI 에이전트 통합을위한 MCP 서버를 가진 실시간 X (Twitter) 데이터 추출 플랫폼.
- [River](https://github.com/online-ml/river) - Python의 온라인 기계 학습
- [MyScale Vector Database Benchmark](https://github.com/myscale/vector-db-benchmark) - 완전히 관리 된 벡터 데이터베이스를 벤치 마크하기위한 프레임 워크
- [dbt Wizard (antigo dbt Copilot)](https://www.getdbt.com/product/dbt-wizard) - dbt 프로젝트 내에서 모델, 테스트 및 직접 문서를 생성하고 설명합니다. <sub>🇧🇷 pt-BR</sub>
- [Duckle](https://github.com/SouravRoy-ETL/duckle) - Local-first, open-source desktop ETL/ELT studio: 캔버스에 파이프라인을 드래그 (또는 내장된 장치 AI 조수) 그리고 DuckDB를 통해 네이티브 속도로 실행. 290+ 커넥터, a...
- [trident-ml](https://github.com/pmerienne/trident-ml) - Trident-ML : 실시간 온라인 기계 학습 라이브러리
- [ArcadeDB](https://arcadedb.com/) - 기본 벡터를 가진 오픈 소스 멀티 모델 데이터베이스는 그래프, 문서, 키 값 및 시간 시리즈 모델을 따라 지원 embedding
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - 이 서버의 대부분 뒤에 열린 기준입니다 — 그것은 생산 자료에 대리인을 연결하기 전에 명세를 이해하는 것이 가치가 있습니다. <sub>🇧🇷 pt-BR</sub>
- [Rawbbit](https://github.com/mirlan-irokez/rawbbit) - 오픈 소스 자체 호스팅 게임 분석 파이프라인. NATS JetStream 버퍼링과 HTTP 이벤트 수집기, 당신이 소유하고있는 개체 저장의 원료 Parquet 및 Metabase를 통해 쿼리를위한 ClickHouse, SQL 또는 ...
- [Pathway](https://github.com/pathwaycom/pathway) - 스트림 처리를위한 Python ETL 프레임 워크, 실시간 분석, LLM 파이프라인 및 RAG.
- [annoy](https://github.com/spotify/annoy) - C++/Python의 가장 가까운 이웃은 메모리 사용 및 로딩 / 디스크에 최적화
- [AKF](https://github.com/HMAKT99/AKF) - AI 기본 파일 형식. 신뢰 점수, 소스 검증 및 20 + 형식으로 포함 된 규정 준수 메타 데이터 (DOCX, PDF, 이미지, 코드). AI 용 EXIF.
- [Zilla](https://github.com/aklivity/zilla) - 이벤트 구동 응용 프로그램 및 AI 에이전트를위한 경량, 멀티 프로토콜 게이트웨이. 노출과 통치 Kafka, MQTT, APIs 및 MCP 공유 라우팅, 보안을 갖춘 하나의 고성능 엔진을 통해 ...

## 🔹 엔진 및 플랫폼

> 데이터 엔지니어링의 엔진 및 플랫폼 링크 15개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Aeron](https://github.com/aeron-io/aeron) - 효율적인 신뢰할 수있는 UDP unicast, UDP 멀티 캐스트 및 IPC 메시지 전송
- [Apache Apex](https://github.com/apache/apex-core) - Apache Apex 코어의 미러
- [Apache Heron](https://github.com/apache/incubator-heron) - Apache Heron (Incubating)는 Twitter에서 실시간 배포, 오류 허용 스트림 처리 엔진입니다.
- [Apache Kafka](https://github.com/apache/kafka) - Apache Kafka - 분산된 이벤트 스트리밍 플랫폼
- [Apache Pulsar](https://github.com/apache/pulsar) - 아파치 Pulsar - 분산된 pub-sub 메시징 시스템
- [Apache RocketMQ](https://github.com/apache/rocketmq) - Apache RocketMQ는 클라우드 네이티브 메시징 및 스트리밍 플랫폼이며, 이벤트 구동 애플리케이션을 구축하기 쉽습니다.
- [Apache Samza](https://github.com/apache/samza) - 아파치 Samza의 거울
- [Apache Spark Streaming](https://github.com/apache/spark) - Apache Spark - 대규모 데이터 처리를위한 통합 분석 엔진
- [Apache StreamPipes](https://github.com/apache/streampipes) - Apache StreamPipes - 자체 서비스(산업) IoT 툴박스를 사용하여 비 기술적인 사용자를 연결, 분석 및 IoT 데이터 스트림을 탐색할 수 있습니다.
- [Arroyo](https://github.com/ArroyoSystems/arroyo) - Rust에서 분산 된 스트림 처리 엔진
- [AthenaX](https://github.com/uber-archive/AthenaX) - SQL 기반 스트리밍 분석 플랫폼
- [AutoMQ](https://github.com/AutoMQ/automq) - S3의 Diskless Kafka®. 10x Cost-Effective. 크로스 - AZ 트래픽 비용 없음. 초에 자동 스케일. 단일 디지 ms 대기 시간입니다. 멀티-AZ 가용성.
- [Bytewax](https://github.com/bytewax/bytewax) - Python Stream 처리
- [eKuiper](https://github.com/lf-edge/ekuiper) - IoT Edge를 위한 경량 데이터 스트림 처리 엔진
- [Esper](https://github.com/espertechinc/esper) - Esper Complex Event Processing, SQL 및 이벤트 시리즈 분석

## 🛠️ 응용 및 도구

> 데이터 엔지니어링의 응용 및 도구 링크 12개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [beava](https://github.com/beava-dev/beava) - 실시간 결정 기능 스트리밍 infra없이. 라이브 이벤트를 제품 반사로 전환 — no Kafka, no Flink, no feature store.
- [Eventum](https://github.com/eventum-generator/eventum) - 테스트, 데모 및 파이프라인에 대한 현실적인 합성 이벤트 — 간소화된 라이브 또는 대량으로 생성
- [javactrl-kafka](https://github.com/javactrl/javactrl-kafka) - 분산, 확장 가능, 결함 유지 보수, Minimalistic Workflow Engine - 없음 DAGs, 아니 YAML, 아니 Cumbersome Diagrams, 그냥 코드
- [Nussknacker](https://github.com/TouK/nussknacker) - 실시간 데이터 / 사용자의 스트림 처리에 대한 자동 작업을위한 낮은 코드 도구.
- [straw](https://github.com/rwalk/straw) - 실시간 스트리밍 검색 플랫폼
- [StreamAlert](https://github.com/airbnb/streamalert) - StreamAlert는 데이터 소스를 사용하여 모든 환경에서 데이터를 분석하고 경고하며 논리를 인식하는 서버가없는 실시간 데이터 분석 프레임워크입니다.
- [Streamdal](https://github.com/streamdal/streamdal) - Code-Native Data 개인 정보 정책
- [StreamFlow](https://github.com/lmco/streamflow) - StreamFlowTM는 워크플로우를 구축하고 모니터링하는 데 도움을 줄 수 있도록 설계된 스트림 처리 도구입니다.
- [StreamingBandit](https://github.com/Nth-iteration-labs/streamingbandit) - Python 응용 프로그램 설정 및 스트리밍 실행 (contextual) Bandit 실험.
- [Streamline](https://github.com/hortonworks/streamline) - StreamLine - 스트리밍 분석
- [Substation](https://github.com/brexhq/substation) - Substation은 routing, normalizing 및 보안 이벤트와 감사 로그를 풍부하게하는 도구 키트입니다.
- [Turbine](https://github.com/Netflix/Turbine) - SSE 스트림 골로저

## 📊 데이터 통합 및 Pipelines

> 데이터 엔지니어링의 데이터 통합 및 Pipelines 링크 10개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Apache Flume](https://github.com/apache/logging-flume) - Apache Flume는 효율적으로 수집, 집계 및 로그와 같은 데이터의 큰 양을 이동하기 위해 배포되고 신뢰할 수 있고 사용 가능한 서비스입니다.
- [Brooklin](https://github.com/linkedin/Brooklin) - 확장 가능한 분산 시스템에서 신뢰할 수있는 근접 데이터 스트리밍
- [Bruin](https://github.com/bruin-data/bruin) - SQL 및 Python을 사용하여 데이터 파이프라인 구축, 다른 소스에서 데이터를 ingest하고 품질 검사를 추가하고 엔드 투 엔드 흐름을 빌드합니다.
- [Camus](https://github.com/LinkedInAttic/camus) - LinkedIn의 이전 세대 Kafka로 HDFS 파이프라인.
- [CocoIndex](https://github.com/cocoindex-io/cocoindex) - 긴 수평선 에이전트 스타에 대 한 Incremental 엔진 그것을 좋아!
- [Databus](https://github.com/linkedin/databus) - Source-agnostic 분산 변경 데이터 캡처 시스템
- [faucet-stream](https://github.com/faucet-hq/faucet-stream) - Rust의 데이터를 이동하는 빠르고 구성 중심 방법 — Native CLI 및 embeddable Rust 라이브러리 ETL
- [Redpanda Connect](https://github.com/redpanda-data/connect) - Fancy 스트림 처리 작업 mundane
- [RudderStack](https://github.com/rudderlabs/rudder-server) - 개인 정보 보호 및 보안은 Golang과 React에서 Segment-alternative를 집중했습니다.
- [StreamPulse](https://github.com/Yacine-ai-tech/StreamPulse) - 고선명 분석 ingestion & 실시간 분석 파이프라인 - HMAC 검증된 webhooks, 3-tier cascade 분류, deduplication, 3-sigma anomaly detection 및 이벤트 커넥터 (n8n, Kafka ...

## 🧊 라이브러리, SDK 및 프로그래밍 모델

> 데이터 엔지니어링의 라이브러리, SDK 및 프로그래밍 모델 링크 9개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Akka](https://github.com/akka/akka-core) - Elastic, agile 및 resilient인 앱을 구축하고 실행하는 플랫폼. SDK, 라이브러리 및 호스팅 환경.
- [Apache Beam](https://github.com/apache/beam) - Apache Beam은 배치 및 스트리밍 데이터 처리를위한 통합 프로그래밍 모델입니다.
- [Apache Edgent](https://github.com/apache/incubator-retired-edgent) - Apache Edgent의 미러(Incubating)
- [Apache Pekko](https://github.com/apache/pekko) - Java/Scala를 사용하여 매우 동시, 배포 및 탄력성 메시지 중심 애플리케이션 구축
- [Apache SAMOA](https://github.com/apache/incubator-samoa) - Apache 사모아의 미러 (Incubating)
- [Apache StormCrawler](https://github.com/apache/stormcrawler) - Apache Storm에 기반한 확장성, 성숙 및 다용도 웹 크롤러
- [coast](https://github.com/bkirwi/coast) - Experiments 에 영화
- [Daggy](https://github.com/synacker/daggy) - Daggy - Data Aggregation Utility 및 C/C++ 개발자 라이브러리
- [DataSketches](https://github.com/apache/datasketches-java) - 스토캐스틱 스트리밍 알고리즘의 소프트웨어 라이브러리, a.k.a. sketches

## 🗄️ 관련 기사

> 데이터 엔지니어링의 관련 기사 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [RQLite](https://github.com/rqlite/rqlite) - Raft consensus 프로토콜을 사용하여 SQLite를 복제합니다.
- [MySQL](https://www.mysql.com/) - 세계에서 가장 인기있는 오픈 소스 데이터베이스.
- [TiDB](https://github.com/pingcap/tidb) - MySQL 프로토콜과 호환되는 분산된 NewSQL 데이터베이스.
- [Percona XtraBackup](https://www.percona.com/software/mysql-database/percona-xtrabackup) - 무료 오픈 소스, Percona Server, MySQL® 및 MariaDB®의 모든 버전에 대한 완벽한 온라인 백업 솔루션.
- [mysql_utils](https://github.com/pinterest/mysql_utils) - Pinterest MySQL 관리 도구.
- [MariaDB](https://mariadb.org/) - MySQL의 향상된 드롭 인 교체.

## 🔵 일괄 처리

> 데이터 엔지니어링의 일괄 처리 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Hadoop MapReduce](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) - 대용량의 데이터(Multi-terabyte data-sets)를 처리하는 애플리케이션을 쉽게 작성할 수 있는 소프트웨어 프레임워크 - 대형 클러스터 (thousands of nodes)에 in-parallel -... <sub>📖 문서</sub>
- [Spark](https://spark.apache.org/) - 단일 노드 기계 또는 클러스터에서 데이터 엔지니어링, 데이터 과학 및 기계 학습을 실행하기위한 다국어 엔진.
- [Spark Packages](https://spark-packages.org/) - Apache Spark에 대한 패키지의 커뮤니티 인덱스.
- [Deep Spark](https://github.com/Stratio/deep-spark) - 다른 데이터 저장소와 Apache Spark를 연결. Deprecated.
- [Spark RDD API Examples](https://homepage.cs.latrobe.edu.au/zhe/ZhenHeSparkRDDAPIExamples.html) - Zhen He의 예.
- [Livy](https://livy.incubator.apache.org/) - REST 불꽃 서버.

## 🔹 인증현황

> 데이터 엔지니어링의 인증현황 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [dbt Learn — cursos e certificação](https://learn.getdbt.com/) - Analytics Engineering 인증 시험과 공식 dbt Labs 트레일. <sub>🇧🇷 pt-BR</sub>
- [Astronomer Certification](https://www.astronomer.io/certification/) - Astro 플랫폼 뒤에 회사에 의해 유지되는 Apache Airflow의 공식 인증. <sub>🇧🇷 pt-BR</sub>
- [Databricks Certified Data Engineer Associate](https://www.databricks.com/learn/certification/data-engineer-associate) - Spark, Delta Lake 및 lakehouse 파이프라인에 중점을 둔 Databricks 항목 인증. <sub>🇧🇷 pt-BR</sub>
- [Databricks Certified Data Engineer Professional](https://www.databricks.com/learn/certification/data-engineer-professional) - Advanced Databricks 인증: 규모에 파이프라인의 모델링, 최적화 및 생산. <sub>🇧🇷 pt-BR</sub>
- [AWS Certified Data Engineer – Associate](https://aws.amazon.com/certification/certified-data-engineer-associate/) - AWS 인증 (AWS 클라우드에 데이터 파이프라인을 구축하는 사람들을 위해 2024). <sub>📚 도서 · 🇧🇷 pt-BR</sub>
- [Google Cloud — Professional Data Engineer](https://cloud.google.com/learn/certification/data-engineer) - Google Cloud 인증은 규모 데이터 처리 시스템을 설계 및 운영합니다. <sub>🇧🇷 pt-BR</sub>

## 📊 차트 및 대시보드

> 데이터 엔지니어링의 차트 및 대시보드 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Highcharts](https://www.highcharts.com/) - 순수 JavaScript로 작성된 차트 라이브러리는 웹 사이트 또는 웹 애플리케이션에 대화형 차트를 추가하는 쉬운 방법을 제공합니다.
- [ZingChart](https://www.zingchart.com/) - 모든 데이터 세트에 대한 빠른 JavaScript 차트.
- [C3.js](https://c3js.org/) - D3-based 재사용할 수 있는 도표 도서관.
- [D3.js](https://d3js.org/) - Data를 기반으로 문서 조작을위한 JavaScript 라이브러리.
- [D3Plus](https://d3plus.org/) - D3의 더 간단한, 사촌을 사용하기 쉬운. 당신이 다만 자료를 폐쇄할 수 있는 가장 진보 된 템플렛.
- [SmoothieCharts](https://smoothiecharts.org/) - 스트리밍 데이터의 JavaScript Charting Library.

## 📊 자료 Ingestion

> 데이터 엔지니어링의 자료 Ingestion 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [DataSpoc Pipe](https://github.com/dataspoclab/dataspoc-pipe) - 클라우드 버킷 (S3, GCS, Azure)의 Parquet 파일에 400 + Singer 탭을 연결하는 데이터 섭취 엔진. 자동 카탈로그와 함께 스트리밍, 증가.
- [Enrich.sh](https://enrich.sh/) - JSON을 REST API로 변환하는 관리된 이벤트 ingestion service는 Hive-partitioned Parquet on Cloudflare R2, DuckDB, ClickHouse, BigQuery, Snowflake 및 Python에서 쿼리할 수 있습니다.
- [enrich-companies](https://github.com/Alessandro114/enrich-companies) - CLI 도구는 회사 데이터 (금융, 연락처, 메타데이터)를 250M + 회사 레코드로 CSV 파일을 풍부하게합니다. npm에서 사용할 수 있습니다.
- [ingestr](https://github.com/bruin-data/ingestr) - 단일 명령으로 데이터베이스의 데이터를 복사하는 CLI 도구. PostgreSQL, MySQL, MongoDB, Salesforce, Shopify를 포함한 50 + 소스 지원
- [Kafka](https://kafka.apache.org/) - 배포된 커밋 로그로 재발송을 취소할 수 있습니다.
- [BottledWater](https://github.com/confluentinc/bottledwater-pg) - PostgreSQL에서 Kafka로 데이터 캡처를 변경하십시오. Deprecated.

## 🖥️ 파일 시스템

> 데이터 엔지니어링의 파일 시스템 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [HDFS](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) - commodity 하드웨어에서 실행하도록 설계된 분산 파일 시스템. <sub>📖 문서</sub>
- [Snakebite](https://github.com/spotify/snakebite) - 순수 python HDFS 클라이언트.
- [AWS S3](https://aws.amazon.com/s3/) - Object Storage는 어디에서나 데이터를 검색하기 위해 내장되어 있습니다. <sub>📚 도서</sub>
- [smart_open](https://github.com/RaRe-Technologies/smart_open) - 큰 파일 스트리밍을위한 Utils (S3, HDFS, gzip, bz2).
- [Alluxio](https://www.alluxio.org/) - 메모리 중심의 분산 스토리지 시스템은 Spark 및 MapReduce와 같은 클러스터 프레임 워크를 통해 메모리 속도에서 신뢰할 수있는 데이터 공유를 가능하게합니다.
- [CEPH](https://ceph.com/) - 우수한 성능, 신뢰성 및 확장성을 위해 설계된 통합된 분산 스토리지 시스템.

## 🔹 Stream 처리

> 데이터 엔지니어링의 Stream 처리 링크 6개로, 커뮤니티가 큐레이션한 목록에서 모았습니다.

- [Apache Beam](https://beam.apache.org/) - 많은 실행 엔진에서 실행되는 일괄 및 스트리밍 데이터 처리 작업을 구현하는 통합 프로그래밍 모델.
- [Spark Streaming](https://spark.apache.org/streaming/) - 확장 가능한 오류 허용 스트리밍 응용 프로그램을 구축하기 쉬운.
- [Apache Flink](https://flink.apache.org/) - 데이터 스트림을 통해 분산 컴퓨팅에 대한 데이터 배포, 통신 및 오류 공차를 제공하는 스트리밍 Dataflow 엔진.
- [Apache Storm](https://storm.apache.org/) - 무료 및 오픈 소스 배포 실시간 계산 시스템.
- [Apache Samza](https://samza.apache.org/) - 분산 된 스트림 처리 프레임 워크.
- [Apache NiFi](https://nifi.apache.org/) - 사용하기 쉽고 강력하고 신뢰할 수있는 시스템을 사용하여 데이터를 처리 및 배포합니다.

## 🧺 더 많은 링크

> 별도 섹션을 두기에는 너무 작은 주제에서 나온 데이터 엔지니어링 링크입니다.

- [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering) - 프레임 워크, 도구 및 데이터 엔지니어링 리소스의 목록은 범주에 의해 조직됩니다. <sub>📋 awesome 리스트</sub>
- [Databricks — O que é engenharia de dados?](https://www.databricks.com/glossary/data-engineering) - Databricks의 생명주기에서 데이터 엔지니어링 역할에 대한 공식 설명. <sub>🇧🇷 pt-BR</sub>
- [IBM — What is data engineering?](https://www.ibm.com/think/topics/data-engineering) - IBM의 개념, 도구 및 데이터 엔지니어링 작업의 책임에 대한 설명. <sub>🇧🇷 pt-BR</sub>
- [Google Cloud — O que é engenharia de dados?](https://cloud.google.com/learn/what-is-data-engineering) - 공식 Google Cloud는 파이프라인의 개요, 섭취 및 데이터 변환. <sub>🇧🇷 pt-BR</sub>
- [dbt Labs — What is analytics engineering?](https://www.getdbt.com/blog/what-is-analytics-engineering) - Data Engineering and Analysis 사이 하이브리드 기능 구축 분석 및 dbt와 함께 탄생 한 분석. <sub>🇧🇷 pt-BR</sub>
- [Hamilton](https://github.com/dagworks-inc/hamilton) - Apache Hamilton은 데이터 과학자와 엔지니어가 테스트 가능한 모듈, 자동 문서화 데이터 흐름을 정의하며 라인age/tracing 및 메타데이터를 인코딩합니다. python의 모든 것을 실행하고 스케일링합니다.
- [LangChain](https://github.com/langchain-ai/langchain) - 에이전트 엔지니어링 플랫폼.
- [Apache Airflow — Core concepts: DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) - Airflow의 중앙 개념 : DAG (task graph)를 정의하고 구성하는 방법. <sub>📖 문서</sub>
- [Apache Airflow — Best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) - DAGs를 유지하고 쉽게 쓰기를위한 공식 최고의 연습 가이드. <sub>📖 문서</sub>
- [Dagster — Documentação](https://docs.dagster.io/) - 데이터 자산에 중점을 둔 현대 오케스트라의 문서 (일부 자산), 테스트 및 관찰 가능성. <sub>📖 문서 · 🇧🇷 pt-BR</sub>
- [Prefect — Documentação](https://docs.prefect.io/) - 공식 사전 문서, Python Orchestrator는 단순성 및 실패 탄력에 초점을 맞추고 있습니다. <sub>📖 문서 · 🇧🇷 pt-BR</sub>
- [Mage — Documentação](https://docs.mage.ai/) - Mage 문서, 데이터 파이프라인 도구와 시각적 편집기 및 코드 블록. <sub>📖 문서 · 🇧🇷 pt-BR</sub>
- [datacompy](https://github.com/capitalone/datacompy) - Pandas, Polars, Spark 등의 두 가지 DataFrames의 비교를 용이하게 하는 Python 라이브러리입니다. 이 라이브러리는 기본 equality checks를 통해 디파니시로 상세한 통찰력을 제공함으로써...
- [dvt](https://github.com/GoogleCloudPlatform/professional-services-data-validator) - Data Validation Tool은 소스 및 타겟 테이블에서 데이터를 비교하여 일치합니다. 열 검증, 행 유효성 검사, schema validation, 사용자 정의 쿼리 검증 및 광고 hoc SQL을 제공합니다 ...
- [koala-diff](https://github.com/godalida/koala-diff) - Rust와 Polars를 사용하여 로컬로 큰 데이터셋(CSV, Parquet)을 비교할 수 있는 고성능 파이썬 라이브러리입니다. OOM 오류를 방지하고 대화형 HTML 데이터를 생성하기 위해 0-copy 스트리밍 기능을 갖추고 있습니다...
- [FutureSearch SDK](https://github.com/futuresearch/futuresearch-python) - Python SDK는 병렬 웹 검색 에이전트를 통해 전송
- [Alura — Formação Engenheiro(a) de Dados](https://www.alura.com.br/formacao-engenheiro-dados) - 데이터 엔지니어링 트레일: Python, Spark, Airflow 및 클라우드. 유료 코스 <sub>🎓 강좌 · 🇧🇷 pt-BR</sub>
- [Alura — Airflow: orquestração de pipelines de dados](https://www.alura.com.br/curso-online-airflow-orquestracao-pipelines-dados) - Apache Airflow에서 DAGs의 창조와 관현에 전념한 유료 코스. <sub>🎓 강좌 · 🇧🇷 pt-BR</sub>
- [Alura — dbt: modelagem de dados em projeto analítico](https://www.alura.com.br/curso-online-dbt-modelagem-dados-projeto-analitico) - 실제 분석 프로젝트 내에서 dbt와 데이터 변환 및 모델링에 대한 유료 과정. <sub>🎓 강좌 · 🇧🇷 pt-BR</sub>
- [DIO — Trilhas e bootcamps](https://www.dio.me/) - 무료 데이터 엔지니어링 트레일과 bootcamps, 인증 포털. <sub>🎓 강좌 · 🇧🇷 pt-BR</sub>
- [dbt Labs — dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) - dbt Labs의 공식 및 무료 과정: 모델링, 테스트, 문서 및 DBT 프로젝트 배포. <sub>🇧🇷 pt-BR</sub>
- [Fundamentals of Data Engineering — Joe Reis, Matt Housley](https://www.amazon.com.br/dp/1098108302) - 현대 데이터 엔지니어링의 완벽한 수명주기를 정의하는 참조 책 (2022). 유료 책. <sub>📚 도서 · 🇧🇷 pt-BR</sub>
- [Data Pipelines with Apache Airflow — Bas Harenslak, Julian de Ruiter (Manning)](https://www.manning.com/books/data-pipelines-with-apache-airflow) - Airflow와 함께 구축, 테스트 및 모니터링 파이프라인을 위한 실제 참조. 유료 책.
- [The Data Warehouse Toolkit — Ralph Kimball](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) - 데이터 창고를 공급하는 모든 파이프 라인에 대한 치수 모델링에 관한 고전. 유료 책.
- [Data Hackers](https://www.youtube.com/@datahackers) - 브라질에서 가장 큰 데이터 커뮤니티의 채널 : 인터뷰, 직업 및 기술 콘텐츠 데이터 엔지니어링. <sub>📺 채널</sub>
- [Téo Calvo](https://www.youtube.com/@teocalvo) - 분석 및 데이터 엔지니어링의 실제 콘텐츠, SQL에 초점을 맞추고, Python과 day-to-day 도구. <sub>📺 채널</sub>
- [Neylson Crepalde](https://www.youtube.com/@neylsoncrepalde) - 통계, 데이터 및 데이터 엔지니어링은 브라질 데이터 과학자에 의해 설명되었습니다. <sub>📺 채널</sub>
- [DataTalksClub](https://www.youtube.com/@DataTalksClub) - 삶, 인터뷰 및 비디오 데이터 공학의 전체 과정 채널. <sub>📺 채널</sub>
- [Data Hackers Podcast](https://www.datahackers.com.br/podcast/) - Community Podcast Data Hackers: 브라질에서 시장, 경력 및 데이터 엔지니어링. <sub>🇧🇷 pt-BR</sub>
- [dbt Labs Blog](https://www.getdbt.com/blog) - 분석 엔지니어링, 모델링 및 dbt 생태계의 공식 블로그.
- [Astronomer Blog](https://www.astronomer.io/blog/) - Apache Airflow 튜토리얼과 뉴스를 가진 공식 Astronomer 블로그.
- [Airbnb Tech Blog](https://airbnb.tech/) - 에어비앤비 엔지니어링 블로그, Apache Hudi를 시작된 데이터 플랫폼에 대한 게시물.
- [Seattle Data Guy — Blog](https://www.theseattledataguy.com/) - 경력과 데이터 아키텍처에 대한 블로그 및 뉴스 레터, 숙련 된 데이터 엔지니어.
- [Monte Carlo Blog](https://montecarlo.ai/blog) - 관찰성 및 데이터 품질에 대한 블로그, "날짜 가동 시간"의 개념의 창조적 인 회사에 의해 유지.
- [Apache Avro](https://avro.apache.org/) - Apache AvroTM는 데이터 직렬화 시스템입니다.
- [Apache Parquet](https://parquet.apache.org/) - Hadoop 생태계의 모든 프로젝트에서 사용할 수있는 기둥 저장 형식은 데이터 처리 프레임 워크, 데이터 모델 또는 프로그래밍 언어 선택과 상관없이.
- [Snappy](https://github.com/google/snappy) - 빠른 압축기/decompressor. Parquet와 함께 사용하는.
- [PigZ](https://zlib.net/pigz/) - 현대 멀티 프로세서, 다중 코어 기계에 대한 gzip의 병렬 구현.
- [Apache ORC](https://orc.apache.org/) - Hadoop workloads에 가장 작은, 빠른 기둥 저장.
- [Flotilla](https://github.com/tylertreat/Flotilla) - 스케일 업 벤치마킹을위한 자동화 된 메시지 큐 오케스트라.
- [storm-perf-test](https://github.com/yahoo/storm-perf-test) - 단순 폭풍 성능/스트레스 테스트
- [streaming-benchmarks](https://github.com/yahoo/streaming-benchmarks) - Apache Storm, 아파치 Spark, Apache Flink 등 낮은 지연 시간(Streaming) 솔루션을 위한 벤치 마크 ...
- [Apache Airflow](https://airflow.apache.org/) - 파이썬에서 작성된 코드로 데이터 파이프라인 오케스트라; 시장에서 가장 많이 사용됩니다.
- [Mage](https://www.mage.ai/) - 하이브리드 편집기 (visual + code) 및 재사용 블록이있는 데이터 파이프라인 도구.
- [Kestra](https://kestra.io/) - 데이터 워크플로우(YAML)의 선언적인 오케스트라터 (Declarative Orchestrator)는 확장성 및 시각 인터페이스에 초점을 맞추고 있습니다.
- [dbt Labs — jaffle_shop](https://github.com/dbt-labs/jaffle-shop) - 공식 dbt 데모 프로젝트 : 모델링, 테스트 및 문서 연습을위한 fictitious 저장소. <sub>🇧🇷 pt-BR</sub>
- [Base dos Dados](https://basedosdados.org/) - BigQuery에서 SQL을 통해 처리 및 사용 가능한 브라질 공공 데이터 - 브라질의 실제 데이터를 연습하기위한 훌륭한.
- [Portal Brasileiro de Dados Abertos](https://dados.gov.br/) - 브라질 정부의 실제 공공 데이터는 테스트 파이프라인에로드합니다. <sub>🇧🇷 pt-BR</sub>
- [State of Data Brazil 2024/2025 (Data Hackers + Bain)](https://www.datahackers.news/p/relatorio2024-2025) - 브라질 데이터 시장에서 더 높은 연구 : 급여, 위치, 도구 및 고용. <sub>🇧🇷 pt-BR</sub>
- [Salario.com.br — Engenheiro de Dados](https://www.salario.com.br/profissao/engenheiro-de-dados-cbo-212205/) - 공식 CAGED 데이터를 기반으로 데이터 엔지니어의 평균 급여, 바닥 및 천장. <sub>🇧🇷 pt-BR</sub>
- [Programathor — vagas de engenharia de dados](https://programathor.com.br/jobs-data-engineering) - 브라질의 기술 관련 데이터 엔지니어링 <sub>🇧🇷 pt-BR</sub>
- [Remotar](https://remotar.com.br/) - 브라질에 대한 100 % 원격 작업, 데이터 엔지니어링을 포함. <sub>🇧🇷 pt-BR</sub>
- [RemoteOK — vagas de engenharia de dados](https://remoteok.com/remote-data-engineer-jobs) - 데이터 엔지니어링에 의해 필터링 된 국제 원격 공간.
- [Data Hackers](https://www.datahackers.com.br/) - 브라질에서 가장 큰 데이터 커뮤니티, Slack, 이벤트 및 뉴스 레터. <sub>🇧🇷 pt-BR</sub>
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) - 가장 큰 국제 데이터 엔지니어링 커뮤니티, 도구 및 경력에 대한 일일 토론. <sub>👥 커뮤니티 · 🇧🇷 pt-BR</sub>
- [dbt Community](https://www.getdbt.com/community/join-the-community) - dbt Labs의 공식 커뮤니티, Slack 활성과 연례 Coalesce 이벤트.
- [Apache Airflow — Comunidade oficial](https://airflow.apache.org/community/) - 공식 에어 플로우 커뮤니티 페이지: 슬랙, 메일링 리스트 및 프로젝트에 기여하는 방법. <sub>🇧🇷 pt-BR</sub>
- [Locally Optimistic](https://locallyoptimistic.com/) - 분석 엔지니어링과 "modern data stack"에 중점을 둔 커뮤니티 및 블로그.
- [Bonnard](https://bonnard.dev/) - Governed, 고객의 데이터에 다중 계층 MCP 액세스. 창고를 켜거나 dbt 또는 semantic 층을 안전하고 신뢰할 수있는 MCP AI 에이전트를위한.
- [Nika](https://github.com/supernovae-st/nika) - AI 데이터 파이프라인에 대한 Intent-as-code 워크플로우 엔진 : Tamper-evident run trace와 함께 실행하기 전에 YAML DAGs statically check (schema, permissions, cost floor)를 검토 할 수 있습니다.
- [OrionBelt Semantic Layer](https://github.com/ralfbecher/orionbelt-semantic-layer) - YAML 정의 차원, 측정 및 메트릭을 컴파일하는 오픈 소스 세마틱 사이드카 8 엔진 (BigQuery, ClickHouse, Databricks, Dremio, DuckDB, MySQL, PostgreSQL ...
- [DataFlow](https://github.com/OpenDCAI/DataFlow) - 데이터 준비, 합성 데이터 생성 및 AI/data 파이프라인을 위한 오픈 소스 플랫폼. 데이터와 AI 작업을 통해 워크플로우 단계 자동화에 대한 재사용 가능한 기술이 포함되어 있습니다.

## 🧾 이 영역의 출처

> 위의 링크 중 필수 링크를 제외한 나머지는 아래의 큐레이션 목록에서 모았습니다. 목록을 관리해 주시는 분들께 감사드립니다.

- [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) <sub>🔗 5 · ⚖️ sem-licenca</sub>
- [arthurspk/guiadeengenhariadedados](https://github.com/arthurspk/guiadeengenhariadedados) <sub>🔗 56 · ⚖️ MIT</sub>
- [dangkhoasdc/awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) <sub>🔗 7 · ⚖️ CC0-1.0</sub>
- [igorbarinov/awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering) <sub>🔗 56 · ⚖️ CC0-1.0</sub>
- [manuzhang/awesome-streaming](https://github.com/manuzhang/awesome-streaming) <sub>🔗 56 · ⚖️ sem-licenca</sub>

---
[⬆️ 맨 위로](#-데이터-엔지니어링) · [← 데이터와 인공지능](README.md)
