# Cartesia — Sonic Ultra-Low Latency Voice API (<150ms TTFB)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Cartesia — Sonic Ultra-Low Latency Voice API (<150ms TTFB) Setup Guide

* **Official Platform:** [https://play.cartesia.ai/](https://play.cartesia.ai/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** Sonic API Free Tier starter credits (~100,000 characters).
  * **Rate Limits:** 30 RPM / 10 concurrent streams.
  * **Base Endpoint:** `https://api.cartesia.ai/tts/bytes`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`sonic-english`** | Sonic English | 44.1kHz Stereo | Sub-150ms real-time conversational synthesis |
| **`sonic-multilingual`** | Sonic Multilingual | Multiple languages | Natural voice in French, Spanish, German, Portuguese |
| **`sonic-fast`** | Sonic Fast | 24kHz optimized | Ultra-low bandwidth and instant packet streaming |

### Step-by-Step Instructions:
1. Visit [https://play.cartesia.ai/](https://play.cartesia.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export CARTESIA_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.cartesia.ai/tts/bytes/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CARTESIA_API_KEY" \
  -d '{
    "model": "sonic-english",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

url = "https://api.cartesia.ai/tts/bytes"
headers = {
    "X-API-Key": "YOUR_CARTESIA_API_KEY",
    "Cartesia-Version": "2024-06-10",
    "Content-Type": "application/json"
}
payload = {
    "model_id": "sonic-english",
    "transcript": "Hello from Cartesia Sonic real-time voice.",
    "voice": {"mode": "id", "id": "a0e99841-438c-4a64-b679-ae501e7d6091"},
    "output_format": {"container": "raw", "encoding": "pcm_s16le", "sample_rate": 24000}
}
res = requests.post(url, json=payload, headers=headers)
print("Audio bytes received:", len(res.content))
```

---

<a name="português"></a>
## 🇧🇷 Cartesia — Sonic API de Voz Ultra-Rápida (<150ms de Latência) — Guia de Configuração

* **Link da Plataforma:** [https://play.cartesia.ai/](https://play.cartesia.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** Free Tier Sonic API com créditos iniciais de teste sem cartão.
  * **Limites de Taxa:** 30 RPM / 10 concurrent streams.
  * **Endpoint Base:** `https://api.cartesia.ai/tts/bytes`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`sonic-english`** | Sonic English | 44.1kHz Stereo | Sub-150ms real-time conversational synthesis |
| **`sonic-multilingual`** | Sonic Multilingual | Multiple languages | Natural voice in French, Spanish, German, Portuguese |
| **`sonic-fast`** | Sonic Fast | 24kHz optimized | Ultra-low bandwidth and instant packet streaming |

### Passo a Passo de Onboarding:
1. Acesse [https://play.cartesia.ai/](https://play.cartesia.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export CARTESIA_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.cartesia.ai/tts/bytes/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CARTESIA_API_KEY" \
  -d '{
    "model": "sonic-english",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

url = "https://api.cartesia.ai/tts/bytes"
headers = {
    "X-API-Key": "YOUR_CARTESIA_API_KEY",
    "Cartesia-Version": "2024-06-10",
    "Content-Type": "application/json"
}
payload = {
    "model_id": "sonic-english",
    "transcript": "Hello from Cartesia Sonic real-time voice.",
    "voice": {"mode": "id", "id": "a0e99841-438c-4a64-b679-ae501e7d6091"},
    "output_format": {"container": "raw", "encoding": "pcm_s16le", "sample_rate": 24000}
}
res = requests.post(url, json=payload, headers=headers)
print("Audio bytes received:", len(res.content))
```
