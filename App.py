from controller.Controller import *
from view.View import tkinterApp
from model.Model import Model

model = Model()
controller = Controller()
controller.setModel(model)
view = tkinterApp(controller)

view.mainloop()