from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)



client = genai.Client(api_key="")


# simple in-memory chat history (per server run)
chat_history = []

RESEARCH_SYSTEM_PROMPT = """
You are an advanced research assistant.

Rules:
- Answer with structured reasoning
- Be precise and technical when useful
- When topic is analytical → break into sections
- When helpful → include:
  • Key Concepts
  • Methodology
  • Findings
  • Limitations
  • Conclusion
- Prefer depth over brevity
- Avoid fluff
"""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    research_mode = data.get("research_mode", False)

    try:

        # Build prompt with memory
        context_block = "\n".join(chat_history[-6:])  # last turns only

        if research_mode:
            final_prompt = f"""
{RESEARCH_SYSTEM_PROMPT}

Conversation Context:
{context_block}

User Question:
{user_message}

Respond as a research report.
"""
        else:
            final_prompt = f"""
Context:
{context_block}

User:
{user_message}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=final_prompt
        )

        reply = response.text

        # store memory
        chat_history.append(f"User: {user_message}")
        chat_history.append(f"Assistant: {reply}")

        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": str(e)}), 500


@app.route('/reset', methods=['POST'])
def reset():
    chat_history.clear()
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True, port=2005)
