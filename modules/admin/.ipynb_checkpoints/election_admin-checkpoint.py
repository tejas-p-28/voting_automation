# from db.admin_db import admin_db
import sqlite3
from datetime import datetime
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
    if result == const_name:
        print('constituency already exists')
    else:
        print(f'{const_name} added !!!!')
        max_retry = 3
        for i in range(max_retry):
            date = input('enter the date for commencement (DD-MM-YYYY) : ')
            print('Enter the start time : ')
            hour = input('enter Hour for the commencement : ')
            minute = input('enter minute for the commencement : ')
            date1 = datetime.strptime(date, '%d-%m-%y')
            if date1 > datetime.now():
                print(f' election to start from {date1} at {hour}:{minute} am')
                end_date = input('enter the end date for the election : ')
                print(f'election to be end in {end_date} days')
                break
            else:
                print('please enter the date in future')
    dbc_in_file.commit()
    
    
    # const = f"SELECT * FROM constituent WHERE const_name = '{const_name}';"
    
    


    dbc_in_file.close()
def add_voter():
    head.header()
    print(r"Enter voter's details : ")
    full_name = input('Full Name : ')
    print('Name Stored')

def update_voter():
    print('3')

def log_out():
    print('4')