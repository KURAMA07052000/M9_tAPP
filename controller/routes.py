from view.SignUp import SignUp
from view.SignIn import SignIn

class Controller():
    def __init__(self):
        self.ALL_PAGES = [SignIn ,SignUp]
        self.VIEW = None

    def setView(self,controller):
        self.VIEW = controller

    def toSignUp(self):
        self.VIEW.show_frame(SignUp)

    def toSignIn(self):
        self.VIEW.show_frame(SignIn)