import tkinter as tk
from tkinter import *
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.append(os.getcwd())

class VehicleUsage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller

        # Heading
        heading = tk.Label(self, text="Vehicle Usage", fg="#F08080", bg="white", font=("Microsft YaHei UI Light", 23, "bold"))
        heading.place(x=320, y=20)

        # Logout button
        logout = Button(self, image=self.CONTROLLER.ASSETS['logoutbutton'], border=0, bg="white", command=self.CONTROLLER.logout)
        logout.place(x=850, y=10)

        # Fetching the vehicle usage data
        self.vehicle_usage_data = self.get_vehicle_usage_data()

        # Plotting vehicle usage data
        self.plot_vehicle_usage()
        Button(self, width=25, pady=7, text="RETURN", bg="#CD3333", fg="white", border=0,
               command=self.CONTROLLER.toManagerHome).place(x=700, y=450)

    def get_vehicle_usage_data(self):
        vehicle_usage_data = self.CONTROLLER.MODEL.DATA['orders'].get_vehicle_usage_data()
        return vehicle_usage_data

        # return {
        #     "AB1234": 5,
        #     "BC2345": 3,
        #     "CD3456": 10,
        #     "DE4567": 8
        # }


    def plot_vehicle_usage(self):
        if(self.vehicle_usage_data == None or len(self.vehicle_usage_data) == 0):
            return
        vehicles = list(self.vehicle_usage_data.keys())
        usages = list(self.vehicle_usage_data.values())

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(vehicles, usages, color='#F08080')
        ax.set_xlabel('Plate Number')
        ax.set_ylabel('Usage')
        ax.set_title('Vehicle Usage')
        # Ensure y-axis is integer
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

        # Embed the plot in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=80, y=80)
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

    pg = VehicleUsage(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()