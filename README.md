# Gestion de Prêts - Application Flask

## Description
Une application web Flask pour gérer les clients et les prêts. L'application permet d'ajouter des clients, d'enregistrer des prêts, et de consulter les listes de clients et de prêts.

## Fonctionnalités
- Ajouter un nouveau client.
- Enregistrer un nouveau prêt.
- Consulter la liste des clients.
- Consulter la liste des prêts.

## Prérequis
- Python 3.x
- Flask
- MySQL
- Bibliothèque `mysql-connector-python`
- dotenv `python-dotenv`

## Installation
1. Clonez ce dépôt :
   git clone https://github.com/25Abzo/GestionPret.git

## Créez un fichier .env à la racine du projet avec les informations de connexion à la base de données :
DB_HOST=localhost
DB_USER=user
DB_PASSWORD=password
DB_NAME=GestionPrêts

## Installer les paquets nécessaires
pip install -r requirements.txt

Lancez l'application Flask :
python app.py
