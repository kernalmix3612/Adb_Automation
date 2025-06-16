import os
import time
import tkinter as tk
from tkinter import messagebox
# Import threading to allow background execution without freezing the UI
import threading
output = os.popen("adb devices").readlines() # read all the adb devices command output
space = "\t"
print(output)
serial_list = []

def check_device():
    for serial in output[1:len(output)-1]:
            dut_serial = serial[:serial.find(space)]
            serial_list.append(dut_serial)
            #print(serial_list)

def check_device_connection():
    if len(serial_list) == 0:
         print ("There is no devices")
         return None
    elif len(serial_list) == 1:
         print(f"Device is conncected, connected devive {serial_list[0]}")
         return serial_list[0]
    else:
         ##method 1 to print device list
         #print("There is mutipal devices")
         #number = 0
         #for serial in serial_list:
         #     number+=1
         #     print(f"{number}:{serial}")

         ##method 2 to print device list 
         # enumerate() is a built-in function that adds a counter to an iterable and returns it as an enumerate object.
         print("There is mutipal devices")
         for index, serial in enumerate(serial_list): 
              print(f"{index+1}: {serial}") # index start at 0
         while True:
          user_choice = input('Please select the device:') ##type is string so make sure change to int if need it
          if user_choice.isdigit() and 1<= int(user_choice) <=len(serial_list):
               #print(f'result is {serial_list[int(user_choice)-1]}')
               return serial_list[int(user_choice)-1]
          else:
               break

              

def take_screenshot(adb_device):
    os.popen(f"adb -s {adb_device} shell screencap -p /sdcard/screen.png") #Take screenshot command and save as screen.png
    time.sleep(2)
    print("Screenshoot captured")
    return

# Global flag to control stopping of auto tapping loop
stop_tapping = False

def auto_tapping(adb_device, x, y, count, delay):
    # Reset the stop flag each time auto tapping is started
    global stop_tapping
    stop_tapping = False
    for i in range(count):
        # If stop flag is set, exit the loop early
        if stop_tapping:
            print("Auto tapping stopped.")
            break
        os.popen(f"adb -s {adb_device} shell input tap {x} {y}")
        time.sleep(delay)
        print(f"Screen touched {i+1}")

def choose_function(adb_devices):
     while True:
          print("1: Screen_shoot")
          print("2: Auto_click")
          user_choice = input('Please select the device:')
          if user_choice == 1:
               take_screenshot(adb_devices)
               break
          elif user_choice == 2:
               auto_tapping(adb_devices)
               break
          

def create_ui():
    check_device()
    device = check_device_connection()
    if not device:
        messagebox.showwarning("Warning", "No devices connected.")
        return

    def on_screenshot():
        take_screenshot(device)
        messagebox.showinfo("Success", "Screenshot captured!")

    def on_autoclick():
        try:
            x = int(x_entry.get())
            y = int(y_entry.get())
            count = int(tap_entry.get())
            delay = float(delay_entry.get())
            # Start auto tapping in a background thread so UI stays responsive
            threading.Thread(target=auto_tapping, args=(device, x, y, count, delay), daemon=True).start()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for X, Y, tap count, and delay.")

    # Function to stop the ongoing auto tapping by setting the stop flag
    def stop_autoclick():
        global stop_tapping
        stop_tapping = True

    root = tk.Tk()
    root.title("ADB Device Control")
    root.geometry("600x500")

    label = tk.Label(root, text=f"Device: {device}", pady=10)
    label.pack()

    coord_frame = tk.Frame(root)
    coord_frame.pack(pady=5)

    tk.Label(coord_frame, text="X:").grid(row=0, column=0)
    x_entry = tk.Entry(coord_frame, width=5)
    x_entry.grid(row=0, column=1)

    tk.Label(coord_frame, text="Y:").grid(row=0, column=2)
    y_entry = tk.Entry(coord_frame, width=5)
    y_entry.grid(row=0, column=3)

    tk.Label(root, text="Number of Taps:").pack()
    tap_entry = tk.Entry(root, width=10)
    tap_entry.pack(pady=5)

    tk.Label(root, text="Delay between taps (seconds):").pack()
    delay_entry = tk.Entry(root, width=10)
    delay_entry.pack(pady=5)

    screenshot_btn = tk.Button(root, text="Take Screenshot", command=on_screenshot)
    screenshot_btn.pack(pady=5)

    auto_click_btn = tk.Button(root, text="Auto Click", command=on_autoclick)
    auto_click_btn.pack(pady=5)

    # Button to stop auto tapping process
    stop_click_btn = tk.Button(root, text="Stop Auto Click", command=stop_autoclick)
    stop_click_btn.pack(pady=5)

    root.mainloop()

def main():
    create_ui()

if __name__ == '__main__':
    main()