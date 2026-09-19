# Tavily AI — Real-Time Web Search for Autonomous Agents (1,000 Searches/Mo Free)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Tavily AI — Real-Time Web Search for Autonomous Agents (1,000 Searches/Mo Free) Setup Guide

* **Official Platform:** [https://app.tavily.com/](https://app.tavily.com/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** 1,000 search API credits per month free forever without credit card.
  * **Rate Limits:** 100 RPM.
  * **Base Endpoint:** `https://api.tavily.com`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`tavily-search-basic`** | Tavily Search (Basic) | Web Query | Cleaned markdown snippets for LLM context (1 credit) |
| **`tavily-search-advanced`** | Tavily Search (Advanced) | In-depth Web Query | Full raw content, academic & deep sources (2 credits) |
| **`tavily-extract`** | Tavily Extract | Raw URLs | Ad-free tabular and textual HTML extraction |

### Step-by-Step Instructions:
1. Visit [https://app.tavily.com/](https://app.tavily.com/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export TAVILY_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.tavily.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TAVILY_API_KEY" \
  -d '{
    "model": "search",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

url = "https://api.tavily.com/search"
payload = {
    "api_key": "YOUR_TAVILY_API_KEY",
    "query": "What are the latest breakthroughs in AI inference September 2026?",
    "search_depth": "basic",
    "include_answer": True
}
response = requests.post(url, json=payload)
print("Answer:", response.json().get("answer"))
```

---

<a name="português"></a>
## 🇧🇷 Tavily AI — Busca em Tempo Real para Agentes (1.000 Buscas/Mês Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://app.tavily.com/](https://app.tavily.com/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** 1.000 requisições de busca por mês gratuitas perpétuas sem cartão.
  * **Limites de Taxa:** 100 RPM.
  * **Endpoint Base:** `https://api.tavily.com`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`tavily-search-basic`** | Tavily Search (Basic) | Web Query | Cleaned markdown snippets for LLM context (1 credit) |
| **`tavily-search-advanced`** | Tavily Search (Advanced) | In-depth Web Query | Full raw content, academic & deep sources (2 credits) |
| **`tavily-extract`** | Tavily Extract | Raw URLs | Ad-free tabular and textual HTML extraction |

### Passo a Passo de Onboarding:
1. Acesse [https://app.tavily.com/](https://app.tavily.com/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export TAVILY_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.tavily.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TAVILY_API_KEY" \
  -d '{
    "model": "search",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

url = "https://api.tavily.com/search"
payload = {
    "api_key": "YOUR_TAVILY_API_KEY",
    "query": "What are the latest breakthroughs in AI inference September 2026?",
    "search_depth": "basic",
    "include_answer": True
}
response = requests.post(url, json=payload)
print("Answer:", response.json().get("answer"))
```
