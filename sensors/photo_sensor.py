import RPi.GPIO as GPIO
import argparse
import json
import time

# Refer to the pin numbers by their pin number since BCM codes change between Pi versions.
# See https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BCM)

# rc_time gets the light level whenever it's called.
def rc_time(pin_to_circuit):
    count = 0

    # Output on the pin for 0.1 to reset
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

def main():
    parser = argparse.ArgumentParser("get temperature and humidity from photo-sensor RC circuit on pin")
    parser.add_argument('pin',
        help="GPIO.BCM pin number connecting to the sensor circuit")
    args = parser.parse_args()
    data = {'light_level': rc_time(args.pin)}
    json_data = json.dumps(data)
    print("returning json encoded data")
    print(json_data)
    return json_data

main()
