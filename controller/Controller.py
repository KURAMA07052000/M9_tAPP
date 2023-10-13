from view.SignUp import SignUp
from view.SignIn import SignIn
from view.UserHome import UserHome
from view.Wallet import Wallet
from view.RentCar import RentCar
from view.ReturnCar import ReturnCar
from view.Payment import Payment
from view.OrderHistory import OrderHistory

class Controller():
    def __init__(self):
        self.ALL_PAGES = [SignIn ,SignUp, UserHome, Wallet, RentCar, ReturnCar, Payment, OrderHistory]
        self.VIEW = None
        self.UserID = None
        self.WalletID = None
        self.UserType = None

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

    def toPayment(self):
        self.VIEW.show_frame(Payment)

    def toOrderHistory(self):
        self.VIEW.show_frame(OrderHistory)
    
    def login(self, email:str, password:str):
        self.UserID, self.WalletID, self.UserType = self.MODEL.User.login(email,password)
        if self.UserID!=None and self.WalletID!=None and self.UserType!=None:
            self.toUserHome()
        else:
            print('Wrong ui and pass')

    def signup(self, name:str, email:str, phone_num:str, password:str, user_kind:str):
        self.MODEL.User.create_new(name, email, phone_num, password, user_kind)
        self.toSignIn()

    def logout(self):
        self.UserID, self.WalletID, self.UserType = [None]*3
        self.toSignIn()