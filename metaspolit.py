#!/bin/usr/python3

import os
import socket
import sys
import time
import requests
import urllib3



os.system("clear")


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++ The War is not over yet ++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    
wa = """
                                                                          /?/       // 
                ++++++++++++                    ++++ +       + ++++    +--+-+      //
                ++++++++++++++                   ++++  ++    ++ ++++  +     +     //
                +++                              ++++   +    +  +++++      +     /_?____ ___
                +++                              ++++    +   +  ++++       +     |_____||__|
                +++                              ++++     + +   ++++    + ) )          || ? 
                +++                              ++++     + +   ++++        ) )        ||   ?
                +++    ++++++++    ++++++        
                +++     +++++      ++++++ 
                +++++++++++++                   +++         +++         +++ METASPOLIT 4
                +++++++++++++                     ++      +++  +++    ++ 
                                                    ++  +++     +++ ++
                                                       ++        +++ 




+++++++++++++++++++++++++++++++++ 0 Day GMissle port scanner +++++++++++++++++++++++++++++++++++++++






"""




print(wa)



def help_area():
    h_resources = """
    set -delete = Delete all content in database
    set -DB = Start a simple database creation
    set -mfsvenom = Create a backdoor to existing app or bind to an existing app to gain access
    set -wbserver = Start a webserver
    set -poison IP = poison an IP till it goes down 
    
    """
    print(h_resources)



def console_keyWords(con):
    con = con
    print("con > " +con)
    print("Metaspolit would like to create a DB (yes/no)?: ")
    ch = input("Choose option: ")
    if ch == "yes":
        caution_sign = '''

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        +     +++++++++++                                                       +                   
        +     /  ?  \   +                                                       +
        +    /  ??   \  +    CAUTION ONCE THis is done please run:                 +                             
        +   / __?____ \ +    bash db.sh to countinue                         +                        
        +   +++++++++++++                                                       +                     
        +                                                                       +
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                   






        '''
        print(caution_sign)
        time.sleep(10)
        print("please wait....")
        os.system("chmod 777 db.py")
        os.system("chmod 777 db.sh")
        print("done")
        
        





    elif ch == "no":
        os.system("clear")
        os.system("python3 main.py")

    else:
        print("[ X ] Incorrect...starting again")
        time.sleep(3)
        os.system("clear")
        os.system("python3 metaspolit.py")









print("[ X ] Starting metaspolit....")
time.sleep(5)
con = input("mfs4: ")
if con == "set -DB":
    console_keyWords(con)
elif con == "set -help":
    help_area()
        

else:
    print("Please try typing set -help to see Help command list")
    time.sleep(3)
    print("Starting again...in 3seconds")
    time.sleep(3)
    os.system("python3 metaspolit.py")
    






