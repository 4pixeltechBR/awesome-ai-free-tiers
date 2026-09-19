# 🦜 Maritaca AI (MariTalk) — The Brazilian LLM Champion (Free Tier)

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Maritaca AI Setup Guide

* **Official Platform:** [https://plataforma.maritaca.ai/](https://plataforma.maritaca.ai/)
* **Credit Card Required for Free Tier?** ❌ **NO** (Tier 0 free experimentation quota)
* **Phone / SMS Verification?** ❌ **NO** (Email or Google login)
* **Free Quota Highlights:**
  * **Tier 0 (Free):** Up to **50 RPM and 500,000 TPM** for developer testing without entering a credit card.
  * **OpenAI SDK Compatible:** Native compatibility via base URL `https://chat.maritaca.ai/api`.
* **Canonical API Model IDs:**
  * **`sabia-4`**: State-of-the-art frontier model for Portuguese, Brazilian cultural/legal context, and complex reasoning.
  * **`sabia-4-thinking`**: Deep reasoning variant with extended Chain-of-Thought and tool usage.
  * **`sabiazinho-4`**: Ultra-fast, low-latency, and cost-efficient compact model.
  * **`sabia-3` / `sabiazinho-3`**: Previous generation models maintained for legacy stability.

### Step-by-Step Instructions:
1. Visit [https://plataforma.maritaca.ai/](https://plataforma.maritaca.ai/) and register a free account.
2. In the dashboard menu, navigate to **Chaves de API** (API Keys).
3. Click **Criar chave de API** (Create API Key), name your key, and copy it.

### 1-Line Test Command (Terminal / cURL - OpenAI Compatible):
```bash
curl https://chat.maritaca.ai/api/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_MARITACA_API_KEY" \
  -d '{
    "model": "sabiazinho-4",
    "messages": [{"role": "user", "content": "Explique computação quântica em duas frases."}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia Oficial Maritaca AI (MariTalk) — A IA Brasileira

* **Link Oficial da Plataforma:** [https://plataforma.maritaca.ai/](https://plataforma.maritaca.ai/)
* **Exige Cartão de Crédito?** ❌ **NÃO** (Cota gratuita no Tier 0 para testes)
* **Exige SMS ou Telefone?** ❌ **NÃO** (Cadastro rápido com email ou Google)
* **Destaques da Cota Gratuita:**
  * **Tier 0 (Gratuito):** Até **50 requisições/minuto (RPM) e 500.000 tokens/minuto (TPM)** para experimentação sem cobrança.
  * **Compatível com o SDK da OpenAI:** Basta apontar o `base_url` para `https://chat.maritaca.ai/api`.
* **Identificadores Canônicos de Modelo:**
  * **`sabia-4`**: Modelo de fronteira com entendimento profundo da língua portuguesa, jurisprudência brasileira, ENEM, concursos e nuances culturais.
  * **`sabia-4-thinking`**: Variante de raciocínio aprofundado com Chain-of-Thought.
  * **`sabiazinho-4`**: Modelo leve, extremamente rápido e de baixíssima latência.
  * **`sabia-3` / `sabiazinho-3`**: Modelos estáveis da geração anterior.

### Passo a Passo:
1. Acesse [https://plataforma.maritaca.ai/](https://plataforma.maritaca.ai/) e crie sua conta gratuita.
2. No menu lateral, acesse **Chaves de API**.
3. Clique em **Criar chave de API**, defina um identificador e copie a chave gerada.

### Teste no Terminal (cURL compatível com OpenAI):
```bash
curl https://chat.maritaca.ai/api/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUA_CHAVE_MARITACA" \
  -d '{
    "model": "sabiazinho-4",
    "messages": [{"role": "user", "content": "Explique o que é o Pix em uma frase."}]
  }'
```
