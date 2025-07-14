import grovepi
import time

LED_PORT = 2   # Buzzer connected to digital port D2

def activate_led_sensor():
    try:
        # Activate buzzer for 2 seconds
        grovepi.pinMode(LED_PORT, "OUTPUT")
        grovepi.digitalWrite(LED_PORT, 0)#
        print("Buzzer activated for 2 seconds.")
        time.sleep(2)
        grovepi.digitalWrite(LED_PORT, 0)#

    except IOError as e:
        return {
            "error": "Failed to read from DHT sensor or control buzzer",
            "message": str(e)
        }
