import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/custom-gpt', methods=['POST'])
def custom_gpt():
    data = request.json
    if data is None:
        return jsonify({'error': 'No data provided'}), 400
    messages = data.get('messages', '')

    if not messages:
        return jsonify({'error': 'No messages provided'}), 400

    if not openai.api_key:
        return jsonify({'error': 'OpenAI API key not set'}), 500

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=messages,
            max_tokens=200  # Increased to allow for more detailed responses
        )

        return jsonify({
            'response': response['choices'][0]['message']['content'].strip()
        })

    except openai.error.OpenAIError as e:
        return jsonify({'error': f'OpenAI API error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
