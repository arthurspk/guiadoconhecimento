<p align="center">
  <img src="images/logo.svg" alt="Guia do Conhecimento" width="160" height="160">
</p>

<h1 align="center">Guia do Conhecimento</h1>

## 🎯 このガイドについて

> **Guia do Conhecimento**は、無料で公開されているオープンな知識マップです。**9部門**、**72分野**、**38職種**にわたって整理された**55357件のリンク**を通じて、**誰でも**自分の分野に最適なサイト、コース、ツール、リポジトリ、awesomeリスト、コミュニティ、ユーティリティを見つけられます。対象は、開発、データ、セキュリティ、デザイン、動画編集、映画、写真、音楽、マーケティング、有料トラフィック、営業、金融、法律、医療、科学、教育、語学など多岐にわたります。各分野は**厳選リンク**から始まり、**その職種に応用した人工知能**のセクションがあり、コミュニティによる優れたキュレーションリストのリンクが続きます。さらに各職種に**1000件のAIリポジトリ**があります。すべてのリンクに説明があり、ガイド全体が**12言語**で読めます。

- 🗂️ [分野カタログ](i18n/ja/areas/CATALOGO.md): 全72分野を部門別に、リンク件数つきで掲載。
- 🧭 [職種別の学習パス](i18n/ja/trilhas/README.md): 38の学習パス。フロントエンド開発者からフィルムメーカー、トラフィックマネージャー、教員まで。
- 🧠 [職種別のAIリポジトリ](i18n/ja/ia/profissoes/README.md): AIリポジトリ38000件、各職種に1000件。

## 💡 このガイドの構成

