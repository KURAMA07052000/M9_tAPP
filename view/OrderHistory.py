import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

from controller.Controller import *
import os
import sys

sys.path.append(os.getcwd())


class OrderHistory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller

        frame=tk.Frame(self,width=350,height=350, bg='white')
        frame.place(x=480, y=70)
        
        heading=tk.Label(frame,text="Your Order History", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        heading.place(x=100, y=5)

        GButton_495=tk.Button(self)
        GButton_495["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_495["font"] = ft
        GButton_495["fg"] = "#000000"
        GButton_495["justify"] = "center"
        GButton_495["text"] = "MODIFY"
        GButton_495.place(x=400,y=120,width=70,height=25)
        GButton_495["command"] = self.GButton_495_command

        GButton_165=tk.Button(self)
        GButton_165["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_165["font"] = ft
        GButton_165["fg"] = "#000000"
        GButton_165["justify"] = "center"
        GButton_165["text"] = "MODIFY"
        GButton_165.place(x=400,y=180,width=70,height=25)
        GButton_165["command"] = self.GButton_165_command

        GButton_568=tk.Button(self)
        GButton_568["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_568["font"] = ft
        GButton_568["fg"] = "#000000"
        GButton_568["justify"] = "center"
        GButton_568["text"] = "MODIFY"
        GButton_568.place(x=400,y=240,width=70,height=25)
        GButton_568["command"] = self.GButton_568_command

        GButton_228=tk.Button(self)
        GButton_228["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_228["font"] = ft
        GButton_228["fg"] = "#000000"
        GButton_228["justify"] = "center"
        GButton_228["text"] = "MODIFY"
        GButton_228.place(x=400,y=300,width=70,height=25)
        GButton_228["command"] = self.GButton_228_command

        GButton_626=tk.Button(self)
        GButton_626["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_626["font"] = ft
        GButton_626["fg"] = "#000000"
        GButton_626["justify"] = "center"
        GButton_626["text"] = "Back"
        GButton_626.place(x=240,y=360,width=71,height=30)
        GButton_626["command"] = self.GButton_626_command

        GLabel_94=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_94["font"] = ft
        GLabel_94["fg"] = "#333333"
        GLabel_94["justify"] = "center"
        GLabel_94["text"] = "ORDER 1"
        GLabel_94.place(x=90,y=120,width=70,height=25)

        GLabel_578=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_578["font"] = ft
        GLabel_578["fg"] = "#333333"
        GLabel_578["justify"] = "center"
        GLabel_578["text"] = "ACTIVE/NON-ACTIVE"
        GLabel_578.place(x=220,y=120,width=118,height=30)

        GLabel_367=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_367["font"] = ft
        GLabel_367["fg"] = "#333333"
        GLabel_367["justify"] = "center"
        GLabel_367["text"] = "NON-ACTIVE"
        GLabel_367.place(x=230,y=180,width=87,height=30)

        GLabel_922=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_922["font"] = ft
        GLabel_922["fg"] = "#333333"
        GLabel_922["justify"] = "center"
        GLabel_922["text"] = "NON-ACTIVE"
        GLabel_922.place(x=220,y=240,width=97,height=34)

        GLabel_273=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_273["font"] = ft
        GLabel_273["fg"] = "#333333"
        GLabel_273["justify"] = "center"
        GLabel_273["text"] = "NON-ACTIVE"
        GLabel_273.place(x=220,y=300,width=100,height=35)

        GLabel_713=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_713["font"] = ft
        GLabel_713["fg"] = "#333333"
        GLabel_713["justify"] = "center"
        GLabel_713["text"] = "ORDER2"
        GLabel_713.place(x=80,y=180,width=88,height=34)

        GLabel_973=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_973["font"] = ft
        GLabel_973["fg"] = "#333333"
        GLabel_973["justify"] = "center"
        GLabel_973["text"] = "ORDER3"
        GLabel_973.place(x=90,y=240,width=70,height=25)

        GLabel_8=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#333333"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "ORDER4"
        GLabel_8.place(x=90,y=300,width=70,height=25)

    def GButton_495_command(self):
        print("command")


    def GButton_165_command(self):
        print("command")


    def GButton_568_command(self):
        print("command")


    def GButton_228_command(self):
        print("command")


    def GButton_626_command(self):
        print("command")



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False, False)

    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    controller = None


    pg = OrderHistory(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()