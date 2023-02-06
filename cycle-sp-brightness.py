# with some help from ChatGPT and the work from https://github.com/Plippo/asus-wmi-screenpad

import os
brightness_path = "/sys/class/leds/asus::screenpad/brightness"

f = open(brightness_path, "r")

global brightness
brightness = int(''.join(filter(str.isdigit, f.read())))

def set_brightness(brightness):
    with open(brightness_path, 'w') as brightness_file:
        brightness_file.write(str(brightness))

def increase_brightness():
    global brightness
    brightness = min(255, brightness + 5)
    set_brightness(brightness)
    print("Brightness increased to:", brightness)

def decrease_brightness():
    global brightness
    brightness = max(0, brightness - 5)
    set_brightness(brightness)
    print("Brightness decreased to:", brightness)

if brightness == 30:
    brightness = 85
elif brightness == 85:
    brightness = 170
elif brightness == 170:
    brightness = 255
elif brightness == 255:
    brightness = 0
else:
    brightness = 30

set_brightness(brightness)
print("Brightness set to:", brightness)
f.close()