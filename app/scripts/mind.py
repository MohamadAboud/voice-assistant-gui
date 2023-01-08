from app.data.data import Data
from app.scripts.convert_text_to_voice import convertTextToVoice
from app.scripts.convert_voice_to_text import convertVoiceToText
from app.scripts.respond import respond


class Mind:

    @classmethod
    def respond(cls,text):
        Data.voiceText = text
        res = respond(text)

        from app.routes.pages.welcome_screen import ChatScreen
        ChatScreen.instance.addMessage(text=text, isUser=True)
        ChatScreen.instance.addMessage(text=res, isUser=False)

        cls.speak(res)

    @classmethod
    def speak(cls,text):
        convertTextToVoice(text)

    @classmethod
    def recordAudio(cls,ask:str):
        if ask: cls.speak(ask)
        text = convertVoiceToText()
        Data.voiceText = text
        cls.respond(text)