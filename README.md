# 🎙️ DCMS (Dynamic Command Management System)

An automated, voice-activated desktop assistant built with Python. 

## 🚀 Features
* **Voice Activation:** Seamless background listening with a wake-word toggle.
* **Smart App Launching:** Opens local system applications without hardcoded paths.
* **Web Integration:** Automatically searches Google or plays media directly on YouTube.
* **Modern GUI:** Features a sleek, dark-mode terminal interface to log commands and system states.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Interface:** CustomTkinter
* **Core Libraries:** `speech_recognition`, `AppOpener`, `pywhatkit`

## ⚙️ Installation
1. Clone the repository: `git clone https://github.com/VegitoBlue26/DCMS-For-Git.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment and install dependencies: `pip install -r requirements.txt`
4. Run the system manually to test: `python DCMSmain.pyw`

## 💻 System Integration (Auto-Start on Windows)
To make DCMS a true background assistant, you can set it to launch automatically when you turn on your computer. 

**Note:** Do *not* place the repository folder inside OneDrive or move the `venv` directly into your startup folder, as this will break the environment paths.

**How to set up Auto-Start:**
1. Right-click on your Desktop -> **New** -> **Shortcut**.
2. Click "Browse" and locate the `pythonw.exe` file inside your project's virtual environment (e.g., `C:\Path\To\DCMS\venv\Scripts\pythonw.exe`). The 'w' ensures it runs silently without a terminal window.
3. In the shortcut text box, add a space after the executable path, and paste the full path to `DCMSmain.pyw` in quotes. 
   * *Example:* `"C:\DCMS\venv\Scripts\pythonw.exe" "C:\DCMS\DCMSmain.pyw"`
4. Name the shortcut "DCMS" and click Finish.
5. Press `Windows Key + R`, type `shell:startup`, and press Enter.
6. Drag and drop your new shortcut into this Startup folder. 

DCMS will now initialize silently in the background every time you log into Windows, waiting for the wake word.