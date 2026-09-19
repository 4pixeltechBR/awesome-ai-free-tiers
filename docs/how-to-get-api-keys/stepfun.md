# StepFun (Jieyue Xingchen) — 256k Long-Context & MoE (¥50 RMB Free)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 StepFun (Jieyue Xingchen) — 256k Long-Context & MoE (¥50 RMB Free) Setup Guide

* **Official Platform:** [https://platform.stepfun.ai/](https://platform.stepfun.ai/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** Phone signup (international codes supported)
* **Free Quota Highlights:**
  * **Free Allocation:** ¥50 RMB (~$7.00 USD) welcome grant on registration.
  * **Rate Limits:** 60 RPM / 100.000 TPM.
  * **Base Endpoint:** `https://api.stepfun.com/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`step-1-8k`** | Step-1 8K | 8.192 / 4.096 | Ultra-fast response for short conversations |
| **`step-1-32k`** | Step-1 32K | 32.768 / 4.096 | Balanced context and low latency |
| **`step-1-128k`** | Step-1 128K | 131.072 / 4.096 | Long document ingestion and legal synthesis |
| **`step-1-256k`** | Step-1 256K | 262.144 / 8.192 | Colossal 256k token context window |
| **`step-1v-8k`** | Step-1V Vision | Multimodal | Vision-language OCR and diagram understanding |
| **`step-2-16k`** | Step-2 MoE | MoE Reasoning | Frontier-level logical analysis and problem solving |
| **`step-audio-3`** | StepAudio v3 | Audio Native | Direct audio comprehension and voice interaction |

### Step-by-Step Instructions:
1. Visit [https://platform.stepfun.ai/](https://platform.stepfun.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export STEPFUN_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.stepfun.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STEPFUN_API_KEY" \
  -d '{
    "model": "step-1-32k",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.stepfun.com/v1",
    api_key="YOUR_STEPFUN_API_KEY"
)

response = client.chat.completions.create(
    model="step-1-32k",
    messages=[{"role": "user", "content": "Hello from StepFun API!"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

---

<a name="português"></a>
## 🇧🇷 StepFun (Jieyue Xingchen) — Contexto de 256k & MoE (¥50 RMB Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://platform.stepfun.ai/](https://platform.stepfun.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** Phone signup (international codes supported)
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** ¥50 RMB (~$7.00 USD) em créditos de boas-vindas sem cartão.
  * **Limites de Taxa:** 60 RPM / 100.000 TPM.
  * **Endpoint Base:** `https://api.stepfun.com/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`step-1-8k`** | Step-1 8K | 8.192 / 4.096 | Ultra-fast response for short conversations |
| **`step-1-32k`** | Step-1 32K | 32.768 / 4.096 | Balanced context and low latency |
| **`step-1-128k`** | Step-1 128K | 131.072 / 4.096 | Long document ingestion and legal synthesis |
| **`step-1-256k`** | Step-1 256K | 262.144 / 8.192 | Colossal 256k token context window |
| **`step-1v-8k`** | Step-1V Vision | Multimodal | Vision-language OCR and diagram understanding |
| **`step-2-16k`** | Step-2 MoE | MoE Reasoning | Frontier-level logical analysis and problem solving |
| **`step-audio-3`** | StepAudio v3 | Audio Native | Direct audio comprehension and voice interaction |

### Passo a Passo de Onboarding:
1. Acesse [https://platform.stepfun.ai/](https://platform.stepfun.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export STEPFUN_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.stepfun.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $STEPFUN_API_KEY" \
  -d '{
    "model": "step-1-32k",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.stepfun.com/v1",
    api_key="YOUR_STEPFUN_API_KEY"
)

response = client.chat.completions.create(
    model="step-1-32k",
    messages=[{"role": "user", "content": "Hello from StepFun API!"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```
