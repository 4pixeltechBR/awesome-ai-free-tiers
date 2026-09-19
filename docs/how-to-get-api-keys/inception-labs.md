# 🚀 Inception Labs (Mercury API) — 100M Free Tokens

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Inception Labs Setup Guide

* **Official Platform:** [https://platform.inceptionlabs.ai/](https://platform.inceptionlabs.ai/)
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ❌ **NO** (Google or GitHub OAuth)
* **Free Quota Highlights:**
  * **100,000,000 Free Tokens:** Automatically credited to your balance upon account creation.
  * **Rate Limits:** 60 RPM with up to 5 concurrent requests.
  * **Ultra-Low Latency:** Mercury architecture optimized for real-time sub-300ms time-to-first-token (TTFT) and 150+ tokens/sec throughput.
  * **OpenAI SDK Compatible:** Base URL `https://api.inceptionlabs.ai/v1`.
* **Canonical API Model IDs:**
  * **`mercury-chat`**: General conversational and document synthesis model (128k context).
  * **`mercury-coder`**: Specialized coding model for code completion, generation, and agentic workflows (128k context).

### Step-by-Step Instructions:
1. Visit [https://platform.inceptionlabs.ai/](https://platform.inceptionlabs.ai/) and sign in with Google or GitHub.
2. In the left navigation bar, click on **API Keys**.
3. Click **Create New Key**, assign a label, and copy your `sk-...` secret key.
4. Check your **Billing / Usage** tab to confirm your 100M free token balance.

### 1-Line Test Command (cURL):
```bash
curl https://api.inceptionlabs.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_INCEPTION_API_KEY" \
  -d '{
    "model": "mercury-chat",
    "messages": [{"role": "user", "content": "Explain Mercury architecture in one sentence."}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia de Configuração Inception Labs (Mercury API)

* **Link da Plataforma:** [https://platform.inceptionlabs.ai/](https://platform.inceptionlabs.ai/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS / Telefone?** ❌ **NÃO** (Login com Google ou GitHub)
* **Destaques da Cota Gratuita:**
  * **100.000.000 de Tokens Gratuitos:** Creditados automaticamente no saldo da conta no momento da criação.
  * **Limites de Taxa:** 60 requisições/minuto (RPM) e 5 conexões concorrentes.
  * **Velocidade Extrema:** Arquitetura proprietária Mercury com primeiro token abaixo de 300ms e mais de 150 tokens/segundo.
  * **Compatível com OpenAI SDK:** Endpoint base `https://api.inceptionlabs.ai/v1`.
* **Identificadores Canônicos de Modelo:**
  * **`mercury-chat`**: Modelo principal para conversação, síntese e raciocínio (128k contexto).
  * **`mercury-coder`**: Modelo especializado em geração, auditoria e refatoração de código (128k contexto).

### Passo a Passo:
1. Acesse [https://platform.inceptionlabs.ai/](https://platform.inceptionlabs.ai/) e faça login via Google ou GitHub.
2. No menu lateral, clique em **API Keys**.
3. Clique em **Create New Key**, defina um nome e copie sua chave de API.
4. Verifique na aba de **Billing** que os 100 Milhões de tokens estão ativos.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.inceptionlabs.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUA_CHAVE_INCEPTION" \
  -d '{
    "model": "mercury-chat",
    "messages": [{"role": "user", "content": "Olá, teste de bancada!"}]
  }'
```
