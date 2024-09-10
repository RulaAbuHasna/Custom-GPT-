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
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    if not openai.api_key:
        return jsonify({'error': 'OpenAI API key not set'}), 500

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100,
        )

        return jsonify({
            'response': response.choices[0].text.strip()
        })

    except openai.error.OpenAIError as e:
        return jsonify({'error': f'OpenAI API error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
