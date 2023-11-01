import tkinter as tk
from tkinter import *
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.append(os.getcwd())

class ChargeStatistics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller

        # Heading
        heading = tk.Label(self, text="Charge Statistics", fg="#F08080", bg="white", font=("Microsft YaHei UI Light", 23, "bold"))
        heading.place(x=320, y=20)

        # Logout button
        logout = Button(self, image=self.CONTROLLER.ASSETS['logoutbutton'], border=0, bg="white", command=self.CONTROLLER.logout)
        logout.place(x=850, y=10)

        # get Data
        self.get_charge_statistics_data()
        # draw graph
        self.draw_chart()

        Button(self, width=25, pady=7, text="RETURN", bg="#CD3333", fg="white", border=0,
               command=self.CONTROLLER.toManagerHome).place(x=700, y=450)


    def get_charge_statistics_data(self):
        self.data = self.CONTROLLER.MODEL.DATA['orders'].get_charge_statistics_data()
        for i in self.data:
            print(i, self.data[i])
    def draw_chart(self):
        vehicle_plates = list(self.data.keys())
        real_charges = list(self.data.values())
        total_charge = sum(real_charges)
        charges = [(charge / total_charge) * 100 for charge in real_charges]

        fig, ax = plt.subplots(figsize=(6, 4.5))      # scale smaller

        ax.bar(vehicle_plates, charges, color='#F08080')
        ax.set_xlabel('Vehicle Plate Number')
        ax.set_ylabel('Charge Percentage')
        ax.set_title('Total Charge per Vehicle')
        ax.tick_params(axis='x', rotation=30)  # Rotate x labels for better visualization
        ax.tick_params(axis='x', labelsize=8)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(padx=10, pady=10)



if __name__=='__main__':
    from controller.Controller import Controller

    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False,False)

    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    controller = Controller()
    controller.setView(root)

    pg = ChargeStatistics(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()