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
        self.end_time = end_time
        self.start_time = start_time
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
        self.end_time = order[3]
        self.start_time = order[4]
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

    def to_string_orderId_and_listId(self):
        return str(self.order_id[-5:]) + ' ' + str(self.vehicle_id[-5:]) + ' ' +  self.end_time_string




if __name__ == '__main__':
    u = Order()
    # u.CREATE_TABLE()
    # u.create_new()

