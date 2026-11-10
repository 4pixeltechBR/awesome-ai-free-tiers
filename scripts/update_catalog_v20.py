import re

file_path = r"E:\Arquivos desenvolvimento\freetiers_apis.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Header Lines
header_old = """# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MANUAL DE CONSULTA: FREE TIERS DE LLM & POLÍTICAS DE USO (Outubro 2026)
# Compilação e Revisão de Fatos: 07 de outubro de 2026 (v19)
# Histórico: 27/05 → 15/07 → 23/07 → 16/08 → 19/08 → 25/08 (v8) → 06/09 (v9) → 17/09 (v10) → 17/09 (v11) → 17/09 (v12) → 17/09 (v13) → 18/09 (v14) → 19/09 (v15) → 20/09 (v16) → 29/09 (v17) → 05/10 (v18) → 07/10/2026 (v19 atual)
# Fontes: Páginas oficiais consultadas em 07/10/2026 (preços, termos, rate limits, políticas de privacidade) + catálogo herdado da v18 (itens não reverificados marcados como "não verificado em 07/10/2026")
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

header_new = """# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MANUAL DE CONSULTA: FREE TIERS DE LLM & POLÍTICAS DE USO (Novembro 2026)
# Compilação e Validação Fina: 10 de novembro de 2026 (v20)
# Histórico: 27/05 → 15/07 → 23/07 → 16/08 → 19/08 → 25/08 (v8) → 06/09 (v9) → 17/09 (v10) → 17/09 (v11) → 17/09 (v12) → 17/09 (v13) → 18/09 (v14) → 19/09 (v15) → 20/09 (v16) → 29/09 (v17) → 05/10 (v18) → 07/10 (v19) → 10/11/2026 (v20 atual)
# Fontes: Páginas oficiais consultadas em 10/11/2026 (preços, termos, rate limits, APIs multimodais e políticas) + catálogo herdado da v19
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

if header_old in content:
    content = content.replace(header_old, header_new, 1)
else:
    print("WARNING: header_old not matched directly, adjusting...")

# 2. Add v20 release note block right above v19
v19_marker = "> **🧭 ATUALIZAÇÃO 07/10/2026 v19 (REVISÃO DE FATOS CONTRA FONTES OFICIAIS, TERMOS & LGPD, ESTRATÉGIA SEGMENTADA)**:"
v20_block = """> **🚀 ATUALIZAÇÃO 10/11/2026 v20 (EXPANSÃO MULTIMODAL DE VOZ/ÁUDIO & VÍDEO, FISH AUDIO, META-ROTEADOR OPENROUTER, TTS GROQ & SILICONFLOW GTM)**:
> 1. **Fish Audio (`fish.audio`) Adicionado no Pilar 2**: Inclusão de provedor de voz/TTS de altíssima fidelidade e clonagem com cota permanente gratuita na API via modelo neural **`s2.1-pro-free`** ($0.00 / 1M UTF-8 bytes na API, 5 concorrências, sem necessidade de cartão de crédito) + 8.000 créditos mensais na interface web.
> 2. **Groq Cloud (Síntese Vocal / TTS Canopy Labs)**: Adicionados os modelos ultrarrápidos de TTS **`canopy-labs/orpheus-v1-en`** e **`canopy-labs/orpheus-arabic-saudi`** integrados à infraestrutura LPU ao lado de `whisper-large-v3` e `whisper-large-v3-turbo`.
> 3. **OpenRouter (`openrouter/free` & Limites Confirmados)**: Mapeamento oficial do meta-roteador **`openrouter/free`** para roteamento dinâmico automático com suporte a ferramentas, saídas estruturadas e visão. Limites confirmados: 20 RPM, 50 RPD no tier gratuito padrão e 1.000 RPD para contas com recarga acumulada de $10 USD vitalícia.
> 4. **SiliconFlow (Consolidação de Domínio GTM & FLUX.2)**: Domínio oficial consolidado em **`https://api.siliconflow.cn/v1`** com aceleração global; modelos Qwen3/Qwen2.5 e DeepSeek mantidos em Free Tier permanente; modelos FLUX.2 em inferência serverless por imagem.
> 5. **Auditoria de Mídia Criativa (Vídeo & Imagem - Kling AI, Recraft, Fal.ai)**:
>    * **Kling AI**: 66 créditos diários gratuitos renovados a cada 24h no web app (vídeos 720p 5s). API direta sem free tier permanente (trial packs a partir de $9 USD).
>    * **Recraft AI**: Studio web gratuito com 50 créditos/dia; API estritamente pré-paga ($1 USD = 1.000 unidades de API).
>    * **fal.ai**: Sem cota contínua gratuita de API; cobrança pré-paga por megapixel ($0.003 em FLUX.1-schnell, $0.025 em FLUX.1-dev) e vídeo ($0.20 a $0.40/s).
> 6. **Rastreamento Ativo de Promoções (Q4 2026)**:
>    * DeepSeek Off-Peak (-50%): das 22h-01h e 03h-07h BRT em dias úteis e 100% nos fins de semana.
>    * Maritaca AI: -30% em horário noturno (22h-06h) e -50% na Batch API.
>    * Voyage AI: 200M tokens trial no cadastro.
>    * Nenhuma concessão temporária com data de término expirou sem registro.
>
""" + v19_marker

