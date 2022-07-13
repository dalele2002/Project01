import pygame

# game board
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('plane battle game')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