> 全体から具体へ向かう3つの階層があります。**部門**(例: デザインとクリエイティブ)→**分野**(例: 動画編集)→**トピック**(例: ノンリニア編集ソフト)。各分野は1ページで、目次、**⭐ まずはここから**セクション、**🤖 AI**セクションがあり、トピックは件数の多い順に並び、それぞれに説明が付いています。すべてオープンなデータベース(`data/links.jsonl`)が元になり、Pythonのスクリプトで生成されるため、ガイド全体を再生成、検証、拡張できます。構成は、[guiadevbrasil](https://github.com/arthurspk/guiadevbrasil)と[guiadomaestri](https://github.com/arthurspk/guiadomaestri)のガイドに倣っています。

## 🌍 翻訳

> このガイドを他の言語で読みたい方は、下から選んでください。どの言語でも、ページ、セクション、各リンクの説明がその言語で表示されます。説明は自動翻訳です。誤りの修正にご協力いただけると、コミュニティの助けになります。`docs/` の詳細ドキュメントはポルトガル語です。

🇧🇷・**Português (Brasil) —** [este arquivo](README.md)<br>
🇺🇸・**English —** [Click Here](README.en.md)<br>
🇪🇸・**Español —** [Clic aquí](README.es.md)<br>
🇨🇳・**中文 —** [点击这里](README.zh.md)<br>
🇮🇳・**हिन्दी —** [यहाँ क्लिक करें](README.hi.md)<br>
🇸🇦・**العربية —** [اضغط هنا](README.ar.md)<br>
🇫🇷・**Français —** [Cliquez ici](README.fr.md)<br>
🇮🇹・**Italiano —** [Clicca qui](README.it.md)<br>
🇰🇷・**한국어 —** [여기 클릭](README.ko.md)<br>
🇷🇺・**Русский —** [Нажмите здесь](README.ru.md)<br>
🇩🇪・**Deutsch —** [Hier klicken](README.de.md)<br>
🇯🇵・**日本語 —** [このファイル](README.ja.md)<br>

## 📚 目次

> このページのセクションを、登場順に並べています。

[⭐ まずはここから](#-まずはここから) — 探しているものへの最短ルート。 <br>
[📖 ドキュメント](#-ドキュメント) — 使い方、構成、貢献方法。 <br>
[🗂️ 部門と分野](#️-部門と分野) — すべての部門と分野。 <br>
[🧭 職種別の学習パス](#-職種別の学習パス) — キャリアをどこから始めるか。 <br>
[🤖 すべての分野のAI](#-すべての分野のai) — 各職種に応用した人工知能。 <br>
[🧠 職種別のAIリポジトリ1000件](#-職種別のaiリポジトリ1000件) — 各職種のAIリポジトリ、新しいツール、自動化。 <br>
[🔢 数字で見るガイド](#-数字で見るガイド) — リンクの件数、種類、出どころ。 <br>
[📜 利用できるスクリプト](#-利用できるスクリプト) — Pythonのコレクター、翻訳ツール、ジェネレーター、バリデーター。 <br>
[🛠️ 再生成と検証](#️-再生成と検証) — すべてを再構築して確認する。 <br>
[🤝 貢献](#-貢献) — リンク、分野、翻訳の提案方法。 <br>
[⚖️ ライセンスとクレジット](#️-ライセンスとクレジット) — 各リンクの出どころ。 <br>
[⚠️ ご注意](#️-ご注意) — 外部リンクについて。 <br>
[🌟 Star History](#-star-history) — リポジトリのスター数のグラフ。 <br>

## ⭐ まずはここから

> 目的に合わせた7つのショートカットです。

- [🧭 **自分の職種がわかっている**](i18n/ja/trilhas/README.md): その職種の学習パスを開き、分野を順番にたどります。
- [🗂️ **テーマがわかっている**](i18n/ja/areas/CATALOGO.md): カタログを開いて、分野へ直接移動します。
- [🤖 **仕事でAIを使いたい**](i18n/ja/ia/README.md): 各職種のAIセクションを1か所に集めました。
- [🧠 **自分の職種向けのAIリポジトリがほしい**](i18n/ja/ia/profissoes/README.md): 職種ごとに1000件のリポジトリを、テーマ別に分けています。
- [🎬 **映像・音響の仕事をしている**](i18n/ja/areas/criacao/recursos-audiovisuais.md): LUT、エフェクト、トランジション、プリセット、フォント、効果音、フリー音楽、stock footage。
- [🧰 **良いツールだけがほしい**](i18n/ja/areas/ferramentas/README.md): オンラインツール、OS別アプリ、拡張機能、API、無料リソース。
- 🔎 **特定のものを探していますか?** 分野のページで `Ctrl+F` を使うか、このリポジトリのGitHub検索をご利用ください。データベース全体は [`data/links.csv`](data/links.csv) にあり、任意のスプレッドシートで開けます。

## 📖 ドキュメント

> このガイドのドキュメントです。初めての方は01から読んでください。

- [🧭 01 · **このガイドの使い方**](docs/01-como-usar.md) — ナビゲーション、記号、学習への活用方法。
- [🗺️ 02 · **構成と分類**](docs/02-organizacao-e-taxonomia.md) — 部門、分野、トピックと、そうなっている理由。
- [🥾 03 · **職種別の学習パス**](docs/03-trilhas-por-profissao.md) — 学習パスの使い方と作り方。
- [📐 04 · **データ形式**](docs/04-formato-dos-dados.md) — `data/` 内の各ファイルのフィールド。
- [🕷️ 05 · **Scraplingによる収集**](docs/05-coleta-com-scrapling.md) — リンクの収集、検証、更新の方法。
- [🔍 06 · **キュレーションと品質**](docs/06-curadoria-e-qualidade.md) — 採用と除外の基準、重複排除、分野ごとの上限。
- [⚖️ 07 · **情報源とライセンス**](docs/07-fontes-e-licencas.md) — すべての情報源と、クレジット、ライセンス。
- [🤝 08 · **貢献方法**](docs/08-como-contribuir.md) — リンク、分野、学習パス、翻訳の提案。
- [🤖 09 · **すべての分野のAI**](docs/09-ia-em-todas-as-areas.md) — AIレイヤーの作り方と、AIを責任を持って使う方法。

## 🗂️ 部門と分野

> 9部門、72分野。各部門には、分野の概要と各分野の最初の厳選リンクをまとめたページがあります。

- [💻 **テクノロジーと開発**](i18n/ja/areas/tecnologia/README.md) — 🔗 5051
  - [🧮 コンピュータサイエンスの基礎](i18n/ja/areas/tecnologia/fundamentos-computacao.md) — アルゴリズム、データ構造、OS、コンパイラ、理論。
  - [🔤 プログラミング言語](i18n/ja/areas/tecnologia/linguagens.md) — Python、JavaScript、Java、Go、Rust、C#、PHP、Kotlin、Swiftなど数十の言語。
  - [🎨 フロントエンド](i18n/ja/areas/tecnologia/front-end.md) — HTML、CSS、JavaScript、フレームワーク、アクセシビリティ、Webパフォーマンス。
  - [⚙️ バックエンド](i18n/ja/areas/tecnologia/back-end.md) — API、サーバーフレームワーク、認証、キュー、マイクロサービス。
  - [📱 モバイル](i18n/ja/areas/tecnologia/mobile.md) — Android、iOS、Flutter、React Native、ストア公開。
  - [🎮 ゲーム開発](i18n/ja/areas/tecnologia/games.md) — エンジン、グラフィックス、ゲームデザイン、アセット、ゲームプログラミング。
  - [☁️ DevOpsとクラウド](i18n/ja/areas/tecnologia/devops-cloud.md) — CI/CD、コンテナ、Kubernetes、IaC、AWS、Azure、GCP、SRE。
  - [🗄️ データベース](i18n/ja/areas/tecnologia/bancos-de-dados.md) — SQL、NoSQL、モデリング、最適化、運用管理。
  - [✅ QAとテスト](i18n/ja/areas/tecnologia/qa-testes.md) — 自動テスト、手動テスト、パフォーマンス、モバイル、ソフトウェア品質。
  - [🏛️ アーキテクチャとソフトウェアエンジニアリング](i18n/ja/areas/tecnologia/arquitetura-software.md) — システム設計、パターン、クリーンコード、DDD、スケーラビリティ。
  - [🐧 Linux、システム、ターミナル](i18n/ja/areas/tecnologia/sistemas-linux.md) — Linux、シェル、システム管理、コマンドライン。
  - [🌐 ネットワークと通信](i18n/ja/areas/tecnologia/redes.md) — プロトコル、ネットワークインフラ、SDN、電気通信。
  - [🔌 組み込み、IoT、ハードウェア](i18n/ja/areas/tecnologia/embarcados-iot.md) — Arduino、Raspberry Pi、電子工作、ロボティクス、ファームウェア。
  - [⛓️ ブロックチェーンとWeb3](i18n/ja/areas/tecnologia/blockchain-web3.md) — スマートコントラクト、Ethereum、応用暗号、分散システム。
  - [🛠️ 開発者向けツール](i18n/ja/areas/tecnologia/ferramentas-dev.md) — エディタ、Git、ターミナル、生産性向上、開発用ユーティリティ。
  - [🌱 オープンソース](i18n/ja/areas/tecnologia/open-source.md) — 貢献の仕方、プロジェクトの探し方、フリーソフトウェアの維持。
- [🤖 **データと人工知能**](i18n/ja/areas/dados-ia/README.md) — 🔗 1289
  - [📊 データ分析とBI](i18n/ja/areas/dados-ia/analise-de-dados.md) — Excel、分析用SQL、ダッシュボード、可視化、ビジネスインテリジェンス。
  - [🔀 データエンジニアリング](i18n/ja/areas/dados-ia/engenharia-de-dados.md) — パイプライン、ETL、データレイク、ストリーミング、オーケストレーション。
  - [🧠 データサイエンスとmachine learning](i18n/ja/areas/dados-ia/ciencia-de-dados-ml.md) — 統計、従来型ML、ディープラーニング、コンピュータビジョン、NLP。
  - [✨ 生成AIとLLM](i18n/ja/areas/dados-ia/ia-generativa.md) — LLM、エージェント、プロンプト、RAG、MCP、AIツール。
  - [🗃️ データセットとオープンデータ](i18n/ja/areas/dados-ia/datasets.md) — 公開データ、政府のオープンデータ、学習用データセット。
- [🔒 **セキュリティとプライバシー**](i18n/ja/areas/seguranca/README.md) — 🔗 722
  - [🛡️ サイバーセキュリティ](i18n/ja/areas/seguranca/ciberseguranca.md) — ペンテスト、ブルーチーム、CTF、マルウェア、フォレンジック、バグバウンティ。
  - [🔎 OSINTと調査](i18n/ja/areas/seguranca/osint.md) — オープンソースインテリジェンスと調査の手法。
  - [🕶️ プライバシーとデータ保護](i18n/ja/areas/seguranca/privacidade.md) — デジタルプライバシー、LGPD/GDPR、保護ツール。
- [🎬 **デザインとクリエイティブ**](i18n/ja/areas/criacao/README.md) — 🔗 1895
  - [🖌️ UI/UXデザイン](i18n/ja/areas/criacao/design-ui-ux.md) — インターフェースデザイン、UXリサーチ、デザインシステム、プロトタイピング。
  - [🖍️ グラフィックデザインとイラスト](i18n/ja/areas/criacao/design-grafico.md) — タイポグラフィ、色彩、ビジュアルアイデンティティ、イラスト、グラフィック素材。
  - [🎞️ 動画編集](i18n/ja/areas/criacao/edicao-de-video.md) — 編集ソフト、color grading、字幕、コーデック、ポストプロダクションの流れ。
  - [🎥 フィルムメイキングと映画](i18n/ja/areas/criacao/filmmaking.md) — 脚本、演出、映画の撮影、制作、配給。
  - [🪄 映像・音響素材](i18n/ja/areas/criacao/recursos-audiovisuais.md) — LUT、エフェクト、トランジション、プリセット、オーバーレイ、フォント、効果音、フリー音楽、stock footage。
  - [📷 写真](i18n/ja/areas/criacao/fotografia.md) — 撮影技術、編集、機材、画像素材サイト。
  - [🧊 モーションデザイン、3D、アニメーション](i18n/ja/areas/criacao/motion-3d.md) — Blender、モーショングラフィックス、2D/3Dアニメーション、視覚効果。
  - [🎧 音声、音楽、ポッドキャスト](i18n/ja/areas/criacao/audio-musica.md) — 音楽制作、DAW、プラグイン、ミキシング、ポッドキャスト。
  - [✍️ ライティング](i18n/ja/areas/criacao/escrita.md) — 文章作成、コピーライティング、技術文書、校正、出版。
- [📈 **マーケティングと営業**](i18n/ja/areas/marketing-vendas/README.md) — 🔗 1170
  - [📣 デジタルマーケティング](i18n/ja/areas/marketing-vendas/marketing-digital.md) — 戦略、ファネル、メールマーケティング、自動化、グロース。
  - [🎯 有料トラフィック](i18n/ja/areas/marketing-vendas/trafego-pago.md) — Google Ads、Meta Ads、TikTok Ads、LinkedIn Ads、効果測定、クリエイティブ。
  - [🔍 SEO](i18n/ja/areas/marketing-vendas/seo.md) — テクニカルSEO、コンテンツ、リンクビルディング、分析ツール。
  - [📲 SNSとコンテンツ](i18n/ja/areas/marketing-vendas/social-media.md) — SNS、コンテンツ制作、クリエイター、投稿のスケジュール管理。
  - [🤝 営業とCRM](i18n/ja/areas/marketing-vendas/vendas.md) — 見込み客の開拓、交渉、CRM、営業オペレーション。
  - [🛒 EC](i18n/ja/areas/marketing-vendas/e-commerce.md) — ネットショップ、プラットフォーム、決済、物流、マーケットプレイス。
- [💼 **ビジネスとマネジメント**](i18n/ja/areas/negocios/README.md) — 🔗 1622
  - [🚀 起業とスタートアップ](i18n/ja/areas/negocios/empreendedorismo.md) — 事業の立ち上げと拡大、資金調達、ビジネスモデル、SaaS。
  - [📦 プロダクトマネジメント](i18n/ja/areas/negocios/produto.md) — ディスカバリー、ロードマップ、指標、プロダクトマネジメントの実践。
  - [🗂️ プロジェクトマネジメントとアジャイル](i18n/ja/areas/negocios/gestao-de-projetos.md) — Scrum、Kanban、PMBOK、ツール、チームのリーダーシップ。
  - [💰 金融と投資](i18n/ja/areas/negocios/financas.md) — 個人の資産管理、投資、金融市場、企業財務。
  - [🧾 会計と税務](i18n/ja/areas/negocios/contabilidade.md) — 会計、税金、MEI(ブラジルの個人事業主制度)、税務の定型業務。
  - [👥 人事と人材マネジメント](i18n/ja/areas/negocios/rh-pessoas.md) — 採用、組織文化、オンボーディング、報酬、リーダーシップ。
  - [⚖️ 法務と法律](i18n/ja/areas/negocios/juridico.md) — 法令、デジタル法、契約、リーガルテック。
  - [🛟 カスタマーサポートとカスタマーサクセス](i18n/ja/areas/negocios/atendimento-suporte.md) — サポート、カスタマーサクセス、ヘルプデスク、ナレッジベース。
- [🔬 **科学、医療、教育**](i18n/ja/areas/ciencia-educacao/README.md) — 🔗 2238
  - [➗ 数学と統計](i18n/ja/areas/ciencia-educacao/matematica.md) — 基礎から応用まで、統計、微積分、線形代数。
  - [🔭 物理学と天文学](i18n/ja/areas/ciencia-educacao/fisica-astronomia.md) — 物理学、天文学、天体物理学、宇宙科学。
  - [⚗️ 化学](i18n/ja/areas/ciencia-educacao/quimica.md) — 一般化学、計算化学、実験室向けツール。
  - [🧬 生物学とバイオインフォマティクス](i18n/ja/areas/ciencia-educacao/biologia.md) — 生物学、遺伝学、バイオインフォマティクス、生命科学。
  - [🩺 医学と医療](i18n/ja/areas/ciencia-educacao/saude.md) — 医学、公衆衛生、デジタルヘルス、ウェルビーイング。
  - [🧠 心理学と神経科学](i18n/ja/areas/ciencia-educacao/psicologia.md) — 心理学、神経科学、行動、メンタルヘルス。
  - [📉 経済学](i18n/ja/areas/ciencia-educacao/economia.md) — 経済学、計量経済学、公共政策。
  - [🏛️ 人文学](i18n/ja/areas/ciencia-educacao/humanidades.md) — 歴史、哲学、社会学、地理学、芸術。
  - [🗣️ 語学](i18n/ja/areas/ciencia-educacao/idiomas.md) — 英語、スペイン語などの言語: コース、アプリ、練習。
  - [🎓 教育と指導](i18n/ja/areas/ciencia-educacao/educacao.md) — プラットフォーム、無料コース、MOOC、教員向けリソース。
  - [📚 学術研究](i18n/ja/areas/ciencia-educacao/pesquisa-academica.md) — 論文、学術データベース、LaTeX、文献管理、オープンサイエンス。
- [🧭 **キャリアと生産性**](i18n/ja/areas/carreira/README.md) — 🔗 997
  - [💼 キャリアと求人](i18n/ja/areas/carreira/carreira-vagas.md) — 求人、履歴書、面接、キャリアのロードマップ、給与。
  - [🏝️ リモートワークとフリーランス](i18n/ja/areas/carreira/trabalho-remoto-freela.md) — リモート求人、フリーランス向けプラットフォーム、デジタルノマド、自分の仕事の管理。
  - [⏱️ 生産性と整理術](i18n/ja/areas/carreira/produtividade.md) — メソッド、ノートアプリ、タスク管理、集中、セカンドブレイン。
  - [👋 コミュニティ、イベント、コンテンツ](i18n/ja/areas/carreira/comunidades.md) — コミュニティ、イベント、ニュースレター、ポッドキャスト、チャンネル。
  - [♿ アクセシビリティ](i18n/ja/areas/carreira/acessibilidade.md) — デジタルアクセシビリティ、支援技術、インクルージョン。
- [🧰 **ツールとユーティリティ**](i18n/ja/areas/ferramentas/README.md) — 🔗 2373
  - [🌍 オンラインツール](i18n/ja/areas/ferramentas/ferramentas-online.md) — ブラウザ上のコンバーター、ジェネレーター、エディタ、ユーティリティ。
  - [🪄 AIツール](i18n/ja/areas/ferramentas/ferramentas-ia.md) — テキスト、画像、動画、音声、生産性向上のためのAIアプリ。
  - [🏠 セルフホスト](i18n/ja/areas/ferramentas/self-hosted.md) — 自分で運用するソフトウェア: 自前のクラウド、メディア、自動化。
  - [🖥️ macOS・Windows・Linux向けアプリ](i18n/ja/areas/ferramentas/apps-sistemas.md) — 各OSで使える優れたアプリケーション。
  - [📲 Android・iOS向けアプリ](i18n/ja/areas/ferramentas/apps-celular.md) — スマートフォン向けの便利なアプリとオープンソースのアプリ。
  - [🧩 ブラウザ拡張機能](i18n/ja/areas/ferramentas/extensoes-navegador.md) — Chrome、Firefoxなどのブラウザ向け拡張機能。
  - [🔗 公開API](i18n/ja/areas/ferramentas/apis-publicas.md) — プロジェクト、学習、プロトタイプに使える無料のAPI。
  - [🎁 無料リソース](i18n/ja/areas/ferramentas/recursos-gratuitos.md) — 画像素材サイト、アイコン、フォント、カラーパレット、モックアップ、テンプレート。
  - [⚡ 自動化とノーコード](i18n/ja/areas/ferramentas/automacao.md) — ワークフローの自動化、ノーコード、ローコード、連携。

## 🧭 職種別の学習パス

> 各学習パスは、ある職種に重要な分野を、学ぶ価値のある順にまとめています。

- [🎨 フロントエンド開発者](i18n/ja/trilhas/README.md#-フロントエンド開発者) — ブラウザで人々が使うインターフェースを作る。
- [⚙️ バックエンド開発者](i18n/ja/trilhas/README.md#️-バックエンド開発者) — API、ビジネスロジック、連携、サーバー上で動くものを作る。
- [📱 モバイル開発者](i18n/ja/trilhas/README.md#-モバイル開発者) — AndroidとiOSのアプリを作る。
- [🎮 ゲーム開発者](i18n/ja/trilhas/README.md#-ゲーム開発者) — ゲームをプログラムし、デザインし、公開する。
- [☁️ DevOps、SRE、クラウド](i18n/ja/trilhas/README.md#️-devopssreクラウド) — デリバリーを自動化し、インフラを運用し、システムを稼働させ続ける。
- [✅ QAエンジニアとテストアナリスト](i18n/ja/trilhas/README.md#-qaエンジニアとテストアナリスト) — 手動テスト、自動テスト、パフォーマンステストで品質を保証する。
- [📊 データアナリストとBI](i18n/ja/trilhas/README.md#-データアナリストとbi) — データを、答え、ダッシュボード、意思決定に変える。
- [🔀 データエンジニア](i18n/ja/trilhas/README.md#-データエンジニア) — 信頼できるデータパイプラインとデータ基盤を構築する。
- [🧠 データサイエンティストとMLエンジニア](i18n/ja/trilhas/README.md#-データサイエンティストとmlエンジニア) — 統計とmachine learningでデータをモデル化する。
- [✨ AIエンジニアとLLMエンジニア](i18n/ja/trilhas/README.md#-aiエンジニアとllmエンジニア) — 言語モデル、エージェント、RAGでプロダクトを作る。
- [🛡️ セキュリティ専門家](i18n/ja/trilhas/README.md#️-セキュリティ専門家) — システムを守り、防御をテストし、インシデントを調査する。
- [🖌️ UI/UXデザイナー](i18n/ja/trilhas/README.md#️-uiuxデザイナー) — 人を中心にした体験とインターフェースをデザインする。
- [🖍️ グラフィックデザイナーとイラストレーター](i18n/ja/trilhas/README.md#️-グラフィックデザイナーとイラストレーター) — アイデンティティ、ビジュアル作品、イラストを制作する。
- [🎞️ 動画エディター](i18n/ja/trilhas/README.md#️-動画エディター) — 編集し、色と音を整え、動画を仕上げる。
- [🎥 フィルムメーカーと映画制作者](i18n/ja/trilhas/README.md#-フィルムメーカーと映画制作者) — 脚本を書き、撮影し、演出し、映画や動画を配給する。
- [📷 フォトグラファー](i18n/ja/trilhas/README.md#-フォトグラファー) — 写真を撮り、編集し、販売する。
- [🧊 モーションデザイナーと3Dアーティスト](i18n/ja/trilhas/README.md#-モーションデザイナーと3dアーティスト) — アニメーションを作り、モデリングし、視覚効果を制作する。
- [🎧 音楽プロデューサーとポッドキャスター](i18n/ja/trilhas/README.md#-音楽プロデューサーとポッドキャスター) — 録音し、ミックスし、音楽とポッドキャストを公開する。
- [✍️ ライター、コピーライター、作家](i18n/ja/trilhas/README.md#️-ライターコピーライター作家) — 伝え、納得させ、売れる文章を書く。
- [🎯 トラフィックマネージャー](i18n/ja/trilhas/README.md#-トラフィックマネージャー) — 有料メディアを計画し、購入し、最適化する。
- [📣 デジタルマーケター](i18n/ja/trilhas/README.md#-デジタルマーケター) — デジタルで顧客を引きつけ、転換し、維持する。
- [📲 SNS運用担当とコンテンツクリエイター](i18n/ja/trilhas/README.md#-sns運用担当とコンテンツクリエイター) — SNS向けのコンテンツを企画し、制作する。
- [🤝 営業とSDR](i18n/ja/trilhas/README.md#-営業とsdr) — 見込み客を開拓し、交渉し、契約をまとめる。
- [🛒 店舗オーナーとECマネージャー](i18n/ja/trilhas/README.md#-店舗オーナーとecマネージャー) — オンラインで販売し、ネットショップを運営する。
- [🚀 起業家](i18n/ja/trilhas/README.md#-起業家) — 事業を立ち上げ、成長させる。
- [📦 プロダクトマネージャー](i18n/ja/trilhas/README.md#-プロダクトマネージャー) — 何を、なぜ作るのかを決める。
- [🗂️ プロジェクトマネージャーとアジャイル実践者](i18n/ja/trilhas/README.md#️-プロジェクトマネージャーとアジャイル実践者) — 人、期限、成果物を整理する。
- [💰 金融、投資、会計](i18n/ja/trilhas/README.md#-金融投資会計) — 個人と企業のお金を管理する。
- [👥 人事と採用](i18n/ja/trilhas/README.md#-人事と採用) — 人を引きつけ、育て、支える。
- [⚖️ 弁護士と法務担当者](i18n/ja/trilhas/README.md#️-弁護士と法務担当者) — 法律、契約、コンプライアンスに携わる。
- [🛟 カスタマーサポートとカスタマーサクセス](i18n/ja/trilhas/README.md#-カスタマーサポートとカスタマーサクセス) — 問題を解決し、顧客を成功へ導く。
- [🎓 教員と教育者](i18n/ja/trilhas/README.md#-教員と教育者) — 教え、学習教材を作る。
- [📚 学生(受験生、大学生、独学者)](i18n/ja/trilhas/README.md#-学生受験生大学生独学者) — 自分の力で、無料で、方法を持って学ぶ。
- [🔬 研究者と科学者](i18n/ja/trilhas/README.md#-研究者と科学者) — 科学的な知見を生み出し、発表する。
- [🩺 医療従事者](i18n/ja/trilhas/README.md#-医療従事者) — 人の健康を支え、医療でデータとテクノロジーを活用する。
- [🔌 メイカー、電子工作、ロボティクス](i18n/ja/trilhas/README.md#-メイカー電子工作ロボティクス) — ハードウェア、センサー、マイコンでプロジェクトを作る。
- [🏝️ フリーランスとリモートワーカー](i18n/ja/trilhas/README.md#️-フリーランスとリモートワーカー) — 独立して、または遠隔で働く。
- [🧰 すべての人へ: デジタル生活の基本](i18n/ja/trilhas/README.md#-すべての人へ-デジタル生活の基本) — 誰にでも役立つツール、アプリ、心がけ。

## 🤖 すべての分野のAI

> どの分野のページにもAIセクションがあります。AIリンクは合計2465件で、そのうち734件が厳選リンクです。職種向けツール、エージェント用のスキル、プラグイン、MCP、無料コース、プロンプトガイド、規制、責任ある利用を扱います。

- [🤖 **すべての分野のAI**](i18n/ja/ia/README.md): 各分野のAIセクションを、部門別に1か所へ集めました。
- 💡 例: [動画編集](i18n/ja/areas/criacao/edicao-de-video.md#-動画編集のai) · [有料トラフィック](i18n/ja/areas/marketing-vendas/trafego-pago.md#-有料トラフィックのai) · [法務と法律](i18n/ja/areas/negocios/juridico.md#-法務と法律のai) · [医学と医療](i18n/ja/areas/ciencia-educacao/saude.md#-医学と医療のai) · [教育と指導](i18n/ja/areas/ciencia-educacao/educacao.md#-教育と指導のai) · [QAとテスト](i18n/ja/areas/tecnologia/qa-testes.md#-qaとテストのai) · [会計と税務](i18n/ja/areas/negocios/contabilidade.md#-会計と税務のai) · [UI/UXデザイン](i18n/ja/areas/criacao/design-ui-ux.md#-uiuxデザインのai).

## 🧠 職種別のAIリポジトリ1000件

> **38000件のリポジトリ**(重複を除くと26307件)。38職種それぞれに1000件、100%がAI、新しいツール、AIによる自動化に特化しています。テーマ別に分け、スター数順に並べ、それぞれに説明を付けています。

- [🎨 フロントエンド開発者](i18n/ja/ia/profissoes/desenvolvedor-front-end.md)
- [⚙️ バックエンド開発者](i18n/ja/ia/profissoes/desenvolvedor-back-end.md)
- [📱 モバイル開発者](i18n/ja/ia/profissoes/desenvolvedor-mobile.md)
- [🎮 ゲーム開発者](i18n/ja/ia/profissoes/desenvolvedor-de-jogos.md)
- [☁️ DevOps、SRE、クラウド](i18n/ja/ia/profissoes/devops-sre.md)
- [✅ QAエンジニアとテストアナリスト](i18n/ja/ia/profissoes/qa.md)
- [📊 データアナリストとBI](i18n/ja/ia/profissoes/analista-de-dados.md)
- [🔀 データエンジニア](i18n/ja/ia/profissoes/engenheiro-de-dados.md)
- [🧠 データサイエンティストとMLエンジニア](i18n/ja/ia/profissoes/cientista-de-dados.md)
- [✨ AIエンジニアとLLMエンジニア](i18n/ja/ia/profissoes/engenheiro-de-ia.md)
- [🛡️ セキュリティ専門家](i18n/ja/ia/profissoes/seguranca.md)
- [🖌️ UI/UXデザイナー](i18n/ja/ia/profissoes/designer-ui-ux.md)
- [🖍️ グラフィックデザイナーとイラストレーター](i18n/ja/ia/profissoes/designer-grafico.md)
- [🎞️ 動画エディター](i18n/ja/ia/profissoes/editor-de-video.md)
- [🎥 フィルムメーカーと映画制作者](i18n/ja/ia/profissoes/filmmaker.md)
- [📷 フォトグラファー](i18n/ja/ia/profissoes/fotografo.md)
- [🧊 モーションデザイナーと3Dアーティスト](i18n/ja/ia/profissoes/motion-3d.md)
- [🎧 音楽プロデューサーとポッドキャスター](i18n/ja/ia/profissoes/produtor-musical.md)
- [✍️ ライター、コピーライター、作家](i18n/ja/ia/profissoes/redator.md)
- [🎯 トラフィックマネージャー](i18n/ja/ia/profissoes/gestor-de-trafego.md)
- [📣 デジタルマーケター](i18n/ja/ia/profissoes/profissional-de-marketing.md)
- [📲 SNS運用担当とコンテンツクリエイター](i18n/ja/ia/profissoes/social-media.md)
- [🤝 営業とSDR](i18n/ja/ia/profissoes/vendedor.md)
- [🛒 店舗オーナーとECマネージャー](i18n/ja/ia/profissoes/e-commerce.md)
- [🚀 起業家](i18n/ja/ia/profissoes/empreendedor.md)
- [📦 プロダクトマネージャー](i18n/ja/ia/profissoes/product-manager.md)
- [🗂️ プロジェクトマネージャーとアジャイル実践者](i18n/ja/ia/profissoes/gerente-de-projetos.md)
- [💰 金融、投資、会計](i18n/ja/ia/profissoes/financas.md)
- [👥 人事と採用](i18n/ja/ia/profissoes/rh.md)
- [⚖️ 弁護士と法務担当者](i18n/ja/ia/profissoes/advogado.md)
- [🛟 カスタマーサポートとカスタマーサクセス](i18n/ja/ia/profissoes/atendimento.md)
- [🎓 教員と教育者](i18n/ja/ia/profissoes/professor.md)
- [📚 学生(受験生、大学生、独学者)](i18n/ja/ia/profissoes/estudante.md)
- [🔬 研究者と科学者](i18n/ja/ia/profissoes/pesquisador.md)
- [🩺 医療従事者](i18n/ja/ia/profissoes/saude.md)
- [🔌 メイカー、電子工作、ロボティクス](i18n/ja/ia/profissoes/maker.md)
- [🏝️ フリーランスとリモートワーカー](i18n/ja/ia/profissoes/freelancer.md)
- [🧰 すべての人へ: デジタル生活の基本](i18n/ja/ia/profissoes/usuario.md)

## 🔢 数字で見るガイド

> 件数は、ジェネレーターが実行のたびに計算します。

| 指標 | 値 |
|---|---|
| 🔗 分野カタログのリンク数 | 17357 |
| 🧬 カタログ内の重複を除いたURL数 | 15493 |
| 🗂️ 部門 / 分野 | 9 / 72 |
| ⭐ 厳選リンク | 1998 |
| 🤖 各分野のAIリンク数 | 2465 |
| 🧠 職種別のAIリポジトリ(重複除く) | 38000 (26307) |
| 📋 情報源にしたキュレーションリスト | 397 |
| 🌍 ガイドの言語数 | 12 |
| 🧾 種類別 | 🌐 サイト 8638 · 📦 リポジトリ 6084 · 🛠️ ツール 661 · 📖 ドキュメント 616 · 🎓 コース 281 · 📋 awesomeリスト 224 · 👥 コミュニティ 183 · 🎬 動画 174 · 📚 書籍 150 · 📱 アプリ 137 · 📺 チャンネル 118 · 📄 学術論文 91 |

| 部門 | カバー範囲 | 分野 | 🔗 リンク |
|---|---|:--:|:--:|
| [💻 テクノロジーと開発](i18n/ja/areas/tecnologia/README.md) | プログラミング、Web、モバイル、ゲーム、インフラ、テスト、ソフトウェアを作る仕事。 | 16 | 5051 |
| [🤖 データと人工知能](i18n/ja/areas/dados-ia/README.md) | データ分析、データエンジニアリング、データサイエンス、machine learning、生成AI。 | 5 | 1289 |
| [🔒 セキュリティとプライバシー](i18n/ja/areas/seguranca/README.md) | 攻撃型・防御型のサイバーセキュリティ、OSINT、プライバシー、コンプライアンス。 | 3 | 722 |
| [🎬 デザインとクリエイティブ](i18n/ja/areas/criacao/README.md) | デザイン、動画、映画、映像・音響素材、写真、アニメーション、音声、執筆。 | 9 | 1895 |
| [📈 マーケティングと営業](i18n/ja/areas/marketing-vendas/README.md) | デジタルマーケティング、有料トラフィック、SEO、SNS、営業、EC。 | 6 | 1170 |
| [💼 ビジネスとマネジメント](i18n/ja/areas/negocios/README.md) | 起業、プロダクト、プロジェクト、金融、人事、法務。 | 8 | 1622 |
| [🔬 科学、医療、教育](i18n/ja/areas/ciencia-educacao/README.md) | 理系・生物系の科学、医療、人文学、語学、教育。 | 11 | 2238 |
| [🧭 キャリアと生産性](i18n/ja/areas/carreira/README.md) | 求人、リモートワーク、フリーランス、生産性、コミュニティ、アクセシビリティ。 | 5 | 997 |
| [🧰 ツールとユーティリティ](i18n/ja/areas/ferramentas/README.md) | オンラインツール、OS別アプリ、セルフホスティング、API、無料リソース。 | 9 | 2373 |

## 📜 利用できるスクリプト

> すべてPythonで生成されます。手作業で編集されたページはありません。

| スクリプト | 内容 |
|---|---|
| [`scripts/coletar.py`](scripts/coletar.py) | キュレーションリストをダウンロードし(Scrapling、予備としてgit)、各リンクの名前、説明、トピックを抽出します。 |
| [`scripts/selecionar.py`](scripts/selecionar.py) | 正規化と重複排除を行い、ライセンスポリシーを適用し、説明を必須とし、情報源を順番に回しながら上限付きで各分野のリンクを選びます。 |
| [`scripts/coletar_repos_ia.py`](scripts/coletar_repos_ia.py) | GitHubで各職種のAIリポジトリを職種ごとに1000件検索します。 |
| [`scripts/descrever.py`](scripts/descrever.py) | 説明のないリポジトリの公開説明文を取得します。 |
| [`scripts/traduzir.py`](scripts/traduzir.py) | オープンモデルを使い、オフラインで説明とトピックをガイドの各言語へ翻訳します。 |
| [`scripts/gerar.py`](scripts/gerar.py) | README、部門・分野・学習パス・AIの各ページを全言語分、さらにカタログとCSVを生成します。 |
| [`scripts/checar_links.py`](scripts/checar_links.py) | リンクが応答するかを確認し、リンク切れに印を付けます。 |
| [`tests/validar.py`](tests/validar.py) | データ、ページ、アンカー、説明、言語、件数を検証します。 |

## 🛠️ 再生成と検証

> 生成と検証に必須なのはPython 3の標準ライブラリだけです。Scraplingは収集を改善し、Argos Translateが翻訳を行います。

```bash
python3 scripts/coletar.py            # → data/brutos.jsonl.gz
python3 scripts/descrever.py          # → data/descricoes.json
python3 scripts/selecionar.py         # → data/links.jsonl
python3 scripts/coletar_repos_ia.py   # → data/repos-ia.jsonl
python3 scripts/traduzir.py           # → data/i18n/desc.<idioma>.json.gz
python3 scripts/gerar.py              # → README*, areas/, trilhas/, ia/, i18n/
python3 tests/validar.py              # → "OK"
```

## 🤝 貢献

> 提案は大歓迎です。足りないリンク、新しい分野、学習パス、より良い翻訳など。

- **新しいリンク:** `data/essenciais.json` に追加するか(その分野の厳選リンクの場合)、`data/fontes.json` に**キュレーションリスト**を提案してください。その後、ジェネレーターを実行します。
- **リンク切れや翻訳の問題:** ページのアドレスとリンクを添えてissueを作成してください。
- 手順は [docs/08 · 貢献方法](docs/08-como-contribuir.md) と [CONTRIBUTING.md](CONTRIBUTING.md) にあります。

## ⚖️ ライセンスとクレジット

> リンクはコミュニティが管理する**397件のキュレーションリスト**から集めており、ライセンスとともに [docs/07](docs/07-fontes-e-licencas.md) と各分野のフッターに掲載しています。このガイドの内容は**CC BY-SA 4.0**、スクリプトは**MIT**です([LICENSE](LICENSE)を参照)。ライセンスのないリスト、GPL、非営利限定のリストの文章はコピーしていません。

## ⚠️ ご注意

> このガイドは第三者のサイトやリポジトリを指しています。いずれとも提携関係はなく、各内容の責任は管理者にあります。リンクは変わります。リンク切れを見つけたらお知らせください。攻撃的なセキュリティの内容は、学習と**許可された範囲内での利用のみ**を目的としています。

## 🌟 Star History

> このガイドが役に立ったら、ぜひスターをお願いします。より多くの人に届くきっかけになります。

[![Star History Chart](https://api.star-history.com/svg?repos=arthurspk/guiadoconhecimento&type=Date)](https://star-history.com/#arthurspk/guiadoconhecimento&Date)
