import socket
import pygame



HEADER = 64
PORT = 5050
FORMAT = "utf-8"
QUIT_MSG = "\\quit"
SERVER = input("Server IP (Local): ")
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def Send(msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

while True:
    sendMsg = input("Message: ")
    Send(sendMsg)