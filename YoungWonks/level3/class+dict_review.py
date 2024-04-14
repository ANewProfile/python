class Superhero:
    def __init__(self):
        self.health = 100
        self.stamina = 50
    
    def attack(self, target, damage):
        target.health -= damage
        self.stamina -= 5
    
    def heal(self, health):
        self.health += health
        self.stamina -= 2


class Spiderman(Superhero):
    def __init__(self):
        super().__init__()
    
    def climb_wall(self):
        print('I\'m cool')
        self.stamina -= 10
    
    def attack(self, target, damage):
        target.health -= damage
        self.stamina -= 5
        print('Wachow!')

player1 = Superhero()
player2 = Spiderman()

print(player1.health, player1.stamina)
print(player2.health, player2.stamina)

player1.attack(player2, 10)

print(player1.health, player1.stamina)
print(player2.health, player2.stamina)
