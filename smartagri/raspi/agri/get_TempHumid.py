import RPi.GPIO as GPIO
import os
from smbus2 import SMBus
import time

SHT35_ADDR = 0x45
SHT35_CMD_MSB = 0x21
SHT35_CMD_LSB = 0x30
SHT35_READ_MSB = 0xE0
SHT35_READ_LSB = 0x00

class SHT35():
    myBus = ""
    if GPIO.RPI_INFO['P1_REVISION'] == 1:
        myBus = 0
    else:
        myBus = 1
    bus = SMBus(myBus)

    def setUp(self):
        # write command for periodic continuous measurement (1mps)
        self.bus.write_i2c_block_data(SHT35_ADDR, SHT35_CMD_MSB, [SHT35_CMD_LSB])

    def tempConverter(self, msb, lsb):
        # Temperature conversion formula
        mlsb = ((msb << 8) | lsb) 
        return (-45 + 175 * int(str(mlsb), 10) / (pow(2, 16) - 1))   

    def humidConverter(self, msb, lsb):
        # Humidity conversion formula
        mlsb = ((msb << 8) | lsb)
        return (100 * int(str(mlsb), 10) / (pow(2, 16) - 1))

    def getValue(self):
        time.sleep(1)
        self.bus.write_byte_data(SHT35_ADDR, SHT35_READ_MSB, SHT35_READ_LSB)
        data = self.bus.read_i2c_block_data(SHT35_ADDR, SHT35_READ_LSB, 6)
        temp = self.tempConverter(data[0], data[1])
        humid = self.humidConverter(data[3], data[4])
        return round(temp,2), round(humid,2)

if __name__ == '__main__':
    mySHT35 = SHT35()
    mySHT35.setUp()
    for a in range(100):
        t,h = mySHT35.getValue()
        #os.system("clear")
        print( str('{:.4g}'.format(t)) + "C" )
        print( str('{:.4g}'.format(h)) + "%" )
        print("------")
