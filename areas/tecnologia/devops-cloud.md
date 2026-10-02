# ☁️ DevOps e Cloud

> CI/CD, containers, Kubernetes, IaC, AWS, Azure, GCP e SRE. **303 links** nesta área: 19 essenciais escolhidos a dedo, 43 de inteligência artificial e 241 reunidos de 10 listas curadas.

[← 💻 Tecnologia e Desenvolvimento](README.md) · [🗂️ Catálogo completo](../CATALOGO.md) · [🏠 Início](../../README.md)

## 📚 Índice

[⭐ Comece por aqui](#-comece-por-aqui) <sub>19</sub> <br>
[🤖 IA para DevOps e Cloud](#-ia-para-devops-e-cloud) <sub>43</sub> <br>
[◾ Ferramentas para hospedar seu site](#-ferramentas-para-hospedar-seu-site) <sub>24</sub> <br>
[◾ Automation and CI/CD](#-automation-and-cicd) <sub>6</sub> <br>
[◾ Beginner Guides](#-beginner-guides) <sub>6</sub> <br>
[◾ Build And Release System](#-build-and-release-system) <sub>6</sub> <br>
[◾ Builder](#-builder) <sub>6</sub> <br>
[◾ Cloud Platforms](#-cloud-platforms) <sub>6</sub> <br>
[◾ CloudFormation](#-cloudformation) <sub>6</sub> <br>
[◾ CloudWatch](#-cloudwatch) <sub>6</sub> <br>
[◾ Cluster Provisioning](#-cluster-provisioning) <sub>6</sub> <br>
[◾ Cluster Resources Management](#-cluster-resources-management) <sub>6</sub> <br>
[◾ Code Pipeline](#-code-pipeline) <sub>6</sub> <br>
[◾ Command Line Tools](#-command-line-tools) <sub>6</sub> <br>
[◾ Docker](#-docker) <sub>6</sub> <br>
[◾ Engine & Runtime](#-engine--runtime) <sub>6</sub> <br>
[◾ How-To](#-how-to) <sub>6</sub> <br>
[◾ Mais links](#-mais-links) <sub>133</sub> <br>
[🧾 Fontes desta área](#-fontes-desta-área)

## ⭐ Comece por aqui

- [roadmap.sh - DevOps](https://roadmap.sh/devops) - Roteiro visual de estudos para DevOps.
- [Docker - Get started](https://docs.docker.com/get-started/) - Guia oficial para começar com containers, imagens e Compose.
- [Kubernetes (pt-BR)](https://kubernetes.io/pt-br/docs/home/) - Documentação oficial do Kubernetes em português. <sub>pt-BR</sub>
- [Descomplicando Kubernetes](https://github.com/badtuxx/DescomplicandoKubernetes) - Livro/curso aberto em português sobre Kubernetes, da LINUXtips. <sub>pt-BR</sub>
- [LINUXtips](https://www.youtube.com/@LinuxTips) - Canal brasileiro sobre Linux, DevOps, containers e Kubernetes. <sub>pt-BR · canal</sub>
- [Terraform Tutorials](https://developer.hashicorp.com/terraform/tutorials) - Tutoriais oficiais de infraestrutura como código com Terraform. <sub>curso</sub>
- [Ansible](https://docs.ansible.com/) - Documentação da ferramenta de automação e gerência de configuração.
- [GitHub Actions](https://docs.github.com/pt/actions) - Documentação em português de CI/CD com GitHub Actions. <sub>pt-BR</sub>
- [AWS Skill Builder](https://skillbuilder.aws/) - Centenas de cursos gratuitos da AWS e preparação para certificações. <sub>curso</sub>
- [Microsoft Learn - Azure](https://learn.microsoft.com/pt-br/training/azure/) - Trilhas gratuitas de Azure em português, incluindo AZ-900. <sub>pt-BR · curso</sub>
- [Google Skills](https://www.skills.google/) - Plataforma do Google com treinamentos de Google Cloud e IA. <sub>curso</sub>
- [Google SRE Books](https://sre.google/books/) - Livros do Google sobre Site Reliability Engineering, com leitura online gratuita. <sub>livro</sub>
- [Prometheus](https://prometheus.io/docs/introduction/overview/) - Documentação do sistema de monitoramento e alertas por métricas.
- [Grafana Docs](https://grafana.com/docs/) - Documentação de Grafana, Loki, Tempo e demais ferramentas de observabilidade.
- [CNCF Landscape](https://landscape.cncf.io/) - Mapa interativo das ferramentas do ecossistema cloud native.
- [Killercoda](https://killercoda.com/) - Laboratórios interativos no navegador de Linux, Kubernetes e DevOps.
- [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way) - Tutorial que monta um cluster Kubernetes manualmente para entender cada peça.
- [90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps) - Jornada de estudos de DevOps em 90 dias, aberta e gratuita.
- [DevOps Exercises](https://github.com/bregman-arie/devops-exercises) - Centenas de perguntas e exercícios de DevOps, Linux, cloud e redes.

## 🤖 IA para DevOps e Cloud

> Ferramentas, skills, MCPs, cursos, guias de prompt e uso responsável de IA para quem trabalha com devops e cloud. Veja também [🤖 IA para todas as áreas](../../ia/README.md).

### Essenciais de IA

- [K8sGPT](https://github.com/k8sgpt-ai/k8sgpt) - CLI e operador open source que varre clusters Kubernetes e explica problemas em linguagem natural.
- [kubectl-ai](https://github.com/GoogleCloudPlatform/kubectl-ai) - Assistente de IA no terminal que traduz pedidos em comandos e operações kubectl.
- [HolmesGPT](https://github.com/robusta-dev/holmesgpt) - Agente open source (CNCF) que investiga incidentes de produção e aponta a causa raiz em Kubernetes, VMs e nuvem.
- [Terraform MCP Server](https://github.com/hashicorp/terraform-mcp-server) - Servidor MCP oficial da HashiCorp que dá a agentes acesso ao Terraform Registry para gerar IaC correta.
- [AWS MCP Servers](https://github.com/awslabs/mcp) - Coleção oficial de servidores MCP da AWS para documentação, IaC, custos e serviços da nuvem.
- [Microsoft MCP (Azure MCP Server)](https://github.com/microsoft/mcp) - Repositório oficial dos servidores MCP da Microsoft, incluindo o Azure MCP Server.
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) - Assistente de IA da AWS para código, operação de recursos na nuvem e transformação de aplicações; tem nível gratuito.
- [Gemini Cloud Assist](https://cloud.google.com/products/gemini/cloud-assist) - Assistente de IA do Google Cloud para projetar, implantar, monitorar, depurar e otimizar custos.
- [Azure Copilot](https://learn.microsoft.com/en-us/azure/copilot/overview) - Documentação do assistente de IA do portal Azure para gerenciar e diagnosticar recursos.
- [Gordon (Docker AI)](https://docs.docker.com/ai/gordon/) - Assistente de IA do Docker que analisa o ambiente, sugere correções e executa comandos com permissão.
- [Docker MCP Catalog e Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) - Catálogo de servidores MCP em contêineres e gateway para gerenciá-los de forma centralizada.
- [Pulumi Neo](https://www.pulumi.com/product/neo/) - Agente de IA da Pulumi para provisionar, governar e otimizar infraestrutura em nuvem; pago.
- [Datadog Bits AI SRE](https://www.datadoghq.com/product/ai/bits-ai-sre/) - Agente de SRE da Datadog que investiga alertas automaticamente e sugere causa raiz; pago.

### Mais ferramentas e recursos de IA

- [D-Bot: Database Diagnosis System using Large Language Models](https://arxiv.org/pdf/2312.01454.pdf) - [project]. -red) <sub>artigo científico</sub>
- [Datadog](https://www.datadoghq.com/) - A monitoring and security platform for cloud applications
- [Alpaca](https://github.com/tatsu-lab/stanford_alpaca) - Code and documentation to train Stanford's Alpaca models, and generate the data.
- [Machine Learning](https://aws.amazon.com/machine-learning/) - Provides managed machine learning technology. <sub>livro</sub>
- [The Claude Agent Skill for Terraform and OpenTofu - testing, modules, CI/CD, and production patterns](https://github.com/antonbabenko/terraform-skill) - Claude Code skill for Terraform and OpenTofu — testing, module design, CI/CD workflows, and production patterns.
- [Kubeflow](https://github.com/kubeflow/kubeflow) - Kubeflow is a Cloud Native platform for machine learning based on Google’s internal machine learning pipelines.
- [DLIA](https://github.com/zorak1103/dlia) - DLIA is an AI-powered Docker log monitoring agent that uses Large Language Models (LLMs) to intelligently analyze container logs, detect anomalies, and provide contextual insights over time.
- [IBM Cloud](https://www.ibm.com/cloud) - Tools, data & APIs to make AI real now.
- [TrioXpert: An Automated Incident Management Framework for Microservice System](https://arxiv.org/abs/2506.10043) - [project] [code]. <sub>artigo científico</sub>
- [听云 TINGYUN](https://www.tingyun.com/lp.html) - 端到端的全平台应用性能管理系统
- [BELLE](https://github.com/LianjiaTech/BELLE) - A 7B Large Language Model fine-tune by 34B Chinese Character Corpus, based on LLaMA and Alpaca.
- [Terraform Academy](https://www.terraformacademy.app/) - Interactive Terraform / IaC learning platform with hands-on labs, certification prep (HashiCorp, AWS, GCP, Azure, Docker, Kubernetes, GitOps), AI coaching, and progress tracking. See also the SRE Pro Tips blog and the mobile/PWA apps below.
- [nos](https://github.com/nebuly-ai/nos) - nos is an open-source platform to efficiently run AI workloads on Kubernetes, increasing GPU utilization and reducing infrastructure and operational costs.
- [Den](https://github.com/us/den) - Self-hosted sandbox runtime for AI agents with Docker containers, security hardening, REST API and WebSocket support.
- [KubeStellar Console](https://console.kubestellar.io/) - Open source AI-powered multi-cluster Kubernetes dashboard with real-time observability, AI-guided operations, and 20+ CNCF integrations (Argo, Kyverno, Prometheus, Grafana, Istio, Flux, Falco, OPA/Gatekeeper). CNCF Sandbox project.
- [OpsAgent: An Evolving Multi-agent System for Incident Management in Microservices](https://arxiv.org/abs/2510.24145) - [project] [code]. <sub>artigo científico</sub>
- [Keep](https://www.keephq.dev/) - Open-source alert management and AIOps platform
- [Bloom](https://github.com/bigscience-workshop/model_card) - BigScience Large Open-science Open-access Multilingual Language Model
- [Terraform Academy — iOS](https://apps.apple.com/us/app/terraform-academy/id6745738634) - Native iOS app for the Terraform Academy interactive learning platform. Hands-on labs, certification prep (HashiCorp, AWS, GCP, Azure, Docker, Kubernetes, GitOps), AI coaching, and progress sync across devices. <sub>app</sub>
- [Gantry (Desktop)](https://github.com/getgantry/gantry) - Native macOS app (SwiftUI, no Electron) for managing and monitoring Docker hosts, local and over SSH: fleet dashboard, live logs and stats, exec terminal, file browser, and a bundled MCP server for AI agents.
- [Qovery](https://www.qovery.com/) - Enterprise Kubernetes management platform for deploying applications on AWS, GCP, Azure, and Scaleway. Includes Terraform provider, CLI, API, and an AI Agent Skill for deploying from AI coding tools like Claude Code, Cursor, and OpenCode.
- [Graph of States: Solving Abductive Tasks with Large Language Models](https://arxiv.org/abs/2603.21250) - [project] [code]. <sub>artigo científico</sub>
- [dolly](https://github.com/databrickslabs/dolly) - Databricks’ Dolly, a large language model trained on the Databricks Machine Learning Platform
- [Terraform Academy — Android](https://play.google.com/store/apps/details?id=com.terraformacade1.app) - Native Android app for the Terraform Academy learning platform with the same labs, cert prep, and AI coaching as the iOS and web versions. <sub>app</sub>
- [Docker Commander](https://github.com/koduj-dev/docker-commander) - A self-hosted Docker management and monitoring UI with multi-host support, Compose management, aggregated logs, alerts, RBAC, vulnerability scanning, and MCP integration.
- [Merlinn](https://github.com/merlinn-co/merlinn) - Open-source AI on-call developer.
- [MicLog: Towards Accurate and Efficient LLM-based Log Parsing via Progressive Meta In-Context Learning](https://ojs.aaai.org/index.php/AAAI/article/view/37123) - [project]. -red)
- [Falcon 40B](https://huggingface.co/tiiuae/falcon-40b-instruct) - Falcon-40B-Instruct is a 40B parameters causal decoder-only model built by TII based on Falcon-40B and finetuned on a mixture of Baize. It is made available under the Apache 2.0 license.
- [terraform-provider-iterative](https://github.com/iterative/terraform-provider-iterative) - Terraform plugin built with machine learning in mind.
- [SBproxy](https://github.com/soapbucket/sbproxy) - AI gateway and reverse proxy with LLM routing, rate limiting, and YAML config.

## ◾ Ferramentas para hospedar seu site

- [Github Pages](https://pages.github.com/) - Hospedado diretamente de seu repositório GitHub. Basta editar, enviar e suas alterações entrarão em vigor <sub>pt-BR</sub>
- [Award Space](https://www.awardspace.com/) - Hospedagem gratuita na web + um subdomínio gratuito, PHP, MySQL, instalador de aplicativo, envio de e-mail e sem anúncios <sub>pt-BR</sub>
- [Byet](https://byet.host/) - Hospedagem Gratuita e Serviços de Hospedagem Premium.
- [Infinity Free](https://infinityfree.net/) - Free Unlimited Web Hosting
- [1FreeHosting](http://www.1freehosting.com/) - Hospedagem de sites grátis com 100GB de largura de banda
- [Amazon Web Services](https://aws.amazon.com/pt/) - Serviço de aluguel de servidores e outros serviços <sub>livro</sub>
- [BlueHost](https://www.bluehost.com/) - Empresa americana de hospedagem de sites
- [DreamHost](https://www.dreamhost.com/) - Hospedagem de sites de alta disponibilidade
- [Embratel](https://www.embratel.com.br/cloud/hospedagem-de-sites) - Hospedagem de sites nacional <sub>pt-BR</sub>
- [GoDaddy](https://br.godaddy.com/hosting/web-hosting) - Hospedagem de sites internacional
- [GoDaddy](https://br.godaddy.com/) - Empresa de aluguel de servidores compartilhados, dedicados e registro de domínio
- [Google Cloud](https://cloud.google.com/solutions/smb/web-hosting/) - Serviço de aluguel de servidores da Google
- [Heroku](https://www.heroku.com/) - Hospedagem de sites grátis com suporte à NodeJS, Java, Ruby, PHP, Python, Go, Scala e Clojure
- [HostGator](https://www.hostgator.com/) - Hospedagem compartilhada e dedicada para sites e serviços
- [Hostinger](https://www.hostinger.com.br/) - Hospedagem de sites <sub>pt-BR</sub>
- [Hostoo](https://hostoo.io/) - Hospedagem de sites em cloud computing dedicado
- [iPage](https://www.ipage.com/) - Hospedagem de sites gringa com descontos para anúncios
- [KingHost](https://king.host/) - Hospedagem compartilhada e dedicada para sites e serviços de marketing por e-mail
- [Netlify](https://www.netlify.com/) - Hospedagem para sites estáticos que combina implantação global, integração contínua e HTTPS automático <sub>pt-BR</sub>
- [One.com](https://www.one.com/pt-BR/) - Serviços gerais digitais (incluindo hospedagem de sites)
- [Oracle Cloud](https://www.oracle.com/br/cloud/) - Serviço de aluguel de servidores da Oracle
- [Surge](https://surge.sh/) - Hospedagem gratuita para páginas estáticas
- [Umbler](https://www.umbler.com/br) - Hospedagem compartilhada, cloud computing sob taxação de uso <sub>pt-BR</sub>
- [Vercel](https://vercel.com/) - Hospedagem grátis de sites estáticos e serveless

## ◾ Automation and CI/CD

- [Argo CD](https://github.com/argoproj/argo-cd) - Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.
- [Argo Events](https://github.com/argoproj/argo-events) - Argo Events is an event-driven workflow automation framework for Kubernetes which helps you trigger K8s objects, Argo Workflows, Serverless workloads, etc.
- [Argo Rollouts](https://github.com/argoproj/argo-rollouts) - Argo Rollouts controller, uses the Rollout custom resource to provide additional deployment strategies such as Blue Green and Canary to Kubernetes.
- [Argo Workflows](https://github.com/argoproj/argo) - Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes.
- [Argocd autopilot](https://github.com/argoproj-labs/argocd-autopilot) - The Argo-CD Autopilot is a tool which offers an opinionated way of installing Argo-CD and managing GitOps repositories.
- [Flagger](https://github.com/weaveworks/flagger) - Flagger is a progressive delivery tool that automates the release process for applications running on Kubernetes.

## ◾ Beginner Guides

- [A Comprehensive Guide to Terraform](https://www.gruntwork.io/blog/a-comprehensive-guide-to-terraform) - Series of blog posts from the author of "Terraform: Up & Running" that guide the reader from beginning with Terraform to using it in the real world.
- [Using Terraform for Cloud Deployments - Part 1](https://dev.to/koenighotze/using-terraform-for-cloud-deployments---part-1) - Provisioning an EC2 instance.
- [Hello, world: The Fargate/Terraform tutorial I wish I had](https://section411.com/2019/07/hello-world/) - Blog post describing setting up an ECS Fargate cluster from scratch
- [Terraform Security Guide](https://sysdig.com/blog/terraform-security-best-practices/) - Blog post describing security best practices when working with Terraform
- [Building a SaaS API? Don't Forget Your Terraform Provider](https://www.speakeasy.com/blog/build-terraform-providers) - Why you should write a terraform provider
- [Complete Terraform Course in French (Free)](https://blog.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/) - A comprehensive and free course in French to master Terraform, from beginner to advanced usage, with hands-on examples and best practices.

## ◾ Build And Release System

- [Jenkins](http://jenkins-ci.org/)
- [Solano CI](https://www.solanolabs.com/)
- [Concourse](https://concourse-ci.org/)
- [BuildForge](https://jazz.net/downloads/rational-build-forge/)
- [ElectricFlow](http://electric-cloud.com/products/electricflow/)
- [Teamcity](http://www.jetbrains.com/teamcity/index.html)

## ◾ Builder

- [ansible-bender](https://github.com/ansible-community/ansible-bender) - A tool utilising ansible and buildah.
- [apko](https://github.com/chainguard-dev/apko) - Declarative OCI image builder from apk packages; reproducible by design.
- [buildah](https://github.com/containers/buildah) - A tool that facilitates building OCI images.
- [BuildKit](https://github.com/moby/buildkit) - Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit.
- [buildx](https://github.com/docker/buildx) - Official Docker CLI plugin for multi-platform builds backed by BuildKit.
- [cekit](https://github.com/cekit/cekit) - A tool used by openshift to build base images using different build engines.

## ◾ Cloud Platforms

- [Amazon Web Services (AWS)](https://aws.amazon.com/) - Cloud Computing Services. <sub>livro</sub>
- [Google Cloud Platform (GCP)](https://cloud.google.com/) - Cloud Computing Services.
- [Azure](https://azure.microsoft.com/) - Cloud Computing Platform & Services.
- [Alibaba Cloud](https://us.alibabacloud.com/) - Integrated suite of cloud products and services.
- [Oracle Cloud](https://www.oracle.com/cloud/) - Comprehensive and fully integrated stack of cloud applications and platform services.
- [DigitalOcean](https://www.digitalocean.com/) - Helping developers easily build, test, manage, and scale applications of any size.

## ◾ CloudFormation

- [aws-cdk](https://github.com/aws/aws-cdk) - Framework for defining cloud infrastructure in code.
- [aws-cfn-custom-resource-examples](https://github.com/awslabs/aws-cfn-custom-resource-examples) - Custom resource examples.
- [aws-cfn-resource-bridge](https://github.com/aws/aws-cfn-resource-bridge) - Custom resource framework.
- [cfn-python-lint](https://github.com/awslabs/cfn-python-lint) - A tool for linting/validating CloudFormation.
- [cfncluster-cookbook](https://github.com/awslabs/cfncluster-cookbook) - Sample Cookbook.
- [cfncluster](https://github.com/awslabs/cfncluster) - Framework that deploys and maintains HPC clusters.

## ◾ CloudWatch

- [cloudwatch-logs-subscription-consumer](https://github.com/awslabs/cloudwatch-logs-subscription-consumer) - Kinesis stream reader.
- [ecs-cloudwatch-logs](https://github.com/awslabs/ecs-cloudwatch-logs) - Assets in the blog post on using Amazon ECS and Amazon CloudWatch logs.
- [logstash-output-cloudwatchlogs](https://github.com/awslabs/logstash-output-cloudwatchlogs) - A logstash plugin that sends logs to CloudWatch.
- [opsworks-cloudwatch-logs-cookbooks](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks) - OpsWorks sample cookbook.
- [jorgebastida/awslogs](https://github.com/jorgebastida/awslogs) - Simple CLI for querying groups, streams and events.
- [newrelic-platform/newrelic_aws_cloudwatch_plugin](https://github.com/newrelic-platform/newrelic_aws_cloudwatch_plugin) - New Relic plugin.

## ◾ Cluster Provisioning

- [Bootkube](https://github.com/kubernetes-sigs/bootkube) - Bootkube is a tool for launching self-hosted Kubernetes clusters.
- [Claudie](https://github.com/berops/claudie) - Multi-cloud clusters with each nodepool in a different cloud provider.
- [Cluster API](https://github.com/kubernetes-sigs/cluster-api) - Cluster API is a Kubernetes sub-project focused on providing declarative APIs and tooling to simplify provisioning, upgrading, and operating multiple Kubernetes clusters.
- [eksctl](https://github.com/weaveworks/eksctl) - eksctl is a simple CLI tool for creating clusters on EKS - Amazon's new managed Kubernetes service for EC2.
- [k0s](https://github.com/k0sproject/k0s) - k0s - Zero Friction Kubernetes (The Simple, Solid & Certified Kubernetes Distribution)
- [k3d](https://github.com/rancher/k3d) - k3d,and Windows.,destroy,half the memory,highly available,is a tool for running local k3s clusters in docker. It's a single binary about 20 MB. You need to have docker installed.

## ◾ Cluster Resources Management

- [Clusterpedia](https://github.com/clusterpedia-io/clusterpedia) - Clusterpedia is used for complex resource searches across multiple clusters, support simultaneous search of a single kind of resource or multiple kinds of resources existing in multiple clusters.
- [Grafana Tanka](https://github.com/grafana/tanka) - The clean, concise and super flexible alternative to YAML for your Kubernetes cluster.
- [KEDA](https://github.com/kedacore/keda) - KEDA allows for fine grained autoscaling (including to/from zero) for event driven Kubernetes workloads.
- [Kruise](https://github.com/openkruise/kruise) - Kruise consists of several controllers which extend and complement the Kubernetes core controllers for workload management.
- [KubeDirector](https://github.com/bluek8s/kubedirector) - KubeDirector uses standard Kubernetes (K8s) facilities of custom resources and API extensions to implement stateful scaleout application clusters.
- [Kubenav](https://github.com/kubenav/kubenav) - kubenav is the navigator for your Kubernetes clusters right in your pocket.

## ◾ Code Pipeline

- [aws-codepipeline-custom-job-worker](https://github.com/awslabs/aws-codepipeline-custom-job-worker) - Develop your own job worker when creating a custom action.
- [aws-codepipeline-jenkins-aws-codedeploy_linux](https://github.com/awslabs/aws-codepipeline-jenkins-aws-codedeploy_linux) - Four-stage pipeline for Linux.
- [aws-codepipeline-plugin-for-jenkins](https://github.com/awslabs/aws-codepipeline-plugin-for-jenkins) - Jenkins plugin.
- [aws-codepipeline-s3-aws-codedeploy_linux](https://github.com/awslabs/aws-codepipeline-s3-aws-codedeploy_linux) - Simple pipeline for Linux.
- [AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows) - Four-stage pipeline for Windows.
- [AWSCodePipeline-S3-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-S3-AWSCodeDeploy_Windows) - Simple pipeline for Windows.

## ◾ Command Line Tools

- [Helm](https://github.com/helm/helm) - Helm is a tool for managing Charts. Charts are packages of pre-configured Kubernetes resources.
- [Helmfile](https://github.com/helmfile/helmfile) - Helmfile is a declarative spec for deploying helm charts.
- [Helmwave](https://github.com/helmwave/helmwave) - Helmwave is helm3-native tool for deploy your Helm Charts. It is like Docker-Compose, but for Helm.
- [Infra](https://github.com/infrahq/infra) - Infra enables you to discover and access infrastructure (e.g. Kubernetes, databases). We help you connect an identity provider such as Okta or Azure active directory, and map users/groups with the permissions you set to your infrastructure.
- [K9s](https://github.com/derailed/k9s) - K9s provides a terminal UI to interact with your Kubernetes clusters.
- [kapp](https://github.com/vmware-tanzu/carvel-kapp) - kapp is a simple deployment tool focused on the concept of "Kubernetes application" — a set of resources with the same label

## ◾ Docker

- [Curso de Docker Completo](https://www.youtube.com/playlist?list=PLg7nVxv7fa6dxsV1ftKI8FAm4YD6iZuI4)
- [Curso de Docker para iniciantes](https://www.youtube.com/watch?v=np_vyd7QlXk&t=1s&ab_channel=MatheusBattisti-HoradeCodar)
- [Curso de Introdução ao Docker](https://www.youtube.com/playlist?list=PLXzx948cNtr8N5zLNJNVYrvIG6hk0Kxl-)
- [Curso Descomplicando o Docker - LINUXtips 2016](https://www.youtube.com/playlist?list=PLf-O3X2-mxDkiUH0r_BadgtELJ_qyrFJ_)
- [Descomplicando o Docker - LINUXtips 2022](https://www.youtube.com/playlist?list=PLf-O3X2-mxDn1VpyU2q3fuI6YYeIWp5rR)
- [Curso Docker - Jose Carlos Macoratti](https://www.youtube.com/playlist?list=PLJ4k1IC8GhW1kYcw5Fiy71cl-vfoVpqlV)

## ◾ Engine & Runtime

- [colima](https://github.com/abiosoft/colima) - Container runtimes on macOS (and Linux) with minimal setup.
- [containerd](https://github.com/containerd/containerd) - An open and reliable container runtime.
- [cri-o](https://github.com/cri-o/cri-o) - Open Container Initiative-based implementation of Kubernetes Container Runtime Interface.
- [gVisor](https://github.com/google/gvisor) - Application Kernel for Containers.
- [lxc](https://github.com/lxc/lxc) - LXC - Linux Containers.
- [Mocker](https://github.com/us/mocker) - Docker-compatible container CLI for macOS, built on Apple's Containerization framework.

## ◾ How-To

- [How To Write OPA for Terraform](https://scalr.com/learning-center/opa-series-part-1-open-policy-agent-and-terraform) - How to use Open Policy Agent to evaluate and enforce policy on your Terraform plans
- [Deploying Discourse with Terraform](https://www.hashicorp.com/en/blog/deploying-discourse-with-terraform) - Shows how Terraform can create a running instance of Discourse on DigitalOcean in one command.
- [Deploying Django to AWS ECS with Terraform](https://testdriven.io/blog/deploying-django-to-ecs-with-terraform/) - Looks at how to use Terraform to spin up the required AWS infrastructure for running a Django app on ECS.
- [Easily Deploy A Seneca Microservice to ECS with Wercker and Terraform: Part I](https://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-i/) - II & III - Illustrates how Terraform can be incorporated into a microservice deployment pipeline.
- [Terraform for a Highly Available VPN between AWS and Azure](https://web.archive.org/web/20210616132857/https://deployeveryday.com/2020/04/13/vpn-aws-azure-terraform.html) - Terraform code to deploy a highly available VPN between AWS and Azure.
- [Terraforming 1Password](https://1password.com/blog/terraforming-1password) - How 1Password migrated from CloudFormation to Terraform.

## ◾ Mais links

- [continuousIntegration](http://martinfowler.com/articles/continuousIntegration.html)
- [continuousdelivery](http://continuousdelivery.com/)
- [software integration](https://en.wikipedia.org/wiki/System_integration)
- [ci/cd pipeline](https://semaphoreci.com/blog/cicd-pipeline)
- [devopsdays](http://www.devopsdays.org/)
- [ci cheatsheet](https://dzone.com/refcardz/continuous-integration)
- [api-gateway-secure-pet-store](https://github.com/awslabs/api-gateway-secure-pet-store) - Cognito credentials through Lambda.
- [aws-apigateway-sdk-java](https://github.com/awslabs/aws-apigateway-sdk-java) - SDK for Java.
- [aws-apigateway-swagger-importer](https://github.com/awslabs/aws-apigateway-importer) - Tools to work with Swagger.
- [weekly.tf - Terraform Weekly Newsletter](https://www.weekly.tf/) - Weekly newsletter covering Terraform news, open-source projects, announcements, and discussions.
- [Terraform AWS Modules](https://github.com/terraform-aws-modules) - + meta-configurations repository
- [awesome-terraform-compliance](https://github.com/antonbabenko/awesome-terraform-compliance) - Curated list of tools, frameworks, and resources for Terraform compliance and security. <sub>lista awesome</sub>
- [Docker Compose](https://github.com/docker/compose/) - Define and run multi-container applications with Docker.
- [Docker Registry](https://github.com/docker/distribution) - The Docker toolset to pack, ship, store, and deliver content
- [awscli-aliases](https://github.com/awslabs/awscli-aliases) - Repository for AWS CLI aliases.
- [amazon-ecs-cli](https://github.com/aws/amazon-ecs-cli) - ECS CLI using the same Docker Compose file format and familiar Compose commands.
- [aws-cli](https://github.com/aws/aws-cli) - Universal Command Line Interface.
- [awscli-cookbook](https://github.com/awslabs/awscli-cookbook) - Installs the CLI tools and provides a set of LWRPs for use within chef cookbooks.
- [awsmobile-cli](https://github.com/aws/awsmobile-cli) - CLI experience for Frontend developers in the JavaScript ecosystem.
- [achiku/jungle](https://github.com/achiku/jungle) - Operations by EC2 and ELB cli should be simpler.
- [Terraform Best Practices](https://www.terraform-best-practices.com/) - open-source ebook
- [Terraform Terminal Simulator](https://devops-daily.com/games/terraform-terminal-simulator) - Practice init, plan, and apply in a simulated terminal in the browser. Free and open source, no signup.
- [compliance.tf docs](https://compliance.tf/docs/) - Free Terraform implementations of SOC 2, PCI DSS, HIPAA, NIST 800-53, and 35+ other compliance controls — open reference for writing compliant infrastructure code.
- [DevOpsLesson Terraform Playground](https://devopslesson.com/playground/terraform) - Free browser-based Terraform simulator with guided HCL exercises and practice commands.
- [Openstack](https://www.openstack.org/) - Open source software for creating private and public clouds.
- [Apache CloudStack](https://cloudstack.apache.org/) - Designed to deploy and manage large networks of virtual machines.
- [OpenNebula](https://opennebula.org/) - Build Private Clouds and manage Data Center virtualization based on KVM, LXD and VMware.
- [Eucalyptus](https://www.eucalyptus.cloud/) - Building AWS-compatible private and hybrid clouds.
- [DC/OS](https://dcos.io/) - Distributed operating system based on the Apache Mesos distributed systems kernel.
- [Apache Mesos](http://mesos.apache.org/) - Program against your data center like it’s a single pool of resources.
- [appcircle.io](https://appcircle.io/)
- [closeheat](http://closeheat.com/)
- [cloudbees](https://www.cloudbees.com/)
- [elasticbox](https://elasticbox.com/)
- [coveralls](https://coveralls.io/)
- [shippable](https://app.shippable.com/)
- [Ubuntu](https://ubuntu.com/) - Enterprise Open Source and Linux.
- [Rocky Linux](https://rockylinux.org/) - Open-source enterprise operating system designed to be 100% bug-for-bug compatible with Red Hat Enterprise Linux.
- [CoreOS](http://coreos.com/) - The pioneering lightweight container host.
- [OSv](http://osv.io/) - Versatile modular unikernel designed to run unmodified Linux applications securely on micro-VMs in the cloud.
- [Atomic](http://www.projectatomic.io/) - Use immutable infrastructure to deploy and scale your containerized applications.
- [Photon](https://github.com/vmware/photon) - Linux container host optimized for cloud-native applications, cloud platforms, and VMware infrastructure.
- [Creating custom terraform providers](https://blog.pelo.tech/creating-custom-terraform-providers-341311823fa2) - Guide for creating custom providers.
- [Writing a Terraform provider](https://web.archive.org/web/20220516140659/http://blog.jfabre.net/2017/01/22/writing-terraform-provider/) - Guide for creating custom providers.
- [Writing Custom Providers](https://developer.hashicorp.com/terraform/plugin/sdkv2) - Official documentation for creating custom providers.
- [Terraform Provider Code generation](https://www.speakeasy.com/docs/terraform/create-terraform) - Guide to generating a terraform provider from an OpenAPI specification (Vendor Supported)
- [Chainguard Images](https://github.com/chainguard-images/images) - Minimal, signed, SBOM-attested container images built on Wolfi.
- [distroless](https://github.com/GoogleContainerTools/distroless) - Language focused docker images, minus the operating system.
- [melange](https://github.com/chainguard-dev/melange) - Build apk packages from declarative YAML for use with apko.
- [pglayers](https://github.com/pglayers/pglayers) - Pre-built PostgreSQL extensions as composable Docker layers. 50+ extensions, ready-to-use combined images (full, Azure-compatible).
- [Wolfi](https://github.com/wolfi-dev/os) - Undistro Linux designed for containers; glibc-based, signed, daily SBOMs.
- [cloudsearchable](https://github.com/awslabs/cloudsearchable) - An ActiveRecord-style ORM query interface.
- [aws-cloudtrail-processing-library](https://github.com/aws/aws-cloudtrail-processing-library) - Easily consume and process log files.
- [AppliedTrust/traildash](https://github.com/AppliedTrust/traildash) - Slick dashboard.
- [GorillaStack/auto-tag](https://github.com/GorillaStack/auto-tag) - Automatically tag AWS resources on creation, for cost assignment.
- [CatLight](https://catlight.io/)
- [Barklarm](https://www.barklarm.com/)
- [CCMenu](http://ccmenu.org/)
- [Nix/NixOS](https://nixos.org/) - A tool that takes a unique approach to package management and system configuration.
- [Dockerfile Generator](https://github.com/ozankasikci/dockerfile-generator) - dfg is both a Go library and an executable that produces valid Dockerfiles using various input channels.
- [Dockershelf](https://github.com/Dockershelf/dockershelf) - A repository that serves as a collector for docker recipes that are universal, efficient and slim. Images are updated, tested and published daily via a Travis cron job.
- [Dofigen](https://github.com/lenra-io/dofigen) - A Dockerfile generator using a simplified description in YAML or JSON format.
- [Trsuted Builds](https://dockerfile.github.io/) - Trusted Automated Docker Builds. Dockerfile Project maintains a central repository of Dockerfile for various popular open source software services runnable on a Docker container.
- [Ceph](https://ceph.io/en/) - Highly scalable object, block and file-based storage under one whole system.
- [Gluster](https://www.gluster.org/) - Free and open source software scalable network filesystem.
- [LINBIT](https://www.linbit.com/en/) - Create, remove, and replicate block storage devices for datacenter scale environments.
- [XtreemFS](http://www.xtreemfs.org/) - Fault-tolerant distributed file system for all storage needs.
- [min.io](https://min.io/) - High-performance, distributed object storage system.
- [GridWiki](http://wiki.gridengine.info/wiki/index.php/Main_Page)
- [UGE](http://www.univa.com/)
- [SGE](http://gridscheduler.sourceforge.net/)
- [LSF](http://www-03.ibm.com/systems/platformcomputing/products/lsf/)
- [vmwarevshpere](http://www.vmware.com/products/vsphere)
- [citrixserver](http://www.citrix.com/products/xenserver/overview.html)
- [Terraform Design Patterns: the Terrafile](https://bensnape.com/2016/01/14/terraform-design-patterns-the-terrafile/) - Managing Terraform modules and their versions within Terraform projects with Terrafile.
- [Terraform, VPC, and why you want a tfstate file per env](https://charity.wtf/2016/03/30/terraform-vpc-and-why-you-want-a-tfstate-file-per-env/) - Some gotchas surrounding using Terraform in large projects with multiple environments and how to avoid them.
- [Using Pipelines to Manage Environments with Infrastructure as Code](https://medium.com/@kief/https-medium-com-kief-using-pipelines-to-manage-environments-with-infrastructure-as-code-b37285a1cbf5) - Explains different approaches for building a pipeline to handle infrastructure changes moving from one environment to the next.
- [Dockadvisor](https://github.com/deckrun/dockadvisor) - Lightweight Dockerfile linter with 60+ rules, quality scoring, and security checks.
- [docker-image-size-limit](https://github.com/wemake-services/docker-image-size-limit) - A tool to keep an eye on your docker images size.
- [Hadolint](https://github.com/hadolint/hadolint) - A Dockerfile linter that checks for best practices, common mistakes, and is also able to lint any bash written in RUN instructions;.
- [Kubernetes External Secrets](https://github.com/godaddy/kubernetes-external-secrets) - Kubernetes External Secrets allows you to use external secret management systems, like AWS Secrets Manager or HashiCorp Vault, to securely add secrets in Kubernetes.
- [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets) - Encrypt your Secret into a SealedSecret, which is safe to store - even to a public repository.
- [akv2k8s](https://github.com/SparebankenVest/azure-key-vault-to-kubernetes) - Azure Key Vault to Kubernetes (akv2k8s) will make Azure Key Vault objects available to Kubernetes in two ways: as native Kubernetes Secrets; as environment variables directly injected into your Container application
- [Openshift](https://www.openshift.com/) - The Kubernetes platform for big ideas.
- [Cycle.io](https://cycle.io/) - DevOps platform for building platforms. Handle container orchestration, load-balancing, monitoring, and more from a single control plane.
- [Dokku](https://dokku.com/) - Helps you build and manage the lifecycle of applications.
- [Cloud 66](https://www.cloud66.com/) - DevOps as a service that helps to build, deploy and manage any application on any cloud or server.
- [Docker](https://www.docker.com/) - Create, deploy, and run applications by using containers.
- [aws-codedeploy-agent](https://github.com/aws/aws-codedeploy-agent) - Sample agent.
- [aws-codedeploy-plugin](https://github.com/awslabs/aws-codedeploy-plugin) - Jenkins plugin.
- [aws-codedeploy-samples](https://github.com/awslabs/aws-codedeploy-samples) - Samples and template scenarios.
- [Learning HashiCorp Terraform](https://web.archive.org/web/20201108000713/https://www.g10s.io/hashicorp-terraform/) - Guide for Azure.
- [New Terraform Azure Automation Resources](https://bgelens.nl/terraform-automation-resources/) - Azure Automation.
- [Terraforming Azure PaaS](https://devkimchi.com/2019/01/21/terraforming-azure-paas/) - Deploy PaaS Resources on Azure.
- [azure-az104](https://github.com/victorlane/azure-az104) - AZ-104 Azure Administrator study notes and hands-on Terraform examples, including a landing-zone reference architecture.
- [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) - Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. <sub>livro</sub>
- [Azure Container Registry](https://azure.microsoft.com/en-us/products/container-registry/) - Manage a Docker private registry as a first-class Azure resource.
- [Cloudsmith](https://cloudsmith.com/product/formats/docker-registry) - A fully managed package management SaaS, with first-class support for public and private Docker registries (and many others, incl. Helm charts for the Kubernetes ecosystem). Has a generous free-tier and is also completely free for open-source.
- [Container Registry Service](https://container-registry.com/) - Harbor based Container Management Solution as a Service for teams and organizations. Free tier offers 1 GB storage for private repositories.
- [DigitalOcean](https://www.digitalocean.com/products/container-registry) - DigitalOcean Container Registry.
- [boxstarter](http://boxstarter.org/)
- [T.A.D.S. boilerplate](https://github.com/Thomvaill/tads-boilerplate)
- [vagrantup](https://www.vagrantup.com/)
- [veewee](https://github.com/jedi4ever/veewee)
- [Calico Networking](https://github.com/projectcalico/calico) - Calico is an open source networking and network security solution for containers, virtual machines, and bare-metal workloads
- [cert-manager](https://github.com/jetstack/cert-manager) - cert-manager is a Kubernetes add-on to automate the management and issuance of TLS certificates from various issuing sources.
- [cilium](https://github.com/cilium/cilium) - Cilium is a networking, observability, and security solution with an eBPF-based dataplane.
- [CoreDNS](https://github.com/coredns/coredns) - CoreDNS is a fast and flexible DNS server that works on Kubernetes.
- [ingress-nginx](https://github.com/kubernetes/ingress-nginx) - ingress-nginx is an Ingress controller for Kubernetes using NGINX as a reverse proxy and load balancer.
- [Kong for Kubernetes](https://github.com/Kong/kubernetes-ingress-controller) - Configure plugins, health checking, load balancing and more in Kong for Kubernetes Services.
- [Port](https://www.getport.io/) - A platform for building no-code, holistic, Internal Developer Portals.
- [Backstage](https://backstage.io/) - An open platform for building developer portals.
- [Kratix](https://kratix.io/) - A framework used by platform teams to build the custom platforms tailored to their organisation.
- [OpenChoreo](https://openchoreo.dev/) - A complete, modular, open-source developer platform.
- [Curso de Kubernetes: Introdução](https://www.youtube.com/watch?v=n1myN27XLfo&list=PLnPZ9TE1Tj4CpbmTsTgqVpRG0hIgHXsaX&ab_channel=MateusSchwede)
- [Apresentação - Curso de Introdução ao Kubernetes](https://www.youtube.com/watch?v=RuNTvYejG90&list=PLXzx948cNtr8XI5JBemHT9OWuYSPNUtXs&ab_channel=InsightLab)
- [Kubernetes do Zero a Produção](https://www.youtube.com/watch?v=oxWEVQP5_Rg&ab_channel=FullCycle)
- [Mini Curso Gratuito de Kubernetes para Devs Javascript](https://www.youtube.com/watch?v=eXKg9B5ooaY&ab_channel=ErickWendel)
- [Containers, Docker e Kubernetes com Giovanni Bassi / #HipstersPontoTube](https://www.youtube.com/watch?v=wxLvvMxzc1Q&ab_channel=AluraCursosOnline)
- [AWS Lambda the Terraform Way](https://github.com/nsriram/lambda-the-terraform-way) - Understand AWS Lambda in-depth, beyond executing functions, using Terraform. Also includes guides for integration with S3, API Gateway, DynamoDB, Kinesis, SQS.
- [Managing AWS Lambda Functions with Terraform](https://spacelift.io/blog/terraform-aws-lambda) - What is AWS Lambda used for and how to use Terraform to manage AWS Lambda functions?
- [git](http://git-scm.com/)
- [perforce](https://www.perforce.com/)
- [clearcase](http://www-03.ibm.com/software/products/en/clearcase)
- [mercurial](https://www.mercurial-scm.org/)
- [crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane) - Lightweight CLI to manipulate registry images, from go-containerregistry.
- [go-containerregistry](https://github.com/google/go-containerregistry) - Go library and CLI tools (crane, gcrane, registry) for working with container registries.
- [oras](https://github.com/oras-project/oras) - Push and pull arbitrary OCI artifacts to and from any OCI registry.
- [Managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code) - Setup and manage infrastructure as code with Terraform, Cloud Build, and GitOps.
- [Getting started with Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/create-vm-instance) - Using Terraform to create a VM in Google Cloud and Starting a basic Python Flask server.
- [Longhorn](https://github.com/longhorn/longhorn) - Longhorn is a distributed block storage system for Kubernetes.
- [Quay](https://www.projectquay.io/) - Container image registry that enables you to build, organize, distribute, and deploy containers.
- [amazon-cognito-android](https://github.com/aws/amazon-cognito-android) - Sync SDK for Android.

## 🧾 Fontes desta área

Os links acima (fora os essenciais) foram reunidos destas listas curadas. Obrigado a quem as mantém.

- [Jun-jie-Huang/awesome-LLM-AIOps](https://github.com/Jun-jie-Huang/awesome-LLM-AIOps) <sub>0 links · licença MIT</sub>
- [OpsPAI/awesome-AIOps](https://github.com/OpsPAI/awesome-AIOps) <sub>0 links · licença MIT</sub>
- [arthurspk/guiadevbrasil](https://github.com/arthurspk/guiadevbrasil) <sub>35 links · licença MIT</sub>
- [cicdops/awesome-ciandcd](https://github.com/cicdops/awesome-ciandcd) <sub>35 links · licença GPL-2.0</sub>
- [donnemartin/awesome-aws](https://github.com/donnemartin/awesome-aws) <sub>35 links · licença CC-BY-4.0</sub>
- [shuaibiyy/awesome-terraform](https://github.com/shuaibiyy/awesome-terraform) <sub>34 links · licença CC0-1.0</sub>
- [tensorchord/Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) <sub>0 links · licença CC0-1.0</sub>
- [tomhuang12/awesome-k8s-resources](https://github.com/tomhuang12/awesome-k8s-resources) <sub>34 links · licença CC0-1.0</sub>
- [veggiemonk/awesome-docker](https://github.com/veggiemonk/awesome-docker) <sub>34 links · licença Apache-2.0</sub>
- [wmariuss/awesome-devops](https://github.com/wmariuss/awesome-devops) <sub>34 links · licença CC0-1.0</sub>

---
[⬆️ Voltar ao topo](#️-devops-e-cloud) · [← Tecnologia e Desenvolvimento](README.md)
