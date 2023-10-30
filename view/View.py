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
        self.title('')
        
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
        
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        controller.setView(self)

        self.CONTROLER = controller

        self.frames = {}
        
        for F in controller.ALL_PAGES:
            frame = F(self.container, controller)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky ="nsew")

        controller.toSignIn()
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        try:
            frame.refresh()
        except Exception as ex:
            print('o' + str(ex))
        frame.tkraise()

    def init_and_show_frame(self, cont):
        if cont in self.frames:
            # Destroy the old frame
            self.frames[cont].destroy()

        # Create a new frame instance
        frame = cont(self.container, self.CONTROLER)
        self.frames[cont] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

if __name__=='__main__':
    app = tkinterApp()
    app.mainloop()