# ElevenLabs — Voice AI & Hi-Fi TTS (10,000 Chars/Month Free)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 ElevenLabs — Voice AI & Hi-Fi TTS (10,000 Chars/Month Free) Setup Guide

* **Official Platform:** [https://elevenlabs.io/](https://elevenlabs.io/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** 10,000 characters per month free forever renewed every 30 days.
  * **Rate Limits:** 20 RPM / 2 concurrent requests.
  * **Base Endpoint:** `https://api.elevenlabs.io/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`eleven_multilingual_v2`** | Eleven Multilingual v2 | 29 languages (inc. PT) | Gold standard emotional voice synthesis |
| **`eleven_flash_v2_5`** | Eleven Flash v2.5 | ~75ms latency | Real-time conversational agents and voice bots |
| **`eleven_turbo_v2_5`** | Eleven Turbo v2.5 | Low latency | High-speed voiceover generation |

### Step-by-Step Instructions:
1. Visit [https://elevenlabs.io/](https://elevenlabs.io/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export ELEVENLABS_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.elevenlabs.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ELEVENLABS_API_KEY" \
  -d '{
    "model": "eleven_multilingual_v2",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
headers = {
    "xi-api-key": "YOUR_ELEVENLABS_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "text": "Hello world from ElevenLabs free tier!",
    "model_id": "eleven_multilingual_v2"
}
response = requests.post(url, json=data, headers=headers)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
print("Saved speech.mp3")
```

---

<a name="português"></a>
## 🇧🇷 ElevenLabs — Síntese Vocal Hi-Fi (10.000 Chars/Mês Grátis Perpétuos) — Guia de Configuração

* **Link da Plataforma:** [https://elevenlabs.io/](https://elevenlabs.io/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** 10.000 caracteres por mês gratuitos permanentes sem cartão.
  * **Limites de Taxa:** 20 RPM / 2 concurrent requests.
  * **Endpoint Base:** `https://api.elevenlabs.io/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`eleven_multilingual_v2`** | Eleven Multilingual v2 | 29 languages (inc. PT) | Gold standard emotional voice synthesis |
| **`eleven_flash_v2_5`** | Eleven Flash v2.5 | ~75ms latency | Real-time conversational agents and voice bots |
| **`eleven_turbo_v2_5`** | Eleven Turbo v2.5 | Low latency | High-speed voiceover generation |

### Passo a Passo de Onboarding:
1. Acesse [https://elevenlabs.io/](https://elevenlabs.io/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export ELEVENLABS_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.elevenlabs.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ELEVENLABS_API_KEY" \
  -d '{
    "model": "eleven_multilingual_v2",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
headers = {
    "xi-api-key": "YOUR_ELEVENLABS_API_KEY",
    "Content-Type": "application/json"
}
data = {
    "text": "Hello world from ElevenLabs free tier!",
    "model_id": "eleven_multilingual_v2"
}
response = requests.post(url, json=data, headers=headers)
with open("speech.mp3", "wb") as f:
    f.write(response.content)
print("Saved speech.mp3")
```
