# https://wiki.python.org/moin/TimeComplexity
# https://stackoverflow.com/questions/1601151/how-do-i-check-in-sqlite-whether-a-table-exists

# CREATING SAVE FOR CONTINUING GAMES
# ALLIES NOT SPAWNING
# ENEMIES NOT SPAWNING
# AROUND LINE 400
import sqlite3
import pygame
pygame.init()
import time
from math import dist
from random import choice


conn = sqlite3.connect('TowerDefense.db')
c = conn.cursor()

def create_database():
    c.execute("CREATE TABLE IF NOT EXISTS allies (name TEXT, power INTEGER, range INTEGER, cost INTEGER, sell INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS enemies (name TEXT, health INTEGER, speed REAL, points INTEGER)")
    # c.execute("CREATE TABLE IF NOT EXISTS linkedMap (x INTEGER, y INTEGER, prevx INTEGER, prevy INTEGER, nextx INTEGER, nexty INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS setMap (row INTEGER, column INTEGER, type INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS availLocs (x INTEGER, y INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS points (value INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS saveAllies (x INTEGER, y INTEGER, type TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS saveEnemies (x INTEGER, y INTEGER, health INTEGER, type TEXT)")
    
    c.execute("INSERT INTO allies VALUES ('Basic', 1, 3, 2, 1)")
    c.execute("INSERT INTO allies VALUES ('Intermediate', 3, 4, 5, 3)")
    c.execute("INSERT INTO allies VALUES ('Advanced', 6, 6, 10, 5)")
    
    c.execute("INSERT INTO enemies VALUES ('Triangle', 8, 1, 1)")
    c.execute("INSERT INTO enemies VALUES ('Square', 14, 1.5, 3)")
    c.execute("INSERT INTO enemies VALUES ('Circle', 20, 1, 7)")
    
    conn.commit()

def clear_tables_data():
    c.execute("DELETE FROM allies")
    c.execute("DELETE FROM enemies")
    conn.commit()

# clear_tables_data()
# create_database()


def get_text(msg, size, color):
    fontobj = pygame.font.SysFont('freesans', size)
    return fontobj.render(msg, False, color)

c.execute("SELECT * FROM allies WHERE name = 'Basic'")
basic_data = c.fetchone()

c.execute("SELECT * FROM allies WHERE name = 'Intermediate'")
intermediate_data = c.fetchone()

c.execute("SELECT * FROM allies WHERE name = 'Advanced'")
advanced_data = c.fetchone()

c.execute("SELECT * FROM enemies WHERE name = 'Triangle'")
triangle_data = c.fetchone()

c.execute("SELECT * FROM enemies WHERE name = 'Square'")
square_data = c.fetchone()

c.execute("SELECT * FROM enemies WHERE name = 'Circle'")
circle_data = c.fetchone()

def create_save(game):
    # c.execute("DELETE FROM linkedMap")
    c.execute("DELETE FROM setMap")
    c.execute("DELETE FROM availLocs")
    c.execute("DELETE FROM points")
    c.execute("DELETE FROM saveAllies")
    c.execute("DELETE FROM saveEnemies")
    
    # slinked_map: dict = game.linked_map
    sset_map: list = game.set_map
    savail_locs: list = game.avail_locs
    spoints: int = game.points
    sallies: list = game.allies
    senemies: list = game.enemies
    
    # for loc, tile_class in slinked_map.items():
    #     c.execute("INSERT INTO linkedMap VALUES (?, ?, ?, ?, ?, ?)", (loc[0], loc[1], tile_class.previous.location[0], tile_class.previous.location[1], tile_class.next.location[0], tile_class.next.location[1]))
    
    for row_index, row in enumerate(sset_map):
        for tile_index, tile in enumerate(row):
            c.execute("INSERT INTO setMap VALUES (?, ?, ?)", (tile_index, row_index, tile))
    
    for loc in savail_locs:
        c.execute("INSERT INTO availLocs VALUES (?, ?)", (loc[0], loc[1]))
    
    c.execute("INSERT INTO points VALUES (?)", (spoints,))
    
    for ally in sallies:
        if ally.power == basic_data[1]:
            type = 'basic'
        else:
            type = 'intermediate' if ally.power == intermediate_data[1] else 'advanced'
        c.execute("INSERT INTO saveAllies VALUES (?, ?, ?)", (ally.location[0], ally.location[1], type))
    
    for enemy in senemies:
        if enemy.points == triangle_data[1]:
            type = 'triangle'
        else:
            type = 'circle' if enemy.points == circle_data[1] else 'square'
        c.execute("INSERT INTO saveEnemies VALUES (?, ?, ?, ?)", (enemy.location[0], enemy.location[1], enemy.health, type))
        
    conn.commit()
    # linked_map, set_map, avail_locs, points, allies, enemies


