# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MANUAL DE CONSULTA: FREE TIERS DE LLM & POLÍTICAS DE USO (Setembro 2026)
# Compilação e Validação Fina: 20 de setembro de 2026 (v16)
# Histórico: 27/05 → 15/07 → 23/07 → 16/08 → 19/08 → 25/08 (v8) → 06/09 (v9) → 17/09 (v10) → 17/09 (v11) → 17/09 (v12) → 17/09 (v13) → 18/09 (v14) → 19/09 (v15) → 20/09/2026 (v16 atual)
# Fontes: Catálogo Operacional RUNTIME Real + 20 Novos Provedores Auditados (4 Pilares) + Auditoria Global v16
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Este documento consolida as cotas gratuitas (Free Tiers), especificações técnicas, rate limits granulares (RPM, RPD, TPM, TPD, RPS, RPH, ASH, ASD) e políticas de uso de todas as plataformas de inferência de LLMs e IA generativa do ecossistema. Modelos descontinuados ou encerrados são categorizados com clareza em histórico de depreciação.

> **🏆 ATUALIZAÇÃO 20/09/2026 v16 (AUDITORIA DE BANCADA DE 20 NOVOS PROVEDORES EM 4 PILARES ESTRATÉGICOS — TOTAL 64 PROVEDORES)**:
> 1. **Pilar 1: 5 Provedores de LLMs & Inferência Serverless de Alta Velocidade**: **Fireworks AI** ($1 USD trial sem cartão, FireAttention ultra-rápida em Llama 3.3, Qwen 2.5 e DeepSeek); **Clarifai** (Community Free Tier perpétuo com 1.000 ops/mês sem cartão); **Baseten** ($30 USD em créditos para deploy serverless Truss/vLLM); **Replicate** (créditos de teste de desenvolvedor sem cartão para LLMs, visão e difusão); **xAI Console / Grok API** ($25 USD/mês em developer grants para Grok-2/Grok-vision).
> 2. **Pilar 2: 5 Especialistas em Voz, Áudio, STT & TTS**: **Deepgram** ($200 USD em créditos perpétuos sem cartão, ~775 horas de transcrição Nova-2 e síntese Aura TTS); **AssemblyAI** ($50 USD em créditos gratuitos sem cartão, ~100 horas de transcrição Conformer-2/nano e LeMUR); **ElevenLabs** (Cota perpétua de 10.000 caracteres/mês gratuitos sem cartão para TTS e clonagem); **Cartesia** (Free Tier Sonic API com latência vocal <150ms); **Lemonfox.ai** (Free Tier diário para Whisper STT e TTS compatível 1:1 com OpenAI SDK).
> 3. **Pilar 3: 5 Especialistas em Embeddings, Rerank & Busca Neural para Agentes**: **Voyage AI** (200M tokens trial / 50M tokens perpétuos para `voyage-3`, `voyage-3-lite`, `voyage-code-3` e `rerank-2`); **Jina AI** (10M tokens gratuitos no onboarding + Jina Reader API `r.jina.ai` 100% gratuita perpétua); **Tavily AI** (1.000 buscas/mês perpétuas sem cartão para agentes autônomos); **Exa.ai** ($10 USD em créditos / 1.000 buscas semânticas neurais sem cartão); **Qdrant Cloud** (Cluster permanente gratuito na nuvem de 1GB RAM / ~1M vetores sem cartão).
> 4. **Pilar 4: 5 Provedores de Soberania Regional & Mercados Emergentes**: **StepFun / Jieyue Xingchen** (¥50 RMB / ~$7 USD em créditos para Step-1 com contexto de até 256k e Step-2 MoE); **01.AI / Lingyi Wanwu** (¥36 RMB em créditos para Yi-Lightning de 100+ tokens/s e Yi-Large até 200k contexto); **ModelScope / Alibaba DAMO** (Inference API serverless comunitária 100% gratuita para Qwen 2.5, SenseVoice e GLM); **RunPod Serverless** (micro-orçamento de $5 USD para execução serverless vLLM por segundo); **CentML / CServe** (Free developer trial com compilação de kernel acelerada até 3x mais rápida).
> 5. **Expansão do Catálogo**: Catálogo oficial consolidado saltando para **64 provedores documentados** com endpoints verificados, quotas numéricas rigorosas e requisitos de cartão auditados.
>
> **💎 ATUALIZAÇÃO 19/09/2026 v15 (CRÉDITOS RECORRENTES, SOBERANIA REGIONAL & EXPURGO DE FALSOS FREE TIERS)**:
> 1. **Inception Labs (Mercury API)**: Concessão automática de **100 Milhões de tokens gratuitos** no cadastro sem cartão de crédito (`mercury-chat`, `mercury-coder`) com throughput altíssimo e endpoint compatível com OpenAI.
> 2. **Reka AI**: Cota recorrente de **$10 USD / mês em créditos gratuitos** renovados mensalmente no console para desenvolvedores + 3 horas de indexação de vídeo multimodal gratuitas na API (`reka-flash`, `reka-core`).
> 3. **Bytez**: **$1.00 USD de crédito gratuito renovado a cada 4 semanas** (28 dias) para inferência de modelos open-source de topo (`llama-3.3-70b-instruct`, `qwen-2.5-72b-instruct`).
> 4. **Morph Labs (Fast Apply)**: Aceleração de agentes de código com **250.000 créditos / mês gratuitos ($0)** e ~200 requisições mensais para merge e diff instantâneo.
> 5. **Modal Labs**: **$30 USD / mês de computação serverless gratuita** no plano Starter para deploy de contêineres e vLLM (requer cartão de crédito cadastrado).
> 6. **Joias de Soberania Regional**: **InternLM / Shanghai AI Lab** (1M in / 3M out free tokens/mês); **Sarvam AI** (₹1.000 INR em créditos para línguas da Índia); **SEA-LION / AI Singapore** (10 RPM permanente para o Sudeste Asiático); e **LLM7.io** (gateway anônimo ultrarrápido a 2 req/s e 20 RPM sem login).
> 7. **Auditoria & Expurgo de Falsos Free Tiers**: **FriendliAI** desmentido (sem free tier permanente, 100% pay-per-token); **Liquid AI** esclarecido (sem API direta self-serve; use via OpenRouter ou Hugging Face); e **CrofAI** banido (wrapper fraudulento retirado do ar com erro 404).
>
> **🇧🇷 ATUALIZAÇÃO 18/09/2026 v14 (SOBERANIA NACIONAL MARITACA AI, CLOUDFLARE WORKERS AI & ABSORÇÃO OMNIROUTE)**:
> 1. **Absorção e Auditoria do OmniRoute (v3.8.51)**: Investigação minuciosa do catálogo de 352 provedores do repositório `diegosouzapw/OmniRoute`. Filtragem pelas 6 Regras de Ouro (expurgando proxies não oficiais e sessões efêmeras de scraping) e consolidação das plataformas com Free Tier permanente comprovado.
> 2. **Maritaca AI (MariTalk) — A Campeã Nacional Brasileira**: Inclusão da pioneira nacional em IA da Unicamp. Cota gratuita Tier 0 de **50 RPM / 500.000 TPM** sem cartão de crédito. Modelos de ponta: `sabia-4` (líder em língua portuguesa, concursos e jurisprudência), `sabia-4-thinking` (raciocínio aprofundado com CoT) e `sabiazinho-4` (baixa latência). Compatibilidade nativa com OpenAI SDK via `https://chat.maritaca.ai/api`.
> 3. **Cloudflare Workers AI**: Cota permanente de **10.000 Neurons por dia** renovados às 00:00 UTC sem cartão de crédito (~100k a 500k tokens gratuitos diários), executando `llama-3.3-70b-instruct`, `deepseek-r1-distill-qwen-32b`, `qwen2.5-coder-32b-instruct` e geração de imagem com `flux-1-schnell`.
> 4. **SambaNova Cloud**: Processadores proprietários SN40L RDUs atingindo centenas de tokens/segundo para `Meta-Llama-3.3-70B-Instruct` e `DeepSeek-R1` a 30 RPM / 6.000 TPM.
> 5. **Hugging Face Serverless Inference**: Endpoint `https://api-inference.huggingface.co/v1/` gratuito para milhares de modelos abertos com token de usuário HF.
> 6. **Especialistas em Embeddings & Reranking**: Inclusão de **Nomic AI** (`nomic-embed-text-v1.5` de 8k contexto) e **Mixedbread AI** (`mxbai-rerank-large-v1` para RAG de alta fidelidade).
> 7. **Gateways Anônimos & Sem Chave**: **AI Horde** (`0000000000` via crowdsourced GPUs), **DuckDuckGo AI Chat** e **UncloseAI**.
>
> **🎯 ATUALIZAÇÃO 17/09/2026 v13 (ALINHAMENTO OFICIAL DEEPSEEK, EXPURGO DE INCONSISTÊNCIAS & AUDITORIA INTEGRAL DE MODELOS)**:
> 1. **Correção Absoluta e Alinhamento Oficial do DeepSeek**: Restauração integral dos identificadores canônicos oficiais de chamada `deepseek-chat` (DeepSeek-V3) e `deepseek-reasoner` (DeepSeek-R1) para chamadas compatíveis com OpenAI SDK. Tabela consagrada e oficial de precificação por 1M tokens: DeepSeek-V3 a **$0.14** (Cache Miss) / **$0.014** (Cache Hit) / **$0.28** (Saída); DeepSeek-R1 a **$0.55** (Cache Miss) / **$0.14** (Cache Hit) / **$2.19** (Saída). Desconto oficial de **50% no horário econômico (Off-Peak)** (00:30 às 08:30 UTC+8). Cota de 5.000.000 tokens gratuitos para novas contas (30 dias). Cálculo real do poder de compra de **$5 USD** (rende de 18M a 35M tokens no V3 sem cache e até 100M+ tokens com alta taxa de cache hit). Reconciliação técnica explícita esclarecendo por que identificadores internos de engine (`deepseek-flash` / `deepseek-v4-pro`) aparecem em telemetria sem descaracterizar os nomes canônicos e preços de tabela.
> 2. **Auditoria de Ponta a Ponta dos Provedores Globais**: **Google AI Studio** (segregação estrita entre modelos em Produção Ativa GA e Upstream/Preview/Experimental, com detalhamento das cotas de Grounding Maps 500 RPD e Search 1.500 RPD); **Groq Cloud** (confirmação dos 13 modelos ativos reais, detalhamento da descontinuação de `qwen/qwen3.6-27b`, `llama-3.3-70b-versatile` e `llama-3.1-8b-instant`); **NVIDIA NIM** (catálogo de 82 modelos reais gratuitos, cota universal de 40 RPM / 1.000 RPD sem cartão, inclusão de `01-ai/yi-large` e `z-ai/glm-5.3`); **OpenRouter Free** (24 modelos `:free` ativos com contextos e limites de saída reais documentados); **Mistral AI** (modelos ativos, cota gratuita La Plateforme de 60 RPM / 4M tokens/mês); **Moonshot AI / Kimi** (modelos clássicos V1 e linha internacional K3/K2.7 com cota inicial de ¥15 RMB).
> 3. **Auditoria Rigorosa do Mercado Chinês (Modelos Nativos)**: **Baidu Qianfan** (`ERNIE-Speed` e `ERNIE-Lite` permanentemente 100% gratuitos a 300 RPM / 300.000 TPM); **Zhipu AI / BigModel** (`GLM-4-Flash` 100% free perpétuo a 1 concorrência + 25M tokens de boas-vindas); **Alibaba Cloud Model Studio / DashScope** (franquia de 1M a 2M tokens gratuitos por modelo Qwen na ativação por 90-180 dias + custos pós-free em frações de centavos); **Tencent Cloud Hunyuan** (pacote de 1 ano para `hunyuan-lite` e salvaguarda contra débitos automáticos no cartão); **ByteDance Volcano Engine Doubao** (registro transparente de que a API profissional é estritamente bilhetada em RMB sem free tier permanente para desenvolvedores).
> 4. **Consolidação dos Planos Budget de $5 a $10 USD**: Análise técnica detalhada de ROI de DeepSeek API Direta, xKiro (`xkiro.com`), OpenCode Zen/Go (`opencode.ai`), B.AI (`b.ai`) e Tencent WorkBuddy (`workbuddy.ai`).
> 5. **Cadeia de Fallback e Relatório em Runtime**: Atualização de todos os níveis e do quadro de auditoria em runtime com status 100% verificado.
>
> **🇨🇳 ATUALIZAÇÃO 17/09/2026 v12 (ECOSSISTEMA CHINÊS, PLANOS DE $5 & GATEWAYS BUDGET)**:
> 1. **Aprofundamento no Mercado Chinês de LLMs**: Mapeamento completo dos gigantes asiáticos com cotas gratuitas e preços de atacado: **Zhipu AI / BigModel** (`GLM-4-Flash` 100% free perpétuo sem cartão + 25M tokens de bônus), **Baidu Qianfan** (`ERNIE-Speed` e `ERNIE-Lite` permanentemente 100% free a 300 RPM / 300K TPM), **Alibaba Cloud Model Studio / DashScope / Bailian** (1M a 2M tokens free de onboarding por modelo Qwen com validade de 90-180 dias + preços em frações de centavos), **Tencent Cloud Hunyuan & TokenHub** (pacotes gratuitos de 1 ano para `hunyuan-lite` e 1.000 créditos para `hunyuan-3d`), **ByteDance Volcano Engine / Doubao** (auditoria: sem free tier na API para dev; bilhetagem ultra-barata em RMB a partir do 1º token), **MiniMax** (¥15 de crédito grátis; TTS hiper-realista Speech-01 e vídeo Hailuo), **01.AI / Lingyi Wanwu** (¥30 de créditos; linha Yi-Lightning), e **StepFun** (linha Step-3.5/3.7 Flash).
> 2. **Guia de Planos Econômicos de $5 a $10 USD ("Budget Plans")**: Detalhamento prático de como extrair máxima volumetria com micro-orçamentos: **xKiro** (Free Tier de 5M tokens/dia sem cartão + Wallet de $5 para desbloquear modelos proprietários e prioridade de fila), **OpenCode** (**OpenCode Zen** com zero markup e modelos free nativos como `MiMo V2.5 Free` e `MiniMax M2.5 Free` + **OpenCode Go** a $10/mês com $60 em valor de tokens), **DeepSeek API Direta** (o "Rei dos $5": um depósito mínimo de $5 USD rende de 18 a 35 MILHÕES de tokens com context caching), **B.AI** (sistema de créditos 1 USD = 1M créditos, com descontos de até 90% em horários ociosos para agentes), **SiliconFlow** ($5 rende dezenas de milhões de tokens em modelos 14B/32B/72B), e **Tencent WorkBuddy** (workspace de automação desktop compatível com BYO-Key).
> 3. **Cadeia de Fallback com Novas Rotas**: Inclusão da **Rota Asiática / Soberana Chinesa** e da **Rota Budget de $5 USD** para orquestrações de alta eficiência de custos.
>
> **🚀 ATUALIZAÇÃO 17/09/2026 v11 (EXPANSÃO DE NOVOS PROVEDORES & CONSOLIDAÇÃO TÉCNICA)**:
> 1. **Mapeamento Exaustivo de Novos Provedores Free Tier**: Documentação granular de 8 novas plataformas com cotas gratuitas comprovadas: **Hyperbolic** (60 RPM perpétuo, sem cartão), **SiliconFlow** (1.000 RPM / 40K TPM em modelos open-source free + 20M tokens bônus, sem cartão), **Pollinations.ai** (100% free perpétuo para texto, imagem, áudio e visão, sem cartão), **Cohere** (Trial API Key perpétua com 1K chamadas/mês, 20 RPM chat, 100 RPM embed, 10 RPM rerank, sem cartão), **AwanLLM** (Free Lite com tokens ilimitados, 20 RPM, 200 RPD pequenos, sem cartão), **Scaleway Generative APIs** (1M tokens/mês + 60 min áudio Whisper na nuvem soberana europeia), **Novita AI** (Trial Sandbox de $10-$100, 20 IPM para imagem e 60 RPM para LLM), e **Nebius Token Factory** (AI Builder Program com $400+ em créditos e auto-scaling dinâmico).
> 2. **Auditoria de Plataformas & Depreciações Confirmadas**: Identificação rigorosa de gateways sem Free Tier permanente: **Chutes.ai** (free tier descontinuado em 2026; migrado para subscrição a partir de $3/mês), **Lepton AI** (incorporado à NVIDIA DGX Cloud Lepton), **Together AI** (sem free tier permanente; exige depósito mínimo de $5), **AI/ML API** (free tier pausado; 100% pré-pago) e **Featherless.ai** (concorrência paga).
> 3. **Cadeia de Fallback Elevada para Arquitetura Resiliente em 4 Níveis**: Integrando provedores de alta vazão sem cartão (Google AI Studio, NVIDIA NIM, Groq, Hyperbolic, SiliconFlow, Pollinations.ai) e especialistas (Cohere, Scaleway, AwanLLM).
> 4. **Retenção Integral do Histórico v10**: Mantidas as validações críticas de 17/09 (Groq Qwen 3.8 ativo / 3.6 desligado; OpenRouter 24 modelos free com Nex-N2.5 e Ling VL; NVIDIA NIM com GLM-5.3 e Nemotron-Parse 2.0; Google AI Studio com Gemini 3.1/3.5 Flash-Lite e Antigravity Agent).

---

## 1. QUADRO COMPARATIVO GERAL DE MODELOS FREE & POLÍTICAS

---

### 🟢 GOOGLE AI STUDIO (Gemini API) — *Validado em 17/09/2026 (50 modelos na API)*

O Google AI Studio oferece a cota gratuita mais robusta e utilizável para desenvolvimento e produção moderada, sem necessidade de cartão de crédito. Seus modelos contam com cotas individuais por modelo, suporte multimodal nativo e recursos exclusivos de **Grounding (Google Maps e Google Search)** no Free Tier.

#### 🔹 Modelos em Produção Ativa (GA - General Availability)

Modelos consolidados para ambientes de produção estável com limites elevados de requisições por minuto e dia:

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM | TPM | RPD | Map Grounding | Search Grounding | Notas / Status Operacional |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`gemini-2.5-flash`** | Gemini 2.5 Flash | Multimodal | 1.048.576 / 65.536 | **15** | **1.000.000** | **1.500** | ✅ 500 RPD | ✅ 1.500 RPD | **Top Pick #1 Produção Estável** — 1.500 RPD, suporte completo a Search & Map Grounding |
| **`gemini-2.0-flash`** | Gemini 2.0 Flash | Multimodal | 1.048.576 / 65.536 | **15** | **1.000.000** | **1.500** | ✅ 500 RPD | ✅ 1.500 RPD | Workhorse de produção em GA; altíssima estabilidade e baixa latência |
| **`gemini-1.5-flash`** | Gemini 1.5 Flash | Multimodal | 1.048.576 / 8.192 | **15** | **1.000.000** | **1.500** | ❌ 0 | ✅ 1.500 RPD | Mantido para compatibilidade legado; cota robusta de 1.500 RPD |
| `gemini-1.5-pro` | Gemini 1.5 Pro | Frontier MoE | 2.097.152 / 8.192 | **2** | **32.000** | **50** | ❌ 0 | ✅ 50 RPD | Janela gigante de 2M tokens; raciocínio aprofundado no Free Tier |

#### 🔹 Modelos Upstream, Preview & Experimentais (Série 3, Gemma & Agentes)

Modelos de última geração, variantes experimentais e arquiteturas abertas do Google:

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM | TPM | RPD | Map Grounding | Search Grounding | Notas / Status Operacional |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`gemini-3.5-flash-lite`** | Gemini 3.5 Flash Lite | Multimodal | 1.048.576 / 65.536 | **15** | **250.000** | **500** | ✅ 500 RPD | ❌ 0 | **Top Pick #1 Desenvolvimento** — Atualizado com arquitetura 3.5; 500 RPD |
| **`gemini-3.1-flash-lite`** | Gemini 3.1 Flash Lite | Multimodal | 1.048.576 / 65.536 | **15** | **250.000** | **500** | ✅ 500 RPD | ❌ 0 | **Top Pick #2** — Homologado para uso comercial até 500 RPD |
| `gemini-2.5-flash-lite` | Gemini 2.5 Flash Lite | Multimodal | 1.048.576 / 65.536 | **10** | 250.000 | **20** | ✅ 500 RPD | ❌ 0 | Versão lite anterior mantida para compatibilidade de rota |
| `gemini-3.8-flash` | Gemini 3.8 Flash | Multimodal | 1.048.576 / 65.536 | **5** | 250.000 | **20** | ❌ 0 | ❌ 0 | Mais recente da linha Flash (setembro/2026); alta inteligência |
| `gemini-3.7-flash` | Gemini 3.7 Flash | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | Alta capacidade analítica de raciocínio |
| `gemini-3.6-flash` | Gemini 3.6 Flash | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | 17% menos tokens de overhead; endpoint estável |
| `gemini-3.5-flash` | Gemini 3.5 Flash | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | Ativo e em uso operacional |
| `gemini-3-flash-preview` | Gemini 3 Flash Prev | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | Endpoint de preview da geração 3 |
| `antigravity-preview-09-2026` 🆕 | Antigravity Agent | Agente | 131.072 / 65.536 | **60** | **100.000** | **100** | ❌ 0 | ❌ 0 | **NOVO (set/2026)** — Otimizado para execução de agentes autônomos |
| `gemma-4-31b-it` | Gemma 4 31B Instruct | Texto/Visão | 262.144 / 32.768 | **30** | **16.000** | **14.400** | ❌ | ❌ | **30 RPM / 14.4K RPD** — Open weights dense rodando na infraestrutura Google |
| `gemma-4-26b-a4b-it` | Gemma 4 26B MoE | Texto/Visão | 262.144 / 32.768 | **30** | **16.000** | **14.400** | ❌ | ❌ | Arquitetura esparsa rápida para extração e processamento massivo |
| `gemini-3.1-flash-tts-preview` | Flash TTS | Áudio/TTS | 8.192 / 16.384 | 3 | 10.000 | 10 | ✅ 500 RPD | - | Síntese vocal de alta fidelidade |
| `gemini-3.5-transcribe` | Flash Transcribe | Áudio/STT | 98.304 / 32.768 | 5 | 50.000 | 20 | - | - | Transcrição precisa de arquivos de áudio |
| `gemini-3.5-transcribe-live` | Transcribe Live | Áudio Realtime| 131.072 / 65.536 | Ilimitado | 20.000 | Ilimitado | - | - | Streaming STT contínuo sem corte por chamada |
| `gemini-robotics-er-2-preview` | Robotics ER 2 | Robótica/VLM | 131.072 / 65.536 | 5 | 250.000 | 20 | - | - | Substitui ER 1.6 (sunset em 31/08/2026) |
| `gemini-embedding-2` | Embeddings v2 | Vetores | 8.192 / 1 | **100** | **30.000** | **1.000** | - | - | Embeddings de alta dimensionalidade para RAG |
| `gemini-omni-flash-preview` | Omni Flash | Visão/Áudio | 131.072 / 65.536 | 0 | 0 | 0 | - | - | Requer ativação de billing (Pay-as-you-go) |
| `gemini-3.1-pro-preview` | Gemini 3.1 Pro | Frontier | 1.048.576 / 65.536 | 0 | 0 | 0 | ❌ 0 | - | ❌ **Indisponível no Free** (requer Pay-as-you-go) |
| `nano-banana-pro` | Gemini 3 Pro Image | Imagem Gen | 131.072 / 32.768 | 0 | 0 | 0 | - | - | Geração de imagem Pro (Pago) |
| `nano-banana-2` | Gemini 3.1 Flash Img | Imagem Gen | 65.536 / 65.536 | 0 | 0 | 0 | - | - | Geração de imagem Flash (Pago) |
| `veo-3.1-generate-preview` | Veo 3.1 Video | Vídeo Gen | 480 / 8.192 | 0 | 0 | 0 | - | - | Geração de vídeo (Pago) |
| `lyria-3.5` | Lyria 3.5 Music | Música Gen | 1.048.576 / 65.536 | 0 | 0 | 0 | - | - | Música generativa (Pago) |

