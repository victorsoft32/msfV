#!/usr/bin/python3

import sqlite3
import os
import time
import requests



def headerToLogin():
    header = ''' 
 
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 
                          +++                  ++++++++             ++++++++++             ++++++++             +++                             +++
                          +++                  ++++++++             ++++++++++             ++++++++             +++                             +++
                          +++                   ++          ++             ++                                       ++++                  +++888888                 8888
                          +++                   ++          ++             ++                                       ++++                  +++ 888888                8888
                          +++                   ++          ++             ++                                       ++++                  +++   888888              8888
                          +++                   ++          ++             ++          ++++bb               ++++                 +++     8888888          8888
                          +++bbbbbb       ++          ++             ++            ++bb                  ++++                 +++       8888888        8888
                          +++bbbbbb       ++++++++             ++ ++++++bb             ++++++++           +++           888888      8888
                          +++bbbbbb       ++++++++             ++++++++++             ++++++++           +++            8888888888


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++ 0 Day GMissle port scanner +++++++++++++++++++++++++++++++++++++++ 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''


    print(header)








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
            else:
                print("error")
                
        con.close()
            
            
headerToLogin()



print("Login now to contiune")
print("")
user = input("Enter username: ")
passwd = input("Enter password: ")
print("Loading...")
login = userLogin(user,  passwd)
login.userLoginInfo()
    
