#!/bin/usr/python3

import os
import socket
import sys
import time
import requests
import urllib3

os.system("clear")


class warZone:
    def __init__(self, misselHead):
        self.misselHead = misselHead

    def missleLaucher(self):
        print(self.misselHead)




print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++ The War is not over yet ++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    
misselHead = """
                                                                          /?/  
                ++++++++++++                    ++++ +       + ++++    +--+-+
                ++++++++++++++                   ++++  ++    ++ ++++  +     +
                +++                              ++++   +    +  +++++      +
                +++                              ++++    +   +  ++++       +
                +++                              ++++     + +   ++++    + ) )
                +++                              ++++     + +   ++++        ) )
                +++    ++++++++    ++++++        
                +++     +++++      ++++++ 
                +++++++++++++
                +++++++++++++





+++++++++++++++++++++++++++++++++ 0 Day GMissle port scanner +++++++++++++++++++++++++++++++++++++++






"""



ripple = warZone(misselHead)
ripple.missleLaucher()







machine = socket.gethostname()


url = "http://localhost"

url_response = urllib3.PoolManager()

if url_response.request("GET", url):
    url_status = url_response.request("GET", url)
    url_header_status = url_status.status

    if url_header_status == 200:
        ports_to_scan = {"webports_1" : 80, 
                    "webports_2" : 8080, 
                    "webports_3" :1080,
                    "ftp_ports" : 1080,
                    "printers_port" : 5590
                    
                    }
        port1 = ports_to_scan["webports_1"]
        port2 = ports_to_scan["webports_2"]
        port3 = ports_to_scan["webports_3"]

        ports_in = []
        ports_in.insert(0, ports_to_scan)
        sudo = "root"

        ipPinger = input("Enter ip address to run a port scan: ")

       

        print("1 => Web Scans using port 80")
                
        print("2 => Web Scans using port 80")
    
        print("3 => FTP port scan")

        print("4 => Use Metaspolit Scanner")

        print("")
        r = input("Select an Option: ")
        
        if sudo:
            
            if r == "1":
                if port1 == ports_to_scan["webports_1"]:
                    os.system("checking for back ports....")
                    time.sleep(5)
                    print("[X] Starting Apache......")
                    time.sleep(5) 
                    os.system("systemctl start apache2")
                    time.sleep(5)
                    print("[OK] Apache started successfully")
                    time.sleep(5)
                    print("+++++++++++++++++ Result ++++++++++++++++++++")

                    os.system("nmap -p 80 " +ipPinger)
                        
                    print("++++++++++++++++++++++++++++++++++++++++++++++")

            elif r == "2":
                if port2 == ports_to_scan["webports_2"]:
                    os.system("checking for back ports....")
                    time.sleep(5)
                    print("[X] Starting Apache......")
                    time.sleep(5) 
                    os.system("systemctl start apache2")
                    time.sleep(5)
                    print("[OK] Apache started successfully")
                    time.sleep(5)
                    print("+++++++++++++++++ Result ++++++++++++++++++++")

                    os.system("nmap -p 8080 " +ipPinger)
                        
                    print("++++++++++++++++++++++++++++++++++++++++++++++")

                        
            elif r == "3":
                if port3 == ports_to_scan["webports_3"]:
                    os.system("checking for back ports....")
                    time.sleep(5)
                    print("[X] Starting Apache......")
                    time.sleep(5) 
                    os.system("systemctl start apache2")
                    time.sleep(5)
                    print("[OK] Apache started successfully")
                    time.sleep(5)
                    print("+++++++++++++++++ Result ++++++++++++++++++++")

                    os.system("nmap -p 1080 " +ipPinger)
                        
                    print("++++++++++++++++++++++++++++++++++++++++++++++")

            elif r == "4":
                from metaspolit import *
                
                        
            else:
                print("Invalid")



        else:
            print("Please run as root first")
            
    else:
        print("[X]: Not yet pawned")




else:
     print("error")

