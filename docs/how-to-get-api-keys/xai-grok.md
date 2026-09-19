# xAI Console — Grok API ($25/Month Developer Grant)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 xAI Console — Grok API ($25/Month Developer Grant) Setup Guide

* **Official Platform:** [https://console.x.ai/](https://console.x.ai/)
* **Credit Card Required?** ❌ NO / NÃO (for developer tier grant with verified X account)
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** $25.00 USD / month recurring grant for active developers.
  * **Rate Limits:** 60 RPM / 10.000 TPM.
  * **Base Endpoint:** `https://api.x.ai/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`grok-2-1212`** | Grok 2 (1212) | 131.072 / 4.096 | High-intelligence reasoning and general chat |
| **`grok-2-vision-1212`** | Grok 2 Vision | 32.768 / 4.096 | Multimodal text and image analysis |
| **`grok-beta`** | Grok Beta | 131.072 / 4.096 | Continuous release flagship model |
| **`grok-vision-beta`** | Grok Vision Beta | 8.192 / 4.096 | Visual understanding and inspection |

### Step-by-Step Instructions:
1. Visit [https://console.x.ai/](https://console.x.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export XAI_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.x.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-2-1212",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.x.ai/v1",
    api_key="YOUR_XAI_API_KEY"
)

response = client.chat.completions.create(
    model="grok-2-1212",
    messages=[{"role": "user", "content": "What makes Grok unique?"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

---

<a name="português"></a>
## 🇧🇷 xAI Console — Grok API ($25/Mês de Grant de Desenvolvedor) — Guia de Configuração

* **Link da Plataforma:** [https://console.x.ai/](https://console.x.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO (for developer tier grant with verified X account)
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** $25.00 USD / mês em créditos concedidos para desenvolvedores.
  * **Limites de Taxa:** 60 RPM / 10.000 TPM.
  * **Endpoint Base:** `https://api.x.ai/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`grok-2-1212`** | Grok 2 (1212) | 131.072 / 4.096 | High-intelligence reasoning and general chat |
| **`grok-2-vision-1212`** | Grok 2 Vision | 32.768 / 4.096 | Multimodal text and image analysis |
| **`grok-beta`** | Grok Beta | 131.072 / 4.096 | Continuous release flagship model |
| **`grok-vision-beta`** | Grok Vision Beta | 8.192 / 4.096 | Visual understanding and inspection |

### Passo a Passo de Onboarding:
1. Acesse [https://console.x.ai/](https://console.x.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export XAI_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.x.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d '{
    "model": "grok-2-1212",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.x.ai/v1",
    api_key="YOUR_XAI_API_KEY"
)

response = client.chat.completions.create(
    model="grok-2-1212",
    messages=[{"role": "user", "content": "What makes Grok unique?"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```
