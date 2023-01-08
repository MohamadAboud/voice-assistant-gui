import speech_recognition as sr


def convertVoiceToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, 6, 6)
        try:
            voice_data = r.recognize_google(audio)  # audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            return  "I do not understand you"

        except sr.RequestError:
            return  "Make sure the internet connection is connected"

    return voice_data.lower()