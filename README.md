# Watchdog File Sorter

🚀 A Python script that automatically sorts downloaded files into folders based on file type. Uses `watchdog` for real-time monitoring.

## 📌 Features
- 📂 Moves images (`.png`, `.jpg`) to `picsSorted/`
- 📄 Moves PDFs (`.pdf`) to `pdfSorted/`
- 🎯 Uses `watchdog` to monitor directory changes
- 🛠️ Cross-platform support (Mac, Windows, Linux)

## 🛠️ Installation
```sh
git clone https://github.com/AryahCodes/watchdog-file-sorter.git
cd watchdog-file-sorter
pip install -r requirements.txt
python script.py
