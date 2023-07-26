import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import datetime
from database import SIGNUPCSV
from database import LOGINCSV
from database import read_fileCSV
from database import journalENTRY
from database import journalSEARCH

kv = Builder.load_file("my.kv")
users = read_fileCSV("users.csv")
users_dict = users.open_fileCSV()

user = ""


def invalidLogin():
    pop = Popup(
        title="Invalid Login",
        content=Label(text="Invalid username or password."),
        size_hint=(None, None),
        size=(400, 400),
    )
    pop.open()


def invalidSign():
    pop = Popup(
        title="Invalid Sign Up",
        content=Label(text="Invalid username or password."),
        size_hint=(None, None),
        size=(400, 400),
    )
    pop.open()


class WelcomeWin(Screen):
    pass


class MainWin(Screen):
    pass


class LoginWin(Screen):
    username_input_log = ObjectProperty(None)
    password_input_log = ObjectProperty(None)

    def login(self):
        global username_input
        username_input = self.username_input_log.text
        password_input = self.password_input_log.text
        username_input.strip()
        password_input.strip()

        if self.username_input_log.text != "" and self.password_input_log.text != "":
            li = LOGINCSV(
                "users.csv",
                users_dict,
                self.username_input_log.text,
                self.password_input_log.text,
            )
            if li.signup_validation1():
                print("permitted")
                App.get_running_app().root.current = "mainwin"
            else:
                invalidLogin()
        else:
            invalidLogin()

        return username_input

    def return_user():
        return username_input


class SignUpWin(Screen):
    username_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    name_input = ObjectProperty(None)

    def add_user(self):
        if self.username_input.text != "" and self.password_input.text != "":
            su = SIGNUPCSV(
                "users.csv",
                users_dict,
                self.username_input.text,
                self.password_input.text,
            )
            if su.signup_validation():
                pass

            else:
                su.signup_adding_record()
                App.get_running_app().root.current = "mainwin"

        else:
            invalidSign()


class JournalWin(Screen):

    journal_input = ObjectProperty(None)
    btn1_input = ObjectProperty(None)
    btn2_input = ObjectProperty(None)
    btn3_input = ObjectProperty(None)
    btn4_input = ObjectProperty(None)
    btn5_input = ObjectProperty(None)

    rating = "1"

    def btn1(self):
        self.rating = "1"

    def btn2(self):
        self.rating = "2"

    def btn3(self):
        self.rating = "3"

    def btn4(self):
        self.rating = "4"

    def btn5(self):
        self.rating = "5"

    def get_date(self):
        return str(datetime.date.today())

    def add_entry(self):
        user = LoginWin.return_user()

        ju = journalENTRY(
            "users.csv", users_dict, user, self.journal_input.text, self.rating
        )

        ju.journal_save()


class DataWin(Screen):
    date_input = ObjectProperty(None)

    rating = ""
    entry = ""

    def get_entry(self):
        user = LoginWin.return_user()
        js = journalSEARCH(users_dict, user, self.date_input.text)
        self.entry, self.rating = js.journal_search()

        print(self.entry)

    def popup(self):

        pop = Popup(
            title=self.date_input.text,
            content=Label(text=f"Entry: {self.entry}     Rating: {self.rating}"),
            size_hint=(1, 1),
            size=(400, 400),
        )

        pop.open()


class WindowManager(ScreenManager):
    pass


sm = WindowManager()

screens = [
    MainWin(name="mainwin"),
    LoginWin(name="login"),
    SignUpWin(name="signup"),
    JournalWin(name="journal"),
    DataWin(name="data"),
    WelcomeWin(name="welcomewin"),
]  # DataWin(name = "data")]

for screen in screens:
    sm.add_widget(screen)


class MyApp(App):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    MyApp().run()
