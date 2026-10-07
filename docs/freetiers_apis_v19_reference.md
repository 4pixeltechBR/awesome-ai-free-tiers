# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MANUAL DE CONSULTA: FREE TIERS DE LLM & POLÍTICAS DE USO (Outubro 2026)
# Compilação e Revisão de Fatos: 07 de outubro de 2026 (v19)
# Histórico: 27/05 → 15/07 → 23/07 → 16/08 → 19/08 → 25/08 (v8) → 06/09 (v9) → 17/09 (v10) → 17/09 (v11) → 17/09 (v12) → 17/09 (v13) → 18/09 (v14) → 19/09 (v15) → 20/09 (v16) → 29/09 (v17) → 05/10 (v18) → 07/10/2026 (v19 atual)
# Fontes: Páginas oficiais consultadas em 07/10/2026 (preços, termos, rate limits, políticas de privacidade) + catálogo herdado da v18 (itens não reverificados marcados como "não verificado em 07/10/2026")
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Este documento consolida as cotas gratuitas (Free Tiers), especificações técnicas, rate limits granulares (RPM, RPD, TPM, TPD, RPS, RPH, ASH, ASD) e políticas de uso de todas as plataformas de inferência de LLMs e IA generativa do ecossistema. Modelos descontinuados ou encerrados são categorizados com clareza em histórico de depreciação.

> **🧭 ATUALIZAÇÃO 07/10/2026 v19 (REVISÃO DE FATOS CONTRA FONTES OFICIAIS, TERMOS & LGPD, ESTRATÉGIA SEGMENTADA)**:
> *Regra de leitura da v19: tudo que foi conferido em fonte oficial em 07/10/2026 está marcado como "Revisado em 07/10/2026". Tudo que não foi reconferido nesta revisão está marcado como "(não verificado em 07/10/2026)". Onde as notas antigas (v11–v18) abaixo contradizem a v19, vale a v19.*
> 1. **DeepSeek reescrito**: o ID atual é `deepseek-flash` (DeepSeek-V4.1-Flash); o legado `deepseek-v4-flash` ainda é aceito. Preços oficiais de pico/fora de pico corrigidos. Janela de pico corrigida (01–04h e 06–10h UTC em dias úteis = 22h–01h e 03h–07h BRT). Bônus de "5M tokens/30 dias" removido (não consta na página oficial). Thinking ligado por padrão (`extra_body` para desligar). Política de dados: armazenamento na China.
> 2. **Gemini**: 2.0 Flash/Flash-Lite desligados em 01/06/2026; linha 1.5 fora do catálogo; 2.5 Pro **não** foi descontinuado; série 3.x **sem Grounding no Free Tier**; Free Tier usado para melhorar produtos (revisão humana); **cláusula de menores de 18 anos nos termos (vale para Free E Pago)**; limites do Free Tier só visíveis no AI Studio.
> 3. **Groq**: `llama-3.3-70b-versatile` / `llama-3.1-8b-instant` movidos para Enterprise ("Contact Sales"); `qwen/qwen3.6-27b` substituído por `qwen/qwen3.8-27b`; limites free do gpt-oss e Whisper confirmados; preços pagos; ZDR; limites valem por organização.
> 4. **Cerebras**: `llama-3.3-70b` e `qwen-3-32b` descontinuados → `gpt-oss-120b`.
> 5. **NVIDIA NIM**: limites não são publicados oficialmente; acesso gratuito é trial/avaliação — **produção proibida**.
> 6. **OpenRouter**: 20 RPM nos modelos `:free`; limite diário depende de créditos comprados; contas/chaves extras não aumentam limites.
> 7. **xAI**: removido "US$25/mês sem cartão"; programa atual de créditos condicionado a compartilhamento de dados; `grok-2*` obsoleto.
> 8. **Inception**: IDs atuais `mercury-2` / `mercury-2.5`; 100M tokens são crédito **único** por conta.
> 9. **Maritaca**: não existe free tier de API (R$ 20 de crédito no cadastro); tarifa noturna −30% automática e batch até −50%; variante `-br-sp` (inferência 100% no Brasil, +30%); DPA LGPD, sem treino, conteúdo descartado.
> 10. **Mistral**: Free = avaliação/protótipo; treino com dados ligado por padrão no Free (opt-out); "4M tokens/mês" não confirmado.
> 11. **xKiro**: cota diária grátis varia por conta; operador não identificado; repassa pedidos a provedores terceiros não nomeados; termos proíbem burlar cotas e revender.
> 12. **Cloudflare Workers AI**: 10.000 Neurons/dia confirmados; tabela de preço por modelo; modelos frontier (GLM-5.x, DeepSeek V4, Kimi) exigem método de pagamento.
> 13. **Novos na Seção 2**: Xiaomi MiMo pay-as-you-go e planos de assinatura para coding (MiMo Token Plan, Z.ai GLM Coding Plan, MiniMax M Plan Go, OpenCode Go, Alibaba Token Plan), com as restrições de uso em backend.
> 14. **Seção 4 reescrita** como estratégia segmentada por carga de trabalho (escola com dados pessoais / cargas sem dados pessoais / agentes de código), sem o enquadramento "produção sem custo de API". **Nova Seção 5 — Termos & LGPD.**
> 15. **Apêndice A — Arquivados / não recomendados**: gateways anônimos, plataformas chinesas domésticas, regionais irrelevantes (SEA-LION, Sarvam), trials não comerciais e a cadeia de fallback v18. Nada foi apagado.
> 16. **IDs obsoletos marcados** nas tabelas (Llama 3.1, Qwen 2.5, gemini-1.5/2.0, mixtral, gemma2) com "⚠️ ID legado/obsoleto (v19)".
>
> **🏆 ATUALIZAÇÃO 05/10/2026 v18 (AUDITORIA DE INÍCIO DE OUTUBRO, EXPANSÃO MULTIMODAL & RECONCILIAÇÃO GA)**:
> 1. **Google Gemini (GA do Gemini 3.8 Live & Preços do 3.8 Flash)**: Disponibilidade geral (GA) do **Gemini 3.8 Live** e suporte a WebSocket com *Live Extended Thinking*. Preços comerciais do **Gemini 3.8 Flash** consolidados no console; Free Tier mantido em 3.1 Flash / Flash-Lite com cotas dinâmicas por projeto e termos de uso do Free Tier com salvaguarda de logging.
> 2. **DeepSeek (Arquitetura V4.1-Flash & Multimodalidade Nativa)**: Lançamento do **DeepSeek-V4.1-Flash** com visão multimodal nativa. Consolidação de roteamento: aliases `deepseek-flash`, `deepseek-chat` (V3) e `deepseek-reasoner` (R1) com desconto oficial de 50% em horário Off-Peak (00:30–08:30 UTC+8). Depósito de $5 USD rendendo até 35M+ tokens sem cache e 100M+ com cache. ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 3. **NVIDIA NIM (Catálogo Expandido de 90+ Modelos Gratuitos)**: Expansão oficial do programa de desenvolvedores para **90+ modelos de IA** com quota de 40 RPM / 1.000 RPD sem exigência de cartão de crédito no cadastro. ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 4. **Mistral AI (Transição La Plateforme)**: Delimitação estrita do tier de experimentação gratuito para prototipagem de desenvolvedor versus bilhetagem de produção comercial para Mistral Large 3 e Small 4.
> 5. **OpenRouter Free**: Monitoramento de rotação diária de modelos agregados gratuitos sob sufixo `:free` (Nemotron, Qwen e abertos).
>
> **🏆 ATUALIZAÇÃO 29/09/2026 v17 (AUDITORIA DE RIGOR MÁXIMO, EXPURGO DE PLATAFORMAS ENCERRADAS & SINTONIA FINA DE COTAS)**:
> 1. **Expurgo & Descontinuações Confirmadas (Fato 100% Verificado)**:
>    * **Clarifai Encerrado**: A Clarifai encerrou formalmente suas operações independentes de plataforma em 17/07/2026 após sua aquisição pela **Nebius** (NASDAQ: NBIS). Sua tecnologia de inferência e patentes foram incorporadas ao **Nebius Token Factory**, e suas APIs legadas (`api.clarifai.com`) foram desligadas. Transferido formalmente para a seção de encerramentos.
>    * **GitHub Models Descontinuado**: O serviço de inferência e playground do **GitHub Models** (`models.inference.ai.azure.com`) foi oficialmente aposentado pela Microsoft/GitHub em 30/07/2026. Usuários corporativos devem utilizar o Azure AI Foundry, e desenvolvedores sem custo devem recorrer ao OpenRouter Free ou Hugging Face.
> 2. **Transição de Billing & Alertas de Cartão de Crédito**:
>    * **SambaNova Cloud**: Transicionou para modelo comercial Developer Tier (pay-as-you-go, 20M tokens/dia), passando a exigir cadastro de método de pagamento/cartão para emissão de chaves. Removido do fallback prioritário sem cartão.
>    * **Baseten Serverless**: Esclarecido que os $30 USD em créditos de computação Truss/vLLM exigem cadastro de cartão de crédito no console para ativação.
> 3. **Calibração Fina & Métricas Oficiais Verificadas**:
>    * **Maritaca AI (MariTalk)**: Calibração exata das métricas oficiais de Tier 0: **60 RPM**, **128.000 input tokens/min**, **10.000 output tokens/min** e Batch API com teto de 4M caracteres/dia. Consagração dos preços oficiais em Reais (Sabiá-4 a R$ 5/R$ 20 por 1M; Sabiá-4 Thinking a R$ 5/R$ 40; Sabiazinho-4 a R$ 1/R$ 4) e descontos de 50% (Flex/Batch/Noturno 22h-06h) e 75% em cache de contexto. ⚠️ *[Corrigido na v19 — ver seção correspondente]*
>    * **Google AI Studio**: Explicitação da política de cotas avaliadas dinamicamente por projeto no console e salvaguarda de privacidade (dados do Free Tier sujeitos a logging para treinamento de modelos Google; para desativar, requer migração para faturamento pago).
>    * **Exa.ai**: Formalização de que a cota de $10 USD é **recorrente todo mês** (reseta todo dia 1º, rendendo ~1.400 buscas neurais/mês) além do bônus inicial de $10 no onboarding sem cartão.
>    * **Cartesia vs. Lemonfox.ai**: Cartesia opera com cota permanente de 20.000 créditos/mês (Sonic-3 TTS); Lemonfox.ai opera com trial de 1 mês (10M créditos) sucedido por planos budget a partir de $5/mês.
>    * **Voyage AI**: Estruturação da franquia em 200M tokens para modelos modernos (`voyage-4`, `voyage-context-4`, `voyage-code-4`, multimodal) e 50M para modelos legados (`voyage-2`).
>    * **Hugging Face Serverless**: Registro da evolução da API Serverless para alocação mensal de $0.10 USD em créditos para provedores parceiros e foco da engine interna `hf-inference` em tarefas de CPU (embeddings e classificação).
> 4. **Cadeia de Fallback v17 & Integridade de Catálogo**: Recalibração de todos os níveis operacionais eliminando pontos de atrito ou surpresas de cobrança.
> 1. **Pilar 1: 5 Provedores de LLMs & Inferência Serverless de Alta Velocidade**: **Fireworks AI** ($1 USD trial sem cartão, FireAttention ultra-rápida em Llama 3.3, Qwen 2.5 e DeepSeek); **Clarifai** (Community Free Tier perpétuo com 1.000 ops/mês sem cartão); **Baseten** ($30 USD em créditos para deploy serverless Truss/vLLM); **Replicate** (créditos de teste de desenvolvedor sem cartão para LLMs, visão e difusão); **xAI Console / Grok API** ($25 USD/mês em developer grants para Grok-2/Grok-vision). ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 2. **Pilar 2: 5 Especialistas em Voz, Áudio, STT & TTS**: **Deepgram** ($200 USD em créditos perpétuos sem cartão, ~775 horas de transcrição Nova-2 e síntese Aura TTS); **AssemblyAI** ($50 USD em créditos gratuitos sem cartão, ~100 horas de transcrição Conformer-2/nano e LeMUR); **ElevenLabs** (Cota perpétua de 10.000 caracteres/mês gratuitos sem cartão para TTS e clonagem); **Cartesia** (Free Tier Sonic API com latência vocal <150ms); **Lemonfox.ai** (Free Tier diário para Whisper STT e TTS compatível 1:1 com OpenAI SDK).
> 3. **Pilar 3: 5 Especialistas em Embeddings, Rerank & Busca Neural para Agentes**: **Voyage AI** (200M tokens trial / 50M tokens perpétuos para `voyage-3`, `voyage-3-lite`, `voyage-code-3` e `rerank-2`); **Jina AI** (10M tokens gratuitos no onboarding + Jina Reader API `r.jina.ai` 100% gratuita perpétua); **Tavily AI** (1.000 buscas/mês perpétuas sem cartão para agentes autônomos); **Exa.ai** ($10 USD em créditos / 1.000 buscas semânticas neurais sem cartão); **Qdrant Cloud** (Cluster permanente gratuito na nuvem de 1GB RAM / ~1M vetores sem cartão).
> 4. **Pilar 4: 5 Provedores de Soberania Regional & Mercados Emergentes**: **StepFun / Jieyue Xingchen** (¥50 RMB / ~$7 USD em créditos para Step-1 com contexto de até 256k e Step-2 MoE); **01.AI / Lingyi Wanwu** (¥36 RMB em créditos para Yi-Lightning de 100+ tokens/s e Yi-Large até 200k contexto); **ModelScope / Alibaba DAMO** (Inference API serverless comunitária 100% gratuita para Qwen 2.5, SenseVoice e GLM); **RunPod Serverless** (micro-orçamento de $5 USD para execução serverless vLLM por segundo); **CentML / CServe** (Free developer trial com compilação de kernel acelerada até 3x mais rápida).
> 5. **Expansão do Catálogo**: Catálogo oficial consolidado saltando para **64 provedores documentados** com endpoints verificados, quotas numéricas rigorosas e requisitos de cartão auditados.
>
> **💎 ATUALIZAÇÃO 19/09/2026 v15 (CRÉDITOS RECORRENTES, SOBERANIA REGIONAL & EXPURGO DE FALSOS FREE TIERS)**:
> 1. **Inception Labs (Mercury API)**: Concessão automática de **100 Milhões de tokens gratuitos** no cadastro sem cartão de crédito (`mercury-chat`, `mercury-coder`) com throughput altíssimo e endpoint compatível com OpenAI. ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 2. **Reka AI**: Cota recorrente de **$10 USD / mês em créditos gratuitos** renovados mensalmente no console para desenvolvedores + 3 horas de indexação de vídeo multimodal gratuitas na API (`reka-flash`, `reka-core`).
> 3. **Bytez**: **$1.00 USD de crédito gratuito renovado a cada 4 semanas** (28 dias) para inferência de modelos open-source de topo (`llama-3.3-70b-instruct`, `qwen-2.5-72b-instruct`).
> 4. **Morph Labs (Fast Apply)**: Aceleração de agentes de código com **250.000 créditos / mês gratuitos ($0)** e ~200 requisições mensais para merge e diff instantâneo.
> 5. **Modal Labs**: **$30 USD / mês de computação serverless gratuita** no plano Starter para deploy de contêineres e vLLM (requer cartão de crédito cadastrado).
> 6. **Joias de Soberania Regional**: **InternLM / Shanghai AI Lab** (1M in / 3M out free tokens/mês); **Sarvam AI** (₹1.000 INR em créditos para línguas da Índia); **SEA-LION / AI Singapore** (10 RPM permanente para o Sudeste Asiático); e **LLM7.io** (gateway anônimo ultrarrápido a 2 req/s e 20 RPM sem login).
> 7. **Auditoria & Expurgo de Falsos Free Tiers**: **FriendliAI** desmentido (sem free tier permanente, 100% pay-per-token); **Liquid AI** esclarecido (sem API direta self-serve; use via OpenRouter ou Hugging Face); e **CrofAI** banido (wrapper fraudulento retirado do ar com erro 404).
>
> **🇧🇷 ATUALIZAÇÃO 18/09/2026 v14 (SOBERANIA NACIONAL MARITACA AI, CLOUDFLARE WORKERS AI & ABSORÇÃO OMNIROUTE)**:
> 1. **Absorção e Auditoria do OmniRoute (v3.8.51)**: Investigação minuciosa do catálogo de 352 provedores do repositório `diegosouzapw/OmniRoute`. Filtragem pelas 6 Regras de Ouro (expurgando proxies não oficiais e sessões efêmeras de scraping) e consolidação das plataformas com Free Tier permanente comprovado.
> 2. **Maritaca AI (MariTalk) — A Campeã Nacional Brasileira**: Inclusão da pioneira nacional em IA da Unicamp. Cota gratuita Tier 0 de **50 RPM / 500.000 TPM** sem cartão de crédito. Modelos de ponta: `sabia-4` (líder em língua portuguesa, concursos e jurisprudência), `sabia-4-thinking` (raciocínio aprofundado com CoT) e `sabiazinho-4` (baixa latência). Compatibilidade nativa com OpenAI SDK via `https://chat.maritaca.ai/api`. ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 3. **Cloudflare Workers AI**: Cota permanente de **10.000 Neurons por dia** renovados às 00:00 UTC sem cartão de crédito (~100k a 500k tokens gratuitos diários), executando `llama-3.3-70b-instruct`, `deepseek-r1-distill-qwen-32b`, `qwen2.5-coder-32b-instruct` e geração de imagem com `flux-1-schnell`.
> 4. **SambaNova Cloud**: Processadores proprietários SN40L RDUs atingindo centenas de tokens/segundo para `Meta-Llama-3.3-70B-Instruct` e `DeepSeek-R1` a 30 RPM / 6.000 TPM.
> 5. **Hugging Face Serverless Inference**: Endpoint `https://api-inference.huggingface.co/v1/` gratuito para milhares de modelos abertos com token de usuário HF.
> 6. **Especialistas em Embeddings & Reranking**: Inclusão de **Nomic AI** (`nomic-embed-text-v1.5` de 8k contexto) e **Mixedbread AI** (`mxbai-rerank-large-v1` para RAG de alta fidelidade).
> 7. **Gateways Anônimos & Sem Chave**: **AI Horde** (`0000000000` via crowdsourced GPUs), **DuckDuckGo AI Chat** e **UncloseAI**.
>
> **🎯 ATUALIZAÇÃO 17/09/2026 v13 (ALINHAMENTO OFICIAL DEEPSEEK, EXPURGO DE INCONSISTÊNCIAS & AUDITORIA INTEGRAL DE MODELOS)**:
> 1. **Correção Absoluta e Alinhamento Oficial do DeepSeek**: Restauração integral dos identificadores canônicos oficiais de chamada `deepseek-chat` (DeepSeek-V3) e `deepseek-reasoner` (DeepSeek-R1) para chamadas compatíveis com OpenAI SDK. Tabela consagrada e oficial de precificação por 1M tokens: DeepSeek-V3 a **$0.14** (Cache Miss) / **$0.014** (Cache Hit) / **$0.28** (Saída); DeepSeek-R1 a **$0.55** (Cache Miss) / **$0.14** (Cache Hit) / **$2.19** (Saída). Desconto oficial de **50% no horário econômico (Off-Peak)** (00:30 às 08:30 UTC+8). Cota de 5.000.000 tokens gratuitos para novas contas (30 dias). Cálculo real do poder de compra de **$5 USD** (rende de 18M a 35M tokens no V3 sem cache e até 100M+ tokens com alta taxa de cache hit). Reconciliação técnica explícita esclarecendo por que identificadores internos de engine (`deepseek-flash` / `deepseek-v4-pro`) aparecem em telemetria sem descaracterizar os nomes canônicos e preços de tabela. ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 2. **Auditoria de Ponta a Ponta dos Provedores Globais**: **Google AI Studio** (segregação estrita entre modelos em Produção Ativa GA e Upstream/Preview/Experimental, com detalhamento das cotas de Grounding Maps 500 RPD e Search 1.500 RPD); **Groq Cloud** (confirmação dos 13 modelos ativos reais, detalhamento da descontinuação de `qwen/qwen3.6-27b`, `llama-3.3-70b-versatile` e `llama-3.1-8b-instant`); **NVIDIA NIM** (catálogo de 82 modelos reais gratuitos, cota universal de 40 RPM / 1.000 RPD sem cartão, inclusão de `01-ai/yi-large` e `z-ai/glm-5.3`); **OpenRouter Free** (24 modelos `:free` ativos com contextos e limites de saída reais documentados); **Mistral AI** (modelos ativos, cota gratuita La Plateforme de 60 RPM / 4M tokens/mês); **Moonshot AI / Kimi** (modelos clássicos V1 e linha internacional K3/K2.7 com cota inicial de ¥15 RMB). ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 3. **Auditoria Rigorosa do Mercado Chinês (Modelos Nativos)**: **Baidu Qianfan** (`ERNIE-Speed` e `ERNIE-Lite` permanentemente 100% gratuitos a 300 RPM / 300.000 TPM); **Zhipu AI / BigModel** (`GLM-4-Flash` 100% free perpétuo a 1 concorrência + 25M tokens de boas-vindas); **Alibaba Cloud Model Studio / DashScope** (franquia de 1M a 2M tokens gratuitos por modelo Qwen na ativação por 90-180 dias + custos pós-free em frações de centavos); **Tencent Cloud Hunyuan** (pacote de 1 ano para `hunyuan-lite` e salvaguarda contra débitos automáticos no cartão); **ByteDance Volcano Engine Doubao** (registro transparente de que a API profissional é estritamente bilhetada em RMB sem free tier permanente para desenvolvedores).
> 4. **Consolidação dos Planos Budget de $5 a $10 USD**: Análise técnica detalhada de ROI de DeepSeek API Direta, xKiro (`xkiro.com`), OpenCode Zen/Go (`opencode.ai`), B.AI (`b.ai`) e Tencent WorkBuddy (`workbuddy.ai`).
> 5. **Cadeia de Fallback e Relatório em Runtime**: Atualização de todos os níveis e do quadro de auditoria em runtime com status 100% verificado.
>
> **🇨🇳 ATUALIZAÇÃO 17/09/2026 v12 (ECOSSISTEMA CHINÊS, PLANOS DE $5 & GATEWAYS BUDGET)**:
> 1. **Aprofundamento no Mercado Chinês de LLMs**: Mapeamento completo dos gigantes asiáticos com cotas gratuitas e preços de atacado: **Zhipu AI / BigModel** (`GLM-4-Flash` 100% free perpétuo sem cartão + 25M tokens de bônus), **Baidu Qianfan** (`ERNIE-Speed` e `ERNIE-Lite` permanentemente 100% free a 300 RPM / 300K TPM), **Alibaba Cloud Model Studio / DashScope / Bailian** (1M a 2M tokens free de onboarding por modelo Qwen com validade de 90-180 dias + preços em frações de centavos), **Tencent Cloud Hunyuan & TokenHub** (pacotes gratuitos de 1 ano para `hunyuan-lite` e 1.000 créditos para `hunyuan-3d`), **ByteDance Volcano Engine / Doubao** (auditoria: sem free tier na API para dev; bilhetagem ultra-barata em RMB a partir do 1º token), **MiniMax** (¥15 de crédito grátis; TTS hiper-realista Speech-01 e vídeo Hailuo), **01.AI / Lingyi Wanwu** (¥30 de créditos; linha Yi-Lightning), e **StepFun** (linha Step-3.5/3.7 Flash).
> 2. **Guia de Planos Econômicos de $5 a $10 USD ("Budget Plans")**: Detalhamento prático de como extrair máxima volumetria com micro-orçamentos: **xKiro** (Free Tier de 5M tokens/dia sem cartão + Wallet de $5 para desbloquear modelos proprietários e prioridade de fila), **OpenCode** (**OpenCode Zen** com zero markup e modelos free nativos como `MiMo V2.5 Free` e `MiniMax M2.5 Free` + **OpenCode Go** a $10/mês com $60 em valor de tokens), **DeepSeek API Direta** (o "Rei dos $5": um depósito mínimo de $5 USD rende de 18 a 35 MILHÕES de tokens com context caching), **B.AI** (sistema de créditos 1 USD = 1M créditos, com descontos de até 90% em horários ociosos para agentes), **SiliconFlow** ($5 rende dezenas de milhões de tokens em modelos 14B/32B/72B), e **Tencent WorkBuddy** (workspace de automação desktop compatível com BYO-Key). ⚠️ *[Corrigido na v19 — ver seção correspondente]*
> 3. **Cadeia de Fallback com Novas Rotas**: Inclusão da **Rota Asiática / Soberana Chinesa** e da **Rota Budget de $5 USD** para orquestrações de alta eficiência de custos.
>
> **🚀 ATUALIZAÇÃO 17/09/2026 v11 (EXPANSÃO DE NOVOS PROVEDORES & CONSOLIDAÇÃO TÉCNICA)**:
> 1. **Mapeamento Exaustivo de Novos Provedores Free Tier**: Documentação granular de 8 novas plataformas com cotas gratuitas comprovadas: **Hyperbolic** (60 RPM perpétuo, sem cartão), **SiliconFlow** (1.000 RPM / 40K TPM em modelos open-source free + 20M tokens bônus, sem cartão), **Pollinations.ai** (100% free perpétuo para texto, imagem, áudio e visão, sem cartão), **Cohere** (Trial API Key perpétua com 1K chamadas/mês, 20 RPM chat, 100 RPM embed, 10 RPM rerank, sem cartão), **AwanLLM** (Free Lite com tokens ilimitados, 20 RPM, 200 RPD pequenos, sem cartão), **Scaleway Generative APIs** (1M tokens/mês + 60 min áudio Whisper na nuvem soberana europeia), **Novita AI** (Trial Sandbox de $10-$100, 20 IPM para imagem e 60 RPM para LLM), e **Nebius Token Factory** (AI Builder Program com $400+ em créditos e auto-scaling dinâmico).
> 2. **Auditoria de Plataformas & Depreciações Confirmadas**: Identificação rigorosa de gateways sem Free Tier permanente: **Chutes.ai** (free tier descontinuado em 2026; migrado para subscrição a partir de $3/mês), **Lepton AI** (incorporado à NVIDIA DGX Cloud Lepton), **Together AI** (sem free tier permanente; exige depósito mínimo de $5), **AI/ML API** (free tier pausado; 100% pré-pago) e **Featherless.ai** (concorrência paga).
> 3. **Cadeia de Fallback Elevada para Arquitetura Resiliente em 4 Níveis**: Integrando provedores de alta vazão sem cartão (Google AI Studio, NVIDIA NIM, Groq, Hyperbolic, SiliconFlow, Pollinations.ai) e especialistas (Cohere, Scaleway, AwanLLM).
> 4. **Retenção Integral do Histórico v10**: Mantidas as validações críticas de 17/09 (Groq Qwen 3.8 ativo / 3.6 desligado; OpenRouter 24 modelos free com Nex-N2.5 e Ling VL; NVIDIA NIM com GLM-5.3 e Nemotron-Parse 2.0; Google AI Studio com Gemini 3.1/3.5 Flash-Lite e Antigravity Agent).

