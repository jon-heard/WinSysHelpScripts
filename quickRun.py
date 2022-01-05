root = "D:\Program Files\_sysHelpScripts"
apps = [
    "screenOff.pyw",     # 1 key
    "screenRotator.py", # 2 key
    "sleep.pyw",         # 3 key
]

import keyboard
import os

print("----------------------------------------------------------------------")
print("  QUICK RUN")
print("  (hit a number from 1 to " + str(len(apps)) + " to run assigned app)")
print("----------------------------------------------------------------------")
for i in range(len(apps)):
  print("   " + str(i + 1) + ") " + apps[i])
print(" ESC) Cancel")

while True:
    key = keyboard.read_event()
    if (key.event_type != "down"):
        continue

    key = key.scan_code

    if (key == 1):
        print("Quitting...")
        break;
    elif (key >= 2 and key <= 11):
        key = key - 2
        if (key >= len(apps)):
            print("Unassigned app: " + str(key + 1))
        else:
            print("Opening app: " + str(key + 1))
            os.chdir(root)
            os.system(apps[key])
            break;
    else:
        print("Ignoring key press " + str(key))
