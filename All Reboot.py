import os
import subprocess
from ppadb.client import Client as Adbclient
import time

def connect():
    os.system('adb devices')
    client =  Adbclient(host="127.0.0.1", port=5037)
    device = client.devices() #Get the list of connnected devices
    Dev_List = []
    if device:
         for Dev_serial in device:
              serial = Dev_serial.serial #Teanslate to readable device serial number
              Dev_List.append(serial) 

    print(Dev_List)
    return Dev_List

def reboot(Device_List):
     for Device_Serial in Device_List:
          os.system('adb -s {} reboot'.format(Device_Serial))

if __name__ =='__main__':
     Device_List = connect()
     reboot(Device_List)
     
     

