#!/bin/python

import socket
import threading
from queue import Queue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ports_to_scan = range(1, 100)
ports_open = []

queue = Queue()
thread_list = []

def scanPort(host, port):
    try:
        sock.connect((host, port))
        return True
    except:
        return False
    
def fill_queue(ports):
    for i in (ports):
        queue.put(i)


def scanned():
    while not queue.empty():
        port = queue.get()
        if scanPort(port):
            print(f"Port {port} status: Open")
            ports_open.append(port)

def thread_open_ports():
    for i in range(10):
        thread = threading.Thread(target=scanned)
        thread_list.append(thread)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print(f"Open ports are: {ports_to_scan}")

def main():
    on = True
    print(" Py Port Scanner ")
    while on != False:

        host = input("Host IP you want scan >> ")
        scanPort(host, port=0)
        fill_queue(ports_to_scan)

        exit_app = input("Exit (y/n) >> ")
        if exit_app == 'y':
            on = False
        else:
            continue

main()#!/bin/python

import socket
import threading
from queue import Queue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ports_to_scan = range(1, 100)
ports_open = []

queue = Queue()
thread_list = []

def scanPort(host, port):
    try:
        sock.connect((host, port))
        return True
    except:
        return False
    
def fill_queue(ports):
    for i in (ports):
        queue.put(i)


def scanned():
    while not queue.empty():
        port = queue.get()
        if scanPort(port):
            print(f"Port {port} status: Open")
            ports_open.append(port)

def thread_open_ports():
    for i in range(10):
        thread = threading.Thread(target=scanned)
        thread_list.append(thread)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    print(f"Open ports are: {ports_to_scan}")

def main():
    on = True
    print(" Py Port Scanner ")
    while on != False:

        host = input("Host IP you want scan >> ")
        scanPort(host, port=0)
        fill_queue(ports_to_scan)

        exit_app = input("Exit (y/n) >> ")
        if exit_app == 'y':
            on = False
        else:
            continue

main()