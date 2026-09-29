# Clarifai — [RETIRED / DESCONTINUADO] (Acquired by Nebius)

> ⚠️ **STATUS ALERT (July 2026 / Setembro 2026)**:
> **EN:** Clarifai officially ceased independent platform operations on **July 17, 2026** following its acquisition by **Nebius** (NASDAQ: NBIS). Clarifai's core research team and inference engine were absorbed into the **Nebius Token Factory** (`api.studio.nebius.ai`). The standalone `api.clarifai.com` APIs are no longer operational for new accounts.
> **PT:** A Clarifai encerrou formalmente suas operações independentes em **17 de julho de 2026** após sua aquisição pela **Nebius**. Sua equipe e tecnologia foram absorvidas pelo **Nebius Token Factory** (`api.studio.nebius.ai`). As APIs `api.clarifai.com` estão desligadas para novas contas.

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Clarifai — Platform Status & Nebius Migration

* **Official Status:** ❌ **RETIRED (July 17, 2026)** — Acquired by Nebius
* **Successor Platform:** [Nebius Token Factory](https://studio.nebius.ai/)
* **Original Platform:** [https://portal.clarifai.com/](https://portal.clarifai.com/)
* **Credit Card Required?** N/A (Platform retired)
* **Phone / SMS Verification?** N/A
* **Historical Free Quota (Legacy):**
  * **Free Allocation:** Previously 1,000 operations per month free.
  * **Status:** Discontinued. Users must migrate to Nebius Token Factory or active providers like Google AI Studio, NVIDIA NIM, and OpenRouter Free.

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
