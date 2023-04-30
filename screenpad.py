# with some help from ChatGPT and the work from https://github.com/Plippo/asus-wmi-screenpad
# rework
import os

class screenpad():
    def __init__(self):
        self.brightness_path = "/sys/class/leds/asus::screenpad/brightness"
        f = open(self.brightness_path, "r")
        self.brightness = int(''.join(filter(str.isdigit, f.read())))
        f.close()

    def set_brightness(self, brightness):
        self.brightness = brightness
        with open(self.brightness_path, 'w') as brightness_file:
            brightness_file.write(str(brightness))
        brightness_file.close()

    def increase_brightness(self):
        self.brightness = min(255, self.brightness + 5)
        self.set_brightness(self.brightness)
        print("Brightness increased to:", self.brightness)

    def decrease_brightness(self):
        self.brightness = max(0, self.brightness - 5)
        self.set_brightness(self.brightness)
        print("Brightness decreased to:", self.brightness)
    
    def cycle_brightness(self):
        cycle = (0, 30, 85, 170, 255)
        if self.brightness not in cycle:
            self.brightness = min(cycle, key=lambda x:abs(x-self.brightness))
        elif self.brightness == 30:
            self.brightness = 85
        elif self.brightness == 85:
            self.brightness = 170
        elif self.brightness == 170:
            self.brightness = 255
        elif self.brightness == 255:
            self.brightness = 0
        elif self.brightness == 0:
            self.brightness = 30



if __name__ == "__main__":
    sp = screenpad()
    sp.cycle_brightness()
    sp.set_brightness(sp.brightness)
    print("Brightness set to:", sp.brightness)