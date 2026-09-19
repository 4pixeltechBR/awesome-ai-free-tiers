# ModelScope (Alibaba DAMO) — Permanent Free Community Serverless Inference

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 ModelScope (Alibaba DAMO) — Permanent Free Community Serverless Inference Setup Guide

* **Official Platform:** [https://modelscope.cn/](https://modelscope.cn/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO (Free email registration)
* **Free Quota Highlights:**
  * **Free Allocation:** Permanent 100% free daily serverless inference on community models.
  * **Rate Limits:** 30 RPM / 1,000 RPD.
  * **Base Endpoint:** `https://api-inference.modelscope.cn/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`Qwen/Qwen2.5-72B-Instruct`** | Qwen 2.5 72B | 32.768 / 8.192 | Leading open-source model hosted serverless |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`** | Qwen 2.5 Coder 32B | 32.768 / 8.192 | Specialized coding LLM |
| **`ZhipuAI/glm-4-9b-chat`** | GLM-4 9B | 32.768 / 4.096 | Fast dialogue and extraction |
| **`iic/SenseVoiceSmall`** | SenseVoice Small STT | Audio in 5+ languages | Sub-100ms multi-lingual speech-to-text |
| **`damo/cv_tinynas_object-detection`** | TinyNAS Vision | Image / Bounding boxes | Real-time object detection |

### Step-by-Step Instructions:
1. Visit [https://modelscope.cn/](https://modelscope.cn/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export MODELSCOPE_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api-inference.modelscope.cn/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MODELSCOPE_API_KEY" \
  -d '{
    "model": "Qwen/Qwen2.5-72B-Instruct",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api-inference.modelscope.cn/v1",
    api_key="YOUR_MODELSCOPE_API_KEY"
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-72B-Instruct",
    messages=[{"role": "user", "content": "Hello from ModelScope free inference!"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

---

<a name="português"></a>
## 🇧🇷 ModelScope (Alibaba DAMO) — Inferência Serverless Gratuita Permanente — Guia de Configuração

* **Link da Plataforma:** [https://modelscope.cn/](https://modelscope.cn/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO (Free email registration)
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** Inferência serverless comunitária 100% gratuita perpétua sem cartão.
  * **Limites de Taxa:** 30 RPM / 1,000 RPD.
  * **Endpoint Base:** `https://api-inference.modelscope.cn/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`Qwen/Qwen2.5-72B-Instruct`** | Qwen 2.5 72B | 32.768 / 8.192 | Leading open-source model hosted serverless |
| **`Qwen/Qwen2.5-Coder-32B-Instruct`** | Qwen 2.5 Coder 32B | 32.768 / 8.192 | Specialized coding LLM |
| **`ZhipuAI/glm-4-9b-chat`** | GLM-4 9B | 32.768 / 4.096 | Fast dialogue and extraction |
| **`iic/SenseVoiceSmall`** | SenseVoice Small STT | Audio in 5+ languages | Sub-100ms multi-lingual speech-to-text |
| **`damo/cv_tinynas_object-detection`** | TinyNAS Vision | Image / Bounding boxes | Real-time object detection |

### Passo a Passo de Onboarding:
1. Acesse [https://modelscope.cn/](https://modelscope.cn/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export MODELSCOPE_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api-inference.modelscope.cn/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MODELSCOPE_API_KEY" \
  -d '{
    "model": "Qwen/Qwen2.5-72B-Instruct",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api-inference.modelscope.cn/v1",
    api_key="YOUR_MODELSCOPE_API_KEY"
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-72B-Instruct",
    messages=[{"role": "user", "content": "Hello from ModelScope free inference!"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```
