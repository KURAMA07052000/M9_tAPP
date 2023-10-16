from view.User.SignUp import SignUp
from view.User.SignIn import SignIn
from view.User.UserHome import UserHome
from view.User.Wallet import Wallet
from view.User.RentCar import RentCar
from view.User.ReturnCar import ReturnCar
from view.User.Payment import Payment
from view.User.OrderHistory import OrderHistory
from view.Operator.OperatorHome import OperatorHome
from view.Manager.ManagerHome import ManagerHome

class Controller():
    def __init__(self):
        self.ALL_PAGES = [SignUp, UserHome, Wallet, RentCar, ReturnCar, Payment, OrderHistory, SignIn, OperatorHome, ManagerHome]
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
        self.MODEL.DATA['wallet'].refresh()
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
            self.MODEL.set_ids(self.UserID, self.WalletID, self.UserType)
            self.toUserHome()
        else:
            print('Wrong ui and pass')

    def signup(self, name:str, email:str, phone_num:str, password:str, user_kind:str):
        self.MODEL.User.create_new(name, email, phone_num, password, user_kind)
        self.toSignIn()

    def logout(self):
        self.UserID, self.WalletID, self.UserType = [None]*3
        self.toSignIn()