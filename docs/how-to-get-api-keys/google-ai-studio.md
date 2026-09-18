# 🟢 Google AI Studio (Gemini API) — How to Get Your Free API Key

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Google AI Studio Setup Guide

* **Official Portal:** [https://aistudio.google.com/](https://aistudio.google.com/)
* **Credit Card Required?** ❌ **NO** (Zero payment method needed for Free Tier)
* **Phone / SMS Verification?** ❌ **NO** (Standard Google Account login)
* **Free Quota Highlights:**
  * `gemini-2.5-flash`: **15 RPM / 1,000,000 TPM / 1,500 RPD**
  * `gemini-2.0-flash`: **15 RPM / 1,000,000 TPM / 1,500 RPD**
  * `gemini-3.5-flash-lite`: **15 RPM / 250,000 TPM / 500 RPD**
  * **Google Search Grounding:** 1,500 RPD free
  * **Google Maps Grounding:** 500 RPD free

### Step-by-Step Instructions:
1. Go to [https://aistudio.google.com/](https://aistudio.google.com/) and sign in with your Google account.
2. In the top-left sidebar, click **"Get API key"**.
3. Click **"Create API key"**.
4. Choose an existing Google Cloud project or click **"Create API key in new project"** (done instantly in 1 click).
5. Copy your generated key (`AIzaSy...`).

### 1-Line Test Command (Terminal / cURL):
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=YOUR_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"contents": [{"parts":[{"text": "Explain AI in 10 words"}]}]}'
```

---

<a name="português"></a>
## 🇧🇷 Como Obter sua Chave Gratuita no Google AI Studio

* **Link Oficial do Console:** [https://aistudio.google.com/](https://aistudio.google.com/)
* **Exige Cartão de Crédito?** ❌ **NÃO** (Cota gratuita sem cadastrar cartão)
* **Exige SMS ou Telefone?** ❌ **NÃO** (Basta ter uma Conta Google comum)
* **Destaques da Cota Gratuita:**
  * `gemini-2.5-flash`: **15 requisições/min (RPM) / 1.000.000 tokens/min / 1.500 requisições/dia (RPD)**
  * `gemini-2.0-flash`: **15 RPM / 1.000.000 TPM / 1.500 RPD**
  * `gemini-3.5-flash-lite`: **15 RPM / 250.000 TPM / 500 RPD**
  * **Busca no Google (Search Grounding):** 1.500 consultas/dia gratuitas
  * **Google Maps Grounding:** 500 consultas/dia gratuitas

### Passo a Passo:
1. Acesse [https://aistudio.google.com/](https://aistudio.google.com/) e faça login com sua conta Google.
2. No menu lateral esquerdo, clique no botão azul **"Get API key"**.
3. Clique em **"Create API key"**.
4. Selecione a opção **"Create API key in new project"** (cria um projeto novo instantaneamente sem burocracia).
5. Copie sua chave de API gerada (`AIzaSy...`) e salve em segurança no seu `.env`.

### Teste Rápido no Terminal:
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=SUA_CHAVE_API" \
  -H 'Content-Type: application/json' \
  -d '{"contents": [{"parts":[{"text": "Explique IA em 10 palavras"}]}]}'
```