class Ally:
    def __init__(self, power, range, cost, sell, location, attack_pattern = 1):
        self.power = power
        self.range = range
        self.cost = cost
        self.sell = sell
        self.location = location
        self.attack_pattern = attack_pattern
    
    def get_target(self, avail_enemies):
        num_avail_enemies = len(avail_enemies)
        if num_avail_enemies == 1:
            return avail_enemies[0]
        elif num_avail_enemies == 0:
            return None
        else:
            if self.attack_pattern == 1:  # O(n)
                closest_enemy = None
                for enemy in avail_enemies:
                    if closest_enemy:
                        if dist(self.location, enemy.location) < dist(self.location, closest_enemy.location):
                            closest_enemy = enemy
                    else:
                        closest_enemy = enemy
                return closest_enemy
            elif self.attack_pattern == 2:  # O(n)
                farthest_enemy = None
                for enemy in avail_enemies:
                    if farthest_enemy:
                        if dist(self.location, enemy.location) > dist(self.location, farthest_enemy.location):
                            farthest_enemy = enemy
                    else:
                        farthest_enemy = enemy
                return farthest_enemy
            elif self.attack_pattern == 3:  # O(1)
                return choice(avail_enemies)
            elif self.attack_pattern == 4:  # O(n)
                most_hp = None
                for enemy in avail_enemies:
                    if most_hp:
                        if enemy.health > most_hp.health:
                            most_hp = enemy
                    else:
                        most_hp = enemy
                return most_hp
            elif self.attack_pattern == 5:  # O(n)
                least_hp = None
                for enemy in avail_enemies:
                    if least_hp:
                        if enemy.health < least_hp.health:
                            least_hp = enemy
                    else:
                        least_hp = enemy
                return least_hp
    
    def attack(self, enemy):
        enemy.take_damage(self.power)
    
    def draw(self, type):
        if type == 'Basic':
            pygame.draw.rect(window, (0, 255, 0), ((self.location[1]*90)+20, (self.location[0]*90)+10, 50, 70))
        elif type == 'Intermediate':
            pygame.draw.rect(window, (0, 0, 255), ((self.location[1]*90)+20, (self.location[0]*90)+10, 50, 70))
        elif type == 'Advanced':
            pygame.draw.rect(window, (255, 0, 0), ((self.location[1]*90)+20, (self.location[0]*90)+10, 50, 70))

        # pygame.draw.rect(window, '#ff690a', ((self.location[1]*90)+10, (self.location[0]*90)+10, 70, 70))
        # self.location[0] is the y axis
        
class Enemy:
    def __init__(self, health, speed, points, location):
        self.health = health
        self.speed = speed
        self.points = points
        self.location = location

    def move(self, game):
        # print("location is",self.location[0],self.location[1])
        current_tile = game.linked_map[(self.location[0], self.location[1])]
        # print("current tile", current_tile.type)
        next_tile = game.linked_map[(self.location[0], self.location[1])].next
        # print(next_tile.location)
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

    def draw(self):
        pygame.draw.rect(window, (255, 255, 255), ((self.location[1]*90)+10, (self.location[0]*90)+10, 70, 70))

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
        # print(self.allies)
        self.basic = pygame.Rect(750, 50, 30, 70)
        self.intermediate = pygame.Rect(820, 50, 30, 70)
        self.advanced = pygame.Rect(890, 50, 30, 70)
    
    def draw(self, game):
        balance = get_text(f'Balance: {game.points} points', 30, (0, 0, 0))
        window.blit(balance, (750, 10))
        for ally in self.allies:
            if game.points >= ally[3]:
                if ally[0] == 'Basic':
                    pygame.draw.rect(window, (0, 255, 0), self.basic)
                elif ally[0] == 'Intermediate':
                    pygame.draw.rect(window, (0, 0, 255), self.intermediate)
                elif ally[0] == 'Advanced':
                    pygame.draw.rect(window, (255, 0, 0), self.advanced)
            elif game.points <= ally[3]:
                if ally[0] == 'Basic':
                    pygame.draw.rect(window, (0, 255, 0), self.basic, width=3)
                elif ally[0] == 'Intermediate':
                    pygame.draw.rect(window, (0, 0, 255), self.intermediate, width=3)
                elif ally[0] == 'Advanced':
                    pygame.draw.rect(window, (255, 0, 0), self.advanced, width=3)

