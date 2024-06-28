# from db.admin_db import admin_db
import sqlite3

from modules.header import head
from modules.u_input import u_input
max_retry = 1
def verify_cred(u_name,u_pswd):
    
    for i in range(max_retry):
        
        dbc_in_file = sqlite3.connect('election_db')
        db_cursor = dbc_in_file.cursor()
        query = f"select * from admin_db where name = '{u_name}' and pswd={u_pswd};"
        db_cursor.execute(query)
        if not db_cursor.fetchone():
            print('ERROR : invalid credentials')
        else:
            head.header()
            print(f'Welcome !!! You are admin {u_name}')
            admin = ['Conduct Election','Add Voter','Update Voter','Log Out']
            for i,j in enumerate(admin,1):
                print(f'{i}) {j}')
            print('hie')   
            ch = int(input('enter your choice : '))
            if ch == 1:
                conduct_election(u_name)
            elif ch == 2 :
                add_voter()
            elif ch == 3 :
                update_voter()
            elif ch == 4:
                log_out()
            else:
                print('ERROR : Invalid Input')

def conduct_election(u_name):
    head.header(f'Welcome, Admin {u_name}')
    dbc_in_file = sqlite3.connect('election_db')
    db_cursor = dbc_in_file.cursor()
    db_cursor.execute('''create table if not exists constituent 
        (id integer primary key autoincrement,
        const_name varchar(50));''')
    const_name = input('enter the constituency name : ')
    const = f'''INSERT INTO constituent (const_name)
        SELECT '{const_name}'
        FROM (SELECT 1) AS src
        WHERE NOT EXISTS (SELECT 1 FROM constituent WHERE const_name = '{const_name}');'''
    db_cursor.execute(const)
    result =  db_cursor.fetchone()
    for i in result:
        print('constituency already exists')
    else:
        print(f'{const_name} added !!!!')
    dbc_in_file.commit()
    db_cursor.execute('select * from constituent')
    result1 = db_cursor.fetchall()
    for i in result1:
        print(i)
    
    # const = f"SELECT * FROM constituent WHERE const_name = '{const_name}';"
    
    


    dbc_in_file.close()
def add_voter():
    print('2')

def update_voter():
    print('3')

def log_out():
    print('4')