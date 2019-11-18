import pygame
import sys
from random import choice
from pygame.locals import *


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)
PURPLE = (100, 0, 255)
WHITE = (255, 255, 255)

def get_words():
    f = open("words.txt")
    words = []
    line = f.readline()
    while line:
        words.append(line.strip())
        line = f.readline()
    return words

def draw_gallows(screen):
    pygame.draw.rect(screen, PURPLE, (450, 350, 100, 10)) #bottom
    pygame.draw.rect(screen, PURPLE, (495, 250, 10, 100)) #support
    pygame.draw.rect(screen, PURPLE, (450, 250, 50, 10)) #crossbar
    pygame.draw.rect(screen, PURPLE, (450, 250, 10, 25)) #noose

def draw_man(screen, body_part):
    if body_part == "head":
        pygame.draw.circle(screen, RED, (455, 270), 10) #head
    if body_part == "body":
        pygame.draw.line(screen, RED, (455, 280), (455, 320), 3) #body
    if body_part == "l_arm":
        pygame.draw.line(screen, RED, (455, 300),(455, 285), 3)  #arm
    if body_part == "r_arm":
        pygame.draw.line(screen, RED, (455, 300), (465, 285), 3)  #arm
    if body_part == "l_leg":
        pygame.draw.line(screen, RED, (455, 320), (455, 330), 3)  #leg
    if body_part == "r_leg":
        pygame.draw.line(screen, RED, (455, 320), (465, 330), 3)  #leg

def draw_word_spaces(screen, spaces):
    x = 10
    for i in range(spaces):
        pygame.draw.line(screen, YELLOW, (x, 350), (x+20, 350), 3)
        x += 30

def draw_letter(screen, font, word, guess):
    x = 10
    for letter in word:
        if letter == guess:
            letter == font.render(letter,3 , WHITE)
            screen.blit(letter, (x,300))
        x += 30

def get_unique_letters(word):
    unique = ""
    for letter in word:
        if letter not in unique:
            unique += letter
    return unique

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    font = pygame.font.SysFont("monospace", 30)
    draw_gallows(screen)
    words = get_words()
    word = choice(words)

    print(word)


    draw_word_spaces(screen, len(word))
    pygame.display.update()

    body = ["r_leg", "l_leg", "r_arm", "l_arm", "body", "head"]

    correct = ''
    guessed = ''
    unique = get_unique_letter(word)

    while body and len(correct) < len(unique):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.type.unicode.isalpha():
                    guess = event.unicode
                    if guess in word and guess not in correct:
                        draw_letter(screen, font, word, guess)
                        pygame.display.update()
                        correct += guess
                    elif guess not in guessed:
                        body_part = body.pop()
                        draw_man(screen, body_part)
                        pygame.display.update()
                        guessed += guess
    if body:
        text = "You won!"
    else:
        text = "Sorry, the word was " + word

    end_message = font.render(text, 3, WHITE)
    screen.blit(end_message,(0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == "__main__": main()