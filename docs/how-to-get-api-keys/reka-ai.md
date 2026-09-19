# 🔮 Reka AI — $10/Month Recurring Free Credits & Multimodal Video

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Reka AI Setup Guide

* **Official Platform:** [https://platform.reka.ai/](https://platform.reka.ai/)
* **Credit Card Required?** ❌ **NO**
* **Phone / SMS Verification?** ❌ **NO**
* **Free Quota Highlights:**
  * **$10 USD / Month Recurring Free Credits:** Refreshes automatically every month in your developer account.
  * **Video Indexing Bonus:** Includes **3 hours of video analysis & indexing** free of charge on the multimodal API.
  * **Multimodal Frontier:** Native comprehension of text, high-res images, audio files, and full videos.
  * **SDK & OpenAI Compatible:** Supports both official Python SDK (`pip install reka-api`) and standard OpenAI-compatible endpoints (`https://api.reka.ai/v1`).
* **Canonical API Model IDs:**
  * **`reka-flash`**: Frontier multimodal model with lightning speed (128k context, 30 RPM).
  * **`reka-core`**: High-complexity reasoning model for deep analytical tasks (128k context, 10 RPM).
  * **`reka-edge`**: Compact model designed for resource-constrained, high-volume batch tasks (32k context, 60 RPM).

### Step-by-Step Instructions:
1. Navigate to [https://platform.reka.ai/](https://platform.reka.ai/) and register a developer account.
2. In the console, open the **API Keys** section.
3. Click **Create New Key** and save your API token securely.
4. Verify your monthly recurring credit balance under **Usage / Quotas**.

### 1-Line Test Command (cURL):
```bash
curl https://api.reka.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_REKA_API_KEY" \
  -d '{
    "model": "reka-flash",
    "messages": [{"role": "user", "content": "What are the advantages of multimodal AI models?"}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia de Configuração Reka AI

* **Link da Plataforma:** [https://platform.reka.ai/](https://platform.reka.ai/)
* **Exige Cartão de Crédito?** ❌ **NÃO**
* **Exige SMS / Telefone?** ❌ **NÃO**
* **Destaques da Cota Gratuita:**
  * **$10 USD / Mês em Créditos Recorrentes:** Renovados automaticamente todos os meses no console do desenvolvedor.
  * **Bônus Multimodal para Vídeo:** Inclui **3 horas de análise e indexação de vídeo** gratuitas na API multimodal.
  * **Compreensão Multimodal Nativa:** Processa texto, imagens em alta resolução, áudios e vídeos completos.
  * **Compatível com OpenAI e SDK Oficial:** Endpoint OpenAI `https://api.reka.ai/v1` ou biblioteca `reka-api`.
* **Identificadores Canônicos de Modelo:**
  * **`reka-flash`**: Modelo de fronteira multimodal ultrarrápido (128k contexto, 30 RPM).
  * **`reka-core`**: Modelo mais poderoso para raciocínio complexo e tarefas analíticas pesadas (128k contexto, 10 RPM).
  * **`reka-edge`**: Modelo eficiente e veloz para classificação e alto volume (32k contexto, 60 RPM).

### Passo a Passo:
1. Acesse [https://platform.reka.ai/](https://platform.reka.ai/) e crie sua conta de desenvolvedor.
2. No menu do console, vá até a seção **API Keys**.
3. Clique em **Create New Key** e copie seu token de acesso.
4. Verifique seus créditos mensais ativos na aba de **Usage**.

### Teste Rápido no Terminal (cURL):
```bash
curl https://api.reka.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUA_CHAVE_REKA" \
  -d '{
    "model": "reka-flash",
    "messages": [{"role": "user", "content": "Olá, teste multimodal!"}]
  }'
```
