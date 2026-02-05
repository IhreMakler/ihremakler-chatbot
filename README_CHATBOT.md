# 🏠 IhreMakler Chatbot

Eine professionelle Chatbot-Anwendung mit **ChatGPT Integration** im Corporate Design von **IhreMakler**.

## ✨ Features

- ✅ **ChatGPT Integration** - Intelligente Antworten durch OpenAI GPT-3.5-Turbo
- ✅ **Professional Design** - IhreMakler Corporate Identity (Dunkelblau & Türkis)
- ✅ **Chat History** - Unterhaltung speichern und anzeigen
- ✅ **Responsive Layout** - Funktioniert auf allen Geräten
- ✅ **Einfache Bedienung** - Intuitive Web-App ohne Installation

## 🚀 Quick Start (Lokal)

### Voraussetzungen
- Python 3.8+
- OpenAI API Key (kostenlos auf https://platform.openai.com)

### Installation

1. **Repository klonen oder Dateien herunterladen**
```bash
cd ihremakler-chatbot
```

2. **Abhängigkeiten installieren**
```bash
pip install -r requirements.txt
```

3. **Umgebungsvariable setzen**
Erstelle eine `.streamlit/secrets.toml` Datei:
```toml
OPENAI_API_KEY = "sk-..."  # Dein OpenAI API Key
```

4. **App starten**
```bash
streamlit run streamlit_chatbot.py
```

Die App öffnet sich unter: `http://localhost:8501`

## 🌐 Online Deployment (Streamlit Cloud)

### 1. GitHub Repository erstellen
1. Gehe zu https://github.com/new
2. Repository Name: `ihremakler-chatbot`
3. **Public** wählen
4. Erstelle das Repository

### 2. Dateien hochladen
1. Click **"Add file"** → **"Upload files"**
2. Lade hoch:
   - `streamlit_chatbot.py`
   - `requirements.txt`
   - `Logo1.png`
   - `README.md`

### 3. Streamlit Cloud verbinden
1. Gehe zu https://share.streamlit.io
2. Mit GitHub anmelden
3. Click **"New app"**
4. Wähle `ihremakler-chatbot` Repository
5. Main file: `streamlit_chatbot.py`
6. Click **Deploy**

### 4. API Key konfigurieren
1. Nach dem Deployment klick **"Manage app"** (rechts oben)
2. Gehe zu **"Secrets"**
3. Füge ein:
```
OPENAI_API_KEY = "sk-..."
```

✅ Die App lädt sich automatisch neu und funktioniert!

## 🔑 OpenAI API Key bekommen

1. Gehe zu https://platform.openai.com/account/api-keys
2. Melde dich an / Registriere dich
3. Click **"Create new secret key"**
4. Kopiere den Key (👁️ Icon, um ihn zu sehen)
5. **Speichere ihn sicher!**

> **Kosten:** OpenAI berechnet pro API-Nutzung. Kostenlos gibt es $5 Credits für neue Nutzer.

## 📱 Bedienung

1. **Starten:** App öffnet sich im Browser
2. **Frage stellen:** Text in das Eingabefeld eingeben
3. **Senden:** Auf "Senden" Button klicken
4. **Antwort erhalten:** ChatGPT antwortet im Chat-Interface

## 🎨 Design

Die App nutzt das **IhreMakler Corporate Design**:
- **Farben:** Dunkelblau (#062E52), Türkis (#3B8EA0)
- **Schriftart:** Arial, Verdana
- **Layout:** Professionell, modern, benutzerfreundlich

## 📁 Dateien

```
ihremakler-chatbot/
├── streamlit_chatbot.py    # Hauptanwendung
├── requirements.txt        # Python Abhängigkeiten
├── Logo1.png              # IhreMakler Logo
└── README.md              # Diese Datei
```

## ⚙️ Anforderungen

- **Python:** 3.8 oder höher
- **Streamlit:** ^1.16.0
- **OpenAI Python:** ^1.0.0
- **Pillow:** Für Bildunterstützung

## 🐛 Fehlerbehebung

**Problem:** "OpenAI API Key nicht konfiguriert"
- **Lösung:** Stellsicher, dass der Key in Streamlit Secrets eingetragen ist

**Problem:** Keine Antwort vom Chatbot
- **Lösung:** Überprüfe deinen API Key auf https://platform.openai.com
- Stelle sicher, dass du genug Credits/Balance hast

**Problem:** App lädt nicht
- **Lösung:** Überprüfe Terminal auf Fehlermeldungen
- Stelle sicher, dass alle Dateien vorhanden sind

## 📞 Support

Für Fragen zum IhreMakler Service:
- **Email:** info@ihremakler.online
- **Telefon:** +49 30 30398 281
- **Website:** https://www.ihremakler.online

## 📄 Lizenz

© 2024 IhreMakler. Alle Rechte vorbehalten.

---

**Entwickelt mit:** Streamlit + OpenAI ChatGPT + IhreMakler Design CI
