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

### 7. Terms of Service & Privacy/LGPD Compliance (v19)
No route may be recommended for commercial production if the provider's terms explicitly prohibit production use (e.g. trial-only tiers), if the provider logs and trains models on customer data without enterprise guarantees, if the operator is unidentified/unverifiable, or if operating the route requires circumventing terms (such as multi-account pooling). Workloads involving personal or sensitive data must strictly satisfy applicable data privacy laws (LGPD / GDPR).

---

## 🏛️ Mandatory Repository Governance Directives (Rules of Engagement)

Every contributor, maintainer, and autonomous agent working on this repository must enforce the following 5 core operational directives:

1. **Mandatory GitHub Release on Every Update:**  
   Every time the catalog is updated, a formal GitHub Release (with semantic tag) must be published immediately. The release notes must explicitly list:
   - All newly added, launched, or discovered models.
   - All deprecated, disabled, or sunset models with recommended replacement routes.
2. **Active Promotion & Temporary Grant Tracking:**  
   Actively track and document limited-time promotional credits, developer grants, or free tiers. Explicitly list participating models, quota limits, and expiration deadlines. When a promotion ends, it must be explicitly announced in the subsequent release notes.
3. **Production-First Multimodal Expansion & The "Two Cheapest Plans" Rule:**  
   Continuously expand coverage to high-leverage providers that genuinely empower production workflows across text, code, image generation, video, music, audio, and visual effects. For hybrid or paid providers that offer free quotas or micro-budget plans (e.g., OpenCode, xKiro, B.AI), strictly document the **two cheapest plans available**, detailing their exact prices, token/generation limits, concurrency, and benefits. If a paid provider offers no free tier and no distinct micro-budget advantage, do not include it.
4. **Concrete, Auditable & Zero-Hallucination Truth:**  
   Every entry must be anchored in verifiable telemetry or official documentation. When in doubt or when official documentation is ambiguous, do not speculate—either hold back the addition or explicitly flag that parameters are volatile and subject to change.
5. **Global Benchmark Standard:**  
   Treat this repository as the definitive worldwide technical reference for AI free tiers and developer economics. Maintain enterprise-grade precision, zero affiliate spam, and actionable clarity to inspire trust from developers and API providers globally.

---

<a name="português"></a>
## 🇧🇷 As Regras de Auditoria & Governança do Repositório

Este repositório foi construído sobre a verdade técnica absoluta. Para proteger desenvolvedores de cobranças surpresa, cotas fantasmas e códigos de produção quebrados, cada item listado segue rigorosamente estas regras:

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

### 7. Conformidade de Termos de Serviço & Privacidade/LGPD (v19)
Nenhuma rota deve ser recomendada para produção comercial se os termos do provedor proibirem expressamente o uso em produção (ex.: tiers restritos a avaliação/trial), se o provedor registrar e treinar modelos em dados de usuários sem garantias corporativas, se o operador for anônimo/não identificável, ou se o uso exigir burlar termos contratuais (como empilhamento de contas para multiplicar cotas). Cargas com dados pessoais ou sensíveis devem atender rigorosamente à legislação de proteção de dados (LGPD / GDPR).

---

## 🏛️ Diretrizes Mandatórias de Governança (Regras Operacionais)

Qualquer mantenedor, contribuidor ou agente automatizado que atue neste projeto deve cumprir rigorosamente as seguintes 5 regras operacionais:

1. **Release Oficial Obrigatório a Cada Atualização:**  
   Sempre que o catálogo for atualizado, deve-se publicar uma nova Release oficial no GitHub (com tag semântica). As notas da release devem explicitar com clareza cristalina:
   - Todos os modelos novos lançados ou adicionados.
   - Todos os modelos deprecados, descontinuados ou removidos, com indicação de substituto.
2. **Rastreamento Ativo de Promoções e Concessões Temporárias:**  
   Pesquisar ativamente se algum provedor está com promoção ou créditos promocionais ativos (especificando modelos contemplados, limitações e prazos de validade). Assim que a promoção expirar, avisar obrigatoriamente na release seguinte.
3. **Expansão Multimodal Focada em Produção & Regra dos Dois Planos Mais Baratos:**  
   Expandir a cobertura continuamente para provedores que realmente agreguem valor em produção (texto, código, geração de imagens, música, vídeo, áudio e efeitos visuais). Para plataformas híbridas ou pagas com cotas acessíveis (ex.: OpenCode, xKiro, B.AI), documentar obrigatoriamente os **dois planos mais baratos de cada um**, seus limites de taxa, franquias e benefícios. Se uma plataforma paga não oferecer free tier e nem diferencial em micro-planos, não deve ser adicionada.
4. **Verdade Concreta e Auditável (Zero Suposição):**  
   Buscar sempre dados técnicos sólidos e verificáveis. Na menor dúvida, não avançar ou declarar de forma explícita na documentação que o dado é volátil e passível de alteração pela operadora.
5. **Padrão Ouro de Referência Global:**  
   O repositório é uma referência pública consultada por desenvolvedores, startups e provedores de nuvem. Toda informação deve primar por extrema precisão técnica, utilidade prática e transparência radical.
