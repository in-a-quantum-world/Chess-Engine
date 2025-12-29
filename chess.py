#chess board and stuff
import pygame
import random
import math
import numpy
import os
from chess_classes import chess_board
from chess_player import Player
import chess_mves

#initialising pygame
pygame.init()
chess_screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
bg = pygame.Surface((1000,1000))
font = pygame.font.SysFont("Arial",35)

def draw_board(chess_screen):
    for i in range(0,8):
        pygame.draw.line(chess_screen,(0,0,0), (100 + (100 * i), 100), (100 + (100 * i),807),4)
        pygame.draw.line(chess_screen,(0,0,0), (100,100 + (100 * i) ), (807, 100 + (100 * i)),4)
        
    for i in range(0,8):
        for j in range(0,8):
            if (i + j) % 2 == 0:
                #pygame.Rect(left, top, width, height)
                pygame.draw.rect(chess_screen,"white",pygame.Rect(
                    (100 + (100*j)),(100 + (100*i)),100,100))
                
            else:
                #pygame.Rect(left, top, width, height)
                pygame.draw.rect(chess_screen,"black",pygame.Rect(
                    (100 + (100*j)),(100 + (100*i)),100,100))
                
    pygame.display.update()
                


def load_images(images):
    DATA = r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/"
  
    directories_b = []
    directories_w = []
    for i in boardie[0]:
        directories_b.append(DATA  + i)
    for n in boardie[7]:
        directories_w.append(DATA + n)
     
    #black pieces
    for j in range(8):
        temp = boardie[j][0]
        to_load = pygame.image.load(directories_w[j] + ".png")
        chess_screen.blit(to_load,(120 + (j*100),120))
        
    for y in range(8):
        #black pawn
        to_load = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/bp" + ".png")
        chess_screen.blit(to_load,(120 + (y*100),220))
    
    for a in range(8):
        #white pawn
        to_load = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/wp" + ".png")
        chess_screen.blit(to_load,(120 + (a*100),720))
    
    #white pieces
    for k in range(8):
        to_load = pygame.image.load(directories_b[k] + ".png")
        chess_screen.blit(to_load,(120 + (k*100),820))
        temp = boardie[7][k]
        
    pygame.display.update()
        
        
        
boardie = [["bR", "bN", "bB", "bQ","bK","bB","bN","bR"],
                        ["bp","bp","bp","bp","bp","bp","bp","bp"],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        ["wp","wp","wp","wp","wp","wp","wp","wp"],
                        ["wR", "wN", "wB", "wQ","wK","wB","wN","wR"]]
board = chess_board()
images = []
running = True

def move(chess_screen):
    for event in pygame.event.get():
        if event.type == pygame.mouse.get_pressed()[0]:
            print("mouse clicked")
            
            #location of where the screen was clicked
            x, y = pygame.mouse.get_pos()
            row = (x - 100)% 64
            column = (y - 100) % 64
            piece = board[row][column]
            if piece == " ":
                print("no piece has been selected")
            else:
                print(x,y)
                if event.type == pygame.mouse.get_pressed()[0]:
                    print("mouse clicked yet again")
                    a, b = pygame.mouse.get_pos()
                    row2 = (a - 100)% 64
                    column2 = (b - 100) % 64
                    if board[row2][column2] != " ":
                        print("there is already a piece on this square")
                    else:
                        new_square = board[row2][column2]
                        
#checking if a square is empty, contains a friendly piece or an enemy's piece           
def valid_square(x_val,y_val):
    if board.board[x_val][y_val] == " ":
        print("this square doesn't contain a piece")
        return False
    else:
        if board.moves % 2 == 1:
            print("white's turn")
        else:
            print("black's turn")
            
#checking a move for a certain piece is valid. uses the method in the piece's class
def valid_move():
    pass

#this function should highlight the possible moves for a selected piece on the board
def highlight_moves():
    pass

def main():
    running = True
    chess_screen.fill((0,100,70))
    
    draw_board(chess_screen)
    load_images(board)
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x_val = ((x - 100)//100) 
                y_val = ((y - 100)//100) 
                
                if x_val < 0 or y_val < 0:
                    print("you have not entered the number in the correct location")
                else:
                    print(x_val,y_val)
                    if valid_square(x_val,y_val) == True:
                        print("right")
                    pygame.display.flip()
                    pygame.display.update()
                
    pygame.display.update()
    
if __name__ == "__main__":
    main()
    
    
legal_moves = {}
