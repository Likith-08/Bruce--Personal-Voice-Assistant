from PIL import Image
import customtkinter as ctk
from tkinter import scrolledtext
from speech_engine import listen
from features import execute_command
from tts_engine import speak
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def start_listening():
    chat_area.insert("end", "🎤 Listening...\n")
    chat_area.see("end")

    def process():
        command = listen()

        chat_area.insert("end", f"You: {command}\n")
        chat_area.see("end")

        response = execute_command(command)

        chat_area.insert("end", f"Bruce: {response}\n\n")
        chat_area.see("end")

        speak(response)

    threading.Thread(target=process).start()

# GUI setup
root = ctk.CTk()
root.title("Bruce Personal Assistant")
root.geometry("600x700")

# ===== GLOWING CYAN SEPARATOR LINE =====
glow_line = ctk.CTkFrame(
    root,
    height=4,
    fg_color="#91DC8B"
)
glow_line.pack(fill="x", pady=5)

# Top Status Bar Frame
top_frame = ctk.CTkFrame(root, height=40, fg_color="transparent")
top_frame.pack(fill="x", pady=5)

# Digital Clock
import datetime

clock_label = ctk.CTkLabel(
    top_frame,
    text="",
    font=("Arial", 14, "bold"),
    text_color="#bfb6b6"
)
clock_label.pack(side="right", padx=20)

def update_clock():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.configure(text=now)
    root.after(1000, update_clock)

update_clock()

# Load and Display Image
image = Image.open("bruce.jpg")  # change name if different
image = image.resize((120, 120))  # adjust size if needed

photo = ctk.CTkImage(light_image=image, dark_image=image, size=(120, 120))

image_label = ctk.CTkLabel(
    root,
    image=photo,
    text="",
    fg_color="transparent",
    corner_radius=15
)
image_label.pack(pady=10)

# Title Label
title_label = ctk.CTkLabel(
    root,
    text="BRUCE-PERSONAL ASSISTANT",
    font=("Arial", 28, "bold"),
    text_color="#00ffff",
    fg_color="transparent"
)
title_label.pack(pady=20)

# Hover glow effect
def top_glow_on(e):
    image_label.configure(fg_color="#001f2f")
    title_label.configure(text_color="#00ff88")

def top_glow_off(e):
    image_label.configure(fg_color="transparent")
    title_label.configure(text_color="#00ffff")

image_label.bind("<Enter>", top_glow_on)
image_label.bind("<Leave>", top_glow_off)

title_label.bind("<Enter>", top_glow_on)
title_label.bind("<Leave>", top_glow_off)


# Chat Area (Using normal tkinter text inside frame)
chat_frame = ctk.CTkFrame(root, corner_radius=15)
chat_frame.pack(padx=20, pady=10, fill="both", expand=True)

chat_area = scrolledtext.ScrolledText(
    chat_frame,
    wrap="word",
    font=("Consolas", 13),
    bg="#1a1a1a",
    fg="#00ffcc",
    insertbackground="white",
    borderwidth=0
)
chat_area.pack(fill="both", expand=True, padx=10, pady=10)

# Start Button
listen_button = ctk.CTkButton(
    root,
    text="🎤 START LISTENING",
    command=start_listening,
    height=50,
    font=("Arial", 16, "bold"),
    corner_radius=25
)
listen_button.pack(pady=20)
# Startup introduction
intro_message = "Hello, I am Bruce, your voice assistant. Click start listening to begin."
chat_area.insert("end", intro_message + "\n\n")
chat_area.see("end")
speak(intro_message)

root.mainloop()