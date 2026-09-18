# 🐋 DeepSeek API — Free Tokens, Canonical Model IDs & The $5 Super-ROI Guide

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 DeepSeek Official API Guide

* **Official Platform:** [https://platform.deepseek.com/](https://platform.deepseek.com/)
* **Credit Card Required for Free Tier?** ❌ **NO**
* **Phone / SMS Verification?** ✅ **YES** (Standard international mobile SMS confirmation)
* **Free Quota:** **5,000,000 Free Tokens (5M tokens)** automatically granted to new verified accounts (valid for 30 days).
* **Canonical API Model IDs:**
  * **`deepseek-chat`** ➔ DeepSeek-V3 (General conversational, coding, reasoning)
  * **`deepseek-reasoner`** ➔ DeepSeek-R1 (Deep Chain-of-Thought mathematical and logical reasoning)

### 💰 Official Pricing per 1M Tokens & $5 USD ROI
DeepSeek is the undisputed global leader in inference cost-efficiency:
* **DeepSeek-V3 (`deepseek-chat`)**:
  * Input (Cache Miss): **\$0.14** / 1M tokens (Off-Peak: **\$0.07**)
  * Input (Cache Hit): **\$0.014** / 1M tokens (Off-Peak: **\$0.007**)
  * Output: **\$0.28** / 1M tokens (Off-Peak: **\$0.14**)
* **DeepSeek-R1 (`deepseek-reasoner`)**:
  * Input (Cache Miss): **\$0.55** / 1M tokens
  * Input (Cache Hit): **\$0.14** / 1M tokens
  * Output: **\$2.19** / 1M tokens
* **50% Off-Peak Discount**: Every day between 00:30 and 08:30 UTC+8 (China Standard Time).
* **The \$5 USD Power**: A minimum deposit of **\$5 USD yields between 18 Million and 35 Million tokens** on DeepSeek-V3 (and over 100M+ tokens with high prompt caching hit rates).

### Step-by-Step Instructions:
1. Visit [https://platform.deepseek.com/](https://platform.deepseek.com/) and click **Sign Up**.
2. Verify your email and mobile phone number via SMS.
3. Your 5,000,000 free tokens balance will appear immediately under **Usage**.
4. Go to **"API keys"** in the left menu and click **"Create API key"**.
5. Copy your key (`sk-...`).

### 1-Line Test Command (Terminal / cURL):
```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_DEEPSEEK_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello DeepSeek!"}]
  }'
```

---

<a name="português"></a>
## 🇧🇷 Guia Oficial da DeepSeek API

* **Link Oficial da Plataforma:** [https://platform.deepseek.com/](https://platform.deepseek.com/)
* **Exige Cartão de Crédito?** ❌ **NÃO** para a cota de boas-vindas
* **Exige SMS ou Telefone?** ✅ **SIM** (Confirmação por SMS internacional)
* **Cota Gratuita Inicial:** **5.000.000 de tokens grátis (5M tokens)** creditados automaticamente para novas contas verificadas (válidos por 30 dias).
* **Identificadores Canônicos de Modelo:**
  * **`deepseek-chat`** ➔ DeepSeek-V3 (Modelo geral para código, chat e automação)
  * **`deepseek-reasoner`** ➔ DeepSeek-R1 (Raciocínio lógico aprofundado com Chain-of-Thought)

### 💰 Tabela Oficial de Preços e Rendimento de \$5 USD
A DeepSeek é a líder mundial imbatível em custo-benefício de inferência:
* **DeepSeek-V3 (`deepseek-chat`)**:
  * Entrada (Cache Miss): **\$0.14** por 1M de tokens (Horário Econômico: **\$0.07**)
  * Entrada (Cache Hit): **\$0.014** por 1M de tokens (Horário Econômico: **\$0.007**)
  * Saída: **\$0.28** por 1M de tokens (Horário Econômico: **\$0.14**)
* **DeepSeek-R1 (`deepseek-reasoner`)**:
  * Entrada (Cache Miss): **\$0.55** / 1M tokens
  * Entrada (Cache Hit): **\$0.14** / 1M tokens
  * Saída: **\$2.19** / 1M tokens
* **Desconto Noturno de 50% (Off-Peak)**: Todos os dias das 00:30 às 08:30 UTC+8.
* **O Poder de \$5 Dólares**: Uma recarga mínima de **\$5 USD rende entre 18 Milhões e 35 Milhões de tokens** no V3 (ou mais de 100 Milhões de tokens com cache de contexto ativado).

### Passo a Passo:
1. Acesse [https://platform.deepseek.com/](https://platform.deepseek.com/) e faça o cadastro.
2. Valide seu email e número de celular por SMS.
3. Seus 5M de tokens gratuitos aparecerão na tela de saldo.
4. No menu lateral, clique em **"API keys"** e depois em **"Create API key"**.
5. Copie sua chave gerada (`sk-...`).

### Teste Rápido no Terminal:
```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SUA_CHAVE_DEEPSEEK" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Ola DeepSeek!"}]
  }'
```
