# CentML (CServe) — Compiled Accelerated Serverless Inference (Free Trial)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 CentML (CServe) — Compiled Accelerated Serverless Inference (Free Trial) Setup Guide

* **Official Platform:** [https://centml.ai/](https://centml.ai/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** Developer trial credits for compiled model execution.
  * **Rate Limits:** 60 RPM / 100.000 TPM.
  * **Base Endpoint:** `https://api.centml.com/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B CServe | 131.072 / 4.096 | Kernel compilation up to 3x faster than vanilla vLLM |
| **`meta-llama/Llama-3.1-8B-Instruct`** | Llama 3.1 8B CServe | 131.072 / 4.096 | Ultra-fast low-latency triage model |
| **`mistralai/Mistral-Small-24B-Instruct-2501`** | Mistral Small 24B | 32.768 / 4.096 | Balanced reasoning and extraction engine |

### Step-by-Step Instructions:
1. Visit [https://centml.ai/](https://centml.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export CENTML_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.centml.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CENTML_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.centml.com/v1",
    api_key="YOUR_CENTML_API_KEY"
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": "How does CServe kernel acceleration work?"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

---

<a name="português"></a>
## 🇧🇷 CentML (CServe) — Inferência Serverless Compilada (Free Trial) — Guia de Configuração

* **Link da Plataforma:** [https://centml.ai/](https://centml.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** Créditos de teste de desenvolvedor para inferência compilada.
  * **Limites de Taxa:** 60 RPM / 100.000 TPM.
  * **Endpoint Base:** `https://api.centml.com/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`meta-llama/Llama-3.3-70B-Instruct`** | Llama 3.3 70B CServe | 131.072 / 4.096 | Kernel compilation up to 3x faster than vanilla vLLM |
| **`meta-llama/Llama-3.1-8B-Instruct`** | Llama 3.1 8B CServe | 131.072 / 4.096 | Ultra-fast low-latency triage model |
| **`mistralai/Mistral-Small-24B-Instruct-2501`** | Mistral Small 24B | 32.768 / 4.096 | Balanced reasoning and extraction engine |

### Passo a Passo de Onboarding:
1. Acesse [https://centml.ai/](https://centml.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export CENTML_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.centml.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CENTML_API_KEY" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.centml.com/v1",
    api_key="YOUR_CENTML_API_KEY"
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": "How does CServe kernel acceleration work?"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```
