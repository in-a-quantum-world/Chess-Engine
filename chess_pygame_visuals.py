import pygame
from chess_classes import chess_board
from chess_player import Player
from chess_mves import Tree
from chess_move_handler import Move_handler
from chess_randomai import RandomAI
import pygame_widgets
from tkinter import *
from tkinter import messagebox
from pygame_widgets.button import Button as B

import sqlite3

pygame.init()
Tk().wm_withdraw()  # hides tkinter main window

login_screen = pygame.display.set_mode((1000,1000))
chess_screen = pygame.display.set_mode((1500, 1000))
clock = pygame.time.Clock()
bg = pygame.Surface((1000,1000))
font = pygame.font.SysFont("Arial",20)

#---------------------------setting up board---------------------------------------------------------------
def additional_squares(move_list):
    try:
       for move in move_list:
            pygame.draw.rect(chess_screen,"#dde38a",pygame.Rect(
                (100 + (100*move[0])),(100 + (100*move[1])),100,100))
    except TypeError:
        print("empty list")
        

def draw_board(chess_screen):
    pygame.draw.rect(chess_screen, "white", [1100, 300, 300, 700])

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
    
def castle_move_left(board,board2,user):
    current_piece = "wR2" if user == "user1" else "bR2"
    directories_b = []
    directories_w = []
    DATA = r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/"
    for i in board.board[0]:
        directories_b.append(DATA + i)
    for n in board.board[7]:
        directories_w.append(DATA + n)
    x1, y1 = board.get_pos(current_piece)
    x2, y2 = board.get_pos("bK") if user == "user2" else board.get_pos("wK")
    print(board.update_moves())
    print(board.update_board(x1, y1, " "))
    print(board.update_board(x2, y2, " "))
    to_copy1 = DATA + current_piece + "png"
    to_copy2 = DATA + "bK" + "png" if user == "user2" else DATA + "wK" + "png"
    # blitting the rook
    if str(board2[x2][y2])[0] == "b":
        img = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/bR.png")
    else:
        img = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/wR.png")
    x_val2 = 0 if user == "user1" else 7
    y_val2 = 5
    chess_screen.blit(img, (120 + ((y_val2) * 100), 120 + ((x_val2) * 100)))

    # work on this
    if (x1 + y1) % 2 == 0:
        pygame.draw.rect(chess_screen, "#fcfafa", pygame.Rect(
            (100 + (100 * x1)), (100 + (100 * y1)), 100, 100))
    else:
        pygame.draw.rect(chess_screen, "#421f1f", pygame.Rect(
            (100 + (100 * x1)), (100 + (100 * y1)), 100, 100))

    # blitting the king
    if str(board2[x2][y2])[0] == "b":
        img = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/bK.png")
    else:
        img = pygame.image.load(r"C:/Users/rucha/OneDrive/Documents/Python/chess_game/images/wK.png")
    x_val2 = 0 if user == "user1" else 7
    y_val2 = 6
    chess_screen.blit(img, (120 + ((x_val2) * 100), 120 + ((y_val2) * 100)))

    if (x2 + y2) % 2 == 0:
        pygame.draw.rect(chess_screen, "#fcfafa", pygame.Rect(
            (100 + (100 * x2)), (100 + (100 * y2)), 100, 100))
    else:
        pygame.draw.rect(chess_screen, "#421f1f", pygame.Rect(
            (100 + (100 * x2)), (100 + (100 * y2)), 100, 100))
    print("castle move left")
