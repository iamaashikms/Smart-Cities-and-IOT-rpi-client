def publish_sensor_data(data, topic):
    if topic == "sensor.dht.environment":
        msg = "{} | DHT Temp = {}°C, Humidity = {}%".format(
            data['timestamp'], data['temperature'], data['humidity']
        )
    elif topic == "sensor.pir.environment":
        msg = "{} | Motion Detected = {}".format(
            data.get('timestamp', 'N/A'), data.get('motion_detected')
        )
    else:
        msg = "{} | Data: {}".format(
            data.get('timestamp', 'N/A'), data
        )

    print("Publishing to {}: {}".format(topic, msg))
