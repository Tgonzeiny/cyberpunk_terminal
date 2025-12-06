# Cyberpunk Accent Generator — Backend (FastAPI + Fly.io)

A lightweight FastAPI service that transforms plain English text into a cyberpunk-style accent (inspired by Blade Runner / Neuromancer slang).  
This backend is designed to support a retro terminal-style frontend hosted on Vercel.

---

## Features

- FastAPI microservice with a single `/accent` endpoint  
- Accepts JSON input: `{ "text": "hello world" }`
- Returns a modified cyberpunk-infused version of the text
- Utility layer with pluggable "accent modules"
- Fully deployable to Fly.io (Dockerfile + fly.toml included)
- CORS enabled for Vercel frontend

---

## Accent Rules (Current Implementation)

The `utils/accent.py` module applies rules such as:

- Word replacements  
  - “hello” → “oi choom”  
  - “friend” → “runner”  
  - “money” → “eddies”
- Occasional glitch text like `h3ll0`
- Neo-Tokyo slang suffixes
- Light sentence-level rewriting

More rules can be added easily.

---

##  Project Structure

cyberpunk_terminal_backend/
│
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── utils/
│   │   └── accent.py         # Accent transformation logic
│   └── models/
│       └── request.py        # Pydantic models
│
├── tests/
│
├── requirements.txt
├── Dockerfile
├── fly.toml
└── README.md


---

## Local Development

Create a virtual environment:

```bash
python -m venv venv

Activate it:

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the dev server:

uvicorn app.main:app --reload
```
## API Usage
POST /accent

Request:
{
  "text": "hello friend how are you?"
}

Response:
{
  "cyberpunk_text": "oi choom runner, how ya ridin'? //glitch"
}

## Deploying on Fly.io

1. Install Fly CLI
2. Run:
    fly launch
3. Deploy
    fly deploy
The API will be available at your Fly.io URL.

## Next Steps (Frontend Integration)

- A Next.js frontend will:
- Provide a neon cyberpunk terminal UI
- Send POST requests to the /accent endpoint
- Display results with a typing animation
- Create a visually striking demo suitable for LinkedIn posts

## Purpose of This Project
- A fast, flashy, weekend-ready build designed to impress recruiters by showing:
- API development (FastAPI)
- Backend structure & clean architecture
- Deployment experience (Fly.io)
- A fun, unique concept that stands out visually
- Expandable features (AI/ML later if desired)