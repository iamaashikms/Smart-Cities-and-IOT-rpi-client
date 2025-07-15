import time
import sched
from datetime import datetime
from messaging.publish_sensor_data import publish_sensor_data
from sensors.buzzer_sensor import activate_buzzer_sensor
from sensors.dht_sensor import read_dht_sensor
from sensors.led_sensor import activate_led_sensor
from sensors.pir_sensor import read_pir_sensor

# Create scheduler instance
scheduler = sched.scheduler(time.time, time.sleep)

# Time intervals
CHECK_INTERVAL = 5             # Check every 5 seconds
DHT_PUBLISH_INTERVAL = 600     # Publish DHT data every 10 minutes
last_dht_publish_time = 0

motion_event = {
        "motion_detected": True,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
def scheduled_task():
    global last_dht_publish_time

    print("Checking for motion and reading sensors...")

    # Check for motion
    motion_data = read_pir_sensor()
    if motion_data.get("motion_detected"):
        print("Motion detected! Activating buzzer and publishing motion data.")
        activate_buzzer_sensor()
        publish_sensor_data(motion_event, "sensor.pir.environment")
    else:
        print("No motion detected.")

    current_time = time.time()
    if current_time - last_dht_publish_time >= DHT_PUBLISH_INTERVAL:
        # Read and publish DHT sensor data
        dht_data = read_dht_sensor()
        publish_sensor_data(dht_data, "sensor.dht.environment")
        last_dht_publish_time = current_time
        print("DHT data published.")
    else:
        print("DHT data not published yet (waiting for interval).")

    # Reschedule the task
    scheduler.enter(CHECK_INTERVAL, 1, scheduled_task)

def main():
    print("Starting scheduled data collection...")
    scheduler.enter(0, 1, scheduled_task)
    scheduler.run()

if __name__ == "__main__":
    main()
