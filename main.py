from flet import app as runApp
from app.routes.pages.home import HomeScreen

if __name__ == '__main__':
    runApp(
        target=HomeScreen.init,
    )
