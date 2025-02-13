# Watchdog File Sorter  

🚀 A Python script that automatically sorts downloaded files into folders based on file type. Uses `watchdog` for real-time monitoring.  

## 📌 Features  
- 📂 Moves images (`.png`, `.jpeg`, `.jpg`) to `picsSorted/`  
- 📄 Moves PDFs (`.pdf`) to `pdfSorted/`  
- 🎯 Uses `watchdog` to monitor directory changes  
- 🛠️ Cross-platform support (Mac, Windows, Linux)  

---

## 🛠️ Installation & Usage  
 
### **1️⃣ Install Dependencies**  
`git clone https://github.com/AryahCodes/watchdog-file-sorter.git`
`cd watchdog-file-sorter`
`pip install -r requirements.txt`

### ONYL NEEDED IF YOU USE THE OLD VERSION, **2️⃣ Create Required Folders**  
`Before running the script, you must manually create the destination folders, as they do not exist by default.`

`Mac/Linux:
mkdir -p ~/picsSorted ~/pdfSorted
Windows (Command Prompt):
mkdir %USERPROFILE%\picsSorted %USERPROFILE%\pdfSorted`

WITH NEW VERSION, YOU ONLY NEED TO DO STEP ONE

### **3️⃣ Run the Script** 
python script.py

