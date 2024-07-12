from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("es_core_news_md")

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        doc = nlp(data['text'])
        tokens = [{'text': token.text, 'lemma': token.lemma_, 'pos': token.pos_} for token in doc]

        return jsonify({"tokens": tokens})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
