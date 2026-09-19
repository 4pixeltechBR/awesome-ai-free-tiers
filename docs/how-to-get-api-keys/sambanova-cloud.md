# ⚡ SambaNova Cloud — Extreme RDU Speed (Free Developer Tier)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 SambaNova Cloud Setup Guide

* **Official Portal:** [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/)
* **Credit Card Required for Free Tier?** ❌ **NO**
* **Hardware:** Proprietary SN40L Reconfigurable Dataflow Units (RDUs) delivering sub-second frontier inference.
* **Free Quota:** Free Developer Tier with per-day token caps and up to **30 RPM / 6,000 TPM**.
* **Base URL:** `https://api.sambanova.ai/v1` (OpenAI SDK Compatible)
* **Key Free Models:**
  * `Meta-Llama-3.3-70B-Instruct`
  * `DeepSeek-R1`
  * `DeepSeek-R1-Distill-Llama-70B`
  * `Qwen2.5-72B-Instruct`

### Step-by-Step Instructions:
1. Visit [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/) and register a free developer account.
2. Go to **APIs** in the left sidebar.
3. Click **Create API Key** and copy your token.

### 1-Line Test Command (Terminal / cURL):
```bash
curl https://api.sambanova.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_SAMBANOVA_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Meta-Llama-3.3-70B-Instruct",
    "messages": [{"role": "user", "content": "Write a 5-word poem."}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia SambaNova Cloud (RDUs de Altíssima Velocidade)

* **Link Oficial:** [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/)
* **Exige Cartão de Crédito?** ❌ **NÃO** para o plano de desenvolvedor gratuito.
* **Arquitetura:** Processadores RDU SN40L com taxas altíssimas de geração de tokens por segundo.
* **Modelos Disponíveis:** Llama 3.3 70B, DeepSeek-R1, Qwen 2.5 72B.
