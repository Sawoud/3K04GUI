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
import serial
from kivy.uix.slider import Slider


# still have to do the displaying numbers onto the screen
var2 = 0

connection = 0

font_size = 20

def Connect(): # function that deermines if the pace maker is connected or not
    global connection
    ser = serial
    com = "COM4"
    try:
      ser = serial.Serial(com, 9600, timeout=1) # the fn. waits for 1 second, if it cant find a connection it determines its not connected

      while ser.read():
        connection = 0

      connection = 1
      ser.close()

    except serial.serialutil.SerialException:
      connection = 0




class MyGrid(GridLayout):

    def AddButtons(self,x): # this function determines what buttons have to be added
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
        if(x !=5):
            self.doo = Button(text = "DOO")
            self.doo.bind(on_press=self.DOO)
            self.add_widget(self.doo)
        if(x !=6):
            self.aoor = Button(text = "AOOR")
            self.aoor.bind(on_press=self.AOOR)
            self.add_widget(self.aoor)

        if(x !=7):
            self.voor = Button(text = "VOOR")
            self.voor.bind(on_press=self.VOOR)
            self.add_widget(self.voor)

        if(x !=8):
            self.aair = Button(text = "AAIR")
            self.aair.bind(on_press=self.AAIR)
            self.add_widget(self.aair)

        if(x !=9):
            self.vvir = Button(text = "VVIR")
            self.vvir.bind(on_press=self.VVIR)
            self.add_widget(self.vvir)

        if(x !=10):
            self.door = Button(text = "DOOR")
            self.door.bind(on_press=self.DOOR)
            self.add_widget(self.door)


    def Popup(self,var,temp): # this function shows the values of the parameters of each mode
        str = user + "\\" + var +'.txt'
        print(str)
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


    def para(self,var,select):
        global font_size
        self.clear_widgets()
        self.AddButtons(1)
#        self.Popup(var)
        Connect()
