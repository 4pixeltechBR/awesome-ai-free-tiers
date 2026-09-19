# Baseten — Serverless Model Deployments ($30 Free Compute)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Baseten — Serverless Model Deployments ($30 Free Compute) Setup Guide

* **Official Platform:** [https://baseten.co/](https://baseten.co/)
* **Credit Card Required?** ❌ NO / NÃO (for initial $30 compute credits)
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** $30 USD free compute credits on onboarding.
  * **Rate Limits:** 60 RPM bridge default (scale to zero).
  * **Base Endpoint:** `https://bridge.baseten.co/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B Bridge | 131.072 / 4.096 | Serverless vLLM on A100/H100 |
| **`deepseek-ai/DeepSeek-V3`** | DeepSeek-V3 Bridge | 131.072 / 8.192 | High-throughput MoE deployment |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`** | Qwen 2.5 Coder 32B | 131.072 / 8.192 | Code generation specialist |
| **`mistralai/Mistral-Small-24B-Instruct-2501`** | Mistral Small 24B | 32.768 / 4.096 | Sub-200ms TTFT reasoning model |

### Step-by-Step Instructions:
1. Visit [https://baseten.co/](https://baseten.co/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export BASETEN_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://bridge.baseten.co/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BASETEN_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://bridge.baseten.co/v1",
    api_key="YOUR_BASETEN_API_KEY"
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": "What is Truss by Baseten?"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

---

<a name="português"></a>
## 🇧🇷 Baseten — Deploy Serverless de Modelos ($30 em Computação Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://baseten.co/](https://baseten.co/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO (for initial $30 compute credits)
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** $30 USD em créditos de computação gratuitos no onboarding.
  * **Limites de Taxa:** 60 RPM bridge default (scale to zero).
  * **Endpoint Base:** `https://bridge.baseten.co/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B Bridge | 131.072 / 4.096 | Serverless vLLM on A100/H100 |
| **`deepseek-ai/DeepSeek-V3`** | DeepSeek-V3 Bridge | 131.072 / 8.192 | High-throughput MoE deployment |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`** | Qwen 2.5 Coder 32B | 131.072 / 8.192 | Code generation specialist |
| **`mistralai/Mistral-Small-24B-Instruct-2501`** | Mistral Small 24B | 32.768 / 4.096 | Sub-200ms TTFT reasoning model |

### Passo a Passo de Onboarding:
1. Acesse [https://baseten.co/](https://baseten.co/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export BASETEN_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://bridge.baseten.co/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BASETEN_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://bridge.baseten.co/v1",
    api_key="YOUR_BASETEN_API_KEY"
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": "What is Truss by Baseten?"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```