---

## 0. DIRETRIZES MANDATÓRIAS DE GOVERNANÇA & REGRAS OPERACIONAIS

Para manter este catálogo e o repositório como a **referência mundial de consulta técnica sobre Free Tiers e assinaturas de IA**, todas as auditorias, agentes autônomos e mantenedores seguem rigorosamente as seguintes diretrizes:

### 🏛️ As 5 Regras Mandatórias de Governança Operacional:
1. **Release Obrigatório no GitHub a Cada Atualização:**  
   Sempre que o catálogo canônico for atualizado, é obrigatório publicar imediatamente uma nova Release formal no repositório GitHub (com tag semântica). As notas da release devem explicitar com precisão cirúrgica:
   * Quais modelos foram lançados, adicionados ou ativados.
   * Quais modelos foram deprecados, descontinuados ou removidos, com indicação de rotas de substituição.
2. **Rastreamento Ativo de Promoções e Concessões Temporárias:**  
   Pesquisar ativamente se algum provedor está com promoção ou créditos promocionais temporários vigentes, especificando:
   * Modelos contemplados na promoção.
   * Limitações de vazão ou volume (tokens, gerações, concorrência).
   * Prazos e data limite de expiração da concessão.
   * *Aviso de Encerramento:* Quando a promoção acabar ou expirar, deve-se avisar formalmente na Release seguinte e atualizar o catálogo.
3. **Expansão Multimodal para Produção & Regra dos Dois Planos Mais Baratos:**  
   Buscar ativamente novos provedores que agreguem à produção real: texto, código, geração de imagens, música, vídeo, áudio e efeitos especiais.  
   * **Regra dos 2 Planos Budget:** Para provedores pagos ou híbridos com cotas gratuitas ou micro-orçamentos (estilo OpenCode, xKiro, B.AI), é obrigatório documentar os **dois planos mais baratos de cada um**, seus limites numéricos e benefícios reais. Se uma plataforma paga não oferecer free tier e não possuir diferencial em micro-planos, não deve ser adicionada ao catálogo.
4. **Verdade Concreta e Auditável (Tolerância Zero a Alucinações):**  
   Buscar sempre dados técnicos sólidos, verificáveis em documentação oficial ou testes ativos no terminal. Na menor dúvida, não avance; deixe explicitamente registrado que o dado é volátil e passível de alteração pela operadora.
5. **Padrão Ouro de Referência Global:**  
   Este catálogo é a referência de consulta para desenvolvedores, startups e arquitetos de IA. Traga apenas informações pertinentes, de altíssima precisão e utilidade prática para o ecossistema de infraestrutura de inteligência artificial.

### 🛡️ As 7 Regras de Ouro de Verificação Técnica:
1. **Verificabilidade em Runtime (Nada de Especulação):** Teste ativo no terminal ou documentação oficial em vigência.
2. **Apenas Identificadores Canônicos de API:** Nomes comerciais sempre mapeados ao payload JSON exato (`deepseek-flash`, `gemini-2.5-flash`, etc.).
3. **Transparência Granular de Limites:** Proibido termos como "ilimitado"; especifique RPM, TPM, RPD e concorrência.
4. **Classificação Rigorosa de Faturamento:** Segregação estrita entre 🟢 Free Permanente sem cartão, 🟡 Trial de Boas-Vindas com expiração, 🟠 Free Tier exigindo cartão de crédito e 🔵 Micro-Orçamento ($5 USD).
5. **Tolerância Zero a Afiliados e Interesses Comerciais:** Links diretos aos consoles oficiais, sem rastreadores ou parcerias comerciais opacas.
6. **Rastreamento Ativo de Depreciações:** Modelos encerrados nunca são deletados em silêncio; são movidos para o arquivo histórico com data e rotas de migração.
7. **Conformidade de Termos & LGPD (v19):** Nenhuma rota é recomendada para produção se os termos do provedor proibirem produção, se o provedor treinar com os dados enviados, se o operador não for identificável ou se exigir burlar limites (múltiplas contas/chaves). Dados pessoais exigem análise LGPD (ver Seção 5).

---

## 1. QUADRO COMPARATIVO GERAL DE MODELOS FREE & POLÍTICAS

---

### 🟢 GOOGLE AI STUDIO (Gemini API) — *Revisado em 07/10/2026 (página oficial de preços, Gemini API Additional Terms e página de deprecações)*

O Google AI Studio oferece o free tier mais robusto para **desenvolvimento, protótipos e conteúdo sem dados pessoais**, sem necessidade de cartão de crédito. O Grounding gratuito existe apenas na linha **2.5** (Flash / Flash-Lite); na série **3.x** o Grounding **não está disponível no Free Tier**.

> **⚠️ Políticas Críticas (verificadas em 07/10/2026)**:
> 1. **Limites do Free Tier só no AI Studio**: A Google não publica RPM/TPM/RPD do Free Tier na documentação; os valores aparecem apenas no painel de rate limits do projeto (`aistudio.google.com`). Os números de RPM/TPM/RPD das tabelas abaixo vêm de versões anteriores deste manual e estão *(não verificado em 07/10/2026)*.
> 2. **Free Tier é usado para melhorar produtos (com revisão humana)**: Na página de preços, o Free Tier consta como "Used to improve our products: **Yes**" (Pago: **No**). Os termos dizem que revisores humanos podem ler, anotar e processar entradas e saídas do serviço gratuito e orientam: *"Do not submit sensitive, confidential, or personal information to the Unpaid Services"*.
> 3. **Cláusula de idade — vale para Free E Pago**: Gemini API Additional Terms (atualizados em 28/04/2026): é preciso ter 18+ e **não** usar os Serviços em site, app ou serviço *"directed towards or is likely to be accessed by individuals under the age of 18"*. ➜ Atendimento de escola (WhatsApp de escola, alunos) é risco direto: **não usar Gemini nesse caso, nem no plano pago**.
> 4. **Uso profissional & limites**: os termos restringem o uso a fins profissionais/de negócio (não consumidor). Os Google APIs Terms (seção 1d) proíbem tentar contornar limites (ex.: múltiplos projetos/contas para multiplicar cota) e proíbem sublicenciar a API a terceiros (revenda).

#### 🔹 Modelos estáveis (GA) — Free Tier & Preço Pago (por 1M tokens, USD) — *Revisado em 07/10/2026*

| Modelo ID API | Display Name | Free Tier | Preço Pago (In / Out) | Search Grounding | Maps Grounding | Status Operacional (07/10/2026) |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **`gemini-2.5-flash`** | Gemini 2.5 Flash | ✅ Gratuito (limites só no AI Studio) | $0.30 / $2.50 (cache $0.03) | Free: até 500 RPD (compartilhado com Flash-Lite) · Pago: 1.500 RPD grátis, depois $35/1.000 | Free: 500 RPD · Pago: 1.500 RPD grátis, depois $25/1.000 | Sem data de desligamento anunciada |
| **`gemini-2.5-flash-lite`** | Gemini 2.5 Flash-Lite | ✅ Gratuito | $0.10 / $0.40 (cache $0.01) | Free: até 500 RPD (compartilhado com Flash) · Pago: 1.500 RPD grátis | Free: 500 RPD · Pago: 1.500 RPD grátis | Sem data de desligamento anunciada |
| **`gemini-2.5-pro`** | Gemini 2.5 Pro | ✅ Gratuito (consta no Free Tier) | $1.25 / $10.00 (≤200K) · $2.50 / $15.00 (>200K) | Free: não disponível · Pago: 1.500 RPD grátis | Free: não disponível · Pago: 10.000 RPD grátis | **NÃO foi descontinuado** (sem data de desligamento anunciada) — corrige o changelog v4 |

#### ⛔ Modelos Gemini desligados (não usar) — *Revisado em 07/10/2026*

| Modelo ID API | Desligamento | Substituto oficial recomendado |
| :--- | :---: | :--- |
| `gemini-2.0-flash` / `gemini-2.0-flash-001` | **01/06/2026** | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` / `gemini-2.0-flash-lite-001` | **01/06/2026** | `gemini-3.1-flash-lite` |
| `gemini-1.5-flash` / `gemini-1.5-pro` | Fora do catálogo (não constam na página de preços em 07/10/2026; data exata não verificada) | Linha 2.5 / 3.x |

> As linhas `gemini-2.0-flash`, `gemini-1.5-flash` e `gemini-1.5-pro` que a v18 listava como "Produção Ativa GA" foram removidas da tabela de modelos ativos.

#### 💲 Preços pagos da série 3.x (por 1M tokens, USD) — *Revisado em 07/10/2026*

| Modelo ID API | Entrada | Saída (inclui thinking) | Cache | Observação |
| :--- | :---: | :---: | :---: | :--- |
| `gemini-3.1-flash-lite` | $0.25 | $1.50 | $0.025 | Free Tier disponível; Grounding só no pago |
| `gemini-3.5-flash-lite` | $0.30 | $2.50 | $0.03 | Free Tier disponível; Grounding só no pago |
| `gemini-3.6-flash` / `gemini-3.7-flash` / `gemini-3.8-flash` | $0.75 | $3.75 | — | Preço válido até 31/12/2026; depois dobra |

* **Grounding na série 3.x (pago)**: 5.000 buscas/mês grátis (Google Search) e 5.000 prompts/mês (Google Maps), compartilhados entre todos os modelos 3.x; depois $14 por 1.000. **No Free Tier: não disponível.**

#### 🔹 Modelos da Série 3, Gemma & Preview (tabela herdada da v18 — RPM/TPM/RPD *(não verificado em 07/10/2026)*)

Modelos de última geração, variantes experimentais e arquiteturas abertas do Google:

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM* | TPM* | RPD* | Map Grounding | Search Grounding | Notas / Status Operacional |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`gemini-3.5-flash-lite`** | Gemini 3.5 Flash Lite | Multimodal | 1.048.576 / 65.536 | **15** | **250.000** | **500** | ❌ (Free) | ❌ 0 | **Top Pick #1 Desenvolvimento** — Atualizado com arquitetura 3.5 |
| **`gemini-3.1-flash-lite`** | Gemini 3.1 Flash Lite | Multimodal | 1.048.576 / 65.536 | **15** | **250.000** | **500** | ❌ (Free) | ❌ 0 | **Top Pick #2** — Uso comercial permitido pelos termos (fins profissionais), mas **sem dados pessoais** no Free |
| `gemini-3.8-flash` | Gemini 3.8 Flash | Multimodal | 1.048.576 / 65.536 | **5** | 250.000 | **20** | ❌ 0 | ❌ 0 | Mais recente da linha Flash (setembro/2026); alta inteligência |
| `gemini-3.7-flash` | Gemini 3.7 Flash | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | Alta capacidade analítica de raciocínio |
| `gemini-3.6-flash` | Gemini 3.6 Flash | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | 17% menos tokens de overhead; endpoint estável |
| `gemini-3.5-flash` | Gemini 3.5 Flash | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | Ativo e em uso operacional |
| `gemini-3-flash-preview` | Gemini 3 Flash Prev | Multimodal | 1.048.576 / 65.536 | 5 | 250.000 | 20 | ❌ 0 | ❌ 0 | Endpoint de preview da geração 3 |
| `antigravity-preview-09-2026` 🆕 | Antigravity Agent | Agente | 131.072 / 65.536 | **60** | **100.000** | **100** | ❌ 0 | ❌ 0 | **NOVO (set/2026)** — Otimizado para execução de agentes autônomos |
| `gemma-4-31b-it` | Gemma 4 31B Instruct | Texto/Visão | 262.144 / 32.768 | **30** | **16.000** | **14.400** | ❌ | ❌ | **30 RPM / 14.4K RPD** — Open weights dense rodando na infraestrutura Google |
| `gemma-4-26b-a4b-it` | Gemma 4 26B MoE | Texto/Visão | 262.144 / 32.768 | **30** | **16.000** | **14.400** | ❌ | ❌ | Arquitetura esparsa rápida para extração e processamento massivo |
| `gemini-3.1-flash-tts-preview` | Flash TTS | Áudio/TTS | 8.192 / 16.384 | 3 | 10.000 | 10 | ❌ (Free) | - | Síntese vocal de alta fidelidade |
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

\* *RPM/TPM/RPD: valores herdados da v18 — (não verificado em 07/10/2026); conferir no AI Studio.*

#### 🎯 Grounding no Free Tier — *Revisado em 07/10/2026*

O Free Tier só oferece Grounding na **linha 2.5**:

1. **Google Search Grounding**:
   * **Free Tier**: até **500 RPD** em `gemini-2.5-flash` e `gemini-2.5-flash-lite` (limite compartilhado entre os dois). `gemini-2.5-pro`: não disponível no Free.
   * **Pago (2.5)**: 1.500 RPD grátis, depois $35 por 1.000 prompts com grounding.
   * **Série 3.x**: **não disponível no Free Tier**; no pago, 5.000 buscas/mês grátis compartilhadas, depois $14/1.000.
   * ❌ A afirmação da v18 de "1.500 RPD grátis no Free" está **errada** (1.500 RPD é a franquia do plano pago). As rotas `gemini-2` e `default` citadas na v18 dependiam do 2.0 Flash, desligado em 01/06/2026.

2. **Google Maps Grounding**:
   * **Free Tier**: **500 RPD** em `gemini-2.5-flash` / `gemini-2.5-flash-lite`.
   * **Série 3.x (incluindo 3.1/3.5 Flash-Lite)**: **não disponível no Free Tier** — a v18 marcava "✅ 500 RPD" para eles, o que está errado.
   * **Pago**: 2.5 Flash/Flash-Lite: 1.500 RPD grátis, depois $25/1.000; 2.5 Pro: 10.000 RPD grátis; série 3.x: 5.000 prompts/mês grátis, depois $14/1.000.

---

### 🟠 GROQ CLOUD — *Revisado em 07/10/2026 (console.groq.com/docs/models, /docs/rate-limits, Services Agreement)*

Inference engine ultra-rápida (LPU). Os limites abaixo são os do **plano gratuito**. **Os limites valem por organização, não por usuário ou chave** ("Rate limits apply at the organization level, not individual users") — criar chaves extras na mesma organização não aumenta a cota, e criar organizações/contas extras para isso é burlar limite.
🚨 **17/09/2026**: `qwen/qwen3.6-27b` foi **desativado**. Usar `qwen/qwen3.8-27b` (preview).
🚨 **v19**: `llama-3.3-70b-versatile` e `llama-3.1-8b-instant` **não estão mais no self-serve** — aparecem na página oficial de modelos como **Enterprise ("Contact Sales")**. Não usar como rota padrão.

> **Privacidade (07/10/2026)**: sem retenção de dados de inferência por padrão; logs para monitoramento de abuso por até 30 dias, a menos que se ative **Zero Data Retention (ZDR)**; armazenamento nos EUA (GCP). Termos: o titular da conta precisa ter 18+ (não há cláusula proibindo serviços acessados por menores, diferentemente do Gemini).

#### 💲 Preços pagos (Developer / self-serve, por 1M tokens) — *Revisado em 07/10/2026*

| Modelo ID API | Entrada | Saída | Observação |
| :--- | :---: | :---: | :--- |
| `openai/gpt-oss-120b` | $0.15 | $0.60 | Modelo de raciocínio; tokens de raciocínio contam como saída |
| `openai/gpt-oss-20b` | $0.075 | $0.30 | Rápido para roteamento/extração |
| `qwen/qwen3.8-27b` | $0.80 | $4.00 | Preview |
| `whisper-large-v3-turbo` | $0.04 por hora de áudio | — | STT |
| `llama-3.3-70b-versatile` / `llama-3.1-8b-instant` | Enterprise ("Contact Sales") | — | Fora do self-serve |

#### 🆓 Limites do plano gratuito

> Limites de `openai/gpt-oss-120b` / `openai/gpt-oss-20b` (**30 RPM / 1.000 RPD / 8K TPM / 200K TPD**) conferidos em 07/10/2026. Demais linhas herdadas da v18 *(não verificado em 07/10/2026)*. ⚠️ 8K TPM significa que um único prompt grande (ex.: contexto de agente de código) já estoura o limite por minuto.

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

> Limites de Whisper (**20 RPM / 2.000 RPD / 7.200 ASH / 28.800 ASD**) conferidos em 07/10/2026; Orpheus *(não verificado em 07/10/2026)*. Preço pago do `whisper-large-v3-turbo`: $0.04/hora de áudio.

| Modelo | Modalidade | RPM | RPD | ASH / ASD | Validação | Notas |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `whisper-large-v3` | audio STT | **20** | **2.000** | **7.200** / **28.800** | ✅ OK | Transcrição multilingual (8h áudio/dia) |
| `whisper-large-v3-turbo` | audio STT | **20** | **2.000** | **7.200** / **28.800** | ✅ OK | Versão acelerada |
| `canopylabs/orpheus-v1-english` | audio TTS | **10** | **100** | - (1.2K TPM / 3.6K TPD) | ✅ OK | Vozes naturais em inglês |
| `canopylabs/orpheus-arabic-saudi`| audio TTS | **10** | **100** | - (1.2K TPM / 3.6K TPD) | ⚠️ Termos | Requer aceite de termos no console |

#### ⛔ Histórico de Depreciações / Mudanças de Acesso Groq

| Modelo | Data | Situação / Substituto Recomendado |
| :--- | :---: | :--- |
| `qwen/qwen3.6-27b` 🚨 | **17/09/2026** | **Desativado pelo provedor** → Substituir por `qwen/qwen3.8-27b` |
| `llama-3.1-8b-instant` | — (data não verificada) | **Movido para Enterprise ("Contact Sales")** — fora do self-serve (v19; a v18 dizia "desativado em 17/08") → alternativa self-serve: `openai/gpt-oss-20b` |
| `llama-3.3-70b-versatile`| — (data não verificada) | **Movido para Enterprise ("Contact Sales")** — fora do self-serve (v19) → alternativa self-serve: `openai/gpt-oss-120b` |
| `qwen/qwen3-32b` | **17/07/2026** | Descontinuado → `qwen/qwen3.8-27b` |
| `meta-llama/llama-4-scout-17b-16e-instruct` | **17/07/2026** | Descontinuado → `openai/gpt-oss-120b` |
| `qwen-2.5-32b`, `gemma2-9b-it`, `mixtral-8x7b-32768` | — | ⚠️ ID legado/obsoleto (v19): não constam na página oficial de modelos em 07/10/2026 → `openai/gpt-oss-20b` / `openai/gpt-oss-120b` |

---

### 🟢 NVIDIA NIM (build.nvidia.com) — *Revisado em 07/10/2026 (NVIDIA API Trial Terms + FAQ oficial) — SOMENTE TRIAL / AVALIAÇÃO*

> 🚨 **Uso em produção PROIBIDO no acesso gratuito**: os NVIDIA API Trial Terms permitem o uso apenas para teste e avaliação interna; a FAQ oficial define produção como qualquer uso além de desenvolvimento/teste/pesquisa/avaliação, **incluindo atender usuários reais ou transações de negócio**, e exige licença NVIDIA AI Enterprise (ou endpoint pago de parceiro). **Não usar NIM grátis em fallback de produção.**
> **Limites**: a NVIDIA declara que **não publica** os rate limits do trial (variam por modelo e carga; o limite da conta aparece no canto superior direito do build.nvidia.com). Os valores "40 RPM / 1.000 RPD" desta seção vêm da v18 e são **não oficiais** *(não verificado em 07/10/2026)*. Catálogo de modelos abaixo: *(não verificado em 07/10/2026)*.

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

### 🟣 OPENROUTER — *Revisado em 07/10/2026 (docs/api-reference/limits); lista de modelos herdada da v18*

O OpenRouter funciona como agregador universal com roteamento inteligente. **Modelos `:free`**: **20 RPM**; o **limite diário depende do total de créditos já comprados** na conta (um teto abaixo e outro acima de um limiar de créditos) — consulte `GET https://openrouter.ai/api/v1/key` → campo `free_model_daily_requests`. O valor fixo "200 RPD" da v18 está *(não verificado em 07/10/2026)*. A documentação oficial avisa: **"Making additional accounts or API keys will not affect your rate limits"**. A lista de modelos abaixo está *(não verificado em 07/10/2026)* — a oferta `:free` muda com frequência. Modelos `:free` não devem receber dados pessoais.

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

