import tkinter as tk
from tkinter import *
#from ttkbootstrap import Style
#from ttkbootstrap import ttk as bttk
from tkinter import ttk
from controller.Controller import *
import os
import sys

sys.path.append(os.getcwd())


class Payment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.CONTROLLER = controller
        self.get_data()

        frame1 = tk.Frame(self, width=925, height=500, bg="white")
        frame1.place(x=0, y=0)

        pending_frame = tk.Frame(frame1, width=925, height=500, bg="white")
        pending_frame.place(x=0, y=0)

        starting_price_label = tk.Label(frame1, text="Starting price", font=("Inter", 18), fg="black", bg="white")
        starting_price_label.place(x=439, y=117)

        # image = tk.PhotoImage(image)
        image_label = tk.Label(frame1, image = self.CONTROLLER.ASSETS['map'])
        image_label.place(x=0, y=0)

        trip_success_label = tk.Label(frame1, text="The trip has ended successfully! ", font=("Inter", 18, "bold"),
                                      fg="black", bg="white")
        trip_success_label.place(x=411, y=34)

        price_label_1 = tk.Label(frame1, text="£5.00", font=("Inter", 18), fg="black", bg="white")
        price_label_1.place(x=714, y=117)

        time_fee_label = tk.Label(frame1, text="Time fee", font=("Inter", 18), fg="black", bg="white")
        time_fee_label.place(x=439, y=188)
        # Dispatch fee
        price_label_2 = tk.Label(frame1, text=self.dispatch_fee_str, font=("Inter", 18), fg="black", bg="white")
        price_label_2.place(x=714, y=259)

        dispatch_service_fee_label = tk.Label(frame1, text="Dispatch service fee", font=("Inter", 18), fg="black",
                                              bg="white")
        dispatch_service_fee_label.place(x=439, y=259)

        total_label = tk.Label(frame1, text="Total", font=("Inter", 24, "bold"), fg="black", bg="white")
        total_label.place(x=439, y=334)
        # Total fee
        price_label_3 = tk.Label(frame1, text=self.total_fee_str, font=("Inter", 24, "bold"), fg="black", bg="white")
        price_label_3.place(x=714, y=334)
        # Time fee
        price_label_4 = tk.Label(frame1, text=self.duration_fee_str, font=("Inter", 18), fg="black", bg="white")
        price_label_4.place(x=714, y=188)

        start_price_info_label = tk.Label(frame1, text="Starting price includes 4 seconds of time", font=("Inter", 12),
                                          fg="#3D3D3D", bg="white")
        start_price_info_label.place(x=439, y=147)

        duration_info_label = tk.Label(frame1, text="Total duration is " + self.duration_hour_str + " seconds ", font=("Inter", 12), fg="#3D3D3D",
                                       bg="white")
        duration_info_label.place(x=439, y=218)

        rectangle1 = tk.Button(frame1, width=30, text="PAY", height=3, fg="white", bg="#CD3333", relief="solid", bd=0, command=self.pay_fn)
        rectangle1.place(x=480, y=399)

    def pay_fn(self):
        # check wallet amount
        balance = self.CONTROLLER.MODEL.DATA['wallet'].get_balance()
        if(balance < self.total_fee):
            self.CONTROLLER.toWallet()
        else:
            # update wallet amount
            self.CONTROLLER.MODEL.DATA['wallet'].charge(self.total_fee)
            # update order
            self.order.charge = self.total_fee
            self.order.payment_done = True
            self.CONTROLLER.MODEL.DATA['orders'].update(self.order)
            self.CONTROLLER.toUserHome()

    def get_data(self):
        self.order =  self.CONTROLLER.MODEL.DATA['orders'].get_pending_order(self.CONTROLLER.MODEL.DATA['user'].UserID)
        if(self.order == None):
            self.duration_hour_str = "£0.00"
            self.duration_fee_str = "£0.00"
            self.dispatch_fee_str = "£0.00"
            self.total_fee_str = "£0.00"
            self.CONTROLLER.toUserHome()
        else:

            # algorithm of calculating price

            '''
                THIS IS CHANGE FOR BETTER PRESENTATION. SO HOUR WILL BECOME SECONDS
                starting_price : 5 and have 4s of time
                then every hour is 1 pounds
                if pick up location is different from drop off location,
                then add 10 pounds of Dispatch service fee
            '''
            self.duration_hour = (self.order.end_time - self.order.start_time).total_seconds()
            if(self.duration_hour <= 4.0):
                self.duration_fee = 0.0
            else:
                self.duration_fee = 1.0 * (self.duration_hour - 4.0)
            # %.2f: round(number, ndigits)
            if(self.order.pickup_location != self.order.dropoff_location):
                self.dispatch_fee = 10.0
            else:
                self.dispatch_fee = 0.0
            self.starting_price = 5.0
            self.total_fee = self.starting_price + self.duration_fee + self.dispatch_fee

            # string part
            self.duration_hour_str = str(round(self.duration_hour, 2))
            self.duration_fee_str = "£" + str(round(self.duration_fee, 2))
            self.dispatch_fee_str = "£" + str(round(self.dispatch_fee, 2))
            self.total_fee_str = "£" + str(round(self.total_fee, 2))




if __name__ == '__main__':
    root = tk.Tk()
    #style = Style(theme='yeti')
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False, False)

    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # model = Model()
    # controller = Controller()
    # controller.setModel(model)
    controller = None


    pg = Payment(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()