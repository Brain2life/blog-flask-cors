from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8000"}})  # Only allow requests from "http://127.0.0.1:8000/"

@app.route('/', methods=['GET'])
def home():
    return "Hello, CORS-configured world!"

if __name__ == "__main__":
    app.run(debug=True)