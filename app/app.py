from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import openai
import os

app = Flask(__name__)
socketio = SocketIO(app)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat-gpt', methods=['POST'])
def chat_gpt_http():
    data = request.json
    message = data.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}],
            max_tokens=200
        )
        gpt_response = response['choices'][0]['message']['content'].strip()
        return jsonify({'response': gpt_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}],
            max_tokens=200
        )
        gpt_response = response['choices'][0]['message']['content'].strip()
        emit('response', {'data': gpt_response})
    except Exception as e:
        emit('response', {'error': str(e)})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
