#!/usr/bin/env python3
# =============================================================
#   JARVIS BY X
#   Advanced AI Assistant for Termux (Android)
#   Created by ADIl
#   Powered by Multi-Free-AI Providers (Auto-Failover)
# =============================================================

import os
import sys
import json
import time
import re
import subprocess
import requests
from pathlib import Path

# ---------- STYLE CONSTANTS ----------
R = "\033[91m"
G = "\033[92m"
P = "\033[95m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[97m"
BOLD = "\033[1m"
DIM = "\033[2m"
RST = "\033[0m"

# ---------- PATHS ----------
HOME = str(Path.home())
CFG_DIR = os.path.join(HOME, ".jarvis")
CFG_FILE = os.path.join(CFG_DIR, "config.json")
SHOT = os.path.join(CFG_DIR, "screen.png")
CODE_DIR = os.path.join(CFG_DIR, "code")
os.makedirs(CFG_DIR, exist_ok=True)
os.makedirs(CODE_DIR, exist_ok=True)

# ---------- BANNER ----------
BANNER = f"""{R}{BOLD}
     ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
     ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
     ██║███████║██████╔╝██║   ██║██║███████╗
██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝{RST}
{P}{BOLD}         BY  X   ┃   Created by ADIl{RST}
{G}{DIM}        Advanced AI Assistant for Termux{RST}
{P}{DIM}  ══════════════════════════════════════════════{RST}
"""

# ---------- FREE AI PROVIDERS (Auto-Switch) ----------
FREE_PROVIDERS = [
    {"name": "Groq", "url": "https://api.groq.com/openai/v1/chat/completions", "model": "llama-3.3-70b-versatile", "key_env": "GROQ_API_KEY", "cfg_name": "groq_key"},
    {"name": "OpenRouter", "url": "https://openrouter.ai/api/v1/chat/completions", "model": "meta-llama/llama-3.3-70b-instruct:free", "key_env": "OPENROUTER_API_KEY", "cfg_name": "openrouter_key"},
    {"name": "Google Gemini", "url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions", "model": "gemini-1.5-flash", "key_env": "GEMINI_API_KEY", "cfg_name": "gemini_key"},
    {"name": "Mistral", "url": "https://api.mistral.ai/v1/chat/completions", "model": "mistral-small-latest", "key_env": "MISTRAL_API_KEY", "cfg_name": "mistral_key"},
    {"name": "Cerebras", "url": "https://api.cerebras.ai/v1/chat/completions", "model": "llama3.1-8b", "key_env": "CEREBRAS_API_KEY", "cfg_name": "cerebras_key"},
    {"name": "SambaNova", "url": "https://api.sambanova.ai/v1/chat/completions", "model": "Meta-Llama-3.3-70B-Instruct", "key_env": "SAMBANOVA_API_KEY", "cfg_name": "sambanova_key"},
    {"name": "Pollinations (No Key)", "url": "https://text.pollinations.ai/openai", "model": "openai", "key_env": "", "cfg_name": "none"}
]

# ---------- UTILS ----------
def run(cmd, timeout=45):
    try:
        return subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, timeout=timeout
        ).decode(errors="ignore").strip()
    except subprocess.CalledProcessError as e:
        return (e.output or b"").decode(errors="ignore").strip()
    except Exception as e:
        return str(e)

def say(t, c=W):
    print(f"{c}{t}{RST}")

def ask(p, c=G):
    try:
        return input(f"{c}{p}{RST}").strip()
    except (EOFError, KeyboardInterrupt):
        return "exit"

def clear():
    os.system("clear")

def load_cfg():
    if os.path.exists(CFG_FILE):
        try:
            with open(CFG_FILE) as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cfg(c):
    try:
        with open(CFG_FILE, "w") as f:
            json.dump(c, f, indent=2)
    except Exception:
        pass

