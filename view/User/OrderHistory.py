import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

from controller.Controller import *
import os
import sys

sys.path.append(os.getcwd())


class OrderHistory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller
        
        heading=tk.Label(self,text="Your Order History", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        heading.pack(pady=10)
        #Implement the for loop below passing the order data as an argument when ready yall, added it for now
        #for index, entry in enumerate("enter argument here"):
            # card = tk.Frame(self, bg='#CD3333', border=2, height=350, width=800, relief='solid', bd=4, borderwidth=4, highlightthickness=0, highlightcolor="#CD3333", highlightbackground="#CD3333")
            # card.pack(pady=50)

            # entry_label = tk.Label(card, fg="white", bg="#CD3333", text=f"Order {index+1}: {entry}")
            # entry_label.grid(row=0, column=0, sticky='w', padx=(160, 0))

            # modify = tk.Button(card, bg="white", fg="#CD3333", justify="center", text="MODIFY", border=0)
            # modify.grid(row=0, column=2, sticky='e', padx=(0, 160))

            # activity = tk.Label(card, bg="#CD3333", fg="white", justify="center", text="ACTIVE/NON-ACTIVE", border="0")
            # activity.grid(row=0, column=1, padx=(160,160))

            # card.grid_columnconfigure(1, weight=1)
        
        #when implementing the for loop delete this body of code, purly for show
        card = tk.Frame(self, bg='#CD3333', border=2, height=350, width=800, relief='solid', bd=4, borderwidth=4, highlightthickness=0, highlightcolor="#CD3333", highlightbackground="#CD3333")
        #card.grid(row=0, column=0, columnspan=3, pady=(80, 0))
        card.pack(pady=50)
        entry_label = Label(card, fg="white", bg="#CD3333", text=f"Order")
        entry_label.grid(row=0, column=0, sticky='w', padx=(160, 0))
        modify = Button(card, bg="white", fg="#CD3333", justify="center", text="MODIFY", border=0)
        modify.grid(row=0, column=2, sticky='e', padx=(0, 160))
        activity = Label(card, bg="#CD3333", fg="white", justify="center", text="ACTIVE/NON-ACTIVE", border="0")
        activity.grid(row=0, column=1, padx=(160,160))
        card.grid_columnconfigure(1, weight=1)

        Button(self,width=39,pady=7,text="CANCEL",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toUserHome).place(x=140, y=400)
        Button(self, width=39,pady=7,text="CONFIRM",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toWallet).place(x=520, y=400)

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


    pg = OrderHistory(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()