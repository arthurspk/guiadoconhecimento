# 🔀 Engenharia de Dados

> Pipelines, ETL, data lakes, streaming e orquestração. **210 links** nesta área: 20 essenciais escolhidos a dedo, 40 de inteligência artificial e 150 reunidos de 5 listas curadas.

[← 🤖 Dados e Inteligência Artificial](README.md) · [🗂️ Catálogo completo](../CATALOGO.md) · [🏠 Início](../../README.md)

## 📚 Índice

[⭐ Comece por aqui](#-comece-por-aqui) <sub>20</sub> <br>
[🤖 IA para Engenharia de Dados](#-ia-para-engenharia-de-dados) <sub>40</sub> <br>
[◾ Engines and Platforms](#-engines-and-platforms) <sub>7</sub> <br>
[◾ Applications and Tools](#-applications-and-tools) <sub>6</sub> <br>
[◾ Bancos de dados](#-bancos-de-dados) <sub>6</sub> <br>
[◾ Data Engineering blogs of companies](#-data-engineering-blogs-of-companies) <sub>6</sub> <br>
[◾ Data Engineering Whitepapers](#-data-engineering-whitepapers) <sub>6</sub> <br>
[◾ Data Ingestion](#-data-ingestion) <sub>6</sub> <br>
[◾ File System](#-file-system) <sub>6</sub> <br>
[◾ LinkedIn](#-linkedin) <sub>6</sub> <br>
[◾ Managed and Closed Source](#-managed-and-closed-source) <sub>6</sub> <br>
[◾ Stream Processing](#-stream-processing) <sub>6</sub> <br>
[◾ YouTube](#-youtube) <sub>6</sub> <br>
[◾ Mais links](#-mais-links) <sub>83</sub> <br>
[🧾 Fontes desta área](#-fontes-desta-área)

## ⭐ Comece por aqui

- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) - Curso gratuito e aberto que constrói um pipeline completo com Docker, Terraform, dbt, Spark e Kafka. <sub>curso</sub>
- [roadmap.sh - Data Engineer](https://roadmap.sh/data-engineer) - Roteiro interativo do que estudar para se tornar engenheiro de dados.
- [Microsoft Learn - Engenheiro de Dados](https://learn.microsoft.com/pt-br/training/career-paths/data-engineer) - Trilha oficial e gratuita em português com módulos de engenharia de dados no Azure. <sub>pt-BR · curso</sub>
- [Designing Data-Intensive Applications](https://dataintensive.net/) - Livro de Martin Kleppmann sobre os fundamentos de sistemas de dados distribuídos, armazenamento e streaming. <sub>livro</sub>
- [Big Book of Data Engineering](https://www.databricks.com/resources/ebook/big-book-of-data-engineering) - Ebook gratuito da Databricks com padrões e casos práticos de pipelines e lakehouse. <sub>livro</sub>
- [Documentação do Apache Airflow](https://airflow.apache.org/docs/) - Documentação oficial do orquestrador de pipelines mais usado do mercado.
- [Documentação do Apache Spark](https://spark.apache.org/docs/latest/) - Documentação oficial do motor de processamento distribuído, incluindo PySpark e Spark SQL.
- [Documentação do Apache Kafka](https://kafka.apache.org/documentation/) - Documentação oficial da plataforma de streaming de eventos, com Kafka Connect e Kafka Streams.
- [dbt Developer Hub](https://docs.getdbt.com/) - Documentação, guias e boas práticas do dbt para transformação de dados em SQL.
- [DuckDB](https://duckdb.org/) - Banco analítico embutido que consulta Parquet e CSV localmente com SQL, sem cluster.
- [Apache Iceberg](https://iceberg.apache.org/) - Formato de tabela aberto para data lakes com evolução de esquema e time travel.
- [Delta Lake](https://delta.io/) - Framework open source que traz transações ACID e versionamento para data lakes.
- [Dagster](https://dagster.io/) - Orquestrador moderno focado em ativos de dados, linhagem e observabilidade.
- [Prefect](https://www.prefect.io/) - Orquestrador de workflows em Python com agendamento, retentativas e monitoramento.
- [Airbyte](https://airbyte.com/) - Plataforma open source de ingestão de dados (ELT) com centenas de conectores.
- [Start Data Engineering](https://www.startdataengineering.com/) - Artigos práticos sobre design de pipelines, SQL, Airflow, dbt e boas práticas.
- [Data Engineering Weekly](https://www.dataengineeringweekly.com/) - Newsletter semanal com curadoria de artigos e novidades de engenharia de dados.
- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/) - Podcast semanal com entrevistas sobre bancos, pipelines e infraestrutura de dados. <sub>canal</sub>
- [Programação Dinâmica](https://www.youtube.com/@pgdinamica) - Canal brasileiro sobre programação, dados e IA, com conteúdo de Python e pipelines. <sub>pt-BR · canal</sub>
- [Seattle Data Guy](https://www.youtube.com/@SeattleDataGuy) - Canal sobre arquitetura de dados, ferramentas do modern data stack e carreira. <sub>canal</sub>

## 🤖 IA para Engenharia de Dados

> Ferramentas, skills, MCPs, cursos, guias de prompt e uso responsável de IA para quem trabalha com engenharia de dados. Veja também [🤖 IA para todas as áreas](../../ia/README.md).

### Essenciais de IA

- [Genie Code (Databricks)](https://docs.databricks.com/aws/pt/notebooks/databricks-assistant-faq) - Documentação do assistente de IA da Databricks que gera código, constrói pipelines e dashboards e depura erros no workspace. <sub>pt-BR</sub>
- [Gemini no BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview?hl=pt-br) - Documentação oficial da IA do BigQuery: geração de SQL, preparação de dados e análise conversacional. <sub>pt-BR</sub>
- [Copilot no Data Factory (Microsoft Fabric)](https://learn.microsoft.com/pt-br/fabric/data-factory/copilot-fabric-data-factory) - Documentação oficial do Copilot para criar integrações de dados e Dataflow Gen2 em linguagem natural no Fabric. <sub>pt-BR</sub>
- [Snowflake Cortex AI](https://docs.snowflake.com/en/guides-overview-ai-features) - Visão geral das funções de IA do Snowflake (Cortex Agents, AI Functions, Analyst, Search) executadas dentro do perímetro do warehouse.
- [dbt Wizard (antigo dbt Copilot)](https://docs.getdbt.com/docs/cloud/dbt-copilot) - Agente de IA da plataforma dbt que gera modelos, testes, documentação e métricas a partir do contexto do projeto; pago, com teste.
- [dbt MCP Server](https://github.com/dbt-labs/dbt-mcp) - Servidor MCP oficial da dbt Labs que expõe projeto, lineage, métricas e comandos do dbt para agentes de IA; código aberto.
- [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox) - Servidor MCP de código aberto do Google para conectar agentes a bancos como Postgres, MySQL, BigQuery e Spanner com segurança e pool de conexões.
- [Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp) - Servidor MCP para PostgreSQL com análise de saúde do banco, explicação de planos e recomendação de índices; código aberto.
- [Airflow AI SDK](https://github.com/astronomer/airflow-ai-sdk) - SDK da Astronomer para chamar LLMs e agentes como tarefas de DAGs do Apache Airflow; código aberto.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Biblioteca de ETL para documentos não estruturados (PDF, HTML, Word) que prepara dados para RAG e LLMs; código aberto.

### Mais ferramentas e recursos de IA

- [Weaviate](https://github.com/weaviate/weaviate) - [Beginner Guide]
- [DeepLearning.AI — Introduction to Data Engineering](https://www.deeplearning.ai/courses/introduction-to-data-engineering) - Curso curto e gratuito sobre os fundamentos do ciclo de vida da engenharia de dados. <sub>pt-BR</sub>
- [Rivestack](https://rivestack.io/) - Managed PostgreSQL with pgvector for AI workloads. HNSW indexing, sub-4ms latency, and built-in SQL editor with automatic embedding generation.
- [ArcadeDB](https://arcadedb.com/) - open-source multi-model database with native vector embedding support alongside graph, document, key-value and time series models
- [Didática Tech](https://www.youtube.com/@didaticatech) - Cursos e explicações gratuitas em português sobre dados, machine learning e programação. <sub>pt-BR · canal</sub>
- [zvec](https://github.com/alibaba/zvec) - An embedded vector database for on-device RAG and edge AI, the SQLite of vector databases.
- [Chroma](https://github.com/chroma-core/chroma) - AI memory with semantic, full-text, & regex search
- [Monte Carlo](https://montecarlo.ai/) - Plataforma de observabilidade de dados (data + AI observability), que detecta quebras de pipeline antes do usuário final.
- [pdfmux](https://github.com/NameetP/pdfmux) - Python PDF-to-Markdown orchestrator. Classifies each page and routes to the optimal backend (PyMuPDF, Docling, RapidOCR, Gemini Flash), emitting Markdown plus a per-page confidence score so ingestion pipelines can quarantine low-trust pages before feeding LLMs or retrieval.
- [Meilisearch](https://github.com/meilisearch) - Search engine API for Semantic (vectors), full-text & hybrid search
- [GitHub Copilot](https://github.com/features/copilot) - Cursor e Claude Code aceleram a escrita de DAGs, modelos dbt e testes de qualidade — mas sempre rode em um ambiente de teste antes de aplicar em um pipeline de produção. <sub>pt-BR</sub>
- [Xquik](https://xquik.com/) - Real-time X (Twitter) data extraction platform with REST API (76 endpoints), 20 bulk extraction tools, account monitoring, HMAC-signed webhooks, and MCP server for AI agent integration.
- [arroy](https://github.com/meilisearch/arroy) - Approximate Nearest Neighbors Rust library
- [dbt Wizard (antigo dbt Copilot)](https://www.getdbt.com/product/dbt-wizard) - gera e explica modelos, testes e documentação direto dentro do projeto dbt, com o contexto do seu catálogo real. <sub>pt-BR</sub>
- [Duckle](https://github.com/SouravRoy-ETL/duckle) - Local-first, open-source desktop ETL/ELT studio: drag a pipeline onto a canvas (or describe it to a built-in on-device AI assistant) and run it at native speed through DuckDB. 290+ connectors, a scheduler, and an MCP server for driving pipelines from an LLM. No cloud, no servers.
- [brinicle](https://github.com/bicardinal/brinicle) - Resource-efficient C++ vector index engine built for low-RAM production workloads
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - é o padrão aberto por trás da maioria desses servidores — vale entender a especificação antes de conectar um agente a dados de produção. <sub>pt-BR</sub>
- [Rawbbit](https://github.com/mirlan-irokez/rawbbit) - Open-source self-hosted game analytics pipeline. HTTP event collector with NATS JetStream buffering, raw Parquet in object storage you own, and ClickHouse for queries via Metabase, SQL, or a read-only MCP server for AI agents. Designed for teams that want to own their raw game data.
- [VelesDB](https://github.com/cyberlife-coder/VelesDB) - Embedded vector + graph + columnar database. Rust core (~6MB), HNSW with 5 distance metrics, VelesQL (SQL + NEAR + MATCH). Python and Rust SDKs.
- [AKF](https://github.com/HMAKT99/AKF) - The AI native file format. Trust scores, source provenance, and compliance metadata that embed into 20+ formats (DOCX, PDF, images, code). EXIF for AI.
- [SimSIMD](https://github.com/ashvardanian/SimSIMD) - Efficient Alternative to scipy.spatial.distance and numpy.inner
- [CocoIndex](https://github.com/cocoindex-io/cocoindex) - An open source ETL framework to build fresh index for AI.
- [vector-io](https://github.com/AI-Northstar-Tech/vector-io) - Comprehensive Vector Data Tooling.
- [Spark](https://spark.apache.org/) - A multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.
- [VectorDBZ](https://github.com/vectordbz/vectordbz) - GUI desktop app for exploring and debugging vector databases
- [H2O](https://www.h2o.ai/) - Fast scalable machine learning API for smarter applications.
- [Results of the Big ANN: NeurIPS'23 competition.](https://arxiv.org/pdf/2409.17424) - " arXiv preprint arXiv:2409.17424 (2024). <sub>artigo científico</sub>
- [Mahout](https://mahout.apache.org/) - An environment for quickly creating scalable performant machine learning applications.
- [Approximate nearest neighbor search on high dimensional data—experiments, analyses, and improvement](https://arxiv.org/pdf/1610.02455.pdf) - " IEEE Transactions on Knowledge and Data Engineering 32.8 (2019): 1475-1488. <sub>artigo científico</sub>
- [Spark MLlib](https://spark.apache.org/docs/latest/ml-guide.html) - Spark's scalable machine learning library consisting of common learning algorithms and utilities, including classification, regression, clustering, collaborative filtering, dimensionality reduction, as well as underlying optimization primitives.

## ◾ Engines and Platforms

- [Aeron](https://github.com/aeron-io/aeron)
- [Apache Apex](https://github.com/apache/apex-core)
- [Apache Flink](https://github.com/apache/flink)
- [Apache Heron](https://github.com/apache/incubator-heron)
- [Apache Kafka](https://github.com/apache/kafka)
- [Apache Pulsar](https://github.com/apache/pulsar)
- [Apache RocketMQ](https://github.com/apache/rocketmq)

## ◾ Applications and Tools

- [beava](https://github.com/beava-dev/beava)
- [Eventum](https://github.com/eventum-generator/eventum)
- [javactrl-kafka](https://github.com/javactrl/javactrl-kafka)
- [Nussknacker](https://github.com/TouK/nussknacker)
- [straw](https://github.com/rwalk/straw)
- [StreamAlert](https://github.com/airbnb/streamalert)

## ◾ Bancos de dados

- [RQLite](https://github.com/rqlite/rqlite) - Replicated SQLite using the Raft consensus protocol.
- [MySQL](https://www.mysql.com/) - The world's most popular open source database.
- [TiDB](https://github.com/pingcap/tidb) - A distributed NewSQL database compatible with MySQL protocol.
- [Percona XtraBackup](https://www.percona.com/software/mysql-database/percona-xtrabackup) - A free, open source, complete online backup solution for all versions of Percona Server, MySQL® and MariaDB®.
- [mysql_utils](https://github.com/pinterest/mysql_utils) - Pinterest MySQL Management Tools.
- [MariaDB](https://mariadb.org/) - An enhanced, drop-in replacement for MySQL.

## ◾ Data Engineering blogs of companies

- [Netflix](https://netflixtechblog.com/tagged/big-data)
- [Uber](https://www.uber.com/blog/houston/data/?uclick_id=b2f43229-f3f4-4bae-bd5d-10a05db2f70c)
- [Databricks](https://www.databricks.com/blog/category/engineering/data-engineering)
- [Airbnb](https://medium.com/airbnb-engineering/data/home)
- [Amazon AWS Blog](https://aws.amazon.com/blogs/big-data/) <sub>livro</sub>
- [Microsoft Data Architecture Blogs](https://techcommunity.microsoft.com/t5/data-architecture-blog/bg-p/DataArchitectureBlog)

## ◾ Data Engineering Whitepapers

- [A Five-Layered Business Intelligence Architecture](https://ibimapublishing.com/articles/CIBIMA/2011/695619/695619.pdf)
- [Lakehouse:A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)
- [Big Data Quality: A Data Quality Profiling Model](https://link.springer.com/chapter/10.1007/978-3-030-23381-5_5)
- [The Data Lakehouse: Data Warehousing and More](https://arxiv.org/abs/2310.08697) <sub>artigo científico</sub>
- [Spark: Cluster Computing with Working Sets](https://dl.acm.org/doi/10.5555/1863103.1863113)
- [The Google File System](https://research.google/pubs/the-google-file-system/)

## ◾ Data Ingestion

- [DataSpoc Pipe](https://github.com/dataspoclab/dataspoc-pipe) - Data ingestion engine that connects 400+ Singer taps to Parquet files in cloud buckets (S3, GCS, Azure). Streaming, incremental, with auto-catalog.
- [Enrich.sh](https://enrich.sh/) - Managed event ingestion service that converts JSON sent to a REST API into Hive-partitioned Parquet on Cloudflare R2, queryable from DuckDB, ClickHouse, BigQuery, Snowflake, and Python.
- [enrich-companies](https://github.com/Alessandro114/enrich-companies) - CLI tool to enrich CSV files with company data (financials, contacts, metadata) from 250M+ company records. Available on npm.
- [ingestr](https://github.com/bruin-data/ingestr) - CLI tool to copy data between databases with a single command. Supports 50+ sources including PostgreSQL, MySQL, MongoDB, Salesforce, Shopify to any data warehouse.
- [Kafka](https://kafka.apache.org/) - Publish-subscribe messaging rethought as a distributed commit log.
- [BottledWater](https://github.com/confluentinc/bottledwater-pg) - Change data capture from PostgreSQL into Kafka. Deprecated.

## ◾ File System

- [HDFS](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) - A distributed file system designed to run on commodity hardware.
- [Snakebite](https://github.com/spotify/snakebite) - A pure python HDFS client.
- [AWS S3](https://aws.amazon.com/s3/) - Object storage built to retrieve any amount of data from anywhere. <sub>livro</sub>
- [smart_open](https://github.com/RaRe-Technologies/smart_open) - Utils for streaming large files (S3, HDFS, gzip, bz2).
- [Alluxio](https://www.alluxio.org/) - A memory-centric distributed storage system enabling reliable data sharing at memory-speed across cluster frameworks, such as Spark and MapReduce.
- [CEPH](https://ceph.com/) - A unified, distributed storage system designed for excellent performance, reliability, and scalability.

## ◾ LinkedIn

- [Zach Wilson](https://www.linkedin.com/in/eczachly)
- [Chip Huyen](https://www.linkedin.com/in/chiphuyen/)
- [Shashank Mishra](https://www.linkedin.com/in/shashank219/)
- [Ben Rogojan](https://www.linkedin.com/in/benjaminrogojan)
- [Sumit Mittal](https://www.linkedin.com/in/bigdatabysumit/)
- [Darshil Parmar](https://www.linkedin.com/in/darshil-parmar/)

## ◾ Managed and Closed Source

- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) <sub>livro</sub>
- [Azure Stream Analytics](https://azure.microsoft.com/en-us/products/stream-analytics)
- [Concord](https://www.slideshare.net/concord-io/may-2016-data-by-the-bay-concord-simple-flexible-stream-processing-on-apache-mesos)
- [Google Cloud Dataflow](https://cloud.google.com/dataflow/)
- [IBM Streams](https://www.ibm.com/support/pages/ibm-streams-life-cycle-guidance)
- [NVIDIA DeepStream SDK](https://developer.nvidia.com/deepstream-sdk)

## ◾ Stream Processing

- [Apache Beam](https://beam.apache.org/) - A unified programming model that implements both batch and streaming data processing jobs that run on many execution engines.
- [Spark Streaming](https://spark.apache.org/streaming/) - Makes it easy to build scalable fault-tolerant streaming applications.
- [Apache Flink](https://flink.apache.org/) - A streaming dataflow engine that provides data distribution, communication, and fault tolerance for distributed computations over data streams.
- [Apache Storm](https://storm.apache.org/) - A free and open source distributed realtime computation system.
- [Apache Samza](https://samza.apache.org/) - A distributed stream processing framework.
- [Apache NiFi](https://nifi.apache.org/) - An easy to use, powerful, and reliable system to process and distribute data.

## ◾ YouTube

- [ByteByteGo](https://www.youtube.com/c/ByteByteGo) <sub>canal</sub>
- [Data with Baraa](https://www.youtube.com/@DataWithBaraa) <sub>canal</sub>
- [Data with Zach](https://www.youtube.com/@eczachly_) <sub>canal</sub>
- [E-learning Bridge](https://www.youtube.com/@shashank_mishra) <sub>canal</sub>
- [Seattle Data Guy](https://www.youtube.com/c/SeattleDataGuy) <sub>canal</sub>
- [TrendyTech](https://www.youtube.com/c/TrendytechInsights) <sub>canal</sub>

## ◾ Mais links

- [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering) - Lista curada de frameworks, ferramentas e recursos de engenharia de dados, organizada por categoria. <sub>lista awesome</sub>
- [Databricks — O que é engenharia de dados?](https://www.databricks.com/glossary/data-engineering) - Explicação oficial da Databricks sobre o papel da engenharia de dados no ciclo de vida dos dados. <sub>pt-BR</sub>
- [IBM — What is data engineering?](https://www.ibm.com/think/topics/data-engineering) - Introdução da IBM aos conceitos, ferramentas e responsabilidades de quem trabalha com engenharia de dados. <sub>pt-BR</sub>
- [Google Cloud — O que é engenharia de dados?](https://cloud.google.com/learn/what-is-data-engineering) - Visão geral oficial do Google Cloud sobre pipelines, ingestão e transformação de dados. <sub>pt-BR</sub>
- [Fundamentals of Data Engineering](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302/) <sub>livro</sub>
- [Designing Data-Intensive Applications](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321/) <sub>livro</sub>
- [Designing Machine Learning Systems](https://www.amazon.com/Designing-Machine-Learning-Systems-Production-Ready/dp/1098107969) <sub>livro</sub>
- [manuzhang.github.io/awesome-streaming](https://manuzhang.github.io/awesome-streaming/)
- [DataExpert.io Community Discord](https://discord.gg/JGumAXncAK) <sub>comunidade</sub>
- [Data Talks Club Slack](https://datatalks.club/slack)
- [Data Engineer Things Community](https://www.dataengineerthings.org/)
- [AdalFlow Discord](https://discord.com/invite/ezzszrRZvT) <sub>comunidade</sub>
- [Chip Huyen MLOps Discord](https://discord.gg/dzh728c5t3) <sub>comunidade</sub>
- [Apache Airflow — Core concepts: DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html) - Conceito central do Airflow: como definir e organizar um DAG (grafo de tarefas).
- [Apache Airflow — Best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) - Guia oficial de boas práticas para escrever DAGs testáveis e fáceis de manter.
- [Dagster — Documentação](https://docs.dagster.io/) - Documentação do orquestrador moderno com foco em ativos de dados (data assets), testes e observabilidade. <sub>pt-BR</sub>
- [Prefect — Documentação](https://docs.prefect.io/) - Documentação oficial do Prefect, orquestrador Python com foco em simplicidade e resiliência a falhas. <sub>pt-BR</sub>
- [Mage — Documentação](https://docs.mage.ai/) - Documentação oficial do Mage, ferramenta de pipelines de dados com editor visual e blocos de código. <sub>pt-BR</sub>
- [datacompy](https://github.com/capitalone/datacompy) - A Python library that facilitates the comparison of two DataFrames in Pandas, Polars, Spark and more. The library goes beyond basic equality checks by providing detailed insights into discrepancies at both row and column levels.
- [dvt](https://github.com/GoogleCloudPlatform/professional-services-data-validator) - Data Validation Tool compares data from source and target tables to ensure that they match. It provides column validation, row validation, schema validation, custom query validation, and ad hoc SQL exploration.
- [koala-diff](https://github.com/godalida/koala-diff) - A high-performance Python library for comparing large datasets (CSV, Parquet) locally using Rust and Polars. It features zero-copy streaming to prevent OOM errors and generates interactive HTML data quality reports.
- [FutureSearch SDK](https://github.com/futuresearch/futuresearch-python) - Python SDK that dispatches parallel web-research agents across
- [Akka](https://github.com/akka/akka-core)
- [Apache Beam](https://github.com/apache/beam)
- [Apache Edgent](https://github.com/apache/incubator-retired-edgent)
- [Apache Pekko](https://github.com/apache/pekko)
- [Mage](https://www.mage.ai/)
- [Astronomer](https://www.astronomer.io/)
- [Airflow](https://airflow.apache.org/)
- [Kestra](https://kestra.io/)
- [Alura — Formação Engenheiro(a) de Dados](https://www.alura.com.br/formacao-engenheiro-dados) - Trilha completa de engenharia de dados: Python, Spark, Airflow e cloud. Curso pago. <sub>pt-BR · curso</sub>
- [Alura — Airflow: orquestração de pipelines de dados](https://www.alura.com.br/curso-online-airflow-orquestracao-pipelines-dados) - Curso pago dedicado à criação e orquestração de DAGs no Apache Airflow. <sub>pt-BR · curso</sub>
- [Alura — dbt: modelagem de dados em projeto analítico](https://www.alura.com.br/curso-online-dbt-modelagem-dados-projeto-analitico) - Curso pago sobre transformação e modelagem de dados com dbt dentro de um projeto analítico real. <sub>pt-BR · curso</sub>
- [DIO — Trilhas e bootcamps](https://www.dio.me/) - Portal com trilhas e bootcamps gratuitos de engenharia de dados, com certificado. <sub>pt-BR · curso</sub>
- [dbt Labs — dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) - Curso oficial e gratuito da dbt Labs: modelagem, testes, documentação e deploy de projetos dbt. <sub>pt-BR</sub>
- [Apache Flume](https://github.com/apache/logging-flume)
- [Brooklin](https://github.com/linkedin/Brooklin)
- [Bruin](https://github.com/bruin-data/bruin)
- [Camus](https://github.com/LinkedInAttic/camus)
- [Databus](https://github.com/linkedin/databus)
- [Fundamentals of Data Engineering — Joe Reis, Matt Housley](https://www.amazon.com.br/dp/1098108302) - Livro de referência (2022) que define o ciclo de vida completo da engenharia de dados moderna. Livro pago. <sub>pt-BR · livro</sub>
- [Data Pipelines with Apache Airflow — Bas Harenslak, Julian de Ruiter (Manning)](https://www.manning.com/books/data-pipelines-with-apache-airflow) - Referência prática para construir, testar e monitorar pipelines com Airflow. Livro pago.
- [The Data Warehouse Toolkit — Ralph Kimball](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) - O clássico sobre modelagem dimensional, referência para qualquer pipeline que alimenta um data warehouse. Livro pago.
- [Data Hackers](https://www.youtube.com/@datahackers) - Canal da maior comunidade de dados do Brasil: entrevistas, carreira e conteúdo técnico sobre engenharia de dados. <sub>canal</sub>
- [Téo Calvo](https://www.youtube.com/@teocalvo) - Conteúdo prático de análise e engenharia de dados, com foco em SQL, Python e ferramentas do dia a dia. <sub>canal</sub>
- [Neylson Crepalde](https://www.youtube.com/@neylsoncrepalde) - Estatística, dados e engenharia de dados explicados por um cientista de dados brasileiro. <sub>canal</sub>
- [DataTalksClub](https://www.youtube.com/@DataTalksClub) - Canal com lives, entrevistas e o curso completo de engenharia de dados em vídeo. <sub>canal</sub>
- [Data Hackers Podcast](https://www.datahackers.com.br/podcast/) - Podcast da comunidade Data Hackers: mercado, carreira e engenharia de dados no Brasil. <sub>pt-BR</sub>
- [dbt Labs Blog](https://www.getdbt.com/blog) - Blog oficial da dbt Labs sobre analytics engineering, modelagem e o ecossistema dbt.
- [Astronomer Blog](https://www.astronomer.io/blog/) - Blog oficial da Astronomer com tutoriais e novidades do Apache Airflow.
- [Airbnb Tech Blog](https://airbnb.tech/) - Blog de engenharia do Airbnb, com posts sobre a plataforma de dados que originou o Apache Hudi.
- [Seattle Data Guy — Blog](https://www.theseattledataguy.com/) - Blog e newsletter sobre carreira e arquitetura de dados, por um engenheiro de dados experiente.
- [Monte Carlo Blog](https://montecarlo.ai/blog) - Blog sobre observabilidade e qualidade de dados, mantido pela empresa criadora do conceito de "data downtime".
- [Apache Avro](https://avro.apache.org/) - Apache Avro™ is a data serialization system.
- [Apache Parquet](https://parquet.apache.org/) - A columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language.
- [Snappy](https://github.com/google/snappy) - A fast compressor/decompressor. Used with Parquet.
- [PigZ](https://zlib.net/pigz/) - A parallel implementation of gzip for modern multi-processor, multi-core machines.
- [Apache ORC](https://orc.apache.org/) - The smallest, fastest columnar storage for Hadoop workloads.
- [dbt Labs — jaffle_shop](https://github.com/dbt-labs/jaffle-shop) - Projeto de demonstração oficial do dbt: uma loja fictícia para praticar modelagem, testes e documentação. <sub>pt-BR</sub>
- [Base dos Dados](https://basedosdados.org/) - Dados públicos brasileiros tratados e disponíveis via SQL no BigQuery — ótimo para praticar pipelines com dados reais do Brasil.
- [Portal Brasileiro de Dados Abertos](https://dados.gov.br/) - Dados públicos reais do governo brasileiro para carregar em pipelines de teste. <sub>pt-BR</sub>
- [Flotilla](https://github.com/tylertreat/Flotilla)
- [storm-perf-test](https://github.com/yahoo/storm-perf-test)
- [streaming-benchmarks](https://github.com/yahoo/streaming-benchmarks)
- [State of Data Brazil 2024/2025 (Data Hackers + Bain)](https://www.datahackers.news/p/relatorio2024-2025) - Maior pesquisa do mercado brasileiro de dados: salários, cargos, ferramentas e contratação. <sub>pt-BR</sub>
- [Salario.com.br — Engenheiro de Dados](https://www.salario.com.br/profissao/engenheiro-de-dados-cbo-212205/) - Salário médio, piso e teto de engenheiro de dados com base em dados oficiais do CAGED. <sub>pt-BR</sub>
- [Programathor — vagas de engenharia de dados](https://programathor.com.br/jobs-data-engineering) - Vagas de tecnologia no Brasil filtradas por engenharia de dados. <sub>pt-BR</sub>
- [Remotar](https://remotar.com.br/) - Vagas 100% remotas para brasileiros, incluindo engenharia de dados. <sub>pt-BR</sub>
- [RemoteOK — vagas de engenharia de dados](https://remoteok.com/remote-data-engineer-jobs) - Vagas remotas internacionais filtradas por engenharia de dados.
- [In-Stream Big Data Processing](https://highlyscalable.wordpress.com/2013/08/20/in-stream-big-data-processing/)
- [The world beyond batch: Streaming 101](http://radar.oreilly.com/2015/08/the-world-beyond-batch-streaming-101.html)
- [Real Time Analytics: Algorithms and Systems (VLDB 2015)](https://arxiv.org/abs/1708.02621) <sub>artigo científico</sub>
- [Grokking Streaming Systems](https://www.manning.com/books/grokking-streaming-systems)
- [Streaming Systems: The What, Where, When, and How of Large-Scale Data Processing](https://www.oreilly.com/library/view/streaming-systems/9781491983867/) <sub>livro</sub>
- [Hadoop MapReduce](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) - A software framework for easily writing applications which process vast amounts of data (multi-terabyte data-sets) - in-parallel on large clusters (thousands of nodes) - of commodity hardware in a reliable, fault-tolerant manner.
- [Spark Packages](https://spark-packages.org/) - A community index of packages for Apache Spark.
- [Deep Spark](https://github.com/Stratio/deep-spark) - Connecting Apache Spark with different data stores. Deprecated.
- [Spark RDD API Examples](https://homepage.cs.latrobe.edu.au/zhe/ZhenHeSparkRDDAPIExamples.html) - Examples by Zhen He.
- [Data Hackers](https://www.datahackers.com.br/) - A maior comunidade de dados do Brasil, com Slack, eventos e newsletter. <sub>pt-BR</sub>
- [r/dataengineering](https://www.reddit.com/r/dataengineering/) - A maior comunidade internacional de engenharia de dados, com discussões diárias sobre ferramentas e carreira. <sub>pt-BR · comunidade</sub>
- [dbt Community](https://www.getdbt.com/community/join-the-community) - Comunidade oficial da dbt Labs, com Slack ativo e o evento anual Coalesce.
- [alexxubyte](https://twitter.com/alexxubyte/)
- [@dankornas](https://www.twitter.com/dankornas)

## 🧾 Fontes desta área

Os links acima (fora os essenciais) foram reunidos destas listas curadas. Obrigado a quem as mantém.

- [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) <sub>38 links · licença sem-licenca</sub>
- [arthurspk/guiadeengenhariadedados](https://github.com/arthurspk/guiadeengenhariadedados) <sub>38 links · licença MIT</sub>
- [dangkhoasdc/awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) <sub>0 links · licença CC0-1.0</sub>
- [igorbarinov/awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering) <sub>37 links · licença CC0-1.0</sub>
- [manuzhang/awesome-streaming](https://github.com/manuzhang/awesome-streaming) <sub>37 links · licença sem-licenca</sub>

---
[⬆️ Voltar ao topo](#-engenharia-de-dados) · [← Dados e Inteligência Artificial](README.md)
