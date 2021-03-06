import pygame
from pygame.locals import *
clock = pygame.time.Clock()

class Block():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        self.rect = pygame.rect.Rect((self.x, self.y, width, height))

    def draw(self, surface):
        pygame.draw.rect(screen, (55,150,55), self.rect)

        self.x = self.rect.left 
        self.y = self.rect.top

    def move(self, vect):
        x = vect[0] - self.rect.left
        y = vect[1] - self.rect.top

        self.rect.move_ip(x, y)
size = 800,600
block = Block(100, 100, 50, 50)
screen = pygame.display.set_mode(size)
def gameloop():

    loopExit = True

    while loopExit == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loopExit = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    block.move([5,0])

            if event.type == pygame.MOUSEBUTTONUP:
                block.move(pygame.mouse.get_pos())

        screen.fill((25,25,25))

        block.draw(screen)

        clock.tick(60)

        pygame.display.flip()

gameloop()