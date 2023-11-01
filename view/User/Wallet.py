import tkinter as tk
from tkinter import ttk, messagebox
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
        self.GLineEdit_515 = tk.Entry(self)
        self.GLineEdit_515["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        self.GLineEdit_515["font"] = ft
        self.GLineEdit_515["fg"] = "#333333"
        self.GLineEdit_515["bg"] = "white"
        self.GLineEdit_515["justify"] = "left"
        # self.GLineEdit_515["text"] = "Payment amount"
        self.GLineEdit_515.place(x=80, y=80, width=340, height=40)
        Frame(self,width=340, height=2, bg="black").place(x=80, y=120)

        self.GLineEdit_762 = tk.Entry(self)
        self.GLineEdit_762["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        self.GLineEdit_762["font"] = ft
        self.GLineEdit_762["fg"] = "#333333"
        self.GLineEdit_762["bg"] = "white"
        self.GLineEdit_762["justify"] = "left"
        # self.GLineEdit_762["text"] = "Entry"
        self.GLineEdit_762.place(x=80, y=210, width=340, height=40)
        Frame(self,width=340, height=2, bg="black").place(x=80, y=250)

        self.GLineEdit_48 = tk.Entry(self)
        self.GLineEdit_48["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        self.GLineEdit_48["font"] = ft
        self.GLineEdit_48["fg"] = "#333333"
        self.GLineEdit_48["justify"] = "left"
        # self.GLineEdit_48["text"] = "Entry"
        self.GLineEdit_48.place(x=80, y=390, width=70, height=40)
        Frame(self,width=70, height=2, bg="black").place(x=80, y=430)

        self.GLineEdit_346 = tk.Entry(self)
        self.GLineEdit_346["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        self.GLineEdit_346["font"] = ft
        self.GLineEdit_346["fg"] = "#333333"
        self.GLineEdit_346["justify"] = "left"
        # self.GLineEdit_346["text"] = "Entry"
        self.GLineEdit_346.place(x=80, y=300, width=340, height=40)
        Frame(self,width=340, height=2, bg="black").place(x=80, y=340)

        self.GLineEdit_24 = tk.Entry(self)
        self.GLineEdit_24["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        self.GLineEdit_24["font"] = ft
        self.GLineEdit_24["fg"] = "#333333"
        self.GLineEdit_24["justify"] = "left"
        # self.GLineEdit_24["text"] = "Entry"
        self.GLineEdit_24.place(x=180, y=390, width=70, height=40)
        Frame(self,width=70, height=2, bg="black").place(x=180, y=430)

        self.GLineEdit_248 = tk.Entry(self)
        self.GLineEdit_248["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial', size=13)
        self.GLineEdit_248["font"] = ft
        self.GLineEdit_248["fg"] = "#333333"
        self.GLineEdit_248["justify"] = "left"
        # self.GLineEdit_248["text"] = "Entry"
        # CVV hidden
        self.GLineEdit_248.config(show="*")
        self.GLineEdit_248.place(x=310, y=390, width=110, height=40)
        Frame(self,width=110, height=2, bg="black").place(x=310, y=430)

        self.GLabel_211 = tk.Label(self)
        # self.GLabel_211["anchor"] = "w"
        ft = tkFont.Font(family='Arial', size=18)
        self.GLabel_211["font"] = ft
        self.GLabel_211["fg"] = "black"
        self.GLabel_211["bg"] = "white"
        self.GLabel_211["justify"] = "center"
        self.GLabel_211["text"] = f"Current BALANCE: \n $ {self.CONTROLLER.MODEL.DATA['wallet'].balance}"
        self.GLabel_211["relief"] = "ridge"
        self.GLabel_211.place(x=550, y=80, width=306, height=225)

        self.GButton_651 = tk.Button(self)
        self.GButton_651["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=13)
        self.GButton_651["font"] = ft
        self.GButton_651["fg"] = "white"
        self.GButton_651["bg"] = "#CD3333"
        self.GButton_651["justify"] = "center"
        self.GButton_651["text"] = "CANCEL"
        self.GButton_651["border"] = "0"
        self.GButton_651.place(x=550, y=350, width=135, height=40)
        self.GButton_651["command"] = self.GButton_651_command

        self.GButton_721 = tk.Button(self)
        self.GButton_721["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial', size=13)
        self.GButton_721["font"] = ft
        self.GButton_721["fg"] = "white"
        self.GButton_721["bg"] = "#CD3333"
        self.GButton_721["border"] = "0"
        self.GButton_721["justify"] = "center"
        self.GButton_721["text"] = "ADD BALANCE"
        self.GButton_721.place(x=720, y=350, width=135, height=40)
        self.GButton_721["command"] = self.GButton_721_command

        self.GLabel_922 = tk.Label(self)
        ft = tkFont.Font(family='Arial', size=18)
        self.GLabel_922["font"] = ft
        self.GLabel_922["fg"] = "#333333"
        self.GLabel_922["bg"] = "white"
        self.GLabel_922["justify"] = "left"
        self.GLabel_922["anchor"]="w"
        self.GLabel_922["text"] = "Payment Amount: "
        self.GLabel_922.place(x=80, y=40, width=250, height=30)

        self.GLabel_801 = tk.Label(self)
        ft = tkFont.Font(family='Arial', size=16)
        self.GLabel_801["font"] = ft
        self.GLabel_801["fg"] = "#333333"
        self.GLabel_801["bg"] = "white"
        self.GLabel_801["justify"] = "left"
        self.GLabel_801["anchor"]="w"
        self.GLabel_801["text"] = "Bank Details: "
        self.GLabel_801.place(x=80, y=140, width=146, height=30)

        self.GLabel_28 = tk.Label(self)
        ft = tkFont.Font(family='Arial', size=13)
        self.GLabel_28["font"] = ft
        self.GLabel_28["fg"] = "#333333"
        self.GLabel_28["bg"] = "white"
        self.GLabel_28["justify"] = "left"
        self.GLabel_28["anchor"]="w"
        self.GLabel_28["text"] = "Card Holder's Name: "
        self.GLabel_28.place(x=80, y=170, width=154, height=32)

        self.GLabel_704 = tk.Label(self)
        ft = tkFont.Font(family='Arial', size=13)
        self.GLabel_704["font"] = ft
        self.GLabel_704["fg"] = "#333333"
        self.GLabel_704["bg"] = "white"
        self.GLabel_704["anchor"]="w"
        self.GLabel_704["justify"] = "left"
        self.GLabel_704["text"] = "Card Number: "
        self.GLabel_704.place(x=80, y=260, width=132, height=40)

        self.GLabel_date = tk.Label(self)
        ft = tkFont.Font(family='Arial', size=13)
        self.GLabel_date["font"] = ft
        self.GLabel_date["fg"] = "#333333"
        self.GLabel_date["bg"] = "white"
        self.GLabel_date["anchor"]="w"
        self.GLabel_date["justify"] = "left"
        self.GLabel_date["text"] = "Valid Date: "
        self.GLabel_date.place(x=80, y=360, width=132, height=40)


        self.GLabel_761 = tk.Label(self)
        ft = tkFont.Font(family='Arial', size=28)
        self.GLabel_761["font"] = ft
        self.GLabel_761["fg"] = "#333333"
        self.GLabel_761["bg"] = "white"
        self.GLabel_761["justify"] = "center"
        self.GLabel_761["text"] = "/"
        self.GLabel_761.place(x=150, y=390, width=32, height=40)

        self.GLabel_622 = tk.Label(self)
        ft = tkFont.Font(family='Arial', size=13)
        self.GLabel_622["font"] = ft
        self.GLabel_622["fg"] = "#333333"
        self.GLabel_622["bg"] = "white"
        self.GLabel_622["justify"] = "center"
        self.GLabel_622["text"] = "CCV: "
        self.GLabel_622.place(x=250, y=390, width=59, height=40)

    '''
        Cancel Button
    '''
    def GButton_651_command(self):
        self.CONTROLLER.toUserHome()

    '''
        Add Balance Button
    '''
    def GButton_721_command(self):
        if(not self.validate_card_info()):
            return
        amount = int(self.GLineEdit_515.get())
        self.CONTROLLER.MODEL.DATA['wallet'].add_balance(amount)
        self.CONTROLLER.toUserHome()
        # print("command")

    def validate_card_info(self):
        # get data
        card_holder = self.GLineEdit_762.get().strip()
        card_number = self.GLineEdit_346.get().strip()
        valid_month = self.GLineEdit_48.get().strip()
        valid_year = self.GLineEdit_24.get().strip()
        ccv = self.GLineEdit_248.get().strip()
        amount = self.GLineEdit_515.get().strip()
        if not card_holder:
            messagebox.showerror("Error", "Please enter card holder's name!")
            return False
        if len(card_number) != 16 or not card_number.isdigit():
            messagebox.showerror("Error", "Invalid card number! It should be 16 digits.")
            return False
        # Checking the valid month and year format
        if not (valid_month.isdigit() and 1 <= int(valid_month) <= 12):
            messagebox.showerror("Error", "Invalid valid month!")
            return False
        if not (valid_year.isdigit() and 23 <= int(valid_year) <= 99):
            messagebox.showerror("Error", "Invalid valid year!, need to be 2 digits and greater than 23.")
            return False
        if len(ccv) != 3 or not ccv.isdigit():
            messagebox.showerror("Error", "Invalid CCV! It should be 3 digits.")
            return False
        # if not self.luhn_check(card_number):
        #     messagebox.showerror("Error", "Invalid card number, Check again carefully!")
        #     return False
        # Identify card type
        if card_number.startswith("4"):
            messagebox.showinfo("Info", "Visa card pay successfully.")
        elif card_number.startswith("5"):
            messagebox.showinfo("Info", "Master card pay successfully.")
        elif card_number.startswith("62"):
            messagebox.showinfo("Info", "UnionPay card pay successfully.")
        else:
            messagebox.showerror("Error", "Invalid card number")
            return False
        if not amount.isdigit():
            messagebox.showerror("Error", "Invalid amount!")
            return False

        return True

    def luhn_check(self, card_number):
        """
        Check if the provided card number is valid according to the Luhn algorithm.

        :param card_number: A string representation of the card number.
        :return: True if valid, False otherwise.
        """
        # Remove any spaces or hyphens from the card number
        card_number = card_number.replace(" ", "").replace("-", "")

        # Convert the string to a list of integers
        numbers = [int(char) for char in card_number]

        # Reverse the order for easier processing
        numbers.reverse()

        # Double every second digit, starting from the rightmost
        for i in range(1, len(numbers), 2):
            numbers[i] *= 2
            if numbers[i] > 9:
                numbers[i] -= 9

        # If the sum of the digits is divisible by 10, then the number is valid
        return sum(numbers) % 10 == 0

    def refresh(self):
        self.GLineEdit_515.delete(0, END)
        self.GLineEdit_248.delete(0, END)
        self.GLabel_211["text"] = f"Current BALANCE: \n $ {self.CONTROLLER.MODEL.DATA['wallet'].balance}"
        self.GLabel_211.place(x=550, y=80, width=306, height=225)


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