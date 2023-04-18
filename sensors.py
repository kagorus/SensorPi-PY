import adafruit_dht
import board
import time

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
    global tempReadings
    global humidityReadings

    if len(tempReadings) != 60:
        tempReadings.append(temperature_c)
        print(f"append attempted {len(tempReadings)}")
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


def dht_error():
    dhtDevice.exit()


def read_sensor():
    global temperature_c
    global humidity
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity


def take_readings(current_time):
    read_sensor()

    print(
        "Time: {} Raw: {}  Temp:  {:.1f} C    Humidity: {}%  Average Temp (hr): {:.1f}c  Average Humidity "
        "{:.1f}%  Temp Reading Count :  {}".format(current_time, temperature_c, temperature_c, humidity,
                                                   tempAverage, humidAverage, len(tempReadings)))
    append_readings()
