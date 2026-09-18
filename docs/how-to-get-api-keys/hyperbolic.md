# ⚡ Hyperbolic — Decentralized AI Inference Free Tier

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Hyperbolic Setup Guide

* **Official Portal:** [https://app.hyperbolic.xyz/](https://app.hyperbolic.xyz/)
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ❌ **NO** (Email / GitHub)
* **Free Quota Highlights:**
  * Free inference tier with rate limits up to **60 RPM**.
  * Supported open-weight models: `meta-llama/Llama-3.3-70B-Instruct`, `deepseek-ai/DeepSeek-V3`, `Qwen/Qwen2.5-72B-Instruct`.

### Step-by-Step Instructions:
1. Visit [https://app.hyperbolic.xyz/](https://app.hyperbolic.xyz/) and sign in.
2. Go to **Settings ➔ API Keys**.
3. Create and copy your key.

### 1-Line Test Command (Terminal / cURL):
```bash
curl -X POST "https://api.hyperbolic.xyz/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_HYPERBOLIC_KEY" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Como Obter sua Chave Gratuita na Hyperbolic

* **Link Oficial:** [https://app.hyperbolic.xyz/](https://app.hyperbolic.xyz/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS ou Telefone?** ❌ **NÃO**
* **Destaques:** Taxa de até **60 RPM gratuitos** em modelos de código aberto.
