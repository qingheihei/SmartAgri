from get_TempHumid import SHT35
from get_CO2 import UART
from get_Soil_Arduino import read_serial
import time
import requests
import json

AIR_TEMP_ID = 1
AIR_HUMID_ID = 2
AIR_CO2_ID = 3
SOIL_TEMP_ID = 4
SOIL_HUMID_ID = 5
SOIL_EC_ID = 6
URL = "http://172.26.16.6:8888/api/v1/sensorvalues/"
headers = {
    "User-Agent":"curl/7.41.1",
    "Content-Type": "application/json", }

def data_post(data):
    res = requests.post(url=URL,data=json.dumps(data), headers=headers)
    print("post result:",res.text)

def prepare_sensor():
    mySHT35 = SHT35()
    mySHT35.setUp()
    myuart = UART()
    return mySHT35, myuart

def get_value(mySHT35, myuart):    
    # get air temp&humid value
    ari_temp,air_humid = mySHT35.getValue()
    # get co2 value from uart
    air_co2 = myuart.receive_uart()
    #get soil sensor value via serial
    soil_list = read_serial()
    soil_temp = soil_list['Temp']
    soil_humid = soil_list['Humid']
    soild_ec = soil_list['EC']
    return ari_temp, air_humid, air_co2, soil_temp, soil_humid, soild_ec

def main():
    mySHT35, myuart = prepare_sensor()
    
    ari_temp,air_humid,air_co2,soil_temp,soil_humid,soild_ec = get_value(mySHT35, myuart)

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
    data = {"value":soil_temp,
            "unit":"degree",
            "sensor_id":SOIL_TEMP_ID,
            }
    data_post(data)
        
    data = {"value":soil_humid,
            "unit":"percent",
            "sensor_id":SOIL_HUMID_ID,
            }
    data_post(data)

    data = {"value":soild_ec,
            "unit":"mS/cm",
            "sensor_id":SOIL_EC_ID,
            }
    data_post(data)


if __name__ == '__main__':
    main()
