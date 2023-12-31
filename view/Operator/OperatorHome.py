import tkinter as tk
from tkinter import *
from tkinter import ttk, Scrollbar
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

        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.container = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.container, anchor='nw')

        logout = Button(self, image = self.CONTROLLER.ASSETS['logoutbutton'], border=0, bg="white", command=self.CONTROLLER.logout)
        logout.place(x=850,y=10)

        for index, entry in enumerate(self.CONTROLLER.MODEL.DATA['vehicle'].get_vehicle_list()):
            card = tk.Frame(self.container, bg='#CD3333', border=2, height=350, width=500, relief='solid', bd=4, borderwidth=4,
                            highlightthickness=0, highlightcolor="#CD3333", highlightbackground="#CD3333")
            card.pack(pady=10)

            vehicle_plate = entry[1]
            battery_percentage = entry[6]

            entry_text = f"Vehicle {index+1}: {vehicle_plate} - {battery_percentage}%"

            entry_label = tk.Label(card, fg="white", bg="#CD3333", text=entry_text)
            entry_label.grid(row=0, column=0, sticky='w', padx=(120, 0))

            change_location = tk.Button(card, fg="#CD3333", bg="white", text="CHANGE LOCATION",
                                        command=lambda entry_id=entry[0]: self.toChangeLocation(entry_id))
            change_location.grid(row=0, column=2, sticky='e', padx=(0, 120))

            report = tk.Button(card, fg="#CD3333", bg="white", text="CONDITION REPORT",
                               command=lambda entry_id=entry[0]: self.toConditionReport(entry_id))
            report.grid(row=0, column=1, padx=(120, 120))

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def toConditionReport(self, vehicle_id):
        self.CONTROLLER.MODEL.DATA['vehicle'].set_vehicle_id(vehicle_id)
        self.CONTROLLER.toConditionReport()

    def toChangeLocation(self, vehicle_id):
        self.CONTROLLER.MODEL.DATA['vehicle'].set_vehicle_id(vehicle_id)
        self.CONTROLLER.toChangeLocation()

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