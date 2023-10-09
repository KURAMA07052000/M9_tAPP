from view.SignUp import SignUp
from view.SignIn import SignIn
from view.UserHome import UserHome
from view.Wallet import Wallet
from view.RentCar import RentCar

from tkinter import PhotoImage
import os

class Controller():
    def __init__(self):
        self.ALL_PAGES = [SignIn ,SignUp, UserHome, Wallet, RentCar]
        self.VIEW = None

    def init_assets(self):
        self.ASSETS = {
            'logo': PhotoImage(file=os.path.join(os.path.join(os.getcwd(),'assets'),'carrent1.png'))
            }

    def setView(self,controller):
        self.VIEW = controller
        self.init_assets()

    def toSignUp(self):
        self.VIEW.show_frame(SignUp)

    def toSignIn(self):
        self.VIEW.show_frame(SignIn)

    def toUserHome(self):
        self.VIEW.show_frame(UserHome)

    def toWallet(self):
        self.VIEW.show_frame(Wallet)

    def toRentCar(self):
        self.VIEW.show_frame(RentCar)