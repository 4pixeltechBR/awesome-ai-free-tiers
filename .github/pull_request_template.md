## 📋 Pull Request Checklist / Lista de Verificação do PR

> ⚠️ **SECURITY WARNING / ALERTA DE SEGURANÇA:**
> **NEVER commit or paste real API keys or sensitive secrets.** Use placeholders like `YOUR_API_KEY` or `$API_KEY`.
> **NUNCA envie ou cole chaves de API reais ou senhas.** Utilize placeholders como `SUA_CHAVE_API` ou `$API_KEY`.

---

### Description / Descrição
<!-- Briefly describe what this PR adds, updates, or fixes. / Descreva resumidamente o que este PR adiciona, atualiza ou corrige. -->

### Type of Change / Tipo de Mudança
- [ ] 🆕 New Provider Free Tier / Novo Provedor com Free Tier
- [ ] 🔄 Quota / Rate Limit Update / Atualização de Cotas ou Limites
- [ ] ⚠️ Model Deprecation or Sunset / Depreciação ou Encerramento de Modelo
- [ ] 📖 Documentation / How-To Guide / Melhoria de Documentação ou Guia
- [ ] 🐛 Bug Fix or Broken Link / Correção de Link Quebrado ou Bug

---

### 🛡️ Auditing & Verification Compliance (Mandatory / Obrigatório)

Please confirm you have complied with our **6 Auditing Golden Rules** (`docs/auditing_rules.md`):

- [ ] **1. Runtime Verified:** I have tested the endpoint or verified current active documentation.
- [ ] **2. Canonical Model IDs:** Model IDs match the raw JSON payload identifier (e.g., `deepseek-chat`, `gemini-2.5-flash`), NOT internal cluster tags or marketing names.
- [ ] **3. Granular Limits:** Included RPM, TPM, and RPD where available.
- [ ] **4. Billing Classification:** Accurately classified as:
  - `Permanent Free Tier (No CC)`
  - `Welcome Trial / Expiring Credits`
  - `Free Tier (Credit Card Required)`
  - `Micro-Budget ($5 ROI)`
- [ ] **5. Zero Commercial Bias:** NO affiliate links (`?ref=`), NO tracking parameters, NO unverified proxy URLs. Links point directly to the official provider console.
- [ ] **6. HTTP 200 Proof:** I have pasted a reproducible curl test response below (with API key redacted).

```bash
# Paste your test curl command and redacted HTTP 200 response here:
curl -X POST https://api.provider.com/v1/chat/completions \
  -H "Authorization: Bearer $API_KEY" \
  ...
```
