from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess

# Initialize SQLite database
conn = sqlite3.connect('user_database.db')
c = conn.cursor()

# Create a table to store user information
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')
conn.commit()


def signUp():
    username = user.get()
    name = userfullname.get()
    password = passcode.get()

    # Check if username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()

    if result:
        messagebox.showerror("Sign Up Failed", "Username already exists")
    else:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username,name, password))
        conn.commit()
        messagebox.showinfo("Sign Up Successful", "You can now log in")

def close_database():
    conn.close()

root=Tk()
root.title('SignUp')
root.geometry('925x500+300+200')
root.configure(bg='white')
root.resizable(False,False)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480, y=70)

heading=Label(frame,text="SIGN UP", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",23,"bold"))
heading.place(x=100, y=5)

#username box
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Email')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
user.place(x=30, y=80)
user.insert(0,"Email")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)

#username box
def on_enter(e):
    userfullname.delete(0, 'end')
def on_leave(e):
    name = userfullname.get()
    if name=='':
        userfullname.insert(0,'Name')

userfullname = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
userfullname.place(x=30, y=80)
userfullname.insert(0,"Name")
userfullname.bind('<FocusIn>', on_enter)
userfullname.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)

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
Frame(frame, width=295, height=2, bg="black").place(x=25,y=247)


Button(frame,command=signUp,width=39,pady=7,text="Sign",bg="#CD3333", fg="white", border=0).place(x=35, y=274)



root.protocol("WM_DELETE_WINDOW", close_database)
root.mainloop()
