# 🌐 OpenRouter — 24 Free Models (:free tag)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 OpenRouter Free Models Setup Guide

* **Official Portal:** [https://openrouter.ai/](https://openrouter.ai/)
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ❌ **NO** (Google / GitHub / Crypto Wallet)
* **Free Quota Highlights:**
  * OpenRouter routes to over **24 models with the `:free` suffix** completely free of charge.
  * Rate limits for free models: **20 RPM / 200 requests per day (RPD)**.
  * Examples of active free models:
    * `google/gemini-2.0-flash-exp:free`
    * `meta-llama/llama-3.3-70b-instruct:free`
    * `mistralai/mistral-7b-instruct:free`
    * `deepseek/deepseek-r1:free`
    * `qwen/qwen-2.5-72b-instruct:free`

### Step-by-Step Instructions:
1. Visit [https://openrouter.ai/](https://openrouter.ai/) and click **Sign In** (via GitHub or Google).
2. Go to **Keys** ([https://openrouter.ai/keys](https://openrouter.ai/keys)) and click **"Create Key"**.
3. You do NOT need to add credits to call models that end with `:free`.
4. Copy your key (`sk-or-v1-...`).

### 1-Line Test Command (Terminal / cURL):
```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_OPENROUTER_KEY" \
  -d '{
    "model": "google/gemini-2.0-flash-exp:free",
    "messages": [{"role": "user", "content": "Say hello!"}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia de Modelos Gratuitos no OpenRouter

* **Link Oficial do Portal:** [https://openrouter.ai/](https://openrouter.ai/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS ou Telefone?** ❌ **NÃO** (Login com GitHub ou Google)
* **Destaques da Cota Gratuita:**
  * Mais de **24 modelos com sufixo `:free`** disponíveis gratuitamente.
  * Limite típico: **20 requisições/min (RPM) e 200 requisições/dia (RPD)** no nível gratuito.

### Passo a Passo:
1. Acesse [https://openrouter.ai/](https://openrouter.ai/) e faça login.
2. Vá na aba **Keys** e clique em **"Create Key"**.
3. Copie sua chave gerada (`sk-or-v1-...`).

### Teste Rápido no Terminal:
```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUA_CHAVE_OPENROUTER" \
  -d '{
    "model": "google/gemini-2.0-flash-exp:free",
    "messages": [{"role": "user", "content": "Diga ola!"}]
  }'
```
