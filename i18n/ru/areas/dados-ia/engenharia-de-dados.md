# 🔀 Инженерия данных

> Пайплайны, ETL, data lake, стриминг и оркестрация. **Ссылок: 210** в этом направлении: 20 главных, отобранных вручную, 40 по искусственному интеллекту и 150 из 5 кураторских списков.

[← 🤖 Данные и искусственный интеллект](README.md) · [🗂️ Каталог направлений](../CATALOGO.md) · [🏠 Главная](../../../../README.ru.md)

🌍 🇧🇷 [Português (Brasil)](../../../../areas/dados-ia/engenharia-de-dados.md) · 🇺🇸 [English](../../../en/areas/dados-ia/engenharia-de-dados.md) · 🇪🇸 [Español](../../../es/areas/dados-ia/engenharia-de-dados.md) · 🇨🇳 [中文](../../../zh/areas/dados-ia/engenharia-de-dados.md) · 🇮🇳 [हिन्दी](../../../hi/areas/dados-ia/engenharia-de-dados.md) · 🇸🇦 [العربية](../../../ar/areas/dados-ia/engenharia-de-dados.md) · 🇫🇷 [Français](../../../fr/areas/dados-ia/engenharia-de-dados.md) · 🇮🇹 [Italiano](../../../it/areas/dados-ia/engenharia-de-dados.md) · 🇰🇷 [한국어](../../../ko/areas/dados-ia/engenharia-de-dados.md) · 🇷🇺 **Русский** · 🇩🇪 [Deutsch](../../../de/areas/dados-ia/engenharia-de-dados.md) · 🇯🇵 [日本語](../../../ja/areas/dados-ia/engenharia-de-dados.md)

## 📚 Содержание

> Переходите сразу к нужному разделу; число рядом показывает количество ссылок.

