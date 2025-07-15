import time
import sched
import threading
from datetime import datetime
from messaging.publisher import publish_message
from messaging.subscriber import start_subscriber
from sensors.buzzer_sensor import activate_buzzer_sensor
from sensors.dht_sensor import read_dht_sensor
from sensors.led_sensor import activate_led_sensor
from sensors.pir_sensor import read_pir_sensor
from sensors.buzzer_sensor import activate_buzzer_sensor, deactivate_buzzer_sensor
# Create scheduler instance
scheduler = sched.scheduler(time.time, time.sleep)

# Time interval
CHECK_INTERVAL = 5  # Check every 5 seconds


def scheduled_task():
    print("\n[{}] Running scheduled task...".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # Read PIR sensor
    pir_data = read_pir_sensor()
    motion_detected = pir_data.get("motion_detected", False)

    # Read DHT sensor
    dht_data = read_dht_sensor()
    temperature = dht_data.get("temperature")
    humidity = dht_data.get("humidity")

    # Buzzer activation
    buzzer_activated = False
    if motion_detected:
        print("Motion detected! Activating buzzer.")
        activate_buzzer_sensor()
        buzzer_activated = True
    else:
        print("No motion detected.")

    # Build combined payload
    combined_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "motion_detected": motion_detected,
        "temperature": temperature,
        "humidity": humidity,
        "buzzer_activated": buzzer_activated
    }

    # Publish combined data
    publish_message( "sensor.environment",combined_data)
    print("Published combined sensor data to 'sensor.environment'.")

    # Reschedule task
    scheduler.enter(CHECK_INTERVAL, 1, scheduled_task)
def handle_alert(ch, method, body):
    try:
        print("Received alert message:", body.decode())
        alert_data = json.loads(body.decode())

        if alert_data.get("alert") == "high_humidity_alert":
            print("High humidity alert received. Activating buzzer in pattern.")

            def buzzer_pattern():
                for _ in range(4):
                    activate_buzzer_sensor()
                    time.sleep(1)
                    deactivate_buzzer_sensor()
                    time.sleep(1)

            # Run the buzzer pattern in a separate thread so publishing is not blocked
            threading.Thread(target=buzzer_pattern, daemon=True).start()

    except json.JSONDecodeError:
        print("Invalid alert data received:", body.decode())
def main():
    print("Starting scheduled sensor data collection and alert listener...")
    # Start alert subscriber in a separate thread
    threading.Thread(target=lambda: start_subscriber("sensor.alert", handle_alert), daemon=True).start()
    # Start the scheduled sensor publishing
    scheduler.enter(0, 1, scheduled_task)
    scheduler.run()

if __name__ == "__main__":
    main()
