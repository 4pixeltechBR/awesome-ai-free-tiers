# Exa.ai — Neural Semantic Web Search for LLMs ($10 Free Credits)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Exa.ai — Neural Semantic Web Search for LLMs ($10 Free Credits) Setup Guide

* **Official Platform:** [https://dashboard.exa.ai/](https://dashboard.exa.ai/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** $10 USD in free credits (1,000 neural searches) on signup.
  * **Rate Limits:** 60 RPM.
  * **Base Endpoint:** `https://api.exa.ai`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`exa-search-neural`** | Exa Neural Search | Semantic query | Predicts the best web links based on semantic meaning |
| **`exa-search-keyword`** | Exa Keyword Search | Lexical query | Exact text matching for specific technical terms |
| **`exa-get-contents`** | Exa Content Extraction | URL list | Pulls full cleaned markdown with highlights |

### Step-by-Step Instructions:
1. Visit [https://dashboard.exa.ai/](https://dashboard.exa.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export EXA_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.exa.ai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "model": "search",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

url = "https://api.exa.ai/search"
headers = {"x-api-key": "YOUR_EXA_API_KEY", "Content-Type": "application/json"}
data = {
    "query": "Promising open-source AI frameworks released in 2026",
    "type": "neural",
    "use_autoprompt": True,
    "num_results": 3
}
res = requests.post(url, headers=headers, json=data)
print(res.json())
```

---

<a name="português"></a>
## 🇧🇷 Exa.ai — Busca Neural Semântica para LLMs ($10 em Créditos Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://dashboard.exa.ai/](https://dashboard.exa.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** $10 USD em créditos gratuitos sem cartão (~1.000 buscas semânticas).
  * **Limites de Taxa:** 60 RPM.
  * **Endpoint Base:** `https://api.exa.ai`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`exa-search-neural`** | Exa Neural Search | Semantic query | Predicts the best web links based on semantic meaning |
| **`exa-search-keyword`** | Exa Keyword Search | Lexical query | Exact text matching for specific technical terms |
| **`exa-get-contents`** | Exa Content Extraction | URL list | Pulls full cleaned markdown with highlights |

### Passo a Passo de Onboarding:
1. Acesse [https://dashboard.exa.ai/](https://dashboard.exa.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export EXA_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.exa.ai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $EXA_API_KEY" \
  -d '{
    "model": "search",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

url = "https://api.exa.ai/search"
headers = {"x-api-key": "YOUR_EXA_API_KEY", "Content-Type": "application/json"}
data = {
    "query": "Promising open-source AI frameworks released in 2026",
    "type": "neural",
    "use_autoprompt": True,
    "num_results": 3
}
res = requests.post(url, headers=headers, json=data)
print(res.json())
```
