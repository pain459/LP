from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file created: {event.src_path}")
            # Trigger your custom action here
            # For example, you could process the file or send an alert:
            # process_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")
            # Trigger a different action if needed
            # maybe re-process or move the updated file

if __name__ == "__main__":
    # Directory to watch, can be current directory or specified path
    path_to_watch = "."

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
