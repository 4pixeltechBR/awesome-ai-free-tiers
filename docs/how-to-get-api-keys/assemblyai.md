# AssemblyAI — Speech-to-Text & LeMUR ($50 Free Credits)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 AssemblyAI — Speech-to-Text & LeMUR ($50 Free Credits) Setup Guide

* **Official Platform:** [https://assemblyai.com/](https://assemblyai.com/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** $50.00 USD in free credits (~100 to 330 hours of transcription).
  * **Rate Limits:** 100 RPM / 5 concurrent transcriptions.
  * **Base Endpoint:** `https://api.assemblyai.com/v2`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`best`** | Conformer-2 Best STT | Audio URL or upload | State-of-the-art accuracy ($0.0062/min) |
| **`nano`** | Conformer-2 Nano | Fast audio transcription | Ultra-fast low-cost STT ($0.0025/min) |
| **`lemur-70b-chat`** | LeMUR Speech LLM | Transcript + Prompt | QA, summarization and action items from audio |

### Step-by-Step Instructions:
1. Visit [https://assemblyai.com/](https://assemblyai.com/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export ASSEMBLYAI_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.assemblyai.com/v2/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ASSEMBLYAI_API_KEY" \
  -d '{
    "model": "best",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

headers = {"authorization": "YOUR_ASSEMBLYAI_API_KEY", "content-type": "application/json"}
data = {"audio_url": "https://storage.googleapis.com/aai-web-samples/5_Approaches_to_GenAI.mp3"}
response = requests.post("https://api.assemblyai.com/v2/transcript", json=data, headers=headers)
print(response.json())
```

---

<a name="português"></a>
## 🇧🇷 AssemblyAI — Speech-to-Text & LeMUR ($50 em Créditos Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://assemblyai.com/](https://assemblyai.com/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** $50.00 USD em créditos gratuitos sem cartão (~100h a 330h de áudio).
  * **Limites de Taxa:** 100 RPM / 5 concurrent transcriptions.
  * **Endpoint Base:** `https://api.assemblyai.com/v2`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`best`** | Conformer-2 Best STT | Audio URL or upload | State-of-the-art accuracy ($0.0062/min) |
| **`nano`** | Conformer-2 Nano | Fast audio transcription | Ultra-fast low-cost STT ($0.0025/min) |
| **`lemur-70b-chat`** | LeMUR Speech LLM | Transcript + Prompt | QA, summarization and action items from audio |

### Passo a Passo de Onboarding:
1. Acesse [https://assemblyai.com/](https://assemblyai.com/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export ASSEMBLYAI_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.assemblyai.com/v2/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ASSEMBLYAI_API_KEY" \
  -d '{
    "model": "best",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

headers = {"authorization": "YOUR_ASSEMBLYAI_API_KEY", "content-type": "application/json"}
data = {"audio_url": "https://storage.googleapis.com/aai-web-samples/5_Approaches_to_GenAI.mp3"}
response = requests.post("https://api.assemblyai.com/v2/transcript", json=data, headers=headers)
print(response.json())
```
