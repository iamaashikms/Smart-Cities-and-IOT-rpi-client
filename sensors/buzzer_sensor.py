import grovepi
import time

BUZZER_PORT = 3    # Buzzer connected to digital port D2

def activate_buzzer_sensor():
    try:
        # Activate buzzer for 2 seconds
        grovepi.pinMode(BUZZER_PORT, "OUTPUT")
        grovepi.digitalWrite(BUZZER_PORT, 1)
        print("Buzzer activated")

    except IOError as e:
        return {
            "error": "Failed to read from DHT sensor or control buzzer",
            "message": str(e)
        }

def deactivate_buzzer_sensor():
    try:
        # Activate buzzer for 2 seconds
        grovepi.pinMode(BUZZER_PORT, "OUTPUT")
        grovepi.digitalWrite(BUZZER_PORT, 0)
        print("Buzzer deactivated.")

    except IOError as e:
        return {
            "error": "Failed to read from DHT sensor or control buzzer",
            "message": str(e)
        }


def beep_buzzer_sensor():
    try:
        # Activate buzzer for 2 seconds
        grovepi.pinMode(BUZZER_PORT, "OUTPUT")
        print("Beep deactivated.")
        grovepi.digitalWrite(BUZZER_PORT, 1)
        time.sleep(2)
        grovepi.digitalWrite(BUZZER_PORT, 0)
        time.sleep(2)
        print("Beep deactivated.")

    except IOError as e:
        return {
            "error": "Failed to read from DHT sensor or control buzzer",
            "message": str(e)
        }