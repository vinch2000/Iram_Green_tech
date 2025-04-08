"""
Module : main.py
But : Script principal du projet IRAM Green Tech.
Rôle : Lance le processus complet de lecture des capteurs, contrôle des GPIO, enregistrement des données CSV et envoi à PostgreSQL.
"""




import time
from datetime import datetime
from sensors.dht_reader import read_dht_data
from gpio_control.controller import update_gpio_state
from data_handler.logger import create_new_csv, append_data, archive_old_file
from data_handler.db import call_stored_procedure

# === Variables de configuration ===
INTERVAL = 15  # Intervalle entre chaque mesure (en secondes)

# === Identifiant du groupe
rlog_grp = 'E'  # Nom du groupe (ex. Groupe E)

# === Identifiant unique du Raspberry Pi (fixe pour chaque poste)
rlog_id = 5  # Par exemple, Raspberry du groupe E => id 5

# === Capteurs utilisés (fixes, sauf si erreur détectée)
rlog_temp_sensor = 'V'  # V = Valeur OK / R = Rouge / J = Jaune
rlog_hum_sensor = 'V'   # Valeur par défaut

def main():

    print("\n Démarrage du contrôle des capteurs (Ctrl+C pour arrêter)...")

    try:
        while True:
            # Horodatage actuel
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 1. Lecture du capteur DHT22 (température & humidité)
            temperature_c, humidity, temp_error, hum_error = read_dht_data()

            # 2. Gestion des LEDs & ventilateur en fonction de la température
            global rlog_temp_sensor
            rlog_temp_sensor = update_gpio_state(temperature_c)

            # 3. Création d'un nouveau fichier CSV avec un nom basé sur la date/heure
            csv_path, rlog_filename = create_new_csv()

            # 4. Ajout des données dans le fichier CSV
            append_data(
                csv_path,
                rlog_filename,       # Nom unique du fichier = groupe + timestamp
                rlog_grp,            # Groupe (fixe)
                rlog_id,             # Identifiant du poste Raspberry (fixe)
                timestamp,           # Date/heure de la mesure
                temperature_c,
                rlog_temp_sensor,
                temp_error,
                humidity,
                rlog_hum_sensor,
                hum_error
            )

            # 5. Envoi des données à la base PostgreSQL via la procédure
            call_stored_procedure(csv_path)

            # 6. Archivage de l'ancien fichier CSV (si un nouveau est créé)
            archive_old_file()
            # Mon erreur dans le code precedant mais garde pour montrer
            # Incrémentation possible si on veut suivre le nombre de lignes (non obligatoire si rlog_id est fixe)
            # rlog_id += 1

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\n Arrêt du programme par l'utilisateur.")

# === Point d'entrée ===
if __name__ == "__main__":
    main()
