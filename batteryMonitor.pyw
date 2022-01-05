LOW = 50
HIGH = 60
FREQUENCY = 60 * 2   # 60 secs in a minute, 3 minutes

import psutil
import ctypes
import time
MessageBox = ctypes.windll.user32.MessageBoxW

priorMessageTime = time.time()

while(True):
    battery = psutil.sensors_battery()
    PERCENT = battery.percent
    IS_PLUGGED_IN = battery.power_plugged

    message = ""
    if PERCENT <= LOW and not IS_PLUGGED_IN:
        message = "Battery LOW"
    if PERCENT >= HIGH and IS_PLUGGED_IN:
        message = "Battery HIGH"
    if message != "":
        message = (message +
                " (" + str(PERCENT) + "%)\n" +
                str(int((time.time() - priorMessageTime) / 60.0)) +
                " minutes since last message")
        priorMessageTime = time.time()
        MessageBox( None, message, "Battery Monitor", 48)
        

    time.sleep(FREQUENCY)
     
    continue