if v19_marker in content:
    content = content.replace(v19_marker, v20_block, 1)

# 3. Add Fish Audio to Pilar 2 (Voice & Audio)
pilar2_target = "##### 10. Lemonfox.ai (lemonfox.ai) — *Validado em 29/09/2026* ⚠️ *(não verificado em 07/10/2026)*"
fish_audio_block = """##### 11. Fish Audio (fish.audio) — *Validado em 10/11/2026 (Free Developer API Perpétua)* 🆕
* **Console / Cadastro**: [https://fish.audio/](https://fish.audio/) / [https://fish.audio/go-api/](https://fish.audio/go-api/)
* **Endpoint Base**: `https://api.fish.audio/v1`
* **Requisitos de Entrada / Cartão**: ❌ **NÃO exige cartão de crédito** no cadastro.
* **Verificação**: E-mail / Google / GitHub.
* **Tipo de Cota Free**: **Modelo Neural Free Permanente na API (`s2.1-pro-free`)** com bilhetagem a **$0.00 / 1 Milhão de UTF-8 bytes**, permitindo prototipagem e desenvolvimento de assistentes de voz sem nenhum custo de consumo de tokens. Na interface web, oferece **8.000 créditos mensais** (~7 min de áudio) renovados mensalmente.
* **Limites de Taxa Granulares**: **5 requisições concorrentes** (Starter/Free Tier compartilhado entre as chaves da conta), com backoff exponencial do cliente em caso de pico (HTTP 429).
* **Recursos Avançados**: Clonagem de voz zero-shot (com apenas 10 a 30 segundos de áudio de referência), suporte a mais de 10 idiomas (incluindo Português do Brasil com entonação expressiva), controle de pitch/velocidade e latência ultra-reduzida.

| Modelo ID API (Canônico) | Display Name | Modalidade | Latência / Qualidade | Limite Free | Requisitos | Destaques Técnicos |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`s2.1-pro-free`** 🆕 | Fish Speech 2.1 Pro Free | TTS / Clonagem | Alta fidelidade | $0.00 / 1M bytes (5 conc) | ❌ Sem Cartão | Modelo neural oficial gratuito para API; clonagem rápida e TTS conversacional |
| **`s2.1-pro`** | Fish Speech 2.1 Pro | TTS / Voz Premium | Hi-Fi Studio | Pago ($1.50 / 1M bytes) | Saldo pré-pago | Modo de estúdio com prioridade de fila e SLA corporativo |

"""

if pilar2_target in content:
    # insert fish audio right before lemonfox or right after lemonfox table
    content = content.replace(pilar2_target, fish_audio_block + "\n" + pilar2_target, 1)

# 4. Add Groq TTS models
groq_target = "| `qwen/qwen3.8-27b` | text/vision | 131.042 | **30** | **1.000** | **8K** | **200K** | 600+ | ✅ 200 OK | **Único Qwen ativo no Groq** — Substitui 3.6 |"
groq_tts_rows = """| `canopy-labs/orpheus-v1-en` 🆕 | text-to-speech | — | **30** | **1.000** | — | — | Ultra-rápido | ✅ 200 OK | **Síntese de Voz (TTS)** — Modelo de voz Canopy Labs em inglês |
| `canopy-labs/orpheus-arabic-saudi` 🆕 | text-to-speech | — | **30** | **1.000** | — | — | Ultra-rápido | ✅ 200 OK | **Síntese de Voz (TTS)** — Modelo de voz Canopy Labs em árabe |
""" + groq_target

