"""
Module : db.py
But : Connexion à la base PostgreSQL et appel de la procédure stockée load_csv.
"""
import os
from dotenv import load_dotenv
import psycopg

# Paramètres de connexion à la base de données PostgreSQL
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def call_stored_procedure(csv_path):
    """
    Appelle la procédure stockée 'load_csv' en lui passant le chemin du fichier CSV.
    """
    try:
        conn = psycopg.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        cursor.callproc('load_csv', [csv_path])
        conn.commit()
        cursor.close()
        conn.close()
        print(f" Données envoyées via la procédure stockée : {csv_path}")
    except psycopg.DatabaseError as e:
        print(f"[ERREUR BDD] {e}")
    except Exception as e:
        print(f"[ERREUR GÉNÉRALE] {e}")
