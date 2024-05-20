import sqlite3
import pygame


conn = sqlite3.connect('TowerDefense.db')
c = conn.cursor()

def create_database():
    c.execute("CREATE TABLE IF NOT EXISTS allies (name TEXT, power INTEGER, range INTEGER, cost INTEGER, sell INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS enemies (name TEXT, health INTEGER, speed INTEGER, points INTEGER)")
    
    c.execute("INSERT INTO allies VALUES ('Basic', 1, 3, 2, 1)")
    c.execute("INSERT INTO allies VALUES ('Intermediate', 3, 4, 5, 3)")
    c.execute("INSERT INTO allies VALUES ('Advanced', 6, 6, 10, 5)")
    
    c.execute("INSERT INTO enemies VALUES ('Triangle', 1, 3, 1)")
    c.execute("INSERT INTO enemies VALUES ('Square', 5, 1, 3)")
    c.execute("INSERT INTO enemies VALUES ('Circle', 5, 3, 7)")
    
    conn.commit()


class Ally:
    def __init__(self, power, cost, range, sell, location):
        self.power = power
        self.range = range
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
        self.last_position = location

    def move(self, board):
        # move along the path 1 tile
        pass
    
    def take_damage(self, damage):
        self.health -= damage
    
    def defeated(self, game):
        game.deposit(self.points)
        game.enemies.remove(self)

class Tile:
    def __init__(self, type, location):
        self.location = location
        self.type = type
        self.next = None
        self.previous = None
    
    def draw(self):
        if self.type == 0:
            pygame.draw.rect(window, (0, 0, 0), (self.location[1] * 90, self.location[0] * 90, 90, 90))
        elif self.type == 1:
            pygame.draw.rect(window, (0, 0, 255), (self.location[1] * 90, self.location[0] * 90, 90, 90))
        elif self.type == 2:
            pygame.draw.rect(window, (0, 255, 0), (self.location[1] * 90, self.location[0] * 90, 90, 90))
        elif self.type == 3:
            pygame.draw.rect(window, (255, 0, 0), (self.location[1] * 90, self.location[0] * 90, 90, 90))

class Shop:
    def __init__(self):
        c.execute("SELECT * FROM allies")
        self.allies = c.fetchall()
        print(self.allies)
    
    def draw(self, game):
        for ally in self.allies:
            if game.points >= ally[3]:
                if ally[0] == 'Basic':
                    pygame.draw.rect(window, (0, 255, 0), (750, 20, 30, 70))
                elif ally[0] == 'Intermediate':
                    pygame.draw.rect(window, (0, 0, 255), (820, 20, 30, 70))
                elif ally[0] == 'Advanced':
                    pygame.draw.rect(window, (255, 0, 0), (890, 20, 30, 70))
            elif game.points <= ally[3]:
                if ally[0] == 'Basic':
                    pygame.draw.rect(window, (0, 255, 0), (750, 20, 30, 70), width=3)
                elif ally[0] == 'Intermediate':
                    pygame.draw.rect(window, (0, 0, 255), (820, 20, 30, 70), width=3)
                elif ally[0] == 'Advanced':
                    pygame.draw.rect(window, (255, 0, 0), (890, 20, 30, 70), width=3)

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
    
    def spawn_enemy(self, type, location):  # TODO: Numbers update with database
        if type == 'triangle':
            enemy = Enemy(1, 3, 1, location)
        elif type == 'square':
            enemy = Enemy(5, 1, 3, location)
        elif type == 'circle':
            enemy = Enemy(5, 3, 7, location)

        self.enemies.append(enemy)
        # raise Exception('Please put some code in here. It would be much appreciated!')
        
    def spawn_ally(self, type, location):  # TODO: Numbers update with database
        if type == 'basic':
            ally = Ally(1, 3, 2, 1, location)
        elif type == 'intermediate':
            ally = Ally(3, 4, 5, 3, location)
        elif type == 'advanced':
            ally = Ally(6, 6, 10, 5, location)
        
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

for row in map:
    for tile in row:
        if tile == 2:
            start_pos = (row, tile)
        elif tile == 3:
            end_pos = (row, tile)

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tower Defense')
FPS = 30

# create_database()
game = Game(map, 9, [], [])
shop = Shop()


next_enemy = 0
frames = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    if frames % FPS == 0:
        if next_enemy // 20 == 0:
            game.spawn_enemy('triangle', start_pos)
        elif next_enemy // 20 == 1:
            game.spawn_enemy('square', start_pos)
        else:
            game.spawn_enemy('circle', start_pos)
        
        next_enemy += 1
            
    
    window.fill('#e3d9c4')
    for row in range(len(game.board)):
        for tile in range(len(game.board[row])):
            if map[row][tile] == 0:
                pygame.draw.rect(window, (0, 0, 0), (tile * 90, row * 90, 90, 90))
            elif map[row][tile] == 1:
                pygame.draw.rect(window, (0, 0, 255), (tile * 90, row * 90, 90, 90))
            elif map[row][tile] == 2:
                pygame.draw.rect(window, (0, 255, 0), (tile * 90, row * 90, 90, 90))
            elif map[row][tile] == 3:
                pygame.draw.rect(window, (255, 0, 0), (tile * 90, row * 90, 90, 90))
    shop.draw(game)
    
    pygame.display.update()
    
    frames += 1

pygame.quit()
