import tkinter as tk
from tkinter import *

import os
import sys
sys.path.append(os.getcwd())

class ChangeLocation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller      
        heading=tk.Label(self,text="Change Vehicle Location", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        heading.place(x=100, y=5)

        image_label = tk.Label(self, image = self.CONTROLLER.ASSETS['map'])
        image_label.place(x=0, y=0)

        

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