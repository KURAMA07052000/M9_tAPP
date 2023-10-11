from model.init import conn, curr

class Wallet:
    def __init__(self):
        pass
    
    def CREATE_TABLE(self, saftey='on'):
        '''
        Create a user table
        '''
        con = conn()
        cur = curr()

        if saftey == 'off':
            cur.execute('''DROP TABLE IF EXISTS Wallet''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Wallet(
                wallet_id text PRIMARY KEY,
                user_id text UNIQUE NOT NULL,
                balance INTEGER NOT NULL
                );''')
        con.commit()

    def create_new(self, wallet_id, user_id):
        '''
        create user_id
        create wallet_id
        populate wallet table
        populate wallet table
        '''
        con, cur = [conn(), curr()]
        
        cur.execute("""INSERT INTO Wallet (wallet_id, user_id, balance) VALUES(
            ?,
            ?,
            0
            );""", [wallet_id, user_id])
        
        con.commit()




if __name__ == '__main__':
    u = User()
    u.create_new()
