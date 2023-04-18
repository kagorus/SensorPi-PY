import adafruit_dht
import board
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

# Temp/ Humidity Readings
humidity = 0
temperature_c = 0
tempReadings = []
humidityReadings = []
tempAverage = float(0)
humidAverage = float(0)

def append_readings():
    global tempAverage
    global humidAverage
    if len(tempReadings) != 60:
        tempReadings.append(temperature_c)
    else:
        del tempReadings[0]
        tempReadings.append(temperature_c)
    if len(humidityReadings) != 60:
        humidityReadings.append(humidity)
    else:
        del tempReadings[0]
        humidityReadings.append(humidity)
    tempAverage = sum(tempReadings) / len(tempReadings)
    humidAverage = sum(humidityReadings) / len(humidityReadings)