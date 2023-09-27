from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='white')
root.resizable(False,False)

img = PhotoImage(file='carrent1.png')
Label(root,image=img, bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480, y=70)

heading=Label(frame,text="LOG IN", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",23,"bold"))
heading.place(x=100, y=5)

#username box
user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
user.place(x=30, y=80)
user.insert(0,"Email/ Name")
Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)

#password box
code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
code.place(x=30, y=150)
code.insert(0,"Password")
Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)


Button(frame,width=39,pady=7,text="Log in",bg="#CD3333", fg="white", border=0).place(x=35, y=204)

sign_up = Button(frame,width=6,text="SignUp",border=0,bg="white",fg="#732222")
sign_up.place(x=145, y=270)

root.mainloop()