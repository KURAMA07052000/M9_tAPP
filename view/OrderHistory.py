import tkinter as tk
from tkinter import *

from tkinter import ttk
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