### 🟠 MISTRAL AI — *Revisado em 07/10/2026 (Help Center / docs oficiais); tabela de modelos herdada da v18*

O modo **Free (padrão)** da La Plateforme é destinado a **avaliação e prototipagem** e tem os menores limites. Os limites são **por organização e por modelo** (requisições/segundo e tokens/minuto aplicados de forma independente) e aparecem na página *Limits* do Admin Console. **Treino com dados**: no modo Free, as chamadas de API podem ser usadas para treinar modelos **por padrão**, com opt-out em Admin Console → Privacy; no pay-as-you-go o padrão é opt-out (informação de fontes secundárias consultadas em 07/10/2026 — confirmar no Admin Console). Os valores "50K TPM / 4M tokens/mês / ~1 req/s" da v18 estão *(não verificado em 07/10/2026)*. ➜ Não usar como rota de produção nem com dados pessoais sem desligar o treino. Tabela de modelos e RPM: *(não verificado em 07/10/2026)*.

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

### 🟢 DEEPSEEK — *Revisado em 07/10/2026 (página oficial de modelos & preços, política de privacidade e termos)*

A DeepSeek opera uma das infraestruturas de inferência de maior eficiência de custos da indústria (Mixture-of-Experts, cache de contexto automático e desconto fora de pico).

> 🚨 **Correção v19**: as versões v13–v18 afirmavam que os únicos IDs válidos eram `deepseek-chat`/`deepseek-reasoner` e que nunca se deveria enviar `model="deepseek-flash"`. **Isso está errado.** Em 07/10/2026 a documentação oficial orienta o uso de **`deepseek-flash`** (DeepSeek-V4.1-Flash). A seção "Reconciliação de Rotas Internas" da v18 (que tratava `deepseek-flash`/`deepseek-v4-pro` como tags internas de cluster) foi removida por não ter base oficial.

#### 🔑 1. Identificadores de API (Padrão OpenAI SDK) — *Revisado em 07/10/2026*

* **`deepseek-flash`**: DeepSeek-V4.1-Flash — **ID recomendado**.
* **`deepseek-v4-flash`**: ID legado, ainda aceito.
* **`deepseek-v4-pro`**: modelo Pro (preços *(não verificado em 07/10/2026)*).
* `deepseek-chat` / `deepseek-reasoner`: aliases antigos (V3/R1) — status atual *(não verificado em 07/10/2026)*; não usar em código novo.

> **Endpoint Base Oficial**: `https://api.deepseek.com` (ou `https://api.deepseek.com/v1`)
> **Formato de Chamada**: `client = OpenAI(api_key="<DEEPSEEK_API_KEY>", base_url="https://api.deepseek.com")`
> **Thinking ligado por padrão**: os tokens de raciocínio são cobrados como saída, contam em `max_tokens` e aumentam a latência. Para desligar: `extra_body={"thinking": {"type": "disabled"}}`.

#### 💰 2. Preços Oficiais por 1 Milhão de Tokens — `deepseek-flash` (07/10/2026)

| Janela | Entrada (Cache Miss) | Entrada (Cache Hit) | Saída |
| :--- | :---: | :---: | :---: |
| **Pico** | **$0.30** | **$0.006** | **$1.20** |
| **Fora de pico (50% OFF)** | **$0.15** | **$0.003** | **$0.60** |

##### 🌙 Janela de Pico (corrigida na v19)

* **Pico**: **01:00–04:00 e 06:00–10:00 UTC, em dias úteis** = **22:00–01:00 e 03:00–07:00 BRT** (UTC-3).
* **Fora de pico**: todo o restante, **incluindo fins de semana**.
* ❌ A janela "00:30–08:30 UTC+8 / 13:30–21:30 BRT" das versões v13–v18 está **errada**.
* Preços de `deepseek-v4-pro`, contexto máximo e concorrência: *(não verificado em 07/10/2026)*.

#### 🎁 3. Cota Free & Poder de Compra de $5 USD

* **Bônus de "5.000.000 de tokens grátis por 30 dias": REMOVIDO na v19** — não consta na página oficial de preços em 07/10/2026.
* **Depósito mínimo / meios de pagamento / limite de concorrência**: *(não verificado em 07/10/2026)*.
* **Poder de compra (cálculo, `deepseek-flash` fora de pico, thinking desligado)**: $5 ≈ **33M tokens de entrada sem cache** ($0.15/M) **ou** ≈ **8,3M tokens de saída** ($0.60/M). O rendimento real depende da proporção entrada/saída e da taxa de cache hit ($0.003/M fora de pico). Os números "18–35M" e "100M+ com cache" da v18 eram baseados em preços antigos.

#### 🔒 4. Privacidade & LGPD — *Revisado em 07/10/2026*

* **Armazenamento de dados na República Popular da China** (política de privacidade).
* Termos (seção 4.3): permitem uso de entradas de forma desidentificada para melhorar o serviço, com opção de opt-out.
* A política declara que o serviço **não é destinado a dados de crianças nem a dados de saúde**.
* ➜ **Nunca usar com dados pessoais de escola/alunos/responsáveis** (LGPD arts. 11, 14 e 33). Adequado para conteúdo público e código sem segredos.

---

### ⚫ KIMI / MOONSHOT AI — *Validado em 17/09/2026 (APIs Doméstica & Internacional)* ⚠️ *(não verificado em 07/10/2026)*

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

### 🟣 ANTHROPIC (Claude) — *Validado em 29/09/2026 (11 modelos na API)* ⚠️ *(não verificado em 07/10/2026)*

* **Status Free Tier**: ❌ **NÃO HÁ free tier permanente na API direta da Anthropic** ($5 inicial único de créditos para teste no cadastro).
* **Acesso Free via Código**: O antigo **GitHub Models** (`models.inference.ai.azure.com`), que fornecia acesso de teste, consta como **encerrado em 30/07/2026** *(não verificado em 07/10/2026)*. Para uso sem custo, recorra ao webchat em `claude.ai` ou a modelos abertos de raciocínio (ex.: `openai/gpt-oss-120b` no Groq Free).

| Modelo ID API | Contexto | Cota Free API | Acesso Alternativo Gratuito |
| :--- | :---: | :---: | :--- |
| `claude-sonnet-4-6` / `claude-sonnet-5` | 200K / 1M | ❌ Apenas $5 inicial | Webchat em `claude.ai` |
| `claude-opus-4-6` / `claude-opus-5` | 200K / 1M | ❌ Apenas $5 inicial | Webchat com plano Pro |
| `claude-haiku-4-5-20251001` | 200K | ❌ Apenas $5 inicial | Rápido e de baixo custo pago |
| `claude-3.5-sonnet` (legado) | 200K | ❌ GitHub Models Encerrado | Webchat em `claude.ai` (DuckDuckGo AI Chat é só interface web, sem API — movido para o Apêndice A) |

---

### 🟢 OPENAI — *Validado em 17/09/2026 (119 modelos no catálogo)* ⚠️ *(não verificado em 07/10/2026)*

* Chat models (`gpt-4o`, `gpt-4o-mini`, `gpt-5.4`) requerem saldo pré-pago.
* Endpoints gratuitos: `whisper-1` (3 RPM / 200 RPD) e `omni-moderation-latest`.

---

### 🔵 CEREBRAS CLOUD — *Revisado em 07/10/2026 (documentação oficial de deprecações)*

* **Modelos**: `llama-3.3-70b` e `qwen-3-32b` estão **descontinuados** na documentação oficial; a migração indicada é para **`gpt-oss-120b`**.
* **Free Tier**: a v5 registrou "encerrado (HTTP 402 Payment Required)"; status atual do free tier e preços *(não verificado em 07/10/2026)*.
* **Ação**: remover de qualquer cascata as rotas Cerebras configuradas com `llama-3.3-70b`.

---

### 🟢 DEEPINFRA — *Validado em 17/09/2026 (189 modelos no catálogo)* ⚠️ *(não verificado em 07/10/2026)*

* Pay-per-use ultra-econômico sem mínimo de recarga. `openai/gpt-oss-120b` a **$0.08 por milhão de tokens blended**.
* Modelos disponíveis: `Qwen/Qwen3.5-122B-A10B`, `ByteDance/Seed-2.0-mini`, `google/veo-3.1-fast`, `black-forest-labs/FLUX-2-pro`.

---

### 🇨🇳 ECOSSISTEMA CHINÊS — *Plataformas domésticas movidas para o Apêndice A.2 na v19*

As plataformas **domésticas** chinesas (Zhipu BigModel `open.bigmodel.cn`, Baidu Qianfan, Alibaba DashScope China/Bailian, Tencent Hunyuan/TokenHub, ByteDance Volcano/Doubao, MiniMax `api.minimax.chat`, 01.AI, StepFun, ModelScope e InternLM) foram movidas para o **Apêndice A.2**. Motivos: dados processados na China, cadastro frequentemente atrelado a telefone/documento chinês e dados da v12–v18 *(não verificado em 07/10/2026)*. ➜ Não usar com dados pessoais (LGPD art. 33).

As ofertas **internacionais** abaixo continuam úteis para cargas **sem dados pessoais**:

#### 🟢 Z.AI (plataforma internacional da Zhipu) — *Revisado em 07/10/2026*

| Modelo | Entrada | Cache | Saída | Observações |
| :--- | :---: | :---: | :---: | :--- |
| `glm-4.7-flash` | **Grátis** | — | **Grátis** | Modelo gratuito (rate limits *(não verificado em 07/10/2026)*) |
| `glm-4.5-flash` | **Grátis** | — | **Grátis** | Modelo gratuito |
| `glm-5.3-flash` | $0.15 | $0.03 | $0.50 | Thinking **não pode ser desligado** |
| GLM-5.3-FlashX (ID exato não verificado) | $0.37 | $0.075 | $1.25 | — |
| `glm-5.3` | $1.40 | $0.26 | $4.40 | Flagship (página do modelo cita AA Index 57) |

* **Privacidade**: o DPA da Z.ai declara que não armazena conteúdo e que processa em Singapura; a página do fornecedor menciona servir em cluster de chips chineses. ➜ Ok para conteúdo público; evitar dados pessoais.
* **GLM Coding Plan**: ver Seção 2 (planos de assinatura).

#### 🟢 MINIMAX (plataforma internacional — platform.minimax.io) — *Revisado em 07/10/2026*

* **Pay-as-you-go**: `MiniMax-M3` a **$0.30 entrada / $0.06 cache / $1.20 saída** por 1M (preço com 50% de desconto exibido na página oficial; preço cheio *(não verificado em 07/10/2026)*). Thinking adaptativo, pode ser desligado.
* **M3.1-Flash-Preview**: disponível **apenas** via M Plan e MiniMax Code; sempre usa thinking.
* **Privacidade**: dados da API armazenados em data center nos EUA; os termos permitem usar entradas para desenvolver e melhorar serviços. ➜ Não usar com dados pessoais.
* **M Plan (assinatura)**: ver Seção 2.

---


### 🟢 HYPERBOLIC (api.hyperbolic.xyz) — *Validado em 17/09/2026 (Free Basic Tier Perpétuo)* ⚠️ *(não verificado em 07/10/2026)*

A Hyperbolic opera um ecossistema de computação descentralizada e inferência aberta de alta performance com endpoints OpenAI-compatíveis. O plano **Free Basic Tier** oferece inferência gratuita contínua sem data de expiração.

* **Endpoint Base**: `https://api.hyperbolic.xyz/v1` (Compatível com OpenAI SDK / LiteLLM)
* **Tipo de Cota**: Free Tier permanente (Basic Tier).
* **Limite Global de Taxa**: **60 RPM** (Requests Per Minute) fixos no plano gratuito. Upgrade para 600 RPM disponível no plano Pro com depósito único de $5.
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** nem dados de faturamento para uso de inferência serverless. Cadastro via e-mail ou Web3 wallet. Cartão/depósito de $5 é exigido exclusivamente para instâncias de GPU dedicada e provisionamento de volumes de armazenamento.
* **Autenticação**: Bearer token (`Authorization: Bearer <HYPERBOLIC_API_KEY>`) gerado no dashboard (`app.hyperbolic.xyz/settings/api-keys`).

| Modelo ID API | Display Name | Modalidade | Contexto (In / Out) | RPM | TPM / TPD | Tipo de Cota | Capacidades Principais & Notas |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| `meta-llama/Meta-Llama-3.1-405B-Instruct` | Llama 3.1 405B | Texto / Raciocínio | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Flagship open-weights de 405B rodando sob inferência distribuída ⚠️ *ID legado/obsoleto (v19)* |
| `meta-llama/Meta-Llama-3.1-70B-Instruct` | Llama 3.1 70B | Texto / Tool Use | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Workhorse para raciocínio analítico, código e tool calling estruturado ⚠️ *ID legado/obsoleto (v19)* |
| `meta-llama/Meta-Llama-3.1-8B-Instruct` | Llama 3.1 8B | Texto / Velocidade | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Latência ultrabaixa para extração, classificação e parsing de texto ⚠️ *ID legado/obsoleto (v19)* |
| `Qwen/Qwen2.5-72B-Instruct` | Qwen 2.5 72B | Texto / Código | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Excelente em matemática, raciocínio lógico e suporte multilíngue ⚠️ *ID legado/obsoleto (v19)* |
| `Qwen/Qwen2.5-Coder-32B-Instruct` | Qwen 2.5 Coder 32B | Coding Agent | 131.072 / 8.192 | **60** | Dinâmico | Free Perpétuo | Especialista em geração de código, refatoração e resolução de bugs ⚠️ *ID legado/obsoleto (v19)* |
| `deepseek-ai/DeepSeek-V3` | DeepSeek V3 | MoE Geral | 65.536 / 8.192 | **60** | Dinâmico | Free Perpétuo | Arquitetura MoE de 671B com 37B ativos; alta inteligência por custo zero |
| `deepseek-ai/DeepSeek-R1` | DeepSeek R1 | Raciocínio Puro | 65.536 / 8.192 | **60** | Dinâmico | Free Perpétuo | Raciocínio analítico aprofundado com tokens de reflexão (thinking tags) |
| `FLUX.1-dev` | FLUX.1 Dev | Geração de Imagem | 1.024 x 1.024 | **10** | - | Free Perpétuo | Síntese de imagens de 12B parâmetros com alta fidelidade e tipografia |
| `SDXL1.0-base` | Stable Diffusion XL | Geração de Imagem | 1.024 x 1.024 | **20** | - | Free Perpétuo | Geração rápida de imagens em 1024x1024 para prototipagem visual |

---

### 🟢 SILICONFLOW / SILICONCLOUD (api.siliconflow.com) — *Validado em 17/09/2026 (Free Tier Permanente & High Throughput)* ⚠️ *(não verificado em 07/10/2026)*

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
| `Qwen/Qwen2.5-7B-Instruct` | Qwen 2.5 7B | Texto / Chat | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Modelo de 7B denso, balanceado e rápido para tarefas cotidianas ⚠️ *ID legado/obsoleto (v19)* |
| `Qwen/Qwen2.5-Coder-7B-Instruct` | Qwen 2.5 Coder 7B | Código / CLI | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Otimizado para autocompletar e geração de código em 92 linguagens ⚠️ *ID legado/obsoleto (v19)* |
| `Qwen/Qwen2.5-VL-7B-Instruct` | Qwen 2.5 VL 7B | Visão Computacional| 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | VLM com leitura de imagens, diagramas, tabelas e OCR multilíngue ⚠️ *ID legado/obsoleto (v19)* |
| `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`| DeepSeek R1 Qwen 7B| Raciocínio Destilado | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Raciocínio matemático e lógico treinado sob as saídas do DeepSeek R1 |
| `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`| DeepSeek R1 Llama 8B| Raciocínio Destilado | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Variante de raciocínio destilado sob a arquitetura do Llama 3.1 8B ⚠️ *ID legado/obsoleto (v19)* |
| `THUDM/glm-4-9b-chat` | GLM-4 9B Chat | Texto / Tool Use | 32.768 / 4.096 | **1.000** | **40K TPM** | Free Permanente | Modelo bilingue (EN/ZH) da Zhipu AI para extração e diálogos |
| `deepseek-ai/DeepSeek-V3` | DeepSeek V3 Flagship| MoE Geral | 65.536 / 8.192 | 100 | **100 RPD** | Free sem KYC | 671B MoE com limite de 30 RPH / 100 RPD no nível não-verificado |
| `deepseek-ai/DeepSeek-R1` | DeepSeek R1 Flagship| Raciocínio Puro | 65.536 / 8.192 | 100 | **100 RPD** | Free sem KYC | Modelo completo de raciocínio com 30 RPH / 100 RPD no nível free |
| `black-forest-labs/FLUX.1-schnell` | FLUX.1 Schnell | Geração de Imagem | 1.024 x 1.024 | **10** | - | Free Permanente | Síntese de imagem em 4 passos sob licença Apache 2.0 |
| `BAAI/bge-large-zh-v1.5` | BGE Large Chinese | Embeddings | 512 / 1.024 dim | **1.000** | **40K TPM** | Free Permanente | Embedding semântico denso de alta dimensionalidade |
| `BAAI/bge-m3` | BGE M3 Multi-modal | Embeddings Multiling| 8.192 / 1.024 dim | **1.000** | **40K TPM** | Free Permanente | Suporta busca densa, esparsa e multi-vectorial em 100+ idiomas |

---

### 🟢 POLLINATIONS.AI (gen.pollinations.ai) — *Validado em 17/09/2026 (Gateway Multimodal 100% Free Perpétuo)* ⚠️ *(não verificado em 07/10/2026)*

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
| `qwen-coder` | Qwen 2.5 Coder 32B | Código / Refatoração | 32.768 / 8.192 | **60** | Free Perpétuo | Especialista em código, geração de testes e resolução de bugs ⚠️ *ID legado/obsoleto (v19)* |
| `deepseek` | DeepSeek V3 / R1 | Raciocínio MoE | 64.000 / 8.192 | **60** | Free Perpétuo | Raciocínio analítico avançado e geração estruturada de JSON |
| `flux` | FLUX.1 Schnell | Geração de Imagem | 1.024 x 1.024 | **30** | Free Perpétuo | Geração de imagem com qualidade fotorrealista e tipografia nítida |
| `flux-realism` | FLUX Realism Tuned | Imagem Fotorrealista| 1.024 x 1.024 | **20** | Free Perpétuo | Ajustado especificamente para pele humana, iluminação e texturas |
| `turbo` | SDXL Turbo Fast | Geração Rápida | 512 x 512 | **60** | Free Perpétuo | Geração ultrarrápida em 1 passo para prototipagem de UI e ícones |

