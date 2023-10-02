import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

from controller.routes import *

class SignUp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        self.CONTROLLER = controller

        frame=Frame(self,width=350,height=650,bg='white')
        frame.pack(pady=70)

        heading=Label(frame,text="SIGN UP", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",23,"bold"))
        heading.place(x=100, y=5)

        self.emailuser = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.emailuser.place(x=30, y=80)
        self.emailuser.insert(0,"Email")
        self.emailuser.bind('<FocusIn>', lambda x: self.on_enter(element=self.emailuser))
        self.emailuser.bind('<FocusOut>', lambda x: self.on_leave('Email', self.emailuser))

        self.user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.user.place(x=30, y=155)
        self.user.insert(0,"Full Name")
        self.user.bind('<FocusIn>', lambda x: self.on_enter(self.user))
        self.user.bind('<FocusOut>', lambda x: self.on_leave('Full Name', self.user))

        self.phonenum = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.phonenum.place(x=30, y=225)
        self.phonenum.insert(0,"Phone Number")
        self.phonenum.bind('<FocusIn>', lambda x: self.on_enter(element=self.phonenum))
        self.phonenum.bind('<FocusOut>', lambda x: self.on_leave('Phone No.', self.phonenum))

        self.passcode = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.passcode.place(x=30, y=290)
        self.passcode.insert(0,"Password")
        self.passcode.bind('<FocusIn>', lambda x: self.on_enter(element=self.passcode))
        self.passcode.bind('<FocusOut>', lambda x: self.on_leave('Password', self.passcode))

        Button(frame,command=self.signUp,width=39,pady=7,text="Sign",bg="#CD3333", fg="white", border=0).place(x=35, y=334)

    def on_enter(self,element):
        element.delete(0, 'end')
    
    def on_leave(self, text, element):
        name = element.get()
        if name=='':
            element.insert(0,text)

    def signUp(self):
        print(self.user.get(),self.emailuser.get(),self.phonenum.get(),self.passcode.get())
        self.CONTROLLER.toSignIn()



if __name__=='__main__':
    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False,False)

    container = tk.Frame(root)
    container.pack(side = "top", fill = "both", expand = True)    
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    controller = None

    pg = SignUp(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()