"""
Module : dht_reader.py
But : Lire les données de température et d'humidité à partir du capteur DHT22.
Utilisé uniquement sur Raspberry Pi.
"""

import adafruit_dht
import board

# Initialisation du capteur DHT22 connecté sur le pin GPIO 21 (D21)

dht_device = adafruit_dht.DHT22(board.D21, use_pulseio=False)

def read_dht_data():
    """
    Lecture des données du capteur DHT22.
    Retourne : température (°C), humidité (%), message d'erreur température, message d'erreur humidité
    """
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        temp_error = ""
        hum_error = ""
    except RuntimeError as sensor_error:
        temperature_c = 0.0
        humidity = 0.0
        temp_error = "Erreur lecture T°"
        hum_error = "Erreur lecture % Hum"
        print(f"[Capteur DHT] Erreur : {sensor_error}")

    return temperature_c, humidity, temp_error, hum_error
