import os
import time
import subprocess

screenpad_brightness_path = "/sys/class/leds/asus::screenpad/brightness"
main_screen_brightness_path = "/sys/class/backlight/intel_backlight/brightness"

def set_brightness(brightness_path, brightness):
    with open(brightness_path, 'w') as brightness_file:
        brightness_file.write(str(brightness))

def sync_brightness():
    with open(main_screen_brightness_path, 'r') as main_screen_brightness_file:
        main_screen_brightness = int(main_screen_brightness_file.read().strip())
    set_brightness(screenpad_brightness_path, main_screen_brightness)
    print("Brightness synced to:", main_screen_brightness)