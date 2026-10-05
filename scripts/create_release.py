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

body_content = """# 🚀 Awesome AI Free Tiers — Release v18.0.0 (Early October 2026 Live Audit)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Release Notes (English)

The **v18.0.0** release represents our benchmark live audit for early October 2026, delivering fresh validations, major model launches, multimodal expansions, and critical policy updates across 64 curated AI inference providers.

### 🌟 Key Highlights & Model Updates
* **Google Gemini 3.8 Live (General Availability):**
  * Official GA release of **Gemini 3.8 Live** and *Live Extended Thinking* via WebSocket real-time bidirectional streaming.
  * Commercial billing rates for **Gemini 3.8 Flash** locked into Google AI Studio console.
  * Free Tier quotas for Gemini 3.1 Flash & Flash-Lite remain active with dynamic per-project limits.
* **DeepSeek Architecture Expansion (DeepSeek-V4.1-Flash):**
  * Launch of **DeepSeek-V4.1-Flash** featuring native multimodal visual understanding.
  * Canonical routing consolidation: official support for `deepseek-flash`, `deepseek-chat` (V3), and `deepseek-reasoner` (R1).
  * 50% discount confirmed for Off-Peak usage (00:30–08:30 UTC+8).
* **NVIDIA NIM Catalog Expansion:**
  * Expanded to **90+ production & research AI models** for NVIDIA Developer Program members.
  * Free rate limits confirmed: 40 RPM / 1,000 RPD with zero credit card required.
* **Mistral AI (La Plateforme Clarification):**
  * Explicit boundary defined between the free developer experimentation tier and commercial production endpoints (Mistral Large 3 / Small 4).

### 🚨 Critical Security & Deprecation Notices (Preserved from v17 Audit)
* **Clarifai Encerrado (Service Retired):** Ceased standalone operations on July 17, 2026 following acquisition by **Nebius** (NASDAQ: NBIS). Endpoints (`api.clarifai.com`) shut down; technology migrated to Nebius Token Factory (`api.studio.nebius.ai`).
* **GitHub Models Deprecated:** Legacy `models.inference.ai.azure.com` playground officially retired by Microsoft/GitHub on July 30, 2026.
* **SambaNova Cloud Developer Tier:** Transitioned to Developer Tier requiring payment method / credit card registration (20M tokens/day cap once linked).
* **Baseten Serverless:** $30 compute credits require entering a credit card in the workspace settings.
* **Maritaca AI (MariTalk):** Official documented Tier 0 limits calibrated: 60 RPM, 128k input TPM, 10k output TPM, 4M chars/day Batch API, official BRL rates (Sabiá-4 R$ 5 in / R$ 20 out).
* **Exa.ai:** Confirmed recurring $10 USD/month grant (resets 1st of month) + $10 onboarding bonus.
* **Lemonfox.ai:** Confirmed 1-month free trial (10M credits) followed by $5/month budget tier (50M credits).

### 🛠️ Infrastructure & Repository Updates
* **Autonomous Windows Task Scheduler Integration:** Automated background runner (`scripts/scheduled_catalog_audit.py`) running every Mon/Wed/Fri at 17:00 BRT with automatic backup, health checks, and git sync.
* **Dataset Updated:** `data/providers.json` elevated to version `1.4.0` (`last_audit_date: 2026-10-05`).
* **Reference Catalog:** Full reference document updated to `docs/freetiers_apis_v18_reference.md`.

---

<a name="português"></a>
## 🇧🇷 Notas da Versão (Português)

A versão **v18.0.0** consolida a auditoria de início de outubro de 2026, trazendo novas validações de modelos, expansão multimodal e alinhamento estrito de políticas em 64 provedores de inferência de IA.

### 🌟 Principais Atualizações de Modelos
* **Google Gemini 3.8 Live (Disponibilidade Geral - GA):**
  * Lançamento oficial em GA do **Gemini 3.8 Live** com *Live Extended Thinking* via streaming bidirecional em WebSockets.
  * Preços comerciais do **Gemini 3.8 Flash** consolidados no console do Google AI Studio; Free Tier preservado dinamicamente para Gemini 3.1 Flash / Flash-Lite.
* **DeepSeek-V4.1-Flash (Multimodal Nativo):**
  * Lançamento do novo modelo com visão computacional e entendimento multimodal.
  * Roteamento canônico unificado: suporte a `deepseek-flash`, `deepseek-chat` (V3) e `deepseek-reasoner` (R1) com 50% de desconto no horário econômico Off-Peak (00:30–08:30 UTC+8).
* **NVIDIA NIM (Catálogo Ampliado de 90+ Modelos):**
  * Mais de 90 modelos de ponta gratuitos para membros do NVIDIA Developer Program com cota de 40 RPM / 1.000 RPD sem cartão de crédito.
* **Mistral AI (La Plateforme):**
  * Delimitação clara do nível de experimentação gratuito para prototipagem de desenvolvedores.

### 🚨 Alertas Críticos de Encerramento e Faturamento
* **Clarifai:** Encerrado e absorvido pela Nebius Token Factory em 17/07/2026.
* **GitHub Models:** Descontinuado oficialmente em 30/07/2026 pela Microsoft.
* **SambaNova Cloud:** Developer Tier passou a exigir método de pagamento (cartão) para emissão de chaves.
* **Baseten:** Créditos de $30 USD exigem cadastro de cartão no console.
* **Maritaca AI:** Métricas oficiais de Tier 0 (60 RPM, 128k input TPM, 10k output TPM, 4M caracteres/dia na Batch API).
* **Exa.ai:** Cota de $10 USD/mês confirmada como recorrente mensal + bônus de $10.
* **Lemonfox.ai:** Trial de 1 mês (10M créditos) + plano budget de $5/mês.

---
⭐ **Apoie o Projeto:** Se este repositório economiza dinheiro para você e sua equipe, deixe uma Star ⭐ no repositório!
"""

payload = {
    "tag_name": "v18.0.0",
    "target_commitish": "main",
    "name": "🚀 v18.0.0 — Early October 2026 Audit: Gemini 3.8 Live GA, DeepSeek-V4.1 Multimodal & NVIDIA NIM 90+ Models",
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
