# with some help from ChatGPT and the work from https://github.com/Plippo/asus-wmi-screenpad
# rework

#!/usr/bin/env python3

import os

class screenpad():
    def __init__(self):
        self.sp_brightness = None
        self.sp_brightness_path = "/sys/class/leds/asus::screenpad/brightness"

        self.main_screen_brightness = None
        self.main_screen_brightness_path = "/sys/class/backlight/intel_backlight/brightness"
        
        self.main_screen_range = 19200
        self.sp_range = 255
        self.conversion = self.main_screen_range/self.sp_range
        

    def get_brightness(self, path):
        with open(path, 'r') as brightness_file:
            brightness = int(brightness_file.read().strip())
        return brightness
    
    def set_brightness(self, brightness):
        self.sp_brightness = brightness
        with open(self.sp_brightness_path, 'w') as brightness_file:
            brightness_file.write(str(brightness))
        brightness_file.close()

    def increase_brightness(self):
        self.sp_brightness = min(255, self.sp_brightness + 5)
        self.set_brightness(self.sp_brightness)
        print("Brightness increased to:", self.sp_brightness)

    def decrease_brightness(self):
        self.sp_brightness = max(0, self.sp_brightness - 5)
        self.set_brightness(self.sp_brightness)
        print("Brightness decreased to:", self.sp_brightness)
    
    def cycle_brightness(self):
        cycle = (0, 30, 85, 170, 255)
        if self.sp_brightness not in cycle:
            self.sp_brightness = min(cycle, key=lambda x:abs(x-self.sp_brightness))
        elif self.sp_brightness == 30:
            self.sp_brightness = 85
        elif self.sp_brightness == 85:
            self.sp_brightness = 170
        elif self.sp_brightness == 170:
            self.sp_brightness = 255
        elif self.sp_brightness == 255:
            self.sp_brightness = 0
        elif self.sp_brightness == 0:
            self.sp_brightness = 30
    
    def sync_brightness(self):
        self.main_screen_brightness = self.get_brightness(self.main_screen_brightness_path)
        self.set_brightness(int(self.main_screen_brightness // self.conversion))
        print("Main Screen Brightness:", self.main_screen_brightness)
        print("Second Screen Brightness:", self.sp_brightness)


if __name__ == "__main__":
    sp = screenpad()
    sp.sp_brightness = sp.get_brightness(sp.sp_brightness_path)
    sp.cycle_brightness()
    sp.set_brightness(sp.sp_brightness)
    print("Brightness set to:", sp.sp_brightness)
