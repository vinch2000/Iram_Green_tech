"""
Module : controller.py
But : Contrôler les composants GPIO (LEDs, ventilateur) selon la température mesurée.
Utilisé sur Raspberry Pi.
"""

import RPi.GPIO as GPIO

# Définition des ports GPIO utilisés (mode BCM)
LED_ROUGE = 20
LED_JAUNE = 16
LED_VERTE = 13
LED_BLEUE = 19
VENTILATEUR = 26

def setup_gpio():
    """Initialise les ports GPIO en mode sortie (LEDs et ventilateur)."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in [LED_ROUGE, LED_JAUNE, LED_VERTE, LED_BLEUE, VENTILATEUR]:
        GPIO.setup(pin, GPIO.OUT)

def cleanup_gpio():
    """Remet à zéro les ports GPIO (utile à la fin du programme)."""
    GPIO.cleanup()

def control_outputs(temperature_c):
    """
    Allume ou éteint les LEDs et le ventilateur selon la température.
    Retourne une lettre qui indique l'état (R, J, V, '').
    """
    if temperature_c > 25:
        GPIO.output(VENTILATEUR, GPIO.HIGH)
        GPIO.output(LED_ROUGE, GPIO.HIGH)
        GPIO.output(LED_BLEUE, GPIO.HIGH)
        GPIO.output(LED_VERTE, GPIO.LOW)
        GPIO.output(LED_JAUNE, GPIO.LOW)
        return 'R'

    elif temperature_c > 21.25:
        GPIO.output(VENTILATEUR, GPIO.LOW)
        GPIO.output(LED_JAUNE, GPIO.HIGH)
        GPIO.output(LED_ROUGE, GPIO.LOW)
        GPIO.output(LED_BLEUE, GPIO.LOW)
        GPIO.output(LED_VERTE, GPIO.LOW)
        return 'J'

    elif temperature_c <= 20:
        GPIO.output(VENTILATEUR, GPIO.LOW)
        GPIO.output(LED_JAUNE, GPIO.LOW)
        GPIO.output(LED_ROUGE, GPIO.LOW)
        GPIO.output(LED_BLEUE, GPIO.LOW)
        GPIO.output(LED_VERTE, GPIO.LOW)
        return ''

    else:
        GPIO.output(VENTILATEUR, GPIO.LOW)
        GPIO.output(LED_VERTE, GPIO.HIGH)
        GPIO.output(LED_ROUGE, GPIO.LOW)
        GPIO.output(LED_BLEUE, GPIO.LOW)
        GPIO.output(LED_JAUNE, GPIO.LOW)
        return 'V'