# ---------- TOOL CHECK ----------
def has_tool(cmd):
    out = run(cmd).lower()
    return bool(out) and "not found" not in out and "error" not in out and "no module" not in out

def permissions_wizard():
    say("  Scanning system tools...", Y)
    time.sleep(0.3)
    tools = [
        ("Termux:API", "which termux-battery-status", "pkg install termux-api -y"),
        ("Tesseract OCR", "which tesseract", "pkg install tesseract tesseract-data-eng tesseract-data-hin -y"),
        ("Pillow (PIL)", "python -c 'import PIL'", "pkg install python-pillow -y"),
        ("pytesseract", "python -c 'import pytesseract'", "pip install pytesseract --no-deps"),
        ("requests", "python -c 'import requests'", "pip install requests"),
    ]
    missing = []
    for name, check, install in tools:
        if has_tool(check):
            say(f"   [OK]   {name}", G)
        else:
            say(f"   [MISS] {name}", R)
            missing.append((name, install))

    if not missing:
        say("  All components ready.", G)
        return

    print()
    say(f"  {len(missing)} component(s) missing.", Y)
    print()
    say("  Options:", P)
    say("    1)  Auto-install all missing now", W)
    say("    2)  Show manual commands", W)
    say("    3)  Skip (some features may fail)", W)
    say("    4)  Exit", W)

    choice = ask("  Choose [1/2/3/4]: ", P)
    if choice == "1":
        for name, cmd in missing:
            say(f"  Installing {name} ...", C)
            print(run(cmd, timeout=300))
        say("  Installation finished.", G)
    elif choice == "2":
        say("  Run these commands manually:", Y)
        for _, cmd in missing:
            say(f"    {cmd}", C)
        ask("  Press Enter to continue...")
    elif choice == "4":
        say("  Exiting.", R)
        sys.exit(0)

# ---------- SETUP ----------
def setup():
    clear()
    print(BANNER)
    cfg = load_cfg()

    say("  Welcome to JARVIS BY X", P + BOLD)
    say("  ────────────────────────────────────────", DIM)
    print()

    if not cfg.get("setup_done"):
        say("  Free AI API Setup (Kisi ek ki bhi key daal sakte hain)", Y + BOLD)
        print()
        say("  Links to get Free Keys:", C)
        say("    Groq:       https://console.groq.com/keys", W)
        say("    OpenRouter: https://openrouter.ai/keys", W)
        say("    Gemini:     https://aistudio.google.com/apikey", W)
        print()
        
        for p in FREE_PROVIDERS:
            if p["cfg_name"] == "none": continue
            
            # Check env variable first
            env_key = os.getenv(p["key_env"], "")
            if env_key:
                cfg[p["cfg_name"]] = env_key
                continue
                
            k = ask(f"  {p['name']} API Key (Enter to skip): ", P)
            if k and k.lower() not in ("skip", "exit", "quit"):
                cfg[p["cfg_name"]] = k
        
        cfg["setup_done"] = True
        save_cfg(cfg)
        say("\n  Setup complete. Agar koi key nahi daali, toh default free AI use hoga.", G)
        time.sleep(1.5)
    else:
        say("  API settings loaded from ~/.jarvis/config.json", G)

    print()
    permissions_wizard()
    time.sleep(1)
    return cfg

# ---------- AI BRAIN (Multi-Provider Fallback) ----------
SYSTEM_PROMPT = """You are JARVIS BY X, an advanced AI mobile assistant created by ADIl, running on Android via Termux.

Understand and reply in the user's language (Hindi, English, Tamil, Bengali, or any).

Return ONLY valid JSON. No text outside JSON.
Format: {"action":"<name>","parameters":{...},"response":"<short reply>"}

Available actions and parameters:
- chat                     {"":""}
- open_app                 {"package":"com.pkg.name"}
- battery                  {}
- vibrate                  {"ms":500}
- notify                   {"title":"","content":""}
- tts                      {"text":""}
- screenshot               {}
- read_screen              {}
- read_screen_ui           {}
- clipboard_get            {}
- clipboard_set            {"text":""}
- sms_send                 {"number":"","message":""}
- call                     {"number":""}
- volume_up                {}
- volume_down              {}
- flashlight               {"on":true}
- location                 {}
- device_info              {}
- list_files               {"dir":"~/"}
- shell                    {"cmd":"..."}
- write_code               {"prompt":"...","filename":"x.py"}
- read_code                {"filename":"x.py"}
- edit_code                {"filename":"x.py","instruction":"..."}
- run_code                 {"filename":"x.py"}
- delete_code              {"filename":"x.py"}

Keep responses short and friendly. Reply in the user's language."""

