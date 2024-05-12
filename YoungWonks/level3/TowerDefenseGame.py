import sqlite3


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
        # enemy = Enemy
        # self.enemies.append(enemy)
        raise Exception('Please put some code in here. It would be much appreciated!')
        
    def spawn_ally(self, location, ally):
        raise Exception('Please put some code in here. It would be much appreciated!')
