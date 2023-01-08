import pyttsx3




def convertTextToVoice(text: str):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 130)
        engine.say(text)
        engine.runAndWait()
    except Exception as err:
        print(f"error -? {err}")
