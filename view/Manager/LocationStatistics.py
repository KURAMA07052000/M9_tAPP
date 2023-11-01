import tkinter as tk
from tkinter import *
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.append(os.getcwd())

class LocationStatistics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller

        # Heading
        heading = tk.Label(self, text="Location Statistics", fg="#F08080", bg="white", font=("Microsft YaHei UI Light", 23, "bold"))
        heading.place(x=320, y=20)

        # Logout button
        logout = Button(self, image=self.CONTROLLER.ASSETS['logoutbutton'], border=0, bg="white", command=self.CONTROLLER.logout)
        logout.place(x=850, y=10)

        # get Data
        self.get_location_statistics_data()
        # self.pickup_data = {"LocationA": 10, "LocationB": 15, "LocationC": 25}
        # self.dropoff_data = {"LocationA": 20, "LocationB": 10, "LocationC": 20}

        # Plotting location data
        self.plot_pickup_locations()
        self.plot_dropoff_locations()
        Button(self, width=25, pady=7, text="RETURN", bg="#CD3333", fg="white", border=0,
               command=self.CONTROLLER.toManagerHome).place(x=700, y=450)

    def get_location_statistics_data(self):
        self.pickup_data = self.CONTROLLER.MODEL.DATA['orders'].get_pickup_location_statistics_data()
        self.dropoff_data = self.CONTROLLER.MODEL.DATA['orders'].get_dropoff_location_statistics_data()



    def plot_pickup_locations(self):
        labels = list(self.pickup_data.keys())
        sizes = list(self.pickup_data.values())

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title('pick up location statistics')

        # Embed the pie chart in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=0, y=80)
        canvas.draw()

    def plot_dropoff_locations(self):
        labels = list(self.dropoff_data.keys())
        sizes = list(self.dropoff_data.values())

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title('drop off location statistics')

        # Embed the pie chart in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=400, y=80)
        canvas.draw()


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

    pg = LocationStatistics(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()