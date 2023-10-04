import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

import os
import sys

sys.path.append(os.getcwd())


class UserHome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller

        frame = Frame(root, width=350, height=900, bg='white')
        frame.place(x=287.5, y=30)

        heading = Label(frame, text="HOME", fg="#F08080", bg="white", font=("Microsft YaHei UI Light", 23, "bold"))
        heading.place(x=144, y=0)
        heading["justify"] = "center"

        # Home btn
        def rentACar():
            print("rent a car page")

        rentACar = Button(frame, text="Rent a Car", fg="white", border=0, bg="#CD3333", command=rentACar, width=30,
                          height=2)
        rentACar["justify"] = "center"

        def returnACar():
            print("return a car page")

        returnACar = Button(frame, text="Return a Car", fg="white", border=0, bg="#CD3333", command=returnACar,
                            width=30, height=2)
        returnACar["justify"] = "center"

        def reportACar():
            print("report a car page")

        reportACar = Button(frame, text="Report a Car", fg="white", border=0, bg="#CD3333", command=reportACar,
                            width=30, height=2)
        reportACar["justify"] = "center"

        def showOrderHistory():
            print("show order history page")

        showOrderHistory = Button(frame, text="Show Order History", fg="white", border=0, bg="#CD3333",
                                  command=showOrderHistory, width=30, height=2)
        showOrderHistory["justify"] = "center"

        rentACar.place(x=70, y=80)
        returnACar.place(x=70, y=180)
        reportACar.place(x=70, y=280)
        showOrderHistory.place(x=70, y=380)



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False, False)

    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    controller = None

    pg = UserHome(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()