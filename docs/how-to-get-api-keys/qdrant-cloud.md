# Qdrant Cloud — Free Forever Managed Vector Database (1GB RAM)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Qdrant Cloud — Free Forever Managed Vector Database (1GB RAM) Setup Guide

* **Official Platform:** [https://cloud.qdrant.io/](https://cloud.qdrant.io/)
* **Credit Card Required?** ❌ NO / NÃO
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** 1 Free Managed Cloud Cluster (1GB RAM / 0.5 vCPU / ~1M vectors) forever.
  * **Rate Limits:** Hardware-bounded (~100 to 300 QPS, no artificial limits).
  * **Base Endpoint:** `https://<cluster-id>.<region>.gcp.cloud.qdrant.io:6333`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`qdrant-hnsw-dense`** | HNSW Dense Index | 128-4096 dimensions | Millisecond approximate nearest neighbor search |
| **`qdrant-sparse`** | Sparse Vectors Index | BM25 / SPLADE | Hybrid lexical + semantic search engine |
| **`qdrant-payload`** | Payload Filtering | JSON Metadata | Fast pre/post filtering by tenant, tags, or timestamps |

### Step-by-Step Instructions:
1. Visit [https://cloud.qdrant.io/](https://cloud.qdrant.io/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export QDRANT_API_KEY="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://<cluster-id>.<region>.gcp.cloud.qdrant.io:6333/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $QDRANT_API_KEY" \
  -d '{
    "model": "collections",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(
    url="https://YOUR_CLUSTER_ID.gcp.cloud.qdrant.io:6333",
    api_key="YOUR_QDRANT_API_KEY"
)

client.recreate_collection(
    collection_name="demo_docs",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE)
)
print("Collection created successfully!")
```

---

<a name="português"></a>
## 🇧🇷 Qdrant Cloud — Banco Vetorial Gerenciado Grátis Permanente (1GB RAM) — Guia de Configuração

* **Link da Plataforma:** [https://cloud.qdrant.io/](https://cloud.qdrant.io/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** 1 Cluster Gratuito Permanente na Nuvem (1GB RAM / ~1M de vetores) sem cartão.
  * **Limites de Taxa:** Hardware-bounded (~100 to 300 QPS, no artificial limits).
  * **Endpoint Base:** `https://<cluster-id>.<region>.gcp.cloud.qdrant.io:6333`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`qdrant-hnsw-dense`** | HNSW Dense Index | 128-4096 dimensions | Millisecond approximate nearest neighbor search |
| **`qdrant-sparse`** | Sparse Vectors Index | BM25 / SPLADE | Hybrid lexical + semantic search engine |
| **`qdrant-payload`** | Payload Filtering | JSON Metadata | Fast pre/post filtering by tenant, tags, or timestamps |

### Passo a Passo de Onboarding:
1. Acesse [https://cloud.qdrant.io/](https://cloud.qdrant.io/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export QDRANT_API_KEY="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://<cluster-id>.<region>.gcp.cloud.qdrant.io:6333/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $QDRANT_API_KEY" \
  -d '{
    "model": "collections",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(
    url="https://YOUR_CLUSTER_ID.gcp.cloud.qdrant.io:6333",
    api_key="YOUR_QDRANT_API_KEY"
)

client.recreate_collection(
    collection_name="demo_docs",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE)
)
print("Collection created successfully!")
```
