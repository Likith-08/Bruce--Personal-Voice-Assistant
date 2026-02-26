import webbrowser
import os
import random
import datetime
import subprocess
import sys

def execute_command(message):

    message = message.lower()

    # 🔹 Greetings
    if "hello" in message or "hi" in message:
        return "Hello, I am Bruce, your voice assistant. How can I help you?"

    # 🔹 Time
    elif "time" in message:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    # 🔹 Date
    elif "date" in message:
        return "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")

    # 🔹 Open Websites
    elif "open youtube" in message:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "open google" in message:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    elif "open gmail" in message:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    elif "open linkedin" in message:
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn"
    
    elif "open instagram" in message:
        webbrowser.open("https://www.instagram.com/")
        return "Opening instagram"
    
    elif "open Facebook" in message:
        webbrowser.open("https://www.facebook.com/")
        return "Opening Facebook"
    
    elif "open Maps" in message:
        webbrowser.open("https://www.google.com/maps")
        return "Opening Maps"
    
    elif "open Netflix" in message:
        webbrowser.open("https://www.netflix.com/in/")
        return "Opening Netflix"

    # 🔹 Open Applications (Windows)
    elif "open chrome" in message:
        os.system("start chrome")
        return "Opening Chrome"

    elif "open notepad" in message:
        os.system("notepad")
        return "Opening Notepad"

    elif "open calculator" in message:
        os.system("calc")
        return "Opening Calculator"

    elif "open vscode" in message:
        os.system("code")
        return "Opening VS Code"

    # 🔹 Play Music
    elif "play song" in message:
        os.system("start wmplayer")
        return "Playing music"

    # 🔹 Search Google
    elif "search" in message:
        search_query = message.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        return f"Searching for {search_query}"

    # 🔹 System Info
    elif "system info" in message:
        return "You are running on " + sys.platform

    # 🔹 Tell Joke
    elif "joke" in message:
        jokes = [
            "Why do programmers hate nature? Too many bugs.",
            "Why did Python get promoted? Because it had good indentation.",
            "Why do developers love dark mode? Because light attracts bugs."
        ]
        return random.choice(jokes)

    # 🔹 Shutdown
    elif "shutdown" in message:
        os.system("shutdown /s /t 5")
        return "Shutting down the system in 5 seconds"

    # 🔹 Restart
    elif "restart" in message:
        os.system("shutdown /r /t 5")
        return "Restarting the system"

    # 🔹 Exit Assistant
    elif "exit" in message or "close assistant" in message:
        return "Goodbye!"

    else:
        return "I don't understand that command yet."