
#Watches for some even in the directory
import time
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer
import shutil
import logging

def moveThefile(event, string, fileName):
    if isinstance(event, FileSystemEvent):
        logging.info(f"I want to move the file {event.src_path} to the folder {string}")
        try:
            shutil.move(event.src_path, fileName)  
            logging.info(f"Moved the file to folder {string}")
        except FileNotFoundError:
            logging.error("There is a FileNotFoundError.")
        except PermissionError:
            logging.error("There is a PermissionError.")
        except OSError:
            logging.error("The file is open is somewhere so it is unable to be moved.")

#We are using watchdog here. To watch for a event and activate
class MyHandler(FileSystemEventHandler):

    def on_created(self, event): #instead of any action its when we download a new file
        #moves the files into different folders based on type
        if event.src_path.endswith(".png") or event.src_path.endswith(".jpg"):            
            moveThefile(event, "picsSorted", "/Users/aryahb/picsSorted")
        elif event.src_path.endswith(".pdf"):
            moveThefile(event, "pdfSorted", "/Users/aryahb/pdfSorted")

#Checks to see if we run it from command line. 
if __name__ == "__main__":
    path = "/Users/aryahb/Downloads"  #The path I want
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    event_handler = MyHandler() #class we need to write so that something can happen.
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True) #makes the event happen
    observer.start() #start the program

#Makes it so we can run the program without overworking the GPU. Lessens load on GPU.
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
