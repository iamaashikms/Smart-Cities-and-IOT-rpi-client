
from messaging.publish_sensor_data import publish_sensor_data
from sensors.buzzer_sensor import activate_buzzer_sensor
from sensors.dht_sensor import read_dht_sensor
from sensors.led_sensor import activate_led_sensor


# === Fetch and publish everything ===
def main():
    print("Starting data collection...")
    # Read from DHT sensor
    dht_data = read_dht_sensor() 
    activate_buzzer_sensor()
    activate_led_sensor()   
    publish_sensor_data(dht_data)
    print("DHT data published.")
if __name__ == "__main__":
    main()
