from controller.routes import *
from App import tkinterApp

controller = Controller()
view = tkinterApp(controller)

view.mainloop()