# Replicate — Cloud ML Sandbox & Developer Trial Credits

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Replicate — Cloud ML Sandbox & Developer Trial Credits Setup Guide

* **Official Platform:** [https://replicate.com/](https://replicate.com/)
* **Credit Card Required?** ❌ NO / NÃO (for developer trial via GitHub OAuth)
* **Phone / SMS Verification?** ❌ NO / NÃO
* **Free Quota Highlights:**
  * **Free Allocation:** Developer trial runs for language, vision, and diffusion models.
  * **Rate Limits:** Dynamic sandbox queue (1-2 concurrent free runs).
  * **Base Endpoint:** `https://api.replicate.com/v1`
* **Canonical API Model IDs:**

| Canonical Model ID | Display Name | Context Window | Technical Capabilities |
| :--- | :--- | :---: | :--- |
| **`meta/meta-llama-3.3-70b-instruct`** | Llama 3.3 70B | 131.072 / 4.096 | Serverless streaming text generation |
| **`deepseek-ai/deepseek-r1`** | DeepSeek-R1 | 131.072 / 16.384 | Reasoning model with thinking traces |
| **`black-forest-labs/flux-schnell`** | FLUX.1 Schnell | 1 prompt / 1024x1024 | 4-step state-of-the-art diffusion |
| **`yorickvp/llava-13b`** | LLaVA 13B | 4.096 / 1.024 | Visual QA and image understanding |

### Step-by-Step Instructions:
1. Visit [https://replicate.com/](https://replicate.com/) and create your developer account.
2. Navigate to the **API Keys** or **Settings / Credentials** section in the console.
3. Generate a new API key and export it to your environment:
   ```bash
   export REPLICATE_API_TOKEN="your_api_key_here"
   ```
4. Test the connection with the 1-line cURL or Python script below.

### 1-Line Test Command (cURL):
```bash
curl https://api.replicate.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
  -d '{
    "model": "meta/meta-llama-3.3-70b-instruct",
    "messages": [{"role": "user", "content": "Hello runtime verification!"}]
  }'
```

### Python SDK Example:
```python
import replicate

output = replicate.run(
    "meta/meta-llama-3.3-70b-instruct",
    input={"prompt": "Write a haiku about artificial intelligence."}
)
print("".join(output))
```

---

<a name="português"></a>
## 🇧🇷 Replicate — Sandbox ML na Nuvem & Créditos de Desenvolvedor — Guia de Configuração

* **Link da Plataforma:** [https://replicate.com/](https://replicate.com/)
* **Exige Cartão de Crédito?** ❌ NO / NÃO (for developer trial via GitHub OAuth)
* **Exige Telefone / SMS?** ❌ NO / NÃO
* **Destaques da Cota Gratuita:**
  * **Concessão Free:** Predições de teste de desenvolvedor para LLMs, visão e difusão.
  * **Limites de Taxa:** Dynamic sandbox queue (1-2 concurrent free runs).
  * **Endpoint Base:** `https://api.replicate.com/v1`
* **Identificadores Canônicos de Modelo:**

| Modelo ID API | Nome | Janela de Contexto | Capacidades & Casos de Uso |
| :--- | :--- | :---: | :--- |
| **`meta/meta-llama-3.3-70b-instruct`** | Llama 3.3 70B | 131.072 / 4.096 | Serverless streaming text generation |
| **`deepseek-ai/deepseek-r1`** | DeepSeek-R1 | 131.072 / 16.384 | Reasoning model with thinking traces |
| **`black-forest-labs/flux-schnell`** | FLUX.1 Schnell | 1 prompt / 1024x1024 | 4-step state-of-the-art diffusion |
| **`yorickvp/llava-13b`** | LLaVA 13B | 4.096 / 1.024 | Visual QA and image understanding |

### Passo a Passo de Onboarding:
1. Acesse [https://replicate.com/](https://replicate.com/) e crie sua conta de desenvolvedor.
2. Navegue até o painel de **API Keys** ou **Credenciais**.
3. Crie sua chave de API e configure a variável de ambiente:
   ```bash
   export REPLICATE_API_TOKEN="sua_chave_aqui"
   ```
4. Execute o teste rápido de bancada com cURL ou Python.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.replicate.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
  -d '{
    "model": "meta/meta-llama-3.3-70b-instruct",
    "messages": [{"role": "user", "content": "Olá, validação em runtime v16!"}]
  }'
```

### Exemplo em Python:
```python
import replicate

output = replicate.run(
    "meta/meta-llama-3.3-70b-instruct",
    input={"prompt": "Write a haiku about artificial intelligence."}
)
print("".join(output))
```
