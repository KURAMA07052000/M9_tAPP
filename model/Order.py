import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class Order:

    def set_value(self, order_id: int, vehicle_id: int, user_id: int, end_time: datetime, start_time: datetime, pickup_location: str, dropoff_location: str, charge: float, damage_id: int):
        self.order_id = order_id
        self.vehicle_id = vehicle_id
        self.user_id = user_id
        if(start_time != None):
            self.start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
        else:
            self.start_time = None
        if(end_time != None):
            self.end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S.%f')
        else:
            self.end_time = None
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.charge = charge
        self.damage_id = damage_id

    '''
        method: set_value_from_database
        input: order : tuple
        return: boolean
    '''
    def set_value_from_database(self, order : tuple):
        if order == None:
            return False
        self.order_id = order[0]
        self.vehicle_id = order[1]
        self.user_id = order[2]
        # self.end_time = datetime(order[3])
        if(order[4] != None):
            self.start_time = datetime.datetime.strptime(order[4], '%Y-%m-%d %H:%M:%S.%f')
            self.start_time_string = str(self.start_time.strftime("%d/%m/%Y, %H:%M:%S"))
        else:
            self.start_time = None
            self.start_time_string = None
        if(order[3] != None):
            self.end_time = datetime.datetime.strptime(order[3], '%Y-%m-%d %H:%M:%S.%f')
            self.end_time_string = str(self.end_time.strftime("%d/%m/%Y, %H:%M:%S"))
        else:
            self.end_time = None
            self.end_time_string = None
        self.pickup_location = order[5]
        self.dropoff_location = order[6]
        self.charge = order[7]
        self.damage_id = order[8]
        return True

    '''
        method: get_charge
        return: charge : float
    '''
    def get_charge(self):
        if self.charge < 0.0:
            return abs(self.charge)
        if self.charge == 0.0:
            # TODO: calculate Charge
            if self.end_time != None:
                self.charge = -1.0
            return self.charge
        if self.charge > 0.0:
            return self.charge

    '''
        method: create_order
        input: vehicle_id : str, user_id : str, start_time : datetime, pickup_location : str, dropoff_location : str, end_time : datetime = None  
    '''
    def create_order(self, vehicle_id : str, user_id : str, start_time : datetime, pickup_location : str, dropoff_location : str, end_time : datetime = None):
        self.order_id = str(uuid.uuid4())
        self.vehicle_id = vehicle_id
        self.user_id = user_id
        self.start_time = start_time
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.end_time = end_time
        self.end_time_string = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S.%f')
        self.end_time_string = str(self.end_time_string.strftime("%d/%m/%Y, %H:%M:%S"))
        self.charge = 0.0
        self.damage_id = None

    def __init__(self):
        pass

    def __init__(self, order : tuple):
        self.set_value_from_database(order)
        pass

    def to_string_orderId_and_listId(self):
        return "Order ID: " + str(self.order_id[-5:]) + ' | Vehicle ID: ' + str(self.vehicle_id[-5:]) + ' Drop off: ' +  str(self.dropoff_location)

    def get_order_id(self):
        return self.order_id
    '''
        price calculate part
    '''
    def calculate_charge(self):
        hour = (self.end_time - self.start_time).total_seconds()/3600
        self.charge = hour * 5.0

if __name__ == '__main__':
    u = Order()
    # u.CREATE_TABLE()
    # u.create_new()

