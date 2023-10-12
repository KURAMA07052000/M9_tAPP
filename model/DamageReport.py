import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class DamageReport:
    def __init__(self):
        pass

    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a vehicle table
        '''
        con = conn()
        cur = curr()

        if saftey == 'off':
            cur.execute('''DROP TABLE IF EXISTS DamageReport''')

        cur.execute('''CREATE TABLE IF NOT EXISTS DamageReport (
                damage_id text PRIMARY KEY,
                vehicle_id text not null,
                order_id text not null,
                damage_report text not null,
                occured_time datetime not null, 
                fixed_time datetime
                );''')
        con.commit()

    def create_new(self):
        '''
        create vehicle_id
        '''
        con, cur = [conn(), curr()]

        order_id = uuid.uuid4()
        vehicle_id = str(uuid.uuid4())
        damage_id = str(uuid.uuid4())

        order_id = str(order_id)
        st = datetime.datetime.now()

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        cur.execute("""INSERT INTO DamageReport (damage_id, vehicle_id, order_id, damage_report, occured_time, fixed_time)
         values (
         ?,
         ?,
         ?, 
         'broken',
         ?,
         null   
        );""", [damage_id, vehicle_id, order_id, st])

        con.commit()


if __name__ == '__main__':
    u = DamageReport()
    u.CREATE_TABLE()
    u.create_new()
