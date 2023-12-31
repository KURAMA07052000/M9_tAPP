import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

class RentCar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        self.CONTROLLER = controller

        #Dict of all vehicle id -> vehicle plates
        self.vehicle_map = self.CONTROLLER.MODEL.DATA['vehicle'].get_vehicle_map()
        self.vehicle_map_inv = { y:x for x,y in self.vehicle_map.items()}

        style = ttk.Style()
        style.configure('Red.TCombobox', fieldbackground='red', foreground='black')
        style.map('Red.TCombobox', background=[('readonly', 'red')])

        heading=Label(self, text="Rent Your Vehicle", fg="#F08080", bg="white", font=("Microsft YaHei UI Light",19,"bold"))
        heading.place(x=362, y=16)

        type=Label(self, text="Vehicle Type:", fg="black", bg="white", font=("Microsft YaHei UI Light",12))
        type.place(x=100, y=100)

        self.selected = tk.StringVar()
        # DO NOT CHANGE THE RADIO BUTTON TEXT, VALUE OR COMMAND: IT WILL BREAK THE ENTIRE SYSTEM
        self.radio_button1 = tk.Radiobutton(self, text="Type 1", variable=self.selected, value="1", bg="white", highlightthickness=0, font=("Microsft YaHei UI Light",12), command=lambda: self.choose_type('1'))
        self.radio_button2 = tk.Radiobutton(self, text="Type 2", variable=self.selected, value="2", bg="white", highlightthickness=0, font=("Microsft YaHei UI Light",12), command=lambda: self.choose_type('2'))
        self.selected.set(self.CONTROLLER.MODEL.DATA['vehicle'].Type)
        self.radio_button1.place(x=100, y=140)
        self.radio_button2.place(x=100, y=180)

        # date=Label(self,text="Pick-up Time:", fg="black", bg="white", font=("Microsft YaHei UI Light",12))
        # date.place(x=100, y=260)
       
        # self.pickupd = Entry(self, width=25, fg="black", border=0, bg="white", font=("Microsft YaHei UI Light",11))
        # self.pickupd.place(x=150, y=300)
        # self.pickupd.insert(0,"             DD/MM/YYYY")
        # self.pickupd.bind('<FocusIn>', lambda x: self.on_enter(self.pickupd))
        # self.pickupd.bind('<FocusOut>', lambda x: self.on_leave("             DD/MM/YYYY", self.pickupd))
        # Frame(self, width=195, height=2, bg="black").place(x=150,y=330)

        
        self.pick_up_loc = ttk.Combobox(self,values=self.CONTROLLER.MODEL.DATA['vehicle'].get_location_by_type(), style='Red.TCombobox', justify='center')
        self.pick_up_loc['state'] = 'readonly'
        self.pick_up_loc.place(x=510, y=100, width=285, height=30)
        self.pick_up_loc.set("-- Pick-Up Location --" if self.CONTROLLER.MODEL.DATA['vehicle'].Location==None else self.CONTROLLER.MODEL.DATA['vehicle'].Location)

        def choose_location(event):
            location = self.pick_up_loc.get()
            self.CONTROLLER.MODEL.DATA['vehicle'].Location = location
            self.CONTROLLER.hardRefreshRentCar()

        self.pick_up_loc.bind("<<ComboboxSelected>>", choose_location)

        #Get vehicle list
        vehicle_id_by_loc = self.CONTROLLER.MODEL.DATA['vehicle'].get_available_vehicle_by_location()
        vehicle_list = [self.vehicle_map[i] for i in vehicle_id_by_loc]

        self.vehicle = ttk.Combobox(self,values=vehicle_list, style='Red.TCombobox', justify='center')
        self.vehicle['state'] = 'readonly'
        self.vehicle.place(x=510, y=200, width=285, height=30)
        self.vehicle.set("-- Chose your vehicle --" if self.CONTROLLER.MODEL.DATA['vehicle'].Vehicle==None else self.CONTROLLER.MODEL.DATA['vehicle'].Vehicle)

        def choose_vehicle(event):
            vehicle = self.vehicle.get()
            self.CONTROLLER.MODEL.DATA['vehicle'].Vehicle = vehicle
            self.CONTROLLER.MODEL.DATA['vehicle'].vehicle_id = self.vehicle_map_inv[vehicle]
            self.CONTROLLER.hardRefreshRentCar()
            
        self.vehicle.bind("<<ComboboxSelected>>", choose_vehicle)

        Button(self,width=39,pady=7,text="CANCEL",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toUserHome).place(x=140, y=400)
        Button(self, width=39,pady=7,text="CONFIRM",bg="#CD3333", fg="white", border=0, command=self.on_submit).place(x=520, y=400)

    def choose_type(self, type):
        self.CONTROLLER.MODEL.DATA['vehicle'].Type = type
        self.CONTROLLER.hardRefreshRentCar()

    def choose_location(self, location):
        self.CONTROLLER.MODEL.DATA['vehicle'].Location = location
        self.CONTROLLER.hardRefreshRentCar()
        
    def on_enter(self,element):
        element.delete(0, 'end')
    
    def on_leave(self, text, element):
        name = element.get()
        if name=='':
            element.insert(0,text)


    def on_submit(self):
        import datetime
        vehicleID = self.CONTROLLER.MODEL.DATA['vehicle'].vehicle_id 
        userID = self.CONTROLLER.MODEL.DATA['user'].UserID
        pickuploc = self.CONTROLLER.MODEL.DATA['vehicle'].Location
        Vehicle = self.CONTROLLER.MODEL.DATA['vehicle'].Vehicle
        if vehicleID!=None and userID!=None and pickuploc!=None and Vehicle!=None:
            self.CONTROLLER.MODEL.DATA['orders'].create_new_order(vehicleID, userID, datetime.datetime.now(), None, pickuploc, None) 
            self.CONTROLLER.MODEL.DATA['vehicle'].use_vehicle()
            self.CONTROLLER.MODEL.DATA['vehicle'].vehicle_id = None
            self.CONTROLLER.MODEL.DATA['vehicle'].Vehicle = None
            self.CONTROLLER.MODEL.DATA['vehicle'].Location = None
            self.CONTROLLER.hardRefreshRentCar()
            self.CONTROLLER.toUserHome()
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")
        
   

    
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

    pg = RentCar(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()
