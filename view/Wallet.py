import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

import os
import sys

sys.path.append(os.getcwd())


class Wallet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller
        GLineEdit_515 = tk.Entry(root)
        GLineEdit_515["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        GLineEdit_515["font"] = ft
        GLineEdit_515["fg"] = "#333333"
        GLineEdit_515["bg"] = "white"
        GLineEdit_515["justify"] = "left"
        # GLineEdit_515["text"] = "Payment amount"
        GLineEdit_515.place(x=80, y=80, width=340, height=40)
        Frame(width=340, height=2, bg="black").place(x=80, y=120)

        GLineEdit_762 = tk.Entry(root)
        GLineEdit_762["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        GLineEdit_762["font"] = ft
        GLineEdit_762["fg"] = "#333333"
        GLineEdit_762["bg"] = "white"
        GLineEdit_762["justify"] = "left"
        # GLineEdit_762["text"] = "Entry"
        GLineEdit_762.place(x=80, y=210, width=340, height=40)
        Frame(width=340, height=2, bg="black").place(x=80, y=250)

        GLineEdit_48 = tk.Entry(root)
        GLineEdit_48["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        GLineEdit_48["font"] = ft
        GLineEdit_48["fg"] = "#333333"
        GLineEdit_48["justify"] = "left"
        # GLineEdit_48["text"] = "Entry"
        GLineEdit_48.place(x=80, y=390, width=70, height=40)
        Frame(width=70, height=2, bg="black").place(x=80, y=430)

        GLineEdit_346 = tk.Entry(root)
        GLineEdit_346["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        GLineEdit_346["font"] = ft
        GLineEdit_346["fg"] = "#333333"
        GLineEdit_346["justify"] = "left"
        # GLineEdit_346["text"] = "Entry"
        GLineEdit_346.place(x=80, y=300, width=340, height=40)
        Frame(width=340, height=2, bg="black").place(x=80, y=340)

        GLineEdit_24 = tk.Entry(root)
        GLineEdit_24["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        GLineEdit_24["font"] = ft
        GLineEdit_24["fg"] = "#333333"
        GLineEdit_24["justify"] = "left"
        # GLineEdit_24["text"] = "Entry"
        GLineEdit_24.place(x=180, y=390, width=70, height=40)
        Frame(width=70, height=2, bg="black").place(x=180, y=430)

        GLineEdit_248 = tk.Entry(root)
        GLineEdit_248["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        GLineEdit_248["font"] = ft
        GLineEdit_248["fg"] = "#333333"
        GLineEdit_248["justify"] = "left"
        # GLineEdit_248["text"] = "Entry"
        GLineEdit_248.place(x=310, y=390, width=110, height=40)
        Frame(width=110, height=2, bg="black").place(x=310, y=430)

        GLabel_211 = tk.Label(root)
        # GLabel_211["anchor"] = "w"
        ft = tkFont.Font(family='Arial', size=18)
        GLabel_211["font"] = ft
        GLabel_211["fg"] = "black"
        GLabel_211["bg"] = "white"
        GLabel_211["justify"] = "center"
        GLabel_211["text"] = "Current BALANCE: \n $ 3000000"
        GLabel_211["relief"] = "ridge"
        GLabel_211.place(x=550, y=80, width=306, height=225)

        GButton_651 = tk.Button(root)
        GButton_651["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=13)
        GButton_651["font"] = ft
        GButton_651["fg"] = "white"
        GButton_651["bg"] = "#CD3333"
        GButton_651["justify"] = "center"
        GButton_651["text"] = "CANCEL"
        GButton_651["border"] = "0"
        GButton_651.place(x=550, y=350, width=135, height=40)
        GButton_651["command"] = self.GButton_651_command

        GButton_721 = tk.Button(root)
        GButton_721["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=13)
        GButton_721["font"] = ft
        GButton_721["fg"] = "white"
        GButton_721["bg"] = "#CD3333"
        GButton_721["border"] = "0"
        GButton_721["justify"] = "center"
        GButton_721["text"] = "ADD BALANCE"
        GButton_721.place(x=720, y=350, width=135, height=40)
        GButton_721["command"] = self.GButton_721_command

        GLabel_922 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=18)
        GLabel_922["font"] = ft
        GLabel_922["fg"] = "#333333"
        GLabel_922["bg"] = "white"
        GLabel_922["justify"] = "left"
        GLabel_922["anchor"]="w"
        GLabel_922["text"] = "Payment Amount: "
        GLabel_922.place(x=80, y=40, width=250, height=30)

        GLabel_801 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=16)
        GLabel_801["font"] = ft
        GLabel_801["fg"] = "#333333"
        GLabel_801["bg"] = "white"
        GLabel_801["justify"] = "left"
        GLabel_801["anchor"]="w"
        GLabel_801["text"] = "Bank Details: "
        GLabel_801.place(x=80, y=140, width=146, height=30)

        GLabel_28 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=13)
        GLabel_28["font"] = ft
        GLabel_28["fg"] = "#333333"
        GLabel_28["bg"] = "white"
        GLabel_28["justify"] = "left"
        GLabel_28["anchor"]="w"
        GLabel_28["text"] = "Card Holder's Name: "
        GLabel_28.place(x=80, y=170, width=154, height=32)

        GLabel_704 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=13)
        GLabel_704["font"] = ft
        GLabel_704["fg"] = "#333333"
        GLabel_704["bg"] = "white"
        GLabel_704["anchor"]="w"
        GLabel_704["justify"] = "left"
        GLabel_704["text"] = "Card Number: "
        GLabel_704.place(x=80, y=260, width=132, height=40)

        GLabel_date = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=13)
        GLabel_date["font"] = ft
        GLabel_date["fg"] = "#333333"
        GLabel_date["bg"] = "white"
        GLabel_date["anchor"]="w"
        GLabel_date["justify"] = "left"
        GLabel_date["text"] = "Valid Date: "
        GLabel_date.place(x=80, y=360, width=132, height=40)


        GLabel_761 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=28)
        GLabel_761["font"] = ft
        GLabel_761["fg"] = "#333333"
        GLabel_761["bg"] = "white"
        GLabel_761["justify"] = "center"
        GLabel_761["text"] = "/"
        GLabel_761.place(x=150, y=390, width=32, height=40)

        GLabel_622 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=13)
        GLabel_622["font"] = ft
        GLabel_622["fg"] = "#333333"
        GLabel_622["bg"] = "white"
        GLabel_622["justify"] = "center"
        GLabel_622["text"] = "CCV: "
        GLabel_622.place(x=250, y=390, width=59, height=40)

    def GButton_651_command(self):
        print("command")

    def GButton_721_command(self):
        print("command")



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False, False)
    root.title('Wallet')

    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    controller = None

    pg = Wallet(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()