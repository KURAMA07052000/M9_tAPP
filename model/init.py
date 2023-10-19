import sqlite3 as sql

CON = None
CUR = None

def conn():
    global CON
    if CON == None:
        CON = sql.connect('RentEV.db')
    return CON

def close_conn():
    if CON != None:
        CON.commit()
        CON.close()

def curr():
    global CUR
    if CUR == None:
        conn()
        CUR = CON.cursor()

    return CUR

def close_curr():
    if CUR != None:
        CUR.close()

if __name__ == '__main__':
    _c = conn()
    c = curr()

    c.execute('''DROP TABLE IF EXISTS test''')

    c.execute('''CREATE TABLE IF NOT EXISTS test(
              user_id text PRIMARY KEY,
              wallet_id text UNIQUE,
              name text,
              email text,
              phone_num text,
              password text,
              user_kind text
            );''')
    
    _c.commit()

    c.execute("""INSERT INTO test (wallet_id, name, email, phone_num, password, user_kind) VALUES(
            1,
            'Harsh Raj Verma',
            'noneofyourbznz@fo.com',
            '8333844575',
            'Not password',
            'Admin'
            );""")
    
    _c.commit()

    c.execute("SELECT * FROM test")

    for i in c.fetchall():
        print(i)

