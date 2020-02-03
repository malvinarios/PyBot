#!/bin/python3

import sys
import time
import socket

# CONFIGURATION
nickname = "PyBot"
username = "PyIRC"
realname = "Python IRC Bot"
channel = "#Hellas"
server = "irc.provisionweb.org"
port = 5000


# Establish Connection
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.setblocking(False)
time.sleep(0.5)
irc.send(("USER " + username + " " + username + " " + " " + username + " " + realname + "\r\n").encode())
time.sleep(0.5)
irc.send(("NICK "+nickname+"\n").encode())
time.sleep(0.5)
irc.send(("JOIN "+channel+"\n").encode())

msg = "connecting to " + server + ":" + str(port) + "\n"
print(msg)

while 1:
    time.sleep(0.5)
    try:
        msg = irc.recv(2040)
        print(msg)
    except Exception:
        pass
    if str(msg).find("PING ") != -1:
        print("I GOT A PING. I HOPE I SEND A PONG BACK")
        irc.send(("PONG " + str(msg).split()[1]).encode())
    if str(msg).find('Closing link') != -1:
        exit()

input()
