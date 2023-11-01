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
        self.UserID = None
        self.UserType = None
    
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
                email text UNIQUE,
                phone_num text,
                password text,
                user_kind text
                );''')



        self.con.commit()

    def create_new(self, name:str, email:str, phone_num:str, password:str, user_kind:str):
        '''
        create user_id
        create wallet_id
        populate wallet table
        populate wallet table
        '''

        user_id = str(uuid.uuid4())
        wallet_id = str(uuid.uuid4())
        # check if email have already been signed
        self.cur.execute("""SELECT email FROM User WHERE email=?""", (email,))
        self.con.commit()
        if len(self.cur.fetchall())!=0:
            print('Email already exists')
            return False

        self.cur.execute("""INSERT INTO User (user_id, wallet_id, name, email, phone_num, password, user_kind) VALUES(
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
            );""", [user_id, wallet_id, name, email, phone_num, password, user_kind])
        
        w = Wallet()
        w.create_new(wallet_id, user_id)

        self.con.commit()
        return True

        
    
    def login(self, email:str, password:str):
        email = str(email)
        password = str(password)
        print(email)
        print(password)
        self.cur.execute("""SELECT user_id, wallet_id, user_kind FROM User WHERE email=? AND password=?""", (email, password))
        self.con.commit()
        try:
            ret = list(self.cur.fetchall()).copy()[0]
            print('Login details', ret)
            return ret
        except Exception as e:
            print('Login failed')
        
        return [None]*3


    def print_all(self):
        self.cur.execute('SELECT * FROM User')
        for i in self.cur.fetchall():
            print(i)

    def set_id(self, id:str, type:str):
        self.UserID = id
        self.UserType = type

if __name__ == '__main__':
    u = User()
    # u.CREATE_TABLE('on')
    u.print_all()
    # u.create_new('1', '1', '1','1', 'user')
