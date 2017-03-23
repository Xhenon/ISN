import socket
import sys

def recieve():
    while True:
        data = ''
        data = s.recv(1024).decode()

#ip = input("adresse ip: ")
ip = "192.168.0.49"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port =25565
s.connect((ip,port))

thread1 = Thread(target = recieve)
#thread1.start()
s.send("closing".encode())
s.close
sys.exit(0)


