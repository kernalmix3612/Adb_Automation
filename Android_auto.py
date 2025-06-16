import os
import subprocess
from ppadb.client import Client as Adbclient
import time

def connect():
    os.system('adb devices')
    client =  Adbclient(host="127.0.0.1", port=5037)
    devices = client.devices() #Get the list of connnected devices
    if devices:
            print("Connected devices:")
            phone  = devices[0].serial #Teanslate to readable device serial number
            for device in devices:
                 print(f"{device.serial}")
    else:
        print("No devices connected")

    return phone, client

def Take_pic(CamPhone, CamClient):
     os.system('adb -s {} shell am start -W com.google.android.GoogleCamera'.format(CamPhone))
     #os.system('adb -s {} shell input tap 647.0 2236'.format(CamPhone))
     os.system('adb -s {} shell input tap 0 0'.format(CamPhone))
     time.sleep(1)
     os.system('adb -s {} shell input keyevent 27'.format(CamPhone))
     #647.0 2236


if __name__ =='__main__':
     phone, client = connect()
     #Take_pic(phone, client)
     #os.system('adb -s {} shell pm list packages'.format(phone))
     #os.system('adb -s {} shell am start -W com.google.android.GoogleCamera'.format(phone))
     #time.sleep(5)
     #os.system('adb -s {} shell am start -W com.google.android.GoogleCamera'.format(phone))

    #phone, connect = connect()
    
    

    
##os.system('adb devices')
##os.system('')

