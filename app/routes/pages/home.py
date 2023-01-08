
from flet import Stack,Page,MainAxisAlignment
from app.core.core import AppSize,AppStrings,AppColor
from app.routes.routes import routesInit

class HomeScreen:
    
    instance = None
    
    @classmethod
    def init(cls,page:Page):
        cls.instance = cls(page)
        return cls.instance
    
    def __init__(self,page:Page):
        super().__init__()
        
        # variables ...
        self.page = page
        
        # Initialize --------------------
        self.page.title = AppStrings.name
        self.page.bgcolor = AppColor.backgroundColor
        self.page.theme_mode = AppColor.themeMode
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.page.padding = 0
        self.page.margin = 0
        self.page.vertical_alignment = MainAxisAlignment.START
        page.window_width = AppSize.width
        page.window_height = AppSize.height
        
        # body --------------------------------
        self.stack = Stack([
            routesInit['/']
        ])
        
    
        self.page.add(self.stack)
        
        self.__loadFiles()



    def __loadFiles(self):
        ...
