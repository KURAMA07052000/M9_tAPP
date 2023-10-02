import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

class SignIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        logo_path = os.path.join(os.path.join(os.getcwd(),'assets'),'carrent1.png')
        img = ttk.PhotoImage(file=logo_path, master=self)
        ttk.Label(self,image=img).place(x=50,y=50)
        
        #ttk.Label(self,text='Image here').place(x=50,y=50)
        
        frame=ttk.Frame(self,width=350,height=350)
        frame.place(x=480, y=70)
        
        heading=ttk.Label(frame,text="E-VEHICLE", font=("Microsft YaHei UI Light",23,"bold"))
        heading.place(x=100, y=5)
        
        #username box
        def on_enter(e):
            emailuser.delete(0, 'end')
        def on_leave(e):
            name = emailuser.get()
            if name=='':
                emailuser.insert(0,'Email')

        emailuser = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        emailuser.place(x=30, y=80)
        emailuser.insert(0,"Email")
        emailuser.bind('<FocusIn>', on_enter)
        emailuser.bind('<FocusOut>', on_leave)
        #Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)
        
        #password box
        def on_enter(e):
            passcode.delete(0, 'end')
        def on_leave(e):
            name = passcode.get()
            if name=='':
                passcode.insert(0,'Password')

        passcode = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        passcode.place(x=30, y=150)
        passcode.insert(0,"Password")
        passcode.bind('<FocusIn>', on_enter)
        passcode.bind('<FocusOut>', on_leave)
        
        Button(frame,command=self.signIn,width=39,pady=7,text="Log in",bg="#CD3333", fg="white", border=0).place(x=35, y=204)

        sign_up = Button(frame,command=lambda : controller.show_frame(Page2),width=6,text="SignUp",border=0,bg="white",fg="#732222")
        sign_up.place(x=145, y=270)
        
    def signIn():
        print('yayy')


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

    pg = SignIn(container, controller)
    pg.place(x=0,y=0)

    root.mainloop()