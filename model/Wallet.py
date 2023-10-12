import sys 
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from model.init import conn, curr

class Wallet:
    def __init__(self):
        self.cur = curr()
        self.con = conn()
    
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




if __name__ == '__main__':
    u = Wallet()
    u.CREATE_TABLE()
    u.print_all()
