import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class Vehicle:
    def __init__(self):
        pass

    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a vehicle table
        '''
        con = conn()
        cur = curr()

        if saftey == 'off':
            cur.execute('''DROP TABLE IF EXISTS Vehicle''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Vehicle(
                vehicle_id text PRIMARY KEY, 
                vehicle_type text,
                current_location text,
                is_damaged boolean,
                battery_percentage integer
                );''')
        con.commit()

    def create_new(self):
        '''
        create vehicle_id
        '''
        con, cur = [conn(), curr()]

        vehicle_id = uuid.uuid4()

        vehicle_id = str(vehicle_id)

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        cur.execute("""INSERT INTO Vehicle (vehicle_id, vehicle_type, current_location, is_damaged, battery_percentage) VALUES(
            ?,
            'SUV',
            'University of Glasgow',
            false,
            100
            );""", [vehicle_id])

        con.commit()


if __name__ == '__main__':
    u = Vehicle()
    u.CREATE_TABLE()
    u.create_new()
