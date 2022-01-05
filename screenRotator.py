import keyboard
import rotatescreen

print("----------------------------------------------------------------------")
print("  SCREEN ROTATOR")
print("  (hit an arrow key to change rotation, escape to quit)")
print("----------------------------------------------------------------------")

while True:
    key = keyboard.read_event()
    if (key.event_type != "down"):
        continue

    key = key.scan_code

    if (key == 1):
        print("Quitting...")
        break;
    elif (key == 72):
        rotatescreen.get_primary_display().rotate_to(0)
        print("Rotating up")
    elif (key == 75):
        rotatescreen.get_primary_display().rotate_to(90)
        print("Rotating left")
    elif (key == 77):
        rotatescreen.get_primary_display().rotate_to(270)
        print("Rotating right")
    elif (key == 80):
        rotatescreen.get_primary_display().rotate_to(180)
        print("Rotating down")
    else:
        print("Ignoring key press " + str(key))
