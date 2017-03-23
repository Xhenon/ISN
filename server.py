#-*-coding: utf-8 -*-
import socket
from threading import Thread
from time import sleep

ip = "192.168.0.49"
#ip = input("ip du serveur: ")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ip
#socket.gethostname()
port = 25565
serversocket.bind((host, port))
serversocket.listen(5)
global x , clientDict
clientDict = {}
x=0

def loop(client , id):
     global x
     run = True
     while run:
        try:
            data = client.recv(1024).decode()
        except :
            x=0
            clientDict.clear()
            print("----exception----")
            run = False
        else:
            d = data.split(" ")
            print(str(client) , data)
            if data == "connection":
                sendTo(client , "j "+str(x))
                print("Authentification du client")
            elif data=="giveup":
                sendToAll("giveup "+ str(id))
                print("Abandon de", id)
            elif data== "swap":
                print("--Inversion des joueurs--")
                sendToSeveral(getOtherClientID(id) , data)
            elif d[0] == "placer1" or d[0] == "placer2" or d[0] == "placer1f":
                print("Click", id)
                sendToSeveral(getOtherClientID(id) , data)
            elif data=="closing":
                x=0
                clientDict.clear()
                print("déconnexion")
                run = False

def sendToAll(msg):
    try:
        for i in clientDict:
            clientDict[i].send(msg.encode())
    except:
        x=0
        clientDict.clear()
        print("----exception----")


def getOtherClientID(index):
    clients = []
    for i in clientDict:
        if i != index:
            clients.append(i)
    return clients


def sendTo(client , msg):
    try:
       client.send(msg.encode())
    except:
        x=0
        clientDict.clear()
        print("----exception----")

def sendToSeveral(clientid , msg):
    try:
       for i in clientid:
        clientDict[i].send(msg.encode())
    except:
        x=0
        clientDict.clear()
        print("----exception----")

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
