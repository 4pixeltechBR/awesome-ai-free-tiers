import os
import sys
import json
import urllib.request
import ssl

def get_github_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    key_file = r"D:\Chaves APIs.txt"
    if os.path.exists(key_file):
        with open(key_file, "r", encoding="utf-8") as f:
            for line in f:
                if "Antigravity" in line and "ghp_" in line:
                    for part in line.replace(":", " ").replace("=", " ").split():
                        if part.startswith("ghp_"):
                            return part.strip()
            # fallback to any valid token in file
            f.seek(0)
            for line in f:
                if "ghp_" in line:
                    for part in line.replace(":", " ").replace("=", " ").split():
                        if part.startswith("ghp_"):
                            return part.strip()
    return None

token = get_github_token()
url = "https://api.github.com/repos/4pixeltechBR/awesome-ai-free-tiers/releases"

body_content = """# 🚀 Awesome AI Free Tiers — Release v21.0.0 (Sovereign Keyless Gateways, Production Quirks & Gemma 4)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Release Notes (English)

The **v21.0.0** release incorporates exhaustive live-runtime auditing from the Trinity Nexus × OmniRoute Super-Hub audit, expanding the catalog to **74 verified providers** with sovereign European GDPR infrastructure, anonymous developer gateways, Gemma 4 models, and battle-tested mitigations for 6 production routing quirks.

### 🌟 Key Highlights & Model Updates

1. **OVHcloud AI Endpoints (`kepler.ai.cloud.ovh.net`) — Sovereign European Tier-0:**
   * Direct OpenAI-compatible endpoint offering **keyless anonymous access** (2 RPM/IP) or **~400 RPM** with a free developer key generated instantly in the OVHcloud Manager (zero credit card required).
   * **100% Hosted in France (EU/GDPR compliant):** Contractual guarantee of zero prompt retention and zero training on customer data. Completely insulated from the US CLOUD Act.
   * **21 Active Models Audited:** Includes `gpt-oss-120b`, `Qwen3.5-397B-A17B`, `Mistral-Small-3.2-24B`, `DeepSeek-R1-Distill-Llama-70B`, `whisper-large-v3-turbo` (hardware-accelerated STT), and `bge-m3` (dense/sparse multilingual embeddings).

2. **Kilo Code Gateway (`api.kilo.ai/api/gateway`) — Anonymous Coding Gateway:**
   * Keyless developer gateway authenticated via fixed header `Authorization: Bearer anonymous`.
   * Rate quota: **~200 requests/hour per IP**.
   * 21 models optimized for developer workflows (`kilo/auto`, Qwen 2.5 Coder 32B/7B, DeepSeek Coder V2.5).
   * *Privacy Guardrail:* Traffic routed through distributed partner nodes; strictly reserved for open-source and non-sensitive workloads.

3. **Aion Labs (`api.aionlabs.ai/v1`) — Creative Writing & Roleplay Free Tier:**
   * **15 RPM / 20k TPD** perpetual free quota without credit card.
   * Fine-tuned models tailored for multi-turn roleplay, rich character dialogue, and literature without artificial refusal loops.

4. **Gemma 4 Generation & Gemini 3.6 Flash:**
   * Added official support for Google's newest open-weight generation: `google/gemma-4-31b-it:free` and `google/gemma-4-26b-a4b-it:free` on OpenRouter, alongside Gemini 3.6 Flash.
   * Verified 17 operational `:free` models on OpenRouter (including `nvidia/nemotron-3-ultra-550b-a55b:free`, `cohere/north-mini-code:free`, and `google/lyria-3-pro-preview`).

5. **The 6 Production Routing Quirks (Forensic Router Safeguards):**
   * Cataloged concrete production bugs in multi-provider routers (`cascade.py`):
     * *QUIRK 1 (OpenCode session header):* Enforce `X-Session-ID` to avoid HTTP 400.
     * *QUIRK 2 (GitHub Models fake 200 trap):* Intercept text/plain `"OK"` responses on retired endpoints before calling `response.json()`.
     * *QUIRK 3 (Pollinations in-band 402/rate-limit notice):* Sniff first 100 characters of assistant content for in-band rate limit strings.
     * *QUIRK 4 (Groq 413 token count parser):* Extract exact token counts from error payload to auto-rescale requests.
     * *QUIRK 5 (Moonshot partial prefill host-gate):* Enforce `partial=True` when assistant message is sent last.
     * *QUIRK 6 (Open-weight inline tool-call rescue):* Regex extraction of `<tool_call>...</tool_call>` inside text blocks to construct compliant OpenAI tool call objects.

6. **New Welcome Trials & Status Updates:**
   * Added new verified trial credits: **Nscale** ($5 USD), **Upstage Solar** ($10 USD), **AI21 Studio** ($10 USD / 3 months), **Inference.net** ($5 USD via SMS), and **NLP Cloud** ($15 USD).
   * **Ollama Cloud Status Clarification:** Confirmed the old cloud beta free tier is sunset. Cloud now runs on Pay-As-You-Go ($0.05/M) and Pro ($20/mo) / Max ($100/mo) plans. 100% free usage remains available via local hardware execution (`localhost`).
   * **Exclusions:** Confirmed `glhf.chat` shutdown (rebranded to `synthetic.new`, paid only); `Chutes.ai` paid only; `Gonka Broker` requires GNK crypto utility tokens.

---

<a name="português"></a>
## 🇧🇷 Notas da Versão (Português)

A versão **v21.0.0** consolida a auditoria completa da Trinity Nexus × OmniRoute Super-Hub, expandindo o catálogo para **74 provedores verificados** com infraestrutura soberana europeia GDPR sem chave, gateways anônimos para desenvolvedores, modelos Gemma 4 e salvaguardas robustas para 6 quirks de roteamento em produção.

### 🌟 Principais Destaques e Modelos Adicionados

1. **OVHcloud AI Endpoints (`kepler.ai.cloud.ovh.net`) — Soberania Europeia Tier-0:**
   * Endpoint compatível com OpenAI oferecendo **acesso anônimo sem chave** (2 RPM/IP) ou **~400 RPM** com chave gratuita de desenvolvedor emitida instantaneamente no OVHcloud Manager (zero cartão de crédito).
   * **100% Hospedado na França (Conformidade GDPR/RGPD):** Garantia contratual de zero retenção e zero treinamento de IA com os dados de inferência. Imune ao CLOUD Act norte-americano.
   * **21 Modelos Auditados em Produção:** `gpt-oss-120b`, `Qwen3.5-397B-A17B`, `Mistral-Small-3.2-24B`, `DeepSeek-R1-Distill-Llama-70B`, `whisper-large-v3-turbo` (STT acelerado) e `bge-m3` (embeddings densos e esparsos).

2. **Kilo Code Gateway (`api.kilo.ai/api/gateway`) — Hub Anônimo para Programação:**
   * Acesso keyless direto com cabeçalho `Authorization: Bearer anonymous`.
   * Cota: **~200 requisições/hora por IP**.
   * 21 modelos com ênfase em auxílio ao código (`kilo/auto`, Qwen 2.5 Coder 32B/7B, DeepSeek Coder V2.5).
   * *Salvaguarda de Privacidade:* Tráfego processado em nós parceiros; restrito a código aberto e cargas sem dados sensíveis.

3. **Aion Labs (`api.aionlabs.ai/v1`) — Escrita Criativa & Roleplay Gratuito:**
   * Cota permanente de **15 RPM / 20.000 TPD** sem exigência de cartão de crédito.
   * Modelos abertos finetunados para diálogos complexos, RPG e literatura sem recusas artificiais.

4. **Geração Gemma 4 & Gemini 3.6 Flash:**
   * Inclusão dos modelos `google/gemma-4-31b-it:free` e `google/gemma-4-26b-a4b-it:free` no OpenRouter, além do Gemini 3.6 Flash no Google AI Studio.
   * Catálogo ativo de 17 modelos gratuitos `:free` operacionais no OpenRouter (incluindo Nemotron 3 Ultra 550B, Cohere North Mini Code e Lyria 3 preview).

5. **Os 6 Quirks de Roteamento em Produção (Mitigação Forense):**
   * Documentação de salvaguardas para o `cascade.py` e bibliotecas de resiliência:
     * *QUIRK 1 (OpenCode session header):* Injeção de `X-Session-ID` persistente para evitar erro 400.
     * *QUIRK 2 (GitHub Models fake 200 trap):* Interceptação de respostas `text/plain` `"OK"` para evitar falha no `response.json()`.
     * *QUIRK 3 (Pollinations in-band notice):* Varredura do início do texto para detecção de avisos embutidos de rate limit.
     * *QUIRK 4 (Groq 413 token parser):* Extração do cálculo exato de tokens da mensagem 413 para redimensionar requisições.
     * *QUIRK 5 (Moonshot prefill):* Parâmetro `partial=True` quando a última mensagem for do assistente.
     * *QUIRK 6 (Rescue regex de tool calling):* Conversão automática de blocos literais `<tool_call>...</tool_call>` em objetos nativos de tool calls da OpenAI.

6. **Novos Créditos de Boas-Vindas & Status de Billing:**
   * Novos provedores com créditos iniciais auditados: **Nscale** ($5 USD), **Upstage Solar** ($10 USD), **AI21 Studio** ($10 USD / 3 meses), **Inference.net** ($5 USD via SMS) e **NLP Cloud** ($15 USD).
   * **Clarificação do Ollama Cloud:** O antigo free tier em nuvem foi encerrado. A nuvem opera em Pay-As-You-Go ($0.05/M) e planos Pro ($20/mês) / Max ($100/mês). Uso 100% gratuito é mantido via hardware local (`localhost`).
   * **Descontinuações Confirmadas:** `glhf.chat` encerrado (rebatizado para `synthetic.new`, pago); `Chutes.ai` pago; `Gonka Broker` requer tokens de cripto GNK.

---

⭐ **Apoie o Projeto:** Se este repositório economiza dinheiro para você e sua equipe, deixe uma Star ⭐ no repositório!
"""

payload = {
    "tag_name": "v21.0.0",
    "target_commitish": "main",
    "name": "🚀 v21.0.0 — Sovereign Keyless Gateways: OVHcloud AI GDPR Tier, Kilo Code, Aion Labs, Gemma 4 & Production Quirks",
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

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        url_created = res.get("html_url")
        print(f"RELEASE CREATED SUCCESSFULLY: {url_created}")
except Exception as e:
    print(f"ERROR: {e}")
    if hasattr(e, "read"):
        print(e.read().decode("utf-8"))
