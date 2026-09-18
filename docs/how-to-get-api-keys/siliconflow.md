# 🚀 SiliconFlow — 20 Million Free Tokens & Open Weights Gateway

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 SiliconFlow Setup Guide

* **Official Portal:** [https://cloud.siliconflow.cn/](https://cloud.siliconflow.cn/) (Global: [https://siliconflow.com/](https://siliconflow.com/))
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ✅ **YES** (Mobile phone verification required)
* **Free Quota Highlights:**
  * **20,000,000 Free Tokens (20M tokens)** bonus upon account registration.
  * Completely free permanent inference on selected models: `Qwen/Qwen2.5-7B-Instruct`, `internlm/internlm2_5-7b-chat`, `THUDM/glm-4-9b-chat`.
  * High throughput: Up to 1,000 RPM on dedicated tiers.

### Step-by-Step Instructions:
1. Visit [https://cloud.siliconflow.cn/](https://cloud.siliconflow.cn/) and register.
2. Verify your mobile number to unlock your 20M tokens credit.
3. Navigate to **API Keys** and generate a new token (`sk-...`).

### 1-Line Test Command (Terminal / cURL):
```bash
curl -X POST "https://api.siliconflow.cn/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_SILICONFLOW_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen2.5-7B-Instruct",
    "messages": [{"role": "user", "content": "Hello SiliconFlow!"}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Como Obter sua Chave Gratuita na SiliconFlow

* **Link Oficial:** [https://cloud.siliconflow.cn/](https://cloud.siliconflow.cn/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS ou Telefone?** ✅ **SIM**
* **Destaques:** **20 Milhões de tokens grátis** no cadastro + modelos open-source de 7B a 9B com inferência 100% gratuita permanente.
