import tkinter as tk
from tkinter import ttk
from tkinter import *

from controller.Controller import *

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    def __init__(self, controller, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('925x500')
        self.configure(bg='white')
        self.resizable(False,False)
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        controller.setView(self)

        self.frames = {}
        
        for F in controller.ALL_PAGES:
            frame = F(container, controller)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky ="nsew")

        controller.toSignIn()
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__=='__main__':
    app = tkinterApp()
    app.mainloop()