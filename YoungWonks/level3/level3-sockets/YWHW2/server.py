from turtle import width
import pygame
import socket
from threading import Thread

EXIT_MESSAGE = 'exit'
CONNECTED = False
APP_OPEN = False
EXIT_SENT = False

def on_exit():
    global CONNECTED, APP_OPEN, EXIT_SENT
    
    if APP_OPEN:
        pygame.quit()
    
    if not EXIT_SENT:
        exit_message = EXIT_MESSAGE + ' ' * (1024-len(EXIT_MESSAGE))
        conn.sendall(exit_message.encode())
    if CONNECTED:
        conn.close()
    s.close()

s = socket.socket()
host = 'localhost'
port = 12346

pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

red = (255, 0, 0)
blue = (0, 0, 255)

class Square:
    def __init__(self, length, position, color, mass=0):
        self.length = length
        self.position = position
        self. color = color
        self. mass = mass
    
    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.length, self.length))
    
    def move(self, direction, amount):
        if direction == 'left':
            self.position[0] -= amount
        elif direction == 'right':
            self.position[0] += amount
        elif direction == 'up':
            self.position[1] -= amount
        elif direction == 'down':
            self.position[1] += amount

    def send_location(self):
        location = str(self.position[0]) + ', ' + str(self.position[1])
        location = location + ' ' * (1024-len(location))
        conn.sendall(location.encode())

def listen():
    global EXIT_SENT
    
    while True:
        try:
            data = conn.recv(1024).decode().strip()
        except:
            data = 'exit'

        if data == EXIT_MESSAGE:
            EXIT_SENT = True
            on_exit()
        else:
            x, y = data.split(', ')
            client.position = [int(x), int(y)]

s.bind((host, port))
s.listen(3)
conn, addr = s.accept()
CONNECTED = True

t1 = Thread(target=listen)
t1.start()

server = Square(32, [32, 32], red)
client = Square(32, [WIDTH-32, HEIGHT-32], blue)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if server.position[0] < 1:
                    server.position[0] = WIDTH
                server.move('left', 5)
            elif event.key == pygame.K_RIGHT:
                if server.position[0] > WIDTH:
                    server.position[0] = 1
                server.move('right', 5)
            elif event.key == pygame.K_UP:
                if server.position[1] < 1:
                    server.position[1] = HEIGHT
                server.move('up', 5)
            elif event.key == pygame.K_DOWN:
                if server.position[1] > HEIGHT:
                    server.position[1] = 1
                server.move('down', 5)
            
            server.send_location()
    
    window.fill((0, 0, 0))
    server.draw()
    client.draw()
    
    pygame.display.update()

pygame.quit()
APP_OPEN = False
on_exit()
