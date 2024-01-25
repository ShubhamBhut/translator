# Transormer based Flask Translation API with Caching

This is a Flask API that translates text from French to English using the Hugging Face translation model. The API supports caching using Redis to improve response times.

## Setup

### Prerequisites

- Python (version 3.6 or higher)
- Redis Server

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flask-huggingface-translation.git
   cd flask-huggingface-translation
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Redis Installation and Setup

#### Install Redis

#### Start Redis Server

- **Linux / Mac:**
  ```bash
  redis-server
  ```

### Configuration

1. Set up a Hugging Face account and obtain an API token.
2. Start the Redis server on your machine.

### Environment Variables

Create a `.env` file in the project root with the following content:

```env
HUGGING_FACE_API_TOKEN=your_hugging_face_api_token
REDIS_URL=redis://localhost:6379/0
```

Replace `your_hugging_face_api_token` with your actual Hugging Face API token.

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

   The app will be accessible at `http://127.0.0.1:5000/`.

2. Make a POST request to `/translate` with the text to be translated:

   Example using `curl`:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "Bonjour, comment allez-vous?"}' http://127.0.0.1:5000/translate
   ```

   Example using ThunderClient in Visual Studio Code:

   ```http
   POST http://127.0.0.1:5000/translate
   Content-Type: application/json

   {
     "text": "Le chat noir a couru à travers le jardin et a sauté sur le muret en pierre"
   }
   ```

   Output:
   ```
   {
     "translation": "\"The black cat has run through the garden and has jumped on the stone wall."
   }
   ```

3. The API will respond with the translated text.

## Caching

The API supports caching using Redis to improve response times. Translations are cached for 1 hour.

## Contributing

Feel free to contribute to the project by opening issues or pull requests.
