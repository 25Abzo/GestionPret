from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajouter_client_form')
def ajouter_client_form():
    return render_template('ajouter_client.html')

@app.route('/ajouter_client', methods=['POST'])
def ajouter_client():
    data = request.form
    nom = data['nom']
    prenom = data['prenom']
    adresse = data['adresse']
    statut = data['statut']

    cursor = db.cursor()
    sql = "INSERT INTO Client (Nom, Prénom, Adresse, Statut) VALUES (%s, %s, %s, %s)"
    values = (nom, prenom, adresse, statut)

    try:
        cursor.execute(sql, values)
        db.commit()
        return redirect(url_for('index'))
    except mysql.connector.Error as err:
        return f"Erreur lors de l'ajout du client: {err}"

@app.route('/enregistrer_pret_form')
def enregistrer_pret_form():
    return render_template('enregistrer_pret.html')

@app.route('/enregistrer_pret', methods=['POST'])
def enregistrer_pret():
    data = request.form
    id_client = data['id_client']
    montant = data['montant']
    taux = data['taux']
    duree = data['duree']
    mensualite = data['mensualite']
    date_accord = data['date_accord']
    jour_exigibilite = data['jour_exigibilite']

    cursor = db.cursor()

    # Vérifier si l'ID_Client existe
    sql_check = "SELECT ID_Client FROM Client WHERE ID_Client = %s"
    cursor.execute(sql_check, (id_client,))
    result = cursor.fetchone()

    if result is None:
        return "ID_Client n'existe pas. Veuillez d'abord ajouter le client."

    sql = "INSERT INTO Prêt (ID_Client, Montant, Taux, Durée, Mensualité, Date_Accord, Jour_Exigibilité) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (id_client, montant, taux, duree, mensualite, date_accord, jour_exigibilite)

    try:
        cursor.execute(sql, values)
        db.commit()
        return redirect(url_for('confirmation'))
    except mysql.connector.Error as err:
        return f"Erreur lors de l'enregistrement du prêt: {err}"

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/liste_clients')
def liste_clients():
    cursor = db.cursor()
    sql = "SELECT ID_Client, Nom, Prénom, Adresse, Statut FROM Client"
    cursor.execute(sql)
    clients = cursor.fetchall()
    return render_template('liste_clients.html', clients=clients)

@app.route('/liste_prets')
def liste_prets():
    cursor = db.cursor()
    sql = "SELECT Prêt.ID_Prêt, Client.Nom, Client.Prénom, Prêt.Montant, Prêt.Taux, Prêt.Durée, Prêt.Mensualité, Prêt.Date_Accord, Prêt.Jour_Exigibilité FROM Prêt JOIN Client ON Prêt.ID_Client = Client.ID_Client"
    cursor.execute(sql)
    prets = cursor.fetchall()
    return render_template('liste_prets.html', prets=prets)

if __name__ == '__main__':
    app.run(debug=True)