[⭐ Начните здесь](#-начните-здесь) <sub>20</sub> <br>
[🤖 ИИ: Инженерия данных](#-ии-инженерия-данных) <sub>40</sub> <br>
[🔹 Двигатели и платформы](#-двигатели-и-платформы) <sub>15</sub> <br>
[🛠️ Приложения и инструменты](#️-приложения-и-инструменты) <sub>12</sub> <br>
[📊 Интеграция данных и трубопроводы](#-интеграция-данных-и-трубопроводы) <sub>10</sub> <br>
[🧊 Библиотеки, SDK и модели программирования](#-библиотеки-sdk-и-модели-программирования) <sub>9</sub> <br>
[🗄️ Базы данных](#️-базы-данных) <sub>6</sub> <br>
[🔵 Пакетная обработка](#-пакетная-обработка) <sub>6</sub> <br>
[🔹 Сертификация](#-сертификация) <sub>6</sub> <br>
[📊 Диаграммы и панели инструментов](#-диаграммы-и-панели-инструментов) <sub>6</sub> <br>
[📊 Проглатывание данных](#-проглатывание-данных) <sub>6</sub> <br>
[🖥️ Файловая система](#️-файловая-система) <sub>6</sub> <br>
[🔹 Потоковая обработка](#-потоковая-обработка) <sub>6</sub> <br>
[🧺 Другие ссылки](#-другие-ссылки) <sub>62</sub> <br>
[🧾 Источники этого направления](#-источники-этого-направления)

## ⭐ Начните здесь

> Главное по теме «Инженерия данных», отобранное вручную куратором: если времени мало, начните с этих ссылок.

- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) - Свободный и открытый курс строительства полного трубопровода с Docker, Terraform, dbt, Spark и Kafka. <sub>🎓 курс</sub>
- [roadmap.sh - Data Engineer](https://roadmap.sh/data-engineer) - Интерактивный сценарий, вместо того чтобы учиться на инженера данных.
- [Microsoft Learn - Engenheiro de Dados](https://learn.microsoft.com/pt-br/training/career-paths/data-engineer) - Официальная и бесплатная португальская трасса с модулями обработки данных в Azure. <sub>🎓 курс · 🇧🇷 pt-BR</sub>
- [Designing Data-Intensive Applications](https://dataintensive.net/) - Книга Мартина Клеппмана об основах распределенных систем данных, хранения и потоковой передачи. <sub>📚 книга</sub>
- [Big Book of Data Engineering](https://www.databricks.com/resources/ebook/big-book-of-data-engineering) - Databricks бесплатная электронная книга с шаблонами и практическими случаями трубопроводов и озерного домика. <sub>📚 книга</sub>
- [Documentação do Apache Airflow](https://airflow.apache.org/docs/) - Официальная документация наиболее используемого на рынке трубопроводного оркестратора. <sub>📖 документация</sub>
- [Documentação do Apache Spark](https://spark.apache.org/docs/latest/) - Официальная документация распределенного процессора, включая PySpark и Spark SQL. <sub>📖 документация</sub>
- [Documentação do Apache Kafka](https://kafka.apache.org/documentation/) - Официальная документация стриминговой платформы с Kafka Connect и Kafka Streams. <sub>📖 документация</sub>
- [dbt Developer Hub](https://docs.getdbt.com/) - Документация, руководства и передовые методы преобразования данных в SQL. <sub>📖 документация</sub>
- [DuckDB](https://duckdb.org/) - Встроенная аналитическая база данных, которая консультирует Parquet и CSV локально с помощью SQL без кластера.
- [Apache Iceberg](https://iceberg.apache.org/) - Формат открытой таблицы для данных озер со схемой эволюции и путешествия во времени.
- [Delta Lake](https://delta.io/) - Фреймворк с открытым исходным кодом, который приносит транзакции и версии ACID в озера данных.
- [Dagster](https://dagster.io/) - Современный оркестратор сосредоточился на данных, происхождении и наблюдаемости.
- [Prefect](https://www.prefect.io/) - Оркестр рабочего процесса Python с планированием, сохранением и мониторингом.
- [Airbyte](https://airbyte.com/) - Открытая платформа ввода данных (ELT) с сотнями разъемов.
- [Start Data Engineering](https://www.startdataengineering.com/) - Практические статьи по проектированию трубопроводов, SQL, Airflow, dbt и передовой практике.
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) - Еженедельный информационный бюллетень с кураторскими статьями и новостями по разработке данных.
- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/) - Еженедельный подкаст с интервью о банках, трубопроводах и инфраструктуре данных. <sub>📺 канал</sub>
- [Programação Dinâmica](https://www.youtube.com/@pgdinamica) - Бразильский канал по программированию, данным и искусственному интеллекту с содержанием Python и конвейерами. <sub>📺 канал · 🇧🇷 pt-BR</sub>
- [Seattle Data Guy](https://www.youtube.com/@SeattleDataGuy) - Канал об архитектуре данных, современных инструментах стека данных и карьере. <sub>📺 канал</sub>

## 🤖 ИИ: Инженерия данных

> Инструменты, skills, MCP, курсы, руководства по промптам и ответственному использованию ИИ для тех, кто работает в направлении «Инженерия данных». См. также [🤖 ИИ для всех направлений](../../ia/README.md).

### 💎 Главное по ИИ

- [Genie Code (Databricks)](https://docs.databricks.com/aws/pt/notebooks/databricks-assistant-faq) - Databricks AI Wizard документация, которая генерирует код, строит трубопроводы и панели инструментов, а также отлаживает ошибки рабочего пространства. <sub>📖 документация · 🇧🇷 pt-BR</sub>
- [Gemini no BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview?hl=pt-br) - Официальная документация BigQuery AI: генерация SQL, подготовка данных и разговорный анализ. <sub>📖 документация · 🇧🇷 pt-BR</sub>
- [Copilot no Data Factory (Microsoft Fabric)](https://learn.microsoft.com/pt-br/fabric/data-factory/copilot-fabric-data-factory) - Официальная копилотная документация для создания интеграции данных и Dataflow Gen2 на естественном языке. <sub>📖 документация · 🇧🇷 pt-BR</sub>
- [Snowflake Cortex AI](https://docs.snowflake.com/en/guides-overview-ai-features) - Обзор функций ИИ Snowflake (агенты кортекса, функции искусственного интеллекта, аналитик, поиск), выполняемых по периметру склада. <sub>📖 документация</sub>
- [dbt Wizard (antigo dbt Copilot)](https://docs.getdbt.com/docs/cloud/dbt-copilot) - ИИ-агент платформы, генерирующей модели, тесты, документацию и метрики из контекста проекта; платный с тестом. <sub>📖 документация</sub>
- [dbt MCP Server](https://github.com/dbt-labs/dbt-mcp) - Официальный MCP-сервер Dbt Labs, который предоставляет команды проекта, линии, метрики и dbt для агентов ИИ; с открытым исходным кодом.
- [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) - MCP-сервер с открытым исходным кодом Google для безопасного подключения агентов к банкам, таким как Postgres, MySQL, BigQuery и Spanner.
- [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) - MCP-сервер для PostgreSQL с анализом состояния базы данных, объяснением планов и рекомендацией индексов; открытый исходный код.
- [Airflow AI SDK](https://github.com/astronomer/airflow-ai-sdk) - Астроном SDK называет LLM и агенты задачами Apache Airflow DAG.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Библиотека ETL для неструктурированных документов (PDF, HTML, Word), которая готовит данные для RAG и LLM; с открытым исходным кодом.

### 🧪 Другие инструменты и ресурсы по ИИ

- [Weaviate](https://github.com/weaviate/weaviate) - (Путеводитель для начинающих)
- [Dingo](https://github.com/MigoXLab/dingo) - Dingo: комплексный инструмент оценки качества данных, моделей и приложений ИИ
- [DeepLearning.AI — Introduction to Data Engineering](https://www.deeplearning.ai/courses/introduction-to-data-engineering) - Краткий и бесплатный курс по основам жизненного цикла проектирования данных. <sub>🇧🇷 pt-BR</sub>
- [Rivestack](https://rivestack.io/) - Управлял PostgreSQL с pgvector для рабочих нагрузок ИИ. Индексация HNSW, задержка до 4 мс и встроенный редактор SQL с автоматической генерацией встраивания.
- [ArkFlow](https://github.com/arkflow-rs/arkflow) - Высокопроизводительный движок обработки потоков Rust легко интегрирует возможности ИИ, обеспечивая мощную обработку данных в реальном времени и интеллектуальный анализ.
- [txtai](https://github.com/neuml/txtai) - Все-в-одном AI фреймворк для семантического поиска, оркестровки LLM и рабочих процессов языковой модели
- [AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) - AdalFlow: библиотека для создания и автоматической оптимизации приложений LLM.
- [Didática Tech](https://www.youtube.com/@didaticatech) - Бесплатные курсы и объяснения на португальском языке по данным, машинному обучению и программированию. <sub>📺 канал · 🇧🇷 pt-BR</sub>
- [zvec](https://github.com/alibaba/zvec) - Встроенная векторная база данных для RAG на устройстве и edge AI, SQLite векторных баз данных.
- [RisingWave](https://github.com/risingwavelabs/risingwave) - Платформа потоковой передачи событий для агентного ИИ. Постоянно глотать, преобразовывать и обслуживать потоки событий в реальном времени, в масштабе.
- [marqo](https://github.com/marqo-ai/marqo) - Поиск и открытие электронной коммерции - marqo.ai
- [LlamaIndex](https://github.com/run-llama/llama_index) - LlamaIndex — платформа для обработки документов
- [Monte Carlo](https://montecarlo.ai/) - Платформа наблюдения данных (дата + наблюдение ИИ), которая обнаруживает разрывы трубопроводов перед конечным пользователем.
- [pdfmux](https://github.com/NameetP/pdfmux) - Оркестр Python PDF-to-Markdown. Классифицирует каждую страницу и маршруты к оптимальному бэкэнду (PyMuPDF, Docling, RapidOCR, Gemini Flash), излучая Markdown плюс показатель достоверности на…
- [CapyMOA](https://github.com/adaptive-machine-learning/CapyMOA) - CapyMOA делает эффективное машинное обучение для потоков данных в Python. CapyMOA - это набор методов и оценщиков для: классификации, регрессии, кластеризации, обнаружения аномалий…
- [SuperDuperDB](https://github.com/SuperDuperDB/superduperdb) - Superduper: сквозная структура для создания пользовательских приложений и агентов ИИ.
- [GitHub Copilot](https://github.com/features/copilot) - Курсор и код Клода ускоряют написание DAG, моделей долговых обязательств и тестов качества — но всегда выполняются в испытательной среде перед применением на производственном конвейере. <sub>🇧🇷 pt-BR</sub>
- [Xquik](https://xquik.com/) - Платформа для извлечения данных в реальном времени X (Twitter) с REST API (76 конечных точек), 20 инструментами массового извлечения, мониторингом учетных записей, веб-хуками с подписью HMAC и…
- [River](https://github.com/online-ml/river) - Онлайн-машинное обучение на Python
- [MyScale Vector Database Benchmark](https://github.com/myscale/vector-db-benchmark) - Рамки для бенчмаркинга полностью управляемых векторных баз данных
- [dbt Wizard (antigo dbt Copilot)](https://www.getdbt.com/product/dbt-wizard) - генерирует и объясняет модели, тесты и прямую документацию в рамках проекта с учетом его фактического каталога. <sub>🇧🇷 pt-BR</sub>
- [Duckle](https://github.com/SouravRoy-ETL/duckle) - Студия ETL/ELT с открытым исходным кодом для локального рабочего стола: перетащите трубопровод на холст (или опишите его встроенному помощнику AI на устройстве) и запустите его с родной скоростью…
- [trident-ml](https://github.com/pmerienne/trident-ml) - Trident-ML: онлайновая библиотека машинного обучения в реальном времени
- [ArcadeDB](https://arcadedb.com/) - многомодельная база данных с открытым исходным кодом с поддержкой встроенного вектора наряду с моделями графов, документов, ключевых значений и временных рядов
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Это открытый стандарт, лежащий в основе большинства этих серверов — стоит понять спецификацию перед подключением агента к производственным данным. <sub>🇧🇷 pt-BR</sub>
- [Rawbbit](https://github.com/mirlan-irokez/rawbbit) - Открытый исходный код самостоятельно размещенного конвейера игровой аналитики. HTTP сборщик событий с буферизацией NATS JetStream, необработанный паркет в объектном хранилище, которым вы владеете, и…
- [Pathway](https://github.com/pathwaycom/pathway) - Python ETL фреймворк для обработки потоков, аналитики в реальном времени, LLM конвейеров и RAG.
- [annoy](https://github.com/spotify/annoy) - Ближайшие соседи в C++/Python оптимизированы для использования памяти и загрузки/сохранения на диск
- [AKF](https://github.com/HMAKT99/AKF) - Нативный формат файла AI. Оценки доверия, происхождение источника и метаданные соответствия, которые встраиваются в 20+ форматов (DOCX, PDF, изображения, код). EXIF для ИИ.
- [Zilla](https://github.com/aklivity/zilla) - Легкий, многопротокольный шлюз для событийных приложений и агентов ИИ. Экспонировать и управлять Kafka, MQTT, API и MCP с помощью одного высокопроизводительного движка с общей маршрутизацией…

## 🔹 Двигатели и платформы

> Ссылок по теме «Двигатели и платформы» в направлении «Инженерия данных»: 15. Собраны из кураторских списков сообщества.

- [Aeron](https://github.com/aeron-io/aeron) - Эффективная надежная система UDP-unicast, многоадресная передача сообщений UDP и IPC
- [Apache Apex](https://github.com/apache/apex-core) - Зеркало ядра Apache Apex
- [Apache Heron](https://github.com/apache/incubator-heron) - Apache Heron (Incubating) - это распределенный, отказоустойчивый движок обработки потоков в режиме реального времени из Twitter.
- [Apache Kafka](https://github.com/apache/kafka) - Apache Kafka - распределенная потоковая платформа событий
- [Apache Pulsar](https://github.com/apache/pulsar) - Apache Pulsar - распределенная система обмена сообщениями
- [Apache RocketMQ](https://github.com/apache/rocketmq) - Apache RocketMQ - это облачная платформа для обмена сообщениями и потоковой передачи, что упрощает создание приложений на основе событий.
- [Apache Samza](https://github.com/apache/samza) - Зеркало Apache Samza
- [Apache Spark Streaming](https://github.com/apache/spark) - Apache Spark - унифицированный аналитический движок для крупномасштабной обработки данных
- [Apache StreamPipes](https://github.com/apache/streampipes) - Apache StreamPipes - это инструментарий самообслуживания (промышленного) IoT, позволяющий нетехническим пользователям подключаться, анализировать и исследовать потоки данных IoT.
- [Arroyo](https://github.com/ArroyoSystems/arroyo) - Двигатель обработки распределенного потока в Rust
- [AthenaX](https://github.com/uber-archive/AthenaX) - SQL-платформа потоковой аналитики в масштабе
- [AutoMQ](https://github.com/AutoMQ/automq) - Diskless Kafka® на S3. 10x Cost-Effective. No Cross-AZ Traffic Cost. Autoscale in seconds. Однозначная задержка ms. Multi-AZ Availability.
- [Bytewax](https://github.com/bytewax/bytewax) - Обработка Python Stream
- [eKuiper](https://github.com/lf-edge/ekuiper) - Легкий движок обработки потоков данных для IoT edge
- [Esper](https://github.com/espertechinc/esper) - Обработка сложных событий Esper, потоковый анализ SQL и серии событий

## 🛠️ Приложения и инструменты

> Ссылок по теме «Приложения и инструменты» в направлении «Инженерия данных»: 12. Собраны из кураторских списков сообщества.

- [beava](https://github.com/beava-dev/beava) - Функции принятия решений в режиме реального времени без потоковой передачи. Превратите живые события в рефлексы продукта — ни Kafka, ни Flink, ни магазин функций.
- [Eventum](https://github.com/eventum-generator/eventum) - Реалистичные синтетические события для тестирования, демонстраций и трубопроводов — потоковые в прямом эфире или генерируемые оптом
- [javactrl-kafka](https://github.com/javactrl/javactrl-kafka) - Распределенный, масштабируемый, отказоустойчивый, минималистичный рабочий процесс - нет DAGs, нет YAML, нет громоздких диаграмм, просто код
- [Nussknacker](https://github.com/TouK/nussknacker) - Инструмент с низким кодом для автоматизации действий по обработке данных/потоков в реальном времени для пользователей.
- [straw](https://github.com/rwalk/straw) - Платформа для потокового поиска в реальном времени
- [StreamAlert](https://github.com/airbnb/streamalert) - StreamAlert - это бессерверная система анализа данных в режиме реального времени, которая позволяет вам глотать, анализировать и предупреждать данные из любой среды, используя источники данных и…
- [Streamdal](https://github.com/streamdal/streamdal) - Код-нативная конфиденциальность данных
- [StreamFlow](https://github.com/lmco/streamflow) - StreamFlowTM - это инструмент обработки потоков, предназначенный для создания и мониторинга рабочих процессов обработки.
- [StreamingBandit](https://github.com/Nth-iteration-labs/streamingbandit) - Приложение Python для настройки и запуска потоковых (контекстных) бандитских экспериментов.
- [Streamline](https://github.com/hortonworks/streamline) - StreamLine - потоковая аналитика
- [Substation](https://github.com/brexhq/substation) - Подстанция - это инструментарий для маршрутизации, нормализации и обогащения журналов событий безопасности и аудита.
- [Turbine](https://github.com/Netflix/Turbine) - SSE Stream Aggregator

## 📊 Интеграция данных и трубопроводы

> Ссылок по теме «Интеграция данных и трубопроводы» в направлении «Инженерия данных»: 10. Собраны из кураторских списков сообщества.

- [Apache Flume](https://github.com/apache/logging-flume) - Apache Flume - это распределенный, надежный и доступный сервис для эффективного сбора, агрегирования и перемещения больших объемов данных.
- [Brooklin](https://github.com/linkedin/Brooklin) - Расширяемая распределенная система для надежной потоковой передачи данных на ближней линии в масштабе
- [Bruin](https://github.com/bruin-data/bruin) - Создавайте конвейеры данных с помощью SQL и Python, поглощая данные из разных источников, добавляйте проверки качества и создавайте потоки.
- [Camus](https://github.com/LinkedInAttic/camus) - Предыдущее поколение LinkedIn Kafka для HDFS.
- [CocoIndex](https://github.com/cocoindex-io/cocoindex) - Повышенный двигатель для длинного горизонта агентов Стар, если вам нравится!
- [Databus](https://github.com/linkedin/databus) - Источнико-агностическая распределенная система сбора данных изменений
- [faucet-stream](https://github.com/faucet-hq/faucet-stream) - Быстрый, настраиваемый способ перемещения данных в Rust — родной CLI и встроенная библиотека ETL Rust
- [Redpanda Connect](https://github.com/redpanda-data/connect) - Причудливая обработка потока, сделанная оперативно мирской
- [RudderStack](https://github.com/rudderlabs/rudder-server) - Конфиденциальность и безопасность, ориентированные на альтернативный сегмент в Golang and React
- [StreamPulse](https://github.com/Yacine-ai-tech/StreamPulse) - Высокопроизводительный конвейер телеметрии и аналитики в реальном времени — проверенные HMAC веб-хуки, 3-уровневая каскадная классификация, дедупликация, обнаружение аномалий 3-sigma и разъемы…

## 🧊 Библиотеки, SDK и модели программирования

> Ссылок по теме «Библиотеки, SDK и модели программирования» в направлении «Инженерия данных»: 9. Собраны из кураторских списков сообщества.

- [Akka](https://github.com/akka/akka-core) - Платформа для создания и запуска приложений, которые являются эластичными, гибкими и устойчивыми. SDK, библиотеки и размещенные среды.
- [Apache Beam](https://github.com/apache/beam) - Apache Beam - это унифицированная модель программирования для пакетной и потоковой обработки данных.
- [Apache Edgent](https://github.com/apache/incubator-retired-edgent) - Зеркало Apache Edgent (инкубирование)
- [Apache Pekko](https://github.com/apache/pekko) - Создание высококонкурентных, распределенных и устойчивых приложений на основе сообщений с использованием Java/Scala
- [Apache SAMOA](https://github.com/apache/incubator-samoa) - Mirror of Apache Samoa (альбом)
- [Apache StormCrawler](https://github.com/apache/stormcrawler) - Масштабируемый, зрелый и универсальный веб-сканер на основе Apache Storm
- [coast](https://github.com/bkirwi/coast) - Эксперименты в стриминге
- [Daggy](https://github.com/synacker/daggy) - Daggy - Утилита агрегации данных и библиотека разработчиков C/C++ для сбора потоков данных
- [DataSketches](https://github.com/apache/datasketches-java) - Программная библиотека стохастических алгоритмов потоковой передачи, a.k.a. эскизы.

## 🗄️ Базы данных

> Ссылок по теме «Базы данных» в направлении «Инженерия данных»: 6. Собраны из кураторских списков сообщества.

- [RQLite](https://github.com/rqlite/rqlite) - Репликация SQLite с использованием протокола консенсуса Raft.
- [MySQL](https://www.mysql.com/) - Самая популярная в мире база данных с открытым исходным кодом.
- [TiDB](https://github.com/pingcap/tidb) - Распределенная база данных NewSQL, совместимая с протоколом MySQL.
- [Percona XtraBackup](https://www.percona.com/software/mysql-database/percona-xtrabackup) - Бесплатное, с открытым исходным кодом, полное онлайн-решение для резервного копирования всех версий Percona Server, MySQL® и MariaDB®.
- [mysql_utils](https://github.com/pinterest/mysql_utils) - Инструменты управления Pinterest MySQL.
- [MariaDB](https://mariadb.org/) - Усовершенствованная замена для MySQL.

## 🔵 Пакетная обработка

> Ссылок по теме «Пакетная обработка» в направлении «Инженерия данных»: 6. Собраны из кураторских списков сообщества.

- [Hadoop MapReduce](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) - Программный фреймворк для легкого написания приложений, которые обрабатывают огромные объемы данных (множественные терабайтные наборы данных) - параллельно на больших кластерах (тысячах узлов)… <sub>📖 документация</sub>
- [Spark](https://spark.apache.org/) - Многоязычный движок для выполнения инженерии данных, науки о данных и машинного обучения на одноузловых машинах или кластерах.
- [Spark Packages](https://spark-packages.org/) - Индекс пакетов для Apache Spark.
- [Deep Spark](https://github.com/Stratio/deep-spark) - Подключение Apache Spark к разным хранилищам данных.
- [Spark RDD API Examples](https://homepage.cs.latrobe.edu.au/zhe/ZhenHeSparkRDDAPIExamples.html) - Примеры Чжэнь Хэ.
- [Livy](https://livy.incubator.apache.org/) - Сервер REST Spark.

## 🔹 Сертификация

> Ссылок по теме «Сертификация» в направлении «Инженерия данных»: 6. Собраны из кураторских списков сообщества.

- [dbt Learn — cursos e certificação](https://learn.getdbt.com/) - Официальный след DBT Labs с сертификационным экзаменом Analytics Engineering. <sub>🇧🇷 pt-BR</sub>
- [Astronomer Certification](https://www.astronomer.io/certification/) - Официальная сертификация в Apache Airflow, поддерживаемая компанией за платформой Astro. <sub>🇧🇷 pt-BR</sub>
- [Databricks Certified Data Engineer Associate](https://www.databricks.com/learn/certification/data-engineer-associate) - Сертификация входа Databricks была сосредоточена на трубопроводах Spark, Delta Lake и Lakehouse. <sub>🇧🇷 pt-BR</sub>
- [Databricks Certified Data Engineer Professional](https://www.databricks.com/learn/certification/data-engineer-professional) - Advanced Databricks Certification: моделирование, оптимизация и производство трубопроводов в масштабе. <sub>🇧🇷 pt-BR</sub>
- [AWS Certified Data Engineer – Associate](https://aws.amazon.com/certification/certified-data-engineer-associate/) - Сертификация AWS (запущена в 2024 году) для тех, кто строит конвейеры данных на облаке AWS. <sub>📚 книга · 🇧🇷 pt-BR</sub>
- [Google Cloud — Professional Data Engineer](https://cloud.google.com/learn/certification/data-engineer) - Google Cloud Certification для проектирования и эксплуатации систем обработки данных. <sub>🇧🇷 pt-BR</sub>

## 📊 Диаграммы и панели инструментов

> Ссылок по теме «Диаграммы и панели инструментов» в направлении «Инженерия данных»: 6. Собраны из кураторских списков сообщества.

- [Highcharts](https://www.highcharts.com/) - Библиотека графиков, написанная на чистом JavaScript, предлагает простой способ добавления интерактивных диаграмм на ваш сайт или веб-приложение.
- [ZingChart](https://www.zingchart.com/) - Быстрые графики JavaScript для любого набора данных.
- [C3.js](https://c3js.org/) - Библиотека многоразовых диаграмм на основе D3.
- [D3.js](https://d3js.org/) - Библиотека JavaScript для манипулирования документами на основе данных.
- [D3Plus](https://d3plus.org/) - D3 проще и удобнее в использовании. В основном это предопределенные шаблоны, которые можно просто подключить к данным.
- [SmoothieCharts](https://smoothiecharts.org/) - JavaScript Charting Library для потоковой передачи данных.

## 📊 Проглатывание данных

> Ссылок по теме «Проглатывание данных» в направлении «Инженерия данных»: 6. Собраны из кураторских списков сообщества.

- [DataSpoc Pipe](https://github.com/dataspoclab/dataspoc-pipe) - Движок приема данных, который соединяет более 400 кранов Singer с файлами Parquet в облачных ведрах (S3, GCS, Azure). Потоковая передача, инкрементная, с автокаталогом.
- [Enrich.sh](https://enrich.sh/) - Управляемый сервис приема событий, который преобразует JSON, отправленный в REST API, в Hive-partitioned Parquet на Cloudflare R2, запрашиваемый из DuckDB, ClickHouse, BigQuery, Snowflake и Python.
- [enrich-companies](https://github.com/Alessandro114/enrich-companies) - Инструмент CLI для обогащения файлов CSV данными компании (финансы, контакты, метаданные) из записей компаний 250M+. Доступен на npm.
- [ingestr](https://github.com/bruin-data/ingestr) - Инструмент CLI для копирования данных между базами данных с одной командой. Поддерживает более 50 источников, включая PostgreSQL, MySQL, MongoDB, Salesforce, Shopify на любом хранилище данных.
- [Kafka](https://kafka.apache.org/) - Переосмысление сообщений Publish-subscribe в виде распределенного журнала фиксации.
- [BottledWater](https://github.com/confluentinc/bottledwater-pg) - Измените запись данных с PostgreSQL на Kafka.

## 🖥️ Файловая система

> Ссылок по теме «Файловая система» в направлении «Инженерия данных»: 6. Собраны из кураторских списков сообщества.

- [HDFS](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) - Распределенная файловая система, предназначенная для работы на товарном оборудовании. <sub>📖 документация</sub>
- [Snakebite](https://github.com/spotify/snakebite) - Чистый клиент python HDFS.
- [AWS S3](https://aws.amazon.com/s3/) - Объектное хранилище, созданное для извлечения любого количества данных из любой точки мира. <sub>📚 книга</sub>
- [smart_open](https://github.com/RaRe-Technologies/smart_open) - Используйте для потоковой передачи больших файлов (S3, HDFS, gzip, bz2).
- [Alluxio](https://www.alluxio.org/) - Распределенная система хранения данных, ориентированная на память и обеспечивающая надежный обмен данными со скоростью памяти в кластерных средах, таких как Spark и MapReduce.
- [CEPH](https://ceph.com/) - Унифицированная распределенная система хранения, предназначенная для отличной производительности, надежности и масштабируемости.

## 🔹 Потоковая обработка

> Ссылок по теме «Потоковая обработка» в направлении «Инженерия данных»: 6. Собраны из кураторских списков сообщества.

- [Apache Beam](https://beam.apache.org/) - Унифицированная модель программирования, которая реализует как пакетные, так и потоковые задания по обработке данных, которые работают на многих исполнительных механизмах.
- [Spark Streaming](https://spark.apache.org/streaming/) - Упрощает создание масштабируемых отказоустойчивых потоковых приложений.
- [Apache Flink](https://flink.apache.org/) - Движок потокового потока данных, который обеспечивает распределение данных, связь и отказоустойчивость для распределенных вычислений по потокам данных.
- [Apache Storm](https://storm.apache.org/) - Бесплатная и открытая система распределенных вычислений в реальном времени.
- [Apache Samza](https://samza.apache.org/) - Распределенная структура обработки потоков.
- [Apache NiFi](https://nifi.apache.org/) - Легкая в использовании, мощная и надежная система для обработки и распространения данных.

## 🧺 Другие ссылки

> Ссылки по направлению «Инженерия данных» из тем, слишком небольших для отдельного раздела.

- [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering) - Составлен список фреймворков, инструментов и инженерных ресурсов данных по категориям. <sub>📋 awesome-список</sub>
- [Databricks — O que é engenharia de dados?](https://www.databricks.com/glossary/data-engineering) - Официальное объяснение Databricks роли технологии обработки данных в жизненном цикле. <sub>🇧🇷 pt-BR</sub>
- [IBM — What is data engineering?](https://www.ibm.com/think/topics/data-engineering) - Внедрение IBM в концепции, инструменты и обязанности тех, кто работает в области обработки данных. <sub>🇧🇷 pt-BR</sub>
- [Google Cloud — O que é engenharia de dados?](https://cloud.google.com/learn/what-is-data-engineering) - Официальный обзор Google Cloud трубопроводов, поглощения и преобразования данных. <sub>🇧🇷 pt-BR</sub>
- [dbt Labs — What is analytics engineering?](https://www.getdbt.com/blog/what-is-analytics-engineering) - Статья, определяющая аналитическую инженерию, гибридную функцию между инжинирингом данных и анализом, которая родилась вместе с dbt. <sub>🇧🇷 pt-BR</sub>
- [Hamilton](https://github.com/dagworks-inc/hamilton) - Апач Гамильтон помогает ученым и инженерам определять проверяемые, модульные, самодокументирующиеся потоки данных, которые кодируют линии/отслеживание и метаданные.
- [LangChain](https://github.com/langchain-ai/langchain) - Инжиниринговая платформа агента.
- [Apache Airflow — Core concepts: DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) - Основная концепция Airflow: как определить и организовать DAG (граф задач). <sub>📖 документация</sub>
- [Apache Airflow — Best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) - Официальное руководство по передовой практике для написания тестируемых и простых в обслуживании DAG. <sub>📖 документация</sub>
- [Dagster — Documentação](https://docs.dagster.io/) - Документация современного оркестратора, ориентированная на данные активы (активы даты), тестирование и наблюдаемость. <sub>📖 документация · 🇧🇷 pt-BR</sub>
- [Prefect — Documentação](https://docs.prefect.io/) - Официальная префектная документация, оркестратор Python фокусируется на простоте и устойчивости к отказам. <sub>📖 документация · 🇧🇷 pt-BR</sub>
- [Mage — Documentação](https://docs.mage.ai/) - Официальная документация Mage, инструмент конвейера данных с визуальным редактором и кодовыми блоками. <sub>📖 документация · 🇧🇷 pt-BR</sub>
- [datacompy](https://github.com/capitalone/datacompy) - Библиотека Python, которая облегчает сравнение двух DataFrames в Pandas, Polars, Spark и т. Д. Библиотека выходит за рамки базовых проверок равенства, предоставляя подробную информацию о…
- [dvt](https://github.com/GoogleCloudPlatform/professional-services-data-validator) - Инструмент валидации данных сравнивает данные из таблиц источника и цели, чтобы убедиться, что они совпадают. Он обеспечивает проверку столбцов, валидацию строк, валидацию схемы, проверку…
- [koala-diff](https://github.com/godalida/koala-diff) - Высокопроизводительная библиотека Python для сравнения больших наборов данных (CSV, Parquet) локально с использованием Rust и Polars. Она имеет потоковую передачу с нулевым копированием для…
- [FutureSearch SDK](https://github.com/futuresearch/futuresearch-python) - Python SDK, который отправляет параллельные веб-исследователи
- [Alura — Formação Engenheiro(a) de Dados](https://www.alura.com.br/formacao-engenheiro-dados) - Полный набор данных: Python, Spark, Airflow и Cloud. Платный курс. <sub>🎓 курс · 🇧🇷 pt-BR</sub>
- [Alura — Airflow: orquestração de pipelines de dados](https://www.alura.com.br/curso-online-airflow-orquestracao-pipelines-dados) - Платный курс, посвященный созданию и оркестровке DAG в Apache Airflow. <sub>🎓 курс · 🇧🇷 pt-BR</sub>
- [Alura — dbt: modelagem de dados em projeto analítico](https://www.alura.com.br/curso-online-dbt-modelagem-dados-projeto-analitico) - Платный курс по преобразованию данных и моделированию с помощью ДБТ в рамках реального аналитического проекта. <sub>🎓 курс · 🇧🇷 pt-BR</sub>
- [DIO — Trilhas e bootcamps](https://www.dio.me/) - Портал с бесплатными трассами для обработки данных и буткампами, сертифицированный. <sub>🎓 курс · 🇧🇷 pt-BR</sub>
- [dbt Labs — dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) - Официальный и бесплатный курс от dbt Labs: моделирование, тестирование, документирование и развертывание проектов. <sub>🇧🇷 pt-BR</sub>
- [Fundamentals of Data Engineering — Joe Reis, Matt Housley](https://www.amazon.com.br/dp/1098108302) - Справочник (2022), определяющий полный жизненный цикл современной инженерии данных. <sub>📚 книга · 🇧🇷 pt-BR</sub>
- [Data Pipelines with Apache Airflow — Bas Harenslak, Julian de Ruiter (Manning)](https://www.manning.com/books/data-pipelines-with-apache-airflow) - Практическая ссылка на строительство, испытание и мониторинг трубопроводов с помощью Airflow.
- [The Data Warehouse Toolkit — Ralph Kimball](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) - Классика о моделировании размеров, ссылка на любой трубопровод, который питает хранилище данных.
- [Data Hackers](https://www.youtube.com/@datahackers) - Канал крупнейшего в Бразилии информационного сообщества: интервью, карьерный и технический контент по теме «Инжиниринг данных». <sub>📺 канал</sub>
- [Téo Calvo](https://www.youtube.com/@teocalvo) - Практическое содержание анализа и инжиниринга данных с акцентом на SQL, Python и повседневные инструменты. <sub>📺 канал</sub>
- [Neylson Crepalde](https://www.youtube.com/@neylsoncrepalde) - Статистика, данные и инженерия данных объясняются бразильским ученым-данным. <sub>📺 канал</sub>
- [DataTalksClub](https://www.youtube.com/@DataTalksClub) - Канал с жизнями, интервью и полным курсом инженерии видеоданных. <sub>📺 канал</sub>
- [Data Hackers Podcast](https://www.datahackers.com.br/podcast/) - Community Podcast Data Hackers: рынок, карьера и разработка данных в Бразилии. <sub>🇧🇷 pt-BR</sub>
- [dbt Labs Blog](https://www.getdbt.com/blog) - Официальный блог dbt Labs по аналитической инженерии, моделированию и экосистеме.
- [Astronomer Blog](https://www.astronomer.io/blog/) - Официальный блог Astronomer с учебниками и новостями Apache Airflow.
- [Airbnb Tech Blog](https://airbnb.tech/) - Инженерный блог Airbnb с сообщениями на платформе данных, которая была создана Apache Hudi.
- [Seattle Data Guy — Blog](https://www.theseattledataguy.com/) - Блог и информационный бюллетень о карьере и архитектуре данных, подготовленный опытным инженером.
- [Monte Carlo Blog](https://montecarlo.ai/blog) - Блог о наблюдении и качестве данных, поддерживаемый творческой компанией концепции «дата простоя».
- [Apache Avro](https://avro.apache.org/) - Apache Avro - это система сериализации данных.
- [Apache Parquet](https://parquet.apache.org/) - Формат столбцового хранилища, доступный для любого проекта в экосистеме Hadoop, независимо от выбора структуры обработки данных, модели данных или языка программирования.
- [Snappy](https://github.com/google/snappy) - Быстрый компрессор/декомпрессор, используемый с паркетом.
- [PigZ](https://zlib.net/pigz/) - Параллельная реализация gzip для современных многопроцессорных, многоядерных машин.
- [Apache ORC](https://orc.apache.org/) - Самое маленькое и быстрое колонное хранилище для рабочих нагрузок Hadoop.
- [Flotilla](https://github.com/tylertreat/Flotilla) - Автоматизированная оркестровка очередей сообщений для расширенного бенчмаркинга.
- [storm-perf-test](https://github.com/yahoo/storm-perf-test) - Простой штормовой тест / стресс-тест
- [streaming-benchmarks](https://github.com/yahoo/streaming-benchmarks) - Ключевые показатели для решений с низкой задержкой (поток), включая Apache Storm, Apache Spark, Apache Flink и другие.
- [Apache Airflow](https://airflow.apache.org/) - Дирижер конвейера данных как код, написанный на Python; наиболее часто используемый на рынке.
- [Mage](https://www.mage.ai/) - Инструмент конвейера данных с гибридным редактором (визуальный + код) и многоразовыми блоками.
- [Kestra](https://kestra.io/) - Декларативный оркестратор (YAML) рабочих процессов данных, ориентированных на масштабируемость и визуальный интерфейс.
- [dbt Labs — jaffle_shop](https://github.com/dbt-labs/jaffle-shop) - Официальный демонстрационный проект ДБТ: фиктивный магазин для практики моделирования, тестирования и документации. <sub>🇧🇷 pt-BR</sub>
- [Base dos Dados](https://basedosdados.org/) - Бразильские общедоступные данные, обрабатываемые и доступные через SQL в BigQuery — отлично подходит для работы с реальными данными из Бразилии.
- [Portal Brasileiro de Dados Abertos](https://dados.gov.br/) - Реальные публичные данные от бразильского правительства по загрузке на тестовые трубопроводы. <sub>🇧🇷 pt-BR</sub>
- [State of Data Brazil 2024/2025 (Data Hackers + Bain)](https://www.datahackers.news/p/relatorio2024-2025) - Высшие исследования на бразильском рынке данных: зарплаты, должности, инструменты и найм. <sub>🇧🇷 pt-BR</sub>
- [Salario.com.br — Engenheiro de Dados](https://www.salario.com.br/profissao/engenheiro-de-dados-cbo-212205/) - Средняя зарплата, пол и потолок инженера данных на основе официальных данных CAGED. <sub>🇧🇷 pt-BR</sub>
- [Programathor — vagas de engenharia de dados](https://programathor.com.br/jobs-data-engineering) - Вакансии в Бразилии фильтруются с помощью технологии обработки данных. <sub>🇧🇷 pt-BR</sub>
- [Remotar](https://remotar.com.br/) - 100% удаленных рабочих мест для бразильцев, включая инжиниринг данных <sub>🇧🇷 pt-BR</sub>
- [RemoteOK — vagas de engenharia de dados](https://remoteok.com/remote-data-engineer-jobs) - Международные удаленные пространства, отфильтрованные с помощью технологии обработки данных.
- [Data Hackers](https://www.datahackers.com.br/) - Крупнейшее сообщество данных в Бразилии, с Slack, событиями и новостной рассылкой. <sub>🇧🇷 pt-BR</sub>
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) - Крупнейшее международное сообщество по разработке данных, с ежедневными дискуссиями об инструментах и карьере. <sub>👥 сообщество · 🇧🇷 pt-BR</sub>
- [dbt Community](https://www.getdbt.com/community/join-the-community) - Официальное сообщество dbt Labs, с активным Slack и ежегодным мероприятием Coalesce.
- [Apache Airflow — Comunidade oficial](https://airflow.apache.org/community/) - Официальная страница сообщества Airflow: Slack, списки рассылки и способы участия в проекте. <sub>🇧🇷 pt-BR</sub>
- [Locally Optimistic](https://locallyoptimistic.com/) - Сообщество и блог сосредоточены на аналитической инженерии и «современном стеке данных».
- [Bonnard](https://bonnard.dev/) - Управляемый многопользовательский MCP-доступ к данным ваших клиентов. Превратите ваш склад, долговой или семантический слой в безопасный MCP для агентов ИИ на одного клиента.
- [Nika](https://github.com/supernovae-st/nika) - Механизм рабочего процесса с намерением в качестве кода для конвейеров данных ИИ: контролируемые YAML DAG статически проверяются (схема, разрешения, минимальные затраты) перед выполнением, со следами…
- [OrionBelt Semantic Layer](https://github.com/ralfbecher/orionbelt-semantic-layer) - Семантический боковой автомобиль с открытым исходным кодом, который компилирует YAML-определяемые размеры, меры и метрики в оптимизированный SQL на 8 двигателях (BigQuery, ClickHouse, Databricks…
- [DataFlow](https://github.com/OpenDCAI/DataFlow) - Платформа с открытым исходным кодом для подготовки данных, генерации синтетических данных и конвейеров AI / данных. Включает навыки многократного использования для автоматизации шагов рабочего…

## 🧾 Источники этого направления

> Ссылки выше, кроме главных, собраны из этих кураторских списков. Спасибо тем, кто их ведёт.

- [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) <sub>🔗 5 · ⚖️ sem-licenca</sub>
- [arthurspk/guiadeengenhariadedados](https://github.com/arthurspk/guiadeengenhariadedados) <sub>🔗 56 · ⚖️ MIT</sub>
- [dangkhoasdc/awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) <sub>🔗 7 · ⚖️ CC0-1.0</sub>
- [igorbarinov/awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering) <sub>🔗 56 · ⚖️ CC0-1.0</sub>
- [manuzhang/awesome-streaming](https://github.com/manuzhang/awesome-streaming) <sub>🔗 56 · ⚖️ sem-licenca</sub>

---
[⬆️ Наверх](#-инженерия-данных) · [← Данные и искусственный интеллект](README.md)
