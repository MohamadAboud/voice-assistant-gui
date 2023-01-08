from flet import *

from app.core.core import AppColor,AppSize,clamp


class CustomMessage(UserControl):

    def __init__(self,text,isUser=True):
        self.text = text
        self.isUser = isUser
        super().__init__()

    def build(self):
        return Row(
            expand=True,
            controls=[
                Container(width=5),  # Padding

                Container(
                    expand=True,
                    alignment=alignment.center_right if self.isUser else alignment.center_left,
                    content=Container(
                        padding=padding.all(10),
                        border_radius=border_radius.all(15.0),
                        bgcolor=AppColor.primaryColor if self.isUser else AppColor.secondaryColor,
                        content=Text(
                            self.text,
                            color=AppColor.secondaryColor if self.isUser else AppColor.primaryColor,
                            weight=FontWeight.W_500
                        )
                    )
                ),

                Container(width=5),  # Padding

            ]
        )