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

        frame1 = tk.Frame(self, width=925, height=500, bg="white")
        frame1.place(x=0, y=0)

        pending_frame = tk.Frame(frame1, width=925, height=500, bg="white")
        pending_frame.place(x=0, y=0)

        starting_price_label = tk.Label(frame1, text="Starting price", font=("Inter", 20), fg="black", bg="white")
        starting_price_label.place(x=439, y=117)

        # image = tk.PhotoImage(image)
        image_label = tk.Label(frame1, image = self.CONTROLLER.ASSETS['map'])
        image_label.place(x=0, y=0)

        trip_success_label = tk.Label(frame1, text="The trip has ended successfully", font=("Inter", 20, "bold"),
                                      fg="black", bg="white")
        trip_success_label.place(x=411, y=34)

        price_label_1 = tk.Label(frame1, text="£10.00", font=("Inter", 20), fg="black", bg="white")
        price_label_1.place(x=714, y=117)

        time_fee_label = tk.Label(frame1, text="Time fee", font=("Inter", 20), fg="black", bg="white")
        time_fee_label.place(x=439, y=188)

        price_label_2 = tk.Label(frame1, text="£10.00", font=("Inter", 20), fg="black", bg="white")
        price_label_2.place(x=714, y=259)

        dispatch_service_fee_label = tk.Label(frame1, text="Dispatch service fee", font=("Inter", 20), fg="black",
                                              bg="white")
        dispatch_service_fee_label.place(x=439, y=259)

        total_label = tk.Label(frame1, text="Total", font=("Inter", 26, "bold"), fg="black", bg="white")
        total_label.place(x=439, y=334)

        price_label_3 = tk.Label(frame1, text="£30.00", font=("Inter", 26, "bold"), fg="black", bg="white")
        price_label_3.place(x=714, y=334)

        price_label_4 = tk.Label(frame1, text="£10.00", font=("Inter", 20), fg="black", bg="white")
        price_label_4.place(x=714, y=188)

        start_price_info_label = tk.Label(frame1, text="Starting price includes 4 hours of time", font=("Inter", 14),
                                          fg="#3D3D3D", bg="white")
        start_price_info_label.place(x=439, y=142)

        duration_info_label = tk.Label(frame1, text="Total duration is 10 hours", font=("Inter", 14), fg="#3D3D3D",
                                       bg="white")
        duration_info_label.place(x=439, y=213)

        rectangle1 = tk.Button(frame1, width=30, text="PAY", height=3, fg="white", bg="#CD3333", relief="solid", bd=0, )
        rectangle1.place(x=480, y=399)



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