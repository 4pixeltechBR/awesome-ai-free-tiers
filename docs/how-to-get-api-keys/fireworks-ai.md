# Fireworks AI — Ultra-Fast Serverless LLM Inference ($1 Free)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Fireworks AI — Ultra-Fast Serverless LLM Inference ($1 Free) Setup Guide

* **Official Platform:** [https://fireworks.ai/](https://fireworks.ai/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** $1.00 USD free credits on signup without credit card.
  * **Rate Limits:** 600 RPM.
  * **Base Endpoint:** `https://api.fireworks.ai/inference/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`accounts/fireworks/models/llama-v3p3-70b-instruct`** | Llama 3.3 70B Instruct | 131.072 / 4.096 | Open-source workhorse with FireAttention speed |
| **`accounts/fireworks/models/qwen2p5-72b-instruct`** | Qwen 2.5 72B Instruct | 131.072 / 8.192 | Top reasoning and coding model |
| **`accounts/fireworks/models/deepseek-v3`** | DeepSeek-V3 | 131.072 / 8.192 | 671B parameter MoE frontier model |
| **`accounts/fireworks/models/deepseek-r1`** | DeepSeek-R1 | 131.072 / 16.384 | Reasoning model with CoT tokens |
| **`accounts/fireworks/models/firefunction-v2`** | FireFunction v2 | 8.192 / 4.096 | Optimized function/tool calling |

### Step-by-Step Instructions:
1. Visit [https://fireworks.ai/](https://fireworks.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export FIREWORKS_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/llama-v3p3-70b-instruct",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="YOUR_FIREWORKS_API_KEY"
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p3-70b-instruct",
    messages=[{"role": "user", "content": "Explain serverless inference in one sentence."}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

---

<a name="português"></a>
## 🇧🇷 Fireworks AI — Inferência Serverless de Alta Velocidade ($1 Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://fireworks.ai/](https://fireworks.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** $1.00 USD de crédito gratuito no cadastro sem cartão.
  * **Limites de Taxa:** 600 RPM.
  * **Endpoint Base:** `https://api.fireworks.ai/inference/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`accounts/fireworks/models/llama-v3p3-70b-instruct`** | Llama 3.3 70B Instruct | 131.072 / 4.096 | Open-source workhorse with FireAttention speed |
| **`accounts/fireworks/models/qwen2p5-72b-instruct`** | Qwen 2.5 72B Instruct | 131.072 / 8.192 | Top reasoning and coding model |
| **`accounts/fireworks/models/deepseek-v3`** | DeepSeek-V3 | 131.072 / 8.192 | 671B parameter MoE frontier model |
| **`accounts/fireworks/models/deepseek-r1`** | DeepSeek-R1 | 131.072 / 16.384 | Reasoning model with CoT tokens |
| **`accounts/fireworks/models/firefunction-v2`** | FireFunction v2 | 8.192 / 4.096 | Optimized function/tool calling |

### Passo a Passo de Onboarding:
1. Acesse [https://fireworks.ai/](https://fireworks.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export FIREWORKS_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.fireworks.ai/inference/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIREWORKS_API_KEY" \
  -d '{
    "model": "accounts/fireworks/models/llama-v3p3-70b-instruct",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="YOUR_FIREWORKS_API_KEY"
)

response = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p3-70b-instruct",
    messages=[{"role": "user", "content": "Explain serverless inference in one sentence."}],
    max_tokens=100
)
print(response.choices[0].message.content)
```
