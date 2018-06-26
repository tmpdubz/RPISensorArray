# How to use the `*_sensor.py` scripts

Each of the sensor scripts will take in a pin number and return json encoded data for the relevant sensor.

* TODO: figure out wtf to do about python dependencies, ugh.
* TODO: make this OO with a sensor class
* TODO: Sensor class should implement a formatter for each different type of sensor
* TODO: be able to output json
* TODO: be able to stream json to a kafka consumer into a topic
* TODO: Rewrite this in a more sensible, safe language (golang has a fancy new RPi library)
	- This will require a golang rewrite of the DHT adafruit package