class Game:
    def __init__(self, linked_map, set_map, avail_locs, points, allies=[], enemies=[], occupied_locs=[]):
        self.linked_map = linked_map
        self.set_map = set_map
        self.avail_locs = avail_locs
        self.occupied_locs = occupied_locs
        self.points = points
        self.allies = allies
        self.enemies = enemies
    
    def deposit(self, amount):
        self.points += amount
    
    def buy(self, ally):
        if self.points >= ally.cost:
            self.allies.append(ally)
            self.spawn_ally(ally, ally.location)
            self.points -= ally.cost
            self.avail_locs.remove(ally.location)
            self.occupied_locs.append(ally.location)
        else:
            print(self.points, ally.cost)
            raise Exception('Not enough money. PLEASE ADD SOMETHING TO THIS LINE THAT MAKES THIS LOOK BETTER THAN AN ERROR')
    
    def spawn_enemy(self, type, location):
        if type == 'triangle':
            enemy = Enemy(triangle_data[1], triangle_data[2], triangle_data[3], location)
        elif type == 'square':
            enemy = Enemy(square_data[1], square_data[2], square_data[3], location)
        elif type == 'circle':
            enemy = Enemy(circle_data[1], circle_data[2], circle_data[3], location)

        # print(enemy.location)
        self.enemies.append(enemy)
        # raise Exception('Please put some code in here. It would be much appreciated!')
        
    def spawn_ally(self, ally, location):
        # print('ally type', type)
        # if type == 'Basic':
        #     ally = Ally(basic_data[1], basic_data[2], basic_data[3], basic_data[4], location)
        # elif type == 'Intermediate':
        #     ally = Ally(intermediate_data[1], intermediate_data[2], intermediate_data[3], intermediate_data[4], location)
        # elif type == 'Advanced':
        #     ally = Ally(advanced_data[1], advanced_data[2], advanced_data[3], advanced_data[4], location)
        
        self.allies.append(ally)
        # raise Exception('Please put some code in here. It would be much appreciated!')

    def sell_ally(self, ally):
        self.deposit(ally.sell)
        self.allies.remove(ally)
        self.occupied_locs.remove(ally.location)
        self.avail_locs.append(ally.location)

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


c.execute("SELECT * FROM setMap")
set_map_data = c.fetchall()
print(set_map_data)
# ((x INTEGER, y INTEGER, type INTEGER), ...)

c.execute("SELECT * FROM availLocs")
avail_locs_data = c.fetchall()

c.execute("SELECT * FROM points")
points = c.fetchone() or 9

c.execute("SELECT * FROM saveAllies")
allies_data = c.fetchall()

c.execute("SELECT * FROM saveEnemies")
enemies_data = c.fetchall()

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

if set_map_data:
    set_map = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
                ]
    for data in set_map_data:
        print(data)
        set_map[data[1]][data[0]] = data[2]
    print(set_map)


avail_locs = []
for row_index, row in enumerate(set_map):
    for tile_index, tile in enumerate(row):
        # print(f'location ({tile_index}, {row_index}) is type {tile}')
        if tile == 0:
            print(f'appending ({tile_index}, {row_index}) to avail_locs')
            avail_locs.append((row_index, tile_index))
        else:
            print(f'({tile_index}, {row_index}) not appended because it is type {tile}')

        if tile == 2:
            start_pos = (row_index, tile_index)
            # print(start_pos)
        elif tile == 3:
            end_pos = (row_index, tile_index)

linked_map = link_tiles(set_map, start_pos)
# print(avail_locs)
# for loc,tile in linked_map.items():
#     if tile is None:
#         print("map loc", loc, "has none tile")
#     else:
#         print("map loc", loc, "has tile", tile.type, "next is", tile.next, "previous is", tile.previous)

allies = []
for ally_data in allies_data:
    if ally_data[2] == "Basic":
        allies.append(Ally(basic_data[1], basic_data[2], basic_data[3], basic_data[4], (ally_data[0], ally_data[1])))
    if ally_data[2] == "Intermediate":
        allies.append(Ally(intermediate_data[1], intermediate_data[2], intermediate_data[3], intermediate_data[4], (ally_data[0], ally_data[1])))
    if ally_data[2] == "Advanced":
        allies.append(Ally(advanced_data[1], advanced_data[2], advanced_data[3], advanced_data[4], (ally_data[0], ally_data[1])))
        
