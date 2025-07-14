from messaging.publisher import publish_message


def publish_sensor_data(dht_data):
    # --- DHT Sensor Data ---
    print("DHT data fetched:", dht_data)
    if "error" not in dht_data:
        msg = "{} | DHT Temp = {}°C, Humidity = {}%".format(dht_data['timestamp'], dht_data['temperature'], dht_data['humidity'])
        publish_message("sensor.dht.environment", msg)
    else:
        print(" DHT sensor error:", dht_data["error"])