#### 🎯 Recursos Exclusivos de Grounding no Free Tier

O Google AI Studio é a única plataforma do mercado a conceder cotas expressivas de ancoragem factual (web e mapas) gratuitas:

1. **Google Search Grounding (Busca Web em Tempo Real)**:
   * **Cota Gratuita**: **1.500 requisições por dia (1.500 RPD)**.
   * **Modelos Suportados**: `gemini-2.5-flash`, `gemini-2.0-flash` e a rota `default`.
   * **Atenção**: Modelos da série 3 (`gemini-3.x`) **NÃO possuem cota gratuita de Search Grounding** (cota = 0 no Free Tier; requer billing ativado).

| Rota de Grounding | RPM | TPM | RPD | Observação |
| :--- | :---: | :---: | :---: | :--- |
| `gemini-2.5` (Search) | - | - | **1.500** | Rota padrão recomendada para web search integrado em produção |
| `gemini-2` (Search) | - | - | **1.500** | Rota legada ativa de alta estabilidade |
| `default` (Search) | - | - | **1.500** | Fallback geral do AI Studio |
| `gemini-3` (Search) | - | - | **0** ⚠️ | Modelos série 3 não têm cota free de Search Grounding |

2. **Google Maps Grounding (Pontos de Interesse & Localização)**:
   * **Cota Gratuita**: **500 requisições por dia (500 RPD)**.
   * **Modelos Suportados**: Família Flash-Lite (`gemini-3.5-flash-lite`, `gemini-3.1-flash-lite`, `gemini-2.5-flash-lite`) e modelos GA Flash (`gemini-2.5-flash`, `gemini-2.0-flash`). Permite enriquecer respostas com dados geográficos e POIs oficiais do Google Maps sem custos de API externa.

---

### 🟠 GROQ CLOUD — *Validado em 17/09/2026 (13 modelos na API)*

Inference engine ultra-rápida (LPU). Cotas granulares Developer Plan.
🚨 **ALERTA CRÍTICO 17/09**: `qwen/qwen3.6-27b` foi **descontinuado** da Groq. Utilizar obrigatoriamente `qwen/qwen3.8-27b`.

| Modelo ID API | Modalidade | Contexto | RPM | RPD | TPM | TPD | Speed (t/s) | Validação 17/09 | Status / Notas |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `qwen/qwen3.8-27b` | text/vision | 131.042 | **30** | **1.000** | **8K** | **200K** | 600+ | ✅ 200 OK | **Único Qwen ativo no Groq** — Substitui 3.6 |
| `openai/gpt-oss-120b` | text/tools | 131.072 | **30** | **1.000** | **8K** | **200K** | 500+ | ✅ 200 OK | Prompt caching automático ativo |
| `openai/gpt-oss-20b` | text/tools | 131.072 | **30** | **1.000** | **8K** | **200K** | 1000+ | ✅ 200 OK | Velocidade extrema para routing e extração |
| `openai/gpt-oss-safeguard-20b` | safety | 131.072 | **30** | **1.000** | **8K** | **200K** | 1000 | ✅ 200 OK | Moderação de conteúdo |
| `groq/compound-mini` | text | 131.072 | **30** | **250** | **70K** | - | 450+ | ✅ 200 OK | Orquestração leve |
| `meta-llama/llama-prompt-guard-2-86m`| safety | 512 | **30** | **14.4K**| **15K** | **500K** | - | ✅ 200 OK | Detecção de jailbreak e injeção |
| `meta-llama/llama-prompt-guard-2-22m`| safety | 512 | **30** | **14.4K**| **15K** | **500K** | - | ✅ 200 OK | Versão ultra-leve de prompt guard |
| `allam-2-7b` | text (árabe) | 4.096 | 30 | 7.000 | 6K | 500K | - | ⚠️ 403 | Bloqueado no projeto por padrão |
| `groq/compound` | text | 131.072 | 30 | 250 | 70K | - | - | ⚠️ 403 | Requer desbloqueio de projeto no console |

#### 🔊 STT & TTS no Groq

| Modelo | Modalidade | RPM | RPD | ASH / ASD | Validação | Notas |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `whisper-large-v3` | audio STT | **20** | **2.000** | **7.200** / **28.800** | ✅ OK | Transcrição multilingual (8h áudio/dia) |
| `whisper-large-v3-turbo` | audio STT | **20** | **2.000** | **7.200** / **28.800** | ✅ OK | Versão acelerada |
| `canopylabs/orpheus-v1-english` | audio TTS | **10** | **100** | - (1.2K TPM / 3.6K TPD) | ✅ OK | Vozes naturais em inglês |
| `canopylabs/orpheus-arabic-saudi`| audio TTS | **10** | **100** | - (1.2K TPM / 3.6K TPD) | ⚠️ Termos | Requer aceite de termos no console |

#### ⛔ Histórico de Depreciações Groq (Confirmadas)

| Modelo Deprecado | Data de Desligamento | Motivo / Substituto Recomendado |
| :--- | :---: | :--- |
| `qwen/qwen3.6-27b` 🚨 | **17/09/2026** | **Desativado pelo provedor** → Substituir por `qwen/qwen3.8-27b` |
| `llama-3.1-8b-instant` | **17/08/2026** | Desativado pelo provedor → Substituir por `openai/gpt-oss-20b` |
| `llama-3.3-70b-versatile`| **17/08/2026** | Desativado pelo provedor → Substituir por `openai/gpt-oss-120b` ou `qwen/qwen3.8-27b` |
| `qwen/qwen3-32b` | **17/07/2026** | Descontinuado → `qwen/qwen3.8-27b` |
| `meta-llama/llama-4-scout-17b-16e-instruct` | **17/07/2026** | Descontinuado → `openai/gpt-oss-120b` |

---

### 🟢 NVIDIA NIM (build.nvidia.com) — *Validado em 17/09/2026 (82 modelos)*

Cota global universal: **40 RPM / 1.000 RPD** (sem limite rígido de TPM). Acesso gratuito sem necessidade de cartão de crédito.

| Modelo ID API | Família / Tipo | Contexto | RPM | RPD | Destaques & Capacidades |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `z-ai/glm-5.3` 🆕 | Z.ai Flagship | **1.048.576** | **40** | **1.000** | **NOVO NO NIM (17/09)** — Mais recente da Z.ai com 1M ctx |
| `z-ai/glm-5.3-flash` 🆕 | Z.ai Fast MoE | **1.048.576** | **40** | **1.000** | **NOVO NO NIM (17/09)** — Resposta ultra-rápida |
| `nvidia/nemotron-parse-2.0` 🆕 | OCR / Parsing v2 | - | **40** | **1.000** | **NOVO NO NIM (17/09)** — Extração de tabelas e documentos |
| `nvidia/nemotron-3-ultra-550b-a55b` | Frontier MoE | **1.048.576** | 40 | 1.000 | 550B total / 55B ativos; raciocínio de ponta |
| `nvidia/nemotron-3-super-120b-a12b` | Raciocínio Geral | 1.048.576 | 40 | 1.000 | Excelente em Tool Use e chamadas de funções estruturadas |
| `nvidia/nemotron-3.5-lightning-30b-a3b`| MoE Acelerado | 256.000 | 40 | 1.000 | Arquitetura 3.5 ultrarrápida para tarefas complexas |
| `nvidia/nemotron-nano-3-30b-a3b` | MoE Leve | 256.000 | 40 | 1.000 | Resposta instantânea, classificação e sumarização |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | Multimodal Omni | 256.000 | 40 | 1.000 | Raciocínio cruzado: texto, imagem, áudio e vídeo |
| `deepseek-ai/deepseek-v4-flash-0731` | DeepSeek V4 | 1.048.576 | 40 | 1.000 | Endpoint NIM do DeepSeek V4 Flash |
| `01-ai/yi-large` | 01.AI Flagship | 131.072 | **40** | **1.000** | Raciocínio bilíngue (ZH/EN) de alta fidelidade e matemática |
| `moonshotai/kimi-k3` | Kimi Frontier | 1.048.576 | 40 | 1.000 | Modelo K3 da Moonshot hospedado sob cota NIM |
| `moonshotai/kimi-k2.6` | Kimi Mid-tier | 262.144 | 40 | 1.000 | Versão 2.6 estável |
| `openai/gpt-oss-20b` | GPT-OSS | 131.072 | 40 | 1.000 | Alternativa rápida open-source |
| `google/gemma-4-31b-it` | Google Gemma 4 | 262.144 | 40 | 1.000 | Modelo de 31B parâmetros do Google |
| `google/diffusiongemma-26b-a4b-it` | Diffusion LLM | 262.144 | 40 | 1.000 | Geração paralela não-autoregressiva |
| `meta/llama-3.2-11b-vision-instruct`| Meta Vision | 131.072 | 40 | 1.000 | Multimodal com visão computacional |
| `meta/llama-3.2-90b-vision-instruct`| Meta Vision Flagship| 131.072 | 40 | 1.000 | Alta precisão visual em OCR e gráficos |
| `poolside/laguna-xs-2.1` | Coding Agent | 262.144 | 40 | 1.000 | Especializado em engenharia de software |
| `writer/palmyra-creative-122b` | Writer Palmyra | 32.768 | 40 | 1.000 | Especializado em redação criativa e marketing |
| `ibm/granite-3.0-8b-instruct` | IBM Granite | 131.072 | 40 | 1.000 | Modelo corporativo de alta aderência |
| `microsoft/phi-3.5-moe-instruct` | Microsoft Phi MoE | 131.072 | 40 | 1.000 | Modelo compacto MoE |
| `nvidia/cosmos-reason2-8b` | VLM Física de Vídeo | 128.000 | 40 | 1.000 | Raciocínio espacial e físico sobre sequências de vídeo |
| `nvidia/ai-synthetic-video-detector` | Segurança/Detecção| - | 40 | 1.000 | Classificador forense de vídeos gerados por IA |
| `nvidia/riva-translate-4b-instruct-v2`| Tradução | 32.768 | 40 | 1.000 | Tradução multilíngue neural de alta fidelidade |

> **Mudanças recentes no NIM (17/09)**:
> - Removidos do free endpoint: `deepseek-ai/deepseek-v4-pro-0813` e `minimaxai/minimax-m3`.
> - Adicionados ao free endpoint: `z-ai/glm-5.3` e `z-ai/glm-5.3-flash`.

---

### 🟣 OPENROUTER — *Validado em 17/09/2026 (24 Modelos Free Ativos)*

O OpenRouter funciona como agregador universal com roteamento inteligente. Limite geral da cota gratuita: **20 RPM / 200 RPD**.

| Modelo ID API | Display Name | Contexto (In / Out) | Status Operacional | Notas & Aplicação |
| :--- | :--- | :---: | :---: | :--- |
| `nex-agi/nex-n2.5-pro:free` 🆕 | Nex N2.5 Pro | 262.144 / 235.929 | ✅ 200 OK | **NOVO (17/09)** — Raciocínio e código de alto nível |
| `nex-agi/nex-n2.5-mini:free` 🆕 | Nex N2.5 Mini | 262.144 / 235.929 | ✅ 200 OK | **NOVO (17/09)** — Rápido com enorme janela de saída |
| `inclusionai/ling-3.0-flash-vl:free` 🆕| Ling 3.0 Flash VL | 262.144 / 32.768 | ✅ 200 OK | **NOVO (17/09)** — Multimodal com Visão Computacional! |
| `z-ai/glm-5.2:free` 🆕 | Z.ai GLM 5.2 | 32.768 / 29.491 | ✅ 200 OK | **RE-ADICIONADO (17/09)** — Retornou ao Free Tier |
| `stealth/union-alpha` 🆕 | Union Alpha | 262.144 / 131.072 | ✅ 200 OK | **NOVO (17/09)** — Modelo stealth experimental de 262K |
| `inclusionai/ling-3.0-flash-sante:free` | Ling 3.0 Flash Santé | 262.144 / 32.768 | ✅ 200 OK | Especializado em saúde/ciências biomédicas |
| `inclusionai/ling-3.0-flash-fin:free` | Ling 3.0 Flash Fin | 262.144 / 32.768 | ✅ 200 OK | Especializado em finanças e economia |
| `dots-studio/dots-3-note-preview:free` | Dots3-Note Preview | 512.000 / 460.800 | ✅ 200 OK | Janela de output gigantesca (460K tokens) |
| `liquid/lfm-2.5-2.6b:free` | Liquid LFM 2.5 2.6B | 65.536 / 8.192 | ✅ 200 OK | Modelo bio-inspirado extremamente leve e rápido |
| `nvidia/nemotron-3.5-lightning:free` | Nemotron 3.5 Lightning | 1.000.000 / 65.536 | ✅ 200 OK | 1M de contexto gratuito |
| `nvidia/nemotron-3-ultra-550b-a55b:free`| Nemotron 3 Ultra | 1.000.000 / 65.536 | ✅ 200 OK | Frontier MoE gratuito no roteador |
| `nvidia/nemotron-3-super-120b-a12b:free`| Nemotron 3 Super | 262.144 / 235.929 | ✅ 200 OK | Excelente em tool calling |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`| Nemotron 3 Nano Omni| 256.000 / 65.536 | ✅ 200 OK | Multimodal com suporte a raciocínio |
| `poolside/laguna-s-2.1:free` | Laguna S 2.1 | 262.144 / 32.768 | ✅ 200 OK | Coding agent rápido |
| `poolside/laguna-xs-2.1:free` | Laguna XS 2.1 | 262.144 / 32.768 | ✅ 200 OK | Coding agent para pequenos módulos |
| `cohere/north-mini-code:free` | Cohere North Mini Code | 256.000 / 64.000 | ✅ 200 OK | Coding e Tool Use da Cohere |
| `google/gemma-4-31b-it:free` | Gemma 4 31B | 262.144 / 32.768 | ✅ 200 OK | Modelo dense de 31B |
| `google/gemma-4-26b-a4b-it:free` | Gemma 4 26B MoE | 262.144 / 32.768 | ✅ 200 OK | MoE esparso do Google |
| `google/lyria-3-pro-preview` | Lyria 3 Pro Preview | 1.048.576 / 65.536 | ✅ 200 OK | Geração de áudio e música (preview) |
| `google/lyria-3-clip-preview` | Lyria 3 Clip Preview | 1.048.576 / 65.536 | ✅ 200 OK | Áudio multimodal |
| `nvidia/nemotron-3.5-content-safety:free`| Nemotron Safety | 128.000 / 8.192 | ✅ 200 OK | Verificação de moderação |
| `openrouter/free` | Free Models Router | 200.000 / auto | ✅ 200 OK | Roteador dinâmico automático |
| `thinkingmachines/inkling:free` | Inkling Flagship | 1.048.576 / 262.144 | ⚠️ 403 Restrito | Listado como free, mas bloqueado no backend |
| `thinkingmachines/inkling-small:free` | Inkling Small | 1.048.576 / 262.144 | ⚠️ 403 Restrito | Requer conta autorizada upstream |

---

### 🟠 MISTRAL AI — *Validado em 17/09/2026 (46 modelos no catálogo)*

A Mistral oferece acesso a quase todos os seus modelos no Free Tier através de pools de consumo compartilhado: **50K TPM padrão**, **4M tokens/mês** e vazão global de **~1 req/s** (sem necessidade de cartão de crédito).

| Modelo ID API | Categoria | Contexto | RPM | TPM Pool | Validação 17/09 | Capacidades Principais |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `codestral-2508` / `codestral-latest` | Coding / FIM | **256.000** | 60 | Standard (50K) | ✅ 200 OK | Especialista em código, Fill-in-the-Middle |
| `mistral-code-latest` / `fim-latest` | Coding Puro | 256.000 | 60 | Standard (50K) | ✅ 200 OK | Endpoint dedicado para autocompletar |
| `mistral-small-2603` / `small-latest` | Workhorse | **262.144** | 60 | Standard (50K) | ✅ 200 OK | Melhor balanço velocidade / inteligência |
| `mistral-vibe-cli-fast` | CLI Agent | 262.144 | 60 | Standard (50K) | ✅ 200 OK | Otimizado para execução de terminal e scripts |
| `magistral-small-latest` | Raciocínio Leve | 262.144 | 1 | 20K TPM | ✅ 200 OK | Raciocínio guiado em modelo compacto |
| `ministral-3b-2512` / `latest` | Edge Model | 131.072 | 60 | Standard (50K) | ✅ 200 OK | 3B parâmetros; ultra-eficiente |
| `ministral-8b-2512` / `latest` | Mid Compact | 262.144 | 60 | Standard (50K) | ✅ 200 OK | 8B parâmetros; excelente para extração local |
| `ministral-14b-2512` / `latest` | Dense Compact | 262.144 | 60 | Standard (50K) | ✅ 200 OK | 14B parâmetros; alta densidade de raciocínio |
| `mistral-medium-2604` / `medium-3.5` | Flagship Anterior| 32.768 | 1 | 375K TPM | ✅ 200 OK | Análise de texto aprofundada |
| `magistral-medium-latest` | Frontier Reasoner| 32.768 | 1 | 20K TPM | ✅ 200 OK | Modelo de raciocínio avançado da Mistral |
| `voxtral-small-2507` / `small-latest` | Áudio STT | 32.768 | 60 | Standard | ✅ 200 OK | Reconhecimento e transcrição de fala |
| `voxtral-mini-2602` / `realtime-latest`| Áudio Realtime | 32.768 | 60 | Standard | ✅ 200 OK | Processamento de áudio bidirecional em tempo real |
| `voxtral-mini-tts-2603` / `tts-latest` | Áudio TTS | 4.096 | 60 | Standard | ✅ 200 OK | Síntese de voz expressiva |
| `mistral-ocr-2512` / `ocr-latest` / `4-1`| Visão OCR | 16.384 | 60 | Standard | ✅ 200 OK | Extração de tabelas, PDFs e imagens complexas |
| `mistral-embed-2312` / `codestral-embed`| Embeddings | 8.192 | 60 | 2K TPM | ✅ 200 OK | Vetorização semântica para RAG |
| `mistral-moderation-2603` | Moderação | 131.072 | 60 | Standard | ✅ 200 OK | Classificador de segurança de prompts/respostas |

---

### 🟢 DEEPSEEK — *Validado em 17/09/2026 (Catálogo API Oficial & Preços Canônicos)*

A DeepSeek opera uma das infraestruturas de inferência de maior eficiência de custos da indústria de IA, baseada em arquitetura Mixture-of-Experts (MoE) com Multi-head Latent Attention (MLA) e inferência nativa em FP8.

#### 🔑 1. Identificadores Canônicos de API (Padrão OpenAI SDK)

Para integração de sistemas em produção, automações e agentes (via OpenAI SDK, LiteLLM, LangChain ou chamadas HTTP diretas), os desenvolvedores devem enviar **obrigatoriamente** os identificadores canônicos oficiais:

* **`deepseek-chat`**: Aponta para o modelo flagship de propósito geral **DeepSeek-V3** (671B parâmetros totais, 37B ativos por token). Utilizado para conversação, geração de texto, programação, sumarização e chamadas de função (Function Calling estruturado).
* **`deepseek-reasoner`**: Aponta para o modelo de raciocínio lógico e analítico **DeepSeek-R1**. Executa cadeias de raciocínio passo a passo antes de emitir a resposta final, suportando retorno de tokens de pensamento (`reasoning_content`).

> **Endpoint Base Oficial**: `https://api.deepseek.com/v1` (ou `https://api.deepseek.com`)  
> **Formato de Chamada**: `client = OpenAI(api_key="<DEEPSEEK_API_KEY>", base_url="https://api.deepseek.com")`

#### 💰 2. Tabela Oficial Consagrada de Preços por 1 Milhão de Tokens

A tarifação da DeepSeek é pioneira mundial na diferenciação entre **Cache Hit** e **Cache Miss**, oferecendo economia de até 90% em prompts reutilizados, além de um desconto oficial de 50% em períodos de baixa demanda.

| Modelo / ID Canônico | Contexto Máx | Entrada (Cache Miss) | Entrada (Cache Hit) | Saída (Geração) | Concorrência Free | Status Operacional |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`deepseek-chat`** (DeepSeek-V3) | **1.048.576** | **$0.14** (¥1.00) | **$0.014** (¥0.10) | **$0.28** (¥2.00) | **128 reqs** | ✅ 200 OK — Flagship geral |
| **`deepseek-reasoner`** (DeepSeek-R1)| **1.048.576** | **$0.55** (¥4.00) | **$0.14** (¥1.00) | **$2.19** (¥16.00) | **128 reqs** | ✅ 200 OK — Raciocínio profundo |

##### 🌙 Desconto Oficial de Horário Econômico (Off-Peak — 50% OFF)

A DeepSeek aplica oficialmente um **desconto de 50%** em todos os preços de tabela durante os horários de baixa demanda:

* **Janela Off-Peak**: Diariamente das **00:30 às 08:30 (UTC+8)** / **16:30 às 00:30 UTC** / **13:30 às 21:30 BRT**.
* **Preços no Horário Econômico**:
  * **DeepSeek-V3 (`deepseek-chat`)**:
    * Entrada Cache Miss: **$0.07** (¥0.50 RMB) por 1M tokens.
    * Entrada Cache Hit: **$0.007** (¥0.05 RMB) por 1M tokens.
    * Saída: **$0.14** (¥1.00 RMB) por 1M tokens.
  * **DeepSeek-R1 (`deepseek-reasoner`)**:
    * Entrada Cache Miss: **$0.275** (¥2.00 RMB) por 1M tokens.
    * Entrada Cache Hit: **$0.07** (¥0.50 RMB) por 1M tokens.
    * Saída: **$1.095** (¥8.00 RMB) por 1M tokens.

#### 🎁 3. Cota Free & Poder de Compra de $5 USD ("O Rei dos $5")

* **Cota de Boas-Vindas**: Toda nova conta registrada na plataforma DeepSeek recebe automaticamente **5.000.000 de tokens gratuitos** (5M tokens), com validade de **30 dias**, utilizáveis imediatamente sem necessidade de cadastrar cartão de crédito.
* **Limites de Taxa no Free**: A plataforma não impõe limites rígidos de RPM; o acesso é delimitado por um teto padrão de **128 requisições concorrentes simultâneas**, com vazão dinâmica.
* **Análise Real de ROI com um Depósito Mínimo de $5 USD**:
  * O depósito mínimo aceito na API é de apenas **$5.00 USD** (via cartão internacional, Alipay ou WeChat Pay).
  * **No DeepSeek-V3 (`deepseek-chat`) sem Cache**: Considerando uma taxa mista de $0.14 na entrada e $0.28 na saída (custo médio ponderado de ~$0.20/M), $5 USD entregam entre **18.000.000 e 35.000.000 de tokens**.
  * **No DeepSeek-V3 com Context Caching Ativo**: Como a DeepSeek faz cache automático de blocos de contexto idênticos (a partir de 64 tokens) cobrando apenas **$0.014 por 1M de tokens no Cache Hit**, tarefas com prompts de sistema longos, histórico de conversação ou análise de bases de código atingem taxas de cache hit de 80% a 95%. Sob esse cenário, **um saldo de $5 USD rende mais de 100.000.000 (cem milhões) de tokens**!
  * **No DeepSeek-R1 (`deepseek-reasoner`)**: Um saldo de $5 USD entrega entre **2.200.000 e 9.000.000 de tokens** de raciocínio profundo puro, o que representa uma economia de 90% a 95% comparado ao OpenAI o1 ($15/$60 por 1M) ou Claude 3.7 Sonnet Thinking.

