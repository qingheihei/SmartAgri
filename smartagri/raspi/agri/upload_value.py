from get_TempHumid import SHT35
from get_CO2 import UART
from get_Light import TSL2591
from get_ADConverter import getSoilTemp,getSoilEC,getSoilWater,getSolar
import time
import requests
import json
from raspi_define import *

URL = "http://13.230.81.113:8888/api/v1/sensorvalues/"
headers = {
    "User-Agent":"curl/7.41.1",
    "Content-Type": "application/json", }

def data_post(data):
    res = requests.post(url=URL,data=json.dumps(data), headers=headers)
    print("post result:",res.text)

def initialize_sensor():
    mySHT35 = SHT35()
    mySHT35.setUp()
    tsl = TSL2591()
    myuart = UART()
    return mySHT35, tsl, myuart

def get_value(mySHT35, tsl, myuart):    
    # get air temp&humid value
    ari_temp,air_humid = mySHT35.getValue()
    # get co2 value from uart
    air_co2 = myuart.receive_uart()
    air_light = tsl.get_value()
    #get analog sensor value from MCP3208 via SPI
    air_solar = getSolar()
    soil_temp = getSoilTemp()
    soil_ec = getSoilEC()
    soil_water = getSoilWater()
    return ari_temp, air_humid, air_co2, air_light, air_solar, soil_temp, soil_ec, soil_water

def main():
    mySHT35, tsl, myuart = initialize_sensor()
    
    ari_temp,air_humid,air_co2,air_light, air_solar, soil_temp, soil_ec, soil_water = get_value(mySHT35, tsl, myuart)

    data = {"value":ari_temp,
            "unit":"degree",
            "sensor_id":AIR_TEMP_ID,
            }
    data_post(data)
        
    data = {"value":air_humid,
            "unit":"percent",
            "sensor_id":AIR_HUMID_ID,
            }
    data_post(data)

    data = {"value":air_co2,
            "unit":"ppm",
            "sensor_id":AIR_CO2_ID,
            }
    data_post(data)

    data = {"value":air_light,
            "unit":"lux",
            "sensor_id":AIR_LIGHT_ID,}
    data_post(data)

    data = {"value":air_solar,
            "unit":"kW/㎡",
            "sensor_id":AIR_SOLAR_ID,}
    data_post(data)

    data = {"value":soil_temp,
            "unit":"degree",
            "sensor_id":SOIL_TEMP_ID,
            }
    data_post(data)

    data = {"value":soil_ec,
            "unit":"mS/cm",
            "sensor_id":SOIL_EC_ID,
            }
    data_post(data)

       
    data = {"value":soil_water,
            "unit":"percent",
            "sensor_id":SOIL_WATER_ID,
            }
    data_post(data)

if __name__ == '__main__':
    main()
