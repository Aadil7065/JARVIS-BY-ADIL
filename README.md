# 🤖 JARVIS BY X

> **Advanced AI Assistant for Termux (Android)**  
> **Created by ADIl** · Powered by Multi-Free AI APIs

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Platform](https://img.shields.io/badge/Platform-Termux-green)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## ✨ Features

- 🗣️ **Multilingual** — Hindi, English, Tamil, Bengali, aur koi bhi bhasha
- 📱 **Full Device Control** — Battery, vibrate, notification, flashlight, volume, clipboard, SMS, calls
- 📖 **Screen Reading** — OCR (English + Hindi) + native UI dump
- 💻 **Code Assistant** — AI se code likhwana, edit karna, chalana
- 🎤 **Voice Mode** — Speech-to-text support
- 🎨 **Beautiful Terminal UI** — Colorful, interactive interface
- 🔐 **Secure** — API keys local config mein, kabhi GitHub par nahi
- 🛠️ **Auto-setup** — First run par permissions aur API keys manage karta hai
- 🔄 **Auto-Failover** — 10+ Free AI APIs (Groq, Gemini, OpenRouter, etc.) support

---

## 🚀 Installation

### 1. Install Termux & Termux:API (F-Droid se)
- [Termux](https://f-droid.org/packages/com.termux/)
- [Termux:API](https://f-droid.org/packages/com.termux.api/)

<br>

### 2. Update Termux

```bash
pkg update -y && pkg upgrade -y
```

<br>

### 3. Install System Packages

```bash
pkg install git python python-pip tesseract tesseract-data-eng tesseract-data-hin termux-api python-pillow -y
```

<br>

### 4. Clone the Repository

```bash
cd ~
git clone https://github.com/Aadil7065/JARVIS-BY-ADIL.git
cd JARVIS-BY-ADIL
```

<br>

### 5. Install Python Dependencies

```bash
pip install -r requirements.txt
```

```bash
pip install pytesseract --no-deps
```

<br>

### 6. Grant Storage Access

```bash
termux-setup-storage
```
*(Popup aayega, "Allow" par click karein)*

<br>

### 7. Run JARVIS

```bash
python jarvis.py
```

---

## 🔑 How to Get FREE API Keys (No Credit Card Needed)

Aapko kisi ek provider ki free API key chahiye. JARVIS automatically unhe switch karega.

1. **Groq (Best & Fastest):** [https://console.groq.com/keys](https://console.groq.com/keys)
2. **Google Gemini:** [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
3. **OpenRouter:** [https://openrouter.ai/keys](https://openrouter.ai/keys)

Jab aap pehli baar `python jarvis.py` chalayenge, toh JARVIS aapse yeh keys maangega aur safe save kar dega.

---

## ▶️ How to Run

### Basic Run

```bash
cd ~/JARVIS-BY-ADIL
python jarvis.py
```

<br>

### Run from Anywhere

```bash
python ~/JARVIS-BY-ADIL/jarvis.py
```

<br>

### Make Executable and Run

```bash
chmod +x ~/JARVIS-BY-ADIL/jarvis.py
```

```bash
~/JARVIS-BY-ADIL/jarvis.py
```

---

## 🎯 JARVIS Commands (Inside Tool)

Yeh commands aap tool ke andar likhenge (`You ▸` par):

### 📱 Device Control

| Command | Action |
|---|---|
| `mera battery kitna hai` | Battery status |
| `vibrate karo` | Vibrate 500ms |
| `500ms vibrate karo` | Custom vibrate |
| `notify karo 'paani pi lo'` | Notification |
| `awaaz mein bolo 'namaste'` | Text-to-speech |
| `flashlight on karo` | Torch ON |
| `flashlight off karo` | Torch OFF |
| `volume up karo` | Volume up |
| `volume down karo` | Volume down |
| `location dikhao` | GPS location |
| `device info dikhao` | System info |

<br>

### 📲 App Launch

| Command | Action |
|---|---|
| `WhatsApp kholo` | WhatsApp |
| `YouTube kholo` | YouTube |
| `Instagram kholo` | Instagram |
| `Chrome kholo` | Chrome |
| `Camera kholo` | Camera |
| `Settings kholo` | Settings |

<br>

### 💻 Code Assistant

| Command | Action |
|---|---|
| `ek python file likho jo prime check kare` | Generate code |
| `out.py chalao` | Run code |
| `out.py padho` | Read code |
| `out.py edit karo - error handling add karo` | Edit code |
| `out.py delete karo` | Delete code |

<br>

### 🎤 Meta Commands

| Command | Action |
|---|---|
| `help` / `madad` | Show examples |
| `voice` / `sun` / `bolo` | Voice mode |
| `clear` / `cls` | Clear screen |
| `exit` / `quit` / `bye` | Quit tool |

---

## 🧪 System Diagnostic Commands (Termux)

Agar aapko lagta hai koi feature kaam nahi kar raha, toh inhe Termux mein direct chala kar test karein:

### Test Battery
```bash
termux-battery-status
```

<br>

### Test Vibrate
```bash
termux-vibrate -d 500
```

<br>

### Test Notification
```bash
termux-notification --title "Test" --content "Hello"
```

<br>

### Test TTS (Awaaz)
```bash
termux-tts-speak "hello world"
```

<br>

### Test Clipboard
```bash
termux-clipboard-set "hello"
```
```bash
termux-clipboard-get
```

<br>

### Test Screenshot & OCR
```bash
screencap -p ~/test.png
```
```bash
python -c 'import pytesseract; from PIL import Image; print(pytesseract.image_to_string(Image.open("/data/data/com.termux/files/home/test.png")))'
```

<br>

### Test GPS Location
```bash
termux-location
```

<br>

### Test Voice Input
```bash
termux-speech-to-text
```

---

## 🛠️ Maintenance & Update Commands

### Update all packages
```bash
pkg update && pkg upgrade -y
```

<br>

### Reinstall Python / Pillow / Tesseract (Agar kuch kharab ho)
```bash
pkg reinstall python -y
```
```bash
pkg reinstall python-pillow -y
```
```bash
pkg reinstall tesseract tesseract-data-eng tesseract-data-hin -y
```
```bash
pkg reinstall termux-api -y
```

<br>

### Pull Latest Changes from GitHub
```bash
cd ~/JARVIS-BY-ADIL
git pull
```

<br>

### Full Refresh (Fresh Clone)
```bash
cd ~
rm -rf JARVIS-BY-ADIL
git clone https://github.com/Aadil7065/JARVIS-BY-ADIL.git
cd JARVIS-BY-ADIL
pip install -r requirements.txt
pip install pytesseract --no-deps
```

<br>

### Reset API Keys (Agar key galat daal di ho)
```bash
rm ~/.jarvis/config.json
```

<br>

### Clear Generated Code (AI ke banaye code delete karne ke liye)
```bash
rm -rf ~/.jarvis/code/*
```

<br>

### Full JARVIS Reset
```bash
rm -rf ~/.jarvis
```

<br>

### Uninstall JARVIS Completely
```bash
rm -rf ~/JARVIS-BY-ADIL ~/.jarvis
```

---

# ❌ Error / Troubleshooting Guide

Agar aapko koi bhi error aaye, toh yahan dekhein:

<br>

### 1. `ModuleNotFoundError: requests`
**Solution:** 
```bash
pip install requests
```

<br>

### 2. `ModuleNotFoundError: PIL` (Pillow install nahi ho raha)
*Note: Termux mein pip se Pillow install nahi hota, use pkg se karein.*
**Solution:** 
```bash
pkg install python-pillow -y
```

<br>

### 3. `ModuleNotFoundError: pytesseract`
**Solution:** 
```bash
pip install pytesseract --no-deps
```

<br>

### 4. `tesseract: command not found`
**Solution:** 
```bash
pkg install tesseract tesseract-data-eng tesseract-data-hin -y
```

<br>

### 5. `termux-battery-status: command not found`
**Solution:** 
```bash
pkg install termux-api -y
```
*(Aur F-Droid se **Termux:API** app install karein)*

<br>

### 6. `HTTP 402: Insufficient Balance` (DeepSeek ka error)
**Solution:** Ab JARVIS multiple free APIs use karta hai. Agar koi ek API fail ho rahi hai, toh tool automatically doosri API par switch ho jayega. Aapko bas Groq ya Gemini ki free API key daalni hai.
```bash
rm ~/.jarvis/config.json
python jarvis.py
```

<br>

### 7. `HTTP 401: Unauthorized` (API key galat hai)
**Solution:** 
```bash
rm ~/.jarvis/config.json
python jarvis.py
```
*(Phir se chalane par nayi API key daalein)*

<br>

### 8. `Permission denied` (Screen padhte waqt ya file save karte waqt)
**Solution:** 
```bash
termux-setup-storage
```
*(Popup mein Allow karein)*

<br>

### 9. `git: command not found`
**Solution:** 
```bash
pkg install git -y
```

<br>

### 10. Voice input kaam nahi kar raha
**Solution:** 
```bash
pkg install termux-api
```
*(F-Droid se **Termux:API** app install karein aur phone ko restart karein)*

---

## 🧠 Tech Stack

- Python 3.9+
- Multi-Free AI APIs (Groq, Gemini, OpenRouter, etc.)
- Tesseract (Hindi + English OCR)
- Termux:API
- requests

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**ADIl**

---

⭐ Star the repo if you like it!
