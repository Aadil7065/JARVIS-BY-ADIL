JARVIS-BY-ADIL

# 🤖 JARVIS BY X

> **Advanced AI Assistant for Termux (Android)**  
> **Created by ADIl** · Powered by DeepSeek

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

- 🔐 **Secure** — API key local config mein, kabhi GitHub par nahi

- 🛠️ **Auto-setup** — First run par permissions aur API key manage karta hai

pkg update -y && pkg upgrade -y
``

```bash
pkg install git python python-pip tesseract tesseract-data-eng tesseract-data-hin termux-api python-pillow -y
```

```bash
cd ~
git clone https://github.com/Aadil7065/JARVIS-BY-ADIL.git
JARVIS-BY-ADIL
```

```bash

pip install -r requirements.txt

pip install pytesseract --no-deps
```

termux-setup-storage
```

```bash
python -c 'import requests, PIL, pytesseract; print("All OK")'
```

```bash
python jarvis.py
```

---

## 🔑 Get DeepSeek API Key

1. Visit: **https://platform.deepseek.com**
2. Sign Up / Login
3. Left sidebar → **API Keys**
4. **Create new API key** → Name: `jarvis` → Create
5. Copy key: `sk-xxxxxxxxxxxxxxxx`

## ▶️ How to Run


```bash
cd ~/jarvis-by-x
python jarvis.py
```

```bash
python ~/jarvis-by-x/jarvis.py
```

```bash
chmod +x ~/jarvis-by-x/jarvis.py
~/jarvis-by-x/jarvis.py
```

---

## 🎯 JARVIS Commands

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



```bash
pkg update && pkg upgrade -y
```

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

```bash
cd ~/jarvis-by-x
git pull
```

```bash
cd ~/jarvis-by-x
pip install -r requirements.txt --upgrade
```

### Full refresh

```bash
cd ~
rm -rf jarvis-by-x
git clone https://github.com/Aadil7065/JARVIS-BY-ADIL.git
cd jarvis-by-x
pip install -r requirements.txt
pip install pytesseract --no-deps
```

---
### Reset API key

```bash
rm ~/.jarvis/config.json
```

<br>

### Clear generated code

```bash
rm -rf ~/.jarvis/code/*
```

<br>

### Clear screenshots

```bash
rm -f ~/.jarvis/screen.png
```

<br>

### Full JARVIS reset

```bash
rm -rf ~/.jarvis
```

<br>

### Uninstall JARVIS

```bash
rm -rf ~/jarvis-by-x ~/.jarvis
```

```bash
termux-battery-status
```

termux-vibrate -d 500
```


```bash
termux-notification --title "Test" --content "Hello"
```

```bash
termux-tts-speak "hello world"
```

```bash
termux-clipboard-set "hello"
termux-clipboard-get
``` 

```bash
python -c 'import pytesseract; from PIL import Image; print(pytesseract.image_to_string(Image.open("/data/data/com.termux/files/home/test.png")))'
```
### Test GPS location

```bash
termux-location
```

<br>

### Test voice input

```bash
termux-speech-to-text
```

---

## 🛠️ Troubleshooting

### `ModuleNotFoundError: requests`

```bash
pip install requests
```

<br>

### `ModuleNotFoundError: PIL`

```bash
pkg install python-pillow -y
```

<br>

### `ModuleNotFoundError: pytesseract`

```bash
pip install pytesseract --no-deps
```

<br>

### `tesseract: command not found`

```bash
pkg install tesseract tesseract-data-eng tesseract-data-hin -y
```

<br>

### `termux-battery-status: command not found`

```bash
pkg install termux-api -y
```

> F-Droid se **Termux:API** app bhi install karein.

<br>

### `HTTP 401` — API key galat

```bash
rm ~/.jarvis/config.json
python jarvis.py
```


```bash
termux-setup-storage
```

<br>

### `git: command not found`

```bash
pkg install git -y
```

<br>

### Voice not working

```bash
pkg install termux-api
```

> F-Droid se **Termux:API** app install karein.

---



## 🧠 Tech Stack

- Python 3.9+
- DeepSeek (deepseek-chat + deepseek-coder)
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
