from tkinter import PhotoImage
import os

class Model:
    def __init__(self):
        pass
    
    def init_assets(self):
        self.ASSETS = {
            'map': PhotoImage(file=os.path.join(os.path.join(os.getcwd(), 'assets'), 'map.png')),
            'logo': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'carrent1.png')),
            'logoutbutton': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'logout.png')),
            'wallet': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'wallet.png')),
            }