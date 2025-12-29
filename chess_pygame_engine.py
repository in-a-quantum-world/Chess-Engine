#chess engine time!!! wooohooo!!

#chess pygame with the chess ai
#computer generated moves are not random
import pygame
from chess_classes import chess_board
from chess_player import Player
from chess_mves import Tree, Move_handler
from accessing_chess_db import Person
from pygame_widgets.button import Button

import sqlite3

pygame.init()
login_screen = pygame.display.set_mode((1000,1000))
chess_screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
bg = pygame.Surface((1000,1000))
font = pygame.font.SysFont("Arial",35)

#---------------------------setting up board---------------------------------------------------------------

def engine_play(user2,boardie,board):
    #move_choice = user2.get_random_move(boardie,board)
    move,piece = user2.get_random_move(boardie,board)
    print("move is {}, piece is {}".format(move,piece))
    
    return move,piece
    #add this to a tree
    #create a new board object with the move carried out and pieces etc 
    
engine_play_button = Button(
    login_screen, 700, 75, 100, 100, text='Login',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = lambda: engine_play
)

def draw_board(chess_screen):
    for i in range(0,8):
        pygame.draw.line(chess_screen,(0,0,0), (100 + (100 * i), 100), (100 + (100 * i),807),4)
        pygame.draw.line(chess_screen,(0,0,0), (100,100 + (100 * i) ), (807, 100 + (100 * i)),4)
        
    for i in range(0,8):
        for j in range(0,8):
            if (i + j) % 2 == 0:
                #pygame.Rect(left, top, width, height)
                pygame.draw.rect(chess_screen,"#fcfafa",pygame.Rect(
                    (100 + (100*j)),(100 + (100*i)),100,100))
                
            else: #3d0909   #543232
                #pygame.Rect(left, top, width, height)
                pygame.draw.rect(chess_screen,"#421f1f",pygame.Rect(
                    (100 + (100*j)),(100 + (100*i)),100,100))
                
    pygame.display.update()
    
def load_images(images):
    global directories_w
    global directories_b
    global DATA
    DATA = r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/"
    
    directories_b = []
    directories_w = []
    for i in boardie[0]:
        directories_b.append(DATA  + i)
    for n in boardie[7]:
        directories_w.append(DATA + n)
        
    print("directories b: ",directories_b)
    print("directories w: ",directories_w)
    #black pieces
    for j in range(8):
        
        to_load = pygame.image.load(directories_b[j] + ".png")
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
        to_load = pygame.image.load(directories_w[k] + ".png")
        chess_screen.blit(to_load,(120 + (k*100),820))
    
    
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

def reset():
    boardie = [["bR", "bN", "bB", "bQ","bK","bB","bN","bR"],
                        ["bp","bp","bp","bp","bp","bp","bp","bp"],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        ["wp","wp","wp","wp","wp","wp","wp","wp"],
                        ["wR", "wN", "wB", "wQ","wK","wB","wN","wR"]]

    
    
    board = chess_board()
    global directories_w
    global directories_b
    DATA = r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/"
  
    directories_b = []
    directories_w = []
    for i in board.board[0]:
        directories_b.append(DATA  + i)
    for n in board.board[7]:
        directories_w.append(DATA + n)
        
    print("directories b: ",directories_b)
    print("directories w: ",directories_w)
    #black pieces
    for j in range(8):
        
        to_load = pygame.image.load(directories_b[j] + ".png")
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
        to_load = pygame.image.load(directories_w[k] + ".png")
        chess_screen.blit(to_load,(120 + (k*100),820))
    
    pygame.display.update()
    
    
def update_piece(x_val,y_val):
    pass
        
