#!/bin/python

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scanPort(port):
    if soc.connect_ex((host, port)):
        print(f"Port {port} status: Open")
    else:
        print(f"Port {port} status: Closed")

host = input("Host IP you want scan >> ")
port = int(input("Port from the Host you want scan >> "))

scanPort(port)