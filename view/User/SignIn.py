import tkinter as tk
from tkinter import *

import os
import sys
sys.path.append(os.getcwd())

class SignIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        self.CONTROLLER = controller

        label = Label(self, image = self.CONTROLLER.ASSETS['logo'], border=0)
        label.place(x=50,y=50)
        
        frame=tk.Frame(self,width=350,height=350, bg='white')
        frame.place(x=480, y=70)
        
        heading=tk.Label(frame,text="E-VEHICLE", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        heading.place(x=100, y=5)
        
        #username box
        def on_enter(e):
            self.emailuser.delete(0, 'end')
        def on_leave(e):
            name = self.emailuser.get()
            if name=='':
                self.emailuser.insert(0,'Email')

        self.emailuser = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.emailuser.place(x=30, y=80)
        self.emailuser.insert(0,"Email")
        self.emailuser.bind('<FocusIn>', on_enter)
        self.emailuser.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)
        
        #password box
        def on_enter(e):
            self.passcode.delete(0, 'end')
        def on_leave(e):
            name = self.passcode.get()
            if name=='':
                self.passcode.insert(0,'Password')

        self.passcode = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.passcode.place(x=30, y=150)
        self.passcode.insert(0,"Password")
        self.passcode.bind('<FocusIn>', on_enter)
        self.passcode.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)
        
        Button(frame,command=self.signIn,width=39,pady=7,text="Log in",bg="#CD3333", fg="white", border=0).place(x=35, y=204)

        sign_up = Button(frame,command=lambda : controller.toSignUp(),width=6,text="SignUp",border=0,bg="white",fg="#732222")
        sign_up.place(x=145, y=270)
        
    def signIn(self):
        self.CONTROLLER.login(self.emailuser.get(), self.passcode.get())

    def refresh(self):
        self.emailuser.delete(0,END)
        self.emailuser.insert(0,"Email")

        self.passcode.delete(0,END)
        self.passcode.insert(0,'Password')

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

    pg = SignIn(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()