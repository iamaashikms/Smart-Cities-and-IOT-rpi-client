import grovepi

PIR_PORT = 3  # PIR sensor connected to digital port D3

def read_pir_sensor():
    try:
        grovepi.pinMode(PIR_PORT, "INPUT")  # Set PIR sensor pin as input
        motion = grovepi.digitalRead(PIR_PORT)

        if motion == 1:
            print("Motion detected!")
            return {"motion_detected": True}
        else:
            print("No motion detected.")
            return {"motion_detected": False}

    except IOError as e:
        return {
            "error": "Failed to read from PIR sensor",
            "message": str(e)
        }
