#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from random import randint, choice

SCREENSIZE = WIDTH, HEIGHT = (500, 400)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLOR1 = (185, 122, 87)
COLOR2 = (106, 42, 11) #(136, 0, 21)
COLOR3 = (127, 127, 127)

pygame.font.init()

screen = None

label_font = pygame.font.Font(None, 35)
text_font = pygame.font.SysFont("Verdana", 15)
game_over_font = pygame.font.SysFont("Verdana", 15, "bold")

king_font = pygame.font.SysFont("Verdana", 10)
king_text = king_font.render("king", True, COLOR1)

class Piece(object):
    """ The droughts 'piece' object itself"""

    def __init__(self, board, addr, name, color):
        self.board = board
        self.x, self.y = addr
        self.color = color
        self.name = name
        self.isKing = False # is this piece a 'King'?

    def draw(self): # called to draw this piece on the board
        """ Draws this piece on the board """
        
        pygame.draw.circle(screen, self.color, (self.x, self.y), 23)
        if self.isKing:
            screen.blit(king_text, (self.x-12, self.y-8))

    def update(self): # called to update this piece's position
        """ Update the position of this piece """
        
        if self.name == "white" and self.y == 25: self.crowned()
        elif self.name == "black" and self.y >= 350: self.crowned()
        self.draw()

    def move(self, playerMoves):
        """ Moves the piece to a new position """
        
        old, new, piece = playerMoves
        self.board.removePiece((self.x, self.y)) # remove the 'Piece' object
        addr = self.x-25, self.y-25
        empty = Empty(addr)
        self.board.addPiece(empty) # replace it with the 'Empty' object

        # see if player can eat
        obj = self.board.getPiece((new[0], new[1]))
        try:
            if obj.ready: # player will eat
                if piece.name == "white":
                    self.board.game.score += 5 # increase score with Five points

                direction, heading = old
                x, y = new[0], new[1]

                info = {"left":"right", "right": "left", "north": "south", "south": "north"}

                def check(direction, heading, x, y):

                    if direction == "left": x = x+25-50
                    elif direction == "right": x = x+25+50
                    if heading == "north": y = y+25-50
                    elif heading == "south": y = y+25+50

                    piece = self.board.getPiece((x, y))
                    piece.eaten()

                    if direction == "left": x = x-25-50
                    elif direction == "right": x = x-25+50
                    if heading == "north": y = y-25-50
                    elif heading == "south": y = y-25+50

                    check(direction, heading, x, y)

                check(info[direction], info[heading], x, y)
                
                print(piece.name, "eats")
        except:
            print("error getting ready!")
        
        self.board.removePiece((new[0], new[1])) # remove the 'Empty' object
        self.x, self.y = new[0]+25, new[1]+25
        self.board.addPiece(self) # replace it with the 'Piece' object

        if piece.name == "white":
            self.board.game.player = "computer" # switch players

    def getRandomID(self, ids):
        """ Creates and return a randomly-generated number used an an ID for moves """
        
        while True:
            num = randint(1, 1000)
            if num not in ids:
                ids.append(num)
                return num

    def getPossibleMoves(self): # called to get possible positions this piece can go
        """ Calculates and return possible positions this piece can go """
        
        moves = {}

        ids = []

        for piece in self.board.pieces.values():
            if piece.name == "empty":
                piece.glow = False
                piece.ready = False

        self.piece = self

        def check(direction="left", heading="north", x=None, y=None):
            piece = self.piece
            if direction == "left": x -= 50
            else: x += 50

            if heading == "north": y -= 50
            else: y += 50

            if (x, y) in self.board.pieces: # position is empty
                empty = self.board.getPiece((x, y))
                empty.glow = True
                old, new, obj = (direction, heading), (x, y), piece
                identity = self.getRandomID(ids) # get an ID for the move
                moves[identity] = old, new, obj

                if piece.isKing: # piece is a king, so go on
                    check(direction, heading, x, y)
            else: # its not empty, so check if its comrade
                x1, y1 = x+25, y+25
                piece2 = self.board.getPiece((x1, y1))
                try:
                    if piece.isComrade(piece2):# piece is comrade so return
                        return
                    else: # piece is not comrade, so check empty
                        if direction == "left": x2 = x1-25-50
                        else: x2 = x1-25+50

                        if heading == "north": y2 = y1-25-50
                        else: y2 = y1-25+50

                        if (x2, y2) in self.board.pieces: # its empty, so notify player
                            empty = self.board.getPiece((x2, y2))
                            empty.glow = True
                            empty.ready = True

                            old, new, obj = (direction, heading), (x2, y2), piece2
                            identity = self.getRandomID(ids)
                            moves[identity] = old, new, obj

                            check(direction, heading, piece2.x-25, piece2.y-25)
                            check(direction, heading, x2, y2)
                            
                            # check empty or comrade again
                            if direction == "left": x3 = x2-50
                            else: x3 = x2+50

                            if heading == "north": y3 = y2-50
                            else: y3 = y2+50

                            if (x3, y3) in self.board.pieces: # positon(address) is empty
                                return
                            else: # there is a piece, so check if comrade, stop, if not comrade continue
                                x3+=25
                                y3+= 25

                                piece3 = self.board.getPiece((x3, y3))
                                if piece3.isComrade(piece2): # comrades, so stop
                                    return
                                else: # not comrades, so continue
                                    self.piece = piece3
                                    check(direction, heading, x, y)

                            #self.piece = piece2
                            
                            #check(direction, heading, x2, y2) # keep searching
                        else: # its not empty, so return
                            return
                except:
                    pass

        if self.piece.name == "white": direction = "north"
        else: direction = "south"
                    
        check("left", direction, self.piece.x-25, self.piece.y-25)
        check("right", direction, self.piece.x-25, self.piece.y-25)
        
        if self.piece.isKing:
            if self.piece.name == "white": heading = "south"
            else: heading = "north"
            
            check("left", heading, self.piece.x-25, self.piece.y-25)
            check("right", heading, self.piece.x-25, self.piece.y-25)

        if self.piece.name == "white":
            eatMoves =  self.board.game.thinkEatMoves(moves, "person")
            if eatMoves is not None:
                return eatMoves

        return moves

    def isComrade(self, other): # are the pieces comrades ?
        """ Checks if the piece is a comrade with the other piece, by comparinng their names """
        
        if self.name == other.name: 
            return True
        else:
            return False

    def crowned(self): # called when this piece has become a 'King'
        """ Makes this piece become 'King', not an ordinary piece """
        
        self.isKing = True

    def eaten(self): # called when this piece has been 'eaten'
        """ Destroys this piece and is no longer available to the game """
        
        self.board.removePiece((self.x, self.y)) # remove the 'Piece' object
        addr = self.x-25, self.y-25
        empty = Empty(addr)
        self.board.addPiece(empty) # replace it with the 'Empty' object

