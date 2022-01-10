#   command line args:
#       hotkey (default: z)
#       app to run (default: notepad.exe)
#       folder (default: D:\Program Files\_sysHelpScripts)
#       example:
#           hotkeyRunner.pyw x myapp.exe
#           runs myapp.exe when ctrl-shift-x is pressed
#           (folder "D:\Program Files\_sysHelpScripts")

import keyboard
import sys
import os

# args
hotkey = "z"
appToRun = "start notepad.exe"
folder = "D:\Program Files\_sysHelpScripts"
argCount = len(sys.argv)
if argCount > 1:
    hotkey = sys.argv[1]
if argCount > 2:
    appToRun = sys.argv[2]
if argCount > 3:
    folder = sys.argv[3]

print("----------------------------------------------------------------------")
print("  HOTKEY RUNNER")
print("  (Pressing hotkey CTRL-SHIFT-" + hotkey + " executes '" + appToRun + "')")
print("----------------------------------------------------------------------")

def runApp():
    os.chdir(folder)
    os.system(appToRun)
keyboard.add_hotkey("ctrl + shift + " + hotkey, runApp)

keyboard.wait()