###############################################

        self.cols = 3
        self.add_widget(Label(text="Lower Rate Limit"))# these blocks show the specific parameters for the mode...
        self.name1 = TextInput(multiline=False) # ...and gives the user the chance to change them
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = font_size)
        self.submit1.bind(on_press = partial(self.pressed,self.name1,var,'Lower Rate Limit'))
        self.add_widget(self.submit1)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = font_size)
        self.submit2.bind(on_press = partial(self.pressed,self.name2,var,'Upper Rate Limit'))
        self.add_widget(self.submit2)

        if(select == 6 or select == 7 or select == 8 or select == 9 or select == 10):
            self.add_widget(Label(text="Maximum Sensor Rate"))
            self.name16 = TextInput(multiline=False)
            self.add_widget(self.name16)
            self.submit16 = Button(text = "Change",font_size = font_size)
            self.submit16.bind(on_press = partial(self.pressed,self.name16,var,'Maximum Sensor Rate'))
            self.add_widget(self.submit16)


        if(select == 5 or select == 10):
            self.add_widget(Label(text="Fixed AV Delay"))
            self.name14 = TextInput(multiline=False)
            self.add_widget(self.name14)
            self.submit14 = Button(text = "Change",font_size = font_size)
            self.submit14.bind(on_press = partial(self.pressed,self.name14,var,'Fixed AV Delay'))
            self.add_widget(self.submit14)

        if(select == None):
            self.add_widget(Label(text="Dynamic AV Delay"))
            self.name15 = TextInput(multiline=False)
            self.add_widget(self.name15)
            self.submit15 = Button(text = "Change",font_size = font_size)
            self.submit15.bind(on_press = partial(self.pressed,self.name15,var,'Dynamic AV Delay'))
            self.add_widget(self.submit15)


        if(select == 1 or select == 3 or select == 6 or select == 8 or select == 10):
            self.add_widget(Label(text="Atrial Amplitude"))
            self.name3 = TextInput(multiline=False)
            self.add_widget(self.name3)
            self.submit3 = Button(text = "Change",font_size = font_size)
            self.submit3.bind(on_press = partial(self.pressed,self.name3,var,'Atrial Amplitude'))
            self.add_widget(self.submit3)
        if(select == 1 or select == 3  or select == 5 or select == 6  or select == 8 or select == 10):
            self.add_widget(Label(text="Atrial Pulse Width"))
            self.name4 = TextInput(multiline=False)
            self.add_widget(self.name4)
            self.submit4 = Button(text = "Change",font_size = font_size)
            self.submit4.bind(on_press = partial(self.pressed,self.name4,var,'Atrial Pulse Width'))
            self.add_widget(self.submit4)

        if(select == 2 or select == 4  or select == 5 or select == 7  or select == 9 or select == 10):
            self.add_widget(Label(text="Ventricular Amplitude"))
            self.name5 = TextInput(multiline=False)
            self.add_widget(self.name5)
            self.submit5 = Button(text = "Change",font_size = font_size)
            self.submit5.bind(on_press = partial(self.pressed,self.name5,var,'Ventricular Amplitude'))
            self.add_widget(self.submit5)

        if(select == 2 or select == 4  or select == 5 or select == 7 or select == 9 or select == 10):
            self.add_widget(Label(text="Ventricular Pulse Width"))
            self.name6 = TextInput(multiline=False)
            self.add_widget(self.name6)
            self.submit6 = Button(text = "Change",font_size = font_size)
            self.submit6.bind(on_press = partial(self.pressed,self.name6,var,'Ventricular Pulse Width'))
            self.add_widget(self.submit6)


        if(select == 3  or select == 8):
            self.add_widget(Label(text="Atrial Sensitivity"))
            self.name8 = TextInput(multiline=False)
            self.add_widget(self.name8)
            self.submit8 = Button(text = "Change",font_size = font_size)
            self.submit8.bind(on_press = partial(self.pressed,self.name8,var,'Atrial Sensitivity'))
            self.add_widget(self.submit8)

        if(select == 9):
            self.add_widget(Label(text="VRP"))
            self.name21 = TextInput(multiline=False)
            self.add_widget(self.name21)
            self.submit21 = Button(text = "Change",font_size = font_size)
            self.submit21.bind(on_press = partial(self.pressed,self.name21,var,'VRP'))
            self.add_widget(self.submit21)

        if(select == 3  or select == 8 or select == 9):
            self.add_widget(Label(text="ARP"))
            self.name9 = TextInput(multiline=False)
            self.add_widget(self.name9)
            self.submit9 = Button(text = "Change",font_size = font_size)
            self.submit9.bind(on_press = partial(self.pressed,self.name9,var,'ARP'))
            self.add_widget(self.submit9)

        if(select == 3  or select == 8):
            self.add_widget(Label(text="PVARP"))
            self.name10 = TextInput(multiline=False)
            self.add_widget(self.name10)
            self.submit10 = Button(text = "Change",font_size = font_size)
            self.submit10.bind(on_press = partial(self.pressed,self.name10,var,'PVARP'))
            self.add_widget(self.submit10)

        if(select == 3 or select == 4 or select == 8  or select == 9):
            self.add_widget(Label(text="Hysteresis"))
            self.name11 = TextInput(multiline=False)
            self.add_widget(self.name11)
            self.submit11 = Button(text = "Change",font_size = font_size)
            self.submit11.bind(on_press = partial(self.pressed,self.name11,var,'Hysteresis'))
            self.add_widget(self.submit11)

        if(select == 3 or select == 4  or select == 8  or select == 9):
            self.add_widget(Label(text="Rate Smoothing"))
            self.name12 = TextInput(multiline=False)
            self.add_widget(self.name12)
            self.submit12 = Button(text = "Change",font_size = font_size)
            self.submit12.bind(on_press = partial(self.pressed,self.name12,var,'Rate Smoothing'))
            self.add_widget(self.submit12)

        if(select == 4 or select == 9):
            self.add_widget(Label(text="Ventricular Sensitivity"))
            self.name13 = TextInput(multiline=False)
            self.add_widget(self.name13)
            self.submit13 = Button(text = "Change",font_size = font_size)
            self.submit13.bind(on_press = partial(self.pressed,self.name13,var,'Ventricular Sensitivity'))
            self.add_widget(self.submit13)


        if(select == 6 or select == 7 or select == 8 or select == 9 or select == 10):
            self.add_widget(Label(text="Activity Threshold"))
            self.name17 = TextInput(multiline=False)
            self.add_widget(self.name17)
            self.submit17 = Button(text = "Change",font_size = font_size)
            self.submit17.bind(on_press = partial(self.pressed,self.name17,var,'Activity Threshold'))
            self.add_widget(self.submit17)

        if(select == 6 or select == 7 or select == 8 or select == 9 or select == 10):
            self.add_widget(Label(text="Reaction Time"))
            self.name18 = TextInput(multiline=False)
            self.add_widget(self.name18)
            self.submit18 = Button(text = "Change",font_size = font_size)
            self.submit18.bind(on_press = partial(self.pressed,self.name18,var,'Reaction Time'))
            self.add_widget(self.submit18)

        if(select == 6 or select == 7 or select == 8 or select == 9 or select == 10):
            self.add_widget(Label(text="Response Factor"))
            self.name19 = TextInput(multiline=False)
            self.add_widget(self.name19)
            self.submit19 = Button(text = "Change",font_size = font_size)
            self.submit19.bind(on_press = partial(self.pressed,self.name19,var,'Response Factor'))
            self.add_widget(self.submit19)


        if(select == 6 or select == 7 or select == 8 or select == 9 or select == 10):
            self.add_widget(Label(text="Recovery Time"))
            self.name20 = TextInput(multiline=False)
            self.add_widget(self.name20)
            self.submit20 = Button(text = "Change",font_size = font_size)
            self.submit20.bind(on_press = partial(self.pressed,self.name20,var,'Recovery Time'))
            self.add_widget(self.submit20)




        self.add_widget(Label(text="Show "+var+" Parameters Values"))
        self.submitend = Button(text = "Values",font_size = font_size)
        self.submitend.bind(on_press = partial(self.Popup,var))
        self.add_widget(self.submitend)

        global connection
        if(connection == 1): # this block shows the user if the pacemaker is connected or not
            self.add_widget(Label(text="CONNECTED"))
        else:
            self.add_widget(Label(text="NOT CONNECTED"))
    def VOO(self,temp): # This is the VOO function
