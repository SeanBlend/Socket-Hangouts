import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
QUIT_MSG = "\\quit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def HandleClient(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")

    while True:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == QUIT_MSG:
                break

            print(msg)
            sendMsg = input("Message: ").encode(FORMAT)
            conn.send(sendMsg)

    conn.close()


def Start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        
        conn, addr = server.accept()
        thread = threading.Thread(target=HandleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
Start()