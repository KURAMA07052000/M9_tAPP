import tkinter as tk
from tkinter import ttk
from tkinter import *

class ReportCar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        self.CONTROLLER = controller
        Button(self,width=39,pady=7,text="CANCEL",bg="#CD3333", fg="white", border=0, command=self.CONTROLLER.toUserHome).place(x=140, y=400)
        Button(self, width=39,pady=7,text="CONFIRM",bg="#CD3333", fg="white", border=0, command=self.submit_fn).place(x=520, y=400)

       
        self.GText_821 = tk.Text(self, fg="#333333", bg="white", wrap="word")
        self.GText_821.insert("1.0", "Type damage report here.....")
        self.GText_821.place(x=510, y=80, width=369, height=234)


        # get the order history from the database
        self.orders = self.CONTROLLER.MODEL.DATA['orderHistory'].order_history_user_entity(self.CONTROLLER.MODEL.DATA['user'].UserID)


        # processing data
        self.display = []
        for order in self.orders:
            self.display.append(order.to_string_orderId_and_listId())

        self.drop_off_loc = ttk.Combobox(self, values=self.display, style='Red.TCombobox', justify='center')
        self.drop_off_loc.place(x=120, y=80, width=260, height=30)
        # self.drop_off_loc.set("Chose from your ordered vehicles")
        # put orders into the combobox
        print(self.display)
        self.drop_off_loc.set("Chose from your ordered vehicles" if self.display != [] else "No orders found")

    def submit_fn(self):
        # find order
        order = self.orders[self.display.index(self.drop_off_loc.get())]
        print(order)
        report = self.GText_821.get("1.0", "end")
        print(report)
        self.CONTROLLER.MODEL.DATA['damage_report'].report_from_order(order, report)
        self.GText_821.delete("1.0", "end")
        self.CONTROLLER.toUserHome()



    def on_enter(self,element):
        element.delete(0, 'end')
    
    def on_leave(self, text, element):
        name = element.get()
        if name=='':
            element.insert(0,text)

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

    pg = ReportCar(container, controller)
    pg.grid(row = 0, column = 0, sticky ="nsew")

    root.mainloop()



