# ☁️ Cloudflare Workers AI — 10,000 Neurons/Day Free Tier

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Cloudflare Workers AI Setup Guide

* **Official Portal:** [https://dash.cloudflare.com/](https://dash.cloudflare.com/)
* **Credit Card Required for Free Tier?** ❌ **NO** (Included in free Cloudflare accounts)
* **Free Quota:** **10,000 Neurons per day** (resets every day at 00:00 UTC).
  * Equivalent to ~100,000 to 500,000 free tokens/day depending on model parameter size.
* **Top Supported Free Models:**
  * `@cf/meta/llama-3.3-70b-instruct`
  * `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`
  * `@cf/qwen/qwen2.5-coder-32b-instruct`
  * `@cf/baai/bge-large-en-v1.5` (Text Embeddings)
  * `@cf/black-forest-labs/flux-1-schnell` (Image Generation)

### Step-by-Step:
1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Go to **AI ➔ Workers AI**.
3. Create an API token under **Manage API Tokens** with `Workers AI: Read` permissions.
4. Note your **Account ID** found on the right sidebar of the dashboard.

### 1-Line Test Command (Terminal / cURL):
```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/YOUR_ACCOUNT_ID/ai/run/@cf/meta/llama-3.3-70b-instruct" \
  -H "Authorization: Bearer YOUR_CF_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain what a CDN is in 10 words."}'
```

---

<a name="português"></a>
## 🇧🇷 Guia Cloudflare Workers AI (10.000 Neurons/Dia Grátis)

* **Link Oficial do Console:** [https://dash.cloudflare.com/](https://dash.cloudflare.com/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Cota Gratuita:** **10.000 Neurons por dia**, renovados diariamente às 00:00 UTC (equivale a 100k a 500k tokens gratuitos por dia).
* **Modelos Disponíveis:** Llama 3.3 70B, DeepSeek-R1 Distill Qwen 32B, Qwen 2.5 Coder 32B, BGE Embeddings e geração de imagem com Flux-1 Schnell.
