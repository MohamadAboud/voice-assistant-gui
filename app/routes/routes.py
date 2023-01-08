
from app.routes.pages.welcome_screen import ChatScreen

routesInit = {
    '/': ChatScreen.init()
}

routes = {
    '/': ChatScreen.instance
}
