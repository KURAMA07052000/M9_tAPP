import sys 
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from model.init import conn, curr
from model.Wallet import Wallet

import uuid


class User:
    def __init__(self):
        self.con = conn()
        self.cur = curr()
    
    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a user table
        '''

        if saftey == 'off':
            self.cur.execute('''DROP TABLE IF EXISTS User''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS User(
                user_id text PRIMARY KEY,
                wallet_id text UNIQUE NOT NULL,
                name text,
                email text,
                phone_num text,
                password text,
                user_kind text
                );''')
        self.con.commit()

    def create_new(self, data:{}):
        '''
        create user_id
        create wallet_id
        populate wallet table
        populate wallet table
        '''

        user_id = str(uuid.uuid4())
        wallet_id = str(uuid.uuid4())

        w = Wallet()
        w.create_new(wallet_id, user_id)

        self.cur.execute("""INSERT INTO User (user_id, wallet_id, name, email, phone_num, password, user_kind) VALUES(
            ?,
            ?,
            "Harsh Raj Verma",
            "noneofyourbznz@fo.com",
            "8333844575",
            "Not password",
            "Admin"
            );""", (user_id, wallet_id))


    def print_all(self):
        self.cur.execute('SELECT * FROM User')
        for i in self.cur.fetchall():
            print(i)

if __name__ == '__main__':
    u = User()
    u.create_new()
    u.print_all()