---

### 🗄️ COHERE (Trial não comercial) & AWANLLM (modelos "uncensored") — *movidos para o Apêndice A na v19*

* **Cohere Trial API Key**: trial para experimentação **não comercial** → Apêndice A.4.
* **AwanLLM**: gateway de modelos "uncensored/zero-refusal", operador pouco transparente → Apêndice A.1. Não usar em produção.

---
### 🟢 SCALEWAY GENERATIVE APIS (api.scaleway.ai) — *Validado em 17/09/2026 (Free Tier Europeu — 1M Tokens + Áudio)* ⚠️ *(não verificado em 07/10/2026)*

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
| `qwen2.5-coder-32b-instruct` | Qwen 2.5 Coder | Coding Agent | 32.768 / 8.192 | **30** | 1M tokens/mês | Especialista em desenvolvimento de software com suporte a 92 linguagens ⚠️ *ID legado/obsoleto (v19)* |
| `mistral-nemo-12b-instruct-2407`| Mistral NeMo 12B| Workhorse | 128.000 / 4.096 | **30** | 1M tokens/mês | Modelo desenvolvido por Mistral AI e NVIDIA, excelente em raciocínio compacto |
| `pixtral-12b-2409` | Pixtral 12B | Visão Multimodal | 128.000 / 4.096 | **30** | 1M tokens/mês | Modelo multimodal nativo da Mistral para leitura e análise de imagens e gráficos |
| `whisper-large-v3` | Whisper STT | Áudio / Transcrição| Chunks de 30s | **10** | **60 min/mês** | Transcrição de fala multilíngue com alta precisão e pontuação automática |
| `bge-multilingual-gemma2` | Embeddings | Vetorização | 8.192 / 3.584 dim | **30** | 1M tokens/mês | Modelo de embeddings denso derivado da arquitetura Google Gemma 2 ⚠️ *ID legado/obsoleto (v19)* |

---

### 🟡 NOVITA AI (api.novita.ai) — *Validado em 17/09/2026 (Sandbox / Trial Multimodal — LLM & Imagem)* ⚠️ *(não verificado em 07/10/2026)*

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
| `meta-llama/llama-3.1-70b-instruct` | Texto / Tools | 131.072 / 8.192 | **60 RPM** | Trial ($10-$100) | Raciocínio, orquestração de agentes e geração de JSON estruturado ⚠️ *ID legado/obsoleto (v19)* |
| `meta-llama/llama-3.1-8b-instruct` | Texto Rápido | 131.072 / 8.192 | **60 RPM** | Trial ($10-$100) | Processamento rápido com custo marginal e baixa latência ⚠️ *ID legado/obsoleto (v19)* |
| `deepseek/deepseek-r1` | Raciocínio Puro | 65.536 / 8.192 | **60 RPM** | Trial ($10-$100) | Resolução de problemas matemáticos e cadeias lógicas densas |
| `flux.1-schnell` | Geração de Imagem | 1.024 x 1.024 | **20 IPM** | Trial ($10-$100) | Geração de imagens rápida em 4 passos com renderização tipográfica |
| `flux.1-dev` | Imagem Pro | 1.024 x 1.024 | **10 IPM** | Trial ($10-$100) | Síntese de imagem com alta fidelidade a prompts detalhados |
| `stable-diffusion-xl-base` | Imagem Clássica | 1.024 x 1.024 | **20 IPM** | Trial ($10-$100) | SDXL 1.0 para pipelines de imagem e controle por LoRA |

---

### 🔵 NEBIUS TOKEN FACTORY (api.studio.nebius.ai) — *Validado em 17/09/2026 (AI Builder Program & Dynamic Scaling)* ⚠️ *(não verificado em 07/10/2026)*

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
| `meta-llama/Meta-Llama-3.1-405B-Instruct` | Llama 3.1 405B | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Modelo aberto de maior escala rodando em superclusters H100 ⚠️ *ID legado/obsoleto (v19)* |
| `meta-llama/Meta-Llama-3.1-70B-Instruct` | Llama 3.1 70B | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Resposta de baixa latência (TTFT < 200ms) para pipelines críticos ⚠️ *ID legado/obsoleto (v19)* |
| `deepseek-ai/DeepSeek-V3` | DeepSeek V3 | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | DeepSeek V3 hospedado em data centers ocidentais de alta segurança |
| `deepseek-ai/DeepSeek-R1` | DeepSeek R1 | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Raciocínio profundo sem estrangulamento de infraestrutura |
| `Qwen/Qwen2.5-72B-Instruct` | Qwen 2.5 72B | 131.072 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | 72B para tarefas complexas de raciocínio lógico e programação ⚠️ *ID legado/obsoleto (v19)* |
| `mistralai/Mistral-Large-Instruct-2407` | Mistral Large | 128.000 / 8.192 | **60+ RPM Dinâmico** | $400+ Builder | Modelo de raciocínio de ponta da Mistral AI com janela de 128K |

---

### ⛔ AUDITORIA DE GATEWAYS & PLATAFORMAS: SEM FREE TIER PERMANENTE OU DESCONTINUADOS ⚠️ *(não verificado em 07/10/2026)*

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
| **DeepSeek Direto** (`api.deepseek.com`) | Pay-as-you-go | Depósito mínimo *(não verificado em 07/10/2026)* | ≈ **33M tokens de entrada** sem cache ou ≈ **8,3M de saída** (`deepseek-flash` fora de pico, thinking off) | `deepseek-flash` (V4.1), `deepseek-v4-pro` | Preços oficiais 07/10: pico $0.30/$0.006/$1.20; fora de pico $0.15/$0.003/$0.60. ⚠️ Dados armazenados na China — não usar com dados pessoais. |
| **Xiaomi MiMo** (`api.xiaomimimo.com/v1`) 🆕 | Pay-as-you-go | Sem mínimo verificado | `mimo-v2.6-flash`: ≈ **35,7M tokens de entrada** ou ≈ **17,9M de saída** | `mimo-v2.6-flash`, `mimo-v2.6-pro` | $0.14 / cache $0.0028 / $0.28 (Flash); não treina com o conteúdo enviado. |
| **xKiro** (`xkiro.com`) | Wallet pré-pago | Recarga mínima *(não verificado em 07/10/2026)* | Cota diária free **varia por conta** (consultar `GET /v1/usage`); "5M tokens/dia" **não confirmado** | Catálogo com tiers `free` / `paid` / `premium` | ⚠️ Operador não identificado; repassa pedidos a provedores terceiros não nomeados; termos proíbem burlar cotas e revender. Só testes sem dados pessoais. |
| **OpenCode Zen** (`opencode.ai`) | Pay-as-you-go | Sem mínimo ($0 a $5) *(não verificado em 07/10/2026)* | Modelos free (lista muda) + custo por token | Ver docs do Zen | ⚠️ A maioria dos modelos free do Zen **pode usar os dados para treino** no período free (exceções citadas na doc: Space Bunny Free e LongCat 2.5 Preview Free, zero-retention). |
| **OpenCode Go** (`opencode.ai`) | Subscrição Mensal | **$10/mês** (Go Plus: $40/mês) | Limite em US$ **por modelo** (ex.: até $60/mês em DeepSeek V4.1 Flash, MiMo-V2.6-Flash, GLM-5.3-Flash, MiniMax M3; $15 em Kimi K3 / GLM-5.3); janelas: 5h = 20%, semana = 50%, mês = 100% | GLM, Kimi, Qwen, DeepSeek, MiMo, MiniMax, LongCat, Grok e outros | Feito para agentes de código. |
| **B.AI** (`b.ai`) | Sistema de Créditos (1M/$1) | **$5.00** recarga | **5 a 50 MILHÕES** de tokens (horários ociosos) | 20+ modelos globais e chineses (Gemini 3.8, Claude, Hunyuan, Qwen) | Descontos de até 90% em períodos de baixa demanda (off-peak) *(não verificado em 07/10/2026)*. |
| **SiliconFlow** (`api.siliconflow.com`) | Pay-as-you-go | **$5.00** (¥35 RMB) | **10 a 20 MILHÕES** de tokens nos modelos 14B/32B | Qwen 2.5 72B, DeepSeek R1/V3 full, FLUX.1 Dev | *(não verificado em 07/10/2026)*; IDs Qwen 2.5 / DeepSeek V3/R1 provavelmente desatualizados. |

---

### 🛠️ DETALHAMENTO DOS GATEWAYS "BUDGET"

#### 🟡 XKIRO (xkiro.com — AI Gateway Multimodel) — *Revisado em 07/10/2026 (docs.xkiro.com, /terms, /privacy)*
* **Endpoint Base**: `https://api.xkiro.com/v1` (Compatível com OpenAI SDK `/chat/completions`)
* **Acesso Gratuito**: existe uma **cota diária de tokens para modelos do tier `free`**, mas o **valor depende da conta/plano** — consulte `GET https://api.xkiro.com/v1/usage` (`free_tokens.limit_per_day`). O "5M tokens/dia" das versões anteriores **não foi confirmado**.
* **Tiers de modelo**: `free` (qualquer conta, dentro da cota diária), `paid` (plano ou saldo; crédito de trial conta) e `premium` (plano ou **depósito real**; créditos promocionais não liberam). Modelos pay-as-you-go são sempre debitados do wallet. Lista atual em `GET /v1/models` (campo `access_tier`).
* **⚠️ Transparência & Termos**:
  * O site **não identifica a empresa/pessoa que opera o serviço**.
  * Os pedidos são **repassados a provedores terceiros não nomeados**; a política diz não persistir prompts/respostas (só metadados), mas não há DPA nem lista de suboperadores.
  * Os termos **proíbem burlar rate limits/cotas** e **revender** o serviço sem permissão, além de exigir respeitar os termos dos provedores de origem.
* **Uso recomendado**: no máximo testes sem dados pessoais. **Não usar em produção com dados de clientes/alunos.**
* **Wallet**: valores mínimos de recarga e modelos "Claude 3.5 / GPT-4o" citados na v18 *(não verificado em 07/10/2026)*.

#### 🟢 OPENCODE (opencode.ai — OpenCode Zen & Go) — *Revisado em 07/10/2026 (opencode.ai/docs/go, /docs/zen)*
* **Ecossistema**: Focado na comunidade de desenvolvedores e assistentes de código em terminal.
* **OpenCode Zen**:
  * Gateway pay-as-you-go com modelos gratuitos e pagos.
  * **Privacidade dos modelos free**: a doc informa que, em geral, os modelos free podem ter os dados usados para melhorar o modelo durante o período gratuito (ex.: Big Pickle, MiMo, Ling, Nemotron); exceções zero-retention citadas: **Space Bunny Free** e **LongCat 2.5 Preview Free**. ➜ Não enviar código de cliente nem segredos para modelos free.
  * Os nomes "MiMo V2.5 Free" / "MiniMax M2.5 Free" da v18 *(não verificado em 07/10/2026)*; MiMo v2.5 será descontinuado em 21/10/2026.
* **OpenCode Go ($10/mês) e Go Plus ($40/mês)**:
  * Limites definidos em **US$ por modelo**: janela de 5h = 20% do limite mensal do modelo; semana = 50%; mês = 100%.
  * Exemplos de limite mensal no Go: GLM-5.3-Flash $60, MiMo-V2.6-Flash $60, MiniMax M3 $60, DeepSeek V4.1 Flash $60, Kimi K3 $15, GLM-5.3 $15, Qwen3.8 Flash $30 (tabela oficial em 07/10/2026; muda com frequência).
  * Funciona com o OpenCode ou "qualquer agente"; restrição explícita de uso em backend *(não verificado em 07/10/2026)*.

#### 🟢 B.AI (b.ai — "白" / Infraestrutura Econômica de Agentes) ⚠️ *(não verificado em 07/10/2026)*
* **Endpoint Base**: `https://api.b.ai/v1` (OpenAI-compatible)
* **Mecânica Econômica**: Opera sob uma unidade própria de liquidação: **1 USD = 1.000.000 de Créditos B.AI**.
* **Precificação Dinâmica (Off-Peak Discounts)**: Monitora a carga global dos data centers parceiros. Em horários de baixa demanda (madrugadas asiáticas/americanas), aplica **descontos de até 90%** sobre o preço de tabela de modelos como Gemini, Claude, Hunyuan e DeepSeek.
* **Ideal Para**: Agentes de execução noturna (batch processing, data scraping, síntese de relatórios em background) onde $5 USD realizam o trabalho equivalente a $50 USD em APIs tradicionais.

#### 🟢 TENCENT WORKBUDDY (workbuddy.ai) ⚠️ *(não verificado em 07/10/2026)*
* **Natureza**: Não é uma API isolada, mas um **AI-native Desktop Workspace** corporativo desenvolvido pela Tencent Cloud.
* **Política de Custos**: Gratuito para uso pessoal como runtime de agente local. Permite plugar **chaves de API próprias (BYO-Key)** de qualquer provedor compatível com OpenAI (incluindo chaves gratuitas do Groq, SiliconFlow, Zhipu AI ou xKiro).
* **Para Equipes**: Planos baseados em assentos corporativos com pool compartilhado de créditos para automação de rotinas no Office, WeCom e geração automática de planilhas.


---

### 🟢 XIAOMI MIMO — Pay-as-you-go (api.xiaomimimo.com/v1) — *Revisado em 07/10/2026* 🆕

| Modelo ID API | Entrada | Cache | Saída | Observações |
| :--- | :---: | :---: | :---: | :--- |
| `mimo-v2.6-flash` | $0.14 | $0.0028 | $0.28 | Thinking ligado por padrão (pode ser desligado) |
| `mimo-v2.6-pro` | $0.435 | $0.0036 | $0.87 | — |
| `mimo-v2.5` / `mimo-v2.5-pro` | — | — | — | **Descontinuação em 21/10/2026** → migrar para v2.6 |

* **Privacidade (política atualizada em 25/06/2026)**: dados de usuários fora do EEE armazenados em **Singapura**; *"Xiaomi will not use the content you provide for model training"*.
* **Uso**: boa opção barata para cargas sem dados pessoais e agentes de código. Para dados pessoais, ainda há transferência internacional (LGPD art. 33).

---

### 🧾 PLANOS DE ASSINATURA PARA CODING ("Token Plans" / "Coding Plans") — *Revisado em 07/10/2026* 🆕

> ⚠️ **Regra geral**: estes planos são para **uso interativo em ferramentas de programação/agentes**. Vários **proíbem explicitamente** usar a chave do plano em **backends de aplicação, scripts automatizados ou batch** — para produção, use a API pay-as-you-go do mesmo provedor. Usar plano de coding como "API barata" para o bot/CRM viola os termos e pode levar à suspensão.

| Plano | Preço | Cota | Ferramentas | Restrição de uso |
| :--- | :--- | :--- | :--- | :--- |
| **MiMo Token Plan** (Xiaomi) | Lite **$6/mês** · Standard $16 · Pro $50 · Max $100 (anual −12%; 1ª compra −12%) | 4,1B / 11B / 38B / 82B Credits por mês; consumo 0,8× das 00:00–08:00 de Pequim (16:00–24:00 UTC = 13:00–21:00 BRT) | OpenCode, OpenClaw, Claude Code e outras ferramentas de desenvolvimento | Descrito como "solução exclusiva para cenários de programação com IA" em ferramentas de desenvolvimento; proibição explícita de backend *(não verificado em 07/10/2026)* |
| **Z.ai GLM Coding Plan** | A partir de **$18/mês** (Lite); preços Pro/Max *(não verificado em 07/10/2026)* | Créditos: Lite 2.000 por 5h / 10.000 por semana · Pro 12.000 / 60.000 · Max 28.000 / 140.000; fora de pico consome 50% | Claude Code, Cline, OpenCode e ferramentas oficialmente suportadas | **Somente em ferramentas oficialmente suportadas**; uso em ferramentas não suportadas, assento compartilhado ou chamadas anormais aciona restrições |
| **MiniMax M Plan Go** | **$22/mês** ou $220/ano (1º mês −50% até 14/10/2026); Explore $55 · Build $132 | Explore = 3× Go; Build = 7,5× Go (janelas de 5h e semanais) | MiniMax Code + chave de assinatura para Claude Code, Codex, Cursor, OpenCode | A MiniMax orienta **pay-as-you-go para produção**; a chave do plano é separada da chave PAYG |
| **OpenCode Go** | **$10/mês** · Go Plus $40/mês | Limite em US$ por modelo (5h 20% · semana 50% · mês 100%) | OpenCode ou outros agentes | Restrição de backend *(não verificado em 07/10/2026)* |
| **Alibaba Model Studio Token Plan** (Personal; só região Singapura) | Lite **$6/mês** (promoção; cheio $8) · Essential $10 ($16) · Standard $18 ($25) · Pro $68 ($80) | 11.500 / 25.500 / 45.000 / 180.000 Credits por mês | Claude Code, Cursor, Qwen Code, Qoder, OpenClaw | **Proibido** em scripts de automação, backends de aplicação ou chamadas batch; inferência em modo "Global" (transferência internacional de dados) |

> **Alibaba Coding Plan (produto separado)**: o Lite parou de aceitar novas assinaturas em 20/03/2026 e renovações em 13/04/2026; o Pro ($50/mês) era de quantidade limitada. A própria Alibaba recomenda o Token Plan.

---

## 3. PROVEDORES ADICIONAIS & COMPLEMENTARES (ABSORÇÃO OMNIROUTE & SOBERANIA)

