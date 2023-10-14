import tkinter as tk
import tkinter.font as tkFont

class ReportCar(tk.Frame):
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_485=tk.Button(root)
        GButton_485["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_485["font"] = ft
        GButton_485["fg"] = "#000000"
        GButton_485["justify"] = "center"
        GButton_485["text"] = "CANCEL"
        GButton_485.place(x=170,y=350,width=77,height=35)
        GButton_485["command"] = self.GButton_485_command

        GButton_901=tk.Button(root)
        GButton_901["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_901["font"] = ft
        GButton_901["fg"] = "#000000"
        GButton_901["justify"] = "center"
        GButton_901["text"] = "CONFIRM"
        GButton_901.place(x=310,y=350,width=77,height=35)
        GButton_901["command"] = self.GButton_901_command

        GLabel_77=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_77["font"] = ft
        GLabel_77["fg"] = "#333333"
        GLabel_77["justify"] = "center"
        GLabel_77["text"] = "Time for drop-off :"
        GLabel_77.place(x=290,y=140,width=131,height=37)

        GListBox_636=tk.Listbox(root)
        GListBox_636["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_636["font"] = ft
        GListBox_636["fg"] = "#333333"
        GListBox_636["justify"] = "center"
        GListBox_636.place(x=300,y=180,width=174,height=30)

    def GButton_485_command(self):
        print("command")


    def GButton_901_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    reportCar = ReportCar(root)
    root.mainloop()