def call_ai(messages, model="auto", timeout=60):
    cfg = load_cfg()
    last_err = "Koi valid API key nahi mili."
    
    for p in FREE_PROVIDERS:
        # Check if we have a key for this provider
        key = cfg.get(p["cfg_name"], "")
        if not key and p["cfg_name"] != "none":
            continue # Skip if no key and it's not the no-key provider
            
        headers = {"Content-Type": "application/json"}
        if key and key != "none":
            headers["Authorization"] = f"Bearer {key}"
            
        # Use provider's default model
        req_model = p["model"]
        body = {"model": req_model, "messages": messages, "temperature": 0.3}
        
        # Special case for Pollinations
        if p["name"].startswith("Pollinations"):
            body["model"] = "openai"
            
        try:
            say(f"  [Connecting to {p['name']}...]", DIM)
            r = requests.post(p["url"], headers=headers, json=body, timeout=timeout)
            
            if r.status_code == 200:
                data = r.json()
                if "choices" in data and len(data["choices"]) > 0:
                    say(f"  [Connected via {p['name']}]", G)
                    return data["choices"][0]["message"]["content"]
                elif "content" in data:
                    say(f"  [Connected via {p['name']}]", G)
                    return data["content"]
            else:
                err_msg = r.json().get("error", {}).get("message", f"HTTP {r.status_code}")
                last_err = f"{p['name']} error: {err_msg}"
                continue # Move to next provider
                
        except Exception as e:
            last_err = f"{p['name']} connection failed: {str(e)[:50]}"
            continue # Move to next provider
            
    return f"__ERROR__ Saare API fail ho gaye. Last error: {last_err}"

def decide(user_input):
    content = call_ai([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ])
    if content.startswith("__ERROR__"):
        return {"action": "chat", "parameters": {}, "response": content[9:].strip()}
    try:
        s = content.find("{")
        e = content.rfind("}") + 1
        return json.loads(content[s:e])
    except Exception:
        return {"action": "chat", "parameters": {}, "response": content}

# ---------- ACTIONS ----------
def act_battery():
    return run("termux-battery-status")

def act_vibrate(ms=500):
    run(f"termux-vibrate -d {int(ms)}")
    return f"Vibrated {ms}ms"

def act_notify(title, content):
    t = title.replace('"', "'")
    c = content.replace('"', "'")
    run(f'termux-notification --title "{t}" --content "{c}"')
    return "Notification sent"

def act_tts(text):
    safe = text.replace('"', "'")
    run(f'termux-tts-speak "{safe}"')
    return "Speaking..."

def act_screenshot():
    run(f"screencap -p {SHOT}")
    return f"Screenshot: {SHOT}"

def act_read_screen():
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        return "OCR libs missing. Restart to install."
    run(f"screencap -p {SHOT}")
    try:
        txt = pytesseract.image_to_string(Image.open(SHOT), lang="eng+hin").strip()
        return txt or "(no text detected)"
    except Exception as e:
        return f"OCR error: {e}"

def act_read_screen_ui():
    run("uiautomator dump /data/local/tmp/ui.xml >/dev/null 2>&1")
    out = run("cat /data/local/tmp/ui.xml 2>/dev/null")
    if not out:
        return "(UI dump unavailable)"
    try:
        texts = re.findall(r'text="([^"]+)"', out)
        return " | ".join(t for t in texts if t.strip()) or "(empty)"
    except Exception:
        return "(parse error)"

