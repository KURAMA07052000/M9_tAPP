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

    def order_history_user(self, user_id : str = None):
        '''
        Get order history for a user
        '''
        if user_id != None:
            self.user_id = user_id

        self.cur.execute("""SELECT * FROM Orders WHERE user_id = ?;""", [user_id])
        row = self.cur.fetchall()
        return row


if __name__ == '__main__':
    u = OrderHistory()

