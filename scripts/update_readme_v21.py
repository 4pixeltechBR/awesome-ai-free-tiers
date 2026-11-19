import re

readme_path = r"E:\Arquivos desenvolvimento\awesome-ai-free-tiers\README.md"

with open(readme_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Badges & Header
text = text.replace(
    "[![Verified Providers-66-brightgreen.svg]](#)",
    "[![Verified Providers-74-brightgreen.svg]](#)"
)
text = text.replace(
    "[![Audit Version](https://img.shields.io/badge/Audit%20Version-v20%20(10%2F11%2F2026)-blue.svg)](#)",
    "[![Audit Version](https://img.shields.io/badge/Audit%20Version-v21%20(19%2F11%2F2026)-blue.svg)](#)"
)
text = text.replace(
    "docs/freetiers_apis_v20_reference.md",
    "docs/freetiers_apis_v21_reference.md"
)

# 2. English Important Box
old_important_box = """> [!IMPORTANT]
> **🚨 November 2026 Live Audit & Multimodal Media Expansion (v20 Update / 10-11-2026):**
> * **Fish Audio (`fish.audio`) Added:** Permanent Free Developer API for neural Text-to-Speech and voice cloning via model `s2.1-pro-free` at **$0.00 / 1M UTF-8 bytes** (5 concurrent connections, zero credit card required) + 8,000 monthly credits on web app.
> * **Groq Cloud Voice Synthesis Added:** Ultra-fast real-time TTS models `canopy-labs/orpheus-v1-en` and `canopy-labs/orpheus-arabic-saudi` deployed on LPU infrastructure alongside Whisper Large v3 / Turbo.
> * **OpenRouter `openrouter/free` Dynamic Router:** Mapped the official `openrouter/free` meta-router with dynamic fallback based on tool calling and vision capabilities. Rate limits: 20 RPM, 50 RPD standard free tier, scaling to 1,000 RPD upon lifetime $10 USD top-up.
> * **SiliconFlow Domain Migration to GTM:** Official API endpoint unified at `https://api.siliconflow.cn/v1` with global acceleration. Permanent free tiers for Qwen/DeepSeek maintained; FLUX.2 serverless pay-per-image enabled.
> * **Creative Multimodal Media Audit (Video & Image):** Detailed verification of Kling AI (66 daily web credits for 720p 5s video; API strictly prepaid), Recraft AI (50 daily web credits; API prepaid at $1/1,000 units), and fal.ai (prepaid per megapixel and video second).
> * **Q4 2026 Promo Tracking:** Confirmed DeepSeek Off-Peak (-50% nights & weekends), Maritaca Night (-30%) and Batch (-50%), and Voyage AI (200M tokens trial).
> * **Preserved Legal & LGPD Governance:** Retained strict guidelines from v19 (Google AI Studio under-18 restriction, NVIDIA NIM trial-only status, Maritaca `-br-sp` LGPD compliance, and workload-segmented routing)."""

new_important_box = """> [!IMPORTANT]
> **🚨 November 2026 Live Audit & Sovereign Keyless Expansion (v21 Update / 19-11-2026):**
> * **OVHcloud AI Endpoints Added (Sovereign GDPR Tier-0):** Keyless anonymous tier (2 RPM/IP) or ~400 RPM with free key, hosted 100% in France with zero user prompt training and GDPR compliance. 21 models active: `gpt-oss-120b`, `Qwen3.5-397B-A17B`, `Mistral-Small-3.2-24B`, `whisper-large-v3-turbo`, and `bge-m3`.
> * **Kilo Code Gateway Added:** Keyless developer gateway with header `Authorization: Bearer anonymous`, ~200 requests/hour per IP for coding agents and open workloads.
> * **Aion Labs Added:** 15 RPM / 20k TPD without credit card for creative writing, narrative fiction and roleplay.
> * **Gemma 4 Generation & Gemini 3.6 Flash:** Mapped live `google/gemma-4-31b-it:free` and `google/gemma-4-26b-a4b-it:free` on OpenRouter alongside Gemini 3.6 Flash.
> * **6 Production Routing Quirks:** Mapped critical edge-cases in multi-provider routers (OpenCode session header, GitHub Models fake 200 trap, Pollinations in-band 402, Groq 413 parser, Moonshot partial prefill, open-weight inline tool-call rescue).
> * **New Welcome Trials & Status Updates:** Documented Nscale ($5), Upstage Solar ($10), AI21 Studio ($10), Inference.net ($5) and NLP Cloud ($15). Clarified Ollama Cloud commercial transition ($0.05/M tokens; free tier remains local). Confirmed shutdown of `glhf.chat` (now `synthetic.new`, paid only).
>
""" + old_important_box

assert old_important_box in text, "old_important_box not found!"
text = text.replace(old_important_box, new_important_box, 1)

# 3. Update Quick Navigation Matrix in English
old_nav_tier0 = "| **🟢 Tier 0: 100% Free Forever** | Permanent daily quotas, zero billing account needed | ❌ **No CC** | [Google AI Studio](docs/how-to-get-api-keys/google-ai-studio.md), [Groq](docs/how-to-get-api-keys/groq-cloud.md)"
new_nav_tier0 = "| **🟢 Tier 0: 100% Free Forever** | Permanent daily quotas, zero billing account needed | ❌ **No CC** | [OVHcloud AI Endpoints](docs/freetiers_apis_v21_reference.md), [Google AI Studio](docs/how-to-get-api-keys/google-ai-studio.md), [Groq](docs/how-to-get-api-keys/groq-cloud.md)"
text = text.replace(old_nav_tier0, new_nav_tier0, 1)

old_nav_tier3 = "| **🕵️ Tier 3: Anonymous & Keyless** | Zero sign-up, zero API key, zero logging | ❌ **No Account** | [LLM7.io (2 req/s)](docs/how-to-get-api-keys/regional-sovereign-gems.md)"
new_nav_tier3 = "| **🕵️ Tier 3: Anonymous & Keyless** | Zero sign-up, zero API key, zero logging | ❌ **No Account** | [OVHcloud AI (Keyless)](docs/freetiers_apis_v21_reference.md), [Kilo Code Gateway](docs/freetiers_apis_v21_reference.md), [LLM7.io (2 req/s)](docs/how-to-get-api-keys/regional-sovereign-gems.md)"
text = text.replace(old_nav_tier3, new_nav_tier3, 1)

# 4. In Portuguese section, update reference link and badges
pt_target = "### 🛡️ Nossas 5 Diretrizes Mandatórias de Governança"
pt_v21_box = """> [!IMPORTANT]
> **🚨 Auditoria ao Vivo v21 (19/11/2026) — Soberania Europeia Sem Chave, Kilo Code, Aion Labs, Gemma 4 & Quirks de Produção:**
> * **OVHcloud AI Endpoints Adicionado (Tier-0 Soberano GDPR):** Endpoint direto compatível com OpenAI sem chave (2 RPM/IP) ou com chave gratuita (~400 RPM), hospedado 100% na França sem retenção para treino. 21 modelos ativos incluindo `gpt-oss-120b`, `Qwen3.5-397B-A17B`, `Mistral-Small-3.2-24B`, `whisper-large-v3-turbo` e `bge-m3`.
> * **Kilo Code Gateway Adicionado:** Hub anônimo via `Authorization: Bearer anonymous` (~200 req/hora por IP) com 21 modelos para coding.
> * **Aion Labs Adicionado:** 15 RPM / 20k TPD sem cartão para escrita criativa, RPG e narrativa.
> * **Gemma 4 & Gemini 3.6 Flash:** Inclusão dos modelos `gemma-4-31b-it:free` e `gemma-4-26b-a4b-it:free` no OpenRouter.
> * **6 Quirks de Roteamento em Produção:** Documentação das salvaguardas para `cascade.py` (OpenCode session header, GitHub Models fake 200, Pollinations in-band, Groq 413, Moonshot prefill e rescue regex de tool calling).
> * **Atualizações de Billing & Status:** Ollama Cloud agora é pay-as-you-go ($0.05/M; free tier apenas localmente). Novos trials adicionados: Nscale ($5), Upstage Solar ($10), AI21 Studio ($10), Inference.net ($5) e NLP Cloud ($15). `glhf.chat` encerrado.
>
"""
text = text.replace(pt_target, pt_v21_box + pt_target, 1)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"README.md successfully updated! New length: {len(text)} characters.")
