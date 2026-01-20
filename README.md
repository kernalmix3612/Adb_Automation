# ADB Device Control

Simple Tkinter UI for basic Android device control via ADB. It detects connected devices, lets you take a screenshot, and run repeated tap (auto-click) actions with a configurable delay.

## Features
- Detects connected ADB devices and selects one
- Take a device screenshot (saved on the device)
- Auto-tap at specific screen coordinates for a given count and delay
- Stop an in-progress auto-tap loop

## Requirements
- Python 3
- Android Debug Bridge (adb) installed and on your PATH
- Android device with USB debugging enabled
- Tkinter (usually bundled with Python)

## Setup
1. Install Android Platform Tools (adb).
2. Connect a device and run:
   ```bash
   adb devices
   ```
   Confirm the device is listed and authorized.

## Usage
Run the UI:
```bash
python Adb_Device_Control.py
```

In the UI:
- Enter X and Y screen coordinates
- Enter the number of taps and the delay between taps (seconds)
- Click "Auto Click" to start, and "Stop Auto Click" to halt
- Click "Take Screenshot" to capture a screenshot

## Notes
- If multiple devices are connected, the script will prompt in the terminal to choose one.
- The screenshot is saved on the device at `/sdcard/screen.png`.
