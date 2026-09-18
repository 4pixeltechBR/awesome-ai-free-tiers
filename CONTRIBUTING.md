# 🤝 Contributing to Awesome AI Free Tiers / Como Contribuir

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 Community Contribution Guidelines

Welcome to the **Awesome AI Free Tiers & Budget APIs Directory**!  
Our mission is to build the world's most trustworthy, comprehensive, and up-to-date repository of free AI compute and micro-budget inference.

### 🌟 Help Us Spread the Word!
The more developers use and audit this repository, the more leverage we have to convince AI providers to offer permanent free tiers:
1. **Star this repository** on GitHub ⭐ (It helps us gain visibility in GitHub Trending).
2. **Share it** on X/Twitter, LinkedIn, Reddit (`r/LocalLLaMA`, `r/ArtificialInteligence`), Hacker News, and developer Discord servers.
3. **Embed our badge** in your open-source projects!

```markdown
[![Verified AI Free Tier](https://img.shields.io/badge/AI%20Free%20Tier-Verified-success?style=flat-square&logo=github)](https://github.com/4pixeltechBR/awesome-ai-free-tiers)
```

---

### 🏢 Are You an AI Provider? Get Listed!
If your company provides inference with a permanent free tier or ultra-low-cost budget plans:
1. Open a new issue using our **[Official Provider Submission Template](https://github.com/4pixeltechBR/awesome-ai-free-tiers/issues/new?template=01_provider_submission.yml)**.
2. Provide your official developer console URL (NO affiliate links).
3. Specify your canonical model IDs, rate limits (RPM, TPM, RPD), and whether a credit card is required.
4. Once verified by our automated tests and maintainers, your platform will be featured in the directory with the **Verified Provider Seal**!

---

### 🛠️ How to Submit Changes
1. **Fork** this repository.
2. Create a feature branch: `git checkout -b add-provider-name`.
3. Adhere strictly to our **6 Auditing Golden Rules** (`docs/auditing_rules.md`):
   - Only canonical API model IDs (`deepseek-chat`, `gemini-2.5-flash`).
   - Granular limits (RPM, TPM, RPD).
   - Zero affiliate links or referral parameters.
   - Proof of `HTTP 200 OK` terminal response.
4. If adding a new provider, please also create a 60-second tutorial in `docs/how-to-get-api-keys/<provider-name>.md`.
5. Open a **Pull Request** and follow the checklist.

---

<a name="português"></a>
## 🇧🇷 Como Contribuir com o Repositório

Seja muito bem-vindo ao **Awesome AI Free Tiers**!  
Nossa missão é construir a maior e mais confiável biblioteca aberta do mundo sobre cotas gratuitas e planos de baixo custo para desenvolvedores de IA.

### 🌟 Ajude a Divulgar o Movimento!
Quanto maior for a nossa comunidade, mais força teremos para fazer com que os grandes provedores de IA criem e mantenham cotas gratuitas para todos:
1. **Deixe sua Estrela (Star ⭐)** no topo do repositório no GitHub.
2. **Compartilhe o link** no LinkedIn, WhatsApp, Telegram, Reddit e comunidades de programação.
3. **Use nosso selo** no README dos seus projetos de IA!

---

### 🏢 Você é um Provedor de IA? Venha Divulgar!
Se sua plataforma oferece cotas gratuitas ou inferência econômica:
1. Abra uma issue usando o **[Formulário de Submissão de Provedor](https://github.com/4pixeltechBR/awesome-ai-free-tiers/issues/new?template=01_provider_submission.yml)**.
2. Informe o console oficial (sem links de afiliados).
3. Liste os modelos, cotas (RPM, TPM, RPD) e informe se precisa de cartão.
4. Após validação pela nossa equipe, sua plataforma receberá o **Selo Oficial de Provedor Verificado**.

---

### 🛠️ Como Enviar um Pull Request (PR)
1. Faça um **Fork** do repositório.
2. Crie uma branch: `git checkout -b meu-novo-provedor`.
3. Siga à risca as **6 Regras de Ouro de Auditoria** (`docs/auditing_rules.md`):
   - Proibido inventar dados ou modelos fantasmas.
   - Use apenas os nomes oficiais da API (ex: `deepseek-chat`).
   - Zero links de indicação/afiliados.
   - Anexe um teste real de terminal comprovando que a API funciona.
4. Crie o tutorial passo a passo na pasta `docs/how-to-get-api-keys/`.
5. Abra o seu **Pull Request**!
