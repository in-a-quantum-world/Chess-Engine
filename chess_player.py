#chess players - class file
from chess_classes import chess_board, Piece, Knight, Bishop, King, Queen, Rook, Pawn
from accessing_chess_db import Person
from multipledispatch import dispatch
from chess_move_handler import Move_handler
class moves_history_stack():
    def __init__(self):
        self._moves_history = []
        for i in range(50):
            self._moves_history.append(" ")
        self._front = 49
        self._max = 50
        self._rear = 49
        
    def get_stack_moves_history(self):
        return self._moves_history
    
    def get_most_recent_move(self):
        print("most recent move was",self._moves_history[self._front + 1])
        return self._moves_history[self._front + 1]
    
    def store_game_results(self):
        #figure out how this is supposed to work!
        pass
    def auto_store_history(self):
        pass
    
    def IsFull(self):
        if self._rear == 0:
            self.auto_store_history()
            return True
        else:
            return False
    
    def IsEmpty(self):
        if self._front == 50:
            return True
        else:
            return False
        
    def add(self,item,handler):
        print("item is: ",item)
        m1 = item[0][0] 
        n1 = item[0][1]  
        m2 = item[1][0]  
        n2 = item[1][1] 
        piece = item[2]
        #handler.pgn_notation(m1,n1,m2,n2,piece)
        
        if self.IsFull() == True:
            print("Nothing can be added")
        else:
            if self.IsEmpty() == True:
                print("stack is empty")
                self._front -= 1
                self._moves_history[self._rear] = item
                #self._rear -= 1
            else:
                self._moves_history[self._front] = item
                self._front -= 1
                
            print("added")
            
