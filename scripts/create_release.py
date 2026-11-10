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

body_content = """# 🎙️ Awesome AI Free Tiers — Release v20.0.0 (November 2026 Multimodal Media & Neural Audio Audit)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Release Notes (English)

The **v20.0.0** release delivers a major expansion into creative multimodal media (voice synthesis, speech-to-text, generative video, and graphic design), while consolidating dynamic meta-routing and global domain infrastructures across **66 verified providers**.

### 🌟 Key Highlights & Model Updates

1. **Fish Audio (`fish.audio`) Added (Permanent Free Developer API):**
   * Integration of state-of-the-art neural Text-to-Speech (TTS) and zero-shot voice cloning.
   * Model **`s2.1-pro-free`** is permanently available via API at **$0.00 / 1M UTF-8 bytes** (zero consumption fee) with up to **5 concurrent connections** without requiring a credit card.
   * Web Studio provides 8,000 monthly credits (~7 minutes of audio) renewed every month.

2. **Groq Cloud (Speech Synthesis & Canopy Labs Audio):**
   * Real-time Text-to-Speech models **`canopy-labs/orpheus-v1-en`** and **`canopy-labs/orpheus-arabic-saudi`** integrated directly onto Groq's ultra-low latency LPU hardware.
   * Operates alongside production speech-to-text models **`whisper-large-v3`** and **`whisper-large-v3-turbo`**.

3. **OpenRouter Dynamic Meta-Router (`openrouter/free`):**
   * Mapped official support for **`openrouter/free`**, an autonomous meta-router that dynamically inspects prompt requirements (tool-calling, JSON structured outputs, vision) and routes to the best available free model with minimal queue latency.
   * Rate limits confirmed: **20 RPM** global; **50 RPD** for standard free accounts; scaled to **1,000 RPD** upon completing a single lifetime deposit of $10 USD.

4. **SiliconFlow (Global GTM Domain & FLUX.2 Deployment):**
   * SiliconFlow services unified under **`https://api.siliconflow.cn/v1`** with Global Traffic Management (GTM) acceleration, replacing deprecated legacy domains.
   * Maintained permanent free tier for lightweight open models (Qwen and DeepSeek series); launched FLUX.2 serverless pay-per-image inference.

5. **Creative Multimodal Media Audit (Video & Image):**
   * **Kling AI (`kling.ai`)**: Web app provides **66 daily free credits** (up to 2–3 720p 5s video generations/day). API access is strictly prepaid (trial packs from ~$9 USD; ~$0.30–$0.42 per 5s video).
   * **Recraft AI (`recraft.ai`)**: Recraft Studio web app offers **50 daily free credits** for vector SVG/raster design. Recraft API is 100% prepaid at $1 USD = 1,000 API units (units do not expire).
   * **fal.ai (`fal.ai`)**: Confirmed no perpetual free API tier. Fair billing pay-as-you-go per megapixel ($0.003 for FLUX.1 [schnell], $0.025 for FLUX.1 [dev]) and per video second ($0.20–$0.40/s).

6. **Active Q4 2026 Promotion Tracking:**
   * **DeepSeek Off-Peak (-50%):** Active 01:00–04:00 & 06:00–10:00 UTC weekdays (= 22:00–01:00 & 03:00–07:00 BRT) and 100% on weekends.
   * **Maritaca AI:** Maintained 30% discount during night hours (22:00–06:00 BRT) and 50% discount on Batch API.
   * **Voyage AI:** Maintained 200M tokens trial grant for new developer accounts.
   * Zero active promotional developer quotas expired without formal documentation.

---

<a name="português"></a>
## 🇧🇷 Notas da Versão (Português)

A versão **v20.0.0** consolida a auditoria de novembro de 2026 com grande expansão em **mídia multimodal criativa (síntese de voz, transcrição, geração de vídeo e design gráfico)**, mapeamento de meta-roteadores dinâmicos e consolidação de endpoints globais em **66 provedores verificados**.

### 🌟 Principais Destaques e Modelos Adicionados

1. **Fish Audio (`fish.audio`) Adicionado (API Gratuita Permanente):**
   * Inclusão de provedor de referência em Text-to-Speech (TTS) e clonagem de voz zero-shot (10-30s de amostra).
   * Modelo neural **`s2.1-pro-free`** 100% gratuito na API a **$0.00 / 1 Milhão de UTF-8 bytes**, com concorrência de até **5 conexões simultâneas** sem exigência de cartão de crédito.
   * Interface web concede 8.000 créditos mensais renovados todo mês.

2. **Groq Cloud (Síntese Vocal / TTS Canopy Labs):**
   * Modelos em tempo real **`canopy-labs/orpheus-v1-en`** e **`canopy-labs/orpheus-arabic-saudi`** integrados à infraestrutura de LPUs do GroqCloud ao lado de `whisper-large-v3` e `whisper-large-v3-turbo`.

3. **OpenRouter (Meta-Roteador Dinâmico `openrouter/free`):**
   * Suporte documentado para o roteador autônomo **`openrouter/free`**, que despacha chamadas automaticamente para modelos gratuitos com suporte a chamadas de função (tool use), saídas estruturadas e visão computacional.
   * Limites de taxa: 20 RPM; 50 RPD para contas gratuitas; **1.000 RPD** após recarga acumulada de $10 USD vitalícia.

4. **SiliconFlow (Domínio Global GTM & FLUX.2):**
   * Endpoint oficial unificado em **`https://api.siliconflow.cn/v1`** com aceleração global GTM.
   * Modelos abertos Qwen e DeepSeek mantidos no Free Tier perpétuo; suporte a FLUX.2 em bilhetagem serverless por imagem.

5. **Auditoria de Mídia Multimodal (Vídeo, Imagem e Design):**
   * **Kling AI (`kling.ai`)**: Interface web com **66 créditos diários gratuitos** renovados a cada 24h (vídeos de 5s a 720p). API direta sem free tier permanente (pacotes de avaliação a partir de $9 USD).
   * **Recraft AI (`recraft.ai`)**: Studio web gratuito com **50 créditos diários** (vetores SVG e raster). API 100% pré-paga ($1 USD = 1.000 unidades que não expiram).
   * **fal.ai (`fal.ai`)**: Modelo pré-pago por megapixel ($0.003 em FLUX.1-schnell, $0.025 em FLUX.1-dev) e vídeo ($0.20 a $0.40/s), sem cota perpétua gratuita de API.

6. **Monitoramento de Promoções Ativas (Q4 2026):**
   * DeepSeek Off-Peak (-50%): das 22h-01h e 03h-07h BRT em dias úteis e 100% nos fins de semana.
   * Maritaca AI: -30% em horário noturno (22h-06h) e -50% na Batch API.
   * Voyage AI: Franquia de 200M tokens trial preservada.

---
⭐ **Apoie o Projeto:** Se este repositório economiza dinheiro para você e sua equipe, deixe uma Star ⭐ no repositório!
"""

payload = {
    "tag_name": "v20.0.0",
    "target_commitish": "main",
    "name": "🎙️ v20.0.0 — Multimodal Media Expansion: Fish Audio Free API, Groq TTS & OpenRouter Meta-Router",
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