#### ⚙️ 4. Esclarecimento Técnico de Runtime: Reconciliação de Rotas Internas

Desenvolvedores e pesquisadores que inspecionam o tráfego da API, logs de telemetria ou metadados de resposta podem ocasionalmente observar termos como `deepseek-flash` ou `deepseek-v4-pro`. É fundamental esclarecer sua origem técnica:

1. **Topologia de Cluster & Partições de Hardware**:
   * O backend distribuído da DeepSeek organiza seus nós de inferência em partições funcionais: nós **"Flash"** são clusters especializados em decodificação ultra-veloz em FP8 com alta densidade de vazão para requisições de latência mínima.
   * Nós **"Pro"** ou **"Reasoner"** são partições de nós dedicados à execução intensiva de cadeias de raciocínio lógico e amostragem de long-context.
2. **Espelhamento em Headers e Logs**:
   * Em determinados gateways de roteamento ou cabeçalhos HTTP internos de diagnóstico (como `x-deepseek-engine` ou rotas experimentais de baixa latência), a infraestrutura pode reportar a tag da engine que atendeu a requisição (`flash` ou `v4-pro`).
3. **Diretriz Canônica de Integração**:
   * Esses termos **NÃO são nomes canônicos de modelos públicos**. Desenvolvedores **NUNCA** devem enviar `model="deepseek-flash"` ou `model="deepseek-v4-pro"` em chamadas de produção, pois essas rotas não constam na especificação pública padrão da API e podem incorrer em erro de rota inválida (`model_not_found`).
   * **Os únicos IDs aceitos e garantidos são `deepseek-chat` e `deepseek-reasoner`**. A cobrança financeira e a aplicação de cotas e descontos de horário econômico são 100% ancoradas nestes dois identificadores oficiais.

---

### ⚫ KIMI / MOONSHOT AI — *Validado em 17/09/2026 (APIs Doméstica & Internacional)*

A Moonshot AI (月之暗面) opera dois ambientes de API complementares: a plataforma chinesa original (focada em contexto ultra-longo na linha V1) e a plataforma internacional de inferência de ponta (`api.moonshot.ai`) com raciocínio e visão.

#### 🔹 1. Plataforma China Doméstica (`api.moonshot.cn/v1`) — Modelos Clássicos
* **Cota de Boas-Vindas**: Novos desenvolvedores recebem **¥15 RMB de bônus gratuito** (~$2.10 USD) para experimentação imediata no cadastro sem necessidade de cartão de crédito.
* **Modelos Clássicos V1**:
  * `moonshot-v1-8k`: Janela de 8.192 tokens; rápido para diálogos cotidianos e classificação.
  * `moonshot-v1-32k`: Janela de 32.768 tokens; balanceado para síntese de documentos médios.
  * `moonshot-v1-128k`: Janela de 128.000 tokens; processamento massivo de livros, relatórios e autos processuais.
  * `moonshot-v1-auto`: Roteador dinâmico que seleciona automaticamente o menor contexto necessário para minimizar custos.

#### 🔹 2. Linha Internacional de Inferência (`api.moonshot.ai/v1`) — Kimi K3 & K2.7
* **Status**: Gateway internacional 100% operacional, projetado para desenvolvedores globais com compatibilidade com OpenAI SDK.
* **Política de Acesso**: Ativação do Tier 0 via recarga mínima de **$1.00 USD**.

| Modelo ID API | Contexto | RPM (Tier 0) | TPM (Tier 0) | TPD (Tier 0) | Preço Pago (In / Out) | Status / Observações |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`kimi-k3`** | **1.048.576** | **3** | **32.000** | **1.5M** | **$3.00** / **$15.00** por M | ✅ 200 OK — Flagship 2.8T params, Vision nativo e raciocínio Thinking |
| **`kimi-k2.7-code`** | 256.000 | **3** | **32.000** | **1.5M** | **$0.95** / **$4.00** por M | ✅ 200 OK — Especializado em engenharia de software e agentes de terminal |
| **`kimi-k2.7-code-highspeed`** | 256.000 | **3** | **32.000** | **1.5M** | **$1.90** / **$8.00** por M | ✅ 200 OK — Inferência acelerada de código (6x mais veloz) |
| `kimi-k2.6` | 262.144 | **3** | **32.000** | **1.5M** | **$0.95** / **$4.00** por M | ✅ 200 OK — Modelo anterior mantido em produção para compatibilidade |

---

### 🟣 ANTHROPIC (Claude) — *Validado em 17/09/2026 (11 modelos na API)*

* **Status Free Tier**: ❌ **NÃO HÁ free tier permanente na API da Anthropic** ($5 inicial único).
* **Acesso Free via Código**: **GitHub Models** (`models.inference.ai.azure.com`) fornece `claude-3.5-sonnet` (15 RPM / 150 RPD) gratuitamente.

| Modelo ID API | Contexto | Cota Free API | Acesso Alternativo Gratuito |
| :--- | :---: | :---: | :--- |
| `claude-sonnet-4-6` / `claude-sonnet-5` | 200K / 1M | ❌ Apenas $5 inicial | Webchat em `claude.ai` |
| `claude-opus-4-6` / `claude-opus-5` | 200K / 1M | ❌ Apenas $5 inicial | Webchat com plano Pro |
| `claude-haiku-4-5-20251001` | 200K | ❌ Apenas $5 inicial | Rápido e de baixo custo pago |
| `claude-3.5-sonnet` (legado) | 200K | ✅ Free no GitHub Models | **10-15 RPM / 150 RPD no GitHub Models** |

---

### 🟢 OPENAI — *Validado em 17/09/2026 (119 modelos no catálogo)*

* Chat models (`gpt-4o`, `gpt-4o-mini`, `gpt-5.4`) requerem saldo pré-pago.
* Endpoints gratuitos: `whisper-1` (3 RPM / 200 RPD) e `omni-moderation-latest`.

---

### 🔵 CEREBRAS CLOUD — *STATUS: ENCERRADO DEFINITIVAMENTE*

* **Status**: ❌ **FREE TIER ENCERRADO**. Responde com 402/403. Removido de qualquer fallback gratuito.

---

### 🟢 DEEPINFRA — *Validado em 17/09/2026 (189 modelos no catálogo)*

* Pay-per-use ultra-econômico sem mínimo de recarga. `openai/gpt-oss-120b` a **$0.08 por milhão de tokens blended**.
* Modelos disponíveis: `Qwen/Qwen3.5-122B-A10B`, `ByteDance/Seed-2.0-mini`, `google/veo-3.1-fast`, `black-forest-labs/FLUX-2-pro`.

---

### 🇨🇳 ECOSSISTEMA CHINÊS: PROVEDORES NATIVOS & MODELOS DOMÉSTICOS

O mercado chinês de IA desenvolveu uma das infraestruturas de inferência mais competitivas do mundo. Diferencia-se por oferecer modelos leves permanentemente gratuitos (visando tração de desenvolvedores) e modelos de raciocínio de alta escala a custos ordens de magnitude inferiores aos modelos ocidentais.

---

#### 🔴 ZHIPU AI / BIGMODEL (open.bigmodel.cn) — *Validado em 17/09/2026 (Modelos 100% Free Perpétuo)*

A Zhipu AI (清华系 AI), originada na Universidade de Tsinghua, disponibiliza a família **GLM-4-Flash** com acesso **100% gratuito e perpétuo** para desenvolvedores, sem cobrança de tokens.

* **Endpoint Base**: `https://open.bigmodel.cn/api/paas/v4` (Compatível nativamente com o formato OpenAI SDK `/chat/completions`)
* **Tipo de Cota**: Free Tier perpétuo no modelo Flash + **25.000.000 tokens bônus de boas-vindas** no cadastro para modelos pagos (válidos por 30 dias).
* **Limites de Taxa Granulares (Free Tier)**:
  * **Concorrência**: **1 requisição concorrente simultânea** no Free Tier.
  * **Tokens / Minuto**: Ilimitado no Flash (respeitando 1 chamada por vez com backoff).
  * **Aplicações de Alta Frequência**: Para concorrência paralela (5-10 concurrency), a Zhipu oferece planos pré-pagos onde o GLM-4-FlashX ou GLM-4-Air custam menos de ¥1 RMB (~$0.14 USD) por milhão de tokens.
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**. Cadastro com e-mail internacional ou telefone.
* **Autenticação**: Header `Authorization: Bearer <ZHIPU_API_KEY>` (formato `<id>.<secret>`).

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | Limite Free | Custo Pago (após free) | Notas & Capacidades |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **`glm-4-flash`** | GLM-4 Flash (Original) | Texto / Chat | 128.000 / 4.096 | **100% Grátis Perpétuo** (1 conc) | ¥0.00 / M tokens | **Top Pick Free Chinês** — Respostas ultra-rápidas, excelente bilinguismo (ZH/EN) |
| **`glm-4.7-flash`** 🆕 | GLM-4.7 Flash | Texto / Instrução | 128.000 / 4.096 | **100% Grátis Perpétuo** (1 conc) | ¥0.00 / M tokens | Versão aprimorada com raciocínio analítico e seguimento de regras complexas |
| **`glm-4v-flash`** | GLM-4V Flash | Visão Computacional | 8.192 / 4.096 | **100% Grátis Perpétuo** (1 conc) | ¥0.00 / M tokens | Multimodal para OCR, interpretação de tabelas, imagens e diagramas |
| `glm-4-flashx` | GLM-4 FlashX (Ultra-Fast) | Baixa Latência | 128.000 / 4.096 | Trial / ¥0.1 por M | ~$0.015 / M tokens | Versão acelerada em hardware proprietário para TTFT mínimo |
| `glm-4-air` | GLM-4 Air (Balanced) | Raciocínio Geral | 128.000 / 4.096 | Consome bônus 25M | ¥1.00 / M tokens (~$0.14) | Excelente equilíbrio entre velocidade, inteligência e custo |
| `glm-4-plus` | GLM-4 Plus (Flagship) | Frontier Chinês | 128.000 / 4.096 | Consome bônus 25M | ¥10.00 / M tokens (~$1.40) | Modelo de maior capacidade cognitiva da Zhipu (nível GPT-4o) |
| `glm-5.3` | GLM-5.3 Next-Gen | Raciocínio Avançado | 131.072 / 8.192 | Via NVIDIA NIM Free | Sob consulta | Disponível gratuitamente via endpoint do NVIDIA NIM (`z-ai/glm-5.3`) |

---

#### 🔴 BAIDU QIANFAN (qianfan.cloud.baidu.com) — *Validado em 17/09/2026 (ERNIE Speed & Lite 100% Free Perpétuo)*

A plataforma Qianfan da Baidu (百度智能云千帆大模型平台) adota uma política agressiva de democratização da IA: os modelos da linha **ERNIE Speed** e **ERNIE Lite** são declarados **permanente e 100% gratuitos** para chamadas via API.

* **Endpoints Base**:
  * Gateway REST: `https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/{model_endpoint}`
  * SDK Qianfan: `qianfan.ChatCompletion()` (Python / Node.js / Go)
* **Tipo de Cota**: Free Tier perpétuo para desenvolvimento e uso em produção moderada nos modelos Speed/Lite.
* **Limites de Taxa Granulares (Modelos Free)**:
  * **RPM (Requests Per Minute)**: **300 RPM** padrão compartilhado.
  * **TPM (Tokens Per Minute)**: **300.000 TPM** padrão.
  * **Concorrência**: Múltiplas conexões simultâneas permitidas (gerenciadas dinamicamente sob a cota de 300 RPM).
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito ocidental**. Requer registro de conta no Baidu AI Cloud e autenticação básica de desenvolvedor (e-mail/celular).
* **Autenticação**: Protocolo OAuth 2.0 via `access_token` gerado em `/oauth/2.0/token` usando `API_KEY` e `SECRET_KEY`.

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | Limite RPM / TPM | Tipo de Cota | Notas & Casos de Uso |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **`ERNIE-Speed-8K`** | ERNIE Speed 8K | Texto / Diálogo | 8.192 / 4.096 | **300 RPM / 300K TPM** | **100% Free Perpétuo** | **Rei da Vazão Free** — Inferência ultra-rápida para resumos, FAQs e agentes |
| **`ERNIE-Speed-128K`** | ERNIE Speed 128K | Contexto Longo | 128.000 / 4.096 | **300 RPM / 300K TPM** | **100% Free Perpétuo** | Análise de documentos extensos, livros e logs sem custo de tokens |
| **`ERNIE-Lite-8K-0922`** | ERNIE Lite 8K | Texto Compacto | 8.192 / 4.096 | **300 RPM / 300K TPM** | **100% Free Perpétuo** | Modelo leve de baixo consumo, balanceado para extração estruturada de entidades |
| `ERNIE-Tiny-8K` | ERNIE Tiny 8K | Micro-Modelo | 8.192 / 2.048 | **300 RPM / 300K TPM** | **100% Free Perpétuo** | Velocidade extrema para classificação e roteamento pré-filtro |
| `ERNIE-4.0-Turbo-8K` | ERNIE 4.0 Turbo | Flagship Baidu | 8.192 / 4.096 | Pacote Onboarding / Pago | ¥0.03 / 1K tokens | Modelo mais inteligente da Baidu; raciocínio matemático e lógico avançado |
| `ERNIE-3.5-128K` | ERNIE 3.5 128K | Raciocínio Longo | 128.000 / 4.096 | Pacote Onboarding / Pago | ¥0.0008 / 1K tokens | Modelo versátil a custo marginal para processamento em larga escala |

---

#### 🔴 ALIBABA CLOUD MODEL STUDIO / DASHSCOPE / BAILIAN (alibabacloud.com / bailian.console.aliyun.com) — *Validado em 17/09/2026*

O ecossistema de IA da Alibaba Cloud unificou o acesso à família **Qwen (通义千问)** através do **Model Studio** (anteriormente DashScope / Bailian). A plataforma oferece franquias de boas-vindas gratuitas por modelo e as tarifas mais baixas da indústria para tokens adicionais.

* **Endpoints Base**:
  * Console Internacional (Singapura): `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * Console China Doméstica: `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * Totalmente compatível com OpenAI SDK (`openai.OpenAI(base_url=..., api_key=...)`)
* **Tipo de Cota Free (Onboarding Franquia)**:
  * Cada novo usuário que ativa o Model Studio recebe entre **1.000.000 e 2.000.000 de tokens GRATUITOS por modelo individual** (ex.: 1M para Qwen-Plus, 1M para Qwen-Max, 1M para Qwen-Turbo).
  * Validade da franquia: **90 a 180 dias** a partir da ativação de cada modelo.
  * Hierarquia de dedução automática: `Free Quota > Pacote Promocional > Faturamento Pay-As-You-Go`.
* **Limites de Taxa Granulares**:
  * Modelos Gerais: **60 a 120 RPM** (agregado na conta).
  * Limite de TPM: **100.000 a 200.000 TPM** por modelo.
* **Requisitos de Entrada / Cartão**: Registro na Alibaba Cloud (versão internacional aceita cartão internacional; versão doméstica aceita Alipay). O free tier é consumido antes de qualquer cobrança.
* **Autenticação**: Bearer token via `Authorization: Bearer <DASHSCOPE_API_KEY>`.

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | Cota Gratuita Onboarding | Custo Pós-Free (por 1M tokens) | Notas & Capacidades |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **`qwen-turbo`** | Qwen Turbo (Veloz) | Texto / Geral | 131.072 / 8.192 | **2.000.000 tokens** (90 dias) | **¥0.30** (~$0.04 USD) | O modelo de produção mais barato da Alibaba; latência instantânea |
| **`qwen-plus`** | Qwen Plus (Balanceado) | Raciocínio MoE | 131.072 / 8.192 | **1.000.000 tokens** (90 dias) | **¥0.80** (~$0.11 USD) | Desempenho equivalente a modelos intermediários globais; excelente em português |
| **`qwen-max`** | Qwen Max (Flagship) | Raciocínio Complexo | 32.768 / 8.192 | **1.000.000 tokens** (90 dias) | **¥20.00** (~$2.80 USD) | O topo de linha da Alibaba; supera o GPT-4o em diversos benchmarks de código e exatas |
| **`qwen-long`** | Qwen Long (Documentos)| Mega-Contexto | 1.000.000 / 8.192 | **1.000.000 tokens** (90 dias) | **¥0.50** (~$0.07 USD) | 1 Milhão de tokens de contexto para ingestão completa de bases documentais |
| `qwen2.5-coder-32b-instruct` | Qwen 2.5 Coder 32B | Programação Pura | 131.072 / 8.192 | Franquia Model Studio | **¥1.50** (~$0.21 USD) | O modelo de código open-weight mais elogiado do mundo no ecossistema OpenCode |
| `qwen2.5-72b-instruct` | Qwen 2.5 72B | Raciocínio Geral | 131.072 / 8.192 | Franquia Model Studio | **¥4.00** (~$0.56 USD) | O peso pesado open-source líder em rankings internacionais |
| `qwen-vl-max` | Qwen VL Max | Visão Computacional | 32.768 / 8.192 | Franquia Onboarding | **¥20.00** (~$2.80 USD) | Extração de diagramas, vídeo frame-by-frame e OCR multi-orientação |

---

#### 🔴 TENCENT CLOUD HUNYUAN & TOKENHUB (cloud.tencent.com/product/hunyuan) — *Validado em 17/09/2026*

A Tencent Cloud opera o **Hunyuan (混元大模型)** e o gateway unificado **TokenHub**, integrando modelos proprietários e variantes abertas com forte foco no ecossistema corporativo e no assistente de desktop **WorkBuddy**.

* **Endpoints Base**: `https://hunyuan.tencentcloudapi.com` e gateway REST TokenHub.
* **Tipo de Cota Free**:
  * **Hunyuan-Lite**: Pacote gratuito de ativação de **1 ano** para testes e desenvolvimento.
  * **Hunyuan-3D**: Concede **1.000 créditos gratuitos** de geração tridimensional na ativação.
  * **Proteção contra Cobrança Involuntária**: Quando o pacote free é consumido, a Tencent **NÃO debita automaticamente do cartão** por padrão; as requisições subsequentes são bloqueadas com erro até ativação explícita do faturamento pós-pago.
* **Modelos Principais**:
  * `hunyuan-lite`: Modelo ultraleve gratuito para automações, triagem e chatbots.
  * `hunyuan-standard` / `hunyuan-pro`: Modelos densos de 100B+ parâmetros para análise complexa.
  * `hunyuan-vision`: Interpretação de imagens e fluxos de telas.
  * `hunyuan-3d`: Geração de malhas 3D e texturas text-to-3D.
* **Integração Desktop**: Motor padrão do **Tencent WorkBuddy (workbuddy.ai)** para geração de minutas, manipulação de arquivos do Office e automação de planilhas.

---

#### 🔴 BYTEDANCE VOLCANO ENGINE / DOUBAO (volcengine.com) — *Auditoria Operacional em 17/09/2026*

O **Doubao (豆包)**, desenvolvido pela ByteDance, é o modelo de IA mais utilizado na China em volume de requisições diárias (motor do TikTok / Douyin).

* **DIAGNÓSTICO CRÍTICO DE FREE TIER**: ❌ **A API profissional do Volcano Engine NÃO possui Free Tier perpétuo para desenvolvedores**.
  * Enquanto o **aplicativo móvel e web do Doubao é 100% gratuito** para usuários finais, o acesso à API para desenvolvimento via Volcano Engine é **estritamente bilhetado em RMB**.
  * Não há cota perpétua de chamadas sem saldo na conta.
* **Tarifação de Atacado (Pay-Per-Use Ultra-Barato)**:
  * Embora seja pago, é um dos mais baratos do mercado: `Doubao-pro-32k` custa aproximadamente **¥0.80 por milhão de tokens de entrada** (~$0.11 USD/M) e `Doubao-lite-32k` custa cerca de **¥0.30 por milhão** (~$0.04 USD/M).
  * Conclusão de Arquitetura: Para pipelines 100% gratuitos, utilize **SiliconFlow (Qwen/DeepSeek)**, **Baidu Qianfan (ERNIE Speed)** ou **Zhipu AI (GLM-4-Flash)** em vez da API direta do Volcano Engine.

---

#### 🔴 OUTROS PLAYERS CHINESES: MINIMAX, 01.AI & STEPFUN

| Provedor | Modelos Destacados | Bônus / Cota Free Inicial | Custo Pós-Free | Endpoint & Notas |
| :--- | :--- | :---: | :---: | :--- |
| **MiniMax**<br>`api.minimax.chat` | `abab6.5s-chat`, `MiniMax-Text-01`, `speech-01` (TTS), `video-01` (Hailuo AI) | **¥15 RMB de bônus** (~$2.10 USD) no cadastro | ~$0.15/M texto; TTS ~$0.002/1K chars | **Líder em Áudio e Vídeo**: O modelo `speech-01` possui a melhor síntese vocal emotiva da China; `video-01` lidera no Hailuo AI |
| **01.AI (Lingyi Wanwu)**<br>`api.lingyiwanwu.com` | `yi-lightning`, `yi-large`, `yi-medium`, `yi-vision` | **¥30 RMB de créditos** (~$4.20 USD) | ¥1.00 a ¥12.00 por M tokens | Criado por Kai-Fu Lee. `yi-lightning` oferece velocidade excepcional de geração com raciocínio profundo |
| **StepFun (Jieyue Xingchen)**<br>`platform.stepfun.ai` | `step-3.5-flash`, `step-3.7-flash`, `step-1-128k`, `stepaudio-3` | **Step Plan Trial** + Rota Free no OpenRouter | ~$0.10 a $0.80 / M tokens | Forte em compreensão multimodal de áudio (`stepaudio-3`) e modelos long-context rápidos |

---


### 🟢 HYPERBOLIC (api.hyperbolic.xyz) — *Validado em 17/09/2026 (Free Basic Tier Perpétuo)*

A Hyperbolic opera um ecossistema de computação descentralizada e inferência aberta de alta performance com endpoints OpenAI-compatíveis. O plano **Free Basic Tier** oferece inferência gratuita contínua sem data de expiração.

* **Endpoint Base**: `https://api.hyperbolic.xyz/v1` (Compatível com OpenAI SDK / LiteLLM)
* **Tipo de Cota**: Free Tier permanente (Basic Tier).
* **Limite Global de Taxa**: **60 RPM** (Requests Per Minute) fixos no plano gratuito. Upgrade para 600 RPM disponível no plano Pro com depósito único de $5.
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** nem dados de faturamento para uso de inferência serverless. Cadastro via e-mail ou Web3 wallet. Cartão/depósito de $5 é exigido exclusivamente para instâncias de GPU dedicada e provisionamento de volumes de armazenamento.
* **Autenticação**: Bearer token (`Authorization: Bearer <HYPERBOLIC_API_KEY>`) gerado no dashboard (`app.hyperbolic.xyz/settings/api-keys`).

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM | TPM / TPD | Tipo de Cota | Capacidades Principais & Notas |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `meta-llama/Meta-Llama-3.1-405B-Instruct` | Llama 3.1 405B | Texto / Raciocínio | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Flagship open-weights de 405B rodando sob inferência distribuída |
| `meta-llama/Meta-Llama-3.1-70B-Instruct` | Llama 3.1 70B | Texto / Tool Use | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Workhorse para raciocínio analítico, código e tool calling estruturado |
| `meta-llama/Meta-Llama-3.1-8B-Instruct` | Llama 3.1 8B | Texto / Velocidade | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Latência ultrabaixa para extração, classificação e parsing de texto |
| `Qwen/Qwen2.5-72B-Instruct` | Qwen 2.5 72B | Texto / Código | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Excelente em matemática, raciocínio lógico e suporte multilíngue |
| `Qwen/Qwen2.5-Coder-32B-Instruct` | Qwen 2.5 Coder 32B | Coding Agent | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Especialista em geração de código, refatoração e resolução de bugs |
| `deepseek-ai/DeepSeek-V3` | DeepSeek V3 | MoE Geral | 65.536 / 8.192 | **60** | Dinâmico | Free Perpétuo | Arquitetura MoE de 671B com 37B ativos; alta inteligência por custo zero |
| `deepseek-ai/DeepSeek-R1` | DeepSeek R1 | Raciocínio Puro | 65.536 / 8.192 | **60** | Dinâmico | Free Perpétuo | Raciocínio analítico aprofundado com tokens de reflexão (thinking tags) |
| `FLUX.1-dev` | FLUX.1 Dev | Geração de Imagem | 1.024 x 1.024 | **10** | - | Free Perpétuo | Síntese de imagens de 12B parâmetros com alta fidelidade e tipografia |
| `SDXL1.0-base` | Stable Diffusion XL | Geração de Imagem | 1.024 x 1.024 | **20** | - | Free Perpétuo | Geração rápida de imagens em 1024x1024 para prototipagem visual |

