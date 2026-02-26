from tts_engine import speak
from speech_engine import listen
from features import execute_command

speak("Hello, I am Bruce. How can I help you?")

while True:
    command = listen()

    if not command:
        continue

    should_continue = execute_command(command)

    if not should_continue:
        break