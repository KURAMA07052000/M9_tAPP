from tkinter import PhotoImage
import os

from model.User import User
from model.Wallet import Wallet

class Model:
    def __init__(self):
        self.User = User()
        self.Wallet = Wallet()
        self.DATA = {
            'wallet': self.Wallet,
            
        }
        self.User.CREATE_TABLE()
        self.Wallet.CREATE_TABLE()
    
    def init_assets(self):
        self.ASSETS = {
            'map': PhotoImage(file=os.path.join(os.path.join(os.getcwd(), 'assets'), 'map.png')),
            'logo': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'carrent1.png')),
            'logoutbutton': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'logout.png')),
            'wallet': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'wallet.png')),
            }
        
    def set_ids(self, UserID:str, WalletID:str, UserType:str):
        self.Wallet.set_id(WalletID)
        self.User.set_id(UserID, UserType)