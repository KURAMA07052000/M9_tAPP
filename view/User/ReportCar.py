import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

class ReportCar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.CONTROLLER = controller

        GButton_485 = tk.Button(self)
        GButton_485["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=11)
        GButton_485["font"] = ft
        GButton_485["fg"] = "#000000"
        GButton_485["justify"] = "center"
        GButton_485["text"] = "CANCEL"
        GButton_485.place(x=290, y=370, width=131, height=36)
        GButton_485["command"] = self.GButton_485_command

        GButton_901 = tk.Button(self)
        GButton_901["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=11)
        GButton_901["font"] = ft
        GButton_901["fg"] = "#000000"
        GButton_901["justify"] = "center"
        GButton_901["text"] = "CONFIRM"
        GButton_901.place(x=500, y=370, width=132, height=36)
        GButton_901["command"] = self.GButton_901_command

        GLineEdit_821 = tk.Entry(self)
        GLineEdit_821["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_821["font"] = ft
        GLineEdit_821["fg"] = "#333333"
        GLineEdit_821["justify"] = "center"
        GLineEdit_821["text"] = "Type damage report here....."
        GLineEdit_821.place(x=510, y=80, width=369, height=234)
        GLineEdit_821["show"] = "Type damage report here....."


        self.drop_off_loc = ttk.Combobox(self, values=["Vehicle 1", "Vehicle 2", "Vehicle 3"], style='Red.TCombobox', justify='center')
        self.drop_off_loc.place(x=120, y=80, width=260, height=30)
        self.drop_off_loc.set("Chose from your ordered vehicles")

    def GButton_485_command(self):
        print("command")


    def GButton_901_command(self):
        print("command")



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('925x500+300+200')
    root.configure(bg='white')
    root.resizable(False, False)
    root.title('ReportCar')

    container = tk.Frame(root)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    controller = None

    pg = ReportCar(container, controller)
    pg.grid(row=0, column=0, sticky="nsew")

    root.mainloop()



