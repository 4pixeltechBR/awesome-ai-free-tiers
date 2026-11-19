import json
import os

file_path = r"E:\Arquivos desenvolvimento\awesome-ai-free-tiers\data\providers.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data["version"] = "1.7.0"
data["last_audit_date"] = "2026-11-19"
data["audit_notes"] = "v21 Live Audit: OVHcloud AI Endpoints keyless GDPR tier added, Kilo Code keyless gateway added, Aion Labs added, Nscale / Upstage Solar / AI21 / Inference.net / NLP Cloud trials added, Gemma 4 added to OpenRouter, glhf.chat deprecated, Ollama Cloud status clarified."

existing_ids = {p.get("id") for p in data["providers"]}

# 1. Update OpenRouter with Gemma 4 if not present
for p in data["providers"]:
    if p["id"] == "openrouter":
        existing_models = {m.get("canonical_id") for m in p.get("models", [])}
        if "google/gemma-4-31b-it:free" not in existing_models:
            p["models"].append({
                "canonical_id": "google/gemma-4-31b-it:free",
                "display_name": "Gemma 4 31B Instruct (Free)",
                "modality": "text",
                "rate_limits": {"rpm": 20}
            })
        if "google/gemma-4-26b-a4b-it:free" not in existing_models:
            p["models"].append({
                "canonical_id": "google/gemma-4-26b-a4b-it:free",
                "display_name": "Gemma 4 26B-A4B MoE (Free)",
                "modality": "text",
                "rate_limits": {"rpm": 20}
            })

# 2. Add OVHcloud AI Endpoints
if "ovhcloud" not in existing_ids:
    data["providers"].append({
        "id": "ovhcloud",
        "name": "OVHcloud AI Endpoints",
        "console_url": "https://endpoints.ai.cloud.ovh.net/",
        "api_endpoint": "https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "permanent_free",
        "grant": "Keyless anonymous tier at 2 RPM/IP or ~400 RPM with free developer API key generated in OVHcloud Manager without credit card. 100% GDPR compliant hosted in France with zero user data training.",
        "models": [
            {
                "canonical_id": "gpt-oss-120b",
                "display_name": "GPT-OSS 120B",
                "modality": "text",
                "rate_limits": {"rpm": 400}
            },
            {
                "canonical_id": "Qwen3.5-397B-A17B",
                "display_name": "Qwen 3.5 397B A17B MoE",
                "modality": "text",
                "rate_limits": {"rpm": 400}
            },
            {
                "canonical_id": "Mistral-Small-3.2-24B",
                "display_name": "Mistral Small 3.2 24B",
                "modality": "text",
                "rate_limits": {"rpm": 400}
            },
            {
                "canonical_id": "DeepSeek-R1-Distill-Llama-70B",
                "display_name": "DeepSeek R1 Distill Llama 70B",
                "modality": "reasoning",
                "rate_limits": {"rpm": 400}
            },
            {
                "canonical_id": "whisper-large-v3-turbo",
                "display_name": "Whisper Large V3 Turbo",
                "modality": "audio_stt",
                "rate_limits": {"rpm": 400}
            },
            {
                "canonical_id": "bge-m3",
                "display_name": "BGE M3 Multilingual Embeddings",
                "modality": "embeddings",
                "rate_limits": {"rpm": 400}
            }
        ]
    })

# 3. Add Kilo Code Gateway
if "kilo-code" not in existing_ids:
    data["providers"].append({
        "id": "kilo-code",
        "name": "Kilo Code Gateway",
        "console_url": "https://kilo.ai/",
        "api_endpoint": "https://api.kilo.ai/api/gateway",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "anonymous_keyless",
        "grant": "Keyless access with Authorization: Bearer anonymous, ~200 requests/hour per IP for coding and open workloads.",
        "models": [
            {
                "canonical_id": "kilo/auto",
                "display_name": "Kilo Auto Router",
                "modality": "code",
                "rate_limits": {"rph": 200}
            },
            {
                "canonical_id": "qwen2.5-coder-32b-instruct",
                "display_name": "Qwen 2.5 Coder 32B Instruct",
                "modality": "code",
                "rate_limits": {"rph": 200}
            }
        ]
    })

# 4. Add Aion Labs
if "aion-labs" not in existing_ids:
    data["providers"].append({
        "id": "aion-labs",
        "name": "Aion Labs",
        "console_url": "https://aionlabs.ai/",
        "api_endpoint": "https://api.aionlabs.ai/v1",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "permanent_free",
        "grant": "15 RPM / 20k TPD without credit card for creative writing, literature and roleplay.",
        "models": [
            {
                "canonical_id": "aion-narrative-v2",
                "display_name": "Aion Narrative V2",
                "modality": "text_creative",
                "rate_limits": {"rpm": 15, "tpd": 20000}
            }
        ]
    })

# 5. Add Welcome Trials (Nscale, Upstage Solar, AI21 Studio, Inference.net, NLP Cloud)
trial_additions = [
    {
        "id": "nscale",
        "name": "Nscale",
        "console_url": "https://nscale.com/",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "welcome_trial",
        "grant": "$5 USD in serverless GPU & LLM inference compute on signup without credit card."
    },
    {
        "id": "upstage-solar",
        "name": "Upstage Solar",
        "console_url": "https://console.upstage.ai/",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "welcome_trial",
        "grant": "$10 USD welcome credit for Solar Pro 10.7B/22B models and Document AI."
    },
    {
        "id": "ai21-studio",
        "name": "AI21 Studio",
        "console_url": "https://studio.ai21.com/",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "welcome_trial",
        "grant": "$10 USD trial credit valid for 3 months for Jamba 1.5 Mini and Large models."
    },
    {
        "id": "inference-net",
        "name": "Inference.net",
        "console_url": "https://inference.net/",
        "credit_card_required": False,
        "phone_required": True,
        "billing_tier": "welcome_trial",
        "grant": "$5 USD free credit upon SMS phone verification for fast open-weights LLMs."
    },
    {
        "id": "nlp-cloud",
        "name": "NLP Cloud",
        "console_url": "https://nlpcloud.com/",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "welcome_trial",
        "grant": "$15 USD welcome credits for NLP classification, embeddings and LLM generation."
    }
]

for t in trial_additions:
    if t["id"] not in existing_ids:
        data["providers"].append(t)

# 6. Flag glhf.chat and update Ollama Cloud
for p in data["providers"]:
    if p["id"] == "glhf-chat":
        p["status"] = "retired"
        p["retired_date"] = "2026-11-19"
        p["retirement_note"] = "Service shut down and rebranded to synthetic.new (100% paid)."
    elif p["id"] == "ollama-cloud":
        p["status"] = "commercial"
        p["billing_tier"] = "pay_as_you_go"
        p["notes"] = "Cloud free tier sunset in 2026. Operates on Pay-As-You-Go ($0.05/M tokens) and Pro ($20/mo) / Max ($100/mo) plans. 100% free usage available via local execution (localhost)."

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"providers.json updated to v{data['version']}. Total providers: {len(data['providers'])}")
