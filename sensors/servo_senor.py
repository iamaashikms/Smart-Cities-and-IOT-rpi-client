import grovepi
import time

# Servo connected to digital port D5
SERVO_PORT = 5
grovepi.pinMode(SERVO_PORT, "OUTPUT")


def move_servo(angle):
    """Move servo to a specific angle."""
    grovepi.analogWrite(SERVO_PORT, angle)


def move_servo_to_180():
    """Smoothly move servo from current position to 180°."""
    print("Moving servo to 180° smoothly...")
    for angle in range(0, 181, 5):
        move_servo(angle)
        time.sleep(0.05)


def move_servo_to_0():
    """Smoothly move servo from current position to 0°."""
    print("Moving servo to 0° smoothly...")
    for angle in range(180, -1, -5):
        move_servo(angle)
        time.sleep(0.05)
