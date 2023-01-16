from datetime import datetime
import pyjokes
import webbrowser

from app.core.values.strings import AppStrings
from app.data.data import Data


def say(*args):
    for text in args:
        if text in Data.voiceText.lower():
            return True

    return False


def respond(text):
    if say("what is your name", "what's your name", "tell me your name"):
        if Data.username:
            return f"My friends call me {AppStrings.name}"
        else:
            return f"My friends call me {AppStrings.name}. what's your name?"

    elif say("my name is"):
        name = text.split("is")[-1].strip()
        Data.username = name  # save the name
        return "okay,I will remember that " + name

    elif say("what is my name", "what's my name", "say my name"):
        if Data.username:
            return "Your name is " + Data.username
        else:
            return "You haven't told me your name yet"
        
    
    elif say("what is the time"):
        time = datetime.now().strftime("%I:%M %p")
        return f"The time is " + time

    elif say("what is the date"):
        date = datetime.now().strftime("%d %b,%Y")
        return f"The date is " + date

    elif say("tell me a joke"):
        return pyjokes.get_joke()


    elif say("open youtube"):
        url = "https://www.youtube.com"
        webbrowser.open(url)
        return "Youtube is opening"


    elif say("open google"):
        url = "https://www.google.com"
        webbrowser.open(url)
        return "Google is opening"

    else:
        return "I don't know that can you teach me"
