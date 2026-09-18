# 🟠 Groq Cloud (Ultra-Fast LPUs) — How to Get Your Free API Key

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Groq Cloud Setup Guide

* **Official Console:** [https://console.groq.com/](https://console.groq.com/)
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ❌ **NO** (Email / GitHub / Google SSO)
* **Free Quota Highlights:**
  * **13 Active Models** running on Groq's custom LPU hardware (sub-second latency, up to 700+ tokens/sec).
  * `qwen/qwen3.8-27b`: 30 RPM / 6,000 TPM / 1,000 RPD
  * `openai/gpt-oss-120b`: 30 RPM / 8,000 TPM / 1,000 RPD
  * `meta-llama/llama-3.3-70b-versatile` / `llama-3.1-8b-instant`: 30 RPM / 14,400 RPD
  * `whisper-large-v3`: Audio transcription free tier (2,000 audio seconds/hour)

### Step-by-Step Instructions:
1. Visit [https://console.groq.com/](https://console.groq.com/) and create a free account.
2. Navigate to **"API Keys"** in the left sidebar ([https://console.groq.com/keys](https://console.groq.com/keys)).
3. Click **"Create API Key"**, give it a name (e.g. `My-Free-Agent`), and copy the key (`gsk_...`).

### 1-Line Test Command (Terminal / cURL):
```bash
curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
  -H "Authorization: Bearer YOUR_GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen/qwen3.8-27b",
    "messages": [{"role": "user", "content": "Write a 3-word slogan."}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Como Obter sua Chave Gratuita no Groq Cloud

* **Link Oficial do Console:** [https://console.groq.com/](https://console.groq.com/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS ou Telefone?** ❌ **NÃO** (Login com Google, GitHub ou Email)
* **Destaques da Cota Gratuita:**
  * **13 Modelos Ativos** rodando na arquitetura de LPUs proprietárias da Groq (velocidades de 400 a 750+ tokens por segundo).
  * `qwen/qwen3.8-27b`: 30 RPM / 6.000 TPM / 1.000 RPD
  * `openai/gpt-oss-120b`: 30 RPM / 8.000 TPM / 1.000 RPD
  * `whisper-large-v3`: Transcrição de áudio ultrarrápida (2.000 segundos de áudio por hora grátis)

### Passo a Passo:
1. Acesse [https://console.groq.com/](https://console.groq.com/) e crie uma conta gratuita.
2. No menu lateral esquerdo, vá em **"API Keys"**.
3. Clique no botão **"Create API Key"**, defina um nome e copie a chave gerada (`gsk_...`).

### Teste Rápido no Terminal:
```bash
curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
  -H "Authorization: Bearer SUA_CHAVE_GROQ" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen/qwen3.8-27b",
    "messages": [{"role": "user", "content": "Escreva um lema de 3 palavras."}]
  }'
```
