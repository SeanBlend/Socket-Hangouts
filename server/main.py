import socket
import threading

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
QUIT_MSG = "\\quit"
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def Server(conn, addr):
    print(f"[NEW CONNECTION] New player {addr}")

    while True:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == QUIT_MSG:
                break

            print(msg)

    conn.close()
    return


def Main():
    server.listen()
    while True:
        conn, addr = server.accept()
        client = threading.Thread(target=Server, args=(conn, addr))
        client.start()


print(f"[SERVER] Server is starting on {SERVER}")
Main()