enemies = []
for enemy_data in enemies_data:
    if enemy_data[3] == "Triangle":
        enemies.append(Enemy(enemy_data[2], triangle_data[2], triangle_data[3], (enemy_data[0], enemy_data[1])))
    if enemy_data[3] == "Square":
        enemies.append(Enemy(enemy_data[2], square_data[2], square_data[3], (enemy_data[0], enemy_data[1])))
    if enemy_data[3] == "Circle":
        enemies.append(Enemy(enemy_data[2], circle_data[2], circle_data[3], (enemy_data[0], enemy_data[1])))
    

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tower Defense')
FPS = 20

game = Game(linked_map, set_map, avail_locs, points[0], allies, enemies, [ally.location for ally in allies])
shop = Shop()

next_enemy = 1
spawn_enemy = False
spawning_ally = (False, None)
attack_cycle = False

clock = pygame.time.Clock()
frames = 0
running = True
start_time = time.time()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            create_save(game)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spawn_enemy = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button = event.button
            mouse_pos = event.pos
            if button == 1:
                if shop.basic.collidepoint(mouse_pos):
                    spawning_ally = (True, 'Basic')
                    # game.buy(Ally(basic_data[1], basic_data[2], basic_data[3], basic_data[4], location))
                    # print("basic")
                elif shop.intermediate.collidepoint(mouse_pos):
                    spawning_ally = (True, 'Intermediate')
                    # game.buy(Ally(intermediate_data[1], intermediate_data[2], intermediate_data[3], intermediate_data[4], location))
                    # print("intermediate")
                elif shop.advanced.collidepoint(mouse_pos):
                    spawning_ally = (True, 'Advanced')
                    # game.buy(Ally(advanced_data[1], advanced_data[2], advanced_data[3], advanced_data[4], location))
                    # print("advanced")
                else:
                    if spawning_ally[0]:
                        # print('spawning ally')
                        ally_type = spawning_ally[1]
                        if mouse_pos[0] < 720:
                            loc_x = mouse_pos[0] // 90
                            loc_y = mouse_pos[1] // 90
                            location = (loc_y, loc_x)
                            if spawning_ally[0] and location in game.avail_locs:
                                if ally_type == 'Basic':
                                    game.buy(Ally(basic_data[1], basic_data[2], basic_data[3], basic_data[4], location))
                                elif ally_type == 'Intermediate':
                                    game.buy(Ally(intermediate_data[1], intermediate_data[2], intermediate_data[3], intermediate_data[4], location))
                                elif ally_type == 'Advanced':
                                    game.buy(Ally(advanced_data[1], advanced_data[2], advanced_data[3], advanced_data[4], location))
                            elif location not in game.avail_locs:
                                print(f'{location} not in avail_locs')
                                # print('avail locs:', game.avail_locs)
                        
                        spawning_ally = (False, None)
            elif button == 3:
                if mouse_pos[0] < 720:
                    loc_x = mouse_pos[0] // 90
                    loc_y = mouse_pos[1] // 90
                    location = (loc_y, loc_x)
                    if location in game.occupied_locs:
                        for ally in game.allies:
                            if ally.location == location:
                                game.sell_ally(ally)
                    
            
    
    if (time.time() - start_time) >= 2:
        spawn_enemy = True
        start_time = time.time()
        attack_cycle = True
    
    for enemy in game.enemies:
        if enemy.health <= 0:
            game.enemies.remove(enemy)
            game.deposit(enemy.points)
        else:
            speed = enemy.speed
            if frames % (speed * FPS) == 0:
                enemy.move(game)
    
    if spawn_enemy:
        if next_enemy // 7 == 0:
            game.spawn_enemy('triangle', start_pos)
        elif next_enemy // 10 == 1:
            game.spawn_enemy('square', start_pos)
        else:
            game.spawn_enemy('circle', start_pos)
        
        spawn_enemy = False
        next_enemy += 1
    
    if attack_cycle:
        for ally in game.allies:  # total time complexity: O(n^2)
            avail_enemies = [enemy for enemy in game.enemies if dist(ally.location, enemy.location) <= ally.range]
            target = ally.get_target(avail_enemies)
            if target:
                ally.attack(target)
        attack_cycle = False
            
    
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
    
    for enemy in game.enemies:
        enemy.draw()
    
    for ally in game.allies:
        if ally.power == basic_data[1]:
            ally.draw('Basic')
        elif ally.power == intermediate_data[1]:
            ally.draw('Intermediate')
        elif ally.power == advanced_data[1]:
            ally.draw('Advanced')
    
    pygame.display.update()
    
    frames += 1

pygame.quit()
