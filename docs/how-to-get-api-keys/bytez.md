# 📦 Bytez — $1.00 Recurring Every 4 Weeks (Free Tier)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Bytez Setup Guide

* **Official Platform:** [https://bytez.com/](https://bytez.com/)
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ❌ **NO**
* **Free Quota Highlights:**
  * **$1.00 USD Free Credit Renewed Every 4 Weeks (28 Days):** Automatically replenished on your balance.
  * **Real Value:** Because open weights on Bytez are billed at fractions of a cent, \$1 gives you between **2,000,000 and 5,000,000 tokens** per cycle.
  * **OpenAI SDK Compatible:** Base URL `https://api.bytez.com/v1`.
* **Available Models:**
  * `meta-llama/llama-3.3-70b-instruct`
  * `qwen/qwen-2.5-72b-instruct`
  * `mistralai/mistral-7b-instruct`

### Step-by-Step Instructions:
1. Visit [https://bytez.com/](https://bytez.com/) and register with your email or GitHub.
2. Go to **Dashboard > API Keys**.
3. Generate a new API key and copy it.
4. Check your recurring credit cycle under **Account > Credits**.

### 1-Line Test Command (cURL):
```bash
curl https://api.bytez.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BYTEZ_KEY" \
  -d '{
    "model": "meta-llama/llama-3.3-70b-instruct",
    "messages": [{"role": "user", "content": "Hello from Bytez!"}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia de Configuração Bytez

* **Link da Plataforma:** [https://bytez.com/](https://bytez.com/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS / Telefone?** ❌ **NÃO**
* **Destaques da Cota Gratuita:**
  * **$1.00 USD de Crédito Renovado a Cada 4 Semanas (28 Dias):** Reabastecido automaticamente sem ação manual.
  * **Rendimento Real:** Com os preços de atacado da plataforma, $1 rende entre **2 e 5 Milhões de tokens** por ciclo em modelos abertos de topo.
  * **Compatível com OpenAI SDK:** Endpoint `https://api.bytez.com/v1`.
* **Modelos Disponíveis:**
  * `meta-llama/llama-3.3-70b-instruct`
  * `qwen/qwen-2.5-72b-instruct`
  * `mistralai/mistral-7b-instruct`

### Passo a Passo:
1. Acesse [https://bytez.com/](https://bytez.com/) e crie sua conta com email ou GitHub.
2. Navegue até **Dashboard > API Keys**.
3. Crie uma nova chave e copie seu identificador.
4. Verifique o ciclo de renovação dos seus créditos em **Account > Credits**.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.bytez.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUA_CHAVE_BYTEZ" \
  -d '{
    "model": "meta-llama/llama-3.3-70b-instruct",
    "messages": [{"role": "user", "content": "Olá Bytez!"}]
  }'
```
