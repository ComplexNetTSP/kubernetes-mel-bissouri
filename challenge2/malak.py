from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
   
    client_ip = request.host_url

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return f"""
    <h1>Bienvenue sur mon application Flask</h1>
    <ul>
        <li><strong>Nom:</strong> Malak</li>
        <li><strong>Nom du projet:</strong> Une simple application web</li>
        <li><strong>Version:</strong> V1</li>
        <li><strong>Hostname:</strong> {client_ip}</li>
        <li><strong>Date et Heure:</strong> {current_datetime}</li>
    </ul>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

