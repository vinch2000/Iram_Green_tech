# Projet : Surveillance Température et Humidité - Raspberry Pi

## Description
Ce projet a pour but de surveiller la température et l'humidité à l'aide d'un capteur DHT22 branché sur un Raspberry Pi.
Il permet d'activer un ventilateur et des LEDs en fonction des mesures prises.
Les données sont :
- écrites dans un fichier CSV (toutes les 15 secondes)
- envoyées automatiquement dans une base de données PostgreSQL via une procédure stockée
- archivées pour consultation ultérieure

---

##  Structure des dossiers
```
Iram_Green_Tech/
├── main.py                         # Point d'entrée principal du programme
├── sensors/
│   ├── __init__.py
│   └── dht_reader.py              # Lecture des données du capteur DHT22
├── gpio_control/
│   ├── __init__.py
│   └── controller.py              # Contrôle des LEDs et du ventilateur
├── data_handler/
│   ├── __init__.py
│   ├── logger.py                  # Gestion des fichiers CSV
│   └── db.py                      # Envoi des données dans la BDD PostgreSQL
├── data/
│   ├── records/                   # Contient le fichier CSV actif
│   └── archive/                   # Contient les fichiers CSV archivés
├── requirements.txt              # Librairies minimales (utilisables sur Windows)
├── requirements-rpi.txt          # Librairies complètes pour Raspberry Pi
```

---

## Installation

### Sur Raspberry Pi (recommandé)
```bash
sudo apt update && sudo apt install python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-rpi.txt
```

### Sur un PC (lecture du code uniquement, pas d'exécution GPIO)
```bash
pip install -r requirements.txt
```

---

## ✅ Utilisation
```bash
python main.py
```
Le script :
- crée un nouveau fichier CSV toutes les 15 secondes
- ajoute les données lues du capteur dans ce fichier
- appelle la procédure PostgreSQL `load_csv(<chemin_du_fichier>)`
- archive l'ancien fichier CSV

---

## Explication simple pour les étudiants

### Modules clés :
- `dht_reader.py` : lit les données du capteur (température et humidité)
- `controller.py` : allume ou éteint les LEDs et le ventilateur selon la température
- `logger.py` : crée un fichier CSV, ajoute les mesures, archive l'ancien
- `db.py` : envoie les données dans PostgreSQL avec une procédure stockée

### Bibliothèques importantes :
- `adafruit-circuitpython-dht` : pour le capteur DHT22 (version moderne)
- `board` : pour utiliser les pins du Raspberry Pi (ex. `board.D21`)
- `RPi.GPIO` : pour contrôler les ports GPIO
- `psycopg` : pour se connecter à PostgreSQL en Python

### Point d'explication suplémentaire après vérrification des bibliothèques
### Pourquoi on n'utilise pas `adafruit_python_dht==1.4.0` ?
> Ce paquet est une ancienne version écrite en C, difficile à installer et non maintenue.  
> On préfère `adafruit-circuitpython-dht` qui est en Python pur, facile à installer, compatible `board`, et évolutif pour tous les projets modernes.

---

##  Objectif éducatif
Ce projet permet d'apprendre :
- l'utilisation de capteurs avec le Raspberry Pi
- la programmation modulaire Python (plusieurs fichiers)
- la gestion de fichiers CSV
- la connexion à une base PostgreSQL
- la bonne structure d'un projet professionnel simple

---

Créé avec Coeur pour l'équipe éducative Iram Green Tech 


**Vincent Dubuisson – INF.B**


---



