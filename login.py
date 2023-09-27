from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess


conn = sqlite3.connect('user_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')
conn.commit()

def signIn():
    username = user.get()
    password = passcode.get()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()

    if result:
        messagebox.showinfo("Login Successful", "Welcome, " + username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def signUp():
    subprocess.run(['python', '.\signup.py'])

def close_database():
    conn.close()

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='white')
root.resizable(False,False)


img = PhotoImage(file='carrent1.png')
Label(root,image=img, bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480, y=70)

heading=Label(frame,text="E-VEHICLE", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",23,"bold"))
heading.place(x=100, y=5)

#username box
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Email/ Name')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
user.place(x=30, y=80)
user.insert(0,"Email/ Name")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)

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
Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)


Button(frame,command=signIn,width=39,pady=7,text="Log in",bg="#CD3333", fg="white", border=0).place(x=35, y=204)

sign_up = Button(frame,command=signUp,width=6,text="SignUp",border=0,bg="white",fg="#732222")
sign_up.place(x=145, y=270)

root.protocol("WM_DELETE_WINDOW", close_database)
root.mainloop()