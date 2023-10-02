from controller.Controller import *
from view.View import tkinterApp

controller = Controller()
view = tkinterApp(controller)

view.mainloop()