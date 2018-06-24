import Adafruit_DHT
import argparse
import json


def get_humidity(pin_to_circuit):
    return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_to_circuit)[0]


def get_temperature(pin_to_circuit):
    return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_to_circuit)[1]


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