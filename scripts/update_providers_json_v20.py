import json

file_path = r"E:\Arquivos desenvolvimento\awesome-ai-free-tiers\data\providers.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data["version"] = "1.6.0"
data["last_audit_date"] = "2026-11-10"
data["audit_notes"] = "v20 Live Audit: Fish Audio permanent free API added, Groq TTS Orpheus models added, OpenRouter openrouter/free meta-router mapped, SiliconFlow GTM endpoint updated."

# Check and update Groq
for p in data["providers"]:
    if p["id"] == "groq-cloud":
        existing_models = [m.get("canonical_id") for m in p.get("models", [])]
        if "canopy-labs/orpheus-v1-en" not in existing_models:
            p["models"].append({
                "canonical_id": "canopy-labs/orpheus-v1-en",
                "display_name": "Canopy Labs Orpheus V1 English",
                "modality": "audio_tts",
                "rate_limits": {"rpm": 30, "rpd": 1000}
            })
        if "canopy-labs/orpheus-arabic-saudi" not in existing_models:
            p["models"].append({
                "canonical_id": "canopy-labs/orpheus-arabic-saudi",
                "display_name": "Canopy Labs Orpheus Arabic Saudi",
                "modality": "audio_tts",
                "rate_limits": {"rpm": 30, "rpd": 1000}
            })
    elif p["id"] == "openrouter":
        existing_models = [m.get("canonical_id") for m in p.get("models", [])]
        if "openrouter/free" not in existing_models:
            p["models"].insert(0, {
                "canonical_id": "openrouter/free",
                "display_name": "OpenRouter Free Meta-Router",
                "modality": "dynamic_multimodal",
                "rate_limits": {"rpm": 20, "rpd": 50, "rpd_with_10usd_topup": 1000}
            })
    elif p["id"] == "siliconflow":
        p["console_url"] = "https://cloud.siliconflow.cn/"
        p["api_endpoint"] = "https://api.siliconflow.cn/v1"
        p["notes"] = "Global traffic accelerated via GTM domain api.siliconflow.cn. Permanent free tier for lightweight open models; FLUX.2 serverless pay-per-image."

# Add Fish Audio if not present
if not any(p.get("id") == "fish-audio" for p in data["providers"]):
    data["providers"].append({
        "id": "fish-audio",
        "name": "Fish Audio",
        "console_url": "https://fish.audio/",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "permanent_free",
        "grant": "Model s2.1-pro-free 100% free at $0.00 / 1M UTF-8 bytes in the API with 5 concurrency. Web app provides 8,000 monthly credits.",
        "models": [
            {
                "canonical_id": "s2.1-pro-free",
                "display_name": "Fish Speech 2.1 Pro Free",
                "modality": "audio_tts",
                "pricing_per_1m_bytes_usd": 0.0,
                "rate_limits": {
                    "concurrency": 5
                }
            },
            {
                "canonical_id": "s2.1-pro",
                "display_name": "Fish Speech 2.1 Pro (Studio)",
                "modality": "audio_tts",
                "pricing_per_1m_bytes_usd": 1.50
            }
        ]
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"providers.json updated to v{data['version']}. Total providers: {len(data['providers'])}")
