import tkinter as tk
from tkinter import ttk
from tkinter import *

from view.SignIn import SignIn

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('925x500+300+200')
        self.configure(bg='white')
        self.resizable(False,False)
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in [SignIn]:
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(SignIn)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__=='__main__':
    app = tkinterApp()
    app.mainloop()