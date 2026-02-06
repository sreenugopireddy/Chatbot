# 🧠 Luma — AI Research Chatbot (Flask + Gemini)

Luma is a web-based AI chatbot built using **Flask** and **Google Gemini API**.  
It provides conversational answers and can be switched into **Research Mode** to generate structured, analytical, report-style responses.

The project includes a modern chat UI and a backend research assistant engine with contextual memory.

---

## 🚀 Features

- 💬 Real-time AI chat interface
- 🔬 Research Mode for structured, in-depth answers
- 🧠 Multi-turn conversation memory
- 🎨 Dark / Light theme toggle
- ⌨️ Typing animation + markdown formatting
- 📋 Copy message support
- 🧹 One-click chat reset
- 🧩 Suggestion prompts
- 🔒 API key via environment variables (secure)

---

## 🏗️ Tech Stack

**Frontend**
- HTML5
- CSS3 (custom theme system)
- Vanilla JavaScript
- Font Awesome icons

**Backend**
- Python
- Flask
- Google Gemini API (`google-genai`)

---

## 📂 Project Structure

Chatbot/
│
├── main.py # Flask backend server
├── templates/
│ └── index.html # Chat UI
├── static/ # (optional) CSS / assets
├── README.md
└── requirements.txt


---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/luma-chatbot.git
cd luma-chatbot
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
3️⃣ Install Dependencies
pip install flask google-genai
(or use requirements.txt if you create one)

4️⃣ Set Gemini API Key
Create environment variable:

Windows PowerShell

setx GEMINI_API_KEY "YOUR_API_KEY"
Mac/Linux

export GEMINI_API_KEY=YOUR_API_KEY
Restart terminal after setting.

5️⃣ Run App
python main.py
Open browser:

http://localhost:2005
🔬 Research Mode
Research Mode changes the model prompt behavior to produce:

structured explanations

technical depth

methodology sections

conclusions

limitations

analytical formatting

Toggle Research Mode using the flask icon button in the chat header.

🧠 Backend Logic Overview
The chatbot backend:

receives user message via /chat endpoint

optionally activates research prompt template

injects recent conversation context

sends structured prompt to Gemini model

returns formatted response

stores short conversation memory

📡 API Endpoint
POST /chat
Request

{
  "message": "Explain RAG architecture",
  "research_mode": true
}
Response

{
  "reply": "Structured research-style answer..."
}
🔒 Security Notes
API keys are not stored in source code

Use environment variables

If a key is ever exposed → rotate immediately

Do not commit .env files

🧪 Example Use Cases
Research topic exploration

Literature review drafts

Technical concept breakdown

Experiment planning

AI/ML explanations

Structured report generation

🛠️ Future Improvements
Planned upgrades:

PDF research paper reader

citation generator

web search integration

multi-chat sessions

vector memory store

paper summarization

dataset suggestion engine

export chat to PDF/Markdown

