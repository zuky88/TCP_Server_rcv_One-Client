#!/usr/bin/env python3

import threading
import datetime
import socket

ADDRESS = '127.0.0.1'
PORT = 60000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen()

def serverMain(clientno, client):
    while True:
        msg = client.recv(BUFSIZE).decode()
        now = str(datetime.datetime.now())
        print("[server]Received message from client({0}):{1}[{2}]".format(clientno, msg, now))

def thread_start():
    clientno = 0
    print('[server]Waiting access from client.')
    client, address = server.accept()
    now = str(datetime.datetime.now())
    clientno += 1
    print("[server]Conected client({0}, {1}, {2})[{3}]".format(clientno, client, address, now))
    t = threading.Thread(target = serverMain, args=(clientno, client,))
    t.setDaemon(True)
    t.start()





