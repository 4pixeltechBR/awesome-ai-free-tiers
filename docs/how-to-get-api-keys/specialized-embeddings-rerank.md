# 🎯 Specialized Free Embeddings & Reranking (Nomic & Mixedbread)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Free Embeddings & Reranking Setup

RAG (Retrieval-Augmented Generation) pipelines require dedicated embeddings and rerankers. These platforms offer specialized free tiers:

### 1. Nomic AI (Nomic Embed)
* **Official Portal:** [https://www.nomic.ai/](https://www.nomic.ai/)
* **Credit Card?** ❌ **NO**
* **Free Quota:** Free API tier for open-source vector embeddings without payment method.
* **Models:** `nomic-embed-text-v1.5` (8,192 context window, state-of-the-art embedding quality), `nomic-embed-vision-v1.5`.

```bash
curl https://api-inference.nomic.ai/v1/embedding/text \
  -H "Authorization: Bearer YOUR_NOMIC_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "nomic-embed-text-v1.5", "texts": ["Search query here"]}'
```

### 2. Mixedbread AI (Embeddings & Reranking)
* **Official Portal:** [https://www.mixedbread.ai/](https://www.mixedbread.ai/)
* **Credit Card?** ❌ **NO**
* **Free Quota:** Free monthly tier for embeddings and rerankers.
* **Models:** `mxbai-rerank-large-v1`, `mxbai-embed-large`.

```bash
curl https://api.mixedbread.ai/v1/reranking \
  -H "Authorization: Bearer YOUR_MIXEDBREAD_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mixedbread-ai/mxbai-rerank-large-v1",
    "query": "Deep learning architectures",
    "input": ["Document 1 text...", "Document 2 text..."]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia de Embeddings e Reranking Gratuitos (Nomic & Mixedbread)

Pipelines de RAG profissionais exigem modelos especializados de vetores e reordenação (rerank):

1. **Nomic AI**: `nomic-embed-text-v1.5` com janela de 8.192 tokens e cota gratuita sem cartão.
2. **Mixedbread AI**: O melhor modelo de rerank de código aberto (`mxbai-rerank-large-v1`) com plano gratuito para desenvolvedores.