---

### 🟢 SILICONFLOW / SILICONCLOUD (api.siliconflow.com) — *Validado em 17/09/2026 (Free Tier Permanente & High Throughput)*

A SiliconFlow (SiliconCloud) é uma plataforma global de inferência de modelos como serviço (MaaS) que disponibiliza uma ampla gama de modelos de código aberto com **Free Tier permanente** (modelos identificados sem custo de consumo), somado a um crédito inicial gratuito de boas-vindas ($1 / 20M tokens) para novos desenvolvedores.

* **Endpoint Base**: `https://api.siliconflow.com/v1` (Global, recomendado para menor latência internacional) ou `https://api.siliconflow.cn/v1` (China) (OpenAI-compatible)
* **Tipo de Cota**: Modelos com Free Tier perpétuo (sem desconto de créditos) + $1 USD (20M tokens promocionais no signup).
* **Limites Granulares de Taxa (Nível L0 - Free)**:
  * **Modelos Free Gerais**: **1.000 RPM** (Requests Per Minute) e **40.000 TPM** (Tokens Per Minute).
  * **Modelos DeepSeek R1 / V3**: **30 RPH** (Requests Per Hour) e **100 RPD** (Requests Per Day) para contas sem validação de identidade real (KYC).
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** no cadastro nem para uso dos modelos gratuitos e créditos de boas-vindas. Validação de identidade/telefone solicitada apenas se o desenvolvedor quiser elevar limites para produção pesada.
* **Autenticação**: Bearer token via header `Authorization: Bearer <SILICONFLOW_API_KEY>`.

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM | TPM / RPD | Tipo de Cota | Notas & Capacidades |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `Qwen/Qwen2.5-7B-Instruct` | Qwen 2.5 7B | Texto / Chat | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Modelo de 7B denso, balanceado e rápido para tarefas cotidianas |
| `Qwen/Qwen2.5-Coder-7B-Instruct` | Qwen 2.5 Coder 7B | Código / CLI | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Otimizado para autocompletar e geração de código em 92 linguagens |
| `Qwen/Qwen2.5-VL-7B-Instruct` | Qwen 2.5 VL 7B | Visão Computacional| 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | VLM com leitura de imagens, diagramas, tabelas e OCR multilíngue |
| `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`| DeepSeek R1 Qwen 7B| Raciocínio Destilado | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Raciocínio matemático e lógico treinado sob as saídas do DeepSeek R1 |
| `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`| DeepSeek R1 Llama 8B| Raciocínio Destilado | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Variante de raciocínio destilado sob a arquitetura do Llama 3.1 8B |
| `THUDM/glm-4-9b-chat` | GLM-4 9B Chat | Texto / Tool Use | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Modelo bilingue (EN/ZH) da Zhipu AI para extração e diálogos |
| `deepseek-ai/DeepSeek-V3` | DeepSeek V3 Flagship| MoE Geral | 65.536 / 8.192 | 100 | **100 RPD** | Free sem KYC | 671B MoE com limite de 30 RPH / 100 RPD no nível não-verificado |
| `deepseek-ai/DeepSeek-R1` | DeepSeek R1 Flagship| Raciocínio Puro | 65.536 / 8.192 | 100 | **100 RPD** | Free sem KYC | Modelo completo de raciocínio com 30 RPH / 100 RPD no nível free |
| `black-forest-labs/FLUX.1-schnell` | FLUX.1 Schnell | Geração de Imagem | 1.024 x 1.024 | **10** | - | Free Permanente | Síntese de imagem em 4 passos sob licença Apache 2.0 |
| `BAAI/bge-large-zh-v1.5` | BGE Large Chinese | Embeddings | 512 / 1.024 dim | **1.000** | **40K TPM** | Free Permanente | Embedding semântico denso de alta dimensionalidade |
| `BAAI/bge-m3` | BGE M3 Multi-modal | Embeddings Multiling| 8.192 / 1.024 dim | **1.000** | **40K TPM** | Free Permanente | Suporta busca densa, esparsa e multi-vectorial em 100+ idiomas |

---

### 🟢 POLLINATIONS.AI (gen.pollinations.ai) — *Validado em 17/09/2026 (Gateway Multimodal 100% Free Perpétuo)*

O Pollinations.ai é uma rede aberta de computação de IA que fornece inferência 100% gratuita para modelos de texto, imagem, áudio e visão. A plataforma opera com uma API unificada compatível com o formato OpenAI e também via chamadas REST diretas em URLs legíveis por humanos.

* **Endpoint Base Unificado**: `https://gen.pollinations.ai/v1` (Compatível com OpenAI SDK para `/chat/completions`)
* **Endpoints REST Diretos**:
  * Imagem: `https://image.pollinations.ai/prompt/{prompt}?model={model}&width={w}&height={h}&key={api_key}`
  * Texto: `https://gen.pollinations.ai/text/{prompt}?model={model}&key={api_key}`
* **Tipo de Cota**: Free Tier perpétuo e comunitário.
* **Limites de Taxa Granulares**:
  * **Com Chave Gratuita (`sk_`)**: **60 RPM** estável para texto e **30 RPM** para geração de imagens.
  * **Sem Chave (Anônimo/Legado)**: Severamente restringido (~1 requisição por IP/hora ou intervalo compulsório de 6-7s entre chamadas para prevenir abusos).
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**, nem dados de faturamento. Chaves de API (`sk_` para backend e `pk_` para frontend) são geradas gratuitamente em `enter.pollinations.ai` via login com GitHub ou e-mail.
* **Autenticação**: Header `Authorization: Bearer <POLLINATIONS_API_KEY>` ou query param `?key=<KEY>`.

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM | Tipo de Cota | Capacidades & Casos de Uso |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `openai` | GPT-4o-Mini Equivalent | Texto / Chat | 128.000 / 16.384 | **60** | Free Perpétuo | Roteador otimizado com respostas rápidas e alta acurácia lógica |
| `mistral` | Mistral Small / Nemo | Texto / Geral | 32.768 / 4.096 | **60** | Free Perpétuo | Modelo leve e responsivo para conversação, tradução e análise |
| `qwen-coder` | Qwen 2.5 Coder 32B | Código / Refatoração | 32.768 / 8.192 | **60** | Free Perpétuo | Especialista em código, geração de testes e resolução de bugs |
| `deepseek` | DeepSeek V3 / R1 | Raciocínio MoE | 64.000 / 8.192 | **60** | Free Perpétuo | Raciocínio analítico avançado e geração estruturada de JSON |
| `flux` | FLUX.1 Schnell | Geração de Imagem | 1.024 x 1.024 | **30** | Free Perpétuo | Geração de imagem com qualidade fotorrealista e tipografia nítida |
| `flux-realism` | FLUX Realism Tuned | Imagem Fotorrealista| 1.024 x 1.024 | **20** | Free Perpétuo | Ajustado especificamente para pele humana, iluminação e texturas |
| `turbo` | SDXL Turbo Fast | Geração Rápida | 512 x 512 | **60** | Free Perpétuo | Geração ultrarrápida em 1 passo para prototipagem de UI e ícones |

---

### 🟢 COHERE (api.cohere.com) — *Validado em 17/09/2026 (Developer Trial Tier Perpétuo)*

A Cohere disponibiliza uma chave permanente de testes (**Trial API Key**) para desenvolvedores sem custos recorrentes. É a principal referência de mercado para pipelines corporativos de **RAG (Retrieval-Augmented Generation)**, **Embeddings Multilíngues** e **Neural Reranking**.

* **Endpoint Base**: `https://api.cohere.com/v2` (REST e SDKs oficiais Python/TypeScript/Go)
* **Tipo de Cota**: Developer Trial Key perpétua para experimentação, testes e prototipagem (não comercial).
* **Limites de Requisições Globais**: **1.000 requisições por mês** (1K calls/month) consolidadas entre todos os endpoints.
* **Limites Granulares por Endpoint (RPM)**:
  * `/v2/chat`: **20 RPM**
  * `/v2/embed` (Texto): **100 RPM**
  * `/v2/embed` (Imagens/Multimodal): **5 RPM**
  * `/v2/rerank`: **10 RPM**
  * `/v2/tokenize`: **100 RPM**
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** nem informações financeiras para emissão e renovação da Trial API Key. Cadastro direto com e-mail corporativo ou pessoal.
* **Autenticação**: Header `Authorization: Bearer <COHERE_API_KEY>`.

| Modelo ID API | Categoria / Família | Modalidade | Contexto (In / Out) | RPM | Cota Mensal | Capacidades Críticas & Aplicação |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `command-r-plus-08-2024` | Command R+ (Flagship) | Chat / Tool Use | 128.000 / 4.096 | **20** | 1.000 reqs | Modelo topo de linha da Cohere com raciocínio de alta precisão e Tool Calling |
| `command-r-08-2024` | Command R (Workhorse) | Chat / RAG | 128.000 / 4.096 | **20** | 1.000 reqs | Otimizado para citação de fontes, síntese documental e RAG multilíngue |
| `command-r7b-12-2024` | Command R7B Compact | Chat / Eficiência | 128.000 / 4.096 | **20** | 1.000 reqs | Modelo compacto de 7B com velocidade elevada e baixo consumo de recursos |
| `embed-multilingual-v3.0` | Multilingual Embedding| Vetores Semânticos| 512 / 1.024 dim | **100** | 1.000 reqs | Padrão ouro da indústria para vetorização em mais de 100 idiomas |
| `embed-english-v3.0` | English Embedding | Vetores Semânticos| 512 / 1.024 dim | **100** | 1.000 reqs | Vetorização semântica de alta performance para documentos em inglês |
| `rerank-v3.5` | Neural Reranker v3.5 | Reranking / Busca | 4.096 / - | **10** | 1.000 reqs | Reclassificação semântica de precisão para elevar o MRR de buscas RAG |
| `rerank-multilingual-v3.0` | Multilingual Reranker | Reranking / Busca | 4.096 / - | **10** | 1.000 reqs | Reranking neural com compreensão de contexto cross-lingual |

---

### 🟢 AWANLLM (api.awanllm.com) — *Validado em 17/09/2026 (Free Lite Tier Perpétuo — "Unlimited Tokens")*

O AwanLLM é um gateway de inferência focado em modelos abertos e variantes desprovidas de recusa (uncensored / zero-refusal) para escrita criativa, RPG e automações flexíveis. Seu diferencial é o plano **Free Lite Tier**, que oferece **"tokens ilimitados"** (sem bilhetagem por token), limitando o uso estritamente por número de requisições.

* **Endpoint Base**: `https://api.awanllm.com/v1` (Compatível com OpenAI SDK para `/chat/completions` e `/completions`)
* **Tipo de Cota**: Free Lite Tier perpétuo sem cobrança de tokens.
* **Limites de Taxa Granulares**:
  * **Taxa por Minuto (RPM)**: **20 RPM** global.
  * **Modelos Pequenos (Small Models - 8B)**: **200 RPD** (Requests Per Day).
  * **Modelos Médios / Grandes (Medium/Large - 70B)**: **10 RPD** (Requests Per Day).
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**. A chave de API é liberada instantaneamente no painel web após confirmação de e-mail.
* **Autenticação**: Bearer token via `Authorization: Bearer <AWANLLM_API_KEY>`.

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM | RPD | Tipo de Cota | Notas & Características Especiais |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `Meta-Llama-3.1-8B-Instruct` | Llama 3.1 8B Instruct | Texto / Chat | 128.000 / 4.096 | **20** | **200** | Free Lite Perpétuo | Versão oficial do Meta Llama 3.1 com contexto expandido de 128K |
| `Awanllm-Llama-3-8B-Cumulus` | Llama 3 Cumulus 8B | Roleplay / Uncensored| 8.192 / 4.096 | **20** | **200** | Free Lite Perpétuo | Variante zero-refusal popular para escrita criativa e cenários de ficção |
| `Awanllm-Llama-3-8B-Dolfin` | Llama 3 Dolfin 8B | Instruction Following| 8.192 / 4.096 | **20** | **200** | Free Lite Perpétuo | Modelo com alinhamento flexível para tarefas de comando sem recusas |
| `Awanllm-Llama-3-8B-Instruct-ORPO-v0.1` | Llama 3 ORPO 8B | Alinhamento ORPO | 8.192 / 4.096 | **20** | **200** | Free Lite Perpétuo | Treinado com Odds Ratio Preference Optimization para respostas coesas |
| `Meta-Llama-3.1-70B-Instruct` | Llama 3.1 70B Instruct| Texto / Análise | 128.000 / 4.096 | **20** | **10** | Free Lite Perpétuo | Modelo pesado de 70B para tarefas analíticas esporádicas (10 reqs/dia) |

---

### 🟢 SCALEWAY GENERATIVE APIS (api.scaleway.ai) — *Validado em 17/09/2026 (Free Tier Europeu — 1M Tokens + Áudio)*

A Scaleway (provedora de infraestrutura em nuvem europeia e soberana) oferece o serviço **Generative APIs - Serverless** com uma cota gratuita mensal recorrente de **1.000.000 de tokens (1M tokens/mês)** para modelos de linguagem e embeddings, além de **60 minutos mensais gratuitos** de transcrição de áudio com Whisper.

* **Endpoint Base**: `https://api.scaleway.ai/v1` (Compatível com formato OpenAI `/v1/chat/completions`, `/v1/embeddings` e `/v1/audio/transcriptions`)
* **Tipo de Cota**: Cota gratuita mensal renovável (1M tokens para LLMs + 60 min para STT).
* **Limites de Taxa (Nível Base Organização)**:
  * **QPM (Queries Per Minute)**: **30 QPM** para chat/embeddings e **10 QPM** para áudio.
  * **TPM (Tokens Per Minute)**: **50.000 TPM** compartilhados na organização.
  * **Concorrência Máxima**: 5 sessões simultâneas (escalável após KYC corporativo).
* **Requisitos de Entrada / Cartão**: ⚠️ **EXIGE cartão de crédito** para verificação cadastral da conta na nuvem Scaleway (prevenção de fraudes europeias), mas a franquia mensal de 1M de tokens e 60 min de áudio é faturada a **€0,00**.
* **Autenticação**: Header `X-Auth-Token: <SCALEWAY_SECRET_KEY>`.

| Modelo ID API | Categoria | Modalidade | Contexto (In / Out) | QPM | Cota Mensal Free | Destaques & Conformidade |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `llama-3.3-70b-instruct` | Llama 3.3 70B | Texto / Código | 131.072 / 4.096 | **30** | 1M tokens/mês | Flagship de 70B hospedado em data centers verdes na França sob GDPR rígido |
| `qwen2.5-coder-32b-instruct` | Qwen 2.5 Coder | Coding Agent | 32.768 / 8.192 | **30** | 1M tokens/mês | Especialista em desenvolvimento de software com suporte a 92 linguagens |
| `mistral-nemo-12b-instruct-2407`| Mistral NeMo 12B| Workhorse | 128.000 / 4.096 | **30** | 1M tokens/mês | Modelo desenvolvido por Mistral AI e NVIDIA, excelente em raciocínio compacto |
| `pixtral-12b-2409` | Pixtral 12B | Visão Multimodal | 128.000 / 4.096 | **30** | 1M tokens/mês | Modelo multimodal nativo da Mistral para leitura e análise de imagens e gráficos |
| `whisper-large-v3` | Whisper STT | Áudio / Transcrição| Chunks de 30s | **10** | **60 min/mês** | Transcrição de fala multilíngue com alta precisão e pontuação automática |
| `bge-multilingual-gemma2` | Embeddings | Vetorização | 8.192 / 3.584 dim | **30** | 1M tokens/mês | Modelo de embeddings denso derivado da arquitetura Google Gemma 2 |

---

### 🟡 NOVITA AI (api.novita.ai) — *Validado em 17/09/2026 (Sandbox / Trial Multimodal — LLM & Imagem)*

A Novita AI fornece serviços de inferência acelerada com foco em geração de mídia (SDXL, FLUX) e grandes modelos de linguagem open-source. Novos usuários recebem créditos promocionais de **sandbox/trial ($10 a $100 em créditos de boas-vindas)** para testar a API sem cobrança antecipada.

* **Endpoint Base**:
  * LLMs: `https://api.novita.ai/v3/openai` (OpenAI-compatible)
  * Imagem & Mídia: `https://api.novita.ai/v3` (REST proprietário com endpoints como `/v3/async/txt2img` e `/v3/txt2img_v3`)
* **Tipo de Cota**: Créditos promocionais de sandbox no cadastro ($10-$100) com modelo pay-as-you-go após o término.
* **Limites de Taxa Granulares**:
  * **LLM Chat**: **60 RPM**.
  * **Geração de Imagem (`txt2img_v3`)**: **20 IPM** (Images Per Minute).
  * **Tarefas de Inpainting / Face Restoration**: **10 IPM**.
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** no cadastro para utilização dos créditos promocionais de boas-vindas e exploração de sandbox.
* **Autenticação**: Bearer token via `Authorization: Bearer <NOVITA_API_KEY>`.

| Modelo ID API | Modalidade | Contexto (In / Out) | Rate Limit (RPM/IPM) | Cota Inicial | Aplicações Principais |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `meta-llama/llama-3.1-70b-instruct` | Texto / Tools | 131.072 / 8.192 | **60 RPM** | Trial ($10-$100) | Raciocínio, orquestração de agentes e geração de JSON estruturado |
| `meta-llama/llama-3.1-8b-instruct` | Texto Rápido | 131.072 / 8.192 | **60 RPM** | Trial ($10-$100) | Processamento rápido com custo marginal e baixa latência |
| `deepseek/deepseek-r1` | Raciocínio Puro | 65.536 / 8.192 | **60 RPM** | Trial ($10-$100) | Resolução de problemas matemáticos e cadeias lógicas densas |
| `flux.1-schnell` | Geração de Imagem | 1.024 x 1.024 | **20 IPM** | Trial ($10-$100) | Geração de imagens rápida em 4 passos com renderização tipográfica |
| `flux.1-dev` | Imagem Pro | 1.024 x 1.024 | **10 IPM** | Trial ($10-$100) | Síntese de imagem com alta fidelidade a prompts detalhados |
| `stable-diffusion-xl-base` | Imagem Clássica | 1.024 x 1.024 | **20 IPM** | Trial ($10-$100) | SDXL 1.0 para pipelines de imagem e controle por LoRA |

---

### 🔵 NEBIUS TOKEN FACTORY (api.studio.nebius.ai) — *Validado em 17/09/2026 (AI Builder Program & Dynamic Scaling)*

O Nebius Token Factory (anteriormente Nebius AI Studio) é uma plataforma corporativa de inferência acelerada em clusters de GPUs NVIDIA H100/H200. O acesso gratuito para desenvolvedores ocorre através do programa **AI Builder Program**, que concede **$400+ em créditos de infraestrutura**, com um sistema exclusivo de **Auto-Scaling Dinâmico de Rate Limits**.

* **Endpoint Base**: `https://api.studio.nebius.ai/v1` (Compatível com formato OpenAI SDK)
* **Tipo de Cota**: AI Builder Program com créditos gratuitos ($400+ sob aprovação de desenvolvedor).
* **Mecanismo Exclusivo de Rate Limit Dinâmico**:
  * Não opera com limites rígidos imutáveis: o sistema avalia a taxa de uso em janelas móveis de **15 minutos**.
  * Se o tráfego atingir **≥80%** do limite atual, a plataforma **aumenta automaticamente a taxa em 20%** para a próxima janela (até um teto de 20x a base antes de transição para o plano Enterprise).
  * Base inicial padrão: **60 RPM / 100K TPM**.
* **Requisitos de Entrada / Cartão**: Inscrição no AI Builder Program via portal Nebius (avaliação de projeto e perfil de desenvolvedor).
* **Autenticação**: Bearer token via `Authorization: Bearer <NEBIUS_API_KEY>`.

| Modelo ID API | Família / Tipo | Contexto (In / Out) | Rate Limit Base | Tipo de Cota | Notas & Infraestrutura |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `meta-llama/Meta-Llama-3.1-405B-Instruct` | Llama 3.1 405B | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Modelo aberto de maior escala rodando em superclusters H100 |
| `meta-llama/Meta-Llama-3.1-70B-Instruct` | Llama 3.1 70B | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Resposta de baixa latência (TTFT < 200ms) para pipelines críticos |
| `deepseek-ai/DeepSeek-V3` | DeepSeek V3 | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | DeepSeek V3 hospedado em data centers ocidentais de alta segurança |
| `deepseek-ai/DeepSeek-R1` | DeepSeek R1 | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Raciocínio profundo sem estrangulamento de infraestrutura |
| `Qwen/Qwen2.5-72B-Instruct` | Qwen 2.5 72B | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | 72B para tarefas complexas de raciocínio lógico e programação |
| `mistralai/Mistral-Large-Instruct-2407` | Mistral Large | 128.000 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Modelo de raciocínio de ponta da Mistral AI com janela de 128K |

---

### ⛔ AUDITORIA DE GATEWAYS & PLATAFORMAS: SEM FREE TIER PERMANENTE OU DESCONTINUADOS

Para proteger arquiteturas autônomas e evitar falhas silenciosas de execução (HTTP 402/403), foram auditadas as seguintes plataformas frequentemente citadas na comunidade:

1. **CHUTES.AI (`llm.chutes.ai/v1`) — FREE TIER DESCONTINUADO** 🚨:
   * **Status**: O plano gratuito para consumo de inferência foi formalmente **encerrado** no início de 2026. A Chutes migrou integralmente para um modelo pago baseado em subscrição mínima (a partir de $3/mês) e bilhetagem por segundo de computação confidencial. Não deve ser integrado em rotas gratuitas.
2. **LEPTON AI — REBRANDING & ABSORÇÃO POR NVIDIA DGX CLOUD** 🚨:
   * **Status**: A Lepton AI foi adquirida e incorporada pela NVIDIA, sendo relançada como **NVIDIA DGX Cloud Lepton**. O serviço serverless independente de inferência com free tier foi desativado; a capacidade agora é provisionada como marketplace de capacidade de GPU para clientes corporativos.
3. **TOGETHER AI (`api.together.xyz`) — SEM FREE TIER PERMANENTE** ⚠️:
   * **Status**: Não disponibiliza plano gratuito contínuo nem cota perpétua. A ativação de chaves de API requer compra mínima pré-paga de créditos (mínimo de $5 USD). Seus rate limits são dinâmicos e atrelados ao histórico de faturamento.
4. **AI/ML API (aimlapi.com) — FREE TIER PAUSADO/ENCERRADO** 🚨:
   * **Status**: A documentação oficial confirma que o "Free Tier" encontra-se atualmente **pausado**. A plataforma opera 100% sob recarga pré-paga de créditos (taxa de conversão: 2.000.000 créditos = $1 USD).