####################################################
        var = "VOO"
        self.clear_widgets()
        self.AddButtons(2)
        Connect()

###############################################
        self.cols = 3

        self.add_widget(Label(text="Lower Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press = partial(self.pressed,self.name1,var,'Lower Rate Limit'))
        self.add_widget(self.submit1)

        self.cols = 1
        self.AddButtons(0)
# MODE FUNCTIONS

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


    def AAI(self,temp): # this is the AAI function
####################################################
        var = "AAI"
        self.clear_widgets()
        self.AddButtons(3)
        Connect()

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


        self.add_widget(Label(text="Atrial Sensitivity"))
        self.name5 = TextInput(multiline=False)
        self.add_widget(self.name5)
        self.submit5 = Button(text = "Change",font_size = 30)
        self.submit5.bind(on_press = partial(self.pressed,self.name5,var,'Atrial Sensitivity'))
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



    def VVI(self,temp): # this is the VVI function
####################################################
        var = "VVI"
        self.clear_widgets()
        self.AddButtons(4)
        Connect()

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
        self.name5 = TextInput(multiline=False)
        self.add_widget(self.name5)
        self.submit5 = Button(text = "Change",font_size = 30)
        self.submit5.bind(on_press = partial(self.pressed,self.name5,var,'Ventricular Pulse Width'))
        self.add_widget(self.submit5)

        self.add_widget(Label(text="Ventricular Sensitivity"))
        self.name6 = TextInput(multiline=False)
        self.add_widget(self.name6)
        self.submit6 = Button(text = "Change",font_size = 30)
        self.submit6.bind(on_press = partial(self.pressed,self.name6,var,"Ventricular Sensitivity"))
        self.add_widget(self.submit6)

        self.add_widget(Label(text="Hysteresis"))
        self.name7 = TextInput(multiline=False)
        self.add_widget(self.name7)
        self.submit7 = Button(text = "Change",font_size = 30)
        self.submit7.bind(on_press = partial(self.pressed,self.name7,var,"Hysteresis"))
        self.add_widget(self.submit7)

        self.add_widget(Label(text="Rate Smoothing"))
        self.name8 = TextInput(multiline=False)
        self.add_widget(self.name8)
        self.submit8 = Button(text = "Change",font_size = 30)
        self.submit8.bind(on_press = partial(self.pressed,self.name8,var,"Rate Smoothing"))
        self.add_widget(self.submit8)

        self.add_widget(Label(text="Show "+var+" Parameters Values"))
        self.submit9 = Button(text = "Values",font_size = 30)
        self.submit9.bind(on_press = partial(self.Popup,var))
        self.add_widget(self.submit9)
        global connection
        if(connection == 1):
            self.add_widget(Label(text="CONNECTED"))
        else:
            self.add_widget(Label(text="NOT CONNECTED"))


####################################################

    def DOO(self,temp): # This is the AOO function
        var = "DOO"
        self.para(var,5)
####################################################

    def AOOR(self,temp): # This is the VOO function
        var = "AOOR"
        self.para(var,6)
####################################################
    def VOOR(self,temp): # this is the AAI function
        var = "VOOR"
        self.para(var,7)
####################################################
    def AAIR(self,temp): # this is the VVI function
        var = "AAIR"
        self.para(var,8)
####################################################
####################################################
    def VVIR(self,temp): # this is the VVI function
        var = "VVIR"
        self.para(var,9)
####################################################
####################################################
    def DOOR(self,temp): # this is the VVI function
        var = "DOOR"
        self.para(var,10)
####################################################

    def pressed(self,instance,mode,var,temp3): # this function is invoked when the user presses any change button
        global user

        str = user + '\\' + mode+'.txt' # the path for the required file
        print(str)
        f = open(str, "r+")
        lines = f.readlines()
        print(lines)
        i = 0
        line=""
        for line in lines: # this for loop finds where the requested parameter is located

            pos = line.find("(")
            print(pos)
            pos1 = line.find("\n")
            print(pos1)
            line = line[:pos] + line[pos1+1:]
            print("line",line)
            print("var",var)
            if(line == var):
                break
            else:
                i = i + 1
        print(line)
        line = line + "(" + instance.text + ")" + "\n" # the line gets the parameter inputed between the brackets
        print(line)
        print("1",lines)

        lines[i] = line
        print("2",lines)
        lines = ''.join(lines)
        print("3",lines)
        f.seek(0)
        f.write(lines)# file gets overwritten with the new information
        f.truncate()
        f.close()

class MyApp(App):
    def build(self):
        return MyGrid()

user = ""
def main(info):
    global user
    user = info
    print("this is",info)
    MyApp().run()

#main("hellloMAIN")
