import tkinter as tk
from tkinter import *
from tkinter import ttk

import os
import sys
sys.path.append(os.getcwd())

class ChangeLocation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller      
        #heading=tk.Label(self,text="Change Vehicle Location", fg="#F08080", bg="white",font=("Microsft YaHei UI Light",23,"bold"))
        #heading.place(x=100, y=15)
        '''CREATE TABLE IF NOT EXISTS Vehicle(
                        vehicle_id text PRIMARY KEY, 
                        vehicle_plate_num text,
                        vehicle_type text,
                        current_location text,
                        is_damaged boolean,
                        is_in_use boolean,
                        battery_percentage integer
                        );
        '''
        self.case = self.CONTROLLER.MODEL.DATA['vehicle'].get_vehicle_by_id()
        if(self.case != None):
            vehicle_heading_txt = "Vehicle Plate: " + self.case[1]
            current_location_txt = self.case[3]
        else:
            vehicle_heading_txt = "Vehicle Plate: "
            current_location_txt = "Current Location: "



        operatorMap = tk.Label(self, image = self.CONTROLLER.ASSETS['map'])
        operatorMap.pack(side='right')



        vehicle_heading = tk.Label(self, text=vehicle_heading_txt, fg="black", bg="white", font=("Microsft YaHei UI Light",25,"bold")) #update this to display vehicle make/ or number
        vehicle_heading.place(x=100, y=120)
        label1 = tk.Label(self, text="Current Location: ", fg="black", bg="white", font=("Microsft YaHei UI Light",16,"bold"))
        label1.place(x=100, y=200)

        location = tk.Label(self, text=current_location_txt, fg="black", bg="white", font=("Microsft YaHei UI Light",12,"bold")) #update this to display cars location
        location.place(x=320, y=200)

        self.change_location = ttk.Combobox(self, values=self.CONTROLLER.MODEL.DATA['vehicle'].get_all_location())
        self.change_location['state'] = 'readonly'
        self.change_location.place(x=100, y=250, width=390)
        
        Button(self,width=25,pady=7,text="CANCEL",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toOperatorHome).place(x=100, y=300)
        Button(self, width=25,pady=7,text="CONFIRM",bg="#CD3333", fg="white", border=0, command=self.submit_location).place(x=320, y=300)

    def submit_location(self):
        loc = self.change_location.get()
        print("Change location to: " + loc)
        self.CONTROLLER.MODEL.DATA['vehicle'].update_vehicle_location(location = loc)
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

    pg = ChangeLocation(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()