from typing import List

from flet import *
from app.core.core import AppSize, AppColor, AppStrings
from app.widgets.widgets import CustomTextField,CustomMessage


class ChatScreen(UserControl):
    instance = None

    @classmethod
    def init(cls):
        cls.instance = cls()
        return cls.instance

    def __init__(self):
        self.__messages = []
        self.__msgBody = Column(
                            expand=True,
                            alignment=MainAxisAlignment.END,
                            horizontal_alignment=CrossAxisAlignment.END,
                            controls=[CustomMessage(message,isUser=idx%2 ==0) for idx,message in enumerate(self.messages)],
                            scroll=ScrollMode.HIDDEN
                        )

        super().__init__()


    def build(self):
        return Container(
            alignment=alignment.center,
            height=AppSize.height,
            width=AppSize.width,
            bgcolor=AppColor.secondaryColor,
            content=Column(
                spacing=0.0,
                controls=[
                    self.__AppBar(),

                    self.__Body(),
                ]
            )
        )

    @property
    def messages(self):
        return self.__messages


    def addMessage(self,text,isUser=True):
        self.__msgBody.controls.append(CustomMessage(text,isUser=isUser))
        self.__msgBody.update()


    #############################| Widgets
    def __AppBar(self):
        return Container(
            bgcolor=AppColor.secondaryColor,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                height=AppSize.height * 0.1,
                controls=[
                    IconButton(
                        tooltip="Mohamad Aboud",
                        icon=icons.PERSON,
                        on_click=lambda e: print(e.data)
                    ),

                    Text(
                        AppStrings.name,
                        weight=FontWeight.BOLD,
                        size=28,
                    ),

                    IconButton(
                        tooltip="Settting",
                        icon=icons.SETTINGS,
                        on_click=lambda e: print(e.data)
                    ),
                ]
            )
        )

    def __Body(self):


        return Container(
            bgcolor=AppColor.backgroundColor,
            expand=True,
            clip_behavior=ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
            border_radius=border_radius.vertical(top=35.0),
            content=Column(
                controls=[
                    Container(
                        expand=True,
                        content=self.__msgBody
                    ),

                    Divider(),  # horizontal line

                    CustomTextField(),

                    Container(height=AppSize.height * .06),  # Padding
                ]
            )
        )
