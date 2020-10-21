# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
import os
from part2 import *

import os.path
import shutil

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                if db.num_users()<10:
                    db.add_user(self.email.text, self.password.text, self.namee.text)
                    x=self.email.text
                    try:
                        os.makedirs(self.email.text)
                    except:
                        print("This user's folder has already been created")

                    with open(os.path.join(x,"Mode1.txt"), "a") as fileopened:
                        fileopened.write(self.namee.text+"\n"+"mode1")
                    with open(os.path.join(x,"Mode2.txt"), "a") as fileopened1:
                        fileopened1.write(self.namee.text+"\n"+"mode2")
                    with open(os.path.join(x,"Mode3.txt"), "a") as fileopened2:
                        fileopened2.write(self.namee.text+"\n"+"mode3")
                    with open(os.path.join(x,"Mode4.txt"), "a") as fileopened3:
                        fileopened3.write(self.namee.text+"\n"+"mode4")
                    self.reset()
                    sm.current = "login"

                else:
                    ToManyAccountsForm()
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class WelcomeWindow(Screen):
    num = ObjectProperty(None)

    def startbutton(self):
        sm.current="login"
    def on_enter(self, *args):
        number = str(db.num_users())
        self.num.text = "There are currently " +number+" users stored in the database"
class DeleteAccountWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
    def submit(self):
        if db.validate(self.email.text, self.password.text):
            ###code to delete stuff here
            db.delete_user(self.email.text)
            shutil.rmtree(os.getcwd()+'\\'+self.email.text)
            db.delete_user(self.email.text)
            self.reset()
        else:
            invalidLogin()
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            App.get_running_app().stop()
            main(self.email.text)
        else:
            invalidLogin()
    def deleteBtn(self):
        self.reset()
        sm.current="delete"

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    print("MainWindow")
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        print("on_enter")


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()

def ToManyAccountsForm():
    pop = Popup(title='To Many Accounts Form',
                      content=Label(text='There are already 10 users stored'),
                      size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [WelcomeWindow(name="welcome"),LoginWindow(name="login"), CreateAccountWindow(name="create"), DeleteAccountWindow(name="delete")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "welcome"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    print(db.num_users())
    MyMainApp().run()
