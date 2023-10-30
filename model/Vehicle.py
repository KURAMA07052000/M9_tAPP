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

        cur.execute('''CREATE TABLE IF NOT EXISTS Vehicle(
                vehicle_id text PRIMARY KEY, 
                vehicle_plate_num text,
                vehicle_type text,
                current_location text,
                is_damaged boolean,
                is_in_use boolean,
                battery_percentage integer
                );''')

        con.commit()

        self.create_new('1', 'veh_T1_L1', 'loc1', False, 100, False)
        self.create_new('1', 'veh_T1_L2', 'loc2', False, 100, False)
        self.create_new('1', 'veh_T1_L3', 'loc3', False, 100, False)
        self.create_new('1', 'veh_T1_L4', 'loc4', False, 100, False)
        self.create_new('2', 'veh_T2_L1', 'loc1', False, 100, False)
        self.create_new('2', 'veh_T2_L2', 'loc2', False, 100, False)
        self.create_new('2', 'veh_T2_L3', 'loc3', False, 100, False)
        self.create_new('2', 'veh_T2_L4', 'loc4', False, 100, False)
        


    def create_new(self, vehicle_type: str, vehicle_plate_num:str, current_location: str, is_damaged: bool, battery_percentage: int, is_in_use: bool):

        vehicle_id = uuid.uuid4()

        vehicle_id = str(vehicle_id)
        self.cur.execute("""INSERT INTO Vehicle (vehicle_id, vehicle_plate_num, vehicle_type, current_location, is_damaged, battery_percentage, is_in_use) VALUES(
            ?,
            ?,
            ?,
            ?,
            ?,
            ?, 
            ?
            );""", [vehicle_id, vehicle_plate_num, vehicle_type, current_location, is_damaged, battery_percentage, is_in_use])
        
        self.con.commit()



    def create_new_test(self):
        '''
        create vehicle_id
        '''
        vehicle_id = str(uuid.uuid4())

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        self.cur.execute("""INSERT INTO Vehicle (vehicle_id, vehicle_type, current_location, is_damaged, battery_percentage, is_in_use) VALUES(
            ?,
            'SUV',
            'University of Glasgow',
            false,
            100, 
            false
            );""", [vehicle_id])

        self.con.commit()

    '''
        method: get_vehicle_type
        return: List of vehicle type
    '''
    def get_vehicle_type(self):
        self.cur.execute("""SELECT vehicle_type FROM Vehicle""")
        return self.cur.fetchall()

    '''
        method: get_available_vehicle_by_location
        return: List of available vehicle in certain location 
    '''
    def get_available_vehicle_by_location(self):
        if self.Location==None:
            self.cur.execute("""SELECT vehicle_plate_num || " - " ||  vehicle_id as VehicleUUID FROM Vehicle WHERE is_damaged = false AND is_in_use = false""")
            data = self.cur.fetchall().copy()
            data = [i[0] for i in data]
            return data
        self.cur.execute("""SELECT vehicle_plate_num || " - " ||  vehicle_id as VehicleUUID FROM Vehicle WHERE current_location = ? AND vehicle_type = ? AND is_damaged = false AND is_in_use = false""", [self.Location, self.Type])
        data = self.cur.fetchall().copy()
        data = [i[0] for i in data]
        return data

    '''
        method get_available_vehicle_type_by_location
        return: List of available vehicle type in certain location
    '''
    def get_available_vehicle_type_by_location(self):
        self.cur.execute("""SELECT vehicle_type FROM Vehicle WHERE current_location = ? AND is_damaged = false AND is_in_use = false""", [self.Location])
        return self.cur.fetchall()

    '''
        method: get_available_vehicle_by_type
        return: List of available vehicle in certain type
    '''
    def get_available_vehicle_by_type(self, vehicle_type: str):
        print(vehicle_type)
        self.cur.execute("""SELECT * FROM Vehicle WHERE vehicle_type = ? AND is_damaged = false AND is_in_use = false""", [vehicle_type])
        data = self.cur.fetchall().copy()
        for i in data:
            print(i)
        return data
    
    def get_location_by_type(self):
        self.cur.execute("""SELECT current_location FROM Vehicle WHERE vehicle_type = ? AND is_damaged = false""", [self.Type])
        data = self.cur.fetchall().copy()
        for i in data:
            print(i)
        return data

    def get_all_location(self):
        self.cur.execute("""SELECT DISTINCT current_location FROM Vehicle""")
        data = self.cur.fetchall().copy()
        for i in data:
            print(i)
        return data

    '''
        method: get_available_vehicle_by_type_and_location
        return: List of available vehicle in certain type and location
    '''
    def get_available_vehicle_by_type_and_location(self, vehicle_type: str, location: str):
        self.cur.execute("""SELECT vehicle_id FROM Vehicle WHERE vehicle_type = ? AND current_location = ? AND is_damaged = false AND is_in_use = false""", [vehicle_type, location])
        return self.cur.fetchall()

    '''
        TODO: 
        method: get_vehicle_by_id
        return: Vehicle
    '''

    '''
        method: use_vehicle
        input: 
            vehicle_id: str
        return: None
    '''
    def use_vehicle(self):
        self.cur.execute("""UPDATE Vehicle SET is_in_use = true WHERE vehicle_id = ?""", [self.VehicleID])
        self.con.commit()
    '''
        method: return_vehicle
        input:
            vehicle_id: str, current_location: str, battery_percentage: int
        return: None            
    '''
    def return_vehicle(self, vehicle_id: str, current_location: str, battery_percentage: int):
        self.cur.execute("""UPDATE Vehicle SET is_in_use = false, current_location = ?, battery_percentage = ? WHERE vehicle_id = ?""", [current_location, battery_percentage, vehicle_id])
        self.con.commit()
    '''
        method: set_damage
        input:
            vehicle_id: str, is_damaged: bool
        return: None
    '''
    def set_damage(self, vehicle_id: str, is_damaged: bool):
        self.cur.execute("""UPDATE Vehicle SET is_damaged = ? WHERE vehicle_id = ?""", [is_damaged, vehicle_id])
        self.con.commit()



    def vehicle_type(self):
        self.cur.execute("""SELECT vehicle_type FROM Vehicle;""")
        return self.cur.fetchall()

    def current_location(self):
        self.cur.execute("""SELECT current_location FROM Vehicle;""")
        return self.cur.fetchall()



if __name__ == '__main__':
    u = Vehicle()
    u.CREATE_TABLE()