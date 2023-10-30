import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

class ReturnCar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        self.CONTROLLER = controller

        # get data
        # self.order = self.get_data()
        self.order = self.CONTROLLER.MODEL.DATA['orders'].get_active_order(self.CONTROLLER.MODEL.DATA['user'].UserID)
        print(self.order)
        # to string
        if (self.order == None):
            order_str = "No Active Order"
        else:
            order_str = "Pick Up Loc: " + self.order.pickup_location + " | Order ID: " + self.order.get_order_id()[-5:]
        print(order_str)
        style = ttk.Style()
        style.configure('Red.TCombobox', fieldbackground='red', foreground='black')
        style.map('Red.TCombobox', background=[('readonly', 'red')])

        heading=Label(self, text="Return A Vehicle", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",19,"bold"))
        heading.place(x=362, y=16)

        self.vehicle = ttk.Combobox(self,values=[order_str], style='Red.TCombobox', justify='center')

        self.vehicle.place(x=100, y=120, width=285, height=30)
        self.vehicle.set("Chose your vehicle")
        # TODO: location
        self.drop_off_loc = ttk.Combobox(self,values=["1", "2", "3"], style='Red.TCombobox', justify='center')
        self.drop_off_loc.place(x=100, y=200, width=285, height=30)
        self.drop_off_loc.set("Drop-Off Location")

        date=Label(self,text="Drop-off Time:", fg="black", bg="white", font=("Microsft YaHei UI Light",12))
        date.place(x=550, y=120)
       
        self.battery = Entry(self,width=25, fg="black", border=2, bg="white", font=("Microsft YaHei UI Light",11))
        self.battery.place(x=550, y=150)
        self.battery.insert(0,"battery percentage")
        self.battery.bind('<FocusIn>', lambda x: self.on_enter(self.battery))
        self.battery.bind('<FocusOut>', lambda x: self.on_leave("battery percentage", self.battery))
      

        Button(self,width=39,pady=7,text="CANCEL",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toUserHome).place(x=140, y=400)
        Button(self,width=39,pady=7,text="CONFIRM",bg="#CD3333", fg="white", border=0, command=self.sumbit).place(x=520, y=400)
    def on_enter(self,element):
        element.delete(0, 'end')
    
    def on_leave(self, text, element):
        name = element.get()
        if name=='':
            element.insert(0,text)

    def sumbit(self):
        battery_percentage = self.battery.get()
        loc = self.drop_off_loc.get()
        self.order.pickup_location = loc
        self.order.end_time = datetime.datetime.now()
        self.order.charge = -1  # switch into pending state
        self.CONTROLLER.MODEL.DATA['orders'].update(self.order)
        print("return car success")
        # update vehicle status
        self.CONTROLLER.MODEL.DATA['vehicle'].return_vehicle(current_location=loc, battery_percentage=battery_percentage, vehicle_id=self.order.vehicle_id)
        self.CONTROLLER.toPayment()


    
if __name__=='__main__':
    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False,False)

    container = tk.Frame(root)
    container.pack(side = "top", fill = "both", expand = True)    
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    controller = None

    pg = ReturnCar(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()
