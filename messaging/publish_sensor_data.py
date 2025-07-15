from messaging.publisher import publish_message


def publish_sensor_data(data, topic):
    if topic == "sensor.dht.environment":
        msg = "{} | DHT Temp = {}°C, Humidity = {}%".format(
            data['timestamp'], data['temperature'], data['humidity']
        )
        publish_message(topic, msg)
    elif topic == "sensor.pir.environment":
        msg = "{} | Motion Detected = {}".format(
            data.get('timestamp', 'N/A'), data.get('motion_detected')
        )
        publish_message(topic, msg)
    else:
        msg = "{} | Data: {}".format(
            data.get('timestamp', 'N/A'), data
        )
        publish_message(topic, msg)

    print("Publishing to {}: {}".format(topic, msg))
