import grovepi
import time

BUZZER_PORT = 2    # Buzzer connected to digital port D2

def activate_buzzer_sensor():
    try:
        # Read temperature and humidity from DHT sensor


        # Activate buzzer for 2 seconds
        grovepi.pinMode(BUZZER_PORT, "OUTPUT")
        grovepi.digitalWrite(BUZZER_PORT, 1)
        print("Buzzer activated for 5 seconds.")
        time.sleep(5)
        grovepi.digitalWrite(BUZZER_PORT, 0)#

    except IOError as e:
        return {
            "error": "Failed to read from DHT sensor or control buzzer",
            "message": str(e)
        }
