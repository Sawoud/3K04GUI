#!/usr/bin/env python
from kivy.app import App #We need to import the bits of kivy we need as we need them as importing everything would slow the app down unnecessarily
from kivy.uix.widget import Widget #this is a thing that you want the App to display
from kivy.uix.label import Label #this will import the code for the label in which we want to display Hello World!
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import os.path
# still have to do the displaying numbers onto the screen
var2 = 0

connection = 1

class MyGrid(GridLayout):
    def AddButtons(self,x):
        if(x != 1):
            self.aoo = Button(text = "AOO")
            self.aoo.bind(on_press=self.AOO)
            self.add_widget(self.aoo)

        if(x != 2):
            self.voo = Button(text = "VOO")
            self.voo.bind(on_press=self.VOO)
            self.add_widget(self.voo)
        if(x != 3):
            self.aai = Button(text = "AAI")
            self.aai.bind(on_press=self.AAI)
            self.add_widget(self.aai)
        if(x !=4):
            self.vvi = Button(text = "VVI")
            self.vvi.bind(on_press=self.VVI)
            self.add_widget(self.vvi)


    def Popup(self,var,temp):
        str = user + '\\' + var +'.txt'
        f = open(str,"r")
        popup = Popup(title=var+" Parameters",
        content=Label(text=f.read()),
        size_hint=(None, None), size=(400, 400))
        popup.open()

    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        # popup = Popup(title='Test popup',
        # content=Label(text='Hello world'),
        # size_hint=(None, None), size=(400, 400))
        # popup.open()

        self.cols = 2
        self.aoo = Button(text = "AOO")
        self.aoo.bind(on_press=self.AOO)
        self.add_widget(self.aoo)

        self.voo = Button(text = "VOO")
        self.voo.bind(on_press=self.VOO)
        self.add_widget(self.voo)

        self.aai = Button(text = "AAI")
        self.aai.bind(on_press=self.AAI)
        self.add_widget(self.aai)

        self.vvi = Button(text = "VVI")
        self.vvi.bind(on_press=self.VVI)
        self.add_widget(self.vvi)



#command= lambda: time_delay(e1.get(),root)
#class MyFunctions():
    def AOO(self,temp): #done
####################################################
        var = "AOO"
        self.clear_widgets()
        self.AddButtons(1)
