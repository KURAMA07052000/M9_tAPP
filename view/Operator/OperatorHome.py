import tkinter as tk
from tkinter import *

import os
import sys
sys.path.append(os.getcwd())

class OperatorHome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller      
        heading=tk.Label(self,text="Operator Home", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        heading.pack(pady=10)
        heading.place(x=100, y=5)

        
        for index, entry in enumerate(self.CONTROLLER.MODEL.DATA['orderHistory'].order_history_user(self.CONTROLLER.MODEL.DATA['user'].UserID)):
            card = tk.Frame(self, bg='#CD3333', border=2, height=350, width=800, relief='solid', bd=4, borderwidth=4, highlightthickness=0, highlightcolor="#CD3333", highlightbackground="#CD3333")
            card.pack(pady=10)

            order_name = entry[1]  
            # start_time = entry[4]  
            # end_time = entry[3]    

            entry_label = tk.Label(card, fg="white", bg="#CD3333", text=f"Order {index+1}: Name - {order_name}")
            entry_label.grid(row=0, column=0, sticky='w', padx=(160, 0))

            change_location = tk.Button(card, fg="#CD3333", bg="white", text="CHANGE LOCATION", command=self.CONTROLLER.toChangeLocation)
            change_location.grid(row=0, column=2, sticky='e', padx=(0, 160))

            report = tk.Button(card, fg="#CD3333", bg="white", text="LOAD REPORT")
            report.grid(row=0, column=1, padx=(160,160))

            card.grid_columnconfigure(1, weight=1)
        
if __name__=='__main__':
    from controller.Controller import Controller

    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False,False)

    container = tk.Frame(root)
    container.pack(side = "top", fill = "both", expand = True)    
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    controller = Controller()
    controller.setView(root)

    pg = OperatorHome(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()