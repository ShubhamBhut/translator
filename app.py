from flask import Flask, request, jsonify
from flask_caching import Cache
import requests
import os

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/kailorston/Fr-En"
HEADERS = {"Authorization": f"{os.getenv('HUGGING_FACE_API_TOKEN')}"}

app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_URL"] = os.getenv("REDIS_URL", "redis://localhost:6379/0")
cache = Cache(app)

class TranslationInput:
    def __init__(self, text):
        self.text = text

@app.route("/translate", methods=["POST"])
@cache.cached(timeout=60 * 60, key_prefix=lambda: request.get_json()["text"])  # Cache for 1 hour
def translate():

    data = request.get_json()
    text_input = TranslationInput(data.get("text"))

    payload = {"inputs": f"Translate from French to English: {text_input.text}"}

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        print(response)
        response.raise_for_status()
        translation = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error yo": str(e)}), 500

    return jsonify({"translation": translation[0]["generated_text"]})

if __name__ == "__main__":
    app.run(debug=True)
