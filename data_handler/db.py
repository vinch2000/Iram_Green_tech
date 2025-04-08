"""
Module : db.py
But : Connexion à la base PostgreSQL et appel de la procédure stockée load_csv.
"""

import psycopg

# Paramètres de connexion à la base de données PostgreSQL
DB_HOST = "172.20.2.200"
DB_PORT = "5432"
DB_NAME = "tbl_log_raspberry"
DB_USER = "jpo2025"
DB_PASS = "jpo2025"

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
