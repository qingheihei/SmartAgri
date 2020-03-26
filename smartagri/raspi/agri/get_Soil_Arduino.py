import serial
import time
import ast

def converter_string(str):
    # "{'Humid':0.00, 'EC':0.00, 'Temp':147.00}"
    value_dict = ast.literal_eval(str)
    return value_dict

def read_serial():
    seri = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    time.sleep(1)
    read_str = seri.readline().strip()
    str = (read_str.decode('utf-8'))
    value_dict = {}
    try:
        value_dict = converter_string(str)
    except serial.SerialException:
        print(traceback.format_exc())
    except ValueError:
        print("serial read format error")
    return value_dict

if __name__ == '__main__':
    while True:
        time.sleep(1)
        print(read_serial())
        
