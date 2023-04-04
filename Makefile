install:
	python3 install-screenpad-wmi.py install

remove:
	python3 install-screenpad-wmi.py remove

reinstall:
	python3 install-screenpad-wmi.py reinstall

reload: # reload kernel module to avoid restart
	sudo rmmod asus_nb_wmi asus_wmi
	sudo modprobe asus_nb_wmi asus_wmi