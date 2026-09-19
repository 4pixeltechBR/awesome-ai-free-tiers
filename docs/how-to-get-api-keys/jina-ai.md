# Jina AI — Embeddings, Rerankers & Reader API (10M Free Tokens)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Jina AI — Embeddings, Rerankers & Reader API (10M Free Tokens) Setup Guide

* **Official Platform:** [https://cloud.jina.ai/](https://cloud.jina.ai/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** 10M free tokens on signup + Jina Reader (r.jina.ai) 100% free forever.
  * **Rate Limits:** 500 RPM with key / 20 RPM anonymous Reader.
  * **Base Endpoint:** `https://api.jina.ai/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`jina-embeddings-v3`** | Jina Embeddings v3 | 8.192 ctx / Matryoshka dims | 89 languages, adaptive dimension representation |
| **`jina-reranker-v2-base-multilingual`** | Jina Reranker v2 | 8.192 ctx / Cross-Encoder | Cross-lingual search reranking |
| **`jina-colbert-v2`** | Jina ColBERT v2 | 8.192 ctx / Token-level | Multi-vector granular token retrieval |
| **`r.jina.ai`** | Jina Reader Engine | Web Scraper for LLM | Converts any web URL to pristine markdown |

### Step-by-Step Instructions:
1. Visit [https://cloud.jina.ai/](https://cloud.jina.ai/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export JINA_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.jina.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -d '{
    "model": "jina-embeddings-v3",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import requests

# Test Jina Reader (No key required!)
res = requests.get("https://r.jina.ai/https://github.com")
print(res.text[:300])

# Test Jina Embeddings
headers = {"Authorization": "Bearer YOUR_JINA_API_KEY", "Content-Type": "application/json"}
payload = {"model": "jina-embeddings-v3", "input": ["Hello Jina AI"]}
res_emb = requests.post("https://api.jina.ai/v1/embeddings", headers=headers, json=payload)
print("Dim:", len(res_emb.json()["data"][0]["embedding"]))
```

---

<a name="português"></a>
## 🇧🇷 Jina AI — Embeddings, Rerank & Reader API (10M Tokens Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://cloud.jina.ai/](https://cloud.jina.ai/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** 10 Milhões de tokens grátis + Reader API 100% perpétua e gratuita.
  * **Limites de Taxa:** 500 RPM with key / 20 RPM anonymous Reader.
  * **Endpoint Base:** `https://api.jina.ai/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`jina-embeddings-v3`** | Jina Embeddings v3 | 8.192 ctx / Matryoshka dims | 89 languages, adaptive dimension representation |
| **`jina-reranker-v2-base-multilingual`** | Jina Reranker v2 | 8.192 ctx / Cross-Encoder | Cross-lingual search reranking |
| **`jina-colbert-v2`** | Jina ColBERT v2 | 8.192 ctx / Token-level | Multi-vector granular token retrieval |
| **`r.jina.ai`** | Jina Reader Engine | Web Scraper for LLM | Converts any web URL to pristine markdown |

### Passo a Passo de Onboarding:
1. Acesse [https://cloud.jina.ai/](https://cloud.jina.ai/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export JINA_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.jina.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $JINA_API_KEY" \
  -d '{
    "model": "jina-embeddings-v3",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import requests

# Test Jina Reader (No key required!)
res = requests.get("https://r.jina.ai/https://github.com")
print(res.text[:300])

# Test Jina Embeddings
headers = {"Authorization": "Bearer YOUR_JINA_API_KEY", "Content-Type": "application/json"}
payload = {"model": "jina-embeddings-v3", "input": ["Hello Jina AI"]}
res_emb = requests.post("https://api.jina.ai/v1/embeddings", headers=headers, json=payload)
print("Dim:", len(res_emb.json()["data"][0]["embedding"]))
```
