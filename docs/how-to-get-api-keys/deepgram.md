# Deepgram — Nova-2 Speech-to-Text & Aura TTS ($200 Free Credits)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Deepgram — Nova-2 Speech-to-Text & Aura TTS ($200 Free Credits) Setup Guide

* **Official Platform:** [https://console.deepgram.com/](https://console.deepgram.com/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** $200 USD in free perpetual credits (~775 hours of Nova-2 STT).
  * **Rate Limits:** 1,000 RPM / 100 concurrent streams.
  * **Base Endpoint:** `https://api.deepgram.com/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`nova-2`** | Nova-2 Speech-to-Text | WAV, MP3, FLAC, OGG | Fastest & cheapest STT ($0.0043/min) |
| **`nova-2-general`** | Nova-2 Multilingual | 30+ languages (inc. pt-BR) | Accurate accents and punctuation |
| **`nova-2-meeting`** | Nova-2 Meetings | Conference multi-speaker | Speaker diarization and noise filtering |
| **`aura-asteria-en`** | Aura TTS Asteria | Text to Speech | Sub-200ms TTFB female conversational voice |
| **`aura-orion-en`** | Aura TTS Orion | Text to Speech | Deep natural male conversational voice |

### Step-by-Step Instructions:
1. Visit [https://console.deepgram.com/](https://console.deepgram.com/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export DEEPGRAM_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.deepgram.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPGRAM_API_KEY" \
  -d '{
    "model": "nova-2",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

url = "https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true"
headers = {
    "Authorization": "Token YOUR_DEEPGRAM_API_KEY",
    "Content-Type": "audio/wav"
}
with open("sample.wav", "rb") as audio:
    response = requests.post(url, headers=headers, data=audio)
print(response.json())
```

---

<a name="português"></a>
## 🇧🇷 Deepgram — Nova-2 STT & Aura TTS ($200 em Créditos Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://console.deepgram.com/](https://console.deepgram.com/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** $200 USD em créditos perpétuos sem cartão (~775 horas de STT).
  * **Limites de Taxa:** 1,000 RPM / 100 concurrent streams.
  * **Endpoint Base:** `https://api.deepgram.com/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`nova-2`** | Nova-2 Speech-to-Text | WAV, MP3, FLAC, OGG | Fastest & cheapest STT ($0.0043/min) |
| **`nova-2-general`** | Nova-2 Multilingual | 30+ languages (inc. pt-BR) | Accurate accents and punctuation |
| **`nova-2-meeting`** | Nova-2 Meetings | Conference multi-speaker | Speaker diarization and noise filtering |
| **`aura-asteria-en`** | Aura TTS Asteria | Text to Speech | Sub-200ms TTFB female conversational voice |
| **`aura-orion-en`** | Aura TTS Orion | Text to Speech | Deep natural male conversational voice |

### Passo a Passo de Onboarding:
1. Acesse [https://console.deepgram.com/](https://console.deepgram.com/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export DEEPGRAM_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.deepgram.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPGRAM_API_KEY" \
  -d '{
    "model": "nova-2",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

url = "https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true"
headers = {
    "Authorization": "Token YOUR_DEEPGRAM_API_KEY",
    "Content-Type": "audio/wav"
}
with open("sample.wav", "rb") as audio:
    response = requests.post(url, headers=headers, data=audio)
print(response.json())
```
