#random move AI
from chess_classes import Pawn, King, Queen, Knight, Bishop, Rook, chess_board
from chess_player import moves_history_stack, Player
import random
class RandomAI():
    points = 0
    def __init__(self,colour):
        self._colour = colour
        
        self.player_knight_1 = Knight(self._colour,1)
        self.player_rook_1 = Rook(self._colour,1)
        self.player_bishop_1 = Bishop(self._colour,1)
        self.player_queen = Queen(self._colour)
        self.player_king = King(self._colour)
        
        self.player_knight_2 = Knight(self._colour,2)
        self.player_rook_2 = Rook(self._colour,2)
        self.player_bishop_2 = Bishop(self._colour,2)
        
        self.pawn1 = Pawn(self._colour,1)
        self.pawn2 = Pawn(self._colour,2)
        self.pawn3 = Pawn(self._colour,3)
        self.pawn4 = Pawn(self._colour,4)
        self.pawn5 = Pawn(self._colour,5)
        self.pawn6 = Pawn(self._colour,6)
        self.pawn7 = Pawn(self._colour,7)
        self.pawn8 = Pawn(self._colour,8)
        
        self.__dummy_player = Player(colour)
    def colour(self):
        return self._colour
    def get_all_valid_moves(self,m1,n1,board,piece):
        self.all_valid_moves = self.__dummy_player.get_all_valid_moves(m1,n1,board,piece)
        return self.all_valid_moves
    def inst_moves_history(self):
        self._all_moves = moves_history_stack()
        
    def get_stack_moves_history(self):
        return self._all_moves.get_stack_moves_history()
    
    def get_whole_move_history(self,big_board):
        if big_board.is_game_over("x") == True:
            all_user_game_history = self._all_moves.get_stack_moves_history()
    
    def get_most_recent_move(self):
        return self._all_moves.get_most_recent_move()
    def add_history(self,sublist):
        self._all_moves.add(sublist)
    
    def update_points(cls,num):
        cls.points += num
        print("points are now:",cls.points)
        return cls.points
    
    def in_check(self,opponent,board):
        check = False
        temp_board = chess_board()
        temp_board.new_board(board)
        move = opponent.get_most_recent_move()
        print("this was the most recent move",move)
        m2 = move[1][0]
        n2 = move[1][1]
        piece = move[2]
        name = piece
        move_list = []
        #if str(piece)[0] == "b":
        
        if name[1:2] == "R":
            piece_num = int(name[2:3])
            if piece_num == 1:
                move_list = opponent.player_rook_1.all_moves(m2,n2,board)
            elif piece_num == 2:
                move_list = opponent.player_rook_2.all_moves(m2,n2,board)
                
        elif name[1:2] == "N":
            print("trying to move knight")
            piece_num = int(name[2:3])
            if piece_num == 1:
                move_list = opponent.player_knight_1.all_moves(m2,n2,board)
            elif piece_num == 2:
                move_list = opponent.player_knight_2.all_moves(m2,n2,board)
                
        elif name[1:2] == "B":
            print("trying to move bishop")
            piece_num = int(name[2:3])
            if piece_num == 1:
                move_list = opponent.player_bishop_1.all_moves(m2,n2,board)
            elif piece_num == 2:
                move_list = opponent.player_bishop_2.all_moves(m2,n2,board)
                
        elif name[1:2] == "Q":
            move_list = opponent.player_queen.all_moves(m2,n2,board)
        elif name[1:2] == "K":
            move_list = opponent.player_king.all_moves(m2,n2,board)
        elif name[1:2] == "p":
            piece_num = int(name[2:3])
            if piece_num == 1:
                move_list = opponent.pawn1.all_moves(m2,n2,board,temp_board)
            elif piece_num == 2:
                move_list = opponent.pawn2.all_moves(m2,n2,board,temp_board)
            elif piece_num == 3:
                move_list = opponent.pawn3.all_moves(m2,n2,board,temp_board)
            elif piece_num == 4:
                move_list = opponent.pawn4.all_moves(m2,n2,board,temp_board)
            elif piece_num == 5:
                move_list = opponent.pawn5.all_moves(m2,n2,board,temp_board)
            elif piece_num == 6:
                move_list = opponent.pawn6.all_moves(m2,n2,board,temp_board)
            elif piece_num == 7:
                move_list = opponent.pawn7.all_moves(m2,n2,board,temp_board)
            elif piece_num == 8:
                move_list = opponent.pawn8.all_moves(m2,n2,board,temp_board)
                
        print("this is the moves list:",move_list)
        print("self colour is {}, opponent colour is {}".format(self._colour,opponent.colour()))
        try:
            for move in move_list:
                print(move)
                if move == [4,7] and (self._colour == "white" and opponent.colour() == "black"):
                    check = True
                    break
                elif move == [4,0] and (self._colour == "black" and opponent.colour() == "white"):
                    check = True
                    break
            print("check is: ",check)
        except TypeError:
            print("type error.")
        return check
            
    def get_piece_index(self,boardie,piece):
        self.find = piece
        n1,m1 = 0,0
        for x in range(0,8):
            for y in range(0,8):
                
                if boardie[x][y] == self.find:
                    print("x is {}, y is {}".format(x,y))
                    return x,y
                    #check this
                
    
    def find_all_moves(self,boardie,board):
        possible_move_list = []
        
        if self._colour == "white":
            pre = "w"
        else:
            pre = "b"
        #edit this
            #change all board parameters to boardie
        try:
            possible_move_list.append([self.player_rook_1.all_moves(self.get_piece_index(boardie,str(pre + "R1"))[0],self.get_piece_index(boardie,str(pre + "R1"))[1],boardie),pre+"R1"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.player_rook_2.all_moves(self.get_piece_index(boardie,str(pre + "R2"))[0],self.get_piece_index(boardie,str(pre + "R2"))[1],boardie),pre+"R2"])
        except:
            print("piece not found")
        try:
        
            possible_move_list.append([self.player_knight_1.all_moves(self.get_piece_index(boardie,str(pre + "N1"))[0],self.get_piece_index(boardie,str(pre + "N1"))[1],boardie),pre+"N1"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.player_knight_2.all_moves(self.get_piece_index(boardie,str(pre + "N2"))[0],self.get_piece_index(boardie,str(pre + "N2"))[1],boardie),pre+"N2"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.player_bishop_1.all_moves(self.get_piece_index(boardie,str(pre + "B1"))[0],self.get_piece_index(boardie,str(pre + "B1"))[1],boardie),pre+"B1"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.player_bishop_2.all_moves(self.get_piece_index(boardie,str(pre + "B2"))[0],self.get_piece_index(boardie,str(pre + "B2"))[1],boardie),pre+"B2"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.player_queen.all_moves(self.get_piece_index(boardie,str(pre + "Q"))[0],self.get_piece_index(boardie,str(pre + "Q"))[1],boardie),pre+"Q"])
        except:
            print("piece not found")
            #possible_move_list.append(self.player_king.all_moves(self.get_piece_index(board,str(pre + "K"))[0],self.get_piece_index(board,str(pre + "K"))[1],boardie))
        try:
            possible_move_list.append([self.pawn1.all_moves(self.get_piece_index(boardie,str(pre + "p1"))[0],self.get_piece_index(boardie,str(pre + "p1"))[1],boardie,board),pre+"p1"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.pawn2.all_moves(self.get_piece_index(boardie,str(pre + "p2"))[0],self.get_piece_index(boardie,str(pre + "p2"))[1],boardie,board),pre+"p2"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.pawn3.all_moves(self.get_piece_index(boardie,str(pre + "p3"))[0],self.get_piece_index(boardie,str(pre + "p3"))[1],boardie,board),pre+"p3"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.pawn4.all_moves(self.get_piece_index(boardie,str(pre + "p4"))[0],self.get_piece_index(boardie,str(pre + "p4"))[1],boardie,board),pre+"p4"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.pawn5.all_moves(self.get_piece_index(boardie,str(pre + "p5"))[0],self.get_piece_index(boardie,str(pre + "p5"))[1],boardie,board),pre+"p5"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.pawn6.all_moves(self.get_piece_index(boardie,str(pre + "p6"))[0],self.get_piece_index(boardie,str(pre + "p6"))[1],boardie,board),pre+"p6"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.pawn7.all_moves(self.get_piece_index(boardie,str(pre + "p7"))[0],self.get_piece_index(boardie,str(pre + "p7"))[1],boardie,board),pre+"p7"])
        except:
            print("piece not found")
        try:
            possible_move_list.append([self.pawn8.all_moves(self.get_piece_index(boardie,str(pre + "p8"))[0],self.get_piece_index(boardie,str(pre + "p8"))[1],boardie,board),pre+"p8"])
        except:
            print("piece not found")
        #no blanks
        try:
            move_r1 = self.player_rook_1.all_moves(self.get_piece_index(boardie,str(pre + "R1"))[0],self.get_piece_index(boardie,str(pre + "R1"))[1],boardie)
            if move_r1 != []:
                possible_move_list.append([move_r1,pre+"R1"])
        except TypeError:
            print("piece was killed")
        try:
            move_r2 = self.player_rook_2.all_moves(self.get_piece_index(boardie,str(pre + "R2"))[0],self.get_piece_index(boardie,str(pre + "R2"))[1],boardie)
            if move_r2 != []:
                possible_move_list.append([move_r2,pre+"R2"])
        except TypeError:
            print("piece was killed")
        try:
            move_n1 = self.player_knight_1.all_moves(self.get_piece_index(boardie,str(pre + "N1"))[0],self.get_piece_index(boardie,str(pre + "N1"))[1],boardie)
            if move_n1 != []:
                possible_move_list.append([move_n1,pre+"N1"])
        except TypeError:
            print("piece was killed")
        try:
            move_n2 = self.player_knight_2.all_moves(self.get_piece_index(boardie,str(pre + "N2"))[0],self.get_piece_index(boardie,str(pre + "N2"))[1],boardie)
            if move_n2 != []:
                possible_move_list.append([move_n2,pre+"N2"])        
        except TypeError:
            print("piece was killed")
        try:
            move_b1 = self.player_bishop_1.all_moves(self.get_piece_index(boardie,str(pre + "B1"))[0],self.get_piece_index(boardie,str(pre + "B1"))[1],boardie)
            if move_b1 != []:
                possible_move_list.append([move_b1,pre+"B1"])
        except TypeError:
            print("piece was killed")
        try:
            move_b2 = self.player_bishop_2.all_moves(self.get_piece_index(boardie,str(pre + "B2"))[0],self.get_piece_index(boardie,str(pre + "B2"))[1],boardie)
            if move_b2 != []:
                possible_move_list.append([move_b2,pre+"B2"])
        except TypeError:
            print("piece was killed")
        try:
            move_q = self.player_queen.all_moves(self.get_piece_index(boardie,str(pre + "Q"))[0],self.get_piece_index(boardie,str(pre + "Q"))[1],boardie)
            if move_q != []:
                possible_move_list.append([move_q,pre+"Q"])
        except TypeError:
            print("piece was killed")
        #possible_move_list.append(self.player_king.all_moves(self.get_piece_index(board,str(pre + "K"))[0],self.get_piece_index(board,str(pre + "K"))[1],boardie))
        try:
            move_p1 = self.pawn1.all_moves(self.get_piece_index(boardie,str(pre + "p1"))[0],self.get_piece_index(boardie,str(pre + "p1"))[1],boardie)
            if move_p1 != []:
                possible_move_list.append([move_p1,pre+"p1"])
        except TypeError:
            print("piece was killed")
                
                
                
        try:    
            move_p2 = self.pawn2.all_moves(self.get_piece_index(boardie,str(pre + "p2"))[0],self.get_piece_index(boardie,str(pre + "p2"))[1],boardie)
            if move_p2 != []:
                possible_move_list.append([move_p2,pre+"p2"])
        except TypeError:
            print("piece was killed")
        
        
        try:
            move_p3 = self.pawn3.all_moves(self.get_piece_index(boardie,str(pre + "p3"))[0],self.get_piece_index(boardie,str(pre + "p3"))[1],boardie)
            if move_p3 != []:
                possible_move_list.append([move_p3,pre+"p3"])
        except TypeError:
            print("piece was killed")
        try:
            move_p4 = self.pawn4.all_moves(self.get_piece_index(boardie,str(pre + "p4"))[0],self.get_piece_index(boardie,str(pre + "p4"))[1],boardie)
            if move_p4 != []:
                possible_move_list.append([move_p4,pre+"p4"])
        except TypeError:
            print("piece was killed")
        
        try:
            move_p5 = self.pawn5.all_moves(self.get_piece_index(boardie,str(pre + "p5"))[0],self.get_piece_index(boardie,str(pre + "p5"))[1],boardie)
            if move_p5 != []:
                possible_move_list.append([move_p5,pre+"p5"])
        except TypeError:
            print("piece was killed")
        try:
            move_p6 = self.pawn6.all_moves(self.get_piece_index(boardie,str(pre + "p6"))[0],self.get_piece_index(boardie,str(pre + "p6"))[1],boardie)
            if move_p6 != []:
                possible_move_list.append([move_p6,pre+"p6"])
        except TypeError:
            print("piece was killed")
        try:
            move_p7 = self.pawn7.all_moves(self.get_piece_index(boardie,str(pre + "p7"))[0],self.get_piece_index(boardie,str(pre + "p7"))[1],boardie)
            if move_p7 != []:
                possible_move_list.append([move_p7,pre+"p7"])
        except TypeError:
            print("piece was killed")
        try:
            move_p8 = self.pawn8.all_moves(self.get_piece_index(boardie,str(pre + "p8"))[0],self.get_piece_index(boardie,str(pre + "p8"))[1],boardie)
            if move_p8 != []:
                possible_move_list.append([move_p8,pre+"p8"])
        except TypeError:
            print("piece was killed")
        
        return possible_move_list
                        
    def get_random_move(self,boardie,board):
        possible_move_list = self.find_all_moves(boardie,board)
        length = len(possible_move_list)
        num1 = random.randint(0,length - 1)
        move = random.choice(possible_move_list[num1][0])
        piece = possible_move_list[num1][1]
        """
        print("these are possible moves: ",possible_move_list)
        print("5,6 and 6,5 respectively: {}, {}".format(boardie[5][6], boardie[6][5]))
        move = possible_move_list[0][0]
        piece = possible_move_list[0][1]
        """
        
        
        print("chosen move is {}, piece is {}".format(move,piece))
        """
        try:
            move = random.choice(sublist)
        except TypeError:
            
            move = random.choice(sublist)
            #chsange this
        print("this is the selected move: ",move)
        """
        return move,piece
                        
    def access_to_move(self,name,m1,n1,m2,n2,board,big_board):
        print("trying to access move")
        if name[0] == "b":
            print("black piece")
            if name[0:2] == "bR":
                print("moving rook")
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_rook_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_rook_1.move(m1,n1,m2,n2,board)
                    
            elif name[0:2] == "bN":
                print("trying to move knight")
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_knight_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_knight_2.move(m1,n1,m2,n2,board)
                    
            elif name[0:2] == "bB":
                print("trying to move bishop")
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_bishop_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_bishop_1.move(m1,n1,m2,n2,board)
                    
            elif name == "bQ":
                return self.player_queen.move(m1,n1,m2,n2,board)
            elif name == "bK":
                return self.player_king.move(m1,n1,m2,n2,board)
            elif name[0:2] == "bp":
                print("moving black pawn")
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.pawn1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.pawn2.move(m1,n1,m2,n2,board)
                elif piece_num == 3:
                    return self.pawn3.move(m1,n1,m2,n2,board)
                elif piece_num == 4:
                    return self.pawn4.move(m1,n1,m2,n2,board)
                elif piece_num == 5:
                    return self.pawn5.move(m1,n1,m2,n2,board)
                elif piece_num == 6:
                    return self.pawn6.move(m1,n1,m2,n2,board)
                elif piece_num == 7:
                    return self.pawn7.move(m1,n1,m2,n2,board)
                elif piece_num == 8:
                    return self.pawn8.move(m1,n1,m2,n2,board)
                    
        elif name[0] == "w":
            if name[0:2] == "wR":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_rook_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_rook_1.move(m1,n1,m2,n2,board)
                print("moving rook")
            elif name[0:2] == "wN":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_knight_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_knight_1.move(m1,n1,m2,n2,board)
                    
            elif name[0:2] == "wB":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_bishop_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_bishop_1.move(m1,n1,m2,n2,board)
                    
            elif name == "wQ":
                return self.player_queen.move(m1,n1,m2,n2,board)
            elif name == "wK":
                return self.player_king.move(m1,n1,m2,n2,big_board)
                
            elif name[0:2] == "wp":
                print("trying to move pawn")
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.pawn1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.pawn2.move(m1,n1,m2,n2,board)
                elif piece_num == 3:
                    return self.pawn3.move(m1,n1,m2,n2,board)
                elif piece_num == 4:
                    return self.pawn4.move(m1,n1,m2,n2,board)
                elif piece_num == 5:
                    return self.pawn5.move(m1,n1,m2,n2,board)
                elif piece_num == 6:
                    return self.pawn6.move(m1,n1,m2,n2,board)
                elif piece_num == 7:
                    return self.pawn7.move(m1,n1,m2,n2,board)
                elif piece_num == 8:
                    return self.pawn8.move(m1,n1,m2,n2,board)                
    #update user points once a kill has been made
    def update_points(cls,num):
        cls.points += num
        print("points are now:",cls.points)
        return cls.points
            