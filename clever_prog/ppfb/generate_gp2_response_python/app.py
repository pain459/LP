from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model = pipeline("text-generation", model="gpt2")


@app.route('/generate', methods=['POST'])
def generate_text():
    user_input = request.json.get('input')

    if not user_input:
        return jsonify({'error': 'Please provide "input" in the request body'}), 400

    sentences = model(user_input,
                      do_sample=True, top_k=50,
                      temperature=0.9, max_length=100,
                      num_return_sequences=2)

    generated_texts = [sentence["generated_text"] for sentence in sentences]

    return jsonify({'generated_text': generated_texts})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
