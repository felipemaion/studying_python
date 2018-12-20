import sys, pygame, time
from pygame.locals import *
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
background_color = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            ballrect.move(pygame.mouse.get_pos())
    ballrect = ballrect.move(speed)
    time.sleep(0.001) # not so fast!!!
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background_color)
    screen.blit(ball, ballrect)
    pygame.display.flip()