# This Python file uses the following encoding: utf-8
import requests
from bs4 import BeautifulSoup
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os
import time
from config import Config

Config = Config()

print(Config.INFLUX_ADDR)

client = InfluxDBClient(url=Config.INFLUX_ADDR, token=Config.INFLUX_TOKEN, org=Config.INFLUX_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)
#query_api = client.query_api()

bucketname=Config.INFLUX_BUCKET
orgname=Config.INFLUX_ORG
label_measurement=Config.LABEL_MEASUREMENT
label_temperature=Config.LABEL_TEMP
label_dewpoint=Config.LABEL_DEWPOINT
url=Config.WEATHER_URL
timer=int(Config.REPEAT_DELAY)


while True:
    response = requests.get(url)
    doc = BeautifulSoup(response.text, "html.parser")
    cells = doc.findAll('td')
    currentweather = str(cells[3])
    currentweather_split = currentweather.split()
    currentweather_split2 = currentweather_split[1].split('>')
    currentweather_split3 = currentweather_split2[2].split('°')
    local_temp = float(currentweather_split3[0])

    dewpointCell = str(cells[35])
    dewpointCell_split = dewpointCell.split('>')
    dewpointCell_split1 = dewpointCell_split[2].split('°')
    dewpoint = float(dewpointCell_split1[0])

    print("Temperature is " + str(local_temp) + "°C")
    print("Dewpoint is " + str(dewpoint) + "°C")

    try:
        write_api.write(bucket=bucketname, record=[{"measurement": label_measurement, "fields": {label_dewpoint: dewpoint, label_temperature: local_temp } } ])
    except Exception as e:
        print(e)

    time.sleep(timer)