### 🦜 MARITACA AI (MariTalk) — A Campeã Nacional Brasileira de IA — *Revisado em 07/10/2026 (maritaca.ai/api, /planos, /tratamento-de-dados, /dpa, /termos)*
* **Console / Cadastro**: [https://plataforma.maritaca.ai/](https://plataforma.maritaca.ai/)
* **Endpoint Base**: `https://chat.maritaca.ai/api` (compatível com o SDK da OpenAI). A documentação atual mostra exemplos com a Responses API — confirmar `/chat/completions` antes de integrar numa cascata baseada em Chat Completions *(não verificado em 07/10/2026)*.
* **❌ Não existe free tier de API**: o plano gratuito é do **Chat** (20 mensagens por semana). Na API, novos usuários recebem **R$ 20 em créditos** (a plataforma anuncia "sem cartão de crédito"; o README oficial no GitHub cita o crédito ao cadastrar cartão ou fazer a primeira recarga, mínimo R$ 5).
* **Rate limits**: "Tier 0 grátis com 60 RPM / 128K input TPM / 10K output TPM" e "Batch 4M caracteres/dia" da v17 *(não verificado em 07/10/2026)* — conferir os limites reais no console.
* **Por que é Vital**: Desenvolvida no Brasil (origem na Unicamp), a família **Sabiá** é especializada em português e no contexto brasileiro (jurisprudência, ENEM, OAB, editais, nuances regionais).
* **Precificação Oficial (por 1M tokens, R$)**:

| Modelo ID API | Contexto | Entrada | Saída | Variante `-br-sp` (100% Brasil) | Uso indicado |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`sabia-4-thinking`** | 128K na plataforma (a página da API cita 1M; divergência não resolvida) | R$ 5,00 | R$ 40,00 | R$ 6,50 / R$ 52,00 | Raciocínio |
| **`sabia-4`** | 128K | R$ 5,00 | R$ 20,00 | R$ 6,50 / R$ 26,00 | Uso geral, RAG, redação longa |
| **`sabiazinho-4`** | 128K | R$ 1,00 | R$ 4,00 | **R$ 1,30 / R$ 5,20** | Classificação, respostas curtas, atendimento |
| `sabia-3` / `sabiazinho-3` | — | — | — | — | Legados *(não verificado em 07/10/2026)* |

* **Variante `-br-sp`**: mesmo modelo com sufixo `-br-sp` (ex.: `sabiazinho-4-br-sp`) = **inferência 100% em território nacional**, custo **30% acima** do padrão.
* **Descontos**: **tarifa noturna automática de −30%** (página da plataforma) e **Batch API com até −50%**; a página de planos resume como "descontos de até 50% para uso noturno e em batch". O "−50% das 22h às 06h" e o "−75% em cache" da v17 *(não verificado em 07/10/2026)*.
* **🔒 Dados & LGPD (07/10/2026)**:
  * Maritaca Inteligência Artificial Ltda. (CNPJ 48.565.396/0001-40) atua como **operadora** dos dados enviados via API, com **DPA sob a LGPD**.
  * Conteúdo de prompts e respostas da API **descartado imediatamente** após a geração; **nunca usado para treino**, ajuste fino, avaliação ou destilação.
  * Logs técnicos sem conteúdo (IP, data/hora, tokens) por até 18 meses (Marco Civil); logs de erro podem reter conteúdo por até 30 dias.
  * Termos: titular da conta deve ter 18+; não há cláusula proibindo serviços acessados por menores.
* **➜ Opção nº 1 deste manual para dados pessoais de brasileiros** (ver Seção 4.2).

---

### ☁️ CLOUDFLARE WORKERS AI — *Revisado em 07/10/2026 (página oficial de preços, atualizada em 01/10/2026)*
* **Console**: [https://dash.cloudflare.com/](https://dash.cloudflare.com/)
* **Cota Gratuita**: **10.000 Neurons por dia** (nos planos Workers Free **e** Workers Paid), reset diário às 00:00 UTC. Acima disso, só no **Workers Paid**, a **$0.011 por 1.000 Neurons**.
* **Rendimento Real (cálculo)**: depende do modelo. Ex.: `@cf/openai/gpt-oss-120b` = 31.818 neurons/M de entrada e 68.182/M de saída → 10K neurons ≈ **314K tokens só de entrada** ou ≈ **147K só de saída**. `@cf/meta/llama-3.3-70b-instruct-fp8-fast` (26.668 / 204.805 neurons por M) → ≈ 375K de entrada ou ≈ 49K de saída. O "100K–500K tokens/dia" da v14 só vale para cargas com pouca saída.
* **Modelos que exigem método de pagamento** (Workers Paid ou créditos AI Gateway): `@cf/zai-org/glm-5.2`, `@cf/zai-org/glm-5.3`, `@cf/zai-org/glm-5.3-flash`, `@cf/deepseek-ai/deepseek-v4-flash-0731`, `@cf/deepseek-ai/deepseek-v4-pro-0813`, `@cf/moonshotai/kimi-k2.6`, `@cf/moonshotai/kimi-k2.7-code`.
* **Modelos úteis dentro da cota gratuita (preço equivalente por 1M tokens)**:

| Modelo ID API | Entrada | Saída | Uso |
| :--- | :---: | :---: | :--- |
| `@cf/openai/gpt-oss-120b` | $0.350 | $0.750 | Texto geral / raciocínio |
| `@cf/openai/gpt-oss-20b` | $0.200 | $0.300 | Rápido |
| `@cf/zai-org/glm-4.7-flash` | $0.060 | $0.400 | Barato, bom custo/benefício |
| `@cf/google/gemma-4-26b-a4b-it` | $0.100 | $0.300 | MoE do Google |
| `@cf/qwen/qwen3-30b-a3b-fp8` | $0.051 | $0.335 | MoE leve |
| `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | $0.293 | $2.253 | ID atual (a v14 citava `@cf/meta/llama-3.3-70b-instruct`) |
| `@cf/openai/whisper-large-v3-turbo` | $0.0005 por minuto de áudio | — | STT |
| `@cf/baai/bge-m3` | $0.012 | — | Embeddings multilíngues |
| `@cf/black-forest-labs/flux-1-schnell` | por tile/step | — | Imagem |

* **Requisitos**: conta Cloudflare; "sem cartão no Workers Free" *(não verificado em 07/10/2026)*. Política de dados *(não verificado em 07/10/2026)*.

---

### ⚡ SAMBANOVA CLOUD — *Transição para Developer Tier Pago (Setembro 2026)* ⚠️ *(não verificado em 07/10/2026)*
* **Console**: [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/)
* **Endpoint Base**: `https://api.sambanova.ai/v1` (Compatível com OpenAI SDK)
* **Infraestrutura**: Chips proprietários **SN40L RDUs (Reconfigurable Dataflow Units)** com throughput ultra-rápido.
* **Status de Acesso (Auditoria 29/09/2026)**: 🟠 **Requer método de pagamento / cartão de crédito**. A plataforma encerrou a distribuição de cotas livres sem método de pagamento e migrou para o **Developer Tier** (pay-as-you-go).
* **Limites do Developer Tier**: Limite padrão de até **20 Milhões de tokens por dia** em modelos de produção e preview após validação de pagamento.
* **Modelos Disponíveis**: `Meta-Llama-3.3-70B-Instruct`, `DeepSeek-R1`, `DeepSeek-R1-Distill-Llama-70B`, `Qwen2.5-72B-Instruct`.

---

### 🤗 HUGGING FACE SERVERLESS INFERENCE API ⚠️ *(não verificado em 07/10/2026)*
* **Console / Tokens**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
* **Endpoint Base**: `https://api-inference.huggingface.co/v1/` (Compatível com OpenAI)
* **Modelo Operacional (2026)**: A plataforma evoluiu do modelo antigo de requisições por hora para uma concessão mensal de **$0.10 USD em créditos gratuitos** renovados mensalmente no dashboard para roteamento via Inference Providers parceiros, enquanto a infraestrutura interna `hf-inference` é dedicada prioritariamente a tarefas de CPU (embeddings semânticos e classificação).
* **Acervo de Modelos**: Acesso serverless imediato a milhares de modelos open-source:
  * `meta-llama/Llama-3.3-70B-Instruct`
  * `Qwen/Qwen2.5-72B-Instruct`
  * `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`
  * `BAAI/bge-large-en-v1.5` (Vetores)
  * `openai/whisper-large-v3` (Transcrição de voz)

---

### 🎯 ESPECIALISTAS EM EMBEDDINGS & RERANKING ⚠️ *(não verificado em 07/10/2026)*
Para arquiteturas avançadas de RAG (Retrieval-Augmented Generation) sem onerar a cota de chat:
1. **Nomic AI (`https://www.nomic.ai/`)**:
   * Modelo: `nomic-embed-text-v1.5` (Janela de 8.192 tokens com dimensionalidade configurável).
   * Cota: Free Tier com dezenas de milhares de requisições de vetorização gratuitas sem cartão.
2. **Mixedbread AI (`https://www.mixedbread.ai/`)**:
   * Modelos: `mxbai-rerank-large-v1` (Rerank state-of-the-art) e `mxbai-embed-large`.
   * Cota: Cota mensal gratuita para desenvolvedores.

---

### 🕵️ GATEWAYS ANÔNIMOS & SEM CHAVE — *movidos para o Apêndice A.1 na v19*

AI Horde, DuckDuckGo AI Chat, UncloseAI (e LLM7.io, AwanLLM) foram movidos para o **Apêndice A.1**: operador desconhecido ou comunitário, sem DPA; no AI Horde os workers voluntários podem ler os prompts; o DuckDuckGo AI é só interface web (sem API). **Nunca usar em produção nem com dados pessoais.**

---

### ❌ GITHUB MODELS (STATUS: DESCONTINUADO EM 30/07/2026) ⚠️ *(não verificado em 07/10/2026)*
* **Endpoint Anterior**: `https://models.inference.ai.azure.com`
* **Status**: ❌ **SERVIÇO ENCERRADO DEFINITIVAMENTE**.
* **Diagnóstico Operacional**: A Microsoft e o GitHub descontinuaram formalmente o playground e a API de inferência do GitHub Models em 30 de julho de 2026. Usuários que utilizavam os endpoints devem migrar para o **Azure AI Foundry** (plataforma comercial do Azure) ou utilizar gateways gratuitos auditados como **Google AI Studio**, **NVIDIA NIM** e **OpenRouter Free**.

---

### 🚀 INCEPTION LABS (Mercury API) — 100 Milhões de Tokens (crédito único) — *Revisado em 07/10/2026 (docs.inceptionlabs.ai)*
* **Console / Cadastro**: [https://platform.inceptionlabs.ai/](https://platform.inceptionlabs.ai/)
* **Endpoint Base**: `https://api.inceptionlabs.ai/v1` (compatível com OpenAI SDK: `/v1/chat/completions`)
* **Cota**: **crédito ÚNICO de 100.000.000 de tokens** por conta nova, **compartilhado entre todos os modelos**, sem dados de pagamento. Não é recorrente; quando acabar, é preciso cadastrar pagamento em Billing.
* **Requisitos**: "sem cartão" confirmado; "sem telefone, login com Google/GitHub" *(não verificado em 07/10/2026)*.

| Modelo | Contexto | Preço (por 1M, após o crédito) | Destaques |
| :--- | :---: | :---: | :--- |
| **Mercury 2.5** (`mercury-2.5` — ID exato a confirmar em `/v1/models`) | 260K | $0.20 / $0.75 (lançamento: $0.04 / $0.15, 80% OFF) | Raciocínio ajustável, tool calling paralelo, JSON por schema |
| **`mercury-2`** | 128K | $0.25 / cache $0.025 / $0.75 | Tool calling, structured outputs |
| **Mercury Edit 2** | 32K (FIM / NextEdit) | $0.25 / cache $0.025 / $0.75 | Endpoints `/v1/fim/completions` e `/v1/edit/completions` |

* ⚠️ Os IDs `mercury-chat` / `mercury-coder` (v15–v18) estão **obsoletos**. RPM 60 / concorrência 5 *(não verificado em 07/10/2026)*.

---

### 🔮 REKA AI — Créditos Recorrentes Mensais & Vídeo Multimodal ⚠️ *(não verificado em 07/10/2026)*
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

### 📦 BYTEZ — $1.00 Renovado a Cada 4 Semanas ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://bytez.com/](https://bytez.com/)
* **Endpoint Base**: `https://api.bytez.com/v1` (Compatível nativo com OpenAI SDK)
* **Requisitos**: ❌ **Zero Cartão de Crédito**
* **Cota Recorrente**: **$1.00 USD de crédito gratuito renovado a cada 4 semanas (28 dias)**.
* **Poder de Compra do $1**: Como a inferência na Bytez custa frações de centavos para modelos abertos, $1 permite rodar entre **2.000.000 e 5.000.000 de tokens** por ciclo de renovação.
* **Modelos Disponíveis**: `meta-llama/llama-3.3-70b-instruct`, `qwen/qwen-2.5-72b-instruct`, `mistralai/mistral-7b-instruct`.

---

### ⚡ MORPH LABS (Fast Apply) — Acelerador de Agentes de Código ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://morphllm.com/](https://morphllm.com/)
* **Endpoint Base**: `https://api.morphllm.com/v1`
* **Requisitos**: ❌ **Zero Cartão de Crédito**
* **Cota Gratuita Permanente**: **250.000 créditos / mês gratuitos ($0)** e até 200 requisições mensais de Fast Apply.
* **O que Resolve**: Desenvolvido especificamente para agentes autônomos de código (estilo Cline, Cursor, Aider). Aplica diffs gigantescos e alterações de arquivos em menos de 1 segundo sem re-gerar o arquivo inteiro, economizando 90% de tokens de saída.

---

### 🖥️ MODAL LABS — Nuvem Serverless de GPUs ($30/Mês Grátis) ⚠️ *(não verificado em 07/10/2026)*
* **Console**: [https://modal.com/](https://modal.com/)
* **Cota Recorrente**: **$30 USD em créditos de computação gratuitos por mês** no plano Starter.
* **Requisitos**: 🟠 **Requer Cartão de Crédito** para destravar os $30 (sem cartão limita a $5).
* **Para que serve**: Permite subir instâncias de vLLM, Ollama, Whisper ou geração de imagens em GPUs A10G / L4 / H100 sob demanda com desligamento a zero em segundos quando ocioso.

---

### 🌏 JOIAS DE SOBERANIA REGIONAL & GATEWAYS ULTRARRÁPIDOS — *movidos para o Apêndice A.3 na v19*

InternLM (China doméstica), Sarvam AI (línguas da Índia), SEA-LION (línguas do Sudeste Asiático) e LLM7.io (gateway anônimo) foram movidos para o **Apêndice A.3**: irrelevantes para português e/ou sem operador identificável para produção.

---

### ⚠️ AUDITORIA & EXCLUSÕES DE SEGURANÇA (FALSOS FREE TIERS & ALERTAS) ⚠️ *(não verificado em 07/10/2026)*

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

> **Nota v19**: Cartesia (Pilar 2) e StepFun / 01.AI / ModelScope (Pilar 4) foram movidos para o Apêndice A; xAI (Pilar 1) foi corrigido. Os demais itens dos pilares estão *(não verificado em 07/10/2026)*; IDs como Llama 3.x, Qwen 2.5 e DeepSeek-V3/R1 nesses provedores podem estar desatualizados.

---

#### 🚀 PILAR 1: 5 PROVEDORES DE LLMS E INFERÊNCIA SERVERLESS DE ALTA VELOCIDADE

Provedores especializados em latência mínima no primeiro token (TTFT) e taxas extremas de geração (150 a 300 tokens/segundo) para orquestrações de agentes e processamento massivo:

##### 1. Fireworks AI (fireworks.ai) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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
| **`accounts/fireworks/models/qwen2p5-72b-instruct`** | Qwen 2.5 72B Instruct | Texto | 131.072 / 8.192 | 600 RPM / 10k TPM | $0.20 / $0.20 por 1M | Alta inteligência analítica e exatas ⚠️ *ID legado/obsoleto (v19)* |
| **`accounts/fireworks/models/deepseek-v3`** | DeepSeek-V3 MoE | MoE Texto | 131.072 / 8.192 | 600 RPM / 10k TPM | $0.20 / $0.28 por 1M | Modelo MoE de 671B parâmetros com 37B ativos |
| **`accounts/fireworks/models/deepseek-r1`** | DeepSeek-R1 Reasoner | Raciocínio | 131.072 / 16.384 | 600 RPM / 10k TPM | $0.55 / $2.19 por 1M | Raciocínio profundo e cadeias de pensamento completas |
| **`accounts/fireworks/models/firefunction-v2`** | FireFunction v2 | Tool Calling | 8.192 / 4.096 | 600 RPM / 10k TPM | $0.20 / $0.20 por 1M | Especializado em invocação estruturada de ferramentas JSON |

##### 2. Clarifai (clarifai.com) — *STATUS: ENCERRADO / ABSORVIDO NA NEBIUS EM 17/07/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Status**: ❌ **PLATAFORMA INDEPENDENTE ENCERRADA DEFINITIVAMENTE**.
* **Diagnóstico Operacional**: Em maio de 2026, a Clarifai foi adquirida pela empresa de infraestrutura de IA **Nebius** (NASDAQ: NBIS). Em 17 de julho de 2026, os serviços da plataforma independente Clarifai (APIs `api.clarifai.com`, modelos customizados e portal) foram oficialmente desligados. A equipe de pesquisa e a tecnologia de orquestração de inferência foram migradas para o **Nebius Token Factory** (`api.studio.nebius.ai`).
* **Ação Recomendada**: Desenvolvedores devem descontinuar o uso da biblioteca `clarifai` e migrar para o **Nebius Token Factory** (AI Builder Program) ou para gateways multimodais ativos como **Google AI Studio** e **OpenRouter Free**.

##### 3. Baseten (baseten.co) — *Validado em 29/09/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://baseten.co/](https://baseten.co/)
* **Endpoint Base**: `https://bridge.baseten.co/v1` ou `https://model-<model_id>.api.baseten.co/v1` (Compatível nativo com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: 🟠 **EXIGE cartão de crédito** cadastrado no workspace para desbloqueio dos créditos de teste.
* **Verificação**: E-mail profissional / GitHub + Cartão de crédito válido.
* **Tipo de Cota Free**: **$30.00 USD em créditos de computação gratuitos** concedidos no onboarding de desenvolvedor.
* **Arquitetura & Deploy**: Permite servir modelos open-source utilizando **Truss** (framework open-source da Baseten) e **vLLM / SGLang** em GPUs A100/H100, com desligamento automático a zero (scale-to-zero) quando inativo para não desperdiçar créditos.
* **Limites de Taxa**: Até 60 RPM no bridge compartilhado; taxa de throughput dependente do número de réplicas ativas.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limite / Cota | Requisitos | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B Bridge | Texto | 131.072 / 4.096 | $30 em créditos | ❌ Sem Cartão | Inferência de altíssima velocidade em GPUs A100 dedicadas |
| **`deepseek-ai/DeepSeek-V3`** | DeepSeek-V3 Bridge | MoE Texto | 131.072 / 8.192 | $30 em créditos | ❌ Sem Cartão | Deploy de MoE com otimização de tensor parallelism |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`** | Qwen 2.5 Coder 32B | Programação | 131.072 / 8.192 | $30 em créditos | ❌ Sem Cartão | Especializado em análise e refatoração de código com vLLM ⚠️ *ID legado/obsoleto (v19)* |
| **`mistralai/Mistral-Small-24B-Instruct-2501`** | Mistral Small 24B | Raciocínio | 32.768 / 4.096 | $30 em créditos | ❌ Sem Cartão | Modelo intermediário ultrarrápido com TTFT sub-200ms |

##### 4. Replicate (replicate.com) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

##### 5. xAI Console / Grok API (console.x.ai) — *Revisado em 07/10/2026*
* **Console / Cadastro**: [https://console.x.ai/](https://console.x.ai/)
* **Endpoint Base**: `https://api.x.ai/v1` (Compatível com OpenAI SDK)
* 🚨 **Correção v19**: o "Developer Grant de **US$25/mês sem cartão**" **não existe mais**. O programa atual concede **US$150/mês em créditos** a equipes que **aceitam compartilhar dados** com a xAI, **após gastar ao menos US$5** na API; a adesão é por equipe, feita por admin, e **não pode ser desfeita** (fonte: busca em 07/10/2026 apontando docs.x.ai; confirmar antes de aderir).
* **A API é paga** (créditos pré-pagos ou fatura mensal); o Playground do console é gratuito.
* **Modelo atual**: Grok 4.7 — **$2 / $6** por 1M tokens (até 200K de contexto) e **$4 / $12** acima de 200K.
* ⚠️ `grok-2-1212`, `grok-2-vision-1212`, `grok-beta` e `grok-vision-beta` estão **obsoletos**. Os limites "60 RPM / 10K TPM" *(não verificado em 07/10/2026)*.
* ⚠️ O programa de compartilhamento de dados é **incompatível com dados pessoais** (LGPD).

---

#### 🎙️ PILAR 2: 5 ESPECIALISTAS EM VOZ, ÁUDIO, STT E TTS

Provedores dedicados à transcrição de fala em texto (Speech-to-Text) com acurácia ultra-alta e síntese de voz (Text-to-Speech) de baixa latência para agentes conversacionais:

##### 6. Deepgram (deepgram.com) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

##### 7. AssemblyAI (assemblyai.com) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

##### 8. ElevenLabs (elevenlabs.io) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

###### 9. Cartesia (cartesia.ai) — *movido para o Apêndice A.4 na v19 (free tier não comercial)*

##### 10. Lemonfox.ai (lemonfox.ai) — *Validado em 29/09/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://lemonfox.ai/](https://lemonfox.ai/)
* **Endpoint Base**: `https://api.lemonfox.ai/v1` (Compatível 1:1 com a API de Áudio da OpenAI)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** no trial.
* **Verificação**: E-mail simples para geração instantânea de chave de API.
* **Mecânica de Acesso**: Opera sob um **Trial de Boas-Vindas de 1 Mês** (com até 10 Milhões de créditos gratuitos, equivalendo a ~30 horas de transcrição Whisper ou ~2 milhões de caracteres TTS). Após o período de avaliação, o acesso é mantido através de planos budget ultra-acessíveis a partir de **$5.00 USD / mês**.
* **Compatibilidade Drop-in**: Substitui diretamente as rotas `/v1/audio/transcriptions` e `/v1/audio/speech` da OpenAI em bibliotecas e agentes existentes, apenas mudando `base_url` e `api_key`.
* **Limites de Taxa**: 20 RPM no período de trial e planos budget.

| Modelo ID API (Canônico) | Display Name | Modalidade | Compatibilidade | Limites de Taxa | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`whisper-1`** | Lemonfox Whisper STT | STT / Transcrição | OpenAI `/audio/transcriptions` | 20 RPM | Transcrição precisa de áudio com timestamps de palavras |
| **`lemonfox-tts-v1`** | Lemonfox TTS Engine | TTS / Síntese | OpenAI `/audio/speech` | 20 RPM | Geração de áudio MP3 a partir de texto com múltiplas vozes |
| **`lemonfox-embed-v1`** | Lemonfox Embeddings | Embeddings de Texto | OpenAI `/embeddings` | 20 RPM | Vetorização semântica rápida para busca e similaridade |

---

#### 🔍 PILAR 3: 5 ESPECIALISTAS EM EMBEDDINGS, RERANK & BUSCA NEURAL PARA AGENTES

Plataformas de infraestrutura vetorial e pesquisa em tempo real construídas especificamente para agentes autônomos e sistemas RAG de alta fidelidade:

##### 11. Voyage AI (voyageai.com) — *Validado em 29/09/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://dash.voyageai.com/](https://dash.voyageai.com/)
* **Endpoint Base**: `https://api.voyageai.com/v1/embeddings` e `https://api.voyageai.com/v1/rerank` (REST e SDK Python `voyageai`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google / GitHub.
* **Tipo de Cota Free**:
  * **200 Milhões de tokens gratuitos** de trial para modelos modernos de ponta (`voyage-4`, `voyage-context-4`, `voyage-code-4`, multimodal).
  * **50 Milhões de tokens gratuitos** para modelos especializados e de geração anterior (`voyage-multilingual-2`, `voyage-finance-2`, `voyage-law-2`).
  * *Nota*: Os tokens gratuitos não se aplicam ao endpoint Batch API.
* **Reputação na Indústria**: O motor Voyage AI é oficialmente recomendado pela Anthropic para RAG com a família Claude, superando modelos de embedding da OpenAI em quase todos os benchmarks MTEB. Suporta janelas gigantes de **32.000 tokens por documento**.
* **Limites de Taxa**: **300 RPM**, **1.000.000 TPM** no Free Tier.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto / Dimensões | Limites de Taxa | Cota Gratuita | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`voyage-3`** | Voyage-3 General Embedding | Embeddings | 32.000 ctx / 1024 dims | 300 RPM / 1M TPM | 200M tokens trial | Top #1 mundial em recuperação densa de texto geral |
| **`voyage-3-lite`** | Voyage-3-Lite Fast | Embeddings | 32.000 ctx / 512 dims | 300 RPM / 1M TPM | 200M tokens trial | Dimensionalidade compacta para indexação rápida e econômica |
| **`voyage-code-3`** | Voyage Code 3 | Embeddings Código | 32.000 ctx / 1024 dims | 300 RPM / 1M TPM | 200M tokens trial | Especializado em código-fonte, bibliotecas e documentação técnica |
| **`rerank-2`** | Voyage Rerank 2 | Reranking RAG | 16.000 ctx / Cross-Enc | 300 RPM / 1M TPM | 200M tokens trial | Reordenação de máxima precisão para os top 5-10 chunks do RAG |
| **`rerank-2-lite`** | Voyage Rerank 2 Lite | Reranking Rápido | 8.000 ctx / Cross-Enc | 300 RPM / 1M TPM | 200M tokens trial | Latência inferior a 50ms para buscas em tempo real |

##### 12. Jina AI (jina.ai) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://cloud.jina.ai/](https://cloud.jina.ai/)
* **Endpoints Base**:
  * Embeddings & Rerank: `https://api.jina.ai/v1/embeddings` e `https://api.jina.ai/v1/rerank`
  * Reader API: `https://r.jina.ai/<url>` (Converte qualquer URL em markdown limpo)
  * Search Grounding: `https://s.jina.ai/<query>` (Busca web direto em markdown)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / GitHub.
* **Tipo de Cota Free**:
  * **10 Milhões de tokens gratuitos** de boas-vindas no console para embeddings e rerankers.
  * **Jina Reader API (`r.jina.ai`) 100% GRATUITA E PERPÉTUA** (20 RPM anônimo sem chave; 500 RPM com chave free).
* **Limites de Taxa**: **500 RPM** nos endpoints de API com chave gratuita.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto / Dimensões | Limites de Taxa | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`jina-embeddings-v3`** | Jina Embeddings v3 | Embeddings | 8.192 ctx / 1024/512/256 dims | 500 RPM | Suporta Matryoshka Learning (dimensões flexíveis) e 89 línguas |
| **`jina-reranker-v2-base-multilingual`**| Jina Reranker v2 | Reranking | 8.192 ctx / Cross-Encoder | 500 RPM | Suporta Function Calling rerank e recuperação em múltiplos idiomas |
| **`jina-colbert-v2`** | Jina ColBERT v2 | Multi-Vector | 8.192 ctx / Token-level | 500 RPM | Busca granular em nível de token com alta interpretabilidade |
| **`r.jina.ai`** | Jina Reader Engine | Web Scraper LLM | Ilimitado (URL) | 20 a 500 RPM | Transforma páginas dinâmicas e JS em markdown limpo sem anúncios |

##### 13. Tavily AI (tavily.com) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

##### 14. Exa.ai (exa.ai — antigo Metaphor) — *Validado em 29/09/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://dashboard.exa.ai/](https://dashboard.exa.ai/)
* **Endpoint Base**: `https://api.exa.ai/search` (REST e SDK oficial `exa-py`)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google.
* **Tipo de Cota Free**: **Cota Recorrente de $10.00 USD / Mês em créditos gratuitos** renovados no dia 1º de cada mês (~1.400 buscas semânticas padrão/mês) + **$10.00 USD de bônus único de onboarding** ao completar o perfil sem cartão.
* **Busca Neural Semântica**: O Exa utiliza um modelo de linguagem treinado para prever links da web com base no significado semântico do prompt, e não apenas em correspondência de palavras-chave.
* **Limites de Taxa**: **60 RPM**, **~1.400 buscas mensais gratuitas**.

| Modo de Busca (`type`) | Opções de Extração | Limites de Taxa | Custo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :--- |
| **`"neural"`** | `text: true`, `highlights: true` | 60 RPM | 1 crédito / busca | Procura por sentido conceitual ("sites de ferramentas AI indie promissoras") |
| **`"keyword"`** | `text: true` | 60 RPM | 1 crédito / busca | Busca lexical exata quando se procura por nomes de funções ou identificadores |
| `use_autoprompt` | `true` | 60 RPM | Gratuito | Otimiza automaticamente a consulta do usuário em uma query semântica |

##### 15. Qdrant Cloud (qdrant.tech) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

##### 16–18. StepFun, 01.AI e ModelScope — *movidos para o Apêndice A.2 na v19 (plataformas chinesas domésticas)*

##### 19. RunPod Serverless (runpod.io) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

##### 20. CentML / CServe (centml.ai) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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
| **`meta-llama/Llama-3.1-8B-Instruct`** | Llama 3.1 8B CServe | Texto | 131.072 / 4.096 | 60 RPM / 100k TPM | Velocidade extrema para pipelines de extração e triagem rápida ⚠️ *ID legado/obsoleto (v19)* |
| **`mistralai/Mistral-Small-24B-Instruct-2501`**| Mistral Small 24B CServe| Raciocínio | 32.768 / 4.096 | 60 RPM / 100k TPM | Desempenho equilibrado para síntese de documentos e agentes |


## 4. ESTRATÉGIA RECOMENDADA POR CARGA DE TRABALHO (v19 — substitui a "Cadeia de Fallback" v11–v18)

> **Por que mudou**: a cadeia de 50 níveis da v18 era apresentada como arquitetura "para produtos em produção sem custo de API". **Esse enquadramento foi removido.** Vários níveis **proíbem produção** (NVIDIA NIM trial, Mistral Free, trials não comerciais), outros **treinam com os dados** (Gemini Free, Mistral Free por padrão, modelos free do OpenCode Zen) e outros têm **operador não identificado** (xKiro, gateways anônimos). Empilhar dezenas de free tiers também incentiva burlar limites (Seção 5). A cadeia antiga foi preservada, só para consulta histórica, no **Apêndice A.5**.

### 4.1 Premissas de custo (cálculo próprio, não é dado oficial)

* **Agente da escola**: 3 chamadas de LLM por conversa; ~4.400 tokens de entrada por chamada (≈ 50% cacheáveis quando o provedor tem cache) e ~200 tokens de saída; mês de 30 dias.
* **Volume normal**: 100 conversas/dia = **9.000 chamadas/mês**. **Pico de matrícula**: 500 conversas/dia = **45.000 chamadas/mês**.
* **Câmbio**: PTAX de 06/10/2026 = **R$ 4,9698 / US$**.
* Modelos de raciocínio (gpt-oss, DeepSeek, MiMo, GLM) gastam tokens extras de saída; os valores abaixo indicam a premissa usada.

### 4.2 (a) Agente da escola (WhatsApp) — dados pessoais de crianças e responsáveis

| Papel | Provedor / Modelo | Justificativa |
| :--- | :--- | :--- |
| **Principal** | **Maritaca `sabiazinho-4-br-sp`** | Empresa brasileira; DPA sob a LGPD; conteúdo da API descartado logo após a resposta; sem treino; inferência 100% no Brasil (`-br-sp`); sem cláusula contra usuários finais menores |
| **Fallback** | **Groq `openai/gpt-oss-120b`** no plano Developer **pago** + **Zero Data Retention** | Barato e rápido; sem cláusula sobre usuários finais menores. Exige base legal e cláusulas-padrão (Res. CD/ANPD 19/2024) para a transferência aos EUA. **Não mandar dados de saúde/inclusão no fallback.** |
| **Áudio (STT)** | **Groq `whisper-large-v3-turbo`** (pago + ZDR) | $0.04 por hora de áudio. No LyrIA, o `audio_transcribe` do `cascade.py` só funciona se Groq estiver no `PROVIDER_ORDER`. |
| **Dev / teste** | Gemini Free, Groq Free, créditos Inception | **Somente com dados sintéticos** |
| **Não usar** | Gemini (Free **e** Pago — cláusula de menores de 18), DeepSeek, xKiro, NVIDIA NIM, Cerebras (`llama-3.3-70b`), OpenRouter `:free`, Mistral Free, plataformas chinesas, gateways anônimos | Termos de uso e/ou LGPD |

**`PROVIDER_ORDER` alvo (LyrIA-CRM `bot/llm/cascade.py`)**:
```env
PROVIDER_ORDER=Maritaca,Groq
MARITACA_MODEL=sabiazinho-4-br-sp
GROQ_MODEL=openai/gpt-oss-120b
GROQ_WHISPER_MODEL=whisper-large-v3-turbo
```
* Exige uma **pequena mudança de código**: adicionar o provider "Maritaca" no `cascade.py` (base_url `https://chat.maritaca.ai/api`, `MARITACA_API_KEY_1/2`, `MARITACA_MODEL`) e repassar as variáveis no `docker-compose.yml`. Antes: validar `/chat/completions`, medir qualidade com um conjunto de testes, conferir rate limits e assinar o DPA.
* **Provisório, sem mudar código**: `PROVIDER_ORDER=Groq` com `GROQ_MODEL=openai/gpt-oss-120b` (pago + ZDR) e `GROQ_WHISPER_MODEL=whisper-large-v3-turbo`.
* **Remover** do `PROVIDER_ORDER` atual (`xKiro,Groq,Cerebras,NIM`): **xKiro, Cerebras e NIM**.

**Custos estimados (agente da escola)**:

| Opção | Normal (9.000 chamadas/mês) | Pico (45.000 chamadas/mês) | Premissa |
| :--- | :---: | :---: | :--- |
| Maritaca `sabiazinho-4-br-sp` | **≈ R$ 61/mês** | **≈ R$ 304/mês** | Sem desconto de cache/noturno |
| Maritaca `sabiazinho-4` (sem residência no Brasil) | ≈ R$ 47/mês | ≈ R$ 234/mês | Sem desconto de cache/noturno |
| Groq `openai/gpt-oss-120b` | ≈ US$ 8,64 (≈ R$ 43) | ≈ US$ 43,20 (≈ R$ 215) | Sem cache; ~500 tokens de saída incluindo raciocínio. Como fallback, só custa quando é acionado |
| Groq Whisper | ≈ US$ 1–3/mês | — | Estimativa; depende do volume de áudio |
| *Referência: Gemini 3.1 Flash-Lite pago* | *≈ US$ 8,14* | *≈ US$ 40,73* | *Descartado pela cláusula de menores de 18* |

**Ações LGPD obrigatórias**: melhorar o anonimizador local (nomes em minúsculas; retirar dados de saúde, alergias e inclusão antes de qualquer envio); RIPD/relatório de impacto; base legal para dados de crianças (art. 14) e dados sensíveis (art. 11); contratos/DPA com cada operador; registro da transferência internacional do fallback (art. 33).

### 4.3 (b) Cargas sem dados pessoais (motor_viral, conteúdo, roteiros MicroBio IA, análises tipo Crivo)

Aqui os free tiers são aceitáveis, **dentro dos termos** (uma conta por provedor, sem rodízio de contas):

1. **Google AI Studio Free** — `gemini-3.1-flash-lite` / `gemini-3.5-flash-lite`; `gemini-2.5-flash` quando precisar de Search Grounding grátis (até 500 RPD).
2. **Groq Free** — `openai/gpt-oss-120b` (30 RPM / 1.000 RPD / 8K TPM / 200K TPD).
3. **Cloudflare Workers AI** — 10.000 Neurons/dia (`@cf/openai/gpt-oss-120b`, `@cf/zai-org/glm-4.7-flash`).
4. **Inception** — crédito único de 100M tokens (Mercury 2.5).
5. **Z.ai `glm-4.7-flash`** (grátis).
6. **Pago barato (rede de segurança)** — DeepSeek `deepseek-flash` fora de pico com thinking desligado, ou MiMo `mimo-v2.6-flash`.

**`PROVIDER_ORDER` sugerido (provedores que o `cascade.py` já suporta)**:
```env
PROVIDER_ORDER=Google,Groq,DeepSeek
GOOGLE_MODEL=gemini-3.1-flash-lite
GROQ_MODEL=openai/gpt-oss-120b
# DeepSeek: modelo deepseek-flash (o padrão atual no código é deepseek-v4-flash, ainda aceito)
```
* Cloudflare, Inception, Z.ai e MiMo exigem novas entradas de provider no código. Para desligar o thinking (DeepSeek/MiMo), o `cascade.py` precisa aceitar `extra_body`.
* **`core/llm_router.py`** (motor_b2b / motor_viral / pixeltech_engine): trocar o SDK obsoleto `google.generativeai` e substituir os modelos Groq obsoletos (`qwen/qwen3.6-27b`, `qwen-2.5-32b`, `gemma2-9b-it`, `mixtral-8x7b-32768`) por `openai/gpt-oss-120b` / `openai/gpt-oss-20b` / `qwen/qwen3.8-27b`.
* ⚠️ **motor_b2b**: se processar nome, e-mail ou telefone de pessoas de contato, **é dado pessoal** (LGPD) — retirar esses dados antes de enviar a free tiers que treinam, ou usar rota paga sem treino.
* **Custo estimado**: ≈ **US$ 0–5/mês**.

### 4.4 (c) Agentes de código

* **Principal**: Codex (plano ChatGPT já pago).
* **API barata**: MiMo `mimo-v2.6-flash` ($0.14 / $0.28) ou DeepSeek `deepseek-flash` fora de pico ($0.15 / $0.60) — só repositórios sem segredos.
* **Assinaturas (somente dentro de ferramentas de código)**: OpenCode Go $10/mês; MiMo Token Plan Lite $6/mês; Alibaba Token Plan Lite $6/mês (promoção); GLM Coding Plan a partir de $18/mês; MiniMax M Plan Go $22/mês.
* **Grátis**: crédito de 100M tokens da Inception; modelos free do OpenCode Zen (podem treinar com o código — nada de código de cliente).
* **Groq Free não serve** para agentes de código: 8K TPM é menor que um único contexto grande.
* **Nunca** colocar `.env`, chaves ou dados reais de clientes no contexto do agente.
* `PROVIDER_ORDER`: não se aplica (agentes de código usam a configuração da própria ferramenta).
* **Custo estimado**: ≈ **US$ 5–15/mês** além do Codex.

### 4.5 O que saiu da estratégia (e por quê)

| Item da v18 | Motivo |
| :--- | :--- |
| NVIDIA NIM em produção | Trial; produção proibida pelos termos |
| xKiro | Operador não identificado; repasse a terceiros não nomeados; cota "5M/dia" não confirmada |
| Cerebras `llama-3.3-70b` | Modelo descontinuado |
| Groq `llama-3.x` | Movido para Enterprise |
| DeepSeek `deepseek-chat`/`reasoner` com preços antigos | IDs, preços e janela de pico errados; dados na China |
| Gemini 1.5 / 2.0 | Desligados |
| xAI "US$25/mês" / grok-2 | Programa inexistente; modelos obsoletos |
| Gateways anônimos, AwanLLM, Pollinations em produção | Sem operador/DPA identificável |
| Plataformas chinesas domésticas | Dados na China; cadastro local; não verificado |
| Trials não comerciais (Cohere, Cartesia) | Uso comercial vedado |

---

## 5. TERMOS DE USO & LGPD (v19) 🆕

1. **Nada de empilhar contas ou chaves para multiplicar cotas grátis.** Google APIs Terms (seção 1d): proibido tentar contornar limites. Groq: limites por organização. OpenRouter: "contas ou chaves adicionais não afetam os limites". xKiro: proíbe burlar cotas. Z.ai: uso anormal aciona restrições. ➜ As 2 chaves por provedor do `cascade.py` (`*_API_KEY_1/2`) só são aceitáveis como **redundância da mesma conta/organização paga**, nunca como contas diferentes para somar free tiers.
2. **Nada de revenda.** Google APIs Terms proíbem sublicenciar a API a terceiros; xKiro proíbe revender sem permissão. Não montar "API barata" para terceiros em cima de free tiers.
3. **Trials são para avaliação.** NVIDIA NIM (produção proibida), Mistral Free (avaliação/protótipo).
4. **Planos de assinatura de coding não são API de backend.** Alibaba Token Plan proíbe backend/automação; Z.ai só em ferramentas suportadas; MiniMax orienta pay-as-you-go para produção.
5. **Quem treina ou pode treinar com os dados**: Gemini Free (com revisão humana), Mistral Free (padrão, com opt-out), modelos free do OpenCode Zen, DeepSeek (desidentificado, com opt-out), MiniMax (termos permitem usar entradas para melhorar serviços), xAI (programa de compartilhamento de dados). ➜ Nunca enviar dados pessoais.
6. **Gateways anônimos e modelos "uncensored"** (AI Horde, UncloseAI, LLM7.io, AwanLLM, DuckDuckGo AI Chat sem API): **nunca em produção** nem com dados pessoais (Apêndice A.1).
7. **Trials não comerciais**: Cohere Trial Key e Cartesia Free (conforme a v18; *não verificado em 07/10/2026*) — só experimentação (Apêndice A.4).
8. **Cláusula de idade**: Gemini API (Free **e** Pago) proíbe uso em serviços dirigidos ou prováveis de serem acessados por menores de 18 anos. Groq e Maritaca exigem 18+ apenas do titular da conta.
9. **LGPD — dados da escola**:
   * **Art. 11** (dados sensíveis, ex.: saúde, alergias, inclusão): base legal específica e minimização; não enviar a provedores no exterior quando evitável.
   * **Art. 14** (crianças e adolescentes): tratamento no melhor interesse; consentimento específico de pelo menos um dos pais/responsável quando aplicável.
   * **Art. 33** (transferência internacional): cláusulas-padrão contratuais da **Res. CD/ANPD nº 19/2024** ou outro mecanismo válido para qualquer provedor fora do Brasil (Groq/EUA, MiMo/Singapura, etc.).
   * Exigir DPA de cada operador; preferir residência no Brasil (Maritaca `-br-sp`); ZDR quando disponível.
10. **IDs legados/obsoletos (não usar em código novo)**: `llama-3.1-*` (Groq: Enterprise; demais provedores: legado), `llama-3.3-70b` (Cerebras: descontinuado; Groq: Enterprise), `Qwen2.5-*` / `qwen-2.5-*`, `gemini-1.5-*`, `gemini-2.0-*` (desligados em 01/06/2026), `mixtral-8x7b-32768`, `gemma2-9b-it`, `qwen/qwen3.6-27b`, `grok-2*`, `mercury-chat`/`mercury-coder`.


---

## 6. RELATÓRIO DE AUDITORIA & VALIDAÇÃO REAL EM RUNTIME

### Revisão v19 — Fontes oficiais consultadas em 07/10/2026

| Provedor | Fonte consultada | Achado principal |
| :--- | :--- | :--- |
| **Google Gemini** | ai.google.dev: pricing, terms, deprecations | 2.0 Flash desligado em 01/06/2026; 2.5 Pro sem data de desligamento; sem Grounding no Free na série 3.x; Free usado para melhorar produtos; cláusula de menores de 18 (Free e Pago) |
| **Groq** | console.groq.com/docs/models, /docs/rate-limits, Services Agreement | Llama 3.x → Enterprise; gpt-oss 30 RPM / 1K RPD / 8K TPM / 200K TPD; Whisper 20 RPM / 2K RPD; limites por organização; preços pagos |
| **Cerebras** | Documentação de deprecações | `llama-3.3-70b` e `qwen-3-32b` descontinuados → `gpt-oss-120b` |
| **NVIDIA NIM** | API Trial Terms + FAQ | Somente teste/avaliação; produção exige licença; limites não publicados |
| **OpenRouter** | docs/api-reference/limits | 20 RPM `:free`; limite diário depende de créditos comprados; contas extras não ajudam |
| **Mistral** | Help Center / docs | Free = avaliação/protótipo; limites por organização e modelo |
| **DeepSeek** | Página de modelos & preços; política de privacidade | `deepseek-flash`; pico $0.30/$0.006/$1.20; fora de pico $0.15/$0.003/$0.60; dados na China |
| **Maritaca** | maritaca.ai/api, /planos, /tratamento-de-dados, /dpa, /termos | Sem free tier de API; R$ 20 de crédito; `-br-sp`; sem treino; DPA LGPD |
| **Cloudflare Workers AI** | developers.cloudflare.com (pricing, 01/10/2026) | 10K Neurons/dia; $0.011/1K Neurons; modelos frontier exigem pagamento |
| **Inception** | docs.inceptionlabs.ai | 100M tokens únicos; `mercury-2` / Mercury 2.5 |
| **xAI** | Busca (docs.x.ai) | US$150/mês com compartilhamento de dados após gasto de US$5; Grok 4.7 |
| **xKiro** | docs.xkiro.com, /terms, /privacy, /about | Cota free varia; operador não identificado; proíbe burlar cotas e revender |
| **Xiaomi MiMo** | mimo.mi.com (preços, Token Plan) | v2.6-flash $0.14/$0.28; Token Plan $6–$100 |
| **Z.ai** | docs.z.ai (devpack) | GLM Coding Plan a partir de $18; só ferramentas suportadas |
| **MiniMax** | platform.minimax.io (M Plan) | Go $22/mês; PAYG para produção |
| **OpenCode** | opencode.ai/docs/go, /docs/zen | Go $10 / Go Plus $40; modelos free do Zen podem treinar |
| **Alibaba** | alibabacloud.com (Token Plan) | $6–$68/mês (promoção); proibido em backends |

### Validação Executada em 29/09/2026 (Consolidado v17 — histórico; ⚠️ não reverificado em 07/10/2026; ver correções da v19 acima)

| Provedor Auditado | Endpoint Validado | Modelos no Catálogo | Status de Resposta | Diagnóstico / Achados Operacionais (29/09) |
| :--- | :--- | :---: | :---: | :--- |
| **Fireworks AI** 🚀 | `api.fireworks.ai/inference/v1` | **5 modelos** | ✅ **HTTP 200** | $1 USD trial sem cartão; FireAttention ultra-rápida (250 t/s) em Llama 3.3 e DeepSeek |
| **Clarifai** 🚨 | `api.clarifai.com/v2` | - | ❌ **Encerrado 17/07/2026**| Adquirida pela Nebius; plataforma e APIs desligadas em 17/07/2026 (absorvida na Token Factory) |
| **Baseten** 🚀 | `bridge.baseten.co/v1` | **4 modelos** | ⚠️ **Requer Cartão** | $30 USD em créditos para deploy serverless Truss/vLLM (exige cartão no cadastro) |
| **Replicate** 🚀 | `api.replicate.com/v1` | **4 modelos** | ✅ **HTTP 200** | Créditos de teste de desenvolvedor sem cartão para LLMs, FLUX e visão |
| **xAI Console (Grok)** 🚀 | `api.x.ai/v1` | **4 modelos** | ✅ **HTTP 200** | $25 USD/mês em developer grants para Grok-2/Grok-vision sem cartão ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **Deepgram** 🎙️ | `api.deepgram.com/v1` | **5 modelos** | ✅ **HTTP 200** | $200 USD em créditos perpétuos sem cartão; ~775h de transcrição Nova-2 e Aura TTS |
| **AssemblyAI** 🎙️ | `api.assemblyai.com/v2` | **3 modelos** | ✅ **HTTP 200** | $50 USD em créditos sem cartão; ~100-330h de transcrição Conformer-2/nano e LeMUR |
| **ElevenLabs** 🎙️ | `api.elevenlabs.io/v1` | **3 modelos** | ✅ **HTTP 200** | Cota perpétua de 10.000 chars/mês sem cartão para síntese vocal hiper-realista |
| **Cartesia** 🎙️ | `api.cartesia.ai/tts/bytes` | **3 modelos** | ✅ **HTTP 200** | Free Tier permanente de 20.000 créditos/mês (Sonic-3 TTS, latência <150ms) sem cartão ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **Lemonfox.ai** 🎙️ | `api.lemonfox.ai/v1` | **3 modelos** | ✅ **HTTP 200** | Trial de 1 mês (10M créditos) + planos budget $5/mês; Whisper STT e TTS OpenAI-compatível |
| **Voyage AI** 🔍 | `api.voyageai.com/v1` | **5 modelos** | ✅ **HTTP 200** | 200M tokens trial (linha moderna) / 50M tokens (linha legada) sem cartão |
| **Jina AI** 🔍 | `api.jina.ai/v1` / `r.jina.ai` | **4 modelos** | ✅ **HTTP 200** | 10M tokens free + Reader API `r.jina.ai` 100% gratuita perpétua (500 RPM com chave free) |
| **Tavily AI** 🔍 | `api.tavily.com/search` | **Search API** | ✅ **HTTP 200** | 1.000 buscas/mês perpétuas sem cartão para agentes autônomos (LangChain/CrewAI) |
| **Exa.ai** 🔍 | `api.exa.ai/search` | **Neural Search** | ✅ **HTTP 200** | Cota recorrente de $10 USD/mês (~1.400 buscas/mês) + $10 bônus inicial sem cartão |
| **Qdrant Cloud** 🔍 | `cloud.qdrant.io:6333` | **Vector DB** | ✅ **HTTP 200** | Cluster gratuito permanente na nuvem de 1GB RAM / ~1M vetores sem cartão |
| **StepFun** 🌏 | `api.stepfun.com/v1` | **7 modelos** | ✅ **HTTP 200** | ¥50 RMB (~$7 USD) em créditos sem cartão; Step-1 com contexto de até 256k tokens |
| **01.AI (Lingyi)** 🌏 | `api.lingyiwanwu.com/v1` | **6 modelos** | ✅ **HTTP 200** | ¥36 RMB em créditos sem cartão; Yi-Lightning a 100+ tokens/s e Yi-Large 200k |
| **ModelScope** 🌏 | `api-inference.modelscope.cn/v1`| **5 modelos** | ✅ **HTTP 200** | 30 RPM / 1.000 RPD 100% gratuitos perpétuos em cluster comunitário Alibaba DAMO |
| **RunPod Serverless** 💵 | `api.runpod.ai/v2` | **vLLM Endpoints**| ✅ **HTTP 200** | Micro-orçamento de $5 USD com execução serverless por segundo e scale-to-zero |
| **CentML / CServe** 🚀 | `api.centml.com/v1` | **3 modelos** | ✅ **HTTP 200** | Free developer trial com compilação acelerada CServe até 3x mais veloz |
| **Inception Labs** 💎 | `api.inceptionlabs.ai/v1` | **2 modelos** | ✅ **HTTP 200** | 100 Milhões de tokens free creditados no signup sem cartão; Mercury API ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **Reka AI** 💎 | `api.reka.ai/v1` | **3 modelos** | ✅ **HTTP 200** | $10/mês em créditos recorrentes perpétuos + 3h vídeo; multimodal frontier |
| **Bytez** 💎 | `api.bytez.com/v1` | **3 modelos** | ✅ **HTTP 200** | $1.00 USD renovado a cada 4 semanas sem cartão; Llama 3.3 70B e Qwen 72B |
| **Morph Labs** 💎 | `api.morphllm.com/v1` | **Fast Apply** | ✅ **HTTP 200** | 250k créditos/mês ($0) + 200 reqs/mês para diff instantâneo em agentes de código |
| **Modal Labs** 🖥️ | `modal.com` | **GPU Serverless**| ✅ **HTTP 200** | $30 USD/mês compute credits no plano Starter (requer cartão) |
| **InternLM (Shanghai AI)** 💎| `internlm.intern-ai.org.cn` | **3 modelos** | ✅ **HTTP 200** | 1M in / 3M out tokens/mês gratuitos sem cartão para devs |
| **Sarvam AI** 🇮🇳 | `api.sarvam.ai` | **3 modelos** | ✅ **HTTP 200** | ₹1.000 INR em créditos de boas-vindas perpétuos sem cartão; línguas da Índia |
| **SEA-LION (AI SG)** 🇸🇬 | `api.sea-lion.ai/v1` | **2 modelos** | ✅ **HTTP 200** | 10 RPM / 100k TPM permanente sem cartão para Sudeste Asiático |
| **LLM7.io** 💎 | `api.llm7.io/v1` | **Multi-model** | ✅ **HTTP 200** | Gateway anônimo 2 req/s, 20 RPM, 100 req/hr sem cadastro nem chave |
| **Maritaca AI (MariTalk)** 🇧🇷| `chat.maritaca.ai/api` | **5 modelos** | ✅ **HTTP 200** | Cota Tier 0 de 60 RPM / 128k in / 10k out sem cartão; Batch API 4M chars/dia; preços em R$ ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **Cloudflare Workers AI** ☁️ | `api.cloudflare.com` | **10+ modelos** | ✅ **HTTP 200** | 10.000 Neurons/dia gratuitos perpétuos sem cartão (~100k-500k tokens/dia) ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **SambaNova Cloud** ⚠️ | `api.sambanova.ai/v1` | **4 modelos** | ⚠️ **Requer Pagamento** | Transicionou para Developer Tier com exigência de cartão/pagamento (20M tokens/dia) |
| **Nomic & Mixedbread** 🎯 | `api.nomic.ai` / `api.mixedbread.ai` | **Embed/Rerank** | ✅ **HTTP 200** | Vetores e Rerank com cotas gratuitas dedicadas sem onerar chat |
| **Google AI Studio** | `generativelanguage.googleapis.com` | **50 modelos** | ✅ **HTTP 200** | Cotas gerenciadas dinamicamente no AI Studio Console; política de data logging no Free ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **Groq Cloud** | `api.groq.com/openai/v1` | **13 modelos** | ✅ **HTTP 200** | `qwen3.6-27b` desligado (404); `qwen3.8-27b` é o único Qwen ativo ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **NVIDIA NIM** | `integrate.api.nvidia.com/v1` | **82 modelos** | ✅ **HTTP 200** | `z-ai/glm-5.3` e `glm-5.3-flash` ativos; 40 RPM / 1.000 RPD sem cartão ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **OpenRouter** | `openrouter.ai/api/v1` | **24 free** | ✅ **HTTP 200** | 24 modelos `:free` com Nex N2.5 Pro/Mini, Ling VL e GLM 5.2 ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **Mistral AI** | `api.mistral.ai/v1` | **46 modelos** | ✅ **HTTP 200** | 60 RPM / 4M tokens/mês no plano La Plateforme sem cartão ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **DeepSeek** | `api.deepseek.com` | **2 modelos** | ✅ **HTTP 200** | IDs canônicos `deepseek-chat` e `deepseek-reasoner`; $5 rende 18M-35M+ tokens ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **Zhipu AI BigModel** 🇨🇳| `open.bigmodel.cn/api/paas/v4`| **15+ modelos** | ✅ **HTTP 200** | GLM-4-Flash e GLM-4.7-Flash 100% free perpétuo (1 conc) + 25M tokens bônus |
| **Baidu Qianfan** 🇨🇳 | `aip.baidubce.com/rpc/2.0` | **30+ modelos** | ✅ **HTTP 200** | ERNIE-Speed e ERNIE-Lite permanentemente gratuitos a 300 RPM / 300K TPM |
| **Alibaba Model Studio** 🇨🇳| `dashscope.aliyuncs.com` | **45+ modelos** | ✅ **HTTP 200** | 1M a 2M tokens gratuitos por modelo (Qwen-Turbo/Plus/Max/Long) por 90-180 dias |
| **Tencent Hunyuan** 🇨🇳 | `hunyuan.tencentcloudapi.com`| **10+ modelos** | ✅ **HTTP 200** | Pacote gratuito de 1 ano para Hunyuan-Lite; sem cobrança surpresa |
| **xKiro Gateway** 💵 | `api.xkiro.com/v1` | **40+ modelos** | ✅ **HTTP 200** | Free Tier de 5M tokens/dia sem cartão; recarga de $5 no wallet ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **OpenCode Zen/Go** 💵 | `opencode.ai` | **Curadoria Dev** | ✅ **HTTP 200** | Modelos free nativos (MiMo/MiniMax M2.5 Free); Go entrega $60 em tokens ⚠️ *Corrigido/atualizado na v19 — ver seção do provedor* |
| **B.AI Gateway** 💵 | `api.b.ai/v1` | **20+ modelos** | ✅ **HTTP 200** | 1 USD = 1M créditos; até 90% de desconto dinâmico em horários ociosos |
| **GitHub Models** 🚨 | `models.inference.ai.azure.com` | - | ❌ **Encerrado 30/07/2026**| Aposentado oficialmente pela Microsoft/GitHub em 30 de julho de 2026 |
| **FriendliAI** 🚨 | `api.friendli.ai` | - | ❌ **Falso Free**| Desmentido: 100% faturado pay-per-token comercial, sem free tier perpétuo |
| **Liquid AI** ⚠️ | `liquid.ai` | **LFM 2.5/2.6** | ⚠️ **Sem API Direta**| Sem endpoint self-serve direto; acessar via OpenRouter `:free` ou Hugging Face |
| **CrofAI** 🚨 | `crof.ai` | - | ❌ **HTTP 404/Fraud**| Descontinuado e fora do ar em setembro de 2026; excluído definitivamente |

---

## 7. CHANGELOG HISTÓRICO CONSOLIDADO

| Versão | Data | Principais Mudanças e Marcos Históricos |
| :---: | :---: | :--- |
| **v19** | **07/10/2026** | **🧭 Revisão de Fatos contra Fontes Oficiais, Termos & LGPD e Estratégia Segmentada**: **DeepSeek** reescrito (ID `deepseek-flash`, preços pico/fora de pico, janela de pico 01–04h e 06–10h UTC em dias úteis = 22h–01h e 03h–07h BRT, bônus de 5M removido, thinking por padrão, dados na China). **Gemini**: 2.0 desligado em 01/06/2026, 1.5 fora, 2.5 Pro ativo, sem Grounding no Free na série 3.x, cláusula de menores de 18 (Free e Pago), limites do Free só no AI Studio. **Groq**: Llama 3.x → Enterprise, preços pagos, ZDR, limites por organização. **Cerebras**: `llama-3.3-70b`/`qwen-3-32b` descontinuados. **NIM**: trial sem produção, limites não oficiais. **OpenRouter**: 20 RPM, limite diário depende de créditos, contas extras não ajudam. **xAI**: removido "US$25/mês"; programa de US$150/mês com compartilhamento de dados; grok-2 obsoleto. **Inception**: `mercury-2`/Mercury 2.5; 100M tokens únicos. **Maritaca**: sem free tier de API, R$ 20 de crédito, `-br-sp`, −30% noturno/−50% batch, DPA LGPD. **Mistral**: Free = avaliação; treino por padrão. **xKiro**: cota variável, operador não identificado. **Cloudflare**: preços por modelo e modelos que exigem pagamento. **Novos**: MiMo pay-as-you-go e planos de coding (MiMo Token Plan, GLM Coding Plan, MiniMax M Plan Go, OpenCode Go, Alibaba Token Plan) com restrições de backend. **Seção 4** reescrita por carga de trabalho (escola / sem dados pessoais / coding) com `PROVIDER_ORDER` e custos; **nova Seção 5 — Termos & LGPD**; **Apêndice A** com itens arquivados (gateways anônimos, plataformas chinesas domésticas, SEA-LION, Sarvam, trials não comerciais, cadeia v18). IDs legados marcados. Backup: `freetiers_apis_v18_original.md` / `freetiers_apis_v18_backup.md`. |
| **v18** | **05/10/2026** | **🏆 Auditoria de Início de Outubro, Expansão Multimodal & Reconciliação GA**: Disponibilidade geral (GA) de **Gemini 3.8 Live** e *Live Extended Thinking* via WebSocket; consolidação das tarifas comerciais do **Gemini 3.8 Flash** e cotas dinâmicas do Free Tier no Google AI Studio. Lançamento da arquitetura **DeepSeek-V4.1-Flash** com suporte nativo a visão multimodal; consolidação do roteamento canônico (`deepseek-flash`, `deepseek-chat` e `deepseek-reasoner`) com 50% de desconto Off-Peak (00:30–08:30 UTC+8). Expansão do catálogo de desenvolvedores **NVIDIA NIM** para mais de **90 modelos gratuitos**. Delimitação estrita do nível de experimentação gratuito da **Mistral AI (La Plateforme)** e rotação diária de modelos agregados no **OpenRouter Free**. Backup de segurança mantido em `freetiers_apis.md.bak_v17`. |
| **v17** | **29/09/2026** | **🏆 Auditoria Global de Rigor Máximo, Expurgo de Encerramentos & Sintonia Fina de Cotas**: Expurgo definitivo da **Clarifai** (encerrada e absorvida pela Nebius Token Factory em 17/07/2026) e do **GitHub Models** (descontinuado em 30/07/2026). Registro formal de transição de faturamento na **SambaNova Cloud** (exigência de método de pagamento / cartão no Developer Tier) e **Baseten** ($30 credits exigem cartão no cadastro). Calibração oficial das métricas de **Maritaca AI** (Tier 0 com 60 RPM, 128k input tokens/min, 10k output tokens/min, Batch API 4M chars/dia e tabela de preços em BRL com descontos de 50% Flex/Batch/Noturno e 75% Cache). Explicitação das cotas dinâmicas do **Google AI Studio** e cláusula de data logging no Free Tier. Estruturação do **Exa.ai** ($10/mês recorrente + $10 bônus), **Cartesia** (20.000 créditos/mês Sonic-3) vs. **Lemonfox.ai** (trial 1 mês + $5 budget), e **Voyage AI** (200M moderno / 50M legado). Recalibração de todos os níveis da Cadeia de Fallback. Backup de segurança mantido em `freetiers_apis.md.bak_v16`. |
| **v16** | **20/09/2026** | **🏆 Mapeamento Exaustivo, Validação em Runtime & Auditoria Estrita de 20 Novos Provedores de Inferência (4 Pilares Estratégicos — Total 64 Provedores)**: Consolidação completa e auditada de 20 novas plataformas com Free Tier permanente, créditos comprovados sem cartão e gateways de micro-orçamento de $5 USD: **Pilar 1 (Serverless LLMs)**: Fireworks AI, Clarifai, Baseten, Replicate, xAI Console / Grok API. **Pilar 2 (Voz, Áudio, STT & TTS)**: Deepgram, AssemblyAI, ElevenLabs, Cartesia, Lemonfox.ai. **Pilar 3 (Embeddings, Rerank & Busca Neural)**: Voyage AI, Jina AI, Tavily AI, Exa.ai, Qdrant Cloud. **Pilar 4 (Soberania Regional & Mercados Emergentes)**: StepFun, 01.AI, ModelScope, RunPod Serverless, CentML. Backup em `freetiers_apis.md.bak_v15`. |
| **v15** | **19/09/2026** | **💎 Expansão Global de Free Tiers Recorrentes, Soberania Regional & Expurgo de Falsos Free Tiers**: Incorporação de **Inception Labs** (100M tokens free, Mercury API); **Reka AI** ($10/mês em créditos recorrentes + 3h vídeo); **Bytez** ($1.00 de crédito renovado a cada 4 semanas); **Morph Labs** (250k créditos/mês); **Modal Labs** ($30/mês em computação serverless); e soberania regional (**InternLM**, **Sarvam AI**, **SEA-LION**, **LLM7.io**). Auditoria de segurança: **FriendliAI** desmentido, **Liquid AI** esclarecido e **CrofAI** banido. Backup em `freetiers_apis.md.bak_v14`. |
| **v14** | **18/09/2026** | **🇧🇷 Soberania Nacional Maritaca AI, Cloudflare Workers AI & Absorção OmniRoute**: Integração de Maritaca AI (MariTalk: Sabiá-4, Sabiá-4 Thinking, Sabiazinho-4). Cota de 10.000 Neurons/dia do Cloudflare Workers AI. SambaNova Cloud SN40L RDUs. Hugging Face Serverless Inference. Especialistas em embeddings Nomic AI e Mixedbread AI. Gateways anônimos AI Horde, DuckDuckGo AI e UncloseAI. Backup em `freetiers_apis.md.bak_v13`. |
| **v13** | **17/09/2026** | **🎯 Auditoria Integral, Expurgo de Inconsistências & Alinhamento Rigoroso de Modelos**: Restauração dos identificadores canônicos oficiais da DeepSeek (`deepseek-chat` para V3 e `deepseek-reasoner` para R1); tabela oficial de preços ($0.14 miss / $0.014 hit / $0.28 out no V3; $0.55 miss / $0.14 hit / $2.19 out no R1) e desconto de 50% Off-Peak. Auditoria do Google AI Studio com segregação entre GA e Preview. Validação do Groq Cloud (13 modelos ativos). NVIDIA NIM (82 modelos, 40 RPM / 1.000 RPD). OpenRouter 24 modelos free, Mistral La Plateforme e Moonshot AI / Kimi com ¥15 RMB. Backup em `freetiers_apis.md.bak_v12`. |
| **v12** | **17/09/2026** | **🇨🇳 Aprofundamento no Mercado Chinês & Guia de Planos Econômicos de $5 USD**: Mapeamento do ecossistema doméstico chinês (Zhipu AI BigModel GLM-4-Flash 100% free perpétuo; Baidu Qianfan ERNIE-Speed e Lite 100% free; Alibaba DashScope 1M-2M tokens; Tencent Hunyuan 1 ano free; ByteDance Volcano sem free tier; MiniMax, 01.AI e StepFun). Guia de Planos Budget de $5 (xKiro, OpenCode, DeepSeek direto, B.AI, SiliconFlow e WorkBuddy). |
| **v11** | 17/09/2026 | **🚀 Grande Expansão e Mapeamento Técnico de Novos Provedores de Inferência**: Inclusão de 8 provedores (Hyperbolic, SiliconFlow, Pollinations.ai, Cohere, AwanLLM, Scaleway, Novita, Nebius); auditoria de falsos free tiers (Chutes, Lepton, Together, AI/ML API). |
| **v10** | 17/09/2026 | **🔥 Auditoria em tempo real após 11 dias**: Groq desliga definitivamente `qwen/qwen3.6-27b` (404); OpenRouter Free pula para 24 modelos; NVIDIA NIM adiciona `z-ai/glm-5.3` e `nemotron-parse-2.0`; Google AI Studio adiciona `antigravity-preview-09-2026`. |
| **v9** | 06/09/2026 | Auditoria em tempo real completa: Inclusão do Gemini 3.8 Flash e Qwen 3.8 no Groq; Kimi validado na API `.ai`. |
| **v8** | 25/08/2026 | Aplicação das métricas granulares (RPM/RPD/TPM/TPD/ASH/ASD); expansão do Cloudflare e SambaNova. |
| **v7** | 25/08/2026 | Conciliação profunda com o Catálogo Manus AI v4.0 (17 novos provedores descobertos). |
| **v6** | 25/08/2026 | NVIDIA NIM remove GLM-5.2 e adiciona Llama 3.1 8B; DeepSeek lança V4 Flash Vision Experimental. ⚠️ *ID legado/obsoleto (v19)* |
| **v5** | 19/08/2026 | **🚨 Cerebras encerra Free Tier** (402 Payment Required); Groq desativa Llama 3.1/3.3; Gemini 3.7 Flash. ⚠️ *ID legado/obsoleto (v19)* |
| **v4** | 16/08/2026 | DeepSeek V4 Pro em GA com peak/off-peak pricing; Kimi K3 lançado; Gemini 2.5 Pro descontinuado. |
| **v3** | 23/07/2026 | Lançamento do Gemini 3.6 Flash; desativações no Groq (17/07); NVIDIA NIM atinge 119 modelos. |
| **v2** | 15/07/2026 | Lançamento do Gemini 3.5 Flash; colapso do catálogo Cerebras; Z.AI e MiniMax adicionados. |
| **v1** | 27/05/2026 | Criação do catálogo original (Llama 3.1, Moonshot V1, Cerebras 12 modelos). ⚠️ *ID legado/obsoleto (v19)* |

---

## APÊNDICE A — ARQUIVADOS / NÃO RECOMENDADOS (v19)

> Conteúdo movido do corpo do manual na v19 para não se perder nada (Regra de Ouro 6). **Nada deste apêndice foi reverificado em 07/10/2026** e nenhum item é recomendado para produção ou para dados pessoais. Títulos foram rebaixados um nível; o texto original foi mantido.


### A.1 Gateways anônimos, sem chave e modelos "uncensored" (ex-Seção 3 e ex-AwanLLM)

#### 🕵️ GATEWAYS ANÔNIMOS & SEM CHAVE (ZERO CADASTRO, ZERO CARTÃO)
Para testes de bancada, pipelines educacionais e protótipos onde você não deseja emitir credenciais:
1. **AI Horde (`https://aihorde.net/`)**: Rede voluntária distribuída de GPUs. Permite chamadas com a chave pública anônima `0000000000` para chat (`oai.aihorde.net/v1`) e geração de imagens Stable Diffusion sem conta.
2. **DuckDuckGo AI Chat (`https://duckduckgo.com/duckchat`)**: Interface web gratuita e anônima com Claude 3 Haiku, GPT-4o mini e Llama 3.3 sem retenção de logs.
3. **UncloseAI (`https://uncloseai.com/`)**: Endpoint compatível com OpenAI que aceita qualquer string como chave de API para testes rápidos.

#### 🟢 AWANLLM (api.awanllm.com) — *Validado em 17/09/2026 (Free Lite Tier Perpétuo — "Unlimited Tokens")* ⚠️ *(não verificado em 07/10/2026)*

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
| `Meta-Llama-3.1-8B-Instruct` | Llama 3.1 8B Instruct | Texto / Chat | 128.000 / 4.096 | **20** | **200** | Free Lite Perpétuo | Versão oficial do Meta Llama 3.1 com contexto expandido de 128K ⚠️ *ID legado/obsoleto (v19)* |
| `Awanllm-Llama-3-8B-Cumulus` | Llama 3 Cumulus 8B | Roleplay / Uncensored| 8.192 / 4.096 | **20** | **200** | Free Lite Perpétuo | Variante zero-refusal popular para escrita criativa e cenários de ficção |
| `Awanllm-Llama-3-8B-Dolfin` | Llama 3 Dolfin 8B | Instruction Following| 8.192 / 4.096 | **20** | **200** | Free Lite Perpétuo | Modelo com alinhamento flexível para tarefas de comando sem recusas |
| `Awanllm-Llama-3-8B-Instruct-ORPO-v0.1` | Llama 3 ORPO 8B | Alinhamento ORPO | 8.192 / 4.096 | **20** | **200** | Free Lite Perpétuo | Treinado com Odds Ratio Preference Optimization para respostas coesas |
| `Meta-Llama-3.1-70B-Instruct` | Llama 3.1 70B Instruct| Texto / Análise | 128.000 / 4.096 | **20** | **10** | Free Lite Perpétuo | Modelo pesado de 70B para tarefas analíticas esporádicas (10 reqs/dia) ⚠️ *ID legado/obsoleto (v19)* |



### A.2 Ecossistema chinês doméstico (ex-Seção 1) e StepFun / 01.AI / ModelScope (ex-Pilar 4)

#### 🇨🇳 ECOSSISTEMA CHINÊS: PROVEDORES NATIVOS & MODELOS DOMÉSTICOS

O mercado chinês de IA desenvolveu uma das infraestruturas de inferência mais competitivas do mundo. Diferencia-se por oferecer modelos leves permanentemente gratuitos (visando tração de desenvolvedores) e modelos de raciocínio de alta escala a custos ordens de magnitude inferiores aos modelos ocidentais.

---

##### 🔴 ZHIPU AI / BIGMODEL (open.bigmodel.cn) — *Validado em 17/09/2026 (Modelos 100% Free Perpétuo)* ⚠️ *(não verificado em 07/10/2026)*

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

##### 🔴 BAIDU QIANFAN (qianfan.cloud.baidu.com) — *Validado em 17/09/2026 (ERNIE Speed & Lite 100% Free Perpétuo)* ⚠️ *(não verificado em 07/10/2026)*

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

##### 🔴 ALIBABA CLOUD MODEL STUDIO / DASHSCOPE / BAILIAN (alibabacloud.com / bailian.console.aliyun.com) — *Validado em 17/09/2026* ⚠️ *(não verificado em 07/10/2026)*

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
| `qwen2.5-coder-32b-instruct` | Qwen 2.5 Coder 32B | Programação Pura | 131.072 / 8.192 | Franquia Model Studio | **¥1.50** (~$0.21 USD) | O modelo de código open-weight mais elogiado do mundo no ecossistema OpenCode ⚠️ *ID legado/obsoleto (v19)* |
| `qwen2.5-72b-instruct` | Qwen 2.5 72B | Raciocínio Geral | 131.072 / 8.192 | Franquia Model Studio | **¥4.00** (~$0.56 USD) | O peso pesado open-source líder em rankings internacionais ⚠️ *ID legado/obsoleto (v19)* |
| `qwen-vl-max` | Qwen VL Max | Visão Computacional | 32.768 / 8.192 | Franquia Onboarding | **¥20.00** (~$2.80 USD) | Extração de diagramas, vídeo frame-by-frame e OCR multi-orientação |

---

##### 🔴 TENCENT CLOUD HUNYUAN & TOKENHUB (cloud.tencent.com/product/hunyuan) — *Validado em 17/09/2026* ⚠️ *(não verificado em 07/10/2026)*

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

##### 🔴 BYTEDANCE VOLCANO ENGINE / DOUBAO (volcengine.com) — *Auditoria Operacional em 17/09/2026*

O **Doubao (豆包)**, desenvolvido pela ByteDance, é o modelo de IA mais utilizado na China em volume de requisições diárias (motor do TikTok / Douyin).

* **DIAGNÓSTICO CRÍTICO DE FREE TIER**: ❌ **A API profissional do Volcano Engine NÃO possui Free Tier perpétuo para desenvolvedores**.
  * Enquanto o **aplicativo móvel e web do Doubao é 100% gratuito** para usuários finais, o acesso à API para desenvolvimento via Volcano Engine é **estritamente bilhetado em RMB**.
  * Não há cota perpétua de chamadas sem saldo na conta.
* **Tarifação de Atacado (Pay-Per-Use Ultra-Barato)**:
  * Embora seja pago, é um dos mais baratos do mercado: `Doubao-pro-32k` custa aproximadamente **¥0.80 por milhão de tokens de entrada** (~$0.11 USD/M) e `Doubao-lite-32k` custa cerca de **¥0.30 por milhão** (~$0.04 USD/M).
  * Conclusão de Arquitetura: Para pipelines 100% gratuitos, utilize **SiliconFlow (Qwen/DeepSeek)**, **Baidu Qianfan (ERNIE Speed)** ou **Zhipu AI (GLM-4-Flash)** em vez da API direta do Volcano Engine.

---

##### 🔴 OUTROS PLAYERS CHINESES: MINIMAX, 01.AI & STEPFUN

| Provedor | Modelos Destacados | Bônus / Cota Free Inicial | Custo Pós-Free | Endpoint & Notas |
| :--- | :--- | :---: | :---: | :--- |
| **MiniMax**<br>`api.minimax.chat` | `abab6.5s-chat`, `MiniMax-Text-01`, `speech-01` (TTS), `video-01` (Hailuo AI) | **¥15 RMB de bônus** (~$2.10 USD) no cadastro | ~$0.15/M texto; TTS ~$0.002/1K chars | **Líder em Áudio e Vídeo**: O modelo `speech-01` possui a melhor síntese vocal emotiva da China; `video-01` lidera no Hailuo AI |
| **01.AI (Lingyi Wanwu)**<br>`api.lingyiwanwu.com` | `yi-lightning`, `yi-large`, `yi-medium`, `yi-vision` | **¥30 RMB de créditos** (~$4.20 USD) | ¥1.00 a ¥12.00 por M tokens | Criado por Kai-Fu Lee. `yi-lightning` oferece velocidade excepcional de geração com raciocínio profundo |
| **StepFun (Jieyue Xingchen)**<br>`platform.stepfun.ai` | `step-3.5-flash`, `step-3.7-flash`, `step-1-128k`, `stepaudio-3` | **Step Plan Trial** + Rota Free no OpenRouter | ~$0.10 a $0.80 / M tokens | Forte em compreensão multimodal de áudio (`stepaudio-3`) e modelos long-context rápidos |


###### 16. StepFun / Jieyue Xingchen (platform.stepfun.ai) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

###### 17. 01.AI / Lingyi Wanwu (platform.lingyiwanwu.com) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
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

###### 18. ModelScope / Alibaba DAMO Academy (modelscope.cn) — *Validado em 20/09/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://modelscope.cn/](https://modelscope.cn/)
* **Endpoint Base**: `https://api-inference.modelscope.cn/v1` (Compatível 1:1 com OpenAI SDK)
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: Cadastro gratuito com e-mail no portal ModelScope da Alibaba.
* **Tipo de Cota Perpétua**: **Inference API Serverless Comunitária 100% Gratuita e Permanente**.
* **Infraestrutura Soberana**: O ModelScope (hub aberto de IA da Alibaba DAMO Academy) disponibiliza inferência serverless gratuita para milhares de modelos abertos hospedados nos clusters de GPUs da Alibaba Cloud.
* **Limites de Taxa**: **30 RPM**, até **1.000 requisições gratuitas por dia (RPD)** por usuário.

| Modelo ID API (Canônico) | Display Name | Modalidade | Contexto (In / Out) | Limites de Taxa | Custo | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`Qwen/Qwen2.5-72B-Instruct`** | Qwen 2.5 72B ModelScope | Texto | 32.768 / 8.192 | 30 RPM / 1.000 RPD | **100% Free** | Execução serverless do melhor modelo aberto chinês sem cobrança ⚠️ *ID legado/obsoleto (v19)* |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`**| Qwen 2.5 Coder 32B | Programação | 32.768 / 8.192 | 30 RPM / 1.000 RPD | **100% Free** | Geração e refatoração de código sem gastar saldo ⚠️ *ID legado/obsoleto (v19)* |
| **`ZhipuAI/glm-4-9b-chat`** | GLM-4 9B ModelScope | Diálogo / Chat | 32.768 / 4.096 | 30 RPM / 1.000 RPD | **100% Free** | Modelo leve e responsivo para assistentes e bots |
| **`iic/SenseVoiceSmall`** | SenseVoice Small STT | Áudio / STT | Áudio em 5+ línguas | 30 RPM / 1.000 RPD | **100% Free** | Reconhecimento de fala ultra-rápido (latência < 100ms) e detecção de emoção |
| **`damo/cv_tinynas_object-detection`**| TinyNAS Vision | Visão Computacional| Imagem / Bounding boxes | 30 RPM / 1.000 RPD | **100% Free** | Detecção rápida de objetos em tempo real |



### A.3 Soberania regional & gateways (InternLM, Sarvam, SEA-LION, LLM7.io)

#### 🌏 JOIAS DE SOBERANIA REGIONAL & GATEWAYS ULTRARRÁPIDOS

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


### A.4 Trials não comerciais (Cohere, Cartesia)

#### 🟢 COHERE (api.cohere.com) — *Validado em 17/09/2026 (Developer Trial Tier Perpétuo)* ⚠️ *(não verificado em 07/10/2026)*

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


###### 9. Cartesia (cartesia.ai) — *Validado em 29/09/2026* ⚠️ *(não verificado em 07/10/2026)*
* **Console / Cadastro**: [https://play.cartesia.ai/](https://play.cartesia.ai/)
* **Endpoint Base**: `https://api.cartesia.ai/tts/bytes` ou WebSocket `wss://api.cartesia.ai/tts/websocket`
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito**.
* **Verificação**: E-mail / Google / GitHub.
* **Tipo de Cota Free**: **Free Tier Permanente** concedendo **20.000 créditos / mês gratuitos** renovados a cada ciclo (equivalente a ~20.000 caracteres de TTS no modelo Sonic-3) para uso pessoal e prototipagem (não-comercial).
* **Arquitetura Base**: Baseado na arquitetura **State Space Model (SSM)**, o motor Sonic atinge **latência inferior a 150ms** e suporte a áudio estéreo em 44.1kHz, tornando-o o motor mais rápido para síntese conversacional em tempo real.
* **Limites de Taxa**: **30 RPM**, **1 stream concorrente** no plano gratuito.

| Modelo ID API (Canônico) | Display Name | Modalidade | Taxa de Amostragem | Limites de Taxa | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`sonic-english`** | Sonic English Ultra-Fast | TTS em Inglês | 44.1kHz / 24kHz / 16kHz | 30 RPM / 1 stream | Latência sub-150ms imperceptível para humanos em conversação telefônica |
| **`sonic-multilingual`** | Sonic Multilingual | TTS Multilíngue | 44.1kHz Hi-Fi | 30 RPM / 1 stream | Suporte a Francês, Alemão, Espanhol, Japonês e Português |
| **`sonic-fast`** | Sonic Fast Realtime | TTS Baixa Latência | 24kHz Otimizado | 30 RPM / 1 stream | Ajustado para menor consumo de largura de banda e streaming instantâneo |


### A.5 Cadeia de Fallback v18 (ARQUIVADA — enquadramento "produção sem custo de API" revogado na v19)

### 4. CADEIA DE FALLBACK RECOMENDADA (ARQUITETURA RESILIENTE MULTI-NÍVEL)

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

[NÍVEL 2 — High Throughput, Modelos Abertos & Inferência Serverless Veloz (v17)]
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
   │       Cota: 1.000 RPM / 40.000 TPM (Modelos free com KYC / 100 RPD sem KYC + 20M tokens)
   │
   ├─► 9. OpenRouter Free Tier (nex-agi/nex-n2.5-pro / inclusionai/ling-3.0-flash-vl)
   │       Cota: 20 RPM / 50-200 RPD por modelo (24 modelos ativos com Visão e 262K ctx)
   │
   ├─► 10. Maritaca AI — MariTalk (sabia-4 / sabia-4-thinking / sabiazinho-4) 🇧🇷
   │       Cota: 60 RPM / 128.000 input TPM / 10.000 output TPM (A campeã em português, sem cartão)
   │
   ├─► 11. Baseten Serverless Bridge (Llama-3.3-70B / DeepSeek-V3 / Qwen-Coder) 🆕
   │       Cota: $30 USD em créditos para deploy serverless Truss/vLLM (requer cartão no cadastro)
   │
   ├─► 12. Bytez (llama-3.3-70b / qwen-2.5-72b) 💎
   │       Cota: $1.00 USD renovado a cada 4 semanas sem cartão
   │
   ├─► 13. xAI Console / Grok API (grok-2-1212 / grok-2-vision) 🆕
   │       Cota: $25 USD/mês em developer grants para Grok sem cartão
   │
   └─► 14. Pollinations.ai (openai / deepseek / qwen-coder / flux)
           Cota: 60 RPM texto / 30 RPM imagem (100% free perpétuo, sem login)

[NÍVEL 3 — Especialistas em Voz, Áudio, STT & TTS (Pilar 2 v17)] 🎙️
   │
   ├─► 15. Deepgram (nova-2 / nova-2-general / aura-asteria-en) 🆕
   │       Cota: $200 USD em créditos perpétuos sem cartão (~775 horas de STT e Aura TTS)
   │
   ├─► 16. AssemblyAI (best / nano / lemur-70b-chat) 🆕
   │       Cota: $50 USD em créditos sem cartão (~100-330 horas de transcrição Conformer-2)
   │
   ├─► 17. ElevenLabs (eleven_multilingual_v2 / eleven_flash_v2_5) 🆕
   │       Cota: 10.000 caracteres/mês perpétuos sem cartão (Qualidade Hi-Fi vocal)
   │
   ├─► 18. Cartesia (sonic-english / sonic-multilingual / sonic-fast) 🆕
   │       Cota: 20.000 créditos/mês permanentes (Sonic-3 TTS, latência sub-150ms sem cartão)
   │
   └─► 19. Lemonfox.ai (whisper-1 / lemonfox-tts-v1) 🆕
           Cota: Trial de 1 mês (10M créditos) + planos budget a partir de $5/mês (OpenAI drop-in)

[NÍVEL 4 — Especialistas em Embeddings, Rerank & Busca Neural para Agentes (Pilar 3 v17)] 🔍
   │
   ├─► 20. Voyage AI (voyage-3 / voyage-4 / voyage-code-3 / rerank-2) 🆕
   │       Cota: 200M tokens trial (linha moderna) / 50M tokens (linha legada) sem cartão
   │
   ├─► 21. Jina AI (jina-embeddings-v3 / jina-reranker-v2 / r.jina.ai) 🆕
   │       Cota: 10M tokens free + Reader API 100% perpétua e gratuita (500 RPM com chave free)
   │
   ├─► 22. Tavily AI (tavily search / extract) 🆕
   │       Cota: 1.000 buscas/mês perpétuas sem cartão para agentes autônomos
   │
   ├─► 23. Exa.ai (neural search / text highlights) 🆕
   │       Cota: $10 USD/mês recorrente (~1.400 buscas/mês) + $10 bônus inicial sem cartão
   │
   ├─► 24. Qdrant Cloud (1GB RAM / 0.5 vCPU Free Forever Cluster) 🆕
   │       Cota: Cluster vetorial permanente na nuvem para até 1M de vetores sem cartão
   │
   ├─► 25. Nomic AI & Mixedbread AI (nomic-embed-text-v1.5 / mxbai-rerank-large-v1)
   │       Cota: Milhares de embeddings e reranks gratuitos sem cartão
   │
   └─► 26. Morph Labs Fast Apply (morph-fast-apply) 💎
           Cota: 250.000 créditos/mês ($0) para diff instantâneo em agentes de código

[NÍVEL 5 — Soberania Regional, Mercados Emergentes & Nuvem Serverless (Pilar 4 v17)] 🌏
   │
   ├─► 27. StepFun / Jieyue Xingchen (step-1-128k / step-1-256k / step-2-16k) 🆕
   │       Cota: ¥50 RMB (~$7 USD) em créditos sem cartão (Contexto de até 256k tokens)
   │
   ├─► 28. 01.AI / Lingyi Wanwu (yi-lightning / yi-large / yi-medium-200k) 🆕
   │       Cota: ¥36 RMB em créditos sem cartão (Yi-Lightning a 100+ tokens/segundo)
   │
   ├─► 29. ModelScope / Alibaba DAMO (Qwen2.5-72B / Coder-32B / SenseVoice) 🆕
   │       Cota: 30 RPM / 1.000 RPD 100% gratuitos perpétuos em cluster DAMO
   │
   ├─► 30. InternLM / Shanghai AI Lab (internlm2.5-20b-chat / xcomposer2.5) 💎
   │       Cota: 1.000.000 in / 3.000.000 out tokens/mês gratuitos sem cartão
   │
   ├─► 31. Sarvam AI (sarvam-2b / sarvam-translate) 🇮🇳
   │       Cota: ₹1.000 INR em créditos para 10 línguas da Índia sem cartão
   │
   ├─► 32. SEA-LION / AI Singapore (sea-lion-v3-7b-instruct) 🇸🇬
   │       Cota: 10 RPM / 100.000 TPM para línguas do Sudeste Asiático sem cartão
   │
   ├─► 33. Baidu Qianfan (ERNIE-Speed-8K / ERNIE-Speed-128K / ERNIE-Lite)
   │       Cota: 300 RPM / 300.000 TPM (100% permanente e gratuito sem bilhetagem)
   │
   ├─► 34. Zhipu AI / BigModel (GLM-4-Flash / GLM-4.7-Flash / GLM-4V-Flash)
   │       Cota: 100% Free Perpétuo (1 concorrência contínua, sem cartão) + 25M tokens bônus
   │
   ├─► 35. Alibaba Model Studio / DashScope (Qwen-Turbo / Qwen-Plus / Qwen-Long)
   │       Cota: 1M a 2M tokens free por modelo (90-180 dias) + frações de centavo pós-free
   │
   └─► 36. Tencent Hunyuan & TokenHub (Hunyuan-Lite / Hunyuan-3D)
           Cota: Pacote gratuito de 1 ano para Hunyuan-Lite + 1.000 créditos para 3D

[NÍVEL 6 — Gateways Budget, Micro-Orçamentos ($5) & Serverless por Segundo] 💵
   │
   ├─► 37. DeepSeek API Direta (deepseek-chat [V3] / deepseek-reasoner [R1])
   │       Cota: 5M tokens grátis; Preços Oficiais: $0.14/$0.28 (V3) e $0.55/$2.19 (R1); $5 rende 18M a 35M+ tokens
   │
   ├─► 38. RunPod Serverless (vLLM Llama-3.3-70B / DeepSeek-R1-Distill-32B) 🆕
   │       Cota: Gateway de micro-orçamento ($5 USD) com cobrança por segundo ($0.0002/seg) e scale-to-zero
   │
   ├─► 39. CentML / CServe (Llama-3.3-70B / Mistral-Small) 🆕
   │       Cota: Free developer trial com compilação de kernel acelerada até 3x mais veloz
   │
   ├─► 40. xKiro ($5 Wallet + 5M tokens/dia Free) — 40+ modelos sem filas nem fricção
   ├─► 41. OpenCode Zen / Go ($0 Free Models ou $10/mês para até $60 em tokens de coding)
   ├─► 42. B.AI (1 USD = 1M créditos, com até 90% de desconto em execuções off-peak)
   ├─► 43. Modal Labs ($30/mês em contêineres e GPUs serverless para vLLM; requer cartão)
   ├─► 44. Cloudflare Workers AI (10.000 Neurons/dia gratuitos perpétuos sem cartão)
   ├─► 45. SambaNova Cloud (Llama-3.3-70B / DeepSeek-R1 — requer método de pagamento / cartão no Developer Tier)
   └─► 46. Replicate Developer Sandbox (Predições de teste em LLMs, FLUX e difusão) 🆕

[ROTA ANÔNIMA & SEM CHAVE: ZERO CADASTRO, ZERO RETENÇÃO] 🕵️
   │
   ├─► 47. LLM7.io (api.llm7.io/v1) — 2 req/s, 20 RPM, 100 req/hr livres sem login 💎
   ├─► 48. AI Horde (oai.aihorde.net/v1) — Chave pública `0000000000` em cluster comunitário
   ├─► 49. UncloseAI (uncloseai.com) — Endpoint mock/proxy para testes de integração
   └─► 50. DuckDuckGo AI (duckduckgo.com/duckchat) — Interface anônima com Claude/GPT-4o mini

[PLATAFORMAS AUDITADAS: REMOVIDAS, FALSOS FREE TIERS OU DESCONTINUADAS]
   ❌ Clarifai: Encerrado oficialmente em 17/07/2026 após aquisição pela Nebius (tecnologia absorvida no Nebius Token Factory). 🚨
   ❌ GitHub Models (models.inference.ai.azure.com): Encerrado e aposentado pela Microsoft/GitHub em 30/07/2026. 🚨
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


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# FIM DO MANUAL CANÔNICO — FREE TIERS 2026 (v19 — 07/10/2026)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
