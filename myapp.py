from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image


Window.size = (300, 500)


class HomeWindow(Screen):
    def build(self):
        return


class SignWindow(Screen):
    pass


class LoginWindow(Screen):
    pass


class HomeViews(Screen):
    pass


class RentalsApartments(Screen):
    pass


class HotelRooms(Screen):
    pass


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeWindow(name="Home window"))
        sm.add_widget(SignWindow(name="Sign window"))
        sm.add_widget(LoginWindow(name="Login window"))
        sm.add_widget(HomeViews(name="Home views"))
        sm.add_widget(RentalsApartments(name="Rentals apartments"))
        sm.add_widget(HotelRooms(name="Hotel rooms"))

        return sm


MyApp().run()