def castle_move_right(board, board2, user):
    current_piece = "wR1" if user == "user1" else "bR1"
    x1, y1 = board.get_pos(current_piece)
    x2, y2 = board.get_pos("bK") if user == "user2" else board.get_pos("wK")
    print(board.update_moves())
    print(board.update_board(x1, y1, " "))
    print(board.update_board(x2, y2, " "))
    to_copy1 = DATA + current_piece + "png"
    to_copy2 = DATA + "bK" + "png" if user == "user2" else DATA + "wK" + "png"
    # blitting the rook
    if str(board2[x2][y2])[0] == "b":
        img = pygame.image.load(directories_b[0] + ".png")
    else:
        img = pygame.image.load(directories_w[0] + ".png")
    x_val2 = 0 if user == "user1" else 7
    y_val2 = 5
    chess_screen.blit(img, (120 + ((y_val2) * 100), 120 + ((x_val2) * 100)))

    # work on this
    if (x1 + y1) % 2 == 0:
        pygame.draw.rect(chess_screen, "#fcfafa", pygame.Rect(
            (100 + (100 * x1)), (100 + (100 * y1)), 100, 100))
    else:
        pygame.draw.rect(chess_screen, "#421f1f", pygame.Rect(
            (100 + (100 * x1)), (100 + (100 * y1)), 100, 100))

    # blitting the king
    if str(board2[n1][n2])[4] == "b":
        img = pygame.image.load(directories_b[4] + ".png")
    else:
        img = pygame.image.load(directories_w[4] + ".png")
    x_val2 = 0 if user == "user1" else 7
    y_val2 = 6
    chess_screen.blit(img, (120 + ((x_val2) * 100), 120 + ((y_val2) * 100)))

    if (x2 + y2) % 2 == 0:
        pygame.draw.rect(chess_screen, "#fcfafa", pygame.Rect(
            (100 + (100 * x2)), (100 + (100 * y2)), 100, 100))
    else:
        pygame.draw.rect(chess_screen, "#421f1f", pygame.Rect(
            (100 + (100 * x2)), (100 + (100 * y2)), 100, 100))

def castle_buffer_left():
    print("trying to castle")
    global board2
    board2 = board.board
    user = "user1" if board.moves % 2 == 0 else "user2"
    if user == "user1":
        castle_move_left(board,board2,user)
            #error message - you cannot castle
    else:
        castle_move_left(board,board2, user)
def castle_buffer_right():
    print("castle buffer right")
    global board2
    board2 = board.board
    user = "user1" if board.moves % 2 == 0 else "user2"
    if user == "user1":
        castle_move_right(board,board2,user)
            #error message - you cannot castle
    else:
        castle_move_right(board,board2,user)
castle_right_button = B(
    login_screen, 1000, 800, 85, 30, text='castle right',
    fontSize = 20, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,500, 200), radius=20,
    onClick = castle_buffer_right
)
castle_left_button = B(
    login_screen, 1000, 700, 85, 30, text='castle left',
    fontSize = 20, mar0gin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,500, 200), radius=20,
    onClick = castle_buffer_left
)

def update_piece(x_val,y_val):
    pass
    
    
