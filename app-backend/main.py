
import os
from flask import Flask, jsonify

app = Flask(__name__)
# Variable d'environnement pour le versionnement (CI/CD)
VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Données du backend", "version": VERSION})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