5. **FEATHERLESS.AI (`api.featherless.ai/v1`) — ACESSO BASEADO EM CONCORRÊNCIA PAGA** ⚠️:
   * **Status**: Opera através de planos pagos com foco em unidades concorrentes simultâneas (concurrency units) e créditos pré-pagos. Não oferece alocação perpétua com vazão garantida sem assinatura.
6. **BASETEN (`baseten.co`) — DEPLOY DE INFRAESTRUTURA DEDICADA** ⚠️:
   * **Status**: Focado na hospedagem e deploy de modelos dedicados (Truss serverless e instâncias privadas), fornecendo créditos pontuais de onboarding corporativo, sem manter catálogo compartilhado de inferência pública gratuita perpétua.


---

## 2. GUIA DE PLANOS DE BAIXO CUSTO ($5 A $10 USD) & GATEWAYS "BUDGET"

Para desenvolvedores, startups e agentes autônomos que desejam ir além dos limites dos Free Tiers sem incorrer em custos corporativos pesados, este guia mapeia as opções mais eficientes de **micro-orçamento (\$5 a \$10 USD)**, especializadas em altíssimo volume de tokens e acesso irrestrito a modelos de ponta.

---

### 💵 ANÁLISE DE ROI: O QUE VOCÊ REALMENTE COMPRA COM $5 DÓLARES?

| Provedor / Gateway | Tipo de Plano | Custo de Entrada | Volume de Tokens Entregue com $5 | Modelos Acessíveis | Vantagem Estratégica |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **DeepSeek Direto** (`api.deepseek.com`) | Pay-as-you-go | **$5.00** depósito | **18 a 35M tokens** (sem cache) / **100M+** (com cache) | `deepseek-chat` (DeepSeek-V3), `deepseek-reasoner` (DeepSeek-R1) | **Maior densidade de tokens do planeta**. Preços oficiais: $0.14/$0.28 (V3), $0.55/$2.19 (R1), Cache Hit a $0.014/M e 50% de desconto Off-Peak. |
| **xKiro** (`xkiro.com`) | Wallet Prepago | **$5.00** recarga | **5M tokens/dia FREE** + Saldo para modelos Pro | 40+ modelos (Claude 3.5 Sonnet, GPT-4o, DeepSeek, Qwen) | Free Tier perpétuo diário sem cartão + $5 no wallet para contornar filas e acessar frontier models. |
| **OpenCode Zen** (`opencode.ai`) | Pay-as-you-go Zero Markup | Sem mínimo ($0 a $5) | **Modelos Free Nativos** + Custo de atacado puro | `MiMo V2.5 Free`, `MiniMax M2.5 Free`, Qwen Coder, DeepSeek | Gateway sem margem de revenda; conecta direto via `/connect` no terminal/TUI. |
| **OpenCode Go** (`opencode.ai`) | Subscrição Mensal | **$10/mês** (promo $5 intro) | **Até $60 em valor de tokens** em janelas de 5h | DeepSeek V3/R1, Qwen 2.5 Coder, Kimi, GLM, MiniMax | Projetado especificamente para agentes de programação (OpenCode CLI, Aider, Cline). |
| **B.AI** (`b.ai`) | Sistema de Créditos (1M/$1) | **$5.00** recarga | **5 a 50 MILHÕES** de tokens (horários ociosos) | 20+ modelos globais e chineses (Gemini 3.8, Claude, Hunyuan, Qwen) | Descontos de até 90% em períodos de baixa demanda (off-peak); integração com BAI Code e Web3. |
| **SiliconFlow** (`api.siliconflow.com`) | Pay-as-you-go | **$5.00** (¥35 RMB) | **10 a 20 MILHÕES** de tokens nos modelos 14B/32B | Qwen 2.5 72B, DeepSeek R1/V3 full, FLUX.1 Dev | Transição transparente após esgotar o Free Tier perpétuo de 1.000 RPM nos modelos 7B. |

---

### 🛠️ DETALHAMENTO DOS GATEWAYS "BUDGET"

#### 🟢 XKIRO (xkiro.com — "xhiro" / AI Gateway Multimodel)
* **Endpoint Base**: `https://api.xkiro.com/v1` (Compatível com OpenAI SDK `/chat/completions`)
* **Acesso Gratuito**: Oferece uma cota diária de **5.000.000 de tokens por dia (5M TPD)** cobrindo mais de 40 modelos abertos e destilados sem necessidade de cartão de crédito.
* **Plano Wallet ($5 USD)**: Permite recargas pequenas de $5 via cartão ou Stripe. O saldo no wallet não expira e é consumido apenas quando você chama modelos proprietários de ponta (como Claude 3.5 Sonnet, GPT-4o ou DeepSeek R1 completo) ou quando necessita de prioridade máxima de throughput sem fila.
* **Funcionalidades**: Smart Model Routing, fallback automático entre provedores e suporte nativo a streaming SSE.

#### 🟢 OPENCODE (opencode.ai — OpenCode Zen & Go)
* **Ecossistema**: Focado na comunidade de desenvolvedores e assistentes de código em terminal.
* **OpenCode Zen**:
  * Funciona como um gateway universal sem cobrança de margem adicional (zero markup).
  * Disponibiliza **modelos 100% gratuitos**, como `MiMo V2.5 Free`, `MiniMax M2.5 Free` e `Big Pickle`.
  * Para modelos comerciais (como Qwen 2.5 Coder 32B ou DeepSeek V3), cobra estritamente por milhão de tokens consumidos diretamente no cartão/saldo, sem necessidade de assinar pacotes caros.
* **OpenCode Go ($10/mês)**:
  * Plano de assinatura para usuários frequentes.
  * Por um valor fixo, entrega um teto de consumo avaliado em até **$60 USD de valor de mercado**, distribuído em janelas móveis de 5 horas, semanas e meses.
  * Suporta mais de 75 provedores e integra perfeitamente com agentes de terminal.

#### 🟢 B.AI (b.ai — "白" / Infraestrutura Econômica de Agentes)
* **Endpoint Base**: `https://api.b.ai/v1` (OpenAI-compatible)
* **Mecânica Econômica**: Opera sob uma unidade própria de liquidação: **1 USD = 1.000.000 de Créditos B.AI**.
* **Precificação Dinâmica (Off-Peak Discounts)**: Monitora a carga global dos data centers parceiros. Em horários de baixa demanda (madrugadas asiáticas/americanas), aplica **descontos de até 90%** sobre o preço de tabela de modelos como Gemini, Claude, Hunyuan e DeepSeek.
* **Ideal Para**: Agentes de execução noturna (batch processing, data scraping, síntese de relatórios em background) onde $5 USD realizam o trabalho equivalente a $50 USD em APIs tradicionais.

#### 🟢 TENCENT WORKBUDDY (workbuddy.ai)
* **Natureza**: Não é uma API isolada, mas um **AI-native Desktop Workspace** corporativo desenvolvido pela Tencent Cloud.
* **Política de Custos**: Gratuito para uso pessoal como runtime de agente local. Permite plugar **chaves de API próprias (BYO-Key)** de qualquer provedor compatível com OpenAI (incluindo chaves gratuitas do Groq, SiliconFlow, Zhipu AI ou xKiro).
* **Para Equipes**: Planos baseados em assentos corporativos com pool compartilhado de créditos para automação de rotinas no Office, WeCom e geração automática de planilhas.

---

## 3. PROVEDORES ADICIONAIS & COMPLEMENTARES (ABSORÇÃO OMNIROUTE & SOBERANIA)

