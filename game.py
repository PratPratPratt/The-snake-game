import pygame
import random 
pygame.init()

# display setup

width, height = 500, 500
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snakey-Wakey")
blockie = 50

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
FRUIT_GREEN = (4, 232, 36)
MARRON = (185, 49, 79)
# images
bg = pygame.image.load("grid.png")

#game variables
direction = ""

#functions
def spawn(array, color):
    if ((array[0]<10) and (array[1]<10)):
        array[0] -= 1
        array[1] -= 1
        array[0] *= 50
        array[1] *= 50

    pygame.draw.rect(WIN, color, (array[0], array[1], blockie, blockie))

def comparer(a1,a2):
    if (((a1[0] < 1) or (a1[0] > 10)) or ((a1[1] < 1) or (a1[1] > 10))):
        run = False 
    a1[0] *= 50
    a1[1] *= 50
    a2[0] *= 50
    a2[1] *= 50
    if (a1[0] % a2[0]<50) and (a1[1] % a2[1] < 50):
        return True

# snake
snake_start = random.sample(range(1, 10), 2)
snake = [snake_start]

#fruit
fruit = random.sample(range(1,10), 2)
print (fruit)

# game loop setup
FPS = 60
clock = pygame.time.Clock()
run = True
 
# game loop
while run :
    clock.tick(FPS)
    WIN.blit(bg, (0, 0))
    spawn(fruit, MARRON)
    for i in snake:
        spawn(i, FRUIT_GREEN)
        if comparer(i, fruit):
            fruit = random.sample(range(1,10), 2)            
        if direction == "UP":
            i[1] -= 1
        if direction=="DOWN":
            i[1] +=1
        if direction=="LEFT":
            i[0] -=1
        if direction=="RIGHT":
            i[0] += 1 
        """ 
        if ((i[0] > 10) or (i[0]<1)):
            run = False
        if ((i[1] > 10) or (i[1]<1)):
            run = False 
        """
    pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if ((event.key ==  pygame.K_LEFT) and (not(direction=="RIGHT"))):
                direction = "LEFT"
            if ((event.key == pygame.K_RIGHT) and (not(direction=="LEFT"))):
                direction = "RIGHT"
            if ((event.key == pygame.K_DOWN) and (not(direction=="UP"))):
                direction = "DOWN"
            if ((event.key == pygame.K_UP)) and (not(direction=="DOWN")):
                direction = "UP"
            
    

pygame.quit()  