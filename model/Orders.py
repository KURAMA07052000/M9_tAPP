import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class Orders:
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

    def create_new(self):
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
        ?, 
        null, 
        ?, 
        'University of Glasgow',
        'Glasgow Queen street', 
        99.12,
        null
        );""", [order_id, vehicle_id, user_id, st])

        con.commit()


if __name__ == '__main__':
    u = Orders()
    u.CREATE_TABLE()
    u.create_new()
