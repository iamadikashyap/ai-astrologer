# 🔮 AI Astrologer (Streamlit)

A simple, self-contained AI-style astrologer app that:
- Collects user birth details (Name, Date, Time, Place) via a clean UI
- Generates a rule-based astrology-style reading (sun sign, element, numerology, moon phase, Chinese zodiac)
- Lets the user ask a free-text question and returns a context-aware response
- Provides a downloadable text copy of the reading
- **No external APIs** required

> **Note:** For entertainment purposes only.

## 🏃‍♂️ Quick Start

### 1) Create & activate a virtual environment (recommended)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the app
```bash
streamlit run app.py
```
Open the URL that appears in your terminal (usually (http://localhost:8501/)).

## 🧠 How it Works

- **Sun Sign** determined by your birth date.
- **Element & Traits** tied to your sun sign.
- **Moon Phase** uses a lightweight approximation of the current lunar phase.
- **Numerology (Lucky Number)** uses a simple reduction of the letters/digits in your name.
- **Chinese Zodiac** determined by your birth year.
- **Free-text Question** is routed to a relevant domain (career/love/money/health) using simple keyword matching, and blends in lunar tone + element themes for guidance.

The logic lives in `astrology_engine.py` and is deterministic day-to-day for the same inputs.

## 📦 Project Structure

```
ai-astrologer/
├─ app.py                # Streamlit UI
├─ astrology_engine.py   # Rule-based "AI" logic
├─ requirements.txt
└─ README.md
```

## 🎬 Demo Video (How to Record)

Record a **2–5 minute** demo showing:
1. Opening the app and entering sample details
2. Generating the reading
3. Asking a free-text question and viewing the response
4. Downloading the reading as `.txt`

Suggested script:
- “Here’s the AI Astrologer. I’ll enter Name, Date, Time, Place. After clicking *Get My Reading*, it generates a personalized reading with sun sign, element, moon phase, numerology, and a Chinese zodiac tag. I’ll ask a question about my career; notice the tailored guidance. Finally, I can download the reading.”

Use any screen recorder (QuickTime on macOS, Xbox Game Bar on Windows, or OBS) and save the MP4.

## 🚀 Deploy Options (Optional)

- **Local demo** (recommended for speed) using `streamlit run`.
- **Streamlit Cloud**: push this folder to GitHub and deploy with one click.
- **Docker** (optional):
  ```bash
  docker run -p 8501:8501 -v "$PWD":/app -w /app python:3.11-slim \
    /bin/bash -lc "pip install -r requirements.txt && streamlit run app.py --server.port 8501 --server.address 0.0.0.0"
  ```

## ✅ Deliverables Checklist

- [x] Clean UI for inputs
- [x] Astrology-based output (rule-based)
- [x] Free-text question with a response
- [x] Downloadable reading
- [x] README with setup steps
- [x] Demo video guidance

## ⚠️ Disclaimer

This app is for entertainment and reflective purposes only. It does not provide medical, financial, or legal advice.# ai-astrologer