def move_piece_to(x_val,y_val,x_val2,y_val2,player):
    current_piece = board.board[y_val][x_val]
    
    correct = False
    if board.moves % 2 == 1:
        if user2.access_to_move(current_piece,y_val,x_val,y_val2,x_val2,board.board,board) == True:
            correct = True
            #checking if a kill was made
            print(handler.get_all_moves(y_val,x_val,board.board,current_piece,user2))
            
            if board.board[y_val2][x_val2] != " ":
                killed_piece = board.board[y_val2][x_val2]
                if killed_piece[1] == "Q":
                    num = 9
                elif killed_piece[1] == "p":
                    num = 1
                elif killed_piece[1] == "B":
                    num = 3
                elif killed_piece[1] == "N":
                    num = 3
                elif killed_piece[1] == "R":
                    num = 5
                elif killed_piece[1] == "K":
                    num = 200 #note - a king doesn't carry any points, but this is for the chess engine's benefit, as this is its approximate worth
                    board.game_over()
                user2.update_points(num)
                
        #make sure the correct thing is being returned
    else:
        if user1.access_to_move(current_piece,y_val,x_val,y_val2,x_val2,board.board,board) == True:
            correct = True
            print(handler.get_all_moves(y_val,x_val,board.board,current_piece,user1))
            
            if board.board[y_val2][x_val2] != " ":
                killed_piece = board.board[y_val2][x_val2]
                if killed_piece[1] == "Q":
                    num = 9
                elif killed_piece[1] == "p":
                    num = 1
                elif killed_piece[1] == "B":
                    num = 3
                elif killed_piece[1] == "N":
                    num = 3
                elif killed_piece[1] == "R":
                    num = 5
                elif killed_piece[1] == "K":
                    num = 200
                    board.game_over()
                user1.update_points(num)
            
    if correct == True:
        print(board.update_moves())
        print(board.update_board(y_val2,x_val2,board.board[y_val][x_val]))
        print(board.update_board(y_val,x_val," "))
        to_copy = DATA + current_piece + "png"
        #img = pygame.image.load(to_copy)
        
        print("this needs to be blitted: ",board.board[y_val2][x_val2])
        if str(board.board[y_val2][x_val2])[0] == "b":
            
            if str(board.board[y_val2][x_val2])[1] == "R":
                img = pygame.image.load(directories_b[0] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "N":
                img = pygame.image.load(directories_b[1] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "B":
                img = pygame.image.load(directories_b[2] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "Q":
                img = pygame.image.load(directories_b[3] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "K":
                img = pygame.image.load(directories_b[4] + ".png")
            else:
                img = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/bp" + ".png")
        else:
            if str(board.board[y_val2][x_val2])[1] == "R":
                img = pygame.image.load(directories_w[0] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "N":
                img = pygame.image.load(directories_w[1] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "B":
                img = pygame.image.load(directories_w[2] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "Q":
                img = pygame.image.load(directories_w[3] + ".png")
            elif str(board.board[y_val2][x_val2])[1] == "K":
                img = pygame.image.load(directories_w[4] + ".png")
            else:
                img = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/wp" + ".png")
        
        chess_screen.blit(img,(120 + ((x_val2)*100),120 + ((y_val2) * 100)))
        
        
        #remove piece from previous location
        #work on this
        if (x_val + y_val) % 2 == 0:
            pygame.draw.rect(chess_screen,"#fcfafa",pygame.Rect(
            (100 + (100*x_val)),(100 + (100*y_val)),100,100))
        else:
            pygame.draw.rect(chess_screen,"#421f1f",pygame.Rect(
            (100 + (100*x_val)),(100 + (100*y_val)),100,100))
    """
    if board.moves % 2 == 1:
        user1.get_all_valid_moves(y_val2,x_val2,board.board,str(board[y_val2][x_val2]))
    else:
        user2.get_all_valid_moves(y_val2,x_val2,board.board,str(board[y_val2][x_val2]))
        
    pygame.display.update()
    """
#faulty - try and fix it
def buffer_move_highlight(y_val,x_val):
    print((board.board)[x_val][y_val])
    if board.moves % 2 == 1:
        all_moves = user2.move_highlighting(x_val,y_val,board.board[x_val][y_val],board.board)
    else:
        all_moves = user1.move_highlighting(x_val,y_val,board.board[x_val][y_val],board.board)
    
    additional_squares(all_moves)
        
def move_piece_from(y_val,x_val):
    #cue disaster
    if board.board[x_val][y_val] == " ":
        print("this square doesn't contain a piece")
        return False
    else:
        if board.moves % 2 == 1:
            turn = "black"
            print(("this is the: ",board.board[x_val][y_val])[0])
            if str(board.board[x_val][y_val])[0] == "b":
                print("piece is: ",board.board[x_val][y_val])
                return True
            else:
                print("you picked the opponent's piece")
        else:
            turn = "white"
            print(("this is the: ",board.board[x_val][y_val])[0])
            if str(board.board[x_val][y_val])[0] == "w":
                print("piece is: ",board.board[x_val][y_val])
                return True
            else:
                print("you picked the opponent's piece")
                return False

    
def main():
    running = True
    chess_screen.fill((0,100,70))
    
    draw_board(chess_screen)
    load_images(board)
    selected = []
    player_clicks = []
    #incorporate button rather than using the player clicked thingy
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                #be wary with coordinates
                if board.moves % 2 == 1:
                    print("it is not your turn, it is the engine's turn")
                    move, piece = engine_play(user2,board.board,board)
                    engine_move_to(move,piece,board,board.board)
                    temp_list = [move,piece]
                    #DANGEROUS
                    tree = Tree(templist)
                    tree.generate_branches(user1,user2,board.board,board)
                    #WATCH THIS
                else:
                    x, y = pygame.mouse.get_pos()
                    x_val = ((x - 10)//100) - 1
                    y_val = ((y - 10)//100) - 1
                    
                    if x_val < 0 or y_val < 0:
                        print("you have not entered the number in the correct location")
                    else:
                        print(x_val,y_val)
                        if selected == [x_val,y_val]:
                            player_clicks = []
                        else:
                            selected = [x_val,y_val]
                            player_clicks.append(selected)
                        
                        if len(player_clicks) == 2: #to show that second click has been performed 
                            
                            if move_piece_from(player_clicks[0][0],player_clicks[0][1]) == True:
                                
                                #buffer_move_highlight(player_clicks[0][0],player_clicks[0][1])
                                move_piece_to(player_clicks[0][0],player_clicks[0][1],player_clicks[1][0],player_clicks[1][1],user1)
                                piece_moved = board.board[(player_clicks[1][1])][(player_clicks[1][0])]
                                print("the piece is: ",piece_moved)
                                if board.moves % 2 == 0:
                                    user2.add_history([(player_clicks[0][0],player_clicks[0][1]),(player_clicks[1][0],player_clicks[1][1]),piece_moved])
                                    print("user2 moves history",user2.get_stack_moves_history())
                                    if user1.in_check(user2,board.board) == True:
                                        print("player 1 is in check")
                                    if board.is_game_over(player_clicks[1][1],player_clicks[1][0]) == True:
                                        pygame.quit()
                                else:
                                    print("engine's turn!")
                                    user1.add_history([(player_clicks[0][0],player_clicks[0][1]),(player_clicks[1][0],player_clicks[1][1]),piece_moved])
                                    print("user1 moves history",user1.get_stack_moves_history())
                                    #access db??
                                    if user2.in_check(user1,board.board) == True:
                                        print("player 2 is in check")
                                    if board.is_game_over(player_clicks[1][1],player_clicks[1][0]) == True:
                                        pygame.quit()
                                        
                
                            selected = []
                            player_clicks = []
                            
                        elif len(player_clicks) == 1:
                            #buffer_move_highlight(player_clicks[0][0],player_clicks[0][1])
                            print(player_clicks[0])
                            
                        try:
                            pygame.display.update()
                        except:
                            print("game is over")
                        finally:
                            break
                            
        try:        
            pygame.display.update()
        except:
            print("game is over.")

DATA = r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/"

#---------------------------logging in, creating an account---------------------------------------------
def start_up():
    login_screen.fill((50,30,100))
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")
    
#---------------------object instantiation----------------------------------
user1 = Player("white")
#player 2 will have to be the engine
user2 = Engine("black")
user1.inst_moves_history()
user2.inst_moves_history()

handler = Move_handler()
   
if __name__ == "__main__":
    main()