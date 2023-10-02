import tkinter as tk
from tkinter import ttk
from tkinter import *


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
        
        for F in [StartPage, Page2]:
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        #img = PhotoImage(file='carrent1.png', master=self)
        #Label(self,image=img, bg='white').place(x=50,y=50)
        
        ttk.Label(self,text='Image here').place(x=50,y=50)
        
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
        
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text ="Page 1",
                             command = lambda : controller.show_frame(StartPage))
        
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

app = tkinterApp()
app.mainloop()
