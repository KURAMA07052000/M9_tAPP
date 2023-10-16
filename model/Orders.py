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
        pass

    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a vehicle table
        '''
        con = conn()
        cur = curr()

        if saftey == 'off':
            cur.execute('''DROP TABLE IF EXISTS Orders''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Orders (
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
        con.commit()


    def creat_new(self, order_id: int, vehicle_id: int, user_id: int, end_time: datetime, start_time: datetime, pickup_location: str, dropoff_location: str, charge: float, damage_id: int):
        '''
        Create a new order
        '''
        con, cur = [conn(), curr()]
        order_id = str(uuid.uuid4())

        cur.execute("""INSERT INTO Orders (order_id, vehicle_id, user_id, end_time, start_time,
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
        con.commit()


    def order_history_user(self, user_id: int):
        '''
        Get order history for a user
        '''
        con, cur = [conn(), curr()]

        cur.execute("""SELECT * FROM Orders WHERE user_id = ?;""", [user_id])
        row = cur.fetchall()
        return row

    def create_new_test(self):
        '''
        create vehicle_id
        '''
        con, cur = [conn(), curr()]

        order_id = uuid.uuid4()
        vehicle_id = str(uuid.uuid4())
        user_id = str(uuid.uuid4())

        order_id = str(order_id)
        st = datetime.datetime.now()

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        cur.execute("""INSERT INTO Orders (order_id, vehicle_id, user_id, end_time, start_time, 
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

        con.commit()


if __name__ == '__main__':
    u = Orders()
    u.CREATE_TABLE()
    u.create_new()