def act_open_app(pkg):
    if not pkg:
        return "No package given"
    return run(f"monkey -p {pkg} -c android.intent.category.LAUNCHER 1")

def act_clipboard_get():
    return run("termux-clipboard-get") or "(empty)"

def act_clipboard_set(text):
    safe = text.replace('"', "'")
    run(f'termux-clipboard-set "{safe}"')
    return "Clipboard set"

def act_sms(number, message):
    if not number:
        return "No number given"
    safe = message.replace('"', "'")
    return run(f'termux-sms-send -n {number} "{safe}"')

def act_call(number):
    if not number:
        return "No number given"
    return run(f"termux-telephony-call {number}")

def act_volume(direction):
    key = "24" if direction == "up" else "25"
    run(f"input keyevent {key}")
    return f"Volume {direction}"

def act_flashlight(on):
    run(f"termux-torch {'on' if on else 'off'}")
    return f"Flashlight {'ON' if on else 'OFF'}"

def act_location():
    return run("termux-location")

def act_device_info():
    info = {
        "model": run("getprop ro.product.model"),
        "brand": run("getprop ro.product.brand"),
        "android": run("getprop ro.build.version.release"),
        "battery": run("termux-battery-status"),
    }
    return json.dumps(info, indent=2)

def act_list_files(d):
    return run(f"ls -la {d}")

def act_shell(cmd):
    return run(cmd)

# ---------- CODE MANAGER ----------
def cm_write(prompt, filename):
    if not prompt:
        return "No prompt given"
    code = call_ai(
        [{"role": "user", "content": f"Write Python code for: {prompt}. Return ONLY code, no markdown, no explanations."}],
        model="auto"
    )
    if code.startswith("__ERROR__"):
        return code
    path = os.path.join(CODE_DIR, filename)
    try:
        with open(path, "w") as f:
            f.write(code)
        return f"Saved: {path}"
    except Exception as e:
        return f"Save error: {e}"

def cm_read(filename):
    path = os.path.join(CODE_DIR, filename)
    if not os.path.exists(path):
        return f"Not found: {path}"
    try:
        return open(path).read()
    except Exception as e:
        return f"Read error: {e}"

def cm_edit(filename, instruction):
    path = os.path.join(CODE_DIR, filename)
    if not os.path.exists(path):
        return f"Not found: {path}"
    try:
        old = open(path).read()
    except Exception as e:
        return f"Read error: {e}"
    new = call_ai(
        [{"role": "user", "content": f"Edit this code:\n{old}\n\nInstruction: {instruction}\n\nReturn ONLY the edited code."}],
        model="auto"
    )
    if new.startswith("__ERROR__"):
        return new
    try:
        with open(path, "w") as f:
            f.write(new)
        return f"Edited: {path}"
    except Exception as e:
        return f"Write error: {e}"

def cm_run(filename):
    path = os.path.join(CODE_DIR, filename)
    if not os.path.exists(path):
        return f"Not found: {path}"
    ext = os.path.splitext(filename)[1]
    interp = {".py": "python", ".sh": "bash", ".js": "node"}.get(ext)
    if not interp:
        return f"Unknown extension: {ext}"
    return run(f"{interp} {path}", timeout=90) or "(no output)"

def cm_delete(filename):
    path = os.path.join(CODE_DIR, filename)
    if os.path.exists(path):
        try:
            os.remove(path)
            return f"Deleted: {filename}"
        except Exception as e:
            return f"Delete error: {e}"
    return "File not found"

