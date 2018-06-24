import RPi.GPIO as GPIO
import time

# Refer to the pin numbers by their pin number since BCM codes change between Pi versions.
# See https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setmode(GPIO.BOARD)
# TODO: make this configurable based on a parameter you pass in.
sensor_pin_to_citcuit = 40

def rc_time (pin_to_circuit):
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

# Catch interrupt and cleanup
try:
	while True:
		print(rc_time(sensor_pin_to_citcuit))
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()