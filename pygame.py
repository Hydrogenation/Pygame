import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

#define colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#initialize pygame and create our window
pygame.init()
pygame.mixer.init() #enables sound
screen = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Hydrogenation")
clock = pygame.time.Clock()

#Game Loop
running = True
while running:
    #keep your loop running at the right speed
    clock.tick(FPS)
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #update
    #draw/render
    screen.fill(BLACK)
    #after drawing everything, flip the display
    pygame.display.flip()
pygame.quit()
