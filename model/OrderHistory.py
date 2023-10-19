import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
# from model.Wallet import Wallet

import uuid


class OrderHistory:

    def set_user_id(self, user_id: int):
        self.user_id = user_id

    def __init__(self):
        self.cur = curr()
        self.con = conn()
        self.user_id = None
        pass

    def order_history_user_legacy(self, user_id : str = None):
        '''
        Get order history for a user
        '''
        if user_id != None:
            self.user_id = user_id

        self.cur.execute("""SELECT * FROM Orders WHERE user_id = ?;""", [user_id])
        row = self.cur.fetchall()
        for ro in row:
            print(ro)
        return row

    '''
        method: order_history_user
        input: user_id : str = None
        return: lists[(order_id, vehicle_id, start_time, end_time),...]
    '''
    def order_history_user(self, user_id : str = None):
        '''
        Get order history for a user
        '''
        if user_id != None:
            self.user_id = user_id

        # select order_id, vehicle_id, start_time, end_time
        self.cur.execute("""SELECT order_id, vehicle_id, start_time, end_time FROM Orders WHERE user_id = ?;""", [user_id])
        row1 = self.cur.fetchall()
        row = [list(item) for item in row1]
        print(row)
        for ro in row:
            ro[2] = datetime.datetime.strptime(ro[2], '%Y-%m-%d %H:%M:%S.%f')
            # convert type:
            ro[2] = ro[2].strftime("%d/%m/%Y, %H:%M:%S")
            if ro[3] != None:
                ro[3] = datetime.datetime.strptime(ro[3], '%Y-%m-%d %H:%M:%S.%f')
                ro[3] = ro[3].strftime("%d/%m/%Y, %H:%M:%S")

        return row







if __name__ == '__main__':
    u = OrderHistory()
    u.order_history_user('f4e020a0-3874-4dc0-9c65-2f010fc94005')

