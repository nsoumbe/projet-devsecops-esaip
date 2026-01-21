import os
import requests
from flask import Flask

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend-service:5000")

@app.route('/')
def index():
    try:
        r = requests.get(f"{BACKEND_URL}/api/data")
        return f"Frontend v1 - Réponse : {r.text}"
    except:
        return "Erreur : Backend injoignable"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
