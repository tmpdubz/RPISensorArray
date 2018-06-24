import Adafruit_DHT
import argparse
import json

# Refer to the pin numbers by their pin number since BCM codes change between Pi versions.
# See https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
# GPIO.setmode(GPIO.BOARD)

def get_temperature(pin_to_circuit):
    print(Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_to_circuit))

def get_humidity(pin_to_circuit):
    Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_to_circuit)

def main():
    parser = argparse.ArgumentParser("get temperature and humidity from DHT11 on pin")
    parser.add_argument('pin',
        help="GPIO.BOARD pin number connecting to the sensor circuit")
    args = parser.parse_args()
    get_temperature(args.pin)
    get_humidity(args.pin)

    # data = {'humidity':get_humidity(args.pin), 'temperature':get_temperature(args.pin)}
    # json_data = json.dumps(data)
    # print("returning json encoded data:")
    # print(json_data)


main()