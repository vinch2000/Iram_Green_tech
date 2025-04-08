"""
Module : logger.py
But : Gérer les fichiers CSV (création, écriture, archivage)
"""

import csv
import os
from datetime import datetime
import shutil

# Chemins de base

BASE_DIR = "data/records"
ARCHIVE_DIR = "data/archive"

def create_csv_file():
    """
    Crée un nouveau fichier CSV toutes les 15 secondes.
    Le nom est basé sur le groupe 'E' + horodatage.
    Retourne le chemin complet et le nom du fichier.
    """
    # Création des répertoires si nécessaire

    os.makedirs(BASE_DIR, exist_ok=True)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"E{now}.csv"
    filepath = os.path.join(BASE_DIR, filename)

    with open(filepath, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "rlog_filename", "rlog_grp", "rlog_id", "rlog_timestamp", "rlog_temp",
            "rlog_temp_sensor", "rlog_temp_error",
            "rlog_hum", "rlog_hum_sensor", "rlog_hum_error"
        ])

    print(f" Nouveau fichier CSV créé : {filepath}")
    return filepath, filename

def append_data(csv_path, rlog_filename, rlog_grp, rlog_id, timestamp,
                temperature_c, rlog_temp_sensor, temp_error,
                humidity, rlog_hum_sensor, hum_error):
    """
    Ajoute une ligne de données dans le fichier CSV courant.

    """
    with open(csv_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            rlog_filename,
            rlog_grp,
            rlog_id,
            timestamp,
            temperature_c,
            rlog_temp_sensor,
            temp_error,
            humidity,
            rlog_hum_sensor,
            hum_error
        ])

def archive_old_file(csv_path):
    """
    Déplace le fichier CSV actif vers le répertoire d’archives.
    """
    if os.path.exists(csv_path):
        filename = os.path.basename(csv_path)
        archive_path = os.path.join(ARCHIVE_DIR, filename)
        shutil.move(csv_path, archive_path)
        print(f" Fichier archivé : {archive_path}")
