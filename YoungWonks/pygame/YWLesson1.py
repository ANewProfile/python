import pygame
pygame.init()

WIDTH = 1080
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Square:
    def __init__(self, length, color, position, up=False, down=False, left=False, right=False):
        self.length = length
        self.color = color
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.set_position(position)

    def set_position(self, position):
        self.position = list(position)
        self.top_left = position
        self.top_right = (position[0]+self.length, position[1])
        self.bottom_left = (position[0], position[1]+self.length)
        self.bottom_right = (position[0]+self.length, position[1]+self.length)
    
    def point_in_square(self, point):
        if point[0] in range(self.position[0], self.position[0]+self.length+1) and \
           point[1] in range(self.position[1], self.position[1]+self.length+1):
            # print('Collision!')
            return True
        # print('No collision!')
        return False

    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], self.length, self.length))
    
    def check_collision_square(self, other):
        for point in (other.top_left, other.top_right, other.bottom_left, other.bottom_right):
            # print("is", point, "in", self.position)
            if self.point_in_square(point):
                if True in (other.up, other.down, other.left, other.right):
                    print("Moving collision between user", other.position, "and", self.position)
                if other.up is True:
                    return other.position[0], self.bottom_left[1]
                elif other.down is True:
                    return other.position[0], self.top_left[1]
                if other.left is True:
                    return self.bottom_right[0], other.position[1]
                elif other.right is True:
                    return self.bottom_left[0], other.position[1]
                
        for point in (self.top_left, self.top_right, self.bottom_left, self.bottom_right):
            # print("is", point, "in", self.position)
            if other.point_in_square(point):
                if True in (other.up, other.down, other.left, other.right):
                    print("Moving collision between user", other.position, "and", self.position)
                if other.up is True:
                    return other.position[0], self.bottom_left[1]
                elif other.down is True:
                    return other.position[0], self.top_left[1]
                if other.left is True:
                    return self.bottom_right[0], other.position[1]
                elif other.right is True:
                    return self.bottom_left[0], other.position[1]
        
        return other.position


x = 524
y = 344

user = Square(32, WHITE, (x, y))
collision1 = Square(50, RED, [492, 538])
collision2 = Square(25, RED, [238, 375])
collision3 = Square(40, RED, [846, 192])
collisions = (collision1, collision2, collision3)
# print("obstacles", [c.position for c in collisions])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                if event.key == pygame.K_w:
                    user.up = True
                elif event.key == pygame.K_a:
                    user.left = True
                elif event.key == pygame.K_s:
                    user.down = True
                elif event.key == pygame.K_d:
                    user.right = True
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                if event.key == pygame.K_w:
                    user.up = False
                elif event.key == pygame.K_a:
                    user.left = False
                elif event.key == pygame.K_s:
                    user.down = False
                elif event.key == pygame.K_d:
                    user.right = False

    if user.up is True:
        y -= 1
    if user.left is True:
        x -= 1
    if user.right is True:
        x += 1
    if user.down is True:
        y += 1

    if x > 1048:
        x = 1048
    elif x < 0:
        x = 0
    
    if y > 688:
        y = 688
    elif y < 0:
        y = 0

    window.fill(BLACK)
    user.set_position((x, y))
    for collision in collisions:
        x, y = collision.check_collision_square(user)
        collision.draw()
        user.set_position((x, y))
        user.draw()

    pygame.display.update()


pygame.quit()