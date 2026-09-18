# 🟢 NVIDIA NIM (NVIDIA Inference Microservices) — 82 Free Models

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 NVIDIA NIM Setup Guide

* **Official Catalog:** [https://build.nvidia.com/explore/discover](https://build.nvidia.com/explore/discover)
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ❌ **NO** (Email / NVIDIA Account)
* **Free Quota Highlights:**
  * **82 Active Open-Source & Frontier Models** hosted on NVIDIA's high-performance GPU clusters.
  * Universal rate limits across models: **40 RPM / 1,000 RPD** per free developer account.
  * Popular models: `meta/llama-3.3-70b-instruct`, `mistralai/mistral-large-2-instruct`, `deepseek-ai/deepseek-r1`, `z-ai/glm-5.3`, `moonshotai/kimi-k3`, `nvidia/nemotron-4-340b-instruct`.

### Step-by-Step Instructions:
1. Visit [https://build.nvidia.com/](https://build.nvidia.com/) and click **"Sign In"** (or create a free NVIDIA Developer account).
2. Choose any model from the catalog (e.g. `meta/llama-3.3-70b-instruct`).
3. Click the **"Get API Key"** green button on the model's page.
4. Copy your API Key (`nvapi-...`).

### 1-Line Test Command (Terminal / cURL):
```bash
curl -X POST "https://integrate.api.nvidia.com/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_NVIDIA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta/llama-3.3-70b-instruct",
    "messages": [{"role": "user", "content": "Hello NVIDIA!"}],
    "temperature": 0.5,
    "max_tokens": 128
  }'
```

---

<a name="português"></a>
## 🇧🇷 Como Obter sua Chave Gratuita no NVIDIA NIM

* **Link Oficial do Catálogo:** [https://build.nvidia.com/explore/discover](https://build.nvidia.com/explore/discover)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS ou Telefone?** ❌ **NÃO**
* **Destaques da Cota Gratuita:**
  * **82 Modelos de Ponta Ativos** rodando na infraestrutura oficial de GPUs da NVIDIA.
  * Limite universal de **40 requisições/minuto (RPM) e 1.000 requisições/dia (RPD)** por conta de desenvolvedor gratuita.
  * Inclui Llama 3.3 70B, DeepSeek-R1, Mistral Large 2, GLM-5.3, Kimi K3 e Nemotron.

### Passo a Passo:
1. Acesse [https://build.nvidia.com/](https://build.nvidia.com/) e faça login com sua conta NVIDIA Developer (gratuita).
2. Clique em qualquer modelo do catálogo (ex.: `meta/llama-3.3-70b-instruct`).
3. Clique no botão verde **"Get API Key"**.
4. Copie sua chave de API gerada (`nvapi-...`).

### Teste Rápido no Terminal:
```bash
curl -X POST "https://integrate.api.nvidia.com/v1/chat/completions" \
  -H "Authorization: Bearer SUA_CHAVE_NVIDIA" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta/llama-3.3-70b-instruct",
    "messages": [{"role": "user", "content": "Ola NVIDIA!"}],
    "max_tokens": 128
  }'
```
