import sys 
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from model.init import conn, curr
from model.Wallet import Wallet

import uuid


class User:
    def __init__(self):
        pass
    
    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a user table
        '''
        con = conn()
        cur = curr()

        if saftey == 'off':
            cur.execute('''DROP TABLE IF EXISTS User''')

        cur.execute('''CREATE TABLE IF NOT EXISTS User(
                user_id text PRIMARY KEY,
                wallet_id text UNIQUE NOT NULL,
                name text,
                email text,
                phone_num text,
                password text,
                user_kind text
                );''')
        con.commit()

    def create_new(self):
        '''
        create user_id
        create wallet_id
        populate wallet table
        populate wallet table
        '''
        con, cur = [conn(), curr()]

        user_id = uuid.uuid4()
        wallet_id = uuid.uuid4()

        w = Wallet()
        w.create_new(wallet_id, user_id)

        cur.execute("""INSERT INTO test (user_id, wallet_id, name, email, phone_num, password, user_kind) VALUES(
            ?,
            ?,
            'Harsh Raj Verma',
            'noneofyourbznz@fo.com',
            '8333844575',
            'Not password',
            'Admin'
            );""", [user_id, wallet_id])






if __name__ == '__main__':
    u = User()
    u.CREATE_TABLE()
    u.create_new()
