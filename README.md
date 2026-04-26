# Luma — AI Research Chatbot

A web-based conversational AI built with **Flask** and the **Google Gemini API**. Luma handles everyday chat and switches into a structured **Research Mode** for analytical, report-style responses — complete with contextual memory across the conversation.

---

## Features

- Real-time AI chat interface
- Research Mode for structured, in-depth responses (methodology, analysis, conclusions)
- Multi-turn conversation memory
- Dark / Light theme toggle
- Typing animation with Markdown formatting
- Copy-to-clipboard for any message
- One-click chat reset
- Suggestion prompt chips
- API key loaded from environment variables (never hardcoded)

---

## Tech Stack

**Frontend** — HTML5, CSS3 (custom theme system), Vanilla JavaScript, Font Awesome

**Backend** — Python, Flask, Google Gemini API (`google-genai`)

---

## Project Structure

```
luma-chatbot/
├── main.py              # Flask backend
├── templates/
│   └── index.html       # Chat UI
├── static/              # CSS and assets (optional)
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/luma-chatbot.git
cd luma-chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask google-genai
```

Or if you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API key

**macOS / Linux**
```bash
export GEMINI_API_KEY=your_api_key_here
```

**Windows (PowerShell)**
```powershell
setx GEMINI_API_KEY "your_api_key_here"
```

Restart your terminal after setting the variable.

### 5. Run the app

```bash
python main.py
```

Then open your browser at `http://localhost:2005`.

---

## Research Mode

Toggle Research Mode with the flask icon in the chat header. When active, the model's prompt template shifts to produce:

- Structured explanations with clear sections
- Technical depth appropriate to the topic
- Methodology and approach breakdowns
- Conclusions and identified limitations
- Analytical formatting throughout

---

## How It Works

Each request to `/chat`:

1. Receives the user's message and a `research_mode` flag
2. Selects the appropriate prompt template
3. Injects recent conversation context for continuity
4. Sends the composed prompt to the Gemini model
5. Returns the formatted response and stores it in short-term memory

---

## API Reference

**POST** `/chat`

**Request body**
```json
{
  "message": "Explain RAG architecture",
  "research_mode": true
}
```

**Response**
```json
{
  "reply": "Structured research-style answer..."
}
```

---

## Security

- API keys are never stored in source code
- Always use environment variables or a secrets manager
- If a key is accidentally exposed, rotate it immediately
- Do not commit `.env` files — add them to `.gitignore`

---

## Example Use Cases

- Exploring unfamiliar research topics
- Drafting literature review sections
- Breaking down technical concepts (AI/ML, systems, etc.)
- Planning experiments or study designs
- Generating structured summaries and reports

---

## Roadmap

- PDF research paper ingestion
- Automatic citation generation
- Live web search integration
- Multi-session chat management
- Vector-based long-term memory
- Paper summarization pipeline
- Dataset discovery and suggestion
- Export chat as PDF or Markdown
