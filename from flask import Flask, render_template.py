from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyBkOKOWWH63YSOE7UMedZL4QM92EBT8OD8")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[types.Part.from_text(user_message)],
        config=types.GenerateContentConfig(
            temperature=0,
            top_p=0.95,
            top_k=20
        )
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True, port=2005)
