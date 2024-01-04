from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)  # This will enable CORS for all routes. To disable CORS comment out this line.

@app.route('/')
def home():
    return "Hello, CORS-enabled world!"

if __name__ == "__main__":
    app.run(debug=True)