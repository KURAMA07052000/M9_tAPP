import sys 
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from model.init import conn, curr

class Wallet:
    def __init__(self):
        self.cur = curr()
        self.con = conn()
        self.WalletID = None
        self.balance = 0
    
    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a user table
        '''

        if saftey == 'off':
            self.cur.execute('''DROP TABLE IF EXISTS Wallet''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS Wallet(
                wallet_id text PRIMARY KEY,
                user_id text UNIQUE NOT NULL,
                balance INTEGER NOT NULL
                );''')
        self.con.commit()

    def create_new(self, wallet_id, user_id):
        '''
        create user_id
        create wallet_id
        populate wallet table
        populate wallet table
        '''
        
        self.cur.execute("""INSERT INTO Wallet (wallet_id, user_id, balance) VALUES(
            ?,
            ?,
            0
            );""", [wallet_id, user_id])
        
        self.con.commit()

    def print_all(self):
        self.cur.execute('SELECT * FROM Wallet')
        for i in self.cur.fetchall():
            print(i)

    def set_id(self, id):
        self.WalletID = id

    def refresh(self):
        self.cur.execute('''SELECT balance FROM Wallet WHERE wallet_id=? LIMIT 1''', [self.WalletID])
        self.balance = self.cur.fetchall().copy()[0][0]

    def update_balance(self, val:int):
        self.cur.execute('''UPDATE Wallet SET balance=balance+? WHERE wallet_id=?''', [int(val),self.WalletID])
        self.con.commit()
        self.refresh()


if __name__ == '__main__':
    u = Wallet()
    u.print_all()
    u.set_id('0f8dc118-60ef-4115-ad03-71986f099464')
    u.update_balance('10')
    print(u.balance)

