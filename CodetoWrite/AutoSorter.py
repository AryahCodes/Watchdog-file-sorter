#Watches for some even in the directory
import time
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer
import shutil
import logging
import os


#We need to log what happens.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
#The level tells that we need INFO or higher so like warmings. Debug will be ignored.
#format is that it shows timestamp, then level, then the message

#We have to make the destination folders dynamically
home_Idrectory = os.path.expanduser("~") #This gets us the home directory. Expanduser is a useful command.
#Use expanduser when we want to work with the home directory where the script is outside of.
#Connect home to downloads
downloads_Idrectory = os.path.join(home_Idrectory, "Downloads") #Downloads is common on all platforms.
#Connect home to the folders. Make a list of both folders
folders_Idrectory = {"picsSorted":os.path.join(home_Idrectory, "picsSorted"),
                     "pdfsSorted":os.path.join(home_Idrectory, "pdfSorted")}
#Now all the folders work with the home.

#We have to create folders if it is not already there.
for folder in folders_Idrectory.values:
    os.makedirs(folder, exist_ok=True) #We use makedirs because this won't count for intermediate directories.

#We are moving the file and logging it so we know what is happening.
def moveThefile(event, fileName):
    if isinstance(event, FileSystemEvent):
        
        #create where file should go
        destination = folders_Idrectory.get(fileName)

        logging.info(f"I want to move the file {event.src_path} to the folder {destination}")
        try:
            shutil.move(event.src_path, destination)  
            logging.info(f"Moved the file to folder {destination}")
        except FileNotFoundError:
            logging.error("There is a FileNotFoundError.")
        except PermissionError:
            logging.error("There is a PermissionError.")
        except OSError:
            logging.error("The file is open somewhere so it is unable to be moved.")

#We are using watchdog here. To watch for a event and activate
class MyHandler(FileSystemEventHandler):
    #We need to create an array for pictures and pdfs
    types_Of_Pics = {".jpeg", ".jpg", ".png"}
    pdfs = {".pdf"}
    
    def on_created(self, event): #instead of any action its when we download a new file
        
        #split the files. Use splitext to split the path into two.
        name, file_Ending = os.path.splitext(event.src_path)
        file_Ending = file_Ending.lower() #Lowercase it

        #moves the files into different folders based on type
        if file_Ending in self.types_Of_Pics:
            moveThefile(event, "picsSorted")
        elif file_Ending in self.pdfs:
            moveThefile(event, "pdfSorted")

#Checks to see if we run it from command line. 
if __name__ == "__main__":
    path = downloads_Idrectory  #The path I want. This is what we are watching.
    logging.info("File Sorter is starting...")
    event_handler = MyHandler() #class we need to write so that something can happen.
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True) #makes the event happen
    observer.start() #start the program

#Makes it so we can run the program without overworking the GPU. Lessens load on GPU.
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Stopping file sorter...")
    observer.stop()
observer.join()
logging.info("This script is ENDED. :(")