# 🇪🇺 Mistral AI (La Plateforme) — Free Tier Setup Guide

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Mistral AI Free Tier Guide

* **Official Portal:** [https://console.mistral.ai/](https://console.mistral.ai/)
* **Credit Card Required?** ❌ **NO** (Experimentation Free Tier)
* **Phone / SMS Verification?** ✅ **YES** (Phone verification required to activate API keys)
* **Free Quota Highlights:**
  * Free Experimentation Tier: **60 RPM / 4,000,000 tokens per month**
  * Models available: `codestral-latest`, `mistral-small-latest`, `ministral-8b-latest`, `mistral-embed`

### Step-by-Step Instructions:
1. Visit [https://console.mistral.ai/](https://console.mistral.ai/) and register an account.
2. Complete SMS phone verification.
3. Go to **"API Keys"** in the sidebar.
4. Click **"Create new key"** and copy your token.

### 1-Line Test Command (Terminal / cURL):
```bash
curl https://api.mistral.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_MISTRAL_API_KEY" \
  -d '{
    "model": "mistral-small-latest",
    "messages": [{"role": "user", "content": "Bonjour Mistral!"}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia de Cota Gratuita na Mistral AI

* **Link Oficial do Console:** [https://console.mistral.ai/](https://console.mistral.ai/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS ou Telefone?** ✅ **SIM** (Verificação por SMS necessária)
* **Destaques da Cota Gratuita:**
  * Cota de Experimentação: **60 RPM e até 4 Milhões de tokens por mês gratuitos**.
  * Modelos suportados: `codestral-latest`, `mistral-small-latest`, `ministral-8b-latest`.

### Passo a Passo:
1. Acesse [https://console.mistral.ai/](https://console.mistral.ai/) e cadastre-se.
2. Complete a validação do número de celular por SMS.
3. Acesse a aba **"API Keys"** e gere sua chave.

### Teste Rápido no Terminal:
```bash
curl https://api.mistral.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUA_CHAVE_MISTRAL" \
  -d '{
    "model": "mistral-small-latest",
    "messages": [{"role": "user", "content": "Ola Mistral!"}]
  }'
```
