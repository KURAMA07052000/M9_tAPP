import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class Vehicle:
    def __init__(self):
        self.con = conn()
        self.cur = curr()
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


    def create_new(self, vehicle_type: str, current_location: str, is_damaged: bool, battery_percentage: int):

        vehicle_id = uuid.uuid4()

        vehicle_id = str(vehicle_id)
        self.cur.execute("""INSERT INTO Vehicle (vehicle_id, vehicle_type, current_location, is_damaged, battery_percentage) VALUES(
            ?,
            ?,
            ?,
            ?,
            ?
            );""", [vehicle_id, vehicle_type, current_location, is_damaged, battery_percentage])



    def create_new_test(self):
        '''
        create vehicle_id
        '''
        vehicle_id = str(uuid.uuid4())

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        self.cur.execute("""INSERT INTO Vehicle (vehicle_id, vehicle_type, current_location, is_damaged, battery_percentage) VALUES(
            ?,
            'SUV',
            'University of Glasgow',
            false,
            100
            );""", [vehicle_id])

        self.con.commit()


if __name__ == '__main__':
    u = Vehicle()
    u.CREATE_TABLE()
    u.create_new()
