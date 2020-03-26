import serial
import traceback
import time

class UART:
    def __init__(self):
        try:
            self.seri = serial.Serial(
                port = "/dev/serial0",
                baudrate=38400,
                bytesize = serial.EIGHTBITS,
                parity = serial.PARITY_NONE,
                stopbits = serial.STOPBITS_ONE,
                timeout=10,
            )
        except serial.SerialException:
            print(traceback.format_exc())

        self.seri.flushInput()
        self.seri.flushOutput()
        time.sleep(1)

    def send_uart(self, cmd):
        pass

    def receive_uart(self):
        time.sleep(2)
        try:
            rcvdata = self.seri.readline().decode('utf-8')
        except serial.SerialException:
            print(traceback.format_exc())
        if rcvdata.__contains__("ppm"):
            data = int(rcvdata.replace('ppm','').replace('\n', '').replace('\r', '').strip())
        else:
            print("uart read format error: ",rcvdata)
            data = -1

        return data

if __name__ == '__main__':
    uart = UART()
    while True:
        data = uart.receive_uart()
        print("recv data:{0}".format(data))
