# 🤗 Hugging Face Serverless Inference API — Free Tier Setup Guide

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Hugging Face Serverless Inference Guide

* **Official Portal:** [https://huggingface.co/](https://huggingface.co/)
* **Credit Card Required?** ❌ **NO**
* **Free Quota:** Free serverless inference across thousands of open-source models with any standard free Hugging Face account. Rate limits typically range between **10 to 30 RPM**.
* **Base URL:** `https://api-inference.huggingface.co/v1/` (OpenAI compatible)
* **Popular Supported Free Models:**
  * `meta-llama/Llama-3.3-70B-Instruct`
  * `Qwen/Qwen2.5-72B-Instruct`
  * `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`
  * `BAAI/bge-large-en-v1.5` (Embeddings)
  * `openai/whisper-large-v3` (Speech-to-Text)

### Step-by-Step Instructions:
1. Create a free account at [https://huggingface.co/join](https://huggingface.co/join).
2. Go to **Settings ➔ Access Tokens** ([https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)).
3. Click **New token**, select **Read** permissions, and copy your token (`hf_...`).

### 1-Line Test Command (Terminal / cURL - OpenAI Compatible):
```bash
curl https://api-inference.huggingface.co/v1/chat/completions \
  -H "Authorization: Bearer YOUR_HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Hello Hugging Face!"}],
    "max_tokens": 128
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia Hugging Face Serverless Inference API

* **Link Oficial:** [https://huggingface.co/](https://huggingface.co/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Cota Gratuita:** Acesso serverless gratuito para milhares de modelos open-weights com uma conta comum do Hugging Face.
* **Compatibilidade com OpenAI SDK:** Endpoint padrão `https://api-inference.huggingface.co/v1/`.
