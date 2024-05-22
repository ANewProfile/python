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
    
    c.execute("INSERT INTO enemies VALUES ('Triangle', 1, 1, 1)")
    c.execute("INSERT INTO enemies VALUES ('Square', 5, 2, 3)")
    c.execute("INSERT INTO enemies VALUES ('Circle', 5, 1, 7)")
    
    conn.commit()

def clear_tables_data():
    c.execute("DELETE FROM allies")
    c.execute("DELETE FROM enemies")
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

    def move(self, game):
        print("location is",self.location[0],self.location[1])
        current_tile = game.linked_map[(self.location[0], self.location[1])]
        print("current tile", current_tile.type)
        next_tile = game.linked_map[(self.location[0], self.location[1])].next
        print(next_tile.location)
        # print(next_tile.type)
        if next_tile.type == 3:
            game.lives -= 1
            game.enemies.remove(self)
        else:
            self.location = next_tile.location
    
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

    def set_next(self, next_tile):
        self.next = next_tile

    def set_previous(self, previous_tile):
        self.previous = previous_tile
    
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
    def __init__(self, linked_map, set_map, points, allies, enemies, lives):
        self.linked_map = linked_map
        self.set_map = set_map
        self.points = points
        self.allies = allies
        self.enemies = enemies
        self.lives = lives
    
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
            c.execute("SELECT * FROM enemies WHERE name = 'Triangle'")
            triangle_data = c.fetchone()
            enemy = Enemy(triangle_data[0], triangle_data[1], triangle_data[2], location)
        elif type == 'square':
            c.execute("SELECT * FROM enemies WHERE name = 'Square'")
            square_data = c.fetchone()
            enemy = Enemy(square_data[0], square_data[1], square_data[2], location)
        elif type == 'circle':
            c.execute("SELECT * FROM enemies WHERE name = 'Circle'")
            circle_data = c.fetchone()
            enemy = Enemy(circle_data[0], circle_data[1], circle_data[2], location)

        print(enemy.location)
        self.enemies.append(enemy)
        # raise Exception('Please put some code in here. It would be much appreciated!')
        
    def spawn_ally(self, type, location):  # TODO: Numbers update with database
        if type == 'basic':
            c.execute("SELECT * FROM allies WHERE name = 'Basic'")
            basic_data = c.fetchone()
            ally = Ally(basic_data[0], basic_data[1], basic_data[2], basic_data[3], location)
        elif type == 'intermediate':
            c.execute("SELECT * FROM allies WHERE name = 'Intermediate'")
            intermediate_data = c.fetchone()
            ally = Ally(intermediate_data[0], intermediate_data[1], intermediate_data[2], intermediate_data[3], location)
        elif type == 'advanced':
            c.execute("SELECT * FROM allies WHERE name = 'Advanced'")
            advanced_data = c.fetchone()
            ally = Ally(advanced_data[0], advanced_data[1], advanced_data[2], advanced_data[3], location)
        
        self.allies.append(ally)
        # raise Exception('Please put some code in here. It would be much appreciated!')

def link_tiles(map, start_pos):
    path_tiles = {}
    
    current_type = map[start_pos[0]][start_pos[1]]
    current_pos = start_pos
    last_tile = None
    
    possible_iterations = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    while True:
        current_tile = Tile(current_type, current_pos)
        if last_tile is not None:
            current_tile.set_previous(last_tile)
            last_tile.set_next(current_tile)
        if current_type == 3:
            break
        path_tiles[current_pos] = current_tile
        # next_pos = # find the next pos by looking for a non-0 type that is not here and not last_pos
        for iteration in possible_iterations:
            iter_pos = (current_pos[0] + iteration[0], current_pos[1] + iteration[1])
            if iter_pos[0] < 0 or iter_pos[1] < 0 or iter_pos[0] > 7 or iter_pos[1] > 7:
                continue
            if map[iter_pos[0]][iter_pos[1]] != 0 and\
                (last_tile is None or (iter_pos[0], iter_pos[1]) != last_tile.location):
                next_pos = (current_pos[0] + iteration[0], current_pos[1] + iteration[1])
                break
        
        last_tile = current_tile
        current_pos = next_pos
        current_type = map[current_pos[0]][current_pos[1]]
    
    return path_tiles    
    

# def link_tiles(map):
#     path_tiles = {}
#     for row_index, row in enumerate(map):
#         for col_index, tile_type in enumerate(row):
#             if tile_type in (1, 2, 3):
#                 location = (row_index, col_index)
#                 new_tile = Tile(tile_type, location)
#                 path_tiles[location] = new_tile
#                 if (row_index, col_index - 1) in path_tiles:
#                     path_tiles[(row_index, col_index - 1)].set_next(new_tile)
#                     new_tile.set_previous(path_tiles[(row_index, col_index - 1)])
#                 if (row_index, col_index + 1) in path_tiles:
#                     path_tiles[(row_index, col_index + 1)].set_next(new_tile)
#                     new_tile.set_previous(path_tiles[(row_index, col_index + 1)])
#                 if (row_index - 1, col_index) in path_tiles:
#                     path_tiles[(row_index - 1, col_index)].set_next(new_tile)
#                     new_tile.set_previous(path_tiles[(row_index - 1, col_index)])
#                 if (row_index + 1, col_index) in path_tiles:
#                     path_tiles[(row_index + 1, col_index)].set_next(new_tile)
#                     new_tile.set_previous(path_tiles[(row_index + 1, col_index)])
    
#     return path_tiles

set_map = [
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 3],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0]
]

for row_index, row in enumerate(set_map):
    for tile_index, tile in enumerate(row):
        if tile == 2:
            start_pos = (row_index, tile_index)
            print(start_pos)
        elif tile == 3:
            end_pos = (row_index, tile_index)

linked_map = link_tiles(set_map, start_pos)
for loc,tile in linked_map.items():
    if tile is None:
        print("map loc", loc, "has none tile")
    else:
        print("map loc", loc, "has tile", tile.type, "next is", tile.next, "previous is", tile.previous)
    

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tower Defense')
FPS = 30

# clear_tables_data()
# create_database()
game = Game(linked_map, set_map, 9, [], [], 3)
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
    
    for enemy in game.enemies:
        speed = enemy.speed
        if frames % (speed * FPS) == 0:
            enemy.move(game)
            
    
    window.fill('#e3d9c4')
    for row in range(len(game.set_map)):
        for tile in range(len(game.set_map[row])):
            if game.set_map[row][tile] == 0:
                pygame.draw.rect(window, (0, 0, 0), (tile * 90, row * 90, 90, 90))
            elif game.set_map[row][tile] == 1:
                pygame.draw.rect(window, (0, 0, 255), (tile * 90, row * 90, 90, 90))
            elif game.set_map[row][tile] == 2:
                pygame.draw.rect(window, (0, 255, 0), (tile * 90, row * 90, 90, 90))
            elif game.set_map[row][tile] == 3:
                pygame.draw.rect(window, (255, 0, 0), (tile * 90, row * 90, 90, 90))
    shop.draw(game)
    
    pygame.display.update()
    
    frames += 1

pygame.quit()