class Player():
    points = 0
    #instantiate person class
    #no conficts
    @dispatch(str)
    def __init__(self, colour):
        print("arrived")
        self._colour = colour

        self.player_knight_1 = Knight(self._colour, 1)
        self.player_rook_1 = Rook(self._colour, 1)
        self.player_bishop_1 = Bishop(self._colour, 1)
        self.player_queen = Queen(self._colour)
        self.player_king = King(self._colour)

        self.player_knight_2 = Knight(self._colour, 2)
        self.player_rook_2 = Rook(self._colour, 2)
        self.player_bishop_2 = Bishop(self._colour, 2)

        self.pawn1 = Pawn(self._colour, 1)
        self.pawn2 = Pawn(self._colour, 2)
        self.pawn3 = Pawn(self._colour, 3)
        self.pawn4 = Pawn(self._colour, 4)
        self.pawn5 = Pawn(self._colour, 5)
        self.pawn6 = Pawn(self._colour, 6)
        self.pawn7 = Pawn(self._colour, 7)
        self.pawn8 = Pawn(self._colour, 8)

        # use the user id etc to isntantiate person class
    @dispatch(str,object)
    def __init__(self,colour,person):
        print("arrived")
        self.__curr_user = person
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
        
        
        #use the user id etc to isntantiate person class
        
    def colour(self):
        return self._colour
    def link_with_person(self,person):
        self.__curr_user = person
    def inst_moves_history(self):
        self._all_moves = moves_history_stack()
    
    def get_stack_moves_history(self):
        return self._all_moves.get_stack_moves_history()
    
    def get_whole_move_history(self,big_board):
        if big_board.is_game_over("x") == True:
            all_user_game_history = self._all_moves.get_stack_moves_history()
    def start_game(self,mode):
        self.__curr_user.start_game(mode)
    def get_most_recent_move(self):
        return self._all_moves.get_most_recent_move()
    #this is fed into the fen notation stuff and everything
        
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
            print("trying to move knight to see if check")
            piece_num = int(name[2:3])
            if piece_num == 1:
                move_list = opponent.player_knight_1.all_moves(m2,n2,board)
            elif piece_num == 2:
                move_list = opponent.player_knight_2.all_moves(m2,n2,board)
                
        elif name[1:2] == "B":
            print("trying to move bishop to see if check")
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
                    return self.player_rook_2.move(m1,n1,m2,n2,board)
                    
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
                return self.player_king.move(m1,n1,m2,n2,board,big_board)
            elif name[0:2] == "bp":
                print("moving black pawn")
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.pawn1.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 2:
                    return self.pawn2.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 3:
                    return self.pawn3.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 4:
                    return self.pawn4.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 5:
                    return self.pawn5.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 6:
                    return self.pawn6.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 7:
                    return self.pawn7.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 8:
                    return self.pawn8.move(m1,n1,m2,n2,board,big_board)
                    
        elif name[0] == "w":
            if name[0:2] == "wR":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_rook_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_rook_2.move(m1,n1,m2,n2,board)
                print("moving rook")
            elif name[0:2] == "wN":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_knight_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_knight_2.move(m1,n1,m2,n2,board)
                    
            elif name[0:2] == "wB":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_bishop_1.move(m1,n1,m2,n2,board)
                elif piece_num == 2:
                    return self.player_bishop_2.move(m1,n1,m2,n2,board)
                    
            elif name == "wQ":
                return self.player_queen.move(m1,n1,m2,n2,board)
            elif name == "wK":
                return self.player_king.move(m1,n1,m2,n2,big_board)
                
            elif name[0:2] == "wp":
                print("trying to move pawn")
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.pawn1.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 2:
                    return self.pawn2.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 3:
                    return self.pawn3.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 4:
                    return self.pawn4.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 5:
                    return self.pawn5.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 6:
                    return self.pawn6.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 7:
                    return self.pawn7.move(m1,n1,m2,n2,board,big_board)
                elif piece_num == 8:
                    return self.pawn8.move(m1,n1,m2,n2,board,big_board)
    #update user points once a kill has been made
    def update_points(cls,num):
        cls.points += num
        print("points are now:",cls.points)
        return cls.points
    
    def move_highlighting(self,m1,n1,piece,board):
        if str(piece)[1] == "p":
            pawn_test_obj = Pawn(str(piece)[0],str(piece)[2])
            moves_list = pawn_test_obj.all_moves(m1,n1,board)
            print("this is the moves list:",moves_list)
                
        elif str(piece)[1] == "R":
            rook_test_obj = Rook(str(piece)[0],str(piece)[2])
            moves_list = rook_test_obj.all_moves(m1,n1,board)
                
        elif str(piece)[1] == "N":
            knight_test_obj = Knight(str(piece)[0],str(piece)[2])
            moves_list = knight_test_obj.all_moves(m1,n1,board)
                
        elif str(piece)[1] == "B":
            bishop_test_obj = Bishop(str(piece)[0],str(piece)[2])
            moves_list = bishop_test_obj.all_moves(m1,n1,board)
        
        elif str(piece)[1] == "Q":
            queen_test_obj = Queen(str(piece)[0])
            moves_list = queen_test_obj.all_moves(m1,n1,board)
        
        elif str(piece)[1] == "K":
            king_test_obj = King(str(piece)[0])
            moves_list = king_test_obj.all_moves(m1,n1,board)
        
        
        return moves_list
    
    def add_history(self,board,history_tuple_list,handler,move_no):
        self._all_moves.add(history_tuple_list,handler)
        print("THIS IS history tuple list: ", history_tuple_list)
        self.m1 = history_tuple_list[0][0]
        self.n1 = history_tuple_list[0][1]
        self.m2 = history_tuple_list[1][0]
        self.n2 = history_tuple_list[1][1]
        piece = history_tuple_list[2]
        try:
            pgn_whole_thing = handler.pgn_notation(self.m1, self.n1, self.m2, self.n2, piece, move_no)
            pgn_move = handler.get_pgn()
            # fen_string = handler.fen_conversions(self,move_no, piece, board, killed)
            # self.__curr_user.store_inidiv_move_history(self, ((self.m1,self.n1),(self.m2,self.n2)), board_fen_notation, pgn_move)
        except:
            print("piece error. invalid piece")



        #return self.moves_history
    def get_piece_index(self,boardie,piece):
        self.find = piece
        n1,m1 = 0,0
        for x in range(0,8):
            for y in range(0,8):
                
                if boardie[x][y] == self.find:
                    print("x is {}, y is {}".format(x,y))
                    print("This is board[x][y]: {}, this is board[y][x]: {}".format(boardie[x][y], boardie[y][x]))
                    return x,y
    def all_moves(self,boardie):
        temp_board = chess_board()
        temp_board.new_board(boardie)
        if self._colour == "white":
            pre = "w"
        else:
            pre = "b"

        possible_move_list = []
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
            move_p1 = self.pawn1.all_moves(self.get_piece_index(boardie,str(pre + "p1"))[0],self.get_piece_index(boardie,str(pre + "p1"))[1],boardie,temp_board)
            if move_p1 != []:
                possible_move_list.append([move_p1,pre+"p1"])
        except TypeError:
            print("piece was killed")
        try:    
            move_p2 = self.pawn2.all_moves(self.get_piece_index(boardie,str(pre + "p2"))[0],self.get_piece_index(boardie,str(pre + "p2"))[1],boardie,temp_board)
            if move_p2 != []:
                possible_move_list.append([move_p2,pre+"p2"])
        except TypeError:
            print("piece was killed")
        
        
        try:
            move_p3 = self.pawn3.all_moves(self.get_piece_index(boardie,str(pre + "p3"))[0],self.get_piece_index(boardie,str(pre + "p3"))[1],boardie,temp_board)
            if move_p3 != []:
                possible_move_list.append([move_p3,pre+"p3"])
        except TypeError:
            print("piece was killed")
        try:
            move_p4 = self.pawn4.all_moves(self.get_piece_index(boardie,str(pre + "p4"))[0],self.get_piece_index(boardie,str(pre + "p4"))[1],boardie,temp_board)
            if move_p4 != []:
                possible_move_list.append([move_p4,pre+"p4"])
        except TypeError:
            print("piece was killed")
        
        try:
            move_p5 = self.pawn5.all_moves(self.get_piece_index(boardie,str(pre + "p5"))[0],self.get_piece_index(boardie,str(pre + "p5"))[1],boardie,temp_board)
            if move_p5 != []:
                possible_move_list.append([move_p5,pre+"p5"])
        except TypeError:
            print("piece was killed")
        try:
            move_p6 = self.pawn6.all_moves(self.get_piece_index(boardie,str(pre + "p6"))[0],self.get_piece_index(boardie,str(pre + "p6"))[1],boardie,temp_board)
            if move_p6 != []:
                possible_move_list.append([move_p6,pre+"p6"])
        except TypeError:
            print("piece was killed")
        try:
            move_p7 = self.pawn7.all_moves(self.get_piece_index(boardie,str(pre + "p7"))[0],self.get_piece_index(boardie,str(pre + "p7"))[1],boardie,temp_board)
            if move_p7 != []:
                possible_move_list.append([move_p7,pre+"p7"])
        except TypeError:
            print("piece was killed")
        try:
            move_p8 = self.pawn8.all_moves(self.get_piece_index(boardie,str(pre + "p8"))[0],self.get_piece_index(boardie,str(pre + "p8"))[1],boardie,temp_board)
            if move_p8 != []:
                possible_move_list.append([move_p8,pre+"p8"])
        except TypeError:
            print("piece was killed")
        
        return possible_move_list
    
    
    def get_all_valid_moves(self,m1,n1,board,piece):
        temp_board = chess_board()
        temp_board.new_board(board)
        name = str(piece)
        print("THE PIECES NAME IS",piece)
        if name[0] == "b":
            print("black piece")
            if name[0:2] == "bR":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_rook_1.all_moves(m1,n1,board)
                elif piece_num == 2:
                    return self.player_rook_1.all_moves(m1,n1,board)
                    
            elif name[0:2] == "bN":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_knight_1.all_moves(m1,n1,board)
                elif piece_num == 2:
                    return self.player_knight_2.all_moves(m1,n1,board)
                    
            elif name[0:2] == "bB":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_bishop_1.all_moves(m1,n1,board)
                elif piece_num == 2:
                    return self.player_bishop_1.all_moves(m1,n1,board)
                    
            elif name == "bQ":
                return self.player_queen.all_moves(m1,n1,board)
            elif name == "bK":
                return self.player_king.all_moves(m1,n1,board)
            elif name[0:2] == "bp":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.pawn1.all_moves(m1,n1,board,temp_board)
                elif piece_num == 2:
                    return self.pawn2.all_moves(m1,n1,board,temp_board)
                elif piece_num == 3:
                    return self.pawn3.all_moves(m1,n1,board,temp_board)
                elif piece_num == 4:
                    return self.pawn4.all_moves(m1,n1,board,temp_board)
                elif piece_num == 5:
                    return self.pawn5.all_moves(m1,n1,board,temp_board)
                elif piece_num == 6:
                    return self.pawn6.all_moves(m1,n1,board,temp_board)
                elif piece_num == 7:
                    return self.pawn7.all_moves(m1,n1,board,temp_board)
                elif piece_num == 8:
                    return self.pawn8.all_moves(m1,n1,board,temp_board)
                    
        elif name[0] == "w":
            if name[0:2] == "wR":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_rook_1.all_moves(m1,n1,board)
                elif piece_num == 2:
                    return self.player_rook_1.all_moves(m1,n1,board)
            elif name[0:2] == "wN":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_knight_1.all_moves(m1,n1,board)
                elif piece_num == 2:
                    return self.player_knight_1.all_moves(m1,n1,board)
                    
            elif name[0:2] == "wB":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.player_bishop_1.all_moves(m1,n1,board)
                elif piece_num == 2:
                    return self.player_bishop_1.all_moves(m1,n1,board)
                    
            elif name == "wQ":
                return self.player_queen.all_moves(m1,n1,board)
            elif name == "wK":
                return self.player_king.all_moves(m1,n1,board)
                
            elif name[0:2] == "wp":
                piece_num = int(name[2:3])
                if piece_num == 1:
                    return self.pawn1.all_moves(m1,n1,board,temp_board)
                elif piece_num == 2:
                    return self.pawn2.all_moves(m1,n1,board,temp_board)
                elif piece_num == 3:
                    return self.pawn3.all_moves(m1,n1,board,temp_board)
                elif piece_num == 4:
                    return self.pawn4.all_moves(m1,n1,board,temp_board)
                elif piece_num == 5:
                    return self.pawn5.all_moves(m1,n1,board,temp_board)
                elif piece_num == 6:
                    return self.pawn6.all_moves(m1,n1,board,temp_board)
                elif piece_num == 7:
                    return self.pawn7.all_moves(m1,n1,board,temp_board)
                elif piece_num == 8:
                    return self.pawn8.all_moves(m1,n1,board,temp_board)
    def add_game_history_to_db(self,win,start_time,end_time):
        no_moves = len(self._all_moves)
        #determine what added is
        self.__curr_user.store_game_history(self._all_moves,start_time,win,no_moves)
        self.__curr_user.update_chess_info(self.added,win)
        print("added to game history")
    def update_user_info(self,points):
        self._elo_to_add = points
        self.__curr_user.update_chess_user_info(elo_to_add)
    