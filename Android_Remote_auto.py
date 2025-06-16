import os
import subprocess
from ppadb.client import Client as Adbclient
from datetime import datetime, timedelta
import time

def remote_connect(ipaddress, port):
    os.system('adb devices')
    print("remote connect device is {}:{}'".format(ipaddress, port))
    if ipaddress == None or port == None:
         print("ip address or port is null, ip address = {} and port = {}".format(ipaddress, port))
    client = Adbclient()
    client.remote_connect(ipaddress, port)
    #client = os.system('adb connect {}:{}'.format(ipaddress, port))
    #devices = client.devices(f"{ipaddress}:{port}")
    #if devices:
         #print("Connected devices:")
         #phone = devices[0].serial
         #for device in devices:
              #print(f"{device.serial}")
    #else:
         #print("No devices connected")
    #return phone, client  

def Take_pic():
     os.system('adb shell am start -W com.google.android.GoogleCamera')
     #os.system('adb -s {} shell input tap 647.0 2236'.format(CamPhone))
     os.system('adb shell input tap 0 0')
     time.sleep(10)
     os.system('adb shell input keyevent 27')
     #647.0 2236

def VideoRecording():
     os.system('adb shell am start -W com.google.android.GoogleCamera')
     time.sleep(3)
     os.system("adb shell input tap 2730 635")
     time.sleep(5)
     os.system('adb shell input tap 0 0')
     os.system("adb shell input tap 2275 690")
     time.sleep(20)
     os.system("adb shell input tap 2275 690")
     os.system("adb pull /storage/emulated/0/DCIM/Camera")

if __name__ =='__main__':
     phone = input("Enter the ip addpress: ")
     port = int(input("Enter the port: "))
     remote_connect(phone, port)
     time.sleep(10)
     #Take_pic()
     VideoRecording()
     #os.system('adb -s {} shell pm list packages'.format(phone))
     #os.system('adb -s {} shell am start -W com.google.android.GoogleCamera'.format(phone))
     #time.sleep(5)
     #os.system('adb -s {} shell am start -W com.google.android.GoogleCamera'.format(phone))

    #phone, connect = connect()
    
    

    
##os.system('adb devices')
##os.system('')

