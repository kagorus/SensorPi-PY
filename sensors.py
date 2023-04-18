import adafruit_dht
import board
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)


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

def dht_error():
    dhtDevice.exit()

def take_readings():
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity
    append_readings()
    print(
          "Time: {} Raw: {}  Temp:  {:.1f} C    Humidity: {}%  Average Temp (hr): {:.1f}c  Average Humidity "
          "{:.1f}%  Temp Reading Count :  {}".format(current_time, temperature_c, temperature_c, humidity,
                tempAverage, humidAverage, len(tempReadings)))
 