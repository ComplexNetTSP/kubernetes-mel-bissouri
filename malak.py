from flask import Flask, request, render_template_string
from datetime import datetime
from pymongo import MongoClient

# Configuration de l'application Flask
app = Flask(__name__)

# Configuration de MongoDB avec un nouveau nom de base de données
client = MongoClient("mongodb://admin:password@mongodb:27017/")
db = client["database_challenge3"]  # Nouveau nom de la base de données
collection = db["records"]

@app.route("/")
def home():
    # Informations de l'utilisateur et de la requête
    client_ip = request.remote_addr
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Enregistrement dans la base de données MongoDB
    record = {
        "ip_address": client_ip,
        "date": current_datetime
    }
    collection.insert_one(record)

    # Récupérer les 10 derniers enregistrements
    last_10_records = list(collection.find().sort([('_id', -1)]).limit(10))

    # Affichage des résultats
    return render_template_string("""
    <h1>Bienvenue sur mon application Flask - Version V2</h1>
    <ul>
        <li><strong>Nom:</strong> Malak</li>
        <li><strong>Nom du projet:</strong> Flask + MongoDB App</li>
        <li><strong>Version:</strong> V2</li>
        <li><strong>Hostname:</strong> {{ hostname }}</li>
        <li><strong>Date et Heure:</strong> {{ current_datetime }}</li>
    </ul>
    <h2>Derniers 10 enregistrements:</h2>
    <ul>
        {% for record in last_10_records %}
            <li>{{ record["ip_address"] }} - {{ record["date"] }}</li>
        {% endfor %}
    </ul>
    """, hostname=request.host_url, current_datetime=current_datetime, last_10_records=last_10_records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