# ---------- DISPATCHER ----------
def handle(decision):
    a = decision.get("action", "chat")
    p = decision.get("parameters", {}) or {}
    reply = decision.get("response", "Done")
    try:
        if a == "open_app":         reply = act_open_app(p.get("package", ""))
        elif a == "battery":        reply = act_battery()
        elif a == "vibrate":        reply = act_vibrate(int(p.get("ms", 500)))
        elif a == "notify":         reply = act_notify(p.get("title", "JARVIS BY X"), p.get("content", ""))
        elif a == "tts":            reply = act_tts(p.get("text", reply))
        elif a == "screenshot":     reply = act_screenshot()
        elif a == "read_screen":    reply = act_read_screen()
        elif a == "read_screen_ui": reply = act_read_screen_ui()
        elif a == "clipboard_get":  reply = act_clipboard_get()
        elif a == "clipboard_set":  reply = act_clipboard_set(p.get("text", ""))
        elif a == "sms_send":       reply = act_sms(p.get("number", ""), p.get("message", ""))
        elif a == "call":           reply = act_call(p.get("number", ""))
        elif a == "volume_up":      reply = act_volume("up")
        elif a == "volume_down":    reply = act_volume("down")
        elif a == "flashlight":     reply = act_flashlight(bool(p.get("on", True)))
        elif a == "location":       reply = act_location()
        elif a == "device_info":    reply = act_device_info()
        elif a == "list_files":     reply = act_list_files(p.get("dir", "~/"))
        elif a == "shell":          reply = act_shell(p.get("cmd", "echo hi"))
        elif a == "write_code":     reply = cm_write(p.get("prompt", ""), p.get("filename", "out.py"))
        elif a == "read_code":      reply = cm_read(p.get("filename", "out.py"))
        elif a == "edit_code":      reply = cm_edit(p.get("filename", "out.py"), p.get("instruction", ""))
        elif a == "run_code":       reply = cm_run(p.get("filename", "out.py"))
        elif a == "delete_code":    reply = cm_delete(p.get("filename", "out.py"))
    except Exception as e:
        reply = f"Action error: {e}"
    return reply

# ---------- MAIN LOOP ----------
def main():
    setup()
    clear()
    print(BANNER)
    say("  Ready, ADIl.", G + BOLD)
    say("  Type anything in any language. Type 'help' for examples.", DIM)
    say("  ──────────────────────────────────────────────", P)

    while True:
        try:
            q = ask("\n  You ▸ ", P + BOLD)
        except (EOFError, KeyboardInterrupt):
            say("\n  Goodbye!", P)
            break

        if not q:
            continue
        low = q.lower()

        if low in ("exit", "quit", "bye"):
            say("  Goodbye from JARVIS BY X!", P + BOLD)
            break
        if low in ("clear", "cls"):
            clear(); print(BANNER); continue
        if low == "help":
            say("  ── Examples ──", Y + BOLD)
            for line in [
                "mera battery kitna hai",
                "WhatsApp kholo",
                "screen par kya likha hai",
                "vibrate karo",
                "notify karo 'paani pi lo'",
                "awaaz mein bolo 'namaste'",
                "device info dikhao",
                "clipboard mein 'hello' daalo",
                "ek python file likho jo prime check kare",
                "out.py chalao",
                "sort.py edit karo - reverse sort kare",
            ]:
                say(f"    • {line}", W)
            say("\n  ── Meta commands ──", Y + BOLD)
            say("    voice    → speak your command", W)
            say("    clear    → clear screen", W)
            say("    exit     → quit", W)
            continue
        if low in ("voice", "sun", "bolo"):
            say("  Listening...", Y)
            v = run("termux-speech-to-text")
            if not v:
                say("  Could not hear anything.", R)
                continue
            say(f"  Heard: {v}", DIM)
            q = v

        say("  Thinking...", DIM)
        decision = decide(q)
        reply = handle(decision)
        print()
        say(f"  JARVIS ▸ {reply}", G + BOLD)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        say("\n  Interrupted.", Y)
    except Exception as e:
        say(f"  Fatal error: {e}", R)
