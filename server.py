#-*-coding: utf-8 -*-
import socket
from threading import Thread
from time import sleep

#ip = "192.168.0.49"
ip = input("ip du serveur: ")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ip
#socket.gethostname()
port = 25565
serversocket.bind((host, port))
serversocket.listen(5)
x=0

def loop(client , id):
     while True:
        data = client.recv(1024).decode()
        d = data.split(" ")
        print(str(client) , data)
        if data == "connection":
            sendTo(client , "j "+str(x))
            print("authentification du client")
        elif d[0] == "placer1" or d[0] == "placer2":
            print("mise à jour des clics")
            sendToSeveral(getOtherClientID(id) , data)

def getOtherClientID(index):
    clients = []
    for i in clientDict:
        if i != index:
            clients.append(i)
    return clients


def sendTo(client , msg):
    client.send(msg.encode())

def sendToSeveral(clientid , msg):
    for i in clientid:
        clientDict[i].send(msg.encode())

clientDict = {}

while True:
    (clientsocket, address) = serversocket.accept()
    x += 1
    clientDict[x] = clientsocket
    print(len(clientDict) , "joueurs connecté(s)")
    thread1 = Thread(target = loop , args=(clientsocket,x,))
    thread1.start()


##    data = clientsocket.recv(1024).decode()
##    print (data)
##    r='REceieve'
##    clientsocket.send(r.encode())
