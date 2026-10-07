import json

file_path = "data/providers.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

data["version"] = "1.5.0"
data["last_audit_date"] = "2026-10-07"
data["audit_notes"] = "v19 Fact-Check Audit against official terms, pricing, and LGPD compliance."

for p in data["providers"]:
    pid = p.get("id")
    if pid == "google-ai-studio":
        p["compliance_notes"] = "Free Tier data logged and reviewed by humans for model training. Prohibited for services directed to individuals under 18 (applies to Free and Paid)."
        for m in p.get("models", []):
            if m.get("canonical_id") == "gemini-2.0-flash":
                m["status"] = "deprecated"
                m["deprecation_date"] = "2026-06-01"
    elif pid == "deepseek":
        p["welcome_free_tokens"] = None
        p["data_residency"] = "China"
        p["off_peak_window"] = "01:00-04:00 and 06:00-10:00 UTC weekdays (= 22:00-01:00 and 03:00-07:00 BRT). Weekends 100% off-peak."
        p["thinking_mode"] = 'Enabled by default (consumes output tokens). Disable via extra_body: {"thinking": {"type": "disabled"}}'
        p["models"] = [
            {
                "canonical_id": "deepseek-flash",
                "display_name": "DeepSeek-V4.1-Flash (Recommended)",
                "modality": "multimodal",
                "pricing_per_1m": {
                    "peak_input_cache_miss_usd": 0.30,
                    "peak_input_cache_hit_usd": 0.006,
                    "peak_output_usd": 1.20,
                    "off_peak_input_cache_miss_usd": 0.15,
                    "off_peak_input_cache_hit_usd": 0.003,
                    "off_peak_output_usd": 0.60
                }
            },
            {
                "canonical_id": "deepseek-v4-flash",
                "display_name": "DeepSeek-V4-Flash (Legacy accepted)",
                "modality": "multimodal"
            }
        ]
    elif pid == "nvidia-nim":
        p["billing_tier"] = "trial_evaluation"
        p["terms_restriction"] = "Evaluation & Trial only. Commercial production strictly prohibited under NVIDIA API Trial Terms."
    elif pid == "maritaca-ai":
        p["billing_tier"] = "onboarding_credit_and_paid"
        p["grant"] = "R$ 20 one-time onboarding credit. No perpetual free API tier."
        p["compliance"] = "LGPD DPA available. sabia-4-br-sp variant offers 100% Brazilian data residency."
        p["discounts"] = "Night rate -30% (22h-06h), Batch API -50%."
    elif pid == "inception-labs":
        p["grant"] = "100,000,000 free tokens (one-time onboarding grant per account, non-recurring)"
        p["models"] = [
            {"canonical_id": "mercury-2", "display_name": "Mercury 2", "modality": "text"},
            {"canonical_id": "mercury-2.5", "display_name": "Mercury 2.5", "modality": "text"}
        ]
    elif pid == "groq-cloud":
        p["notes"] = "llama-3.3-70b-versatile and llama-3.1-8b-instant moved to Enterprise (Contact Sales). Limits enforced per organization."

# Add Xiaomi MiMo if not already present
if not any(p.get("id") == "xiaomi-mimo" for p in data["providers"]):
    data["providers"].append({
        "id": "xiaomi-mimo",
        "name": "Xiaomi MiMo",
        "console_url": "https://api.xiaomimimo.com/",
        "credit_card_required": False,
        "phone_required": False,
        "billing_tier": "budget_pay_as_you_go",
        "pricing_per_1m": {
            "input_usd": 0.14,
            "output_usd": 0.28
        },
        "models": [
            {"canonical_id": "mimo-v2.6-flash", "display_name": "MiMo V2.6 Flash", "modality": "text"}
        ],
        "budget_token_plans": [
            {"name": "MiMo Token Plan Lite", "price_usd_monthly": 6.0, "target": "Coding IDE Assistant"},
            {"name": "MiMo Token Plan Pro", "price_usd_monthly": 15.0, "target": "High-Volume Coding"}
        ]
    })

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated providers.json successfully to v{data['version']}. Total providers: {len(data['providers'])}")
