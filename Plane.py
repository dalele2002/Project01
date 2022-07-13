import pygame
import random

# game board
pygame.init()
screen = pygame.display.set_mode((797, 600))
pygame.display.set_caption('plane battle game')
icon = pygame.image.load('R.png')
pygame.display.set_icon(icon)
bgImg = pygame.image.load('battle_plane.jpg')

# player
playerImg = pygame.image.load('player_2.png')
playerX = 365
playerY = 520
playerStep = 0

# enemy
number_of_enemies = 6


class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.x = random.randint(30, 700)
        self.y = random.randint(30, 200)
        self.step = random.uniform(0.03, 0.1)


enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())


# enemy movement
def show_enemy():
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if (e.x > 732 or e.x < 0):
            e.y += 20
            e.step *= -1


# player movement range
def move_player():
    global playerX
    global playerStep
    playerX += playerStep
    if playerX > 732:
        playerX = 732
    if playerX < 1:
        playerX = 1


# game loop(显示游戏画面)
running = True
while running:
    screen.blit(bgImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # player keyboard manipulation(键盘操作)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStep = 0.1
            elif event.key == pygame.K_LEFT:
                playerStep = -0.1
        if event.type == pygame.KEYUP:
            playerStep = 0
    screen.blit(playerImg, (playerX, playerY))

show_enemy()
move_player()
pygame.display.update()
