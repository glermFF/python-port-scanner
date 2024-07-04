#!/bin/python

import socket
import sys
from pyfiglet import figlet_format
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
open_ports = []

def scanPort(host_ip):
    try:
        for port in range(20, 100):
            sleep(1.0)
            conn = sock.connect_ex((host_ip, port))
            if conn:
                print(f"Status da porta {port}: Aberta")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\nFinalizando scan.")
        sys.exit()
    except socket.error:
        print("\n O host não responde.")


if __name__ == "__main__":
    title = figlet_format("PyPortScanner")
    print(title)
    print("-" * 50)
    host_ip = input("Endereço IPv4 do desejado host a ser analisado >> ")
    scanPort(host_ip)