class Empty(object):
    """ Used to hold an 'empty' position(address) on the board """

    def __init__(self, addr):
        self.x, self.y = addr
        self.name = "empty"
        self.glow = False # when true, this piece glows green on the board - showing that a piece may move there
        self.ready = False # when true, this piece glows a small red circle - showing that a piece may move there to
        # eat the opponent piece

    def draw(self):
        pygame.draw.rect(screen, GREEN, Rect(self.x, self.y, 50, 50))

    def drawReady(self):
        pygame.draw.circle(screen, RED, (self.x+25, self.y+25), 15)

    def update(self):
        if self.glow:
            self.draw()
        if self.ready:
            self.drawReady()
            
class Board(object):
    """ The droughts board itself """

    def __init__(self, game):
        self.game = game
        self.pieces = dict()
        self.piecesDrawn = False
        
    def drawBoard(self):
        """ Draws the droughts board """
        
        for i in range(8):
            for j in range(8):
                if (i %2 == 0 and j % 2 == 0) or (i % 2 !=0 and j % 2 != 0):
                    COLOR = COLOR1
                else: COLOR = COLOR2
                pygame.draw.rect(screen, COLOR, Rect(i*50, j*50, 50, 50))

        self.drawLabels()
        
        if not self.piecesDrawn:
            self.drawPieces()
            self.piecesDrawn = True

    def drawLabels(self):
        level_label = label_font.render("LEVEL", True, WHITE)
        level_text = text_font.render(self.game.level, True, WHITE)
        x, y = WIDTH/2+155, HEIGHT/2-190
        screen.blit(level_label, (x, y))
        screen.blit(level_text, (x, y+30))
        x, y = x, y + 60
        score_label = label_font.render("SCORE", True, WHITE)

        score = self.game.score
        if len(str(score)) == 1:
            score = "000" + str(score)
        elif len(str(score)) == 2:
            score = "00" + str(score)
        elif len(str(score)) == 3:
            score = "0" + str(score)
        else: score = str(score)
        
        score_text = text_font.render(score, True, WHITE)
        screen.blit(score_label, (x, y))
        screen.blit(score_text, (x, y+30))

    def drawPieces(self):
        for i in range(8):
            for j in range(2):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    addr = (i*50+25, j*50+25) # the address(or position) of the pieace on the board
                    piece = Piece(self, addr, "black", BLACK)
                    self.addPiece(piece)
                
        for i in range(8):
            for j in range(2, 6):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    addr = (i*50, j*50)
                    piece = Empty(addr)
                    self.addPiece(piece)
            
        for i in range(8):
            for j in range(6, 8):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    addr = (i*50+25, j*50+25)
                    piece = Piece(self, addr, "white", WHITE)
                    self.addPiece(piece)

    def addPiece(self, piece):
        """ Adds a piece object to the board """
        
        self.pieces[(piece.x, piece.y)] = piece

    def getPiece(self, address):
        """ Returns a piece object """
        
        return self.pieces.get(address, None)

    def removePiece(self, address):
        """ Removes a piece from the board """

        try:
            del self.pieces[address]
        except KeyError:
            print("error removing piece!")

