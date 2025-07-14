import grovepi
import time

# Sensor connected to digital port D4
DHT_PORT = 4
DHT_TYPE = 0  # 0 for blue sensor, 1 for white sensor

def read_dht_sensor():
    try:
        temperature, humidity = grovepi.dht(DHT_PORT, DHT_TYPE)
        return {
            "timestamp": time.ctime(),
            "temperature": temperature,
            "humidity": humidity
        }
    except IOError as e:
        return {
            "error": "Failed to read from DHT sensor",
            "message": str(e)
        }
