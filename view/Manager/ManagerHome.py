import csv
import tkinter as tk
import datetime
from tkinter import *
from tkinter import filedialog

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
        self.start_label = tk.Label(self, text="Start Date (Included):", bg='white')
        self.start_label.place(x=170, y=100)

        self.start_date_picker = DateEntry(self)
        self.start_date_picker.place(x=320, y=100)

        # End Date Label and Picker
        self.end_label = tk.Label(self, text="End Date (Included):", bg='white')
        self.end_label.place(x=170, y=140)

        self.end_date_picker = DateEntry(self)
        self.end_date_picker.place(x=320, y=140)

        # Submit Button
        self.vehicle_usage_button = tk.Button(self, width=39, pady=7, text="Show Vehicle Usage", bg="#CD3333", fg="white", border=0,
               command=self.to_vehicle_usage)
        self.vehicle_usage_button.place(x=320, y=200)
        self.location_statistics_button = tk.Button(self, width=39, pady=7, text="Show Location Statistics", bg="#CD3333", fg="white", border=0,
                command=self.to_location_statistics)
        self.location_statistics_button.place(x=320, y=250)
        self.export_botton = tk.Button(self, width=39, pady=7, text="Export Order History to CSV", bg="#CD3333", fg="white", border=0,
                command=self.export_to_csv)
        self.export_botton.place(x=320, y=300)
        self.charge_statistics_button = tk.Button(self, width=39, pady=7, text="Show Charge Statistics", bg="#CD3333", fg="white", border=0,
                command=self.to_charge_statistics)
        self.charge_statistics_button.place(x=320, y=350)

    def to_charge_statistics(self):
        start_date = self.start_date_picker.get_date()
        end_date = self.end_date_picker.get_date()
        # end date need +1
        end_date = end_date + datetime.timedelta(days=1)
        print(start_date, end_date)
        self.CONTROLLER.MODEL.DATA['orders'].setDate(start_date, end_date)
        self.CONTROLLER.toChargeStatistics()

    def export_to_csv(self):
        start_date = self.start_date_picker.get_date()
        end_date = self.end_date_picker.get_date()
        # end date need +1
        end_date = end_date + datetime.timedelta(days=1)
        self.CONTROLLER.MODEL.DATA['orders'].setDate(start_date, end_date)
        data = self.CONTROLLER.MODEL.DATA['orders'].get_all_orders_in_select_date()

        # Prompt the user for a save location and filename
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        # If a path was selected
        if filepath:
            # Write data to the selected CSV file
            with open(filepath, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["order_id", "vehicle_id", "user_id", "end_time", "start_time", "pickup_location",
                                 "dropoff_location", "charge", "damage_id", "payment_done"])  # column headers
                writer.writerows(data)


    def to_vehicle_usage(self):
        start_date = self.start_date_picker.get_date()
        end_date = self.end_date_picker.get_date()
        # end date need +1
        end_date = end_date + datetime.timedelta(days=1)
        print(start_date, end_date)
        self.CONTROLLER.MODEL.DATA['orders'].setDate(start_date, end_date)
        self.CONTROLLER.toVehicleUsage()

    def to_location_statistics(self):
        start_date = self.start_date_picker.get_date()
        end_date = self.end_date_picker.get_date()
        # end date need +1
        end_date = end_date + datetime.timedelta(days=1)
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