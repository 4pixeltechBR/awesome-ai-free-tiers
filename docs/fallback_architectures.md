# 🔄 Production Resilient Multi-Provider Fallback / Arquiteturas de Fallback Resilientes

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 High-Availability Architecture (99.99% Free Uptime)

By combining multiple 100% free providers into an automated fallback cascade, you can run high-throughput production AI applications, automated agents, and batch workflows with **zero infrastructure cost and virtually zero downtime**.

### Recommended Fallback Routing Order

```
[Tier 0: Primary] ➔ Google AI Studio (Gemini 2.5 Flash: 1,500 RPD, 1M TPM, Search Grounding)
      │ (on HTTP 429 Rate Limit / 503 Overload)
      ▼
[Tier 1: Speed]   ➔ Groq Cloud (Qwen 3.8 / GPT-OSS 120B / Llama 3.3: 30 RPM, Ultra-low latency)
      │ (on HTTP 429)
      ▼
[Tier 2: Catalog] ➔ NVIDIA NIM (82 open models: 40 RPM, 1,000 RPD per account)
      │ (on HTTP 429)
      ▼
[Tier 3: Backup]  ➔ Hyperbolic / SiliconFlow / Pollinations (Open-source fallback)
```

### Python Implementation (OpenAI SDK Compatible)

```python
import os
import time
from openai import OpenAI

PROVIDERS = [
    {
        "name": "Google AI Studio",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "api_key": os.getenv("GEMINI_API_KEY"),
        "model": "gemini-2.5-flash",
    },
    {
        "name": "Groq Cloud",
        "base_url": "https://api.groq.com/openai/v1",
        "api_key": os.getenv("GROQ_API_KEY"),
        "model": "qwen/qwen3.8-27b",
    },
    {
        "name": "NVIDIA NIM",
        "base_url": "https://integrate.api.nvidia.com/v1",
        "api_key": os.getenv("NVIDIA_API_KEY"),
        "model": "meta/llama-3.3-70b-instruct",
    },
    {
        "name": "SiliconFlow Free",
        "base_url": "https://api.siliconflow.cn/v1",
        "api_key": os.getenv("SILICONFLOW_API_KEY"),
        "model": "Qwen/Qwen2.5-7B-Instruct",
    }
]

def chat_completion_with_fallback(messages, max_tokens=1024, temperature=0.7):
    last_error = None
    for provider in PROVIDERS:
        if not provider["api_key"]:
            continue
        try:
            client = OpenAI(base_url=provider["base_url"], api_key=provider["api_key"])
            response = client.chat.completions.create(
                model=provider["model"],
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                timeout=15.0
            )
            return {
                "provider": provider["name"],
                "model": provider["model"],
                "content": response.choices[0].message.content
            }
        except Exception as e:
            print(f"⚠️ [{provider['name']}] Failed: {e}. Switching to next provider...")
            last_error = e
            continue
    raise RuntimeError(f"All free providers exhausted! Last error: {last_error}")

# Example Usage
if __name__ == "__main__":
    result = chat_completion_with_fallback([
        {"role": "user", "content": "Explain quantum computing in two simple sentences."}
    ])
    print(f"✅ Success from {result['provider']} ({result['model']}):\n{result['content']}")
```

---

<a name="português"></a>
## 🇧🇷 Arquitetura de Alta Disponibilidade (99.99% Uptime Gratuito)

Combinando múltiplos provedores 100% gratuitos em uma cascata de contingência (*fallback*), você constrói agentes autônomos e serviços de produção com **custo zero de infraestrutura e virtualmente sem quedas por rate limit**.

### Cascata Recomendada

```
[Nível 0: Primário]  ➔ Google AI Studio (Gemini 2.5 Flash: 1.500 RPD, 1M TPM, Grounding)
      │ (em caso de HTTP 429 Rate Limit ou 503)
      ▼
[Nível 1: Velocidade]➔ Groq Cloud (Qwen 3.8 / GPT-OSS 120B / Llama 3.3: LPUs ultrarrápidas)
      │ (em caso de HTTP 429)
      ▼
[Nível 2: Catálogo]  ➔ NVIDIA NIM (82 modelos de ponta: 40 RPM, 1.000 RPD)
      │ (em caso de HTTP 429)
      ▼
[Nível 3: Reserva]   ➔ Hyperbolic / SiliconFlow / Pollinations (Modelos abertos)
```
