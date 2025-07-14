import time
import sched

from messaging.publish_sensor_data import publish_sensor_data
from sensors.buzzer_sensor import activate_buzzer_sensor
from sensors.dht_sensor import read_dht_sensor
from sensors.led_sensor import activate_led_sensor
from sensors.pir_sensor import read_pir_sensor  # <-- You must have this implemented

# Create scheduler instance
scheduler = sched.scheduler(time.time, time.sleep)

# Time interval (in seconds) for checking
CHECK_INTERVAL = 5

def scheduled_task():
    print("Checking for motion and reading sensors...")

    # Check for motion
    motion_data = read_pir_sensor()
    if motion_data.get("motion_detected"):
        print("Motion detected! Activating buzzer.")
        activate_buzzer_sensor()
    else:
        print("No motion detected.")

    # Read and publish DHT sensor data
    dht_data = read_dht_sensor()
    publish_sensor_data(dht_data)
    print("DHT data published.")

    # Reschedule the task
    scheduler.enter(CHECK_INTERVAL, 1, scheduled_task)

def main():
    print("Starting scheduled data collection...")
    scheduler.enter(0, 1, scheduled_task)
    scheduler.run()

if __name__ == "__main__":
    main()
