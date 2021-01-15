import pygame
import socket

pygame.init()

WIDTH, HEIGHT = 1280, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)

PORT = 5555
SERVER = input("Server IP (Local): ")
ADDR = (SERVER, PORT)
QUIT_MSG = "\\quit"
FORMAT = "utf-8"
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def Send(msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength = b' ' * (HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)


def Main():
    FPS = 60
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        DISPLAY.fill(BLACK)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                Send(QUIT_MSG)
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                Send("Mousebutton down")

        pygame.display.update()


Main()