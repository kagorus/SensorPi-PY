import adafruit_dht
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

# Temp/ Humidity Readings
humidity = 0
temperature_c = 0
tempReadings = []
humidityReadings = []
tempAverage = float(0)
humidAverage = float(0)