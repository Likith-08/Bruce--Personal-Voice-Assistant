# 🤖 Bruce – Personal Voice Assistant (GUI Based)

Bruce is a Python-based Personal Voice Assistant built using Tkinter / CustomTkinter GUI.
It can listen to voice commands, execute tasks, and respond using text-to-speech.

This project is completely GUI-based and does NOT use Flask, HTML, or CSS.

------------------------------------------------------------

🚀 FEATURES

- Voice Recognition (Speech to Text)
- Text-to-Speech Response
- Open Websites (YouTube, Google, Gmail)
- Tell Current Time
- Tell Current Date
- Play Songs
- Generate Random Numbers
- Chat Display Interface
- Modern Styled GUI using CustomTkinter
- AI Status Indicator
- Live Digital Clock
- Glow Effects & UI Styling

------------------------------------------------------------

🛠 TECHNOLOGIES USED

- Python 3.10+
- Tkinter
- CustomTkinter
- SpeechRecognition
- Pyttsx3
- Webbrowser module
- Datetime module
- Random module
- Threading

------------------------------------------------------------

📁 PROJECT STRUCTURE

Bruce/
│
├── gui.py               # Main GUI interface
├── speech_engine.py     # Handles voice recognition
├── tts_engine.py        # Handles text-to-speech
├── features.py          # Command execution logic
├── bruce.jpg            # Assistant image
├── README.md
└── .gitignore

------------------------------------------------------------

🧠 HOW THE PROJECT WORKS (STEP-BY-STEP)

1) GUI Starts

When you run:
python gui.py

The GUI window opens.
It shows:
- Assistant image
- Title
- Chat area
- Start Listening button

2) Startup Introduction

When GUI loads:
Bruce introduces himself and speaks:
"Hello, I am Bruce, your voice assistant."

This is done using:
speak(intro_message)

3) Clicking "Start Listening"

When you click the button:
- A new thread starts (to avoid GUI freezing)
- listen() function from speech_engine.py runs

4) Voice Recognition

Inside speech_engine.py:
- Microphone captures audio
- Converts speech to text using SpeechRecognition
- Returns command string

5) Command Execution

The command is sent to:
execute_command(command)

Inside features.py:
It checks commands using conditions like:
if "open youtube" in command:

Then performs actions like:
- Opening browser
- Returning time
- Playing music
- Generating numbers

6) Response Display

The response is:
- Shown in GUI chat area
- Spoken using pyttsx3

------------------------------------------------------------

🎨 UI DESIGN FEATURES

- Modern Dark Theme
- Cyan Glowing Separator Line
- Hover Glow Effects
- Rounded Buttons
- Styled Chat Area
- Digital Clock
- AI ONLINE Indicator

All created using CustomTkinter widgets.

------------------------------------------------------------

⚙️ INSTALLATION GUIDE

Step 1: Clone Repository

git clone : https://github.com/Likith-08/Bruce--Personal-Voice-Assistant
cd Bruce-Personal-Voice-Assistant

Step 2: Install Dependencies

pip install customtkinter
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio

If PyAudio gives error, install compatible wheel manually.

Step 3: Run Project

python gui.py

------------------------------------------------------------

🎤 SUPPORTED COMMANDS

Examples:

- Open YouTube
- Open Google
- Open Gmail
- What is the time
- What is today's date
- Play song
- Generate random number
- Goodbye

------------------------------------------------------------

💡 WHY THREADING IS USED

Threading prevents GUI from freezing while listening to voice input.

Example:
threading.Thread(target=process).start()

------------------------------------------------------------

🔐 GITIGNORE USED

__pycache__/
*.pyc
*.pyo
*.pyd

------------------------------------------------------------

👨‍💻 AUTHOR

Likith Machireddy
CSE Student | Aspiring Python Full Stack Developer

------------------------------------------------------------

📌 CONCLUSION

Bruce AI Assistant is a modular, GUI-based voice assistant built completely in Python.

It demonstrates:
- GUI Development
- Voice Recognition
- Text-to-Speech
- Command Processing
- Multi-file Project Structure
- Git & GitHub Usage

If you like this project, give it a star!
