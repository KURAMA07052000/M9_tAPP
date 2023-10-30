import datetime
import sys
import os

from model.Order import Order

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class DamageReport:
    def __init__(self):
        self.con = conn()
        self.cur = curr()
        self.Type = '1'
        self.Location = None
        self.Vehicle = None
        self.VehicleID = None

    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a vehicle table
        '''
        con = conn()
        cur = curr()

        if saftey == 'off':
            cur.execute('''DROP TABLE IF EXISTS Vehicle''')

        cur.execute('''CREATE TABLE IF NOT EXISTS damage_report(
                damage_id text PRIMARY KEY,
                vehicle_id text,
                order_id text, 
                damage_report text, 
                occured datetime,
                fixed boolean
                );''')

        con.commit()


    def create_new(self, vehicle_id: str, order_id: str, damage_report: str, occured: datetime, fixed: bool):
        damage_id = uuid.uuid4()
        damage_id = str(damage_id)
        self.cur.execute("""INSERT INTO damage_report (damage_id, vehicle_id, order_id, damage_report, occured, fixed) VALUES(
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
            );""", [damage_id, vehicle_id, order_id, damage_report, occured, fixed])
        self.con.commit()

    def create_new_test(self):
        '''
        create vehicle_id
        '''
        vehicle_id = str(uuid.uuid4())

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        self.cur.execute("""insert into damage_report (vehicle_id, order_id, damage_report, occured, fixed) values (
            ?,
            ?,
            ?,
            ?,
            ?
            );""", [vehicle_id, 'order_id', 'damage_report', datetime.datetime.now(), False])

        self.con.commit()


    def report_from_order(self, order : Order, damage_report : str):
        # generate damage_id
        damage_id = str(uuid.uuid4())
        self.cur.execute("""insert into damage_report (damage_id, vehicle_id, order_id, damage_report, occured, fixed) values (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
            );""", [damage_id, order.vehicle_id, order.order_id, damage_report, order.end_time, False])
        self.con.commit()

    def get_damage_case(self):
        self.cur.execute("""
            select damage_id, vehicle_id, damage_report, occured from damage_report where fixed == false
        """)
        self.con.commit()
        case = self.cur.fetchall()
        if case == []:
            return None
        return case[0]

    def fixd_vehicle(self, damage_id):
        # select current damage case
        self.cur.execute("""
            select * from damage_report where damage_id = ?
        """, [damage_id])
        case = self.cur.fetchall()
        print(case)
        if(case == None):
            print("fixd_vehicle: No such damage case")
            return None
        if(case[0][5]==True):
            print("fixd_vehicle: Vehicle already fixed")
            return None
        self.cur.execute("""
            update damage_report set fixed = true where damage_id = ?
        """, [damage_id])
        self.cur.execute("""
            update vehicle set is_damaged = false where vehicle_id = ?
        """, [case[0][1]])
        self.con.commit()



if __name__ == '__main__':
    u = DamageReport()
    u.CREATE_TABLE()