from view.SignUp import SignUp
from view.SignIn import SignIn
from view.UserHome import UserHome
from view.Wallet import Wallet
from view.RentCar import RentCar
from view.ReturnCar import ReturnCar

class Controller():
    def __init__(self):
        self.ALL_PAGES = [SignIn ,SignUp, UserHome, Wallet, RentCar, ReturnCar]
        self.VIEW = None

    def setView(self,controller):
        self.VIEW = controller
        self.MODEL.init_assets()
        self.ASSETS = self.MODEL.ASSETS

    def setModel(self, model):
        self.MODEL = model

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

    def toReturnCar(self):
        self.VIEW.show_frame(ReturnCar)