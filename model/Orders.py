import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class Orders:

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


    def __init__(self):
        self.con = conn()
        self.cur = curr()
        pass

    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a vehicle table
        '''

        if saftey == 'off':
            self.cur.execute('''DROP TABLE IF EXISTS Orders''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Orders (
                order_id text PRIMARY KEY, 
                vehicle_id text not null,
                user_id text not null,
                end_time datetime,
                start_time datetime not null,
                pickup_location text not null,
                dropoff_location text,
                charge double(10,2),
                damage_id text
                );''')
        self.con.commit()


    def creat_new(self, order_id: int, vehicle_id: int, user_id: int, end_time: datetime, start_time: datetime, pickup_location: str, dropoff_location: str, charge: float, damage_id: int):
        '''
        Create a new order
        '''
        order_id = str(uuid.uuid4())

        self.cur.execute("""INSERT INTO Orders (order_id, vehicle_id, user_id, end_time, start_time,
        pickup_location, dropoff_location, charge, damage_id) values (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
        );""", [order_id, vehicle_id, user_id, end_time, start_time, pickup_location, dropoff_location, charge, damage_id])
        self.con.commit()


    def order_history_user(self, user_id: int):

        self.cur.execute("""SELECT * FROM Orders WHERE user_id = ?;""", [user_id])
        row = self.cur.fetchall()
        return row

    def create_new_test(self):
        '''
        create vehicle_id
        '''

        order_id = uuid.uuid4()
        vehicle_id = str(uuid.uuid4())
        user_id = str(uuid.uuid4())

        order_id = str(order_id)
        st = datetime.datetime.now()

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        self.cur.execute("""INSERT INTO Orders (order_id, vehicle_id, user_id, end_time, start_time, 
        pickup_location, dropoff_location, charge, damage_id) values (
        ?, 
        ?, 
        'd830eb0f-9b9f-4b0d-8d4f-01175ec9300e', 
        null, 
        ?, 
        'University of Glasgow',
        'Glasgow Queen street', 
        99.12,
        null
        );""", [order_id, vehicle_id, st])

        self.con.commit()

    '''
        method: create_new_order
        input: vehicle_id, user_id, start_time, end_time, pickup_location, dropoff_location
        Figure out if we need to enter start time
        return: order_id
    '''
    def create_new_order(self, vehicle_id: str, user_id: str, start_time: datetime, end_time: datetime, pickup_location: str, dropoff_location: str):
        order_id = str(uuid.uuid4())
        self.cur.execute("""INSERT INTO Orders (order_id, vehicle_id, user_id, end_time, start_time,
        pickup_location, dropoff_location, charge, damage_id) values (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        -1, 
        ?
        );""", [order_id, vehicle_id, user_id, end_time, start_time, pickup_location, dropoff_location, None])
        self.con.commit()
        # charge = -1 means the order is not completed
        # charge = -2 means the order is completed but not paid
        return order_id

    '''
        method: complete_order
        input: order_id, dropoff_location = None, end_time = None, damage_id = None
        return: order_id
    '''
    # TODO:
    # def complete_order(self, order_id: str, dropoff_location: str = None, end_time: datetime = None, damage_id: str = None):
        # get Order first


if __name__ == '__main__':
    u = Orders()
    # u.CREATE_TABLE()
    # u.create_new()

