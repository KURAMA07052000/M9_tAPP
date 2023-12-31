import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os

class SignUp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        self.CONTROLLER = controller

        frame=Frame(self,width=350,height=650,bg='white')
        frame.pack(pady=70)

        heading=Label(frame,text="SIGN UP", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",19,"bold"))
        heading.place(x=100, y=0)

        self.emailuser = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.emailuser.place(x=30, y=30)
        self.emailuser.insert(0,"Email")
        self.emailuser.bind('<FocusIn>', lambda x: self.on_enter(element=self.emailuser))
        self.emailuser.bind('<FocusOut>', lambda x: self.on_leave('Email', self.emailuser))
        Frame(frame, width=295, height=2, bg="black").place(x=25,y=57)

        self.user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.user.place(x=30, y=95)
        self.user.insert(0,"Full Name")
        self.user.bind('<FocusIn>', lambda x: self.on_enter(self.user))
        self.user.bind('<FocusOut>', lambda x: self.on_leave('Full Name', self.user))
        Frame(frame, width=295, height=2, bg="black").place(x=25,y=127)

        self.phonenum = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.phonenum.place(x=30, y=170)
        self.phonenum.insert(0,"Phone Number")
        self.phonenum.bind('<FocusIn>', lambda x: self.on_enter(element=self.phonenum))
        self.phonenum.bind('<FocusOut>', lambda x: self.on_leave('Phone No.', self.phonenum))
        Frame(frame, width=295, height=2, bg="black").place(x=25,y=197)

        self.passcode = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        self.passcode.place(x=30, y=235)
        self.passcode.insert(0,"Password")
        self.passcode.bind('<FocusIn>', lambda x: self.on_enter(element=self.passcode))
        self.passcode.bind('<FocusOut>', lambda x: self.on_leave('Password', self.passcode))
        # hidden passccode
        self.passcode.config(show="*")
        Frame(frame, width=295, height=2, bg="black").place(x=25,y=267)

        self.user_type = ttk.Combobox(frame, values=["customer", "admin", "manager"], width=23)
        self.user_type.place(x=30, y=275, width=285)
        self.user_type.set("Select User Type")
        self.user_type['state'] = 'readonly'

        Button(frame,command=self.signUp,width=39,pady=7,text="Sign",bg="#CD3333", fg="white", border=0).place(x=35, y=315)

    def on_enter(self,element):
        element.delete(0, 'end')
    
    def on_leave(self, text, element):
        name = element.get()
        if name=='':
            element.insert(0,text)

    def signUp(self):
        print(self.user.get(), self.emailuser.get(), self.phonenum.get(), self.passcode.get(), self.user_type.get())

        email = self.emailuser.get().strip()
        fullname = self.user.get().strip()
        phonenum = self.phonenum.get().strip()
        password = self.passcode.get().strip()
        user_type = self.user_type.get().strip()

        # 检查各项输入
        if not email or "@" not in email:
            messagebox.showwarning("Warning", "Please enter a valid Email.")
            return
        if not fullname:
            messagebox.showwarning("Warning", "Please enter a Full Name.")
            return
        if not phonenum.isdigit():
            messagebox.showwarning("Warning", "Please enter a valid Phone Number.")
            return
        if not password or len(password) < 6:
            messagebox.showwarning("Warning", "Password must be at least 6 characters.")
            return
        if user_type not in ["customer", "admin", "manager"]:
            messagebox.showwarning("Warning", "Please select a valid User Type.")
            return
        # all pass
        print(email, fullname, phonenum, password, user_type)
        if(self.CONTROLLER.signup(fullname, email, phonenum, password, user_type) == False):
            # sign up fail
            messagebox.showerror("Sign Up Failed", "This email has been registered.")
            return


    def refresh(self):
        self.emailuser.delete(0,END)
        self.user.delete(0,END)
        self.phonenum.delete(0,END)
        self.passcode.delete(0,END)

        self.emailuser.insert(0,"Email")
        self.user.insert(0,"Full Name")
        self.phonenum.insert(0,"Phone Number")
        self.passcode.insert(0,"Password")
        self.user_type.set("Select User Type")

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
