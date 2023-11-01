import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
import os
import sys

sys.path.append(os.getcwd())


class ManagerHome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller

        # Heading
        heading = tk.Label(self, text="Manager Home", fg="#F08080", bg="white",
                           font=("Microsft YaHei UI Light", 23, "bold"))
        heading.place(x=320, y=20)

        # Logout button
        logout = Button(self, image=self.CONTROLLER.ASSETS['logoutbutton'], border=0, bg="white",
                        command=self.CONTROLLER.logout)
        logout.place(x=850, y=10)

        # Start Date Label and Picker
        self.start_label = tk.Label(self, text="Start Date:", bg='white')
        self.start_label.place(x=220, y=100)

        self.start_date_picker = DateEntry(self)
        self.start_date_picker.place(x=320, y=100)

        # End Date Label and Picker
        self.end_label = tk.Label(self, text="End Date:", bg='white')
        self.end_label.place(x=220, y=140)

        self.end_date_picker = DateEntry(self)
        self.end_date_picker.place(x=320, y=140)

        # Submit Button
        self.vehicle_usage_button = tk.Button(self, width=39, pady=7, text="Show Vehicle Usage", bg="#CD3333", fg="white", border=0,
               command=self.to_vehicle_usage)
        self.vehicle_usage_button.place(x=320, y=200)
        self.location_statistics_button = tk.Button(self, width=39, pady=7, text="Show Location Statistics", bg="#CD3333", fg="white", border=0,
                command=self.to_location_statistics)
        self.location_statistics_button.place(x=320, y=250)

    def to_vehicle_usage(self):
        start_date = self.start_date_picker.get_date()
        end_date = self.end_date_picker.get_date()
        print(start_date, end_date)
        self.CONTROLLER.MODEL.DATA['orders'].setDate(start_date, end_date)
        self.CONTROLLER.toVehicleUsage()

    def to_location_statistics(self):
        start_date = self.start_date_picker.get_date()
        end_date = self.end_date_picker.get_date()
        print(start_date, end_date)
        self.CONTROLLER.MODEL.DATA['orders'].setDate(start_date, end_date)
        self.CONTROLLER.toLocationStatistics()



if __name__ == '__main__':
    from controller.Controller import Controller

    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False, False)

    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    controller = Controller()
    controller.setView(root)

    pg = ManagerHome(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()