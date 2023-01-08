from flet import *

from app.core.core import AppColor
from app.widgets.widgets import CustomButton


class CustomTextField(UserControl):
    def __init__(self):
        self.__textField =TextField(
                    expand=True,
                    border_radius=border_radius.all(20),
                    hint_text="Enter your text ...",
                    border_color=AppColor.negativeBackgroundColor,
                    on_change=self.__on_change,
                    on_submit=self.__onSubmit,
                )

        self.__sendButton = CustomButton(
            icons=icons.MIC,
            on_click=self.__micClicked
        )

        super().__init__()

    def build(self):
        return Row(
            controls=[
                Container(width=3),  # Padding

                # Text field
                self.__textField,

                # send button
                self.__sendButton,

                Container(width=2)  # Padding
            ]
        )

    #############################| Events
    def __on_change(self, e):
        self.text = e.data
        self.__changeIcons(self.text)

    def __changeIcons(self,text):
        if len(text) == 0:
            self.__sendButton.on_click = self.__micClicked
            self.__sendButton.changeIcons(newIcons=icons.MIC)
        else:
            self.__sendButton.on_click = self.__sendButtonClick
            self.__sendButton.changeIcons(newIcons=icons.SEND)

    def disabledInput(self,val):
        if val:
            self.__sendButton.disabled = True
            self.__textField.disabled = True
            self.__textField.update()
            self.__sendButton.update()
        else:
            self.__sendButton.disabled = False
            self.__textField.disabled = False
            self.__textField.update()
            self.__sendButton.update()

    def __micClicked(self,e):
        self.disabledInput(True)

        from app.scripts.mind import Mind
        Mind.recordAudio(ask="i\'m listening")

        self.disabledInput(False)


    def __sendButtonClick(self,_):
        self.__send()

    def __onSubmit(self,_):
        self.__send()

    def __send(self):
        self.__textField.value = ""
        self.__changeIcons('')
        self.__textField.update()

        from app.scripts.mind import Mind
        Mind.respond(text=self.text)
