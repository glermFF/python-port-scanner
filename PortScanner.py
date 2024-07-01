#!/bin/python

import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = [80, 433, 8080, 9090]

def scanPort(host):
    
    for i in port:
        if tcp.connect_ex((host, i)):
            print(f"Port {i} status: Open")
        else:
            print(f"Port {i} status: Closed")

def main():
    on = True
    print(" Py PORT SCANNER ")
    while on != False:

        host = input("Host IP you want scan >> ")
        scanPort(host)

        exit_app = input("Exit (y/n) >> ")
        if exit_app == 'y':
            on = False
        else:
            continue

main()