def move_piece_to(x_val,y_val,x_val2,y_val2,player):
    current_piece = board.board[y_val][x_val]
    pygame.draw.rect(chess_screen, "white", [1100, 100, 500, 200])
    correct = False
    if board.moves % 2 == 1:
        if en_passant_possible_user2 == True:
            correct = True
            killed_piece = board.board[y_val2+1][x_val2]
            num = 1
            user2.update_points(num)
        elif user2.access_to_move(current_piece,y_val,x_val,y_val2,x_val2,board.board,board) == True:
            correct = True
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
        if en_passant_possible_user2 == True:
            correct = True
            killed_piece = board.board[y_val2+1][x_val2]
            num = 1
            user1.update_points(num)

        elif user1.access_to_move(current_piece,y_val,x_val,y_val2,x_val2,board.board,board) == True:
            correct = True
            
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
        whole_pgn = handler.pgn_notation(y_val, x_val, y_val2, x_val2, current_piece, board.moves)
        length_pgn = len(whole_pgn)
        latest = whole_pgn[length_pgn - 8:length_pgn]
        print("whole pgn is: ", whole_pgn)
        """
        if board.moves > 3:
            left_over = board.moves % 3
            most = board.moves // 3
            for z in range(most):
                pgn_sections_list.append(whole_pgn[(24*z):(24*(z+1))])
        else:
            pgn_sections_list.append(whole_pgn)
        """
        for x in range(board.moves):
            curr_pgn = whole_pgn[(8*(2*x)):(8*((2*x)+1))]
            #curr_pgn = handler.get_pgn()
            text = font.render(curr_pgn, True, "black")
            chess_screen.blit(text, (1100, 200+(30*(x))))

        print(handler.get_all_moves(y_val, x_val, board.board, current_piece, user1))
        print(board.update_board(y_val2,x_val2,board.board[y_val][x_val]))
        current_pgn = handler.get_pgn()
        #to_copy = DATA + current_piece + "png"
        text2 = font.render(latest, True, "black")
        chess_screen.blit(text2, (1100, 150))
        if board.moves % 2 == 1:
            if en_passant_possible_user2 == False:
                current_fen = handler.fen_conversion(board.board,player.colour(),"-","-",0,board.moves)
            else:
                current_fen = handler.fen_conversion(board.board,player.colour(),"",current_pgn,0,board.moves)
        elif board.moves % 2 == 0:
            if en_passant_possible_user1== False:
                current_fen = handler.fen_conversion(board.board,player.colour(),"-","-",0,board.moves)
            else:
                current_fen = handler.fen_conversion(board.board,player.colour(),"",current_pgn,0,board.moves)
        fen_text = font.render(current_fen, True, "black")
        chess_screen.blit(fen_text, (1100, 100))
        print("current fen is", current_fen)
        pygame.display.update()
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
        print("done?")
    """
    if board.moves % 2 == 1:
        user1.get_all_valid_moves(y_val2,x_val2,board.board,str(board[y_val2][x_val2]))
    else:
        user2.get_all_valid_moves(y_val2,x_val2,board.board,str(board[y_val2][x_val2]))
        
    pygame.display.update()
    """
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
    global user1
    user1 = Player("white")
    # player 2 will have to be the engine
    global user2
    user2 = Player("black")
    user1.inst_moves_history()
    user2.inst_moves_history()
    global handler
    handler = Move_handler()
    selected = []
    global player_clicks
    player_clicks = []

    while running:
        events = pygame.event.get()
        #engine_play_button.listen(events)
        #engine_play_button.draw()
        #user_play_button.draw()
       # castle_left_button.show()
        #castle_right_button.show()
        for e in events:

            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                #be wary with coordinates
                x, y = pygame.mouse.get_pos()
                x_val = ((x - 10)//100) - 1
                y_val = ((y - 10)//100) - 1
                print("here")
                if board.castling_valid("white", 7, 7, 7, 6, 7, 5) == True or board.castling_valid("white", 7, 0, 7, 2,7, 3) == True:
                    if user1.in_check(user2, board.board) == True:
                        print("player 1 is in check")
                        messagebox.showinfo(check, "user1 in check")

                    else:
                        print("white can castle")
                        if (x >= 757.5 and x <= 842.5) and (
                                y >= 985 and y <= 1015):  # check if they clicked on a button
                            print('castle right')
                            castle_buffer_right()
                        elif (x >= 757.5 and x <= 842.5) and (y <= 715 and y >= 685):
                            print("castle left")  # check for castling right or left
                            castle_buffer_left()
                if board.castling_valid("black", 0, 7, 0, 6, 0, 5) == True or board.castling_valid("black", 0, 0, 0, 2,0, 3) == True:
                    print("black can castle")

                    if user2.in_check(user1, board.board) == True:
                        print("player 1 is in check")
                        messagebox.showinfo("check", "user2 in check")

                    else:
                        print("Hi")
                        if (x >= 757.5 and x <= 842.5) and (
                                y >= 985 and y <= 1015):  # check if they clicked on a button
                            print('castle right')
                            castle_buffer_right()
                        elif (x >= 757.5 and x <= 842.5) and (y <= 715 and y >= 685):
                            print("castle left")  # check for castling right or left
                            castle_buffer_left()

                if x_val < 0 or y_val < 0:
                    print("you have not entered the number in the correct location")
                    messagebox.showinfo("Re-enter", "You have not entered the number in the correct location")

                if (x >= 757.5 and x <= 842.5) and (y >= 985 and y <= 1015): #check if they clicked on a button
                    print('castle right')
                    castle_buffer_right()
                elif (x >= 757.5 and x <= 842.5) and (y <= 715 and y >= 685):
                    print("castle left")#check for castling right or left
                    castle_buffer_left()
                else:
                    print(x_val,y_val)
                    if selected == [x_val,y_val]:
                        player_clicks = []
                    else:
                        selected = [x_val,y_val]
                        player_clicks.append(selected)
                    
                    if len(player_clicks) == 2: #to show that second click has been performed 
                        if board.moves % 2 == 0:
                            print("hi")
                            global en_passant_possible_user2
                            global en_passant_piece2
                            en_passant_possible_user2 = board.en_passant_valid(player_clicks[1][1], player_clicks[1][1], user2.colour())
                            # buffer_move_highlight(player_clicks[0][0],player_clicks[0][1])
                            piece_moved = board.board[(player_clicks[0][1])][(player_clicks[0][0])]
                            if en_passant_possible_user2 == True:
                                print("en passant is valid")
                                piece_moved = board.board[(player_clicks[0][1])][(player_clicks[0][0])]
                                en_passant_piece2 = piece_moved
                                global en_passant_square2
                                en_passant_square2 = [player_clicks[1][1], player_clicks[1][0]]
                                move_piece_to(player_clicks[0][0], player_clicks[0][1], player_clicks[1][0],
                                          player_clicks[1][1], user2)
                                user1.add_history(board, [(player_clicks[0][0], player_clicks[0][1]),
                                                          (player_clicks[1][0], player_clicks[1][1]), piece_moved],
                                                  handler, board.moves)
                            else:
                                if move_piece_from(player_clicks[0][0],player_clicks[0][1]) == True:
                                    print("board moves is", board.moves)
                                    if board.moves % 2 == 0:
                                        print("hi")
                                        piece_moved = board.board[(player_clicks[0][1])][(player_clicks[0][0])]
                                        move_piece_to(player_clicks[0][0],player_clicks[0][1],player_clicks[1][0],player_clicks[1][1],user2)
                        else:

                            if board.castling_valid("black", 0, 7, 0, 6, 0, 5) == True or board.castling_valid("black", 0, 0, 0, 2, 0, 3) == True:
                                print("can castle")
                            else:
                                global en_passant_possible_user1
                                en_passant_possible_user1 = board.en_passant_valid(player_clicks[1][1],
                                                                             player_clicks[1][0], user1.colour())
                                piece_moved = board.board[(player_clicks[0][1])][(player_clicks[0][0])]
                                if en_passant_possible_user1 == True:
                                    print("en passant is valid")
                                    global en_passant_square1
                                    global en_passant_piece1
                                    en_passant_piece1 = piece_moved
                                    en_passant_square1 = [player_clicks[0][1], player_clicks[0][0]]


                                    move_piece_to(player_clicks[0][0],player_clicks[0][1],player_clicks[1][0],player_clicks[1][1],user2)
                                    print("en passant piece is: ",en_passant_piece1)
                                    print("en passant square is: ",en_passant_square1)
                                    print("the piece is: ",piece_moved)
                                else:
                                    move_piece_to(player_clicks[0][0], player_clicks[0][1], player_clicks[1][0],
                                      player_clicks[1][1], user1)


                            if board.moves % 2 == 0:
                                if piece_moved == " ":
                                    piece_moved = "wp1"
                                user2.add_history(board,[(player_clicks[0][0],player_clicks[0][1]),(player_clicks[1][0],player_clicks[1][1]),piece_moved],handler,board.moves)
                                print("user2 moves history",user2.get_stack_moves_history())
                                #change to the other user
                                if user1.in_check(user2,board.board) == True:
                                    print("player 1 is in check")
                                if board.is_game_over(player_clicks[1][1],player_clicks[1][0]) == True:
                                    pygame.quit()
                            else:
                                user1.add_history(board,[(player_clicks[0][0],player_clicks[0][1]),(player_clicks[1][0],player_clicks[1][1]),piece_moved],handler,board.moves)
                                print("user1 moves history",user1.get_stack_moves_history())
                                #change to the user
                                if user2.in_check(user1,board.board) == True:
                                    print("player 2 is in check")
                                if board.is_game_over(player_clicks[1][1],player_clicks[1][0]) == True:
                                    messagebox.showinfo("Game over" "Checkmate")

                                    return
                                    #pygame.quit()
                                    
                            """
                            if e.type == pygame.MOUSEBUTTONUP:
                                for e in pygame.event.get():
                                    #check for a second mouseclick, following the first one
                                    if e.type == pygame.MOUSEBUTTONDOWN:
                                        x2, y2 = pygame.mouse.get_pos()
                                        x_val2 = ((x2 - 10)//100) - 1
                                        y_val2 = ((y2 - 10)//100) - 1
                                        if valid_square(x_val2,y_val2) == True:
                                            move_piece_to(x_val,y_val,x_val2,y_val2)
                                            
                                            """
                        selected = []
                        player_clicks = []
                        
                    elif len(player_clicks) == 1:
                        #buffer_move_highlight(player_clicks[0][0],player_clicks[0][1])
                        print(player_clicks[0])
                castle_left_button.listen(events)
                #user_play_button.listen(events)
                castle_right_button.listen(events)
                #engine_play_button.listen(events)
                #engine_play_button.draw()
                #user_play_button.draw()
                castle_left_button.draw()
                castle_right_button.draw()
                pygame_widgets.update(events)
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

#---------------------------logging in, creating an account-----------------------------
def start_up():
    login_screen.fill((50,30,100))
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")
    
#---------------------object instantiation----------------------------------
   
if __name__ == "__main__":
    main()