import sys
import os
import datetime

from model.Order import Order

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

    def set_id(self, order_id: str):
        self.order_id = order_id


    def __init__(self):
        self.con = conn()
        self.cur = curr()
        self.start_date = None
        self.end_date = None
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
                damage_id text,
                payment_done BOOLEAN DEFAULT False
                );''')
        self.con.commit()


    def creat_new(self, vehicle_id: str, user_id: str, end_time: datetime, start_time: datetime, pickup_location: str, dropoff_location: str, charge: float, damage_id: str):
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

    def create_from_database(self, order : Order):
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
        );""", [order.order_id, order.vehicle_id, order.user_id, order.end_time, order.start_time, order.pickup_location, order.dropoff_location, order.charge, order.damage_id])
        self.con.commit()
        return True


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
        et = datetime.datetime.now() + datetime.timedelta(days=1)

        # w = Wallet()
        # w.create_new(wallet_id, user_id)

        self.cur.execute("""INSERT INTO Orders (order_id, vehicle_id, user_id, end_time, start_time, 
        pickup_location, dropoff_location, charge, damage_id) values (
        ?, 
        ?, 
        'd830eb0f-9b9f-4b0d-8d4f-01175ec9300e', 
        ?, 
        ?, 
        'University of Glasgow',
        'Glasgow Queen street', 
        99.12,
        null
        );""", [order_id, vehicle_id, et, st])

        self.con.commit()

    '''
        method: create_new_order
        input: vehicle_id, user_id, start_time, end_time, pickup_location, dropoff_location
        Figure out if we need to enter start time
        return: order_id
    '''
    def create_new_order(self, vehicle_id: str, user_id: str, start_time: datetime, end_time: datetime, pickup_location: str, dropoff_location: str):
        order_id = str(uuid.uuid4())
        print('pp')
        self.cur.execute("""INSERT INTO Orders (order_id, vehicle_id, user_id, end_time, start_time,
        pickup_location, dropoff_location, charge, damage_id) values (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        0, 
        ?
        );""", [order_id, vehicle_id, user_id, end_time, start_time, pickup_location, dropoff_location, None])
        self.con.commit()
        # charge = 0 means the order is not completed
        # charge = negative value means the order is completed but not paid

        self.cur.execute('SELECT * FROM Orders')
        print(self.cur.fetchall())

        return order_id

    '''
        method: get_order_by_id
        input: order_id
        return: boolean
    '''
    def get_order_by_id(self, order_id: str):
        self.cur.execute("""SELECT * FROM Orders WHERE order_id = ?;""", [order_id])
        return self.cur.fetchone()
        if self.cur.fetchone() == None:
            return False
        else:
            # store data in self
            self.order_id = self.cur.fetchone()[0]
            self.vehicle_id = self.cur.fetchone()[1]
            self.user_id = self.cur.fetchone()[2]
            self.end_time = self.cur.fetchone()[3]
            self.start_time = self.cur.fetchone()[4]
            self.pickup_location = self.cur.fetchone()[5]
            self.dropoff_location = self.cur.fetchone()[6]
            self.charge = self.cur.fetchone()[7]
            self.damage_id = self.cur.fetchone()[8]
            return True

    '''
        method: get_order_by_vehicle_id
        input: vehicle_id
        return: list of orders
    '''
    def get_order_by_vehicle_id(self, vehicle_id: str):
        self.cur.execute("""SELECT * FROM Orders WHERE vehicle_id = ?;""", [vehicle_id])
        return self.cur.fetchall()

    '''
        method: get_order_by_user_id
        input: user_id
        return: boolean
    '''
    def get_order_by_user_id(self, user_id: str):
        self.cur.execute("""SELECT * FROM Orders WHERE user_id = ?;""", [user_id])


    '''
        method: complete_order
        input: order_id, dropoff_location = None, end_time = None, damage_id = None
        return: boolean
    '''
    def complete_order(self, end_time: datetime, dropoff_location: str, vehicle_id: str ,user_id: str):
        from datetime import datetime
        self.cur.execute("""SELECT order_id, start_time, pickup_location FROM Orders WHERE vehicle_id = ? AND user_id=? AND payment_done=False""", [vehicle_id, user_id])
        data = list(self.cur.fetchone()).copy()
        order_id, start_date, pickup_location = data
        self.cur.execute("""SELECT vehicle_type FROM Vehicle WHERE vehicle_id = ?""", [vehicle_id])
        self.vehicle_type = self.cur.fetchone()[0]
        start_date = datetime.strptime(start_date,"%Y-%m-%d %H:%M:%S.%f")
        time_diff = end_time - start_date

        '''
            THIS IS CHANGE FOR BETTER PRESENTATION. SO HOUR WILL BECOME SECONDS
            starting_price : 5 and have 4s of time
            then every seconds is 1 pounds for type 1 vehicle
            and 1.5 pounds for type 2 vehicle
            if pick up location is different from drop off location,
            then add 10 pounds of Dispatch service fee
        '''
        self.duration_hour = (time_diff).total_seconds()
        # print(self.duration_hour)
        # find vehicle type
        self.vehicle_type = int(self.vehicle_type)
        if (self.duration_hour <= 4.0):
            self.duration_fee = 0.0
        elif (self.vehicle_type == 1):
            self.duration_fee = 1.0 * (self.duration_hour - 4.0)
        elif (self.vehicle_type == 2):
            self.duration_fee = 1.5 * (self.duration_hour - 4.0)
        # %.2f: round(number, ndigits)
        if (pickup_location != dropoff_location):
            self.dispatch_fee = 10.0
        else:
            self.dispatch_fee = 0.0
        self.starting_price = 5.0
        self.total_fee = self.starting_price + self.duration_fee + self.dispatch_fee
        self.total_fee = round(self.total_fee, 2)
        self.cur.execute('''UPDATE Orders SET end_time=?, charge=?, dropoff_location=? WHERE order_id=?''',[end_time, self.total_fee, dropoff_location, order_id])
        self.con.commit()
        return


    def get_active_order(self, user_id: str = None):
        if(user_id == None):
            print("get_active_order(): user_id not found! ")
            return None
        print(user_id)
        self.cur.execute("""SELECT * FROM Orders WHERE charge = 0 and user_id = ?;""", [user_id])
        tmp = self.cur.fetchone()
        if(tmp == None):
            return None
        return Order(tmp)

    def get_pending_order(self, user_id : str = None):
        if(user_id == None):
            print("get_pending_order(): user_id not found! ")
            return None
        self.cur.execute("""SELECT * FROM Orders WHERE payment_done = False and user_id = ? and charge != 0;""", [user_id])
        tmp = self.cur.fetchone()
        if(tmp == None):
            return None
        return Order(tmp)

    def update(self, order: Order):
        if(order == None):
            return False
        self.cur.execute("""UPDATE Orders SET vehicle_id = ?, user_id = ?, end_time = ?, 
        start_time = ?, pickup_location = ?, dropoff_location = ?, charge = ?, damage_id = ?, payment_done = ?
        WHERE order_id = ?;""", [order.vehicle_id, order.user_id, order.end_time,
                                 order.start_time, order.pickup_location, order.dropoff_location,
                                 order.charge, order.damage_id, order.payment_done, order.order_id])
        self.con.commit()
        return True
    
    def get_vehicle_ids_by_user_id(self, user_id):
        self.cur.execute('''SELECT vehicle_id FROM Orders WHERE user_id=? AND charge=0''',[user_id])
        data = list(self.cur.fetchall()).copy()
        return data

    '''
    '''
    def get_vehicle_usage_data(self):
        if(self.start_date == None or self.end_date == None):
            print("get_vehicle_usage_data(): date not found! ")
            return None
        self.cur.execute("""SELECT v.vehicle_plate_num, COUNT(o.order_id) 
                          FROM Orders o 
                          JOIN Vehicle v ON o.vehicle_id = v.vehicle_id
                          WHERE o.start_time BETWEEN ? AND ?
                          GROUP BY v.vehicle_plate_num""",
                          (self.start_date, self.end_date))

        data = {vehicle_plate: count for vehicle_plate, count in self.cur.fetchall()}

        return data

    '''
    
    '''
    def get_pickup_location_statistics_data(self):
        if(self.start_date == None or self.end_date == None):
            return None
        self.cur.execute("""SELECT pickup_location, COUNT(*) 
                          FROM Orders
                          WHERE start_time BETWEEN ? AND ? 
                          GROUP BY pickup_location""",
                          (self.start_date, self.end_date))
        data = {pickup_location: count for pickup_location, count in self.cur.fetchall()}
        return data

    def get_dropoff_location_statistics_data(self):
        if(self.start_date == None or self.end_date == None):
            return None
        self.cur.execute("""SELECT dropoff_location, COUNT(*) 
                          FROM Orders
                          WHERE start_time BETWEEN ? AND ? 
                          GROUP BY dropoff_location""",
                          (self.start_date, self.end_date))
        data = {dropoff_location: count for dropoff_location, count in self.cur.fetchall()}
        return data

    def get_all_orders_in_select_date(self):
        if(self.start_date == None or self.end_date == None):
            return None
        self.cur.execute("""SELECT * FROM Orders WHERE start_time BETWEEN ? AND ?""", (self.start_date, self.end_date))
        data = list(self.cur.fetchall()).copy()
        return data
    '''
        
    '''
    def get_charge_statistics_data(self):
        self.cur.execute("""
            SELECT V.vehicle_plate_num, SUM(O.charge) AS total_charge 
            FROM Orders O
            JOIN Vehicle V on O.vehicle_id = V.vehicle_id
            WHERE O.start_time BETWEEN ? AND ?
            GROUP BY V.vehicle_plate_num
            """, (self.start_date, self.end_date))
        data = {vehicle_plate: total_charge for vehicle_plate, total_charge in self.cur.fetchall()}
        return data


    def setDate(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    '''
        Generate orders
        user_id:f4e020a0-3874-4dc0-9c65-2f010fc94005
        vehicle_id: Random choice
        start_time: Random choice
        end_time: start_time + random choice
        pickup_location: random choice from ['loc1','loc2','loc3','loc4']
        dropoff_location: random choice from ['loc1','loc2','loc3','loc4']
        charge: calculated by calling self.complete_order(self, end_time: datetime, dropoff_location: str, vehicle_id: str ,user_id: str)
        self.order.payment_done = True
        then update order
        damage_id: None
    '''
    def generate_random_orders(self, n=50):
        import random
        user_id = 'f4e020a0-3874-4dc0-9c65-2f010fc94005'
        locations = ['loc1', 'loc2', 'loc3', 'loc4']
        orders_handler = Orders()

        for _ in range(n):
            # randomly select vehicle_id
            self.cur.execute('''SELECT vehicle_id FROM Vehicle''')
            vehicle_id = random.choice(self.cur.fetchall())[0]
            print(vehicle_id)
            # randomly generate start_time and end_time
            start_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 10))
            end_time = start_time + datetime.timedelta(hours=random.randint(1, 48))
            pickup_location = random.choice(locations)
            dropoff_location = random.choice(locations)

            # Creating new order
            order_id = orders_handler.create_new_order(vehicle_id, user_id, start_time, end_time, pickup_location,
                                                       dropoff_location)

            # Completing order
            orders_handler.complete_order(end_time, dropoff_location, vehicle_id, user_id)
            self.cur.execute('''SELECT * FROM Orders WHERE order_id = ?''', [order_id])
            if(self.cur.fetchone()[7] == 0):
                print("Error: order not completed")
                return False

            # setting payment_done to True
            self.cur.execute('''UPDATE Orders SET payment_done = True WHERE order_id = ?''', [order_id])
            # sleep 0.5s
            import time
            # time.sleep(0.5)

    # debug
    def cal_charge_by_order_id(self):
        order_id = 'c903603b-c091-49ad-833b-e7c02eb5c85c'
        self.cur.execute('''SELECT * FROM Orders WHERE order_id = ?''', [order_id])
        self.order11 = Order(self.cur.fetchone())
        self.order11.get_charge()




if __name__ == '__main__':
    o = Orders()
    # o.cur.execute('''SELECT * FROM Orders'''
    o.generate_random_orders(50)


    '''
        def get_all_location(self):
            return ['loc1','loc2','loc3', 'loc4']
    '''
