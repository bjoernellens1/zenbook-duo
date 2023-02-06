#workinprogress

import subprocess

def standard():
    # create a GNOME keyboard shortcut for changing the sp brightness or turning off
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "set_brightness", "['<Super><Launch7>']"])
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "set_brightness-command", "python /usr/local/bin/cycle-sp-brightness.py"])

def extra():
    # create a GNOME keyboard shortcut for increasing the brightness
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "increase-brightness", "['<Ctrl><Alt>Right']"])
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "increase-brightness-command", "python3 -c 'import os; import sys; sys.path.append(os.getcwd()); import script; script.increase_brightness()'"])

    # create a GNOME keyboard shortcut for decreasing the brightness
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "decrease-brightness", "['<Ctrl><Alt>Left']"])
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "decrease-brightness-command", "python3 -c 'import os; import sys; sys.path.append(os.getcwd()); import script; script.decrease_brightness()'"])

    # create a GNOME keyboard shortcut to sync the brightness
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "sync-brightness", "['<Ctrl><Alt>s']"])
    subprocess.run(["gsettings", "set", "org.gnome.desktop.wm.keybindings", "sync-brightness-command", "python3 -c 'import os; import sys; sys.path.append(os.getcwd()); import script; script.sync_brightness()'"])

def neu():
    gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name "'move-window'"
    gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding "'<Primary><Alt>Page_Down'"
    gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command "'/usr/local/bin/move-window.sh'"

standard()