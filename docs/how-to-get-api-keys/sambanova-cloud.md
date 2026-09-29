# ⚡ SambaNova Cloud — Extreme RDU Speed (Free Developer Tier)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 SambaNova Cloud Setup Guide

* **Official Portal:** [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/)
* **Credit Card Required?** 🟠 **YES** (Developer Tier requires an active payment method to run requests as of late September 2026).
* **Hardware:** Proprietary SN40L Reconfigurable Dataflow Units (RDUs) delivering sub-second frontier inference.
* **Developer Tier Quota:** 20 Million tokens per day cap across production and preview models once payment method is verified.
* **Base URL:** `https://api.sambanova.ai/v1` (OpenAI SDK Compatible)
* **Key Free Models:**
  * `Meta-Llama-3.3-70B-Instruct`
  * `DeepSeek-R1`
  * `DeepSeek-R1-Distill-Llama-70B`
  * `Qwen2.5-72B-Instruct`

### Step-by-Step Instructions:
1. Visit [https://cloud.sambanova.ai/](https://cloud.sambanova.ai/) and register a developer account.
2. Link a payment method to activate the Developer Tier.
3. Go to **APIs** in the left sidebar.
4. Click **Create API Key** and copy your token.

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
* **Exige Cartão de Crédito?** 🟠 **SIM** (A plataforma transicionou para o Developer Tier comercial em setembro de 2026, exigindo método de pagamento ativo).
* **Arquitetura:** Processadores RDU SN40L com taxas altíssimas de geração de tokens por segundo.
* **Cota do Developer Tier:** Limite de até 20 Milhões de tokens por dia.
* **Modelos Disponíveis:** Llama 3.3 70B, DeepSeek-R1, Qwen 2.5 72B.