if groq_target in content:
    content = content.replace(groq_target, groq_tts_rows, 1)

# 5. Add OpenRouter openrouter/free
openrouter_target = "| `nex-agi/nex-n2.5-pro:free` 🆕 | Nex N2.5 Pro | 262.144 / 235.929 | ✅ 200 OK | **NOVO (17/09)** — Raciocínio e código de alto nível |"
openrouter_block = """| `openrouter/free` 🆕 | OpenRouter Free Meta-Router | Dinâmico | ✅ 200 OK | **NOVO (v20)** — Roteador inteligente dinâmico para modelos gratuitos com tool-calling e visão |
""" + openrouter_target

if openrouter_target in content:
    content = content.replace(openrouter_target, openrouter_block, 1)

# 6. Add Multimodal Creative Audit section in Section 3
sec3_marker = "## 4. ESTRATÉGIA RECOMENDADA POR CARGA DE TRABALHO"
creative_audit_block = """### 🎨 AUDITORIA DE FERRAMENTAS MULTIMODAIS CRIATIVAS (IMAGEM, VÍDEO & DESIGN) — *Validado em 10/11/2026* 🆕

Mapeamento de plataformas de geração de imagem, vídeo e design para separar claramente o que é cota gratuita de usuário (web) versus exigência de faturamento na API:

#### 1. Kling AI (kling.ai) — Geração de Vídeo AI
* **Web App (Gratuito Diário)**: Fornece **66 créditos gratuitos renovados a cada 24 horas** no login diário ("use ou perca"). Permite gerar até 2 a 3 vídeos curtos (5 segundos em 720p com marca d'água) por dia sem cartão de crédito.
* **API Direta**: ❌ **Não possui Free Tier permanente na API**. Acesso para desenvolvedores exige a contratação de pacotes de créditos ou planos a partir de ~$9 USD/mês. Custo médio de mercado em gateways é de ~$0.30 a $0.42 por clipe de 5 segundos.

#### 2. Recraft AI (recraft.ai) — Design Vetorial & Raster
* **Web App (Gratuito Diário)**: O *Recraft Studio* oferece plano Free ($0) com **50 créditos diários** para uso pessoal e prototipagem com geração de vetores SVG, ícones e ilustrações 3D.
* **API Direta**: ❌ **Não possui Free Tier contínuo na API**. A Recraft API opera estritamente no modelo pré-pago por "API Units" (**$1.00 USD = 1.000 units**), onde unidades compradas não expiram. Ideal para pipelines de produção gráfica automatizada sob micro-orçamento.

#### 3. fal.ai (fal.ai) — Nuvem de Inferência de Difusão & Vídeo
* **Web Sandbox**: Testes pontuais gratuitos na interface sandbox do navegador para modelos abertos.
* **API Direta**: ❌ **Não possui Free Tier contínuo de API**. A plataforma opera sob créditos pré-pagos (validade de 365 dias), com faturamento cirúrgico apenas por saídas bem-sucedidas (*Fair Billing*):
  * **FLUX.1 [schnell]**: ~$0.003 por megapixel.
  * **FLUX.1 [dev]**: ~$0.025 por megapixel.
  * **Vídeo Generativo (Kling/Veo/Hunyuan)**: ~$0.20 a $0.40 por segundo de vídeo gerado.
  * **Concorrência**: Inicia em 2 conexões simultâneas no onboarding e escala dinamicamente com o consumo.

---

""" + sec3_marker

if sec3_marker in content:
    content = content.replace(sec3_marker, creative_audit_block, 1)

# 7. Update Footer
footer_old = "# FIM DO MANUAL CANÔNICO — FREE TIERS 2026 (v19 — 07/10/2026)"
footer_new = "# FIM DO MANUAL CANÔNICO — FREE TIERS 2026 (v20 — 10/11/2026)"
if footer_old in content:
    content = content.replace(footer_old, footer_new, 1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("freetiers_apis.md successfully updated to v20 (10/11/2026)!")
