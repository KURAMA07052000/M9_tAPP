from tkinter import PhotoImage
import os

class Model:
    def init_assets(self):
        self.ASSETS = {
            'logo': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'carrent1.png'))
            }