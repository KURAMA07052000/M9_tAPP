from tkinter import *
from tkinter import messagebox
from user_database import connect_database, close_database, insert_user

def signUp():
    conn, c = connect_database()

    username = user.get()
    phone = phonenum.get()
    email = emailuser.get()
    password = passcode.get()

    if not (username and email and password and phone):
        messagebox.showerror("Error", "All fields must be filled")
        return
    insert_user(conn, c, username, password, email, phone, "", "", "customer")
    close_database(conn)
    messagebox.showinfo("Success", "User registered successfully")

root=Tk()
root.title('SignUp')
root.geometry('925x500+300+200')
root.configure(bg='white')
root.resizable(False,False)

frame=Frame(root,width=350,height=650,bg='white')
frame.pack(pady=70)

heading=Label(frame,text="SIGN UP", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",23,"bold"))
heading.place(x=100, y=5)

#email box
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
Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)

#username box
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Full Name')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
user.place(x=30, y=155)
user.insert(0,"Full Name")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)

# username box
def on_enter(e):
    phonenum.delete(0, 'end')
def on_leave(e):
    name = phonenum.get()
    if name=='':
        phonenum.insert(0,'Phone Number')

phonenum = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
phonenum.place(x=30, y=225)
phonenum.insert(0,"Phone Number")
phonenum.bind('<FocusIn>', on_enter)
phonenum.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25,y=247)

#password box
def on_enter(e):
    passcode.delete(0, 'end')
def on_leave(e):
    name = passcode.get()
    if name=='':
        passcode.insert(0,'Password')

passcode = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
passcode.place(x=30, y=290)
passcode.insert(0,"Password")
passcode.bind('<FocusIn>', on_enter)
passcode.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25,y=317)


Button(frame,command=signUp,width=39,pady=7,text="Sign",bg="#CD3333", fg="white", border=0).place(x=35, y=334)




root.mainloop()
