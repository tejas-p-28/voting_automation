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
                conduct_election()
            elif ch == 2 :
                add_voter()
            elif ch == 3 :
                update_voter()
            elif ch == 4:
                log_out()
            else:
                print('ERROR : Invalid Input')

def conduct_election():
    print('1')

def add_voter():
    print('2')

def update_voter():
    print('3')

def log_out():
    print('4')