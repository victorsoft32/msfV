#!/usr/bin/python3


from pynput.keyboard import Listener
import os
import time
import sqlite3
import random





class userLogin:
    def __init__(self,  user,  passwd):
        self.user = str(user)
        self.passwd = str(passwd)
        
    def userLoginInfo(self):
        
        user1 = self.user
        pass1 = self.passwd
        
        con =  sqlite3.connect("tr.db")
        conr = con.cursor()
        
        query = '''select * from admin_login where username = (?) '''
        query2 = [
            (user1)
        ]
        conr.execute(query,  query2)
        result = conr.fetchall()
        for results in result:
            userid = results[0]
            username = results[1]
            if username == username:
                print("[ OK ] Welcome back ",  username)
                
        con.close()
            
            
            
        
        
        







def create_new_db(sql_create_table):
    sql = sql_create_table
    file_path = "tr.db"
    con = sqlite3.connect(file_path)
    conr = con.cursor()
    conr.execute(sql)
    con.commit()
    con.close()
    

def create_admin_table(sql_admin_table):
    admin_sql = sql_admin_table
    file_path = "tr.db"
    con = sqlite3.connect(file_path)
    conr = con.cursor()
    conr.execute(admin_sql)
    con.commit()
    con.close()
    
    
def create_table_root(username, password):
    username = str(username)
    password = str(password)

    con = sqlite3.connect("tr.db")
    cor = con.cursor()
    randomID = random.randint(0, 10000)
    random_guestID = random.randint(0, 10000)
    sql = ''' insert into admin_login ("admin_id", "username", "password") values (?, ?, ?)'''

    

    r =  [
            (randomID, username, password), 
            (random_guestID,  'guest',  'guest')
          ]
        
        
    

    cor.executemany(sql, r)
    con.commit()
    con.close()








sql_create_table = ''' create table data_feeds (
    fid int(30) primary key,
    data_name text not null,
    data_log text not null
    )
'''

sql_admin_table = ''' create table admin_login (
    admin_id int(30) primary key,
    username varchar(32) not null,
    password varchar(32) not null
)'''



db_success = create_new_db(sql_create_table)
db_admin_table = create_admin_table(sql_admin_table)

db_error = "Unable to create DB"

if db_success == db_success:
    
    print("")
    print("Create a user login")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    print("[ X ] creating.....")
    
    create_table_root(username, password)
    
    print("[ OK ] Done")
    
    print("[ OK ] Adding guest logging and setting it to username: guest and password: guest")
    
    print("[ OK ] Done")
    
    print("Login now to contiune")
    print("")
    user = input("Enter username: ")
    passwd = input("Enter password: ")
    
    login = userLogin(user,  passwd)
    login.userLoginInfo()
    

else:
    print(db_error)








