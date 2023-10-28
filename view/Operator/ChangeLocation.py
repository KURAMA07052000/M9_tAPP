import tkinter as tk
from tkinter import *
from tkinter import ttk

import os
import sys
sys.path.append(os.getcwd())

class ChangeLocation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller      
        #heading=tk.Label(self,text="Change Vehicle Location", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        #heading.place(x=100, y=15)

        operatorMap = tk.Label(self, image = self.CONTROLLER.ASSETS['map'])
        operatorMap.pack(side='right')

        vehicle_heading = tk.Label(self, text="Car 1", fg="black", bg="white", font=("Microsft YaHei UI Light",25,"bold")) #update this to display vehicle make/ or number
        vehicle_heading.place(x=250, y=120)

        label1 = tk.Label(self, text="Current Location: ", fg="black", bg="white", font=("Microsft YaHei UI Light",16,"bold"))
        label1.place(x=100, y=200)

        location = tk.Label(self, text="(show location yall)", fg="black", bg="white", font=("Microsft YaHei UI Light",12,"bold")) #update this to display cars location
        location.place(x=320, y=200)

        change_location = ttk.Combobox(self, values=["loc 1", "loc2", "loc"])
        change_location.place(x=100, y=250, width=390)
        
        Button(self,width=25,pady=7,text="CANCEL",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toOperatorHome).place(x=100, y=300)
        Button(self, width=25,pady=7,text="CONFIRM",bg="#CD3333", fg="white", border=0).place(x=320, y=300)

if __name__=='__main__':
    from controller.Controller import Controller

    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False,False)

    container = tk.Frame(root)
    container.pack(side = "top", fill = "both", expand = True)    
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    controller = Controller()
    controller.setView(root)

    pg = ChangeLocation(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()