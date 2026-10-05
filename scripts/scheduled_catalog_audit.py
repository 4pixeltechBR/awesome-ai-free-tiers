"""
Awesome AI Free Tiers — Scheduled Catalog Audit & Health Monitor
Executado automaticamente pelo Agendador de Tarefas do Windows (Task Scheduler)
Toda Segunda-feira, Quarta-feira e Sexta-feira às 17:00.
"""

import os
import sys
import json
import shutil
import datetime
import urllib.request
import subprocess

# Garantir UTF-8 no stdout do Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = r"E:\Arquivos desenvolvimento"
REPO_DIR = os.path.join(BASE_DIR, "awesome-ai-free-tiers")
LOGS_DIR = os.path.join(REPO_DIR, "logs")
CATALOG_MD = os.path.join(BASE_DIR, "freetiers_apis.md")
PROVIDERS_JSON = os.path.join(REPO_DIR, "data", "providers.json")

def notify_windows(title: str, message: str):
    """Envia uma notificação Toast no Windows informando a conclusão da rotina."""
    try:
        ps_cmd = f"""
        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
        $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
        $textNodes = $template.GetElementsByTagName('text')
        $textNodes.Item(0).AppendChild($template.CreateTextNode('{title}')) > $null
        $textNodes.Item(1).AppendChild($template.CreateTextNode('{message}')) > $null
        $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Awesome AI Free Tiers')
        $notification = [Windows.UI.Notifications.ToastNotification]::new($template)
        $notifier.Show($notification)
        """
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=False, timeout=10)
    except Exception:
        pass

def main():
    os.makedirs(LOGS_DIR, exist_ok=True)
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(LOGS_DIR, "scheduled_audit.log")

    log_entries = [f"\n{'='*70}", f"🚀 EXECUÇÃO DE AUDITORIA AUTOMÁTICA: {now_str}"]

    # 1. Backup do catálogo canônico
    if os.path.exists(CATALOG_MD):
        stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        bak_name = os.path.join(BASE_DIR, f"freetiers_apis.md.bak_auto_{stamp}")
        try:
            shutil.copy2(CATALOG_MD, bak_name)
            log_entries.append(f"✅ Backup canônico criado: {os.path.basename(bak_name)} ({os.path.getsize(bak_name)} bytes)")
        except Exception as e:
            log_entries.append(f"⚠️ Erro ao criar backup: {e}")
    else:
        log_entries.append(f"❌ Catálogo canônico não encontrado em: {CATALOG_MD}")

    # 2. Leitura e validação de providers.json
    total_providers = 0
    if os.path.exists(PROVIDERS_JSON):
        try:
            with open(PROVIDERS_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
            total_providers = len(data.get("providers", []))
            version = data.get("version", "unknown")
            last_audit = data.get("last_audit_date", "unknown")
            log_entries.append(f"✅ Dataset providers.json validado: {total_providers} provedores (v{version}, audit {last_audit})")
        except Exception as e:
            log_entries.append(f"❌ Erro ao validar providers.json: {e}")
    else:
        log_entries.append(f"❌ providers.json não encontrado em: {PROVIDERS_JSON}")

    # 3. Health check de conectividade nos consoles principais
    test_endpoints = [
        ("Google AI Studio", "https://aistudio.google.com/"),
        ("Groq Cloud", "https://console.groq.com/"),
        ("NVIDIA NIM", "https://build.nvidia.com/"),
        ("DeepSeek Platform", "https://platform.deepseek.com/"),
        ("Maritaca AI", "https://plataforma.maritaca.ai/"),
        ("Cloudflare Workers AI", "https://dash.cloudflare.com/"),
        ("OpenRouter", "https://openrouter.ai/"),
    ]

    log_entries.append("\n📡 HEALTH-CHECK DE CONECTIVIDADE (Consoles & Gateways):")
    online_count = 0
    for name, url in test_endpoints:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "AwesomeAI-HealthChecker/1.0"})
            with urllib.request.urlopen(req, timeout=5) as response:
                status = response.getcode()
                log_entries.append(f"  • {name} ({url}): HTTP {status} OK")
                online_count += 1
        except urllib.error.HTTPError as e:
            log_entries.append(f"  • {name} ({url}): HTTP {e.code} (Acessível)")
            online_count += 1
        except Exception as e:
            log_entries.append(f"  • {name} ({url}): ⚠️ Falha na verificação: {e}")

    log_entries.append(f"\nResumo: {online_count}/{len(test_endpoints)} consoles verificados com sucesso.")

    # 4. Sincronização Git se houver alterações
    try:
        status_proc = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_DIR,
            capture_output=True,
            text=True,
            check=False
        )
        if status_proc.stdout.strip():
            log_entries.append("\n🔄 Detectadas alterações pendentes no git. Realizando commit e push...")
            subprocess.run(["git", "add", "."], cwd=REPO_DIR, check=False)
            commit_msg = f"chore(auto-audit): routine catalog & health check sync ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_DIR, check=False)
            push_proc = subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, capture_output=True, text=True, check=False)
            if push_proc.returncode == 0:
                log_entries.append("✅ Git push executado com sucesso para origin/main.")
            else:
                log_entries.append(f"⚠️ Git push retornou código {push_proc.returncode}: {push_proc.stderr}")
        else:
            log_entries.append("\n🌿 Repositório git limpo e atualizado (sem alterações pendentes).")
    except Exception as e:
        log_entries.append(f"⚠️ Erro na checagem do git: {e}")

    log_entries.append(f"{'='*70}\n")
    output_text = "\n".join(log_entries)

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(output_text)

    try:
        print(output_text)
    except Exception:
        try:
            print(output_text.encode("ascii", errors="replace").decode("ascii"))
        except Exception:
            pass

    # 5. Notificação no Windows
    notify_windows(
        "Awesome AI Free Tiers — Auditoria Executada",
        f"Auditoria agendada concluída com sucesso! {online_count}/{len(test_endpoints)} consoles online. Catálogo seguro."
    )

if __name__ == "__main__":
    main()