class Droughts(object):

    def __init__(self):
        self.level = "Easy"
        self.score = 0
        self.player = "person"
        self.currentPiece = None
        self.playerMoves = None
        self.board = Board(self)
        self.gameOver = False
        self.fullscreen = True

    def fullScreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        else:
            screen = pygame.display.set_mode((650, 400), FULLSCREEN, 32)

    def handleEvents(self):
        """ Handles game events """
        
        #if self.player == "person":
            #playerEatMoves = self.thinkEatMovesForUser() # check if user can eat,
            #if so force him or her to do so

            #if playerEatMoves:
             #   self.playerMoves = playerEatMoves
            #else: self.playerMoves = None
            
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                xcor = [i for i in range(x-6, x+37)]
                ycor = [i for i in range(y-6, y+37)]
                for piece_x, piece_y in self.board.pieces.keys():
                    if piece_x in xcor and piece_y in ycor:
                        piece = self.board.getPiece((piece_x, piece_y))
                        if piece.name == "white" and self.player == "person":
                            self.currentPiece = piece
                            self.playerMoves = self.currentPiece.getPossibleMoves()                            
                
                if self.playerMoves is not None and len(self.playerMoves) > 0:

                    moveList = []

                    for old, new, obj in self.playerMoves.values():
                        moveList.append(new)

                    x, y = pygame.mouse.get_pos()
                    
                    for dx, dy in moveList:
                        xcor = [i for i in range(dx-30, dx+30)]
                        ycor = [i for i in range(dy-30, dy+30)]                    
                        if x in xcor and y in ycor:
                            for key, value in self.playerMoves.items():
                                old, new, obj = value
                                if new == (dx, dy):
                                    code = key
                            self.currentPiece.move(self.playerMoves[code]) # move the piece to the new position(address)
                            
            elif event.type == QUIT:
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_DELETE:
                    exit()
                elif event.key == K_SPACE:
                    self.gameOver = True
                elif event.key == K_f:
                    self.fullScreen()
                
        if self.player == "computer":
            moves = {}

            for piece in self.board.pieces.values():
                if piece.name == "black":
                    piece_move = piece.getPossibleMoves()
                    for key, value in piece_move.items():
                        moves[key] = value

            self.thinkEatMoves(moves)  # see if computer might eat

            if not moves:
                self.player = "person"
                return

            keys = [key for key in moves.keys()]
            key = choice(keys)
            old, new, piece = moves[key]
            piece.move(moves[key])

            self.player = "person"

    def thinkEatMovesForUser(self):
        moves = {}
        
        for piece in self.board.pieces.values():
            if piece.name == "white":
                pieceMoves = piece.getPossibleMoves()
                for key, value in pieceMoves.items():
                    moves[key] = value

        eatMoves = {}

        for key, value in moves.items():
            old, new, obj = value
            empty = self.board.getPiece((new[0], new[1]))
            if empty.ready:
                eatMoves[key] = value

        return eatMoves

    def thinkEatMoves(self, moves, player="computer"):
        eatMoves = {}
        
        for key, value in moves.items():
            old, new, obj = value
            empty = self.board.getPiece((new[0], new[1]))
            if empty.ready:
                eatMoves[key] = value

        if eatMoves and player == "computer":
            keys = [key for key in eatMoves.keys()]
            key = choice(keys)
            old, new, piece = eatMoves[key]
            piece.move(eatMoves[key])

            self.player = "person"
            return
        elif eatMoves and player == "person": return eatMoves
        elif not eatMoves and player == "person": return None

    def run(self):
        """ Keeps the game running """
        
        if not self.gameOver:
            screen.fill(COLOR3)
            self.board.drawBoard()
            self.handleEvents()
            for piece in self.board.pieces.values():
                piece.update()
        else:
            self.resetGame()
        pygame.display.update()

    def resetGame(self):
        screen.fill(COLOR3)
        
        game_over_text = "GAME OVER\n\rYour score: {0}\n\rPress SPACE to restart.".format(str(self.score))
        game_over_text = game_over_font.render(game_over_text, True, BLACK)
        text1 = "Droughts version 1.0\n\rCopyright © 2019 Droose Inc"
        text1 = game_over_font.render(text1, True, BLACK)
        text2 = "All rights reserved."
        text2 = game_over_font.render(text2, True, BLACK)
        text3 = "Feedback: peteraugustinemwale@gmail.com"
        text3 = game_over_font.render(text3, True,  BLACK)
        text4 = "Facebook: 'Droose Inc'"
        text4 = game_over_font.render(text4, True,  BLACK)
        
        screen.blit(game_over_text, (WIDTH/2-game_over_text.get_width()/2, HEIGHT/2-1))
        screen.blit(text1, (WIDTH/2-game_over_text.get_width()/2, HEIGHT/2+30))
        screen.blit(text2, (WIDTH/2-game_over_text.get_width()/2, HEIGHT/2+60))
        screen.blit(text3, (WIDTH/2-game_over_text.get_width()/2, HEIGHT/2+90))
        screen.blit(text4, (WIDTH/2-game_over_text.get_width()/2, HEIGHT/2+120))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)
            elif event.type == KEYDOWN and event.key == K_SPACE:
                self.board.pieces = {}
                self.board.piecesDrawn = False
                self.score = 0
                self.gameOver = False
                
def main():
    global screen
    
    screen = pygame.display.set_mode((650, 400), FULLSCREEN, 32)
    pygame.display.set_caption("Droughts(Checkers)")
    screen.fill(COLOR3)
    
    droughts = Droughts()

    while True:
        droughts.run()

if __name__ == "__main__":
    main()