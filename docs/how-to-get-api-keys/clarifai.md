# Clarifai — Community Free Tier (1,000 Free Ops/Month)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Clarifai — Community Free Tier (1,000 Free Ops/Month) Setup Guide

* **Official Platform:** [https://portal.clarifai.com/](https://portal.clarifai.com/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** 1,000 operations per month free forever without credit card.
  * **Rate Limits:** 10 RPM (1 concurrency).
  * **Base Endpoint:** `https://api.clarifai.com/v2`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`openai/chat-completion/models/gpt-4o`** | GPT-4o via Clarifai | 128.000 / 4.096 | Frontier multimodal LLM |
| **`meta/Llama-3/models/llama-3_3-70b-instruct`** | Llama 3.3 70B | 131.072 / 4.096 | Leading open-weight model |
| **`clarifai/main/models/general-image-recognition`** | Visual Classifier | Image / Tags | 10,000+ visual concept recognition |
| **`clarifai/main/models/text-moderation`** | Text Moderation | 8.192 / 128 | Safety guardrail filter |

### Step-by-Step Instructions:
1. Visit [https://portal.clarifai.com/](https://portal.clarifai.com/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export CLARIFAI_PAT="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.clarifai.com/v2/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLARIFAI_PAT" \
  -d '{
    "model": "openai/chat-completion/models/gpt-4o",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

headers = {
    "Authorization": "Key YOUR_CLARIFAI_PAT",
    "Content-Type": "application/json"
}
payload = {
    "inputs": [{"data": {"text": {"raw": "Hello Clarifai!"}}}]
}
response = requests.post(
    "https://api.clarifai.com/v2/users/openai/apps/chat-completion/models/gpt-4o/versions/latest/outputs",
    headers=headers, json=payload
)
print(response.json())
```

---

<a name="português"></a>
## 🇧🇷 Clarifai — Community Free Tier (1.000 Operações/Mês Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://portal.clarifai.com/](https://portal.clarifai.com/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** 1.000 operações por mês gratuitas permanentes sem cartão.
  * **Limites de Taxa:** 10 RPM (1 concurrency).
  * **Endpoint Base:** `https://api.clarifai.com/v2`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`openai/chat-completion/models/gpt-4o`** | GPT-4o via Clarifai | 128.000 / 4.096 | Frontier multimodal LLM |
| **`meta/Llama-3/models/llama-3_3-70b-instruct`** | Llama 3.3 70B | 131.072 / 4.096 | Leading open-weight model |
| **`clarifai/main/models/general-image-recognition`** | Visual Classifier | Image / Tags | 10,000+ visual concept recognition |
| **`clarifai/main/models/text-moderation`** | Text Moderation | 8.192 / 128 | Safety guardrail filter |

### Passo a Passo de Onboarding:
1. Acesse [https://portal.clarifai.com/](https://portal.clarifai.com/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export CLARIFAI_PAT="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.clarifai.com/v2/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLARIFAI_PAT" \
  -d '{
    "model": "openai/chat-completion/models/gpt-4o",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

headers = {
    "Authorization": "Key YOUR_CLARIFAI_PAT",
    "Content-Type": "application/json"
}
payload = {
    "inputs": [{"data": {"text": {"raw": "Hello Clarifai!"}}}]
}
response = requests.post(
    "https://api.clarifai.com/v2/users/openai/apps/chat-completion/models/gpt-4o/versions/latest/outputs",
    headers=headers, json=payload
)
print(response.json())
```
