#ライブラリの読み込み
import RPi.GPIO as GPIO
from time import sleep

# 初期設定
GPIO.setmode(GPIO.BCM)
# 変数定義
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8
# SPI通信用の入出力を定義
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

#MCP3208からSPI通信で12bitのデジタル値を取得。4チャンネル使用可
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if adcnum > 7 or adcnum < 0:
        return -1
    GPIO.output(cspin, GPIO.HIGH)
    GPIO.output(clockpin, GPIO.LOW)
    GPIO.output(cspin, GPIO.LOW)

    commandout = adcnum
    commandout |= 0x18 # start bit + シングルエンドbit
    commandout <<= 3   # LSBから8ビット目を送信するようにする

    for i in range(5):
        if commandout & 0x80:
            GPIO.output(mosipin, GPIO.HIGH)
        else:
            GPIO.output(mosipin, GPIO.LOW)
        commandout <<= 1
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
    adcout = 0
    #
    for i in range(13):
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
        adcout <<= 1
        if i>0 and GPIO.input(misopin) == GPIO.HIGH:
          adcout |= 0x1
    GPIO.output(cspin, GPIO.HIGH)
    return adcout
def getSoilTemp(CH=0):                                               
    CH0_Volt = readadc(CH, SPICLK, SPIMOSI, SPIMISO, SPICS)  
    return round((5*50*CH0_Volt/4096 -10), 3)                                        

def getSoilEC(CH=1):                                                 
    CH1_Volt = readadc(CH, SPICLK, SPIMOSI, SPIMISO, SPICS)  
    return round((5*7*CH1_Volt/4096), 3)                              

def getSoilWater(CH=2):                                              
    CH2_Volt = readadc(CH, SPICLK, SPIMOSI, SPIMISO, SPICS)  
    return round((5*100*CH2_Volt/4096), 3)

def getSolar(CH=4):                                                  
    CH4_Volt = readadc(CH, SPICLK, SPIMOSI, SPIMISO, SPICS)  
    return round((5*CH4_Volt/4096), 3)

if __name__ == "__main__":
    try:                                                
        while True:                                     
            soil_temp_value = getSoilTemp()   
            soil_ec_value = getSoilEC()       
            soil_water_value = getSoilWater() 
            solar_value = getSolar()          
            print("Temp:" + str(soil_temp_value) + "度") 
            print("EC:" + str(soil_ec_value) + "mS/cm") 
            print("Water:"+str(soil_water_value) + "%") 
            print("Solar:"+str(solar_value) + "kW/㎡")   
            print("------")
            sleep(3)
    except KeyboardInterrupt:
        print("stop")                                   
        GPIO.cleanup()
