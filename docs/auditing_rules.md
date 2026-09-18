# 🛡️ The 6 Auditing Golden Rules / As 6 Regras de Ouro de Auditoria

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 The 6 Golden Rules of Verification

This repository is built on absolute technical truth. To protect developers from hidden paywalls, phantom quotas, and broken production code, every entry in this directory must strictly comply with the following 6 rules:

### 1. Runtime Verifiability (No Paper Specs)
Every claimed rate limit, model availability, and quota must be verified against an active, running API call or current official provider documentation. If a provider silently lowers quotas, our listings must reflect reality—not outdated marketing promises.

### 2. Canonical API Identifiers Only
Marketing names (`DeepSeek V3`, `Gemini 2.5 Flash`, `Llama 3.3 70B`) must always be mapped to their raw, exact JSON payload identifier (`deepseek-chat`, `gemini-2.5-flash`, `meta-llama/llama-3.3-70b-instruct`). Never list internal routing nicknames without specifying the canonical ID developers must send in SDK calls.

### 3. Granular Limit Transparency
Vague terms like "generous free tier" or "unlimited" are prohibited. Every model entry must explicitly document:
* **RPM**: Requests Per Minute
* **TPM**: Tokens Per Minute
* **RPD**: Requests Per Day
* **Concurrency**: Maximum simultaneous in-flight connections (when restricted)

### 4. Strict Billing Classification
Every provider must be categorized into one of four unambiguous tiers:
* 🟢 **Permanent Free Tier (No CC)**: Accessible forever with zero payment method or credit card required.
* 🟡 **Welcome Trial / Expiring Credits**: Generous free balance that expires after a fixed window (e.g., 30 to 180 days).
* 🟠 **Free Tier (Credit Card Required)**: Free recurring quota, but requires entering a credit card for anti-abuse identity verification.
* 🔵 **Micro-Budget ($5 ROI)**: Paid inference offering massive token volume (tens of millions of tokens per \$5 deposit).

### 5. Zero Commercial Bias & Zero Affiliate Links
We maintain 100% independence. Referral codes (`?ref=abc`), affiliate links, sponsored trackers, and unverified commercial proxies are strictly forbidden. All links must point directly to the official developer console of the provider.

### 6. Transparent Deprecation Tracking
When a model is sunset or deprecated, it is never silently deleted. It is cataloged in the Deprecation Archive with its sunset date, last known specs, and recommended drop-in replacement route so existing codebases do not break unexpectedly.

---

<a name="português"></a>
## 🇧🇷 As 6 Regras de Ouro de Auditoria

Este repositório foi construído sobre a verdade técnica absoluta. Para proteger desenvolvedores de cobranças surpresa, cotas fantasmas e códigos de produção quebrados, cada item listado segue rigorosamente estas 6 regras:

### 1. Verificabilidade em Runtime (Nada de Especulação)
Todo limite de taxa, disponibilidade de modelo e cota anunciada deve ser comprovado por teste ativo no terminal ou documentação oficial em vigência. Se o provedor reduziu limites ontem, a tabela deve refletir a realidade hoje—não promessas de marketing do passado.

### 2. Apenas Identificadores Canônicos de API
Nomes comerciais (`DeepSeek V3`, `Gemini 2.5 Flash`, `Llama 3.3 70B`) devem sempre ser associados ao identificador exato exigido no payload JSON (`deepseek-chat`, `gemini-2.5-flash`, `meta-llama/llama-3.3-70b-instruct`). Proibido usar apelidos internos de cluster sem explicitar o ID real de chamada.

### 3. Transparência Granular de Limites
Termos vagos como "cota generosa" ou "ilimitado" são proibidos. Cada modelo deve declarar:
* **RPM**: Requisições por Minuto
* **TPM**: Tokens por Minuto
* **RPD**: Requisições por Dia
* **Concorrência**: Número máximo de requisições simultâneas em trânsito

### 4. Classificação Rigorosa de Faturamento (Billing)
Todo provedor é enquadrado em uma das quatro categorias sem ambiguidade:
* 🟢 **Free Tier Permanente (Sem Cartão)**: Acesso perpétuo sem pedir dados de pagamento.
* 🟡 **Trial com Créditos de Boas-Vindas**: Saldo gratuito que expira em um prazo fixo (30 a 180 dias).
* 🟠 **Free Tier com Cartão Obrigatório**: Cota gratuita contínua, mas exige cartão para validação antifraude.
* 🔵 **Micro-Orçamento ($5 USD)**: Pago, mas com altíssimo rendimento (milhões de tokens por \$5).

### 5. Tolerância Zero a Links Afiliados e Interesses Comerciais
Independência técnica total. Links de indicação (`?ref=`), códigos de afiliados, redirecionadores ou proxies comerciais duvidosos são sumariamente rejeitados. Todos os links apontam diretamente para o console oficial do provedor.

### 6. Rastreamento Ativo de Depreciações
Modelos encerrados ou descontinuados nunca são deletados em silêncio. Eles são movidos para a seção de Histórico de Depreciação com a data de encerramento e a rota de substituição recomendada.
