# Voyage AI — World-Leading Embeddings & Rerankers (200M Free Tokens)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Voyage AI — World-Leading Embeddings & Rerankers (200M Free Tokens) Setup Guide

* **Official Platform:** [https://dash.voyageai.com/](https://dash.voyageai.com/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** 200M tokens trial on signup + 50M permanent free quota.
  * **Rate Limits:** 300 RPM / 1.000.000 TPM.
  * **Base Endpoint:** `https://api.voyageai.com/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`voyage-3`** | Voyage-3 General | 32.000 ctx / 1024 dims | Top #1 MTEB retrieval performance |
| **`voyage-3-lite`** | Voyage-3-Lite | 32.000 ctx / 512 dims | High-speed cost-effective embeddings |
| **`voyage-code-3`** | Voyage Code 3 | 32.000 ctx / 1024 dims | Optimized for codebases and technical documentation |
| **`rerank-2`** | Voyage Rerank 2 | 16.000 ctx / Cross-Encoder | State-of-the-art precision for RAG chunk reranking |

### Step-by-Step Instructions:
1. Visit [https://dash.voyageai.com/](https://dash.voyageai.com/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export VOYAGE_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.voyageai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "model": "voyage-3",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import voyageai

vo = voyageai.Client(api_key="YOUR_VOYAGE_API_KEY")
embeddings = vo.embed(["RAG retrieval with Voyage AI"], model="voyage-3")
print("Vector length:", len(embeddings.embeddings[0]))
```

---

<a name="português"></a>
## 🇧🇷 Voyage AI — Embeddings & Rerankers Líderes Mundiais (200M Tokens Grátis) — Guia de Configuração

* **Link da Plataforma:** [https://dash.voyageai.com/](https://dash.voyageai.com/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** 200 Milhões de tokens trial + 50M permanentes sem cartão.
  * **Limites de Taxa:** 300 RPM / 1.000.000 TPM.
  * **Endpoint Base:** `https://api.voyageai.com/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`voyage-3`** | Voyage-3 General | 32.000 ctx / 1024 dims | Top #1 MTEB retrieval performance |
| **`voyage-3-lite`** | Voyage-3-Lite | 32.000 ctx / 512 dims | High-speed cost-effective embeddings |
| **`voyage-code-3`** | Voyage Code 3 | 32.000 ctx / 1024 dims | Optimized for codebases and technical documentation |
| **`rerank-2`** | Voyage Rerank 2 | 16.000 ctx / Cross-Encoder | State-of-the-art precision for RAG chunk reranking |

### Passo a Passo de Onboarding:
1. Acesse [https://dash.voyageai.com/](https://dash.voyageai.com/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export VOYAGE_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.voyageai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "model": "voyage-3",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import voyageai

vo = voyageai.Client(api_key="YOUR_VOYAGE_API_KEY")
embeddings = vo.embed(["RAG retrieval with Voyage AI"], model="voyage-3")
print("Vector length:", len(embeddings.embeddings[0]))
```
