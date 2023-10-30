import tkinter as tk
from tkinter import *
from tkinter import ttk

import os
import sys
sys.path.append(os.getcwd())

class ConditionReport(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller      
        #heading=tk.Label(self,text="Change Vehicle Location", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        #heading.place(x=100, y=15)
        
        battery = Button(self, image = self.CONTROLLER.ASSETS['batterybutton'], border=0, bg="white")
        battery.place(x=850,y=10)

        self.case = self.CONTROLLER.MODEL.DATA['damage_report'].get_damage_case(self.CONTROLLER.MODEL.DATA['vehicle'].VehicleID)
        if(self.case != None):
            print(self.case)
            vh_text = "Vehivle ID: " + self.case[1]
            vehicle_heading = tk.Label(self, text=vh_text, fg="black", bg="white", font=(
            "Microsft YaHei UI Light", 25, "bold"))  # update this to display vehicle make/ or number
            vehicle_heading.pack(pady=180)
            label1_text = "Damage: " + self.case[2]
            label1 = tk.Label(self, text=label1_text, fg="black", bg="white",
                              font=("Microsft YaHei UI Light", 16, "bold"))
            label1.place(x=370, y=250)
        else:
            vehicle_heading = tk.Label(self, text="All vehicles are good", fg="black", bg="white", font=(
            "Microsft YaHei UI Light", 25, "bold"))  # update this to display vehicle make/ or number
            vehicle_heading.pack(pady=180)
        # vehicle_heading = tk.Label(self, text="Car 1", fg="black", bg="white", font=("Microsft YaHei UI Light",25,"bold")) #update this to display vehicle make/ or number
        # vehicle_heading.pack(pady=180)
        #
        # label1 = tk.Label(self, text="Current Condition", fg="black", bg="white", font=("Microsft YaHei UI Light",16,"bold"))
        # label1.place(x = 370, y=250)
        
        Button(self,width=39,pady=7,text="CANCEL",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toOperatorHome).place(x=140, y=350)
        Button(self, width=39,pady=7,text="CAR HAS BEEN FIXED",bg="#CD3333", fg="white", border=0, command=self.fix_vehicle).place(x=520, y=350)

    def fix_vehicle(self):
        self.CONTROLLER.MODEL.DATA['damage_report'].fixd_vehicle(self.case[0])
        self.CONTROLLER.toOperatorHome()


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

    pg = ConditionReport(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()