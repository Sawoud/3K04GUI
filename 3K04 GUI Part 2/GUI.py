#!/usr/bin/env python
from kivy.app import App #We need to import the bits of kivy we need as we need them as importing everything would slow the app down unnecessarily
from kivy.uix.widget import Widget #this is a thing that you want the App to display
from kivy.uix.label import Label #this will import the code for the label in which we want to display Hello World!
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from functools import partial



class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
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

    def AOO(self,temp): #done
        var = "AOO"
        var2 = 1
        self.remove_widget(self.aoo)
        # self.remove_widget(self.voo)
        # self.remove_widget(self.aai)
        # self.remove_widget(self.vvi)
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

    def VOO(self,temp): #done
        self.remove_widget(self.aoo)
        self.remove_widget(self.voo)
        self.remove_widget(self.aai)
        self.remove_widget(self.vvi)
        var2 = 2
        self.cols = 3
        self.add_widget(Label(text="Lower Rate Limit"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.submit = Button(text = "Change",font_size = 30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press=self.pressed)
        self.add_widget(self.submit1)
        print("**")
        self.add_widget(Label(text="Ventricular Amplitude"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)
        print("***")
        self.add_widget(Label(text="Ventricular Pulse Width"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)


    def AAI(self,temp):
        self.remove_widget(self.aoo)
        self.remove_widget(self.voo)
        self.remove_widget(self.aai)
        self.remove_widget(self.vvi)
        var2 = 3
        self.cols = 3
        self.add_widget(Label(text="Lower Rate Limit"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.submit = Button(text = "Change",font_size = 30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press=self.pressed)
        self.add_widget(self.submit1)

        self.add_widget(Label(text="Atrial Amplitude"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)

        self.add_widget(Label(text="Atrial Pulse Width"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)


        self.add_widget(Label(text="Artial Sensitivity"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)

        self.add_widget(Label(text="ARP"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)

        self.add_widget(Label(text="PVARP"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)

        self.add_widget(Label(text="Hysteresis"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)

        self.add_widget(Label(text="Rate Smoothing"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)


    def VVI(self,temp):
        self.remove_widget(self.aoo)
        self.remove_widget(self.voo)
        self.remove_widget(self.aai)
        self.remove_widget(self.vvi)
        self.cols = 3
        var2 = 4
        self.add_widget(Label(text="Lower Rate Limit"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.submit = Button(text = "Change",font_size = 30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.add_widget(Label(text="Upper Rate Limit"))
        self.name1 = TextInput(multiline=False)
        self.add_widget(self.name1)
        self.submit1 = Button(text = "Change",font_size = 30)
        self.submit1.bind(on_press=self.pressed)
        self.add_widget(self.submit1)

        self.add_widget(Label(text="Ventricular Amplitude"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)

        self.add_widget(Label(text="Ventricular Pulse Width"))
        self.name2 = TextInput(multiline=False)
        self.add_widget(self.name2)
        self.submit2 = Button(text = "Change",font_size = 30)
        self.submit2.bind(on_press=self.pressed)
        self.add_widget(self.submit2)


    def pressed(self,instance,temp,temp2,temp3):
        print(instance.text)
        print(temp)
        print(temp2)
        print(temp3)

        pass
class MyApp(App):
    def build(self):
        return MyGrid()

user = ""
def main(dank):
    global user
    print(dank)
    MyApp().run()

main("hellloMAIN")