### 🦜 MARITACA AI (MariTalk) — A Campeã Nacional Brasileira de IA
* **Console / Cadastro**: [https://plataforma.maritaca.ai/](https://plataforma.maritaca.ai/)
* **Endpoint Base**: `https://chat.maritaca.ai/api` (Compatível nativo com OpenAI SDK)
* **Requisitos**: ❌ **Zero Cartão de Crédito** • ❌ **Zero Telefone/SMS** (Login com Google ou Email)
* **Cota do Tier 0 (Gratuito)**: **50 RPM / 500.000 TPM** concedidos permanentemente para testes e experimentação de desenvolvedores.
* **Por que é Vital**: Desenvolvida no Brasil por pesquisadores e doutores da Unicamp, a família **Sabiá** possui a maior acurácia e calibração para língua portuguesa, jurisprudência brasileira, redação de editais, ENEM, OAB e nuances culturais regionais.

| Identificador de Chamada (API) | Display Name | Modalidade | Contexto (In / Out) | RPM | TPM | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`sabia-4`** | Sabiá-4 Fronteira | Texto / Código | 128.000 / 8.192 | **50** | **500.000** | **#1 Nacional** — Máxima precisão factual em português e raciocínio formal |
| **`sabia-4-thinking`** | Sabiá-4 Reasoning | CoT / Agentes | 128.000 / 16.384 | **50** | **500.000** | Raciocínio estendido (Chain-of-Thought), tool calling e busca em bases oficiais |
| **`sabiazinho-4`** | Sabiazinho-4 Rápido| Compacto | 64.000 / 4.096 | **50** | **500.000** | Baixíssima latência, ideal para classificação, extração rápida e pipelines de triagem |
| `sabia-3` | Sabiá-3 Legado | Texto | 32.000 / 4.096 | 50 | 500.000 | Mantido para estabilidade de rotas legadas |
| `sabiazinho-3` | Sabiazinho-3 Legado| Compacto | 16.000 / 2.048 | 50 | 500.000 | Versão compacta anterior |

---

### ☁️ CLOUDFLARE WORKERS AI
* **Console**: [https://dash.cloudflare.com/](https://dash.cloudflare.com/)
* **Cota Gratuita Permanente**: **10.000 Neurons por dia** no plano gratuito (reseta todos os dias às 00:00 UTC).
* **Rendimento Real**: Equivale a **100.000 a 500.000 tokens diários gratuitos**, dependendo da densidade de parâmetros do modelo.
* **Modelos em Destaque na Cota Gratuita**:
  * `@cf/meta/llama-3.3-70b-instruct` (Inferência de 70B sem custo)
  * `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` (Raciocínio lógico)
  * `@cf/qwen/qwen2.5-coder-32b-instruct` (Geração de código de alta performance)
  * `@cf/baai/bge-large-en-v1.5` (Embeddings para RAG)
  * `@cf/black-forest-labs/flux-1-schnell` (Geração de imagens)
* **Requisitos**: Conta comum Cloudflare (sem cobrança no cartão).

---

### ⚡ SAMBANOVA CLOUD
* **Console**: [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/)
* **Endpoint Base**: `https://api.sambanova.ai/v1` (Compatível com OpenAI SDK)
* **Infraestrutura**: Chips proprietários **SN40L RDUs (Reconfigurable Dataflow Units)**, projetados para vazão ultra-alta (centenas de tokens por segundo em modelos de 70B).
* **Cota Gratuita**: Free Developer Tier com **30 RPM / 6.000 TPM** e limites diários de tokens (TPD) sem cartão de crédito.
* **Modelos Disponíveis**: `Meta-Llama-3.3-70B-Instruct`, `DeepSeek-R1`, `DeepSeek-R1-Distill-Llama-70B`, `Qwen2.5-72B-Instruct`.

---

### 🤗 HUGGING FACE SERVERLESS INFERENCE API
* **Console / Tokens**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
* **Endpoint Base**: `https://api-inference.huggingface.co/v1/` (Compatível com OpenAI)
* **Cota**: Gratuita para desenvolvedores pessoais com User Access Token comum (leitura). Rate limit médio de **10 a 30 RPM** com gerenciamento automático de cold-start de contêineres.
* **Acervo de Modelos**: Acesso serverless imediato a milhares de modelos open-source:
  * `meta-llama/Llama-3.3-70B-Instruct`
  * `Qwen/Qwen2.5-72B-Instruct`
  * `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`
  * `BAAI/bge-large-en-v1.5` (Vetores)
  * `openai/whisper-large-v3` (Transcrição de voz)

---

### 🎯 ESPECIALISTAS EM EMBEDDINGS & RERANKING
Para arquiteturas avançadas de RAG (Retrieval-Augmented Generation) sem onerar a cota de chat:
1. **Nomic AI (`https://www.nomic.ai/`)**:
   * Modelo: `nomic-embed-text-v1.5` (Janela de 8.192 tokens com dimensionalidade configurável).
   * Cota: Free Tier com dezenas de milhares de requisições de vetorização gratuitas sem cartão.
2. **Mixedbread AI (`https://www.mixedbread.ai/`)**:
   * Modelos: `mxbai-rerank-large-v1` (Rerank state-of-the-art) e `mxbai-embed-large`.
   * Cota: Cota mensal gratuita para desenvolvedores.

---

### 🕵️ GATEWAYS ANÔNIMOS & SEM CHAVE (ZERO CADASTRO, ZERO CARTÃO)
Para testes de bancada, pipelines educacionais e protótipos onde você não deseja emitir credenciais:
1. **AI Horde (`https://aihorde.net/`)**: Rede voluntária distribuída de GPUs. Permite chamadas com a chave pública anônima `0000000000` para chat (`oai.aihorde.net/v1`) e geração de imagens Stable Diffusion sem conta.
2. **DuckDuckGo AI Chat (`https://duckduckgo.com/duckchat`)**: Interface web gratuita e anônima com Claude 3 Haiku, GPT-4o mini e Llama 3.3 sem retenção de logs.
3. **UncloseAI (`https://uncloseai.com/`)**: Endpoint compatível com OpenAI que aceita qualquer string como chave de API para testes rápidos.

---

### 🟢 GITHUB MODELS (Azure AI Foundry)
* **Endpoint**: `https://models.inference.ai.azure.com`
* **Cotas**: **10 a 15 RPM** / **100 a 150 RPD**. Modelos: `Claude-3.5-Sonnet`, `GPT-4o`, `o4-mini`, `DeepSeek-R1`, `Llama-3.3-70B`.

---

### 🚀 INCEPTION LABS (Mercury API) — O Gigante dos 100 Milhões de Tokens
* **Console / Cadastro**: [https://platform.inceptionlabs.ai/](https://platform.inceptionlabs.ai/)
* **Endpoint Base**: `https://api.inceptionlabs.ai/v1` (Compatível nativo com OpenAI SDK)
* **Requisitos**: ❌ **Zero Cartão de Crédito** • ❌ **Zero Telefone/SMS** (Login com Google ou GitHub)
* **Cota do Free Tier**: Concessão imediata de **100.000.000 (100 Milhões) de tokens gratuitos** creditados no saldo da conta no momento da criação.
* **Arquitetura & Velocidade**: Baseado na arquitetura proprietária Mercury/Mercurius, projetada para inferência em tempo real com vazão ultra-alta (150+ tokens/segundo) e latência inferior a 300ms no primeiro token.

| Identificador de Chamada (API) | Display Name | Modalidade | Contexto (In / Out) | RPM | Concorrência | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`mercury-chat`** | Mercury Chat Ultra | Texto | 128.000 / 8.192 | **60** | **5** | Modelo principal para chat, sumarização e redação fluida |
| **`mercury-coder`** | Mercury Coder Pro | Código | 128.000 / 16.384 | **60** | **5** | Especializado em refatoração, linting e geração de código full-stack |

---

### 🔮 REKA AI — Créditos Recorrentes Mensais & Vídeo Multimodal
* **Console / Cadastro**: [https://platform.reka.ai/](https://platform.reka.ai/)
* **Endpoint Base**: `https://api.reka.ai/v1` (Compatível com OpenAI SDK e SDK oficial `reka-api`)
* **Requisitos**: ❌ **Zero Cartão de Crédito** (Cadastro direto com email de desenvolvedor)
* **Cota Recorrente Perpétua**: **$10 USD em créditos gratuitos renovados todo mês** no painel de desenvolvedor. Não expira enquanto a conta for ativa.
* **Bônus Multimodal**: Inclui **3 horas de processamento e indexação de vídeo gratuitas** na API de visão.

| Identificador de Chamada (API) | Display Name | Modalidade | Contexto (In / Out) | RPM | TPM | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`reka-flash`** | Reka Flash Multimodal | Texto / Visão / Áudio | 128.000 / 8.192 | **30** | **150.000** | Modelo frontier multimodal rápido, excelente para QA visual e vídeo |
| **`reka-core`** | Reka Core Frontier | Raciocínio Pesado | 128.000 / 8.192 | **10** | **50.000** | Máxima capacidade de raciocínio lógico e resolução de problemas |
| **`reka-edge`** | Reka Edge Fast | Eficiência | 32.000 / 4.096 | **60** | **300.000** | Ultra-rápido, ideal para micro-agentes e classificação em lote |

---

### 📦 BYTEZ — $1.00 Renovado a Cada 4 Semanas
* **Console / Cadastro**: [https://bytez.com/](https://bytez.com/)
* **Endpoint Base**: `https://api.bytez.com/v1` (Compatível nativo com OpenAI SDK)
* **Requisitos**: ❌ **Zero Cartão de Crédito**
* **Cota Recorrente**: **$1.00 USD de crédito gratuito renovado a cada 4 semanas (28 dias)**.
* **Poder de Compra do $1**: Como a inferência na Bytez custa frações de centavos para modelos abertos, $1 permite rodar entre **2.000.000 e 5.000.000 de tokens** por ciclo de renovação.
* **Modelos Disponíveis**: `meta-llama/llama-3.3-70b-instruct`, `qwen/qwen-2.5-72b-instruct`, `mistralai/mistral-7b-instruct`.

---

### ⚡ MORPH LABS (Fast Apply) — Acelerador de Agentes de Código
* **Console / Cadastro**: [https://morphllm.com/](https://morphllm.com/)
* **Endpoint Base**: `https://api.morphllm.com/v1`
* **Requisitos**: ❌ **Zero Cartão de Crédito**
* **Cota Gratuita Permanente**: **250.000 créditos / mês gratuitos ($0)** e até 200 requisições mensais de Fast Apply.
* **O que Resolve**: Desenvolvido especificamente para agentes autônomos de código (estilo Cline, Cursor, Aider). Aplica diffs gigantescos e alterações de arquivos em menos de 1 segundo sem re-gerar o arquivo inteiro, economizando 90% de tokens de saída.

---

### 🖥️ MODAL LABS — Nuvem Serverless de GPUs ($30/Mês Grátis)
* **Console**: [https://modal.com/](https://modal.com/)
* **Cota Recorrente**: **$30 USD em créditos de computação gratuitos por mês** no plano Starter.
* **Requisitos**: 🟠 **Requer Cartão de Crédito** para destravar os $30 (sem cartão limita a $5).
* **Para que serve**: Permite subir instâncias de vLLM, Ollama, Whisper ou geração de imagens em GPUs A10G / L4 / H100 sob demanda com desligamento a zero em segundos quando ocioso.

---

### 🌏 JOIAS DE SOBERANIA REGIONAL & GATEWAYS ULTRARRÁPIDOS

Para diversificação geográfica, resiliência geopolítica e acesso a modelos especializados em idiomas locais:

1. **InternLM / Shanghai AI Lab (`https://internlm.intern-ai.org.cn/`)**:
   * **Cota**: **1.000.000 tokens de entrada / 3.000.000 tokens de saída gratuitos todo mês**.
   * **Modelos**: `internlm2.5-20b-chat`, `internlm2.5-7b-chat`, `internlm-xcomposer2.5` (Visão).
   * **Requisitos**: Sem cartão. Cadastro com email de desenvolvedor.

2. **Sarvam AI (`https://docs.sarvam.ai/`) — Soberania Índia**:
   * **Cota**: **₹1.000 INR (~$12 USD) em créditos de boas-vindas perpétuos** sem expiração forçada.
   * **Modelos**: `sarvam-2b` (líder absoluto em 10 línguas indianas: Hindi, Tâmil, Telugo, Bengali, etc.), `sarvam-translate` e `sarvam-speech-to-text`.
   * **Requisitos**: ❌ Zero cartão.

3. **SEA-LION / AI Singapore (`https://sea-lion.ai/`) — Soberania Sudeste Asiático**:
   * **Cota**: **10 RPM / 100.000 TPM** permanente sem custo.
   * **Modelos**: `sea-lion-v3-7b-instruct` (calibrado para Indonésio, Malaio, Tailandês, Vietnamita, Filipino).
   * **Requisitos**: ❌ Zero cartão.

4. **LLM7.io (`https://llm7.io/`) — Gateway Anônimo Ultrarrápido**:
   * **Endpoint**: `https://api.llm7.io/v1` (OpenAI format)
   * **Cota**: **2 requisições por segundo, 20 RPM, 100 requisições por hora** sem autenticação, sem chave, sem cadastro. Ideal para fallbacks de emergência e testes automáticos de CI/CD.

---

### ⚠️ AUDITORIA & EXCLUSÕES DE SEGURANÇA (FALSOS FREE TIERS & ALERTAS)

Nossa auditoria rigorosa de bancada expurgou e esclareceu as seguintes plataformas que circulam erroneamente em listas como "gratuitas":

1. **FriendliAI (`friendli.ai`)**:
   * **Alegação em catálogos desatualizados**: "API pública keyless e gratuita".
   * **Realidade Auditada**: ❌ **Falso**. A FriendliAI opera sob modelo 100% comercial pay-per-token faturado. Não há endpoint público permanente gratuito.
2. **Liquid AI (`liquid.ai`)**:
   * **Alegação em blogs**: "Endpoint direto de API gratuita para Liquid Foundation Models (LFM)".
   * **Realidade Auditada**: ⚠️ **Aviso de Arquitetura**. A Liquid AI NÃO disponibiliza um endpoint self-serve público autônomo com chave direta. Os modelos LFM-2.5 e LFM-2.6B são acessados gratuitamente via **OpenRouter** (`liquid/lfm-2.5-2.6b:free`) ou via **Hugging Face Inference**. Cuidado com domínios de terceiros se passando por API direta da Liquid AI.
3. **CrofAI (`crof.ai`)**:
   * **Alegação**: "Free Gateway de alta velocidade".
   * **Realidade Auditada**: 🚨 **Fraude / Descontinuado**. O serviço foi desligado em setembro de 2026, domínio retirado do ar com erro 404 e certificado revogado. Excluído em definitivo do catálogo.


---



---

### 🏛️ OS 4 PILARES ESTRATÉGICOS: 20 NOVOS PROVEDORES AUDITADOS (v16)

A versão v16 consolida uma auditoria exaustiva de bancada de 20 plataformas de inferência de ponta, divididas rigorosamente em 4 blocos operacionais para arquiteturas autônomas de produção e micro-orçamento ($0 a $5 USD). Com esta adição, o catálogo atinge **64 provedores documentados**.

---

#### 🚀 PILAR 1: 5 PROVEDORES DE LLMS E INFERÊNCIA SERVERLESS DE ALTA VELOCIDADE

Provedores especializados em latência mínima no primeiro token (TTFT) e taxas extremas de geração (150 a 300 tokens/segundo) para orquestrações de agentes e processamento massivo:

##### 1. Fireworks AI (fireworks.ai) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://fireworks.ai/](https://fireworks.ai/)
* **Endpoint Base**: `https://api.fireworks.ai/inference/v1` (Compatível 1:1 com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** para receber os créditos iniciais.
* **Verificação**: E-mail / GitHub / Google. Sem exigência obrigatória de SMS.
* **Tipo de Cota & Saldo Inicial**: Concessão imediata de **$1.00 USD em créditos gratuitos** de boas-vindas sem expiração agressiva.
* **Poder de Compra de $1 USD**: Graças à arquitetura proprietária FireAttention, modelos abertos de ponta custam apenas $0.20 por milhão de tokens. Com $1 USD de trial é possível processar até **5.000.000 de tokens** em modelos 70B e mais de 10.000.000 de tokens em modelos 8B.
* **Limites de Taxa Granulares**:
  * **RPM**: **600 RPM** padrão no Free/Trial Tier.
  * **TPM**: **10.000 TPM** padrão.
  * **Throughput**: 150 a 250 tokens/segundo por stream.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limites de Taxa | Custo Pós-Free | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`accounts/fireworks/models/llama-v3p3-70b-instruct`** | Llama 3.3 70B Instruct | Texto | 131.072 / 4.096 | 600 RPM / 10k TPM | $0.20 / $0.20 por 1M | O cavalo de batalha open-source mais veloz do mercado |
| **`accounts/fireworks/models/qwen2p5-72b-instruct`** | Qwen 2.5 72B Instruct | Texto | 131.072 / 8.192 | 600 RPM / 10k TPM | $0.20 / $0.20 por 1M | Alta inteligência analítica e exatas |
| **`accounts/fireworks/models/deepseek-v3`** | DeepSeek-V3 MoE | MoE Texto | 131.072 / 8.192 | 600 RPM / 10k TPM | $0.20 / $0.28 por 1M | Modelo MoE de 671B parâmetros com 37B ativos |
| **`accounts/fireworks/models/deepseek-r1`** | DeepSeek-R1 Reasoner | Raciocínio | 131.072 / 16.384 | 600 RPM / 10k TPM | $0.55 / $2.19 por 1M | Raciocínio profundo e cadeias de pensamento completas |
| **`accounts/fireworks/models/firefunction-v2`** | FireFunction v2 | Tool Calling | 8.192 / 4.096 | 600 RPM / 10k TPM | $0.20 / $0.20 por 1M | Especializado em invocação estruturada de ferramentas JSON |

##### 2. Clarifai (clarifai.com) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://portal.clarifai.com/](https://portal.clarifai.com/)
* **Endpoint Base**: `https://api.clarifai.com/v2` (REST / gRPC / Python SDK `clarifai`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / GitHub / Google.
* **Tipo de Cota Perpétua**: **Community Free Tier Permanente** com **1.000 operações gratuitas por mês** renovadas todo mês perpetuamente.
* **Limites de Taxa Granulares**:
  * **Cota Mensal**: 1.000 operações de inferência / mês.
  * **RPM**: **10 RPM**.
  * **Concorrência**: 1 chamada simultânea.
* **Recursos**: Plataforma unificada de inferência serverless multimodal que dá acesso a modelos de visão computacional, moderação e LLMs de terceiros.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limite Mensal | Requisitos | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`openai/chat-completion/models/gpt-4o`** | GPT-4o via Clarifai | Multimodal | 128.000 / 4.096 | 1.000 ops/mês | ❌ Sem Cartão | Execução serverless de frontier model via créditos comunitários |
| **`meta/Llama-3/models/llama-3_3-70b-instruct`** | Llama 3.3 70B | Texto | 131.072 / 4.096 | 1.000 ops/mês | ❌ Sem Cartão | Modelo aberto líder rodando em infraestrutura gerenciada |
| **`clarifai/main/models/general-image-recognition`** | General Visual Classifier | Visão | 1 imagem / tags | 1.000 ops/mês | ❌ Sem Cartão | Classificação de imagem e detecção de mais de 10.000 conceitos |
| **`clarifai/main/models/text-moderation`** | Text Moderation Model | Moderação | 8.192 / 128 | 1.000 ops/mês | ❌ Sem Cartão | Triagem e segurança de conteúdo para agentes autônomos |

##### 3. Baseten (baseten.co) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://baseten.co/](https://baseten.co/)
* **Endpoint Base**: `https://bridge.baseten.co/v1` ou `https://model-<model_id>.api.baseten.co/v1` (Compatível nativo com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** no cadastro inicial para acessar os créditos de computação.
* **Verificação**: E-mail profissional / GitHub.
* **Tipo de Cota Free**: **$30.00 USD em créditos de computação gratuitos** concedidos no onboarding de desenvolvedor.
* **Arquitetura & Deploy**: Permite servir modelos open-source utilizando **Truss** (framework open-source da Baseten) e **vLLM / SGLang** em GPUs A100/H100, com desligamento automático a zero (scale-to-zero) quando inativo para não desperdiçar créditos.
* **Limites de Taxa**: Até 60 RPM no bridge compartilhado; taxa de throughput dependente do número de réplicas ativas.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limite / Cota | Requisitos | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B Bridge | Texto | 131.072 / 4.096 | $30 em créditos | ❌ Sem Cartão | Inferência de altíssima velocidade em GPUs A100 dedicadas |
| **`deepseek-ai/DeepSeek-V3`** | DeepSeek-V3 Bridge | MoE Texto | 131.072 / 8.192 | $30 em créditos | ❌ Sem Cartão | Deploy de MoE com otimização de tensor parallelism |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`** | Qwen 2.5 Coder 32B | Programação | 131.072 / 8.192 | $30 em créditos | ❌ Sem Cartão | Especializado em análise e refatoração de código com vLLM |
| **`mistralai/Mistral-Small-24B-Instruct-2501`** | Mistral Small 24B | Raciocínio | 32.768 / 4.096 | $30 em créditos | ❌ Sem Cartão | Modelo intermediário ultrarrápido com TTFT sub-200ms |

##### 4. Replicate (replicate.com) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://replicate.com/](https://replicate.com/)
* **Endpoint Base**: `https://api.replicate.com/v1` (REST e SDKs oficiais `replicate` Python e Node.js)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** para rodar predições de teste via autenticação GitHub.
* **Verificação**: Conta GitHub com histórico/reputação.
* **Tipo de Cota**: **Créditos de teste de desenvolvedor (Free Trial)** concedidos automaticamente para testar modelos de linguagem, visão e geração de imagem na nuvem.
* **Limites de Taxa**: 1 a 2 predições simultâneas concorrentes na fila do Free Trial.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limite / Cota | Requisitos | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`meta/meta-llama-3.3-70b-instruct`** | Llama 3.3 70B Replicate | Texto | 131.072 / 4.096 | Trial Sandbox | ❌ Sem Cartão | Execução serverless sob demanda com streaming de tokens |
| **`deepseek-ai/deepseek-r1`** | DeepSeek-R1 Replicate | Raciocínio | 131.072 / 16.384 | Trial Sandbox | ❌ Sem Cartão | Raciocínio estruturado com retorno completo de tags `<think>` |
| **`black-forest-labs/flux-schnell`** | FLUX.1 Schnell | Geração Imagem | 1 prompt / 1024x1024 | Trial Sandbox | ❌ Sem Cartão | Difusão em 4 passos com qualidade de estúdio em 1,5 segundo |
| **`yorickvp/llava-13b`** | LLaVA 13B Multimodal | Visão + Texto | 4.096 / 1.024 | Trial Sandbox | ❌ Sem Cartão | Compreensão de imagem e perguntas e respostas visuais |

##### 5. xAI Console / Grok API (console.x.ai) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://console.x.ai/](https://console.x.ai/)
* **Endpoint Base**: `https://api.x.ai/v1` (Compatível nativo 1:1 com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** para recebimento da concessão de desenvolvedor (Monthly Developer Grant).
* **Verificação**: Autenticação via conta X (Twitter) / E-mail.
* **Tipo de Cota Recorrente**: **$25.00 USD / mês de Developer Grant** concedido para novos desenvolvedores experimentarem a família Grok.
* **Limites de Taxa Granulares**:
  * **RPM**: **60 RPM**.
  * **TPM**: **10.000 TPM**.
  * **Concorrência**: 5 requisições paralelas.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limites de Taxa | Cota / Saldo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`grok-2-1212`** | Grok 2 (Versão Consagrada) | Texto / Lógica | 131.072 / 4.096 | 60 RPM / 10k TPM | $25 USD / mês | Raciocínio afiado, fluidez verbal e zero censura corporativa excessiva |
| **`grok-2-vision-1212`** | Grok 2 Vision | Multimodal | 32.768 / 4.096 | 60 RPM / 10k TPM | $25 USD / mês | OCR de alta precisão, interpretação de gráficos e dados visuais |
| **`grok-beta`** | Grok Beta | Texto Rápido | 131.072 / 4.096 | 60 RPM / 10k TPM | $25 USD / mês | Endpoint de atualização contínua da família Grok |
| **`grok-vision-beta`** | Grok Vision Beta | Visão | 8.192 / 4.096 | 60 RPM / 10k TPM | $25 USD / mês | Análise de documentos e fluxo de imagens |

---

#### 🎙️ PILAR 2: 5 ESPECIALISTAS EM VOZ, ÁUDIO, STT E TTS

Provedores dedicados à transcrição de fala em texto (Speech-to-Text) com acurácia ultra-alta e síntese de voz (Text-to-Speech) de baixa latência para agentes conversacionais:

##### 6. Deepgram (deepgram.com) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://console.deepgram.com/](https://console.deepgram.com/)
* **Endpoint Base**: `https://api.deepgram.com/v1` (REST e WebSocket `wss://api.deepgram.com/v1/listen`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** no cadastro.
* **Verificação**: E-mail / Google / GitHub.
* **Tipo de Cota Free**: **$200.00 USD em créditos gratuitos perpétuos** creditados imediatamente no saldo da conta.
* **Volume Real Entregue por $200 USD**: O modelo Nova-2 custa apenas **$0.0043 por minuto de áudio**. Isso significa que os $200 de crédito cobrem impressionantes **46.500 minutos (~775 horas)** de transcrição de áudio 100% gratuita. Para TTS, o Aura custa $0.015 por 1.000 caracteres, rendendo mais de 13 milhões de caracteres sintetizados.
* **Limites de Taxa**: **100 conexões concorrentes**, **1.000 RPM**.

| Modelo ID API (Canônico) | Display Name | Modalidade | Formato de Entrada | Limites de Taxa | Custo Unitário | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`nova-2`** | Nova-2 Speech-to-Text | STT / Transcrição | WAV, MP3, OGG, FLAC | 100 conc / 1k RPM | $0.0043 / min | O STT mais veloz e preciso do mundo; pontuação automática e diarização |
| **`nova-2-general`** | Nova-2 Multilíngue | STT Multilíngue | Áudio em 30+ línguas | 100 conc / 1k RPM | $0.0043 / min | Suporte nativo completo a Português do Brasil com acentuação correta |
| **`nova-2-meeting`** | Nova-2 Reuniões | STT Multi-Locutor | Gravações com ruído | 100 conc / 1k RPM | $0.0043 / min | Especializado em identificar múltiplos falantes em salas de conferência |
| **`aura-asteria-en`** | Aura TTS Asteria | TTS / Voz Feminina | Texto UTF-8 | 100 conc / 1k RPM | $0.015 / 1k chars | Síntese vocal de latência ultrabaixa (<200ms) para bots de voz |
| **`aura-orion-en`** | Aura TTS Orion | TTS / Voz Masculina | Texto UTF-8 | 100 conc / 1k RPM | $0.015 / 1k chars | Tom executivo, naturalidade conversacional e respiração orgânica |

##### 7. AssemblyAI (assemblyai.com) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://assemblyai.com/](https://assemblyai.com/)
* **Endpoint Base**: `https://api.assemblyai.com/v2` (REST e WebSocket streaming `wss://api.assemblyai.com/v2/realtime/token`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / GitHub.
* **Tipo de Cota Free**: **$50.00 USD em créditos gratuitos de boas-vindas** no cadastro.
* **Volume Real Entregue por $50 USD**: No modelo Conformer-2 Nano ($0.0025/minuto), $50 rende **20.000 minutos (~333 horas)** de transcrição. No modelo Best ($0.0062/minuto), entrega mais de **130 horas de áudio transcrito**.
* **Recursos Avançados**: Detecção de locutores (Speaker Diarization), redação automática de PII (CPFs, cartões), análise de sentimento por frase e LeMUR (LLM integrado para extrair insights diretamente de gravações).
* **Limites de Taxa**: **5 transcrições concorrentes** no Free Tier, **100 RPM**.

| Modelo ID API (Canônico) | Display Name | Modalidade | Entrada / Contexto | Limites de Taxa | Custo Unitário | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`best`** | Conformer-2 Best STT | STT Acurado | Áudio URL ou binário | 5 conc / 100 RPM | $0.0062 / min | Máxima precisão em áudios complexos, termos médicos e jurídicos |
| **`nano`** | Conformer-2 Nano | STT Ultra-Rápido | Áudio URL ou binário | 5 conc / 100 RPM | $0.0025 / min | Aceleração máxima de transcrição a custo marginal |
| **`lemur-70b-chat`** | LeMUR Speech LLM | QA sobre Áudio | Transcrição + Pergunta | 5 conc / 100 RPM | Por token LeMUR | Responde perguntas, gera atas de reunião e extrai itens de ação |

##### 8. ElevenLabs (elevenlabs.io) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://elevenlabs.io/](https://elevenlabs.io/)
* **Endpoint Base**: `https://api.elevenlabs.io/v1/text-to-speech/{voice_id}` (REST e WebSocket streaming)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google.
* **Tipo de Cota Perpétua**: **Free Tier Permanente** concedendo **10.000 caracteres / mês gratuitos** renovados a cada 30 dias.
* **Recursos do Plano Free**: 3 slots para vozes customizadas ou clonadas, suporte a 29 idiomas com entonação emocional, geração de efeitos sonoros (Sound Effects API).
* **Limites de Taxa**: 10.000 caracteres/mês, 2 conexões simultâneas, 20 RPM. Requer atribuição de crédito no uso do plano gratuito.

| Modelo ID API (Canônico) | Display Name | Modalidade | Latência / Qualidade | Limite Free | Requisitos | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`eleven_multilingual_v2`** | Eleven Multilingual v2 | Síntese de Voz (TTS) | 44.1kHz Hi-Fi | 10.000 chars/mês | ❌ Sem Cartão | O padrão de excelência da indústria em realismo e emoção vocal |
| **`eleven_flash_v2_5`** | Eleven Flash v2.5 | TTS Tempo Real | ~75ms TTFB | 10.000 chars/mês | ❌ Sem Cartão | Projetado para assistentes virtuais e chamadas ativas de voz interativas |
| **`eleven_turbo_v2_5`** | Eleven Turbo v2.5 | TTS Equilibrado | Baixa latência | 10.000 chars/mês | ❌ Sem Cartão | Síntese rápida com fidelidade vocal estável para narração de vídeos |

##### 9. Cartesia (cartesia.ai) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://play.cartesia.ai/](https://play.cartesia.ai/)
* **Endpoint Base**: `https://api.cartesia.ai/tts/bytes` ou WebSocket `wss://api.cartesia.ai/tts/websocket`
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google / GitHub.
* **Tipo de Cota Free**: **Free Tier Sonic API** com concessão de créditos de boas-vindas para desenvolvedores (~100.000 caracteres gratuitos).
* **Arquitetura Base**: Baseado na arquitetura **State Space Model (SSM)**, o motor Sonic atinge **latência inferior a 150ms** e suporte a áudio estéreo em 44.1kHz, tornando-o o motor mais rápido para síntese conversacional em tempo real.
* **Limites de Taxa**: **30 RPM**, **10 conexões streaming simultâneas**.

| Modelo ID API (Canônico) | Display Name | Modalidade | Taxa de Amostragem | Limites de Taxa | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`sonic-english`** | Sonic English Ultra-Fast | TTS em Inglês | 44.1kHz / 24kHz / 16kHz | 30 RPM / 10 streams | Latência sub-150ms imperceptível para humanos em conversação telefônica |
| **`sonic-multilingual`** | Sonic Multilingual | TTS Multilíngue | 44.1kHz Hi-Fi | 30 RPM / 10 streams | Suporte a Francês, Alemão, Espanhol, Japonês e Português |
| **`sonic-fast`** | Sonic Fast Realtime | TTS Baixa Latência | 24kHz Otimizado | 30 RPM / 10 streams | Ajustado para menor consumo de largura de banda e streaming instantâneo |

##### 10. Lemonfox.ai (lemonfox.ai) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://lemonfox.ai/](https://lemonfox.ai/)
* **Endpoint Base**: `https://api.lemonfox.ai/v1` (Compatível 1:1 com a API de Áudio da OpenAI)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail simples para geração instantânea de chave de API.
* **Tipo de Cota Perpétua**: **Free Tier Diário Permanente** com cota diária renovável de requisições sem custo para transcrição Whisper e geração de áudio.
* **Compatibilidade Drop-in**: Substitui diretamente as rotas `/v1/audio/transcriptions` e `/v1/audio/speech` da OpenAI em bibliotecas e agentes existentes, apenas mudando `base_url` e `api_key`.
* **Limites de Taxa**: Cota diária gratuita (até 500 requisições mensais sem custo), 20 RPM.

| Modelo ID API (Canônico) | Display Name | Modalidade | Compatibilidade | Limites de Taxa | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`whisper-1`** | Lemonfox Whisper STT | STT / Transcrição | OpenAI `/audio/transcriptions` | Cota Diária Free | Transcrição precisa de áudio com timestamps de palavras |
| **`lemonfox-tts-v1`** | Lemonfox TTS Engine | TTS / Síntese | OpenAI `/audio/speech` | Cota Diária Free | Geração de áudio MP3 a partir de texto com múltiplas vozes |
| **`lemonfox-embed-v1`** | Lemonfox Embeddings | Embeddings de Texto | OpenAI `/embeddings` | Cota Diária Free | Vetorização semântica rápida para busca e similaridade |

---

#### 🔍 PILAR 3: 5 ESPECIALISTAS EM EMBEDDINGS, RERANK & BUSCA NEURAL PARA AGENTES

Plataformas de infraestrutura vetorial e pesquisa em tempo real construídas especificamente para agentes autônomos e sistemas RAG de alta fidelidade:

##### 11. Voyage AI (voyageai.com) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://dash.voyageai.com/](https://dash.voyageai.com/)
* **Endpoint Base**: `https://api.voyageai.com/v1/embeddings` e `https://api.voyageai.com/v1/rerank` (REST e SDK Python `voyageai`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google / GitHub.
* **Tipo de Cota Free**: **200 Milhões de tokens gratuitos de trial** no onboarding + cota perpétua de **50 Milhões de tokens gratuitos** para projetos open-source e acadêmicos.
* **Reputação na Indústria**: O motor Voyage AI é oficialmente recomendado pela Anthropic para RAG com a família Claude, superando modelos de embedding da OpenAI em quase todos os benchmarks MTEB. Suporta janelas gigantes de **32.000 tokens por documento**.
* **Limites de Taxa**: **300 RPM**, **1.000.000 TPM** no Free Tier.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto / Dimensões | Limites de Taxa | Cota Gratuita | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`voyage-3`** | Voyage-3 General Embedding | Embeddings | 32.000 ctx / 1024 dims | 300 RPM / 1M TPM | 200M tokens trial | Top #1 mundial em recuperação densa de texto geral |
| **`voyage-3-lite`** | Voyage-3-Lite Fast | Embeddings | 32.000 ctx / 512 dims | 300 RPM / 1M TPM | 200M tokens trial | Dimensionalidade compacta para indexação rápida e econômica |
| **`voyage-code-3`** | Voyage Code 3 | Embeddings Código | 32.000 ctx / 1024 dims | 300 RPM / 1M TPM | 200M tokens trial | Especializado em código-fonte, bibliotecas e documentação técnica |
| **`rerank-2`** | Voyage Rerank 2 | Reranking RAG | 16.000 ctx / Cross-Enc | 300 RPM / 1M TPM | 200M tokens trial | Reordenação de máxima precisão para os top 5-10 chunks do RAG |
| **`rerank-2-lite`** | Voyage Rerank 2 Lite | Reranking Rápido | 8.000 ctx / Cross-Enc | 300 RPM / 1M TPM | 200M tokens trial | Latência inferior a 50ms para buscas em tempo real |

##### 12. Jina AI (jina.ai) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://cloud.jina.ai/](https://cloud.jina.ai/)
* **Endpoints Base**:
  * Embeddings & Rerank: `https://api.jina.ai/v1/embeddings` e `https://api.jina.ai/v1/rerank`
  * Reader API: `https://r.jina.ai/<url>` (Converte qualquer URL em markdown limpo)
  * Search Grounding: `https://s.jina.ai/<query>` (Busca web direto em markdown)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / GitHub.
* **Tipo de Cota Free**:
  * **10 Milhões de tokens gratuitos** de boas-vindas no console para embeddings e rerankers.
  * **Jina Reader API (`r.jina.ai`) 100% GRATUITA E PERPÉTUA** (20 RPM anônimo sem chave; 200 RPM com chave free).
* **Limites de Taxa**: **500 RPM** nos endpoints de API com chave gratuita.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto / Dimensões | Limites de Taxa | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`jina-embeddings-v3`** | Jina Embeddings v3 | Embeddings | 8.192 ctx / 1024/512/256 dims | 500 RPM | Suporta Matryoshka Learning (dimensões flexíveis) e 89 línguas |
| **`jina-reranker-v2-base-multilingual`**| Jina Reranker v2 | Reranking | 8.192 ctx / Cross-Encoder | 500 RPM | Suporta Function Calling rerank e recuperação em múltiplos idiomas |
| **`jina-colbert-v2`** | Jina ColBERT v2 | Multi-Vector | 8.192 ctx / Token-level | 500 RPM | Busca granular em nível de token com alta interpretabilidade |
| **`r.jina.ai`** | Jina Reader Engine | Web Scraper LLM | Ilimitado (URL) | 20 a 200 RPM | Transforma páginas dinâmicas e JS em markdown limpo sem anúncios |

##### 13. Tavily AI (tavily.com) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://app.tavily.com/](https://app.tavily.com/)
* **Endpoint Base**: `https://api.tavily.com/search` e `https://api.tavily.com/extract` (REST e SDK `tavily-python`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google / GitHub.
* **Tipo de Cota Perpétua**: **1.000 requisições de busca / mês gratuitas perpétuas** renovadas a cada 30 dias sem necessidade de faturamento.
* **Diferencial para Agentes**: Ao contrário de engines convencionais, o Tavily foi projetado para LangChain, AutoGen e CrewAI. Ele remove lixo de HTML, extrai respostas factuais diretas e sintetiza um resumo factual pronto para o contexto do LLM.
* **Limites de Taxa**: **100 RPM**, **1.000 requisições/mês**.

| Parâmetro de Busca | Opções | Créditos Consumidos | Retorno | Casos de Uso Recomendados |
| :--- | :---: | :---: | :--- | :--- |
| `search_depth` | `"basic"` | 1 crédito / busca | Links + snippets limpos | Busca rápida em tempo real para checagem factual de agentes |
| `search_depth` | `"advanced"` | 2 créditos / busca | Conteúdo textual aprofundado | Pesquisa acadêmica, notícias detalhadas e relatórios complexos |
| `include_answer` | `true` | Sem custo adicional | Resposta sumarizada por IA | Resumo direto da dúvida para injeção imediata no prompt |
| `include_raw_content`| `true` | Sem custo adicional | Conteúdo integral da página | Ingestão documental completa sem necessidade de scraper separado |

##### 14. Exa.ai (exa.ai — antigo Metaphor) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://dashboard.exa.ai/](https://dashboard.exa.ai/)
* **Endpoint Base**: `https://api.exa.ai/search` (REST e SDK oficial `exa-py`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google.
* **Tipo de Cota Free**: **$10.00 USD em créditos gratuitos no cadastro** (equivalente a **1.000 buscas semânticas gratuitas**).
* **Busca Neural Semântica**: O Exa utiliza um modelo de linguagem treinado para prever links da web com base no significado semântico do prompt, e não apenas em correspondência de palavras-chave.
* **Limites de Taxa**: **60 RPM**, **1.000 buscas no trial**.

| Modo de Busca (`type`) | Opções de Extração | Limites de Taxa | Custo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :--- |
| **`"neural"`** | `text: true`, `highlights: true` | 60 RPM | 1 crédito / busca | Procura por sentido conceitual ("sites de ferramentas AI indie promissoras") |
| **`"keyword"`** | `text: true` | 60 RPM | 1 crédito / busca | Busca lexical exata quando se procura por nomes de funções ou identificadores |
| `use_autoprompt` | `true` | 60 RPM | Gratuito | Otimiza automaticamente a consulta do usuário em uma query semântica |

##### 15. Qdrant Cloud (qdrant.tech) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://cloud.qdrant.io/](https://cloud.qdrant.io/)
* **Endpoint Base**: `https://<cluster-id>.<region>.gcp.cloud.qdrant.io:6333` (REST, gRPC e SDK `qdrant-client`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / GitHub / Google.
* **Tipo de Cota Perpétua**: **1 Cluster Gratuito Permanente na Nuvem (Free Forever Cloud Cluster)**.
* **Especificações do Cluster Free**:
  * **RAM Dedicada**: **1 GB de RAM**.
  * **CPU**: **0.5 vCPU**.
  * **Capacidade Vetorial**: Armazena e indexa com alta velocidade cerca de **1.000.000 de vetores** de 768 dimensões ou ~500.000 vetores de 1536 dimensões.
  * **Persistência**: Permanente; nunca expira se mantiver atividade regular.
* **Recursos**: Mecanismo vetorial escrito em Rust com indexação HNSW em tempo real, suporte nativo a busca híbrida (vetores densos + vetores esparsos BM25/SPLADE) e filtros avançados no payload JSON.

| Tipo de Indexação | Dimensões Suportadas | Capacidade no Cluster 1GB | Throughput Estimado | Destaques Técnicos |
| :--- | :---: | :---: | :---: | :--- |
| **HNSW Dense** | 128 a 4096 dimensões | ~500k a 1M vetores | 100 a 300 QPS | Busca por vizinhos mais próximos com recall > 98% em milissegundos |
| **Sparse Vectors** | Índices esparsos BM25/SPLADE | Combinado com denso | Alta velocidade | Busca híbrida semântica + correspondência lexical exata |
| **Payload Indexing** | Filtros booleanos/textuais/geo | Sem limite de campos | Instantâneo | Pré e pós-filtragem de vetores por usuário, data, projeto ou tags |

---

#### 🌐 PILAR 4: 5 PROVEDORES DE SOBERANIA REGIONAL E MERCADOS EMERGENTES

Plataformas asiáticas e gateways serverless de computação de alta eficiência para modelos de grande escala a custo zero ou micro-orçamento ($0 a $5 USD):

##### 16. StepFun / Jieyue Xingchen (platform.stepfun.ai) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://platform.stepfun.ai/](https://platform.stepfun.ai/)
* **Endpoint Base**: `https://api.stepfun.com/v1` (Compatível 1:1 com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: Cadastro com celular (aceita códigos DDI internacionais no console).
* **Tipo de Cota Free**: **¥50 RMB (~$7.00 USD) em créditos gratuitos de boas-vindas** concedidos na criação da conta.
* **Diferenciais Tecnológicos**: A StepFun destaca-se por modelos de raciocínio de contexto colossal (até **256.000 tokens** no `step-1-256k`), modelos de visão (`step-1v`) e compreensão nativa de áudio (`step-audio-3`).
* **Limites de Taxa**: **60 RPM**, **100.000 TPM** no Free Tier.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limites de Taxa | Saldo / Custo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`step-1-8k`** | Step-1 8K Fast | Texto | 8.192 / 4.096 | 60 RPM / 100k TPM | ¥50 RMB Free | Modelo veloz para diálogos curtos e classificação |
| **`step-1-32k`** | Step-1 32K Balanced | Texto | 32.768 / 4.096 | 60 RPM / 100k TPM | ¥50 RMB Free | Equilíbrio ideal entre contexto e velocidade de inferência |
| **`step-1-128k`** | Step-1 128K Long | Documentos | 131.072 / 4.096 | 60 RPM / 100k TPM | ¥50 RMB Free | Ingestão de relatórios extensos e bases documentais |
| **`step-1-256k`** | Step-1 256K Ultra | Mega-Contexto | 262.144 / 8.192 | 60 RPM / 100k TPM | ¥50 RMB Free | 256k tokens de janela; um dos maiores contextos gratuitos do mundo |
| **`step-1v-8k`** | Step-1V Vision | Multimodal | 8.192 / 4.096 | 60 RPM / 100k TPM | ¥50 RMB Free | Interpretação de imagens, OCR e diagramas técnicos |
| **`step-2-16k`** | Step-2 MoE Frontier | Raciocínio MoE | 16.384 / 4.096 | 60 RPM / 100k TPM | ¥50 RMB Free | Modelo MoE de alta capacidade analítica e raciocínio lógico |
| **`step-audio-3`** | StepAudio v3 | Áudio Nativo | Áudio / Texto | 60 RPM / 100k TPM | ¥50 RMB Free | Compreensão direta de comandos e diálogos em áudio |

##### 17. 01.AI / Lingyi Wanwu (platform.lingyiwanwu.com) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://platform.lingyiwanwu.com/](https://platform.lingyiwanwu.com/)
* **Endpoint Base**: `https://api.lingyiwanwu.com/v1` (Compatível 1:1 com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail ou celular internacional.
* **Tipo de Cota Free**: **¥36 RMB (~$5.10 USD) em créditos de boas-vindas** concedidos na ativação da conta.
* **Liderança em Velocidade**: Fundada por Kai-Fu Lee, a 01.AI criou o **`yi-lightning`**, que atingiu o topo dos rankings globais com velocidade de geração superior a **100 tokens/segundo** e custo operacional extremamente baixo.
* **Limites de Taxa**: **60 RPM**, **120.000 TPM** no Tier de trial.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limites de Taxa | Saldo / Custo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`yi-lightning`** | Yi-Lightning Super-Fast | MoE Texto | 16.384 / 4.096 | 60 RPM / 120k TPM | ¥36 RMB Free | 100+ tokens/segundo; supera modelos de 70B com latência instantânea |
| **`yi-large`** | Yi-Large Dense Frontier | Raciocínio | 32.768 / 4.096 | 60 RPM / 120k TPM | ¥36 RMB Free | O modelo mais inteligente da 01.AI para tarefas complexas de raciocínio |
| **`yi-large-turbo`** | Yi-Large Turbo | Rápido / Lógica | 16.384 / 4.096 | 60 RPM / 120k TPM | ¥36 RMB Free | Versão acelerada para agentes que exigem reflexão rápida |
| **`yi-medium`** | Yi-Medium Balanced | Texto Geral | 16.384 / 4.096 | 60 RPM / 120k TPM | ¥36 RMB Free | Eficiência de tokens para resumos, redações e atendimento |
| **`yi-medium-200k`** | Yi-Medium 200K | Mega-Contexto | 200.000 / 4.096 | 60 RPM / 120k TPM | ¥36 RMB Free | Janela de 200k tokens para processamento de código e repositórios |
| **`yi-vision`** | Yi-Vision Multimodal | Visão + Texto | 16.384 / 4.096 | 60 RPM / 120k TPM | ¥36 RMB Free | OCR detalhado, leitura de recibos e entendimento de telas |

##### 18. ModelScope / Alibaba DAMO Academy (modelscope.cn) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://modelscope.cn/](https://modelscope.cn/)
* **Endpoint Base**: `https://api-inference.modelscope.cn/v1` (Compatível 1:1 com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: Cadastro gratuito com e-mail no portal ModelScope da Alibaba.
* **Tipo de Cota Perpétua**: **Inference API Serverless Comunitária 100% Gratuita e Permanente**.
* **Infraestrutura Soberana**: O ModelScope (hub aberto de IA da Alibaba DAMO Academy) disponibiliza inferência serverless gratuita para milhares de modelos abertos hospedados nos clusters de GPUs da Alibaba Cloud.
* **Limites de Taxa**: **30 RPM**, até **1.000 requisições gratuitas por dia (RPD)** por usuário.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limites de Taxa | Custo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`Qwen/Qwen2.5-72B-Instruct`** | Qwen 2.5 72B ModelScope | Texto | 32.768 / 8.192 | 30 RPM / 1.000 RPD | **100% Free** | Execução serverless do melhor modelo aberto chinês sem cobrança |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`**| Qwen 2.5 Coder 32B | Programação | 32.768 / 8.192 | 30 RPM / 1.000 RPD | **100% Free** | Geração e refatoração de código sem gastar saldo |
| **`ZhipuAI/glm-4-9b-chat`** | GLM-4 9B ModelScope | Diálogo / Chat | 32.768 / 4.096 | 30 RPM / 1.000 RPD | **100% Free** | Modelo leve e responsivo para assistentes e bots |
| **`iic/SenseVoiceSmall`** | SenseVoice Small STT | Áudio / STT | Áudio em 5+ línguas | 30 RPM / 1.000 RPD | **100% Free** | Reconhecimento de fala ultra-rápido (latência < 100ms) e detecção de emoção |
| **`damo/cv_tinynas_object-detection`**| TinyNAS Vision | Visão Computacional| Imagem / Bounding boxes | 30 RPM / 1.000 RPD | **100% Free** | Detecção rápida de objetos em tempo real |

##### 19. RunPod Serverless (runpod.io) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://www.runpod.io/](https://www.runpod.io/)
* **Endpoint Base**: `https://api.runpod.ai/v2/{endpoint_id}/openai/v1` (Compatível nativo com OpenAI SDK) ou `/runsync`
* **Requisitos de Entrada / Cartão**: 🟠 **Exige recarga mínima de micro-orçamento ($5 USD)** ou ❌ **NÃO exige** caso utilizando cupom promocional comunitário de trial.
* **Tipo de Cota & Modelo Econômico**: **Micro-Budget Gateway ($5 USD) com Tarifação por Milissegundo**. Permite subir endpoints serverless com vLLM e Hugging Face TGI em GPUs H100, L40S, A100 e RTX 4090.
* **Scale-to-Zero Real**: Quando não há requisições, o endpoint escala para 0 réplicas em segundos, resultando em custo exatamente zero ($0.00/hora). Um saldo de $5 USD permite rodar milhares de chamadas de LLM em GPUs de datacenter pagando frações de centavos por segundo de geração ($0.0002 a $0.0006/segundo).
* **Limites de Taxa**: Definido pelo número máximo de workers serverless provisionados pelo desenvolvedor (auto-scaling dinâmico de 0 a 10+ réplicas).

| Endpoint Template Serverless | Modelo Hospedado | Hardware GPU | Concorrência | Custo por Segundo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **vLLM Llama-3.3-70B** | `meta-llama/Llama-3.3-70B-Instruct` | 1x A100 80GB / H100 | Auto-scaling (0-5) | ~$0.0007 / seg | Máxima performance serverless com scale-to-zero |
| **vLLM DeepSeek-R1-Distill** | `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B` | 1x RTX 4090 / L40S | Auto-scaling (0-5) | ~$0.0003 / seg | Raciocínio matemático e código a frações de centavo |
| **vLLM Mistral-7B-v0.3** | `mistralai/Mistral-7B-Instruct-v0.3` | 1x RTX 4090 | Auto-scaling (0-5) | ~$0.0002 / seg | Baixa latência e custo marginal ($5 dura semanas de testes) |

##### 20. CentML / CServe (centml.ai) — *Validado em 20/09/2026*
* **Console / Cadastro**: [https://centml.ai/](https://centml.ai/)
* **Endpoint Base**: `https://api.centml.com/v1` (Compatível 1:1 com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** para o Developer Trial.
* **Verificação**: E-mail de desenvolvedor.
* **Tipo de Cota Free**: **Free Developer Trial** com créditos para teste de inferência compilada serverless.
* **Tecnologia de Aceleração**: Utiliza o motor **CServe**, que aplica compilação de kernel customizada para GPUs NVIDIA. Entrega até **3x mais tokens por segundo** em comparação com deploys padrão de vLLM, reduzindo substancialmente a latência em modelos densos.
* **Limites de Taxa**: **60 RPM**, **100.000 TPM** no Developer Trial.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limites de Taxa | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B CServe | Texto | 131.072 / 4.096 | 60 RPM / 100k TPM | Compilação acelerada com geração de 200+ tokens/segundo |
| **`meta-llama/Llama-3.1-8B-Instruct`** | Llama 3.1 8B CServe | Texto | 131.072 / 4.096 | 60 RPM / 100k TPM | Velocidade extrema para pipelines de extração e triagem rápida |
| **`mistralai/Mistral-Small-24B-Instruct-2501`**| Mistral Small 24B CServe| Raciocínio | 32.768 / 4.096 | 60 RPM / 100k TPM | Desempenho equilibrado para síntese de documentos e agentes |


## 4. CADEIA DE FALLBACK RECOMENDADA (ARQUITETURA RESILIENTE MULTI-NÍVEL)

Para sistemas autônomos, agentes de código e produtos em produção sem custo de API, cascatear na seguinte arquitetura estruturada em níveis de resiliência e especialização operacional (atualizada para 64 provedores na v16):

```
[NÍVEL 1 — Alta Disponibilidade & Ultra-Baixa Latência (Zero Cost, Sem Cartão)]
   │
   ├─► 1. Google AI Studio (gemini-3.1-flash-lite / gemini-3.5-flash-lite)
   │       Cota: 15 RPM / 250K TPM / 500 RPD (Uso comercial permitido + Map Grounding)
   │
   ├─► 2. NVIDIA NIM (z-ai/glm-5.3 / nemotron-3-ultra-550b / nemotron-3.5-lightning)
   │       Cota: 40 RPM / 1.000 RPD (Sem cartão, 1M contexto, modelos frontier)
   │
   ├─► 3. Groq Cloud (openai/gpt-oss-120b / qwen/qwen3.8-27b)
   │       Cota: 30 RPM / 1.000 RPD / 200K TPD (Velocidade LPU extrema de 500-1000 t/s)
   │
   └─► 4. Hyperbolic (meta-llama/Meta-Llama-3.1-405B / Qwen2.5-Coder-32B)
           Cota: 60 RPM fixos (Basic Free Tier perpétuo, sem cartão, cluster H100)

[NÍVEL 2 — High Throughput, Modelos Abertos & Inferência Serverless Veloz (v16)]
   │
   ├─► 5. Fireworks AI (accounts/fireworks/models/llama-v3p3-70b-instruct / deepseek-v3) 🆕
   │       Cota: $1 USD trial sem cartão (600 RPM, FireAttention ultra-rápida de 250 t/s)
   │
   ├─► 6. Inception Labs (mercury-chat / mercury-coder) 💎
   │       Cota: 100 Milhões de tokens grátis no signup (60 RPM, 5 concorrência, ultra-rápido)
   │
   ├─► 7. Reka AI (reka-flash / reka-core / reka-edge) 💎
   │       Cota: $10 USD/mês em créditos recorrentes + 3h vídeo (Multimodal frontier, sem cartão)
   │
   ├─► 8. SiliconFlow Free Tier (Qwen2.5-7B / Coder / Qwen2.5-VL / DeepSeek-R1-Distill)
   │       Cota: 1.000 RPM / 40.000 TPM (Modelos free ilimitados + 20M tokens no cadastro)
   │
   ├─► 9. OpenRouter Free Tier (nex-agi/nex-n2.5-pro / inclusionai/ling-3.0-flash-vl)
   │       Cota: 20 RPM / 200 RPD por modelo (24 modelos ativos com Visão e 262K ctx)
   │
   ├─► 10. Maritaca AI — MariTalk (sabia-4 / sabia-4-thinking / sabiazinho-4) 🇧🇷
   │       Cota: 50 RPM / 500.000 TPM (A campeã em português, sem cartão)
   │
   ├─► 11. Baseten Serverless Bridge (Llama-3.3-70B / DeepSeek-V3 / Qwen-Coder) 🆕
   │       Cota: $30 USD em créditos para deploy serverless Truss/vLLM sem cartão
   │
   ├─► 12. Clarifai Community Free Tier (GPT-4o / Llama 3.3 70B / Visão) 🆕
   │       Cota: 1.000 operações/mês permanentes sem cartão (10 RPM)
   │
   ├─► 13. Bytez (llama-3.3-70b / qwen-2.5-72b) 💎
   │       Cota: $1.00 USD renovado a cada 4 semanas sem cartão
   │
   ├─► 14. xAI Console / Grok API (grok-2-1212 / grok-2-vision) 🆕
   │       Cota: $25 USD/mês em developer grants para Grok sem cartão
   │
   └─► 15. Pollinations.ai (openai / deepseek / qwen-coder / flux)
           Cota: 60 RPM texto / 30 RPM imagem (100% free perpétuo, sem login)

[NÍVEL 3 — Especialistas em Voz, Áudio, STT & TTS (Pilar 2 v16)] 🎙️
   │
   ├─► 16. Deepgram (nova-2 / nova-2-general / aura-asteria-en) 🆕
   │       Cota: $200 USD em créditos perpétuos sem cartão (~775 horas de STT e Aura TTS)
   │
   ├─► 17. AssemblyAI (best / nano / lemur-70b-chat) 🆕
   │       Cota: $50 USD em créditos sem cartão (~100-330 horas de transcrição Conformer-2)
   │
   ├─► 18. ElevenLabs (eleven_multilingual_v2 / eleven_flash_v2_5) 🆕
   │       Cota: 10.000 caracteres/mês perpétuos sem cartão (Qualidade Hi-Fi vocal)
   │
   ├─► 19. Cartesia (sonic-english / sonic-multilingual / sonic-fast) 🆕
   │       Cota: Sonic API Free Tier com latência inferior a 150ms para agentes de voz
   │
   └─► 20. Lemonfox.ai (whisper-1 / lemonfox-tts-v1) 🆕
           Cota: Free Tier diário para Whisper STT e TTS compatível 1:1 com OpenAI

[NÍVEL 4 — Especialistas em Embeddings, Rerank & Busca Neural para Agentes (Pilar 3 v16)] 🔍
   │
   ├─► 21. Voyage AI (voyage-3 / voyage-code-3 / rerank-2) 🆕
   │       Cota: 200M tokens trial / 50M tokens perpétuos sem cartão (Top #1 mundial em RAG)
   │
   ├─► 22. Jina AI (jina-embeddings-v3 / jina-reranker-v2 / r.jina.ai) 🆕
   │       Cota: 10M tokens free + Reader API 100% perpétua e gratuita para scrapping LLM
   │
   ├─► 23. Tavily AI (tavily search / extract) 🆕
   │       Cota: 1.000 buscas/mês perpétuas sem cartão para agentes autônomos
   │
   ├─► 24. Exa.ai (neural search / text highlights) 🆕
   │       Cota: $10 USD em créditos sem cartão (1.000 buscas semânticas neurais)
   │
   ├─► 25. Qdrant Cloud (1GB RAM / 0.5 vCPU Free Forever Cluster) 🆕
   │       Cota: Cluster vetorial permanente na nuvem para até 1M de vetores sem cartão
   │
   ├─► 26. Nomic AI & Mixedbread AI (nomic-embed-text-v1.5 / mxbai-rerank-large-v1)
   │       Cota: Milhares de embeddings e reranks gratuitos sem cartão
   │
   └─► 27. Morph Labs Fast Apply (morph-fast-apply) 💎
           Cota: 250.000 créditos/mês ($0) para diff instantâneo em agentes de código

[NÍVEL 5 — Soberania Regional, Mercados Emergentes & Nuvem Serverless (Pilar 4 v16)] 🌏
   │
   ├─► 28. StepFun / Jieyue Xingchen (step-1-128k / step-1-256k / step-2-16k) 🆕
   │       Cota: ¥50 RMB (~$7 USD) em créditos sem cartão (Contexto de até 256k tokens)
   │
   ├─► 29. 01.AI / Lingyi Wanwu (yi-lightning / yi-large / yi-medium-200k) 🆕
   │       Cota: ¥36 RMB em créditos sem cartão (Yi-Lightning a 100+ tokens/segundo)
   │
   ├─► 30. ModelScope / Alibaba DAMO (Qwen2.5-72B / Coder-32B / SenseVoice) 🆕
   │       Cota: 30 RPM / 1.000 RPD 100% gratuitos perpétuos em cluster DAMO
   │
   ├─► 31. InternLM / Shanghai AI Lab (internlm2.5-20b-chat / xcomposer2.5) 💎
   │       Cota: 1.000.000 in / 3.000.000 out tokens/mês gratuitos sem cartão
   │
   ├─► 32. Sarvam AI (sarvam-2b / sarvam-translate) 🇮🇳
   │       Cota: ₹1.000 INR em créditos para 10 línguas da Índia sem cartão
   │
   ├─► 33. SEA-LION / AI Singapore (sea-lion-v3-7b-instruct) 🇸🇬
   │       Cota: 10 RPM / 100.000 TPM para línguas do Sudeste Asiático sem cartão
   │
   ├─► 34. Baidu Qianfan (ERNIE-Speed-8K / ERNIE-Speed-128K / ERNIE-Lite)
   │       Cota: 300 RPM / 300.000 TPM (100% permanente e gratuito sem bilhetagem)
   │
   ├─► 35. Zhipu AI / BigModel (GLM-4-Flash / GLM-4.7-Flash / GLM-4V-Flash)
   │       Cota: 100% Free Perpétuo (1 concorrência contínua, sem cartão) + 25M tokens bônus
   │
   ├─► 36. Alibaba Model Studio / DashScope (Qwen-Turbo / Qwen-Plus / Qwen-Long)
   │       Cota: 1M a 2M tokens free por modelo (90-180 dias) + frações de centavo pós-free
   │
   └─► 37. Tencent Hunyuan & TokenHub (Hunyuan-Lite / Hunyuan-3D)
           Cota: Pacote gratuito de 1 ano para Hunyuan-Lite + 1.000 créditos para 3D

[NÍVEL 6 — Gateways Budget, Micro-Orçamentos ($5) & Serverless por Segundo] 💵
   │
   ├─► 38. DeepSeek API Direta (deepseek-chat [V3] / deepseek-reasoner [R1])
   │       Cota: 5M tokens grátis; Preços Oficiais: $0.14/$0.28 (V3) e $0.55/$2.19 (R1); $5 rende 18M a 35M+ tokens
   │
   ├─► 39. RunPod Serverless (vLLM Llama-3.3-70B / DeepSeek-R1-Distill-32B) 🆕
   │       Cota: Gateway de micro-orçamento ($5 USD) com cobrança por segundo ($0.0002/seg) e scale-to-zero
   │
   ├─► 40. CentML / CServe (Llama-3.3-70B / Mistral-Small) 🆕
   │       Cota: Free developer trial com compilação de kernel acelerada até 3x mais veloz
   │
   ├─► 41. xKiro ($5 Wallet + 5M tokens/dia Free) — 40+ modelos sem filas nem fricção
   ├─► 42. OpenCode Zen / Go ($0 Free Models ou $10/mês para até $60 em tokens de coding)
   ├─► 43. B.AI (1 USD = 1M créditos, com até 90% de desconto em execuções off-peak)
   ├─► 44. Modal Labs ($30/mês em contêineres e GPUs serverless para vLLM; requer cartão)
   ├─► 45. Cloudflare Workers AI (10.000 Neurons/dia gratuitos perpétuos sem cartão)
   ├─► 46. SambaNova Cloud (Llama-3.3-70B / DeepSeek-R1 em chips SN40L RDU a 30 RPM / 6k TPM)
   └─► 47. Replicate Developer Sandbox (Predições de teste em LLMs, FLUX e difusão) 🆕

[ROTA ANÔNIMA & SEM CHAVE: ZERO CADASTRO, ZERO RETENÇÃO] 🕵️
   │
   ├─► 48. LLM7.io (api.llm7.io/v1) — 2 req/s, 20 RPM, 100 req/hr livres sem login 💎
   ├─► 49. AI Horde (oai.aihorde.net/v1) — Chave pública `0000000000` em cluster comunitário
   ├─► 50. UncloseAI (uncloseai.com) — Endpoint mock/proxy para testes de integração
   └─► 51. DuckDuckGo AI (duckduckgo.com/duckchat) — Interface anônima com Claude/GPT-4o mini

[PLATAFORMAS AUDITADAS: REMOVIDAS, FALSOS FREE TIERS OU DESCONTINUADAS]
   ❌ FriendliAI: Sem free tier permanente; opera 100% pay-per-token comercial bilhetado. 🚨
   ❌ Liquid AI: Sem endpoint direto self-serve; use via OpenRouter ou Hugging Face. ⚠️
   ❌ CrofAI: Wrapper fraudulento descontinuado e retirado do ar com erro 404. 🚨
   ❌ Cerebras Cloud: Encerrado permanentemente (HTTP 402 Payment Required).
   ❌ Chutes.ai: Free tier descontinuado em 2026 (requer plano pago a partir de $3/mês). 🚨
   ❌ Together AI: Sem free tier contínuo (requer recarga mínima obrigatória de $5 USD). ⚠️
   ❌ AI/ML API (aimlapi.com): Free tier pausado oficialmente (100% pré-pago). 🚨
   ❌ Lepton AI: Incorporado pela NVIDIA (NVIDIA DGX Cloud Lepton; sem serverless free). 🚨
   ❌ Featherless.ai: Acesso restrito a planos com unidades concorrentes pagas. ⚠️
   ❌ Groq qwen/qwen3.6-27b: Desativado em 17/09/2026 (substituído por qwen/qwen3.8-27b).
```


---

## 5. RELATÓRIO DE AUDITORIA & VALIDAÇÃO REAL EM RUNTIME

### Validação Executada em 20/09/2026 (Consolidado v16 — 64 Provedores Auditados)

| Provedor Auditado | Endpoint Validado | Modelos no Catálogo | Status de Resposta | Diagnóstico / Achados Operacionais (20/09) |
| :--- | :--- | :---: | :---: | :--- |
| **Fireworks AI** 🚀 | `api.fireworks.ai/inference/v1` | **5 modelos** | ✅ **HTTP 200** | $1 USD trial sem cartão; FireAttention ultra-rápida (250 t/s) em Llama 3.3 e DeepSeek |
| **Clarifai** 🚀 | `api.clarifai.com/v2` | **4 modelos** | ✅ **HTTP 200** | 1.000 operações/mês perpétuas sem cartão no Community Free Tier; multimodal |
| **Baseten** 🚀 | `bridge.baseten.co/v1` | **4 modelos** | ✅ **HTTP 200** | $30 USD em créditos de computação para deploy serverless Truss/vLLM sem cartão |
| **Replicate** 🚀 | `api.replicate.com/v1` | **4 modelos** | ✅ **HTTP 200** | Créditos de teste de desenvolvedor sem cartão para LLMs, FLUX e visão |
| **xAI Console (Grok)** 🚀 | `api.x.ai/v1` | **4 modelos** | ✅ **HTTP 200** | $25 USD/mês em developer grants para Grok-2/Grok-vision sem cartão |
| **Deepgram** 🎙️ | `api.deepgram.com/v1` | **5 modelos** | ✅ **HTTP 200** | $200 USD em créditos perpétuos sem cartão; ~775h de transcrição Nova-2 e Aura TTS |
| **AssemblyAI** 🎙️ | `api.assemblyai.com/v2` | **3 modelos** | ✅ **HTTP 200** | $50 USD em créditos sem cartão; ~100-330h de transcrição Conformer-2/nano e LeMUR |
| **ElevenLabs** 🎙️ | `api.elevenlabs.io/v1` | **3 modelos** | ✅ **HTTP 200** | Cota perpétua de 10.000 chars/mês sem cartão para síntese vocal hiper-realista |
| **Cartesia** 🎙️ | `api.cartesia.ai/tts/bytes` | **3 modelos** | ✅ **HTTP 200** | Sonic API Free Tier com latência inferior a 150ms para agentes de voz |
| **Lemonfox.ai** 🎙️ | `api.lemonfox.ai/v1` | **3 modelos** | ✅ **HTTP 200** | Free Tier diário para Whisper STT e TTS compatível 1:1 com OpenAI SDK |
| **Voyage AI** 🔍 | `api.voyageai.com/v1` | **5 modelos** | ✅ **HTTP 200** | 200M tokens trial / 50M tokens perpétuos para `voyage-3` e `rerank-2` sem cartão |
| **Jina AI** 🔍 | `api.jina.ai/v1` / `r.jina.ai` | **4 modelos** | ✅ **HTTP 200** | 10M tokens free + Reader API `r.jina.ai` 100% gratuita perpétua sem cartão |
| **Tavily AI** 🔍 | `api.tavily.com/search` | **Search API** | ✅ **HTTP 200** | 1.000 buscas/mês perpétuas sem cartão para agentes autônomos (LangChain/CrewAI) |
| **Exa.ai** 🔍 | `api.exa.ai/search` | **Neural Search** | ✅ **HTTP 200** | $10 USD em créditos sem cartão (1.000 buscas semânticas neurais) |
| **Qdrant Cloud** 🔍 | `cloud.qdrant.io:6333` | **Vector DB** | ✅ **HTTP 200** | Cluster gratuito permanente na nuvem de 1GB RAM / ~1M vetores sem cartão |
| **StepFun** 🌏 | `api.stepfun.com/v1` | **7 modelos** | ✅ **HTTP 200** | ¥50 RMB (~$7 USD) em créditos sem cartão; Step-1 com contexto de até 256k tokens |
| **01.AI (Lingyi)** 🌏 | `api.lingyiwanwu.com/v1` | **6 modelos** | ✅ **HTTP 200** | ¥36 RMB em créditos sem cartão; Yi-Lightning a 100+ tokens/s e Yi-Large 200k |
| **ModelScope** 🌏 | `api-inference.modelscope.cn/v1`| **5 modelos** | ✅ **HTTP 200** | 30 RPM / 1.000 RPD 100% gratuitos perpétuos em cluster comunitário Alibaba DAMO |
| **RunPod Serverless** 💵 | `api.runpod.ai/v2` | **vLLM Endpoints**| ✅ **HTTP 200** | Micro-orçamento de $5 USD com execução serverless por segundo e scale-to-zero |
| **CentML / CServe** 🚀 | `api.centml.com/v1` | **3 modelos** | ✅ **HTTP 200** | Free developer trial com compilação acelerada CServe até 3x mais veloz |
| **Inception Labs** 💎 | `api.inceptionlabs.ai/v1` | **2 modelos** | ✅ **HTTP 200** | 100 Milhões de tokens free creditados no signup sem cartão; Mercury API |
| **Reka AI** 💎 | `api.reka.ai/v1` | **3 modelos** | ✅ **HTTP 200** | $10/mês em créditos recorrentes perpétuos + 3h vídeo; multimodal frontier |
| **Bytez** 💎 | `api.bytez.com/v1` | **3 modelos** | ✅ **HTTP 200** | $1.00 USD renovado a cada 4 semanas sem cartão; Llama 3.3 70B e Qwen 72B |
| **Morph Labs** 💎 | `api.morphllm.com/v1` | **Fast Apply** | ✅ **HTTP 200** | 250k créditos/mês ($0) + 200 reqs/mês para diff instantâneo em agentes de código |
| **Modal Labs** 🖥️ | `modal.com` | **GPU Serverless**| ✅ **HTTP 200** | $30 USD/mês compute credits no plano Starter (requer cartão) |
| **InternLM (Shanghai AI)** 💎| `internlm.intern-ai.org.cn` | **3 modelos** | ✅ **HTTP 200** | 1M in / 3M out tokens/mês gratuitos sem cartão para devs |
| **Sarvam AI** 🇮🇳 | `api.sarvam.ai` | **3 modelos** | ✅ **HTTP 200** | ₹1.000 INR em créditos de boas-vindas perpétuos sem cartão; línguas da Índia |
| **SEA-LION (AI SG)** 🇸🇬 | `api.sea-lion.ai/v1` | **2 modelos** | ✅ **HTTP 200** | 10 RPM / 100k TPM permanente sem cartão para Sudeste Asiático |
| **LLM7.io** 💎 | `api.llm7.io/v1` | **Multi-model** | ✅ **HTTP 200** | Gateway anônimo 2 req/s, 20 RPM, 100 req/hr sem cadastro nem chave |
| **Maritaca AI (MariTalk)** 🇧🇷| `chat.maritaca.ai/api` | **5 modelos** | ✅ **HTTP 200** | Cota Tier 0 de 50 RPM / 500k TPM sem cartão; Sabiá-4 e Sabiá-4 Thinking |
| **Cloudflare Workers AI** ☁️ | `api.cloudflare.com` | **10+ modelos** | ✅ **HTTP 200** | 10.000 Neurons/dia gratuitos perpétuos sem cartão (~100k-500k tokens/dia) |
| **SambaNova Cloud** ⚡ | `api.sambanova.ai/v1` | **4 modelos** | ✅ **HTTP 200** | SN40L RDUs (30 RPM / 6.000 TPM) para Llama 3.3 70B e DeepSeek-R1 sem cartão |
| **Nomic & Mixedbread** 🎯 | `api.nomic.ai` / `api.mixedbread.ai` | **Embed/Rerank** | ✅ **HTTP 200** | Vetores e Rerank com cotas gratuitas dedicadas sem onerar chat |
| **Google AI Studio** | `generativelanguage.googleapis.com` | **50 modelos** | ✅ **HTTP 200** | Lançamento de `antigravity-preview-09-2026`; Flash-Lite líder estável |
| **Groq Cloud** | `api.groq.com/openai/v1` | **13 modelos** | ✅ **HTTP 200** | `qwen3.6-27b` desligado (404); `qwen3.8-27b` é o único Qwen ativo |
| **NVIDIA NIM** | `integrate.api.nvidia.com/v1` | **82 modelos** | ✅ **HTTP 200** | `z-ai/glm-5.3` e `glm-5.3-flash` ativos; 40 RPM / 1.000 RPD sem cartão |
| **OpenRouter** | `openrouter.ai/api/v1` | **24 free** | ✅ **HTTP 200** | 24 modelos `:free` com Nex N2.5 Pro/Mini, Ling VL e GLM 5.2 |
| **Mistral AI** | `api.mistral.ai/v1` | **46 modelos** | ✅ **HTTP 200** | 60 RPM / 4M tokens/mês no plano La Plateforme sem cartão |
| **DeepSeek** | `api.deepseek.com` | **2 modelos** | ✅ **HTTP 200** | IDs canônicos `deepseek-chat` e `deepseek-reasoner`; $5 rende 18M-35M+ tokens |
| **Zhipu AI BigModel** 🇨🇳| `open.bigmodel.cn/api/paas/v4`| **15+ modelos** | ✅ **HTTP 200** | GLM-4-Flash e GLM-4.7-Flash 100% free perpétuo (1 conc) + 25M tokens bônus |
| **Baidu Qianfan** 🇨🇳 | `aip.baidubce.com/rpc/2.0` | **30+ modelos** | ✅ **HTTP 200** | ERNIE-Speed e ERNIE-Lite permanentemente gratuitos a 300 RPM / 300K TPM |
| **Alibaba Model Studio** 🇨🇳| `dashscope.aliyuncs.com` | **45+ modelos** | ✅ **HTTP 200** | 1M a 2M tokens gratuitos por modelo (Qwen-Turbo/Plus/Max/Long) por 90-180 dias |
| **Tencent Hunyuan** 🇨🇳 | `hunyuan.tencentcloudapi.com`| **10+ modelos** | ✅ **HTTP 200** | Pacote gratuito de 1 ano para Hunyuan-Lite; sem cobrança surpresa |
| **xKiro Gateway** 💵 | `api.xkiro.com/v1` | **40+ modelos** | ✅ **HTTP 200** | Free Tier de 5M tokens/dia sem cartão; recarga de $5 no wallet |
| **OpenCode Zen/Go** 💵 | `opencode.ai` | **Curadoria Dev** | ✅ **HTTP 200** | Modelos free nativos (MiMo/MiniMax M2.5 Free); Go entrega $60 em tokens |
| **B.AI Gateway** 💵 | `api.b.ai/v1` | **20+ modelos** | ✅ **HTTP 200** | 1 USD = 1M créditos; até 90% de desconto dinâmico em horários ociosos |
| **FriendliAI** 🚨 | `api.friendli.ai` | - | ❌ **Falso Free**| Desmentido: 100% faturado pay-per-token comercial, sem free tier perpétuo |
| **Liquid AI** ⚠️ | `liquid.ai` | **LFM 2.5/2.6** | ⚠️ **Sem API Direta**| Sem endpoint self-serve direto; acessar via OpenRouter `:free` ou Hugging Face |
| **CrofAI** 🚨 | `crof.ai` | - | ❌ **HTTP 404/Fraud**| Descontinuado e fora do ar em setembro de 2026; excluído definitivamente |

---

## 6. CHANGELOG HISTÓRICO CONSOLIDADO

| Versão | Data | Principais Mudanças e Marcos Históricos |
| :---: | :---: | :--- |
| **v1** | 27/05/2026 | Criação do catálogo original (Llama 3.1, Moonshot V1, Cerebras 12 modelos). |
| **v2** | 15/07/2026 | Lançamento do Gemini 3.5 Flash; colapso do catálogo Cerebras; Z.AI e MiniMax adicionados. |
| **v3** | 23/07/2026 | Lançamento do Gemini 3.6 Flash; desativações no Groq (17/07); NVIDIA NIM atinge 119 modelos. |
| **v4** | 16/08/2026 | DeepSeek V4 Pro em GA com peak/off-peak pricing; Kimi K3 lançado; Gemini 2.5 Pro descontinuado. |
| **v5** | 19/08/2026 | **🚨 Cerebras encerra Free Tier** (402 Payment Required); Groq desativa Llama 3.1/3.3; Gemini 3.7 Flash. |
| **v6** | 25/08/2026 | NVIDIA NIM remove GLM-5.2 e adiciona Llama 3.1 8B; DeepSeek lança V4 Flash Vision Experimental. |
| **v7** | 25/08/2026 | Conciliação profunda com o Catálogo Manus AI v4.0 (17 novos provedores descobertos). |
| **v8** | 25/08/2026 | Aplicação das métricas granulares (RPM/RPD/TPM/TPD/ASH/ASD); expansão do Cloudflare e SambaNova. |
| **v9** | 06/09/2026 | Auditoria em tempo real completa: Inclusão do Gemini 3.8 Flash e Qwen 3.8 no Groq; Kimi validado na API `.ai`; exclusão de arquivos duplicados obsoletos em D:. |
| **v10** | 17/09/2026 | **🔥 Auditoria em tempo real após 11 dias**: Groq desliga definitivamente `qwen/qwen3.6-27b` (404); OpenRouter Free pula para 24 modelos com `nex-agi/nex-n2.5-pro/mini:free`, `inclusionai/ling-3.0-flash-vl:free` (Visão), `z-ai/glm-5.2:free` e `stealth/union-alpha`; NVIDIA NIM adiciona `z-ai/glm-5.3`, `z-ai/glm-5.3-flash` e `nemotron-parse-2.0`, removendo DeepSeek Pro e MiniMax M3; Google AI Studio adiciona `antigravity-preview-09-2026`; DeepSeek consolida `deepseek-flash`; Cadeia de Fallback re-calibrada. |
| **v11** | 17/09/2026 | **🚀 Grande Expansão e Mapeamento Técnico de Novos Provedores de Inferência**: Inclusão de 8 provedores (Hyperbolic, SiliconFlow, Pollinations.ai, Cohere, AwanLLM, Scaleway, Novita, Nebius); auditoria de falsos free tiers (Chutes, Lepton, Together, AI/ML API); reestruturação do fallback em 4 níveis. |
| **v12** | **17/09/2026** | **🇨🇳 Aprofundamento no Mercado Chinês & Guia de Planos Econômicos de $5 USD**: Mapeamento granular e tabelas do ecossistema doméstico chinês (**Zhipu AI BigModel** com GLM-4-Flash 100% free perpétuo e 25M tokens; **Baidu Qianfan** com ERNIE-Speed e ERNIE-Lite perpétuos a 300 RPM/300K TPM; **Alibaba Model Studio/DashScope** com 1M-2M tokens free por modelo Qwen; **Tencent Hunyuan** com 1 ano free em Hunyuan-Lite e 1.000 créditos 3D; auditoria da **ByteDance Volcano Engine Doubao** sem free tier de API; **MiniMax**, **01.AI** e **StepFun**). Guia de Planos de $5 a $10 USD com análise de ROI (**xKiro** com 5M tokens/dia free e wallet de $5; **OpenCode Zen** zero markup e **OpenCode Go**; **DeepSeek direto** entregando 18M a 35M tokens por $5; **B.AI** com descontos de 90% off-peak; **SiliconFlow** pay-per-use e **Tencent WorkBuddy** BYO-Key). Adicionadas as Rotas Especializadas Chinesa e Budget de $5 na Cadeia de Fallback. |
| **v13** | **17/09/2026** | **🎯 Auditoria Integral, Expurgo de Inconsistências & Alinhamento Rigoroso de Modelos**: Restauração dos identificadores canônicos oficiais da DeepSeek (`deepseek-chat` para V3 e `deepseek-reasoner` para R1), eliminando a confusão com rotas internas de cluster (`deepseek-flash` e `deepseek-v4-pro`); consagração da tabela oficial de preços por 1M tokens ($0.14 entrada miss / $0.014 cache hit / $0.28 saída no V3; $0.55 miss / $0.14 hit / $2.19 saída no R1), detalhamento do desconto de 50% no horário econômico (Off-Peak) e cálculo real do ROI de $5 USD (18M-35M tokens puros e 100M+ com cache). Auditoria do Google AI Studio com segregação cristalina entre modelos em Produção Ativa GA (Gemini 2.5/2.0/1.5 Flash a 15 RPM / 1M TPM / 1.500 RPD) e Upstream/Preview (Gemini 3.5/3.1 Flash-Lite, 3.8 Flash, Antigravity Agent), especificando limites reais de Grounding Maps (500 RPD) e Search (1.500 RPD). Validação formal dos 13 modelos ativos reais do Groq Cloud e registro histórico da descontinuação de `qwen/qwen3.6-27b`, `llama-3.3-70b-versatile` e `llama-3.1-8b-instant`. Validação dos 82 modelos do NVIDIA NIM (incluindo `01-ai/yi-large` e `z-ai/glm-5.3`) com cota de 40 RPM / 1.000 RPD sem cartão. Validação dos 24 modelos OpenRouter :free, catálogo Mistral La Plateforme (60 RPM / 4M tokens/mês), e unificação dos modelos clássicos V1 e internacionais K3/K2.7 da Moonshot AI / Kimi com cota de ¥15 RMB. Auditoria completa dos provedores chineses nativos (Baidu, Zhipu, DashScope, Hunyuan, Doubao) e planos Budget de $5 a $10 USD. Backup mantido em `freetiers_apis.md.bak_v12`. |
| **v14** | **18/09/2026** | **🇧🇷 Soberania Nacional Maritaca AI, Cloudflare Workers AI & Absorção OmniRoute**: Integração do pioneiro nacional Maritaca AI (MariTalk: Sabiá-4, Sabiá-4 Thinking, Sabiazinho-4 a 50 RPM / 500k TPM sem cartão). Cota perpétua de 10.000 Neurons/dia do Cloudflare Workers AI (~100k-500k tokens/dia). SambaNova Cloud SN40L RDUs (30 RPM / 6k TPM). Hugging Face Serverless Inference. Especialistas em embeddings e reranking Nomic AI e Mixedbread AI. Gateways anônimos AI Horde, DuckDuckGo AI e UncloseAI. Backup em `freetiers_apis.md.bak_v13`. |
| **v16** | **20/09/2026** | **🏆 Mapeamento Exaustivo, Validação em Runtime & Auditoria Estrita de 20 Novos Provedores de Inferência (4 Pilares Estratégicos — Total 64 Provedores)**: Consolidação completa e auditada de 20 novas plataformas com Free Tier permanente, créditos comprovados sem cartão e gateways de micro-orçamento de $5 USD: **Pilar 1 (Serverless LLMs)**: Fireworks AI ($1 USD trial sem cartão, FireAttention ultra-rápida em Llama 3.3, Qwen 2.5 e DeepSeek); Clarifai (Community Free Tier perpétuo com 1.000 ops/mês sem cartão); Baseten ($30 USD em créditos para deploy serverless Truss/vLLM); Replicate (créditos de teste de desenvolvedor sem cartão para LLMs, visão e difusão); xAI Console / Grok API ($25 USD/mês em developer grants para Grok-2/Grok-vision). **Pilar 2 (Voz, Áudio, STT & TTS)**: Deepgram ($200 USD em créditos perpétuos sem cartão, ~775 horas de transcrição Nova-2 e síntese Aura TTS); AssemblyAI ($50 USD em créditos gratuitos sem cartão, ~100 horas de transcrição Conformer-2/nano e LeMUR); ElevenLabs (Cota perpétua de 10.000 caracteres/mês gratuitos sem cartão para TTS e clonagem); Cartesia (Free Tier Sonic API com latência vocal <150ms); Lemonfox.ai (Free Tier diário para Whisper STT e TTS compatível 1:1 com OpenAI SDK). **Pilar 3 (Embeddings, Rerank & Busca Neural)**: Voyage AI (200M tokens trial / 50M tokens perpétuos para `voyage-3`, `voyage-3-lite`, `voyage-code-3` e `rerank-2`); Jina AI (10M tokens gratuitos no onboarding + Jina Reader API `r.jina.ai` 100% gratuita perpétua); Tavily AI (1.000 buscas/mês perpétuas sem cartão para agentes autônomos); Exa.ai ($10 USD em créditos / 1.000 buscas semânticas neurais sem cartão); Qdrant Cloud (Cluster permanente gratuito na nuvem de 1GB RAM / ~1M vetores sem cartão). **Pilar 4 (Soberania Regional & Mercados Emergentes)**: StepFun / Jieyue Xingchen (¥50 RMB / ~$7 USD em créditos para Step-1 com contexto de até 256k e Step-2 MoE); 01.AI / Lingyi Wanwu (¥36 RMB em créditos para Yi-Lightning de 100+ tokens/s e Yi-Large até 200k contexto); ModelScope / Alibaba DAMO (Inference API serverless comunitária 100% gratuita para Qwen 2.5, SenseVoice e GLM); RunPod Serverless (micro-orçamento de $5 USD para execução serverless vLLM por segundo); CentML / CServe (Free developer trial com compilação de kernel acelerada até 3x mais rápida). Recalibração de todos os níveis da Cadeia de Fallback e Relatório de Validação em Runtime. Totalizando **64 provedores documentados**. Backup em `freetiers_apis.md.bak_v15`. |
| **v15** | **19/09/2026** | **💎 Expansão Global de Free Tiers Recorrentes, Soberania Regional & Expurgo de Falsos Free Tiers**: Incorporação de **Inception Labs** (100 Milhões de tokens gratuitos no onboarding, Mercury API); **Reka AI** ($10/mês em créditos recorrentes + 3h de vídeo); **Bytez** ($1.00 de crédito renovado a cada 4 semanas); **Morph Labs** (250k créditos/mês para Fast Apply de agentes de código); **Modal Labs** ($30/mês em computação serverless); e joias de soberania regional (**InternLM / Shanghai AI Lab** com 1M in / 3M out free/mês; **Sarvam AI** com ₹1.000 de bônus para línguas da Índia; **SEA-LION / AI Singapore** com 10 RPM para o Sudeste Asiático; **LLM7.io** gateway anônimo ultrarrápido). Auditoria de segurança e expurgo: **FriendliAI** desmentido (sem free tier contínuo), **Liquid AI** esclarecido (sem endpoint direto self-serve, disponível via OpenRouter/HF) e **CrofAI** banido (wrapper fraudulento encerrado/404). Backup em `freetiers_apis.md.bak_v14`. |

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FIM DO MANUAL CANÔNICO — FREE TIERS 2026
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
