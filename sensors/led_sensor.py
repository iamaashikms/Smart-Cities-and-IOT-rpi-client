import grovepi
import time

# LED connected to digital port D4 (example)
LED_PORT = 6
grovepi.pinMode(LED_PORT, "OUTPUT")


def initialize_led_off():
    """Ensure the LED is OFF when starting the program."""
    grovepi.digitalWrite(LED_PORT, 0)
    
    print("LED initialized to OFF.")


def turn_led_on():
    """Turn the LED ON."""
    grovepi.digitalWrite(LED_PORT, 1)
    time.sleep(250)
    print("LED turned ON.")


def turn_led_off():
    """Turn the LED OFF."""
    grovepi.digitalWrite(LED_PORT, 0)
    time.sleep(250)
    print("LED turned OFF.")
