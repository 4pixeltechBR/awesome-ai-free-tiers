# Lemonfox.ai — Whisper STT, TTS & Embeddings (1-Month Free Trial + $5/mo Budget Plan)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Lemonfox.ai — Whisper STT, TTS & Embeddings (1-Month Free Trial + $5/mo Budget Plan) Setup Guide

* **Official Platform:** [https://lemonfox.ai/](https://lemonfox.ai/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** 1-month free trial with 10M compute credits (~100 hours of Whisper STT or TTS). Followed by an accessible micro-budget plan at $5/month (50M credits).
  * **Rate Limits:** 20 RPM (trial and developer allocation).
  * **Base Endpoint:** `https://api.lemonfox.ai/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`whisper-1`** | Lemonfox Whisper STT | OpenAI /audio/transcriptions | Direct drop-in replacement for OpenAI Whisper |
| **`lemonfox-tts-v1`** | Lemonfox TTS | OpenAI /audio/speech | Fast MP3/WAV speech synthesis |
| **`lemonfox-embed-v1`** | Lemonfox Embeddings | OpenAI /embeddings | Fast semantic text embeddings |

### Step-by-Step Instructions:
1. Visit [https://lemonfox.ai/](https://lemonfox.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export LEMONFOX_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.lemonfox.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LEMONFOX_API_KEY" \
  -d '{
    "model": "whisper-1",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.lemonfox.ai/v1",
    api_key="YOUR_LEMONFOX_API_KEY"
)

with open("audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
print(transcript.text)
```

---

<a name="português"></a>
## 🇧🇷 Lemonfox.ai — Whisper STT, TTS e Embeddings (Trial Gratuito de 1 Mês + Plano Budget de $5/mês) — Guia de Configuração

* **Link da Plataforma:** [https://lemonfox.ai/](https://lemonfox.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** Trial gratuito de 1 mês com 10M de créditos de computação (~100 horas de Whisper STT ou TTS). Após o período, oferece plano budget ultra-acessível de $5/mês (50M créditos).
  * **Limites de Taxa:** 20 RPM (alocação de trial e desenvolvedor).
  * **Endpoint Base:** `https://api.lemonfox.ai/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`whisper-1`** | Lemonfox Whisper STT | OpenAI /audio/transcriptions | Direct drop-in replacement for OpenAI Whisper |
| **`lemonfox-tts-v1`** | Lemonfox TTS | OpenAI /audio/speech | Fast MP3/WAV speech synthesis |
| **`lemonfox-embed-v1`** | Lemonfox Embeddings | OpenAI /embeddings | Fast semantic text embeddings |

### Passo a Passo de Onboarding:
1. Acesse [https://lemonfox.ai/](https://lemonfox.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export LEMONFOX_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.lemonfox.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LEMONFOX_API_KEY" \
  -d '{
    "model": "whisper-1",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.lemonfox.ai/v1",
    api_key="YOUR_LEMONFOX_API_KEY"
)

with open("audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
print(transcript.text)
```
