from flet import *

from app.core.core import AppColor,AppSize


class CustomButton(UserControl):
    def __init__(self, icons, height=AppSize.height * .08, width=AppSize.height * .085, on_click=None):
        self.__on_click = on_click
        self.__button = ElevatedButton(
            height=height,
            width=width,
            content=Icon(icons),
            on_click=self.on_click,
            style=ButtonStyle(
                animation_duration=500,
                bgcolor={
                    MaterialState.DEFAULT.value: AppColor.primaryColor,
                    MaterialState.HOVERED.value: AppColor.secondaryColor,
                    MaterialState.DISABLED.value: "#E6f8f8f8",
                },
                color={
                    MaterialState.DEFAULT.value: AppColor.secondaryColor,
                    MaterialState.HOVERED.value: AppColor.primaryColor,
                    MaterialState.DISABLED.value:"#E6000000",
                },
                shape={
                    MaterialState.DEFAULT.value: RoundedRectangleBorder(radius=20),
                    MaterialState.HOVERED.value: RoundedRectangleBorder(radius=50),
                    MaterialState.DISABLED.value: RoundedRectangleBorder(radius=75),
                }
            )
        )

        super().__init__()

    def build(self):
        return self.__button

    def changeIcons(self, newIcons):
        self.__button.content = Icon(newIcons)
        self.__button.update()

    @property
    def on_click(self):
        return self.__on_click

    @on_click.setter
    def on_click(self,new):
        self.__button.on_click = new