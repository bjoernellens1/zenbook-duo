import os
import time
import subprocess

from screenpad import screenpad

sp = screenpad()


#screenpad_brightness_path = "/sys/class/leds/asus::screenpad/brightness"
main_screen_brightness_path = "/sys/class/backlight/intel_backlight/brightness"

# def set_brightness(brightness_path, brightness):
#     with open(brightness_path, 'w') as brightness_file:
#         brightness_file.write(str(brightness))

main_screen_range = 19200
second_screen_range = 255
conversion = 19200/255

def sync_brightness():
    with open(main_screen_brightness_path, 'r') as main_screen_brightness_file:
        main_screen_brightness = int(main_screen_brightness_file.read().strip())
    #set_brightness(screenpad_brightness_path, main_screen_brightness)
    sp.set_brightness(int(main_screen_brightness // conversion))
    print("Main Screen Brightness:", main_screen_brightness)
    print("Second Screen Brightness:", sp.brightness)
    #print("Second Screen Brightness:", int(main_screen_brightness // conversion))

while True:
    sync_brightness()
    time.sleep(0.1)