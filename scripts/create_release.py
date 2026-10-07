import os
import sys
import json
import urllib.request

def get_github_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    key_file = r"D:\Chaves APIs.txt"
    if os.path.exists(key_file):
        with open(key_file, "r", encoding="utf-8") as f:
            for line in f:
                if "ghp_" in line:
                    for part in line.replace(":", " ").replace("=", " ").split():
                        if part.startswith("ghp_"):
                            return part.strip()
    return None

token = get_github_token()
url = "https://api.github.com/repos/4pixeltechBR/awesome-ai-free-tiers/releases"

body_content = """# ⚖️ Awesome AI Free Tiers — Release v19.0.0 (October 2026 Fact-Check & Legal/LGPD Governance Audit)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Release Notes (English)

The **v19.0.0** release marks a major paradigm shift for the directory: an exhaustive, sober **fact-check audit against primary official documentation, platform terms of service, and privacy policies** conducted on October 7, 2026. 

This release moves the catalog beyond a mere "free tier hack list" into an **enterprise-grade architectural reference with legal and data privacy (LGPD) compliance**.

### 🔍 Major Corrections & Findings

1. **DeepSeek Official Realignment:**
   * **Canonical API Identifier:** The recommended model is officially **`deepseek-flash`** (DeepSeek-V4.1-Flash). The legacy `deepseek-v4-flash` remains accepted. Prior assertions that only `deepseek-chat`/`reasoner` were valid have been corrected.
   * **Corrected Peak Hours:** Peak pricing applies **01:00–04:00 and 06:00–10:00 UTC on business days** (= **22:00–01:00 and 03:00–07:00 BRT**). Weekends are 100% Off-Peak.
   * **Pricing per 1M Tokens:** Peak: $0.30 input ($0.006 cache hit) / $1.20 output. Off-Peak (50% OFF): $0.15 input ($0.003 cache hit) / $0.60 output.
   * **Promotional Grant:** The unadvertised "5M tokens / 30 days" bonus has been removed. Thinking mode is enabled by default (consumes output tokens; disable via `extra_body`). Data is stored in China.

2. **Google Gemini & AI Studio (Terms, Privacy & Under-18 Restriction):**
   * **Model Deprecations:** Gemini 2.0 Flash and Flash-Lite were permanently shut down on June 1, 2026. Gemini 1.5 family is fully deprecated. Gemini 2.5 Pro remains active.
   * **Grounding Quotas:** Free Tier Search Grounding exists only on Gemini 2.5 Flash/Lite. The Gemini 3.x series has **no Search Grounding in the Free Tier**.
   * **Critical Terms Alert:** Free Tier logs are reviewed by humans for model improvement. Furthermore, Gemini API terms **strictly prohibit use in services directed towards or likely to be accessed by individuals under 18 years of age** (applies to both Free and Paid tiers).

3. **NVIDIA NIM (Production Prohibition):**
   * Developer API access is governed by the *NVIDIA API Trial Terms*, which **strictly prohibit commercial production use**. Documented rate limits (40 RPM / 1,000 RPD) are exclusively for evaluation and prototyping.

4. **Groq Cloud Realignment:**
   * `llama-3.3-70b-versatile` and `llama-3.1-8b-instant` have been transitioned to Enterprise tier ("Contact Sales").
   * `qwen/qwen3.6-27b` officially retired and replaced by `qwen/qwen3.8-27b`.
   * Rate limits are enforced strictly per organization (key rotation under the same org provides zero multiplier).

5. **Maritaca AI (Brazilian Sovereign Champion):**
   * Clarified that there is no perpetual free API tier; access starts with a one-time R$ 20 onboarding credit.
   * Night tariff discount (-30%) and Batch API discount (-50%).
   * `sabia-4-br-sp` variant offers 100% Brazilian data residency and Data Processing Agreements (DPA) compliant with LGPD.

6. **Inception Labs (Mercury API):**
   * The 100M token grant is a **one-time onboarding credit** per account, not a recurring monthly pool. Active models: `mercury-2` and `mercury-2.5`.

7. **New Additions & Budget Providers:**
   * **Xiaomi MiMo Added:** Pay-as-you-go at $0.14 input / $0.28 output per 1M tokens (`mimo-v2.6-flash`), plus coding assistant token plans (MiMo Token Plan Lite at $6/mo).
   * **Coding Token Plans Detailed:** Structured comparison of OpenCode Go ($10/mo), Alibaba Token Plan ($6/mo), and Z.ai GLM Coding Plan.

### 🏛️ Architecture & Governance Restructuring

* **Workload-Segmented Strategy (Section 4):** Replaces legacy fallback chains with a workload-specific routing matrix:
  * **(a) Personal / Sensitive Data:** Strict LGPD compliance routes with DPA and Zero Data Retention (Maritaca `-br-sp` or Groq Paid ZDR; Gemini disqualified due to under-18 clause).
  * **(b) Non-Personal Data:** Legitimate Free Tiers (Google Flash-Lite, Groq gpt-oss-120b, Cloudflare Workers AI).
  * **(c) Coding Agents:** Codex, OpenCode Go, MiMo Token Plan.
* **New Section 5 (Terms & LGPD Compliance):** Enforcing rules against multi-account quota stacking, API reselling, and age gating.
* **Appendix A (Archived / Non-Recommended):** Safely archiving legacy fallback chains, anonymous gateways, and domestic Chinese platforms without loss of audit history.

---

<a name="português"></a>
## 🇧🇷 Notas da Versão (Português)

A versão **v19.0.0** representa uma evolução de maturidade indispensável: uma **revisão de fatos e auditoria jurídica/LGPD completa**, confrontando diretamente as documentações oficiais, termos de serviço e políticas de privacidade vigentes em 07/10/2026.

### 🔍 Principais Correções e Fatos Auditados

1. **Alinhamento Oficial DeepSeek:**
   * **Identificador Recomendado:** O ID oficial atual é **`deepseek-flash`** (DeepSeek-V4.1-Flash); o `deepseek-v4-flash` é legado aceito. A tese anterior de "rotas internas" foi revogada.
   * **Horário de Pico:** Corrigido para **01:00–04:00 e 06:00–10:00 UTC em dias úteis** (= **22:00–01:00 e 03:00–07:00 BRT**). Fins de semana são 100% fora de pico (50% de desconto).
   * **Preços por 1M:** Pico: $0.30 entrada ($0.006 cache hit) / $1.20 saída. Fora de pico: $0.15 entrada ($0.003 cache hit) / $0.60 saída.
   * **Bônus:** Removido o bônus não comprovado de 5M tokens. Thinking vem ligado por padrão; dados armazenados na China.

2. **Google Gemini & AI Studio (Termos, Menores de 18 Anos & Grounding):**
   * **Deprecações Confirmadas:** Família Gemini 2.0 Flash/Lite desligada em 01/06/2026; linha 1.5 fora do catálogo; 2.5 Pro segue ativo.
   * **Grounding:** Série 3.x não possui Grounding no Free Tier (apenas na linha 2.5).
   * **Cláusula Crítica de Idade:** Termos do Google **proíbem expressamente o uso da API (Free e Paga) em serviços direcionados ou acessados por menores de 18 anos**. Inviabiliza Gemini para sistemas escolares/alunos menores de idade.
   * **Privacidade:** Logs do Free Tier são revisados por humanos para treinamento de modelos.

3. **NVIDIA NIM (Proibição de Produção Comercial):**
   * O acesso gratuito de desenvolvedor é governado pelos *NVIDIA API Trial Terms*, que **proíbem expressamente uso em produção comercial**. Cotas de 40 RPM / 1.000 RPD são exclusivas para prototipagem e avaliação.

4. **Groq Cloud:**
   * Modelos `llama-3.3-70b-versatile` e `llama-3.1-8b-instant` migrados para Enterprise ("Contact Sales").
   * `qwen/qwen3.6-27b` descontinuado em favor de `qwen/qwen3.8-27b`. Limites valem por organização.

5. **Maritaca AI (LGPD & Soberania Nacional):**
   * Sem Free Tier perpétuo na API; concessão única de R$ 20 no cadastro.
   * Desconto noturno (-30%) e batch (-50%). Variante `sabia-4-br-sp` oferece 100% de residência de dados no Brasil e DPA formal da LGPD.

6. **Xiaomi MiMo & Planos de Coding Adicionados:**
   * Xiaomi MiMo pay-as-you-go a $0.14 entrada / $0.28 saída por 1M de tokens (`mimo-v2.6-flash`), além dos planos de assinatura de tokens para coding (MiMo Token Plan Lite a $6/mês).

### 🏛️ Reestruturação Arquitetural e Governança

* **Estratégia Segmentada por Carga de Trabalho (Seção 4):**
  * **Cargas com dados pessoais (escola/alunos):** Maritaca `-br-sp` ou Groq pago com ZDR (Zero Data Retention); eliminação de Gemini por cláusula de menores de idade e de free tiers que treinam com dados.
  * **Cargas sem dados pessoais (conteúdo viral, análises públicas):** Free tiers legítimos (Google Flash-Lite, Groq gpt-oss-120b, Cloudflare Workers AI).
  * **Agentes de código:** Codex, OpenCode Go, MiMo Token Plan.
* **Nova Seção 5 (Termos de Uso & LGPD):** Proibição de empilhamento de contas/chaves para somar free tiers, proibição de revenda e diretrizes da LGPD (Art. 11, 14 e 33 da Res. CD/ANPD nº 19/2024).
* **Apêndice A:** Gateways anônimos e plataformas domésticas arquivadas com integridade histórica.

---
⭐ **Apoie o Projeto:** Se este repositório economiza dinheiro para você e sua equipe, deixe uma Star ⭐ no repositório!
"""

payload = {
    "tag_name": "v19.0.0",
    "target_commitish": "main",
    "name": "⚖️ v19.0.0 — Fact-Check Audit, Legal/LGPD Governance & Workload-Segmented Architecture",
    "body": body_content,
    "draft": False,
    "prerelease": False
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "AwesomeAI-ReleaseAgent"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        url_created = res.get("html_url")
        print(f"RELEASE CREATED SUCCESSFULLY: {url_created}")
except Exception as e:
    print(f"ERROR: {e}")
    if hasattr(e, "read"):
        print(e.read().decode("utf-8"))
