import argparse
import os
import subprocess

def install():
    #downloading zip and unpacking it
    subprocess.run(["sudo", "mkdir", "/usr/src/asus-wmi-1.0"])
    os.chdir("/usr/src/asus-wmi-1.0")
    subprocess.run(["sudo", "wget", "https://github.com/Plippo/asus-wmi-screenpad/archive/master.zip"])
    subprocess.run(["sudo", "unzip", "master.zip"])
    subprocess.run(["sudo", "mv", "asus-wmi-screenpad-master/*", "."])
    subprocess.run(["sudo", "rm", "-r", "asus-wmi-screenpad-master"])
    subprocess.run(["sudo", "rm", "master.zip"])

    #preparing for current kernel
    subprocess.run(["sudo", "sh", "prepare-for-current-kernel.sh"])

    #registering with dkms and installing
    subprocess.run(["sudo", "dkms", "add", "-m", "asus-wmi", "-v", "1.0"])
    subprocess.run(["sudo", "dkms", "build", "-m", "asus-wmi", "-v", "1.0"])
    subprocess.run(["sudo", "dkms", "--force", "install", "-m", "asus-wmi", "-v", "1.0"])

    print("installed wmi-screenpad")

def remove():
    subprocess.run(["sudo", "dkms", "remove", "-m", "asus-wmi", "-v", "1.0", "--all"])
    subprocess.run(["sudo", "rm", "-r", "/usr/src/asus-wmi-1.0"])
    print("removed wmi-screenpad")

def reinstall():
    remove()
    install()
    print("reinstall complete")

def install_extras():
    
    subprocess.run(["cd", "/tmp"])
    subprocess.run(["git", "clone", "https://github.com/mjollnir14/gnome-shell-extension-zenbook-duo.git"])
    subprocess.run(["cd", "gnome-shell-extension-zenbook-duo"])
    subprocess.run(["make", "install"])
    print("install_extras complete")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Action to perform: install, remove, or reinstall")
    args = parser.parse_args()

    if args.action == "install":
        install()
    elif args.action == "remove":
        remove()
    elif args.action == "reinstall":
        reinstall()
    else:
        print("Invalid action. Please specify install, remove, or reinstall.")
