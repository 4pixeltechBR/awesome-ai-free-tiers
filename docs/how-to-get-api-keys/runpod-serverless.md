# RunPod Serverless — Scale-to-Zero vLLM Endpoints ($5 Budget Gateway)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 RunPod Serverless — Scale-to-Zero vLLM Endpoints ($5 Budget Gateway) Setup Guide

* **Official Platform:** [https://www.runpod.io/](https://www.runpod.io/)
* **Credit Card Required?** 🟠 YES / SIM (for $5 minimum micro-wallet reload) or community promo code
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** Micro-budget gateway ($5 USD) with true scale-to-zero and per-second billing.
  * **Rate Limits:** Dynamic auto-scaling (0 to 10+ worker GPU replicas).
  * **Base Endpoint:** `https://api.runpod.ai/v2/{endpoint_id}/openai/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B vLLM | 131.072 / 4.096 | A100/H100 serverless template (~$0.0007/sec) |
| **`deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`** | DeepSeek-R1 Distill 32B | 131.072 / 8.192 | RTX 4090 template (~$0.0003/sec) |
| **`mistralai/Mistral-7B-Instruct-v0.3`** | Mistral 7B v0.3 | 32.768 / 4.096 | Ultra-low cost serverless (~$0.0002/sec) |

### Step-by-Step Instructions:
1. Visit [https://www.runpod.io/](https://www.runpod.io/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export RUNPOD_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.runpod.ai/v2/{endpoint_id}/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $RUNPOD_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

# Replace ENDPOINT_ID with your deployed serverless endpoint ID
client = OpenAI(
    base_url="https://api.runpod.ai/v2/ENDPOINT_ID/openai/v1",
    api_key="YOUR_RUNPOD_API_KEY"
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": "Explain per-second serverless GPU billing."}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

---

<a name="português"></a>
## 🇧🇷 RunPod Serverless — Endpoints vLLM com Scale-to-Zero (Gateway de $5) — Guia de Configuração

* **Link da Plataforma:** [https://www.runpod.io/](https://www.runpod.io/)
* **Exige Cartão de Crédito?** 🟠 YES / SIM (for $5 minimum micro-wallet reload) or community promo code
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** Gateway de micro-orçamento ($5 USD) com cobrança por milissegundo e scale-to-zero.
  * **Limites de Taxa:** Dynamic auto-scaling (0 to 10+ worker GPU replicas).
  * **Endpoint Base:** `https://api.runpod.ai/v2/{endpoint_id}/openai/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B vLLM | 131.072 / 4.096 | A100/H100 serverless template (~$0.0007/sec) |
| **`deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`** | DeepSeek-R1 Distill 32B | 131.072 / 8.192 | RTX 4090 template (~$0.0003/sec) |
| **`mistralai/Mistral-7B-Instruct-v0.3`** | Mistral 7B v0.3 | 32.768 / 4.096 | Ultra-low cost serverless (~$0.0002/sec) |

### Passo a Passo de Onboarding:
1. Acesse [https://www.runpod.io/](https://www.runpod.io/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export RUNPOD_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.runpod.ai/v2/{endpoint_id}/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $RUNPOD_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

# Replace ENDPOINT_ID with your deployed serverless endpoint ID
client = OpenAI(
    base_url="https://api.runpod.ai/v2/ENDPOINT_ID/openai/v1",
    api_key="YOUR_RUNPOD_API_KEY"
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": "Explain per-second serverless GPU billing."}],
    max_tokens=100
)
print(response.choices[0].message.content)
```