#        self.Popup(var)
###############################################

        self.cols = 3
        self.add_widget(Label(text="Lower Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press = partial(self.pressed,self.name1,var,'Lower Rate Limit'))
        self.add_widget(self.submit1)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press = partial(self.pressed,self.name2,var,'Upper Rate Limit'))
        self.add_widget(self.submit2)

        self.add_widget(Label(text="Atrial Amplitude"))
        self.name3 = TextInput(multiline=False)
        self.add_widget(self.name3)
        self.submit3 = Button(text = "Change",font_size = 30)
        self.submit3.bind(on_press = partial(self.pressed,self.name3,var,'Atrial Amplitude'))
        self.add_widget(self.submit3)

        self.add_widget(Label(text="Artial Pulse Width"))
        self.name4 = TextInput(multiline=False)
        self.add_widget(self.name4)
        self.submit4 = Button(text = "Change",font_size = 30)
        self.submit4.bind(on_press = partial(self.pressed,self.name4,var,'Artial Pulse Width'))
        self.add_widget(self.submit4)

        self.add_widget(Label(text="Artial Sensitivity"))
        self.name5 = TextInput(multiline=False)
        self.add_widget(self.name5)
        self.submit5 = Button(text = "Change",font_size = 30)
        self.submit5.bind(on_press = partial(self.pressed,self.name5,var,'Artial Sensitivity'))
        self.add_widget(self.submit5)

        self.add_widget(Label(text="ARP"))
        self.name6 = TextInput(multiline=False)
        self.add_widget(self.name6)
        self.submit6 = Button(text = "Change",font_size = 30)
        self.submit6.bind(on_press = partial(self.pressed,self.name6,var,'ARP'))
        self.add_widget(self.submit6)

        self.add_widget(Label(text="PVARP"))
        self.name7 = TextInput(multiline=False)
        self.add_widget(self.name7)
        self.submit7 = Button(text = "Change",font_size = 30)
        self.submit7.bind(on_press = partial(self.pressed,self.name7,var,'PVARP'))
        self.add_widget(self.submit7)

        self.add_widget(Label(text="Show "+var+" Parameters Values"))
        self.submit8 = Button(text = "Values",font_size = 30)
        self.submit8.bind(on_press = partial(self.Popup,var))
        self.add_widget(self.submit8)
        global connection
        if(connection == 1):
            self.add_widget(Label(text="CONNECTED"))
        else:
            self.add_widget(Label(text="NOT CONNECTED"))
    def VOO(self,temp): #done
####################################################
        var = "VOO"
        self.clear_widgets()
        self.AddButtons(2)
###############################################
        self.cols = 3

        self.add_widget(Label(text="Lower Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press = partial(self.pressed,self.name1,var,'Lower Rate Limit'))
        self.add_widget(self.submit1)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press = partial(self.pressed,self.name2,var,'Upper Rate Limit'))
        self.add_widget(self.submit2)


        self.add_widget(Label(text="Ventricular Amplitude"))
        self.name3 = TextInput(multiline=False)
        self.add_widget(self.name3)
        self.submit3 = Button(text = "Change",font_size = 30)
        self.submit3.bind(on_press = partial(self.pressed,self.name3,var,'Ventricular Amplitude'))
        self.add_widget(self.submit3)

        self.add_widget(Label(text="Ventricular Pulse Width"))
        self.name4 = TextInput(multiline=False)
        self.add_widget(self.name4)
        self.submit4 = Button(text = "Change",font_size = 30)
        self.submit4.bind(on_press = partial(self.pressed,self.name4,var,'Ventricular Pulse Width'))
        self.add_widget(self.submit4)

        self.add_widget(Label(text="Show "+var+" Parameters Values"))
        self.submit5 = Button(text = "Values",font_size = 30)
        self.submit5.bind(on_press = partial(self.Popup,var))
        self.add_widget(self.submit5)
        global connection
        if(connection == 1):
            self.add_widget(Label(text="CONNECTED"))
        else:
            self.add_widget(Label(text="NOT CONNECTED"))


    def AAI(self,temp):
####################################################
        var = "AAI"
        self.clear_widgets()
        self.AddButtons(3)
###############################################
        self.cols = 3
        self.add_widget(Label(text="Lower Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press = partial(self.pressed,self.name1,var,'Lower Rate Limit'))
        self.add_widget(self.submit1)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press = partial(self.pressed,self.name2,var,'Upper Rate Limit'))
        self.add_widget(self.submit2)

        self.add_widget(Label(text="Atrial Amplitude"))
        self.name3 = TextInput(multiline=False)
        self.add_widget(self.name3)
        self.submit3 = Button(text = "Change",font_size = 30)
        self.submit3.bind(on_press = partial(self.pressed,self.name3,var,'Atrial Amplitude'))
        self.add_widget(self.submit3)

        self.add_widget(Label(text="Atrial Pulse Width"))
        self.name4 = TextInput(multiline=False)
        self.add_widget(self.name4)
        self.submit4 = Button(text = "Change",font_size = 30)
        self.submit4.bind(on_press = partial(self.pressed,self.name4,var,'Atrial Pulse Width'))
        self.add_widget(self.submit4)


        self.add_widget(Label(text="Artial Sensitivity"))
        self.name5 = TextInput(multiline=False)
        self.add_widget(self.name5)
        self.submit5 = Button(text = "Change",font_size = 30)
        self.submit5.bind(on_press = partial(self.pressed,self.name5,var,'Artial Sensitivity'))
        self.add_widget(self.submit5)

        self.add_widget(Label(text="ARP"))
        self.name6 = TextInput(multiline=False)
        self.add_widget(self.name6)
        self.submit6 = Button(text = "Change",font_size = 30)
        self.submit6.bind(on_press = partial(self.pressed,self.name6,var,'ARP'))
        self.add_widget(self.submit6)

        self.add_widget(Label(text="PVARP"))
        self.name7 = TextInput(multiline=False)
        self.add_widget(self.name7)
        self.submit7 = Button(text = "Change",font_size = 30)
        self.submit7.bind(on_press = partial(self.pressed,self.name7,var,'PVARP'))
        self.add_widget(self.submit7)

        self.add_widget(Label(text="Hysteresis"))
        self.name8 = TextInput(multiline=False)
        self.add_widget(self.name8)
        self.submit8 = Button(text = "Change",font_size = 30)
        self.submit8.bind(on_press = partial(self.pressed,self.name8,var,'Hysteresis'))
        self.add_widget(self.submit8)

        self.add_widget(Label(text="Rate Smoothing"))
        self.name9 = TextInput(multiline=False)
        self.add_widget(self.name9)
        self.submit9 = Button(text = "Change",font_size = 30)
        self.submit9.bind(on_press = partial(self.pressed,self.name9,var,'Rate Smoothing'))
        self.add_widget(self.submit9)

        self.add_widget(Label(text="Show "+var+" Parameters Values"))
        self.submit10 = Button(text = "Values",font_size = 30)
        self.submit10.bind(on_press = partial(self.Popup,var))
        self.add_widget(self.submit10)
        global connection
        if(connection == 1):
            self.add_widget(Label(text="CONNECTED"))
        else:
            self.add_widget(Label(text="NOT CONNECTED"))



    def VVI(self,temp):
####################################################
        var = "VVI"
        self.clear_widgets()
        self.AddButtons(4)
###############################################
        self.cols = 3
        var2 = 4
        self.add_widget(Label(text="Lower Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press = partial(self.pressed,self.name1,var,'Lower Rate Limit'))
        self.add_widget(self.submit1)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press = partial(self.pressed,self.name2,var,'Upper Rate Limit'))
        self.add_widget(self.submit2)

        self.add_widget(Label(text="Ventricular Amplitude"))
        self.name3 = TextInput(multiline=False)
        self.add_widget(self.name3)
        self.submit3 = Button(text = "Change",font_size = 30)
        self.submit3.bind(on_press = partial(self.pressed,self.name3,var,'Ventricular Amplitude'))
        self.add_widget(self.submit3)

        self.add_widget(Label(text="Ventricular Pulse Width"))
        self.name4 = TextInput(multiline=False)
        self.add_widget(self.name4)
        self.submit4 = Button(text = "Change",font_size = 30)
        self.submit4.bind(on_press = partial(self.pressed,self.name4,var,'Ventricular Pulse Width'))
        self.add_widget(self.submit4)

        self.add_widget(Label(text="Show "+var+" Parameters Values"))
        self.submit5 = Button(text = "Values",font_size = 30)
        self.submit5.bind(on_press = partial(self.Popup,var))
        self.add_widget(self.submit5)
        global connection
        if(connection == 1):
            self.add_widget(Label(text="CONNECTED"))
        else:
            self.add_widget(Label(text="NOT CONNECTED"))


    def pressed(self,instance,mode,var,temp3):
        global user

        str = user + '\\' + mode+'.txt'
        print(str)
        f = open(str, "r+")
        lines = f.readlines()
        print(lines)
        i = 0
        line=""
        for line in lines:

            pos = line.find("(")
            print(pos)
            pos1 = line.find("\n")
            print(pos1)
            line = line[:pos] + line[pos1+1:]
            print("line",line)
            print("var",var)
            if(line == var):
                print ("left")
                break
            else:
                i = i + 1
        print("im here")
        print(line)
        line = line + "(" + instance.text + ")" + "\n"
        print(line)
        print("1",lines)

        lines[i] = line
        print("2",lines)
        lines = ''.join(lines)
        print("3",lines)
        f.seek(0)
        f.write(lines)
        f.truncate()
        f.close()

class MyApp(App):
    def build(self):
        return MyGrid()

user = "MIKE"
def main(dank):
    global user
    print(dank)
    MyApp().run()

#main("hellloMAIN")
