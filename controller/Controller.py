from view.Manager.ChargeStatistics import ChargeStatistics
from view.Manager.LocationStatistics import LocationStatistics
from view.Manager.VehicleUsage import VehicleUsage
from view.User.SignUp import SignUp
from view.User.SignIn import SignIn
from view.User.UserHome import UserHome
from view.User.Wallet import Wallet
from view.User.RentCar import RentCar
from view.User.ReturnCar import ReturnCar
from view.User.Payment import Payment
from view.User.OrderHistory import OrderHistory
from view.User.ReportCar import ReportCar
from view.Manager.ManagerHome import ManagerHome
from view.Operator.OperatorHome import OperatorHome
from view.Operator.ChangeLocation import ChangeLocation
from view.Operator.ConditionReport import ConditionReport

class Controller():
    def __init__(self):
        self.ALL_PAGES = [SignUp, UserHome, Wallet, RentCar, ReturnCar, Payment, OrderHistory, SignIn, ReportCar, ChangeLocation, OperatorHome, ManagerHome, ConditionReport]
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

    def toChangeLocation(self):
        self.VIEW.init_and_show_frame(ChangeLocation)

    def toUserHome(self):
        # check if user has order not paid
        self.order = self.MODEL.DATA['orders'].get_pending_order(self.MODEL.DATA['user'].UserID)
        if self.order!=None:
            self.VIEW.init_and_show_frame(Payment)
        else:
            self.VIEW.show_frame(UserHome)

    def toReportCar(self):
        self.VIEW.init_and_show_frame(ReportCar)

    def toWallet(self):
        self.MODEL.DATA['wallet'].refresh()
        self.VIEW.show_frame(Wallet)

    def toRentCar(self):
        # check if user has already rented a car
        self.order = self.MODEL.DATA['orders'].get_active_order(self.MODEL.DATA['user'].UserID)
        if self.order!=None:
            self.VIEW.init_and_show_frame(ReturnCar)
        else:
            self.VIEW.show_frame(RentCar)

    def hardRefreshRentCar(self):
        self.VIEW.init_and_show_frame(RentCar)

    def toReturnCar(self):
        self.VIEW.init_and_show_frame(ReturnCar)

    def toPayment(self):
        self.VIEW.init_and_show_frame(Payment)

    def toOrderHistory(self):
        self.VIEW.init_and_show_frame(OrderHistory)


    def toManagerHome(self):
        self.VIEW.show_frame(ManagerHome)

    def toOperatorHome(self):
        self.VIEW.init_and_show_frame(OperatorHome)

    def toConditionReport(self):
        self.VIEW.init_and_show_frame(ConditionReport)

    def toVehicleUsage(self):
        self.VIEW.init_and_show_frame(VehicleUsage)

    def toLocationStatistics(self):
        self.VIEW.init_and_show_frame(LocationStatistics)

    def toChargeStatistics(self):
        self.VIEW.init_and_show_frame(ChargeStatistics)
    
    def login(self, email:str, password:str):
        self.UserID, self.WalletID, self.UserType = self.MODEL.User.login(email,password)
        if self.UserID!=None and self.WalletID!=None:
            self.MODEL.set_ids(self.UserID, self.WalletID, self.UserType)
            if self.UserType=='customer':
                self.toUserHome()
                return True
            elif self.UserType=='admin':
                self.toOperatorHome()
                return True
            elif self.UserType=='manager':
                self.toManagerHome()
                return True
            else:
                print('Wrong usertype')
                return False
            print('Wrong ui or pass')
        return False

    def signup(self, name:str, email:str, phone_num:str, password:str, user_kind:str):

        if(self.MODEL.User.create_new(name, email, phone_num, password, user_kind) == True):
            self.toSignIn()
            # sign up success
            return True
        return False


    def logout(self):
        self.UserID, self.WalletID, self.UserType = [None]*3
        self.toSignIn()