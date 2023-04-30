import time

from screenpad import screenpad

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


sp = screenpad()

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if sp.get_brightness(sp.sp_brightness_path) != 0:
            sp.sync_brightness()
        else:
            pass

if __name__ == "__main__":
    # specify the file to monitor
    filename = sp.main_screen_brightness_path

    # create the observer and handler
    observer = Observer()
    event_handler = MyHandler()

    # schedule the observer to watch for changes to the file
    observer.schedule(event_handler, path=filename, recursive=False)
    observer.start()

    try:
        # keep the observer running until the script is stopped
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()