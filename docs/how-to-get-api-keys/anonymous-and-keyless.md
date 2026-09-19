# 🕵️ Anonymous & Keyless AI Gateways (Zero Signup, Zero Credit Card)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Anonymous Free AI Access

For testing, education, or prototyping without creating an account or storing API keys:

### 1. AI Horde (Crowdsourced Distributed GPUs)
* **Portal:** [https://aihorde.net/](https://aihorde.net/)
* **Account Required?** ❌ **NO**
* **Anonymous API Key:** `0000000000` (10 zeros)
* **Endpoint:** `https://oai.aihorde.net/v1/chat/completions`
* **Features:** Volunteer GPU cluster providing text completions and Stable Diffusion image generation.

```bash
curl https://oai.aihorde.net/v1/chat/completions \
  -H "Authorization: Bearer 0000000000" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "auto",
    "messages": [{"role": "user", "content": "Hello AI Horde!"}]
  }'
```

### 2. DuckDuckGo AI Chat
* **Portal:** [https://duckduckgo.com/duckchat](https://duckduckgo.com/duckchat)
* **Account Required?** ❌ **NO**
* **Models:** Claude 3 Haiku, GPT-4o mini, Llama 3.3 70B, Mixtral 8x7B.
* **Privacy:** Completely anonymous web interface; prompts are not stored or used for model training.

### 3. UncloseAI
* **Portal:** [https://uncloseai.com/](https://uncloseai.com/)
* **Account Required?** ❌ **NO**
* **API Key:** Accepts any dummy non-empty string.
* **OpenAI SDK Base URL:** `https://api.uncloseai.com/v1`

---

<a name="português"></a>
## 🇧🇷 Acesso Anônimo e Sem Chave (Zero Cadastro, Zero Cartão)

Plataformas para prototipagem rápida e testes sem precisar fornecer email ou criar chaves:

1. **AI Horde (`aihorde.net`)**: Rede distribuída de GPUs voluntárias. Chave anônima pública: `0000000000`.
2. **DuckDuckGo AI Chat (`duckduckgo.com/duckchat`)**: Chat anônimo direto na web com GPT-4o mini, Claude 3 Haiku e Llama 3.3.
3. **UncloseAI (`uncloseai.com`)**: Gateway compatível com OpenAI que aceita qualquer chave arbitrária de teste.
