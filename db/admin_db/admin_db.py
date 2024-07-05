import sqlite3
def sqlI():
    print('this is sql')
dbc_in_file = sqlite3.connect('election_db')
db_cursor = dbc_in_file.cursor()
db_cursor.execute('''create table if not exists admin_db
    (id int primary key,
    name varchar(50),
    pswd int);''')

admin_id = 3
name = 'tejas'
pswd = 123

query = f""" insert into admin_db (id,name,pswd) values({admin_id},'{name}',{pswd})"""
db_cursor.execute(query)
dbc_in_file.commit()
db_cursor.execute('select * from admin_db')
rows = db_cursor.fetchall()
for i in rows:
    print(i)

dbc_in_file.close()