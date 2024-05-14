import sqlite3
import pygame


conn = sqlite3.connect('TowerDefense.db')
c = conn.cursor()

def create_database():
    c.execute("CREATE TABLE IF NOT EXISTS allies (name TEXT, power INTEGER, cost INTEGER, sell INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS enemies (name TEXT, health INTEGER, speed INTEGER, points INTEGER)")
    
    c.execute("INSERT INTO allies VALUES ('Basic', 1, 2, 1)")
    c.execute("INSERT INTO allies VALUES ('Intermediate', 3, 5, 3)")
    c.execute("INSERT INTO allies VALUES ('Advanced', 6, 10, 5)")
    
    c.execute("INSERT INTO enemies VALUES ('Triangle', 1, 3, 1)")
    c.execute("INSERT INTO enemies VALUES ('Square', 5, 1, 3)")
    c.execute("INSERT INTO enemies VALUES ('Circle', 5, 3, 7)")


class Ally:
    def __init__(self, power, cost, sell, location):
        self.power = power
        self.cost = cost
        self.sell = sell
        self.location = location
    
    def attack(self, enemy):
        enemy.take_damage(self.power)
    
    def sell_ally(self, game):
        game.deposit(self.sell)
        game.allies.remove(self)
        
class Enemy:
    def __init__(self, health, speed, points, location):
        self.health = health
        self.speed = speed
        self.points = points
        self.location = location

    def move(self):
        # move along the path 1 tile
        pass
    
    def take_damage(self, damage):
        self.health -= damage
    
    def defeated(self, game):
        game.deposit(self.points)
        game.enemies.remove(self)

class Game:
    def __init__(self, board, points, allies, enemies):
        self.board = board
        self.points = points
        self.allies = allies
        self.enemies = enemies
    
    def deposit(self, amount):
        self.points += amount
    
    def buy(self, ally):
        if self.points >= ally.cost:
            self.allies.append(ally)
            self.spawn_ally(ally.location, ally)
            self.points -= ally.cost
        else:
            raise Exception('Not enough money. PLEASE ADD SOMETHING TO THIS LINE THAT MAKES THIS LOOK BETTER THAN AN ERROR')
    
    def spawn_enemy(self, type, location):
        if type == 'triangle':
            enemy = Enemy(1, 3, 1, location)
        elif type == 'square':
            enemy = Enemy(5, 1, 3, location)
        elif type == 'circle':
            enemy = Enemy(5, 3, 7, location)

        self.enemies.append(enemy)
        # raise Exception('Please put some code in here. It would be much appreciated!')
        
    def spawn_ally(self, type, location):
        if type == 'basic':
            ally = Ally(1, 2, 1, location)
        elif type == 'intermediate':
            ally = Ally(3, 5, 3, location)
        elif type == 'advanced':
            ally = Ally(6, 10, 5, location)
        
        self.allies.append(ally)
        # raise Exception('Please put some code in here. It would be much appreciated!')

map = [
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 3],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0]
]

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tower Defense')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    window.fill('#e3d9c4')
    for row in range(len(map)):
        for tile in range(len(map[row])):
            if map[row][tile] == 0:
                pygame.draw.rect(window, (0, 0, 0), (tile * 90, row * 90, 90, 90))
            elif map[row][tile] == 1:
                pygame.draw.rect(window, (0, 0, 255), (tile * 90, row * 90, 90, 90))
            elif map[row][tile] == 2:
                pygame.draw.rect(window, (0, 255, 0), (tile * 90, row * 90, 90, 90))
            elif map[row][tile] == 3:
                pygame.draw.rect(window, (255, 0, 0), (tile * 90, row * 90, 90, 90))
    
    pygame.display.update()

pygame.quit()
