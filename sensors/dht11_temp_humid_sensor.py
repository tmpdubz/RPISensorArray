import sys
import Adafruit_DHT
import argparse
import json

# Refer to the pin numbers by their pin number since BCM codes change between Pi versions.
# See https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
# GPIO.setmode(GPIO.BOARD)

def get_temperature(pin_to_circuit):
    temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_to_circuit)[1]
    return temperature


def get_humidity(pin_to_circuit):
    humidity = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_to_circuit)[0]
    return humidity

def main():
    parser = argparse.ArgumentParser("get temperature and humidity from DHT11 on pin")
    parser.add_argument('pin',
        help="GPIO.BOARD pin number connecting to the sensor circuit")
    args = parser.parse_args()
    data = {'humidity':get_humidity(args.pin), 'temperature':get_temperature(args.pin)}
    json_data = json.dumps(data)
    print("returning json encoded data:")
    print(json_data)
    return json_data

main()