from multipledispatch import dispatch

class chess_board():
    moves = 0
    def __init__(self):
        self._board = [["bR1", "bN1", "bB1", "bQ","bK","bB2","bN2","bR2"],
                        ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        ["wp1","wp2","wp3","wp4","wp5","wp6","wp7","wp8"],
                        ["wR1", "wN1", "wB1", "wQ","wK","wB2","wN2","wR2"]]
        self._moves = 0
        self._w_king_location = (7,4)
        self._b_king_location = (0,4)

        self._checkmate = False
        self.__game_over = False
        self.__curr_x = 0
        self.__curr_y = 0
        self._w_king_moves = 0
        self._w_rook1_moves = 0
        self._w_rook2_moves = 0
        self._b_king_moves = 0
        self._b_rook1_moves = 0
        self._b_rook2_moves = 0

        self._w_pawn1_moves = 0
        self._w_pawn2_moves = 0
        self._w_pawn3_moves = 0
        self._w_pawn4_moves = 0
        self._w_pawn5_moves = 0
        self._w_pawn6_moves = 0
        self._w_pawn7_moves = 0
        self._w_pawn8_moves = 0

        self._b_pawn1_moves = 0
        self._b_pawn2_moves = 0
        self._b_pawn3_moves = 0
        self._b_pawn4_moves = 0
        self._b_pawn5_moves = 0
        self._b_pawn6_moves = 0
        self._b_pawn7_moves = 0
        self._b_pawn8_moves = 0

        self._white_pawn_list = [self._w_pawn1_moves,self._w_pawn2_moves,self._w_pawn3_moves,self._w_pawn4_moves,self._w_pawn5_moves,self._w_pawn6_moves,self._w_pawn7_moves,self._w_pawn8_moves]
        self._black_pawn_list = [self._b_pawn1_moves,self._b_pawn2_moves,self._b_pawn3_moves,self._b_pawn4_moves,self._b_pawn5_moves,self._b_pawn6_moves, self._b_pawn7_moves,self._b_pawn8_moves]

        self._white_pawn_tuple = enumerate(self._white_pawn_list)
        self._black_pawn_tuple = enumerate(self._black_pawn_list)
        
    def game_over(self):
        self.__game_over = True
    #only used for dummy board
    def new_board(self,board):
        self._board = board
        
    def get_pos(self,piece):
        for x in range(0,8):
            for y in range(0,8):
                if self._board[x][y] == piece:
                    return x,y
                
            
    def is_checkmate(self,m2,n2):
        if self._board[m2][n2] == "bK" and self._moves % 2 == 0:
            return True
        elif self._board[m2][n2] == "wK" and self._moves % 2 == 1:
            return True
        else:
            return False
    def en_passant_valid(self,m1,n1,colour):
        enp_valid = False
        if colour == "black":
            if m1 == 3:
                for x in range(0,8):
                    if self._board[m1][x] == "wp":
                        for i in self._white_pawn_tuple:
                            if i[0] + 1 == self._board[m1][x]:
                                if i[1] == 1:
                                    if n1 == x+1 or n1 == x-1:
                                        enp_valid = True

        else:
            if m1 == 4:
                for x in self._board[m1]:
                    if x[0:1] == "bp":
                        for i in self._black_pawn_tuple:
                            if i[0] + 1 == x[2]:
                                if i[1] == 1:
                                    if n1 == x+1 or n1 == x-1:
                                        enp_valid = True
        return enp_valid
    def en_passant_poss(self,current_user_colour):
        pass
    def castling_rights(self,current_user_colour):
        if current_user_colour == "black":
            count1 = 0
            count2 = 0
            for x in range(1,4):
                if self._board[0][4 + x] == " ":
                    print(0, 4 + x, "is index for board")
                    count2 += 1

            for x in range(1, 3):
                if self._board[0][4 - x] == " ":
                    print(0, 4 - x, "is index for board")
                    count1 += 1

            if count2 == 2:
                if (self.get_pos("bK") == (0,4) and self.get_pos("bR2") == (0,7)):
                    return "b" #king side
            elif count1 == 2:
                if (self.get_pos("bK") == (0, 4) and self.get_pos("bR1") == (0, 0)):
                    return "q"#queen side

        else:
            count1 = 0
            count2 = 0
            for x in range(1, 4):
                if self._board[7][4 + x] == " ":
                    print(0, 4 + x, "is index for board")
                    count2 += 1

            for x in range(1,4):
                if self._board[7][4 - x] == " ":
                    print(7, 4 - x, "is index for board")
                    count1 += 1


            if count2 == 2:
                if (self.get_pos("wK") == (7, 4) and self.get_pos("wR2") == (7, 7)):
                    return "K"
            elif count1 == 2:
                if (self.get_pos("bK") == (7, 4) and self.get_pos("bR1") == (7, 0)):
                    return "Q"

    def castling_valid(self,colour,m1,m2,n1,n2,p1,p2):
        print("we made it?")
        if colour == "black":
            count = 0
            if self._board[m1][m2] == "bR2":
                for x in range(1,m2-3):
                    if self._board[0][4+x] == " ":
                        print(0,4+x,"is index for board")
                        count += 1
            elif self._board[m1][m2] == "bR1":
                for x in range(1,m2+3):
                    if self._board[0][4-x] == " ":
                        print(0,4-x, "is index for board")
                        count += 1

            if count == 2:
                if self._b_king_moves == 0 and self._b_rook2_moves == 0:
                    if (n1 == 0 and n2 == 6) and (p1 == 0 and p2 == 5):
                        return True
                elif self._b_king_moves == 0 and self._b_rook1_moves == 0:
                    if (n1 == 0 and n2 == 2) and (p1 == 0 and p2 == 3):
                        return True
        else:
            count = 0
            if self._board[m1][m2] == "wR1":
                for x in range(1,m2-3):
                    if self.board[7][4 + x] == " ":
                        count += 1
            elif self._board[m1][m2] == "wR2":
                for x in range(1,m2+3):
                    if self.board[7][4 - x] == " ":
                        count += 1
            if count == 2:
                if self._w_king_moves == 0 and self._w_rook2_moves == 0:
                    if (n1 == 7 and n2 == 6) and (p1 == 0 and p2 == 5):
                        return True
                elif self._w_king_moves == 0 and self._w_rook1_moves == 0:
                    if (n1 == 7 and n2 == 2) and (p1 == 0 and p2 == 3):
                        return True

    def pawn_promotion_valid(self,m1,m2):
        pass
            
    @dispatch(int,int)
    def is_game_over(self,m2,n2):
        if self.__game_over == True:
            return True
        if self.is_checkmate(m2,n2) == True:
            self.__game_over = True
        return self.__game_over
    
    
    @dispatch(str)
    def is_game_over(self,over):
        if self.__game_over == True:
            return True
        else:
            return False
        
    #methods for dummy updating, and undoing (?) or just not updating
    #CHANGE INDEXING
    def update_board(self,x,y,val):

        """
        if self.__curr_val[0] == "b":
            if self.__curr_val[1] == "R":
                if self.__curr_val[0] == "2":
                    self._b_rook2_moves += 1
                else:
                    self._b_rook1_moves += 1
            elif self.__curr_val[1] == "K":
                self._b_king_moves += 1
            else:
                for x in self._black_pawn_tuple:
                    if x[0] + 1 == int(self.__curr_val[2]):
                        x[1] += 1
        else:
            if self.__curr_val[1] == "R":
                if self.__curr_val[0] == "2":
                    self._w_rook2_moves += 1
                else:
                    self._w_rook1_moves += 1
            elif self.__curr_val[1] == "K":
                self._w_king_moves += 1
            else:
                for x in self._white_pawn_tuple:
                    if x[0] + 1 == int(self.__curr_val[2]):
                        x[1] += 1
        """
        if (val =="wK"):
            self._w_king_moves += 1
        elif (val == "wR1"):
            self._w_rook1_moves += 1
        elif (val == "wR2"):
            self._w_rook2_moves += 1
        elif (val =="bK"):
            self._b_king_moves += 1
        elif (val == "bR1"):
            self._b_rook1_moves += 1
        elif (val == "bR2"):
            self._b_rook2_moves += 1

        if (val =="wp1"):
            self._w_pawn1_moves += 1
        elif (val == "wp2"):
            self._w_pawn2_moves += 1
        elif (val == "wp3"):
            self._w_pawn3_moves += 1
        elif (val =="wp4"):
            self._w_pawn4_moves += 1
        elif (val == "wp5"):
            self._w_pawn5_moves += 1
        elif (val == "wp6"):
            self._w_pawn6_moves += 1
        elif (val == "wp7"):
            self._w_pawn7_moves += 1
        elif (val == "wp8"):
            self._w_pawn8_moves += 1


        if (val =="bp1"):
            self._b_pawn1_moves += 1
        elif (val == "bp2"):
            self._b_pawn2_moves += 1
        elif (val == "bp3"):
            self._b_pawn3_moves += 1
        elif (val =="bp4"):
            self._b_pawn4_moves += 1
        elif (val == "bp5"):
            self._b_pawn5_moves += 1
        elif (val == "wp6"):
            self._b_pawn6_moves += 1
        elif (val == "bp7"):
            self._b_pawn7_moves += 1
        elif (val == "bp8"):
            self._b_pawn8_moves += 1
        print("val is ",val)
        a,b = self.get_pos(val)
        self.__a = a
        self.__b = b
        self._board[x][y] = val
        self._board[a][b] = " "
        print("board now updated")
        self.__curr_x = x
        self.__curr_y = y
        self.__curr_val = val
        return self._board,self.__curr_x,self.__curr_y,self.__curr_val
    def better_update(self,x,y,val):
        print("board updated")
        a, b = self.get_pos(val)
        self.__a = a
        self.__b = b
        self._board[x][y] = " "
        self._board[a][b] = val
        return self._board
    def undo_recent_move(self):
        return self.better_update(self.__curr_x,self.__curr_y,self.__curr_val)
        #commit these changes
    def update_moves(self):
        self._moves += 1
        print("moves updated")
        return self._moves
    
    @property
    def moves(self):
        return self._moves
    
    def __str__(self):
        print(self._board)
        
    @property
    def board(self):
        return self._board
    
    @property
    def fifty_move_rule(self):
        if self._moves == 50:
            return True
    @property
    def three_fold(self):
        pass
    """"
    def can_castle(self,colour,rook):
        print("rook is ",rook)
        if rook[1:2] == "R1":
            if self._king_moves == 0 and self._rook1_moves == 0:
                x,y = self.get_pos(rook)
                king_piece = str(colour + "K")
                x1,y1 = self.get_pos(king_piece)
                for i in range(y,y1):
                    if self._board[x][i] != "":
                        return False
                return True
    
        elif rook[1:2] == "R2":
            if self._king_moves == 0 and self._rook2_moves == 0:
                x,y = self.get_pos(rook)
                king_piece = str(colour + "K")
                x1,y1 = self.get_pos(king_piece)
                for i in range(y1,y):
                    if self._board[x][i] != "":
                        return False
            
                return True
    """
    @property
    #request for insuff material stuff
    def insufficient_material(self):
        #using larry kaufmann's system for pawn evaluation
        piece_nums = 0
        for x in self._board:
            for y in x:
                if y != "" and y != "bK" and y != "wK":
                    if y[1] == "p":
                        if y[2] == 0 or y[2] == 7:
                            piece_nums += 0.7
                        elif y[2] == 1 or y[2] == 6:
                            piece_nums += 0.85
                        elif y[2] == 2 or y[2] == 5:
                            piece_nums += 0.95
                        else:
                            piece_nums += 1.0
                    elif y[1] == "N":
                        piece_nums += 3.2
                    elif y[1] == "B":
                        piece_nums += 3.3
                    elif y[1] == "R":
                        piece_nums += 4.5
                    elif y[1] == "Q":
                        piece_nums += 9.4
                        
        if piece_nums < 23:
            return True
        else:
            return False

class Piece():
    points = 0
    def __init__(self,colour):
        #super().__init__(colour)
        pass
    
    def move(self):
        pass
    
    def checkValid(self):
        pass
    
    def __init__(self,colour):
        super().__init__()
        self.colour = colour
        self.points = 1
        
    @classmethod
    def example(cls):
        pass
    
    
    def move(self,m1,n1,m2,n2):
        if self.checkValid(m1,m2,n1,n2) == True:
            return True
        
class Pawn(Piece):
    points = 1
    
    def __init__(self,colour,num):
        super().__init__(colour)
        self.colour = colour
        self.num = num
    
    def is_starting(self,m1,n1,m2,n2):
        if self.colour == "black" and m1 == 1:
            print("starting black pawn")
            return True
        elif self.colour == "white" and m1 == 6:
            print("starting white pawn")
            return True
        else:
            return False
    
    
    def validKill(self,m1,n1,m2,n2,board,en_passant_valid):
        print(board)
        print("piece to be killed is",board[m2][n2])
        print("piece colour is",self.colour)
        
        valid_kill = False
        
        if board[m2][n2] != " " and self.colour == "white":
            print("white pawn is trying to kill")
            if en_passant_valid == True:
                if n2 == n1 + 1 or n2 == n1 - 1:
                    valid_kill = True
            if str(board[m2][n2])[0] == "b":
                if m1 - 1 == m2 and n1 - 1 == n2:
                    print("killing piece",board[m2][n2])
                    valid_kill = True
                elif m1 - 1 == m2 and n1 + 1 == n2:
                    print("killing piece",board[m2][n2])
                    valid_kill = True
                    
        elif board[m2][n2] != " " and self.colour == "black":
            print("black pawn is trying to kill")
            if en_passant_valid == True:
                if n2 == n1 + 1 or n2 == n1 - 1:
                    valid_kill = True
            if str(board[m2][n2])[0] == "w":
                if m1 + 1 == m2 and n1 - 1 == n2:
                    print("killing piece",board[m2][n2])
                    valid_kill = True
                elif m1 + 1 == m2 and n1 + 1 == n2:
                    print("killing piece",board[m2][n2])
                    valid_kill = True    
                
        return valid_kill
    
    def checkValid(self,m1,n1,m2,n2,board):
        #m1 and m2 correspond to row number
        #n1 and n2 correspond to column number
        #to access piece: board[m1][n1]
        valid = False
        if self.colour == "black":
            if self.is_starting(m1,n1,m2,n2) == True:
                if m2 - 2 == m1 and n2 == n1:
                    if board[m2-1][n1] == " ":
                        valid = True
                elif m2 - 1 == m1 and n2 == n1:
                    valid = True
            else:
                if m2 - 1 == m1 and n2 == n1:
                    valid = True
                    
        elif self.colour == "white":
            if self.is_starting(m1,n1,m2,n2) == True:
                if m2 + 2 == m1 and n2 == n1:
                    if board[m2+1][n1] == " ":
                        valid = True
                elif m2 + 1 == m1 and n2 == n1:
                    valid = True
            else:
                if m2 + 1 == m1 and n2 == n1:
                    valid = True
                    
        if valid == True:
            print("valid move wihtout killing")
        else:
            print("m1,n1,m2,n2",m1,n1,m2,n2)
                    
        return valid
    """
    def see_is_check(self,all_moves_list,board):
        for move in all_moves_list:
            if self.colour == "white":
                if board[m1][n1] == "bK"
                    return True
            elif self.colour == "black":
                if board[m1][n1] == "wK":
                    return True
        
        return False
    """
    def list_clean_up(self,all_moves_list):
        new_moves_list = []
        for i in range(0,len(all_moves_list)):
            #print(i)
            print("checking {}".format(all_moves_list[i]))
            if all_moves_list[i][0] < 0 or all_moves_list[i][1] < 0:
                print("deleting {}".format(all_moves_list[i]))
                #del all_moves_list[i]
            else:
                new_moves_list.append(all_moves_list[i])
                print("new moves list is now",new_moves_list)
        print("post clean up: ",new_moves_list)
        return new_moves_list
    
    
    def all_moves(self,m1,n1,board,board_class): #SWAP AFTER
        en_passant_valid = False
        if board_class.en_passant_valid(m1, n1, self.colour) == True:
            en_passant_valid = True
        all_moves_list = []
        print("m1 is {},n1 is {}".format(m1,n1))
        print("the piece is",board[m1][n1])
        print("you made it to all moves")
        
        print("self.colour is...",self.colour)
        if self.colour == "black":
            print("HELLO?!?!")
            if self.is_starting(m1,n1,0,0) == True:
                print("it's a starting piece")
                try:
                    if board[m1 + 2][n1] == " ":
                        print("can do starting piece opening")
                        all_moves_list.append([m1+2,n1])
                except IndexError:
                    print("index error")
                try:
                    if board[m1 + 1][n1] == " ":
                        all_moves_list.append([m1+1,n1])
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1-1,n1+1,board,en_passant_valid) == True:
                        if en_passant_valid == False:
                            if str(board[m1 - 1][n1 + 1])[0] == "w":
                                all_moves_list.append([m1 - 1, n1 + 1])
                        else:
                            all_moves_list.append([m1 -1, n1 + 1])
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1-1,n1-1,board,en_passant_valid) == True:
                        if en_passant_valid == False:
                            if str(board[m1 - 1][n1 - 1])[0] == "w":
                                all_moves_list.append([m1- 1, n1 - 1])
                        else:
                            all_moves_list.append([m1 - 1, n1 - 1])
                except IndexError:
                    print("index error")
                    
            else:
                print("not a starting black piece")
                try:
                    print("this is the square to be checked: ",board[m1+1][n1],"and that was it")
                    print("m1+1 is {}, n1 is {}".format(m1+1,n1))
                    if board[m1+1][n1] == " ":
                        all_moves_list.append([m1+1,n1])
                        print("we made it?")
                    else:
                        print("i guess not?")
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1-1,n1+1,board,en_passant_valid) == True:
                        if str(board[m1 - 1][n1+1])[0] == "w":
                            all_moves_list.append([m1-1,n1+1])
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1-1,n1-1,board,en_passant_valid) == True:
                        if str(board[m1 - 1][n1-1])[0] == "w":
                            all_moves_list.append([m1-1,n1-1])
                except IndexError:
                    print("index error")
                
        elif self.colour == "white":
            print("so its a white piece")
            if self.is_starting(m1,n1,0,0) == True:
                try:
                    print("WHITE starting piece")
                    if board[m1-2][n1] == " ":
                        all_moves_list.append([m1-2,n1])
                except IndexError:
                    print("index error")
                try:
                    if board[m1-1][n1] == " ":
                        all_moves_list.append([m1-1,n1])
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1+1,n1+1,board,en_passant_valid) == True:
                        if en_passant_valid == False:
                            if str(board[m1 + 1][n1 + 1])[0] == "b":
                                all_moves_list.append([m1 + 1, n1 + 1])
                        else:
                            all_moves_list.append([m1 + 1, n1 + 1])
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1-1,n1+1,board,en_passant_valid) == True:
                        if en_passant_valid == False:
                            if str(board[m1- 1][n1+1])[0] == "b":
                                all_moves_list.append([m1- 1, n1 +1])
                        else:
                            all_moves_list.append([m1-1, n1+ 1])
                except IndexError:
                    print("index error")
                    
            else:
                try:
                    if board[m1-1][n1] == " ":
                        all_moves_list.append([m1-1,n1])
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1+1,n1+1,board,en_passant_valid) == True:
                        if en_passant_valid == False:
                            if str(board[m1 + 1][n1 + 1])[0] == "b":
                                all_moves_list.append([m1 + 1, n1 +1])
                        else:
                            all_moves_list.append([m1 + 1, n1 + 1])
                except IndexError:
                    print("index error")
                try:
                    if self.validKill(m1,n1,m1+1,n1-1,board,en_passant_valid) == True:
                        if en_passant_valid == False:
                            if str(board[m1 + 1][n1-1])[0] == "b":
                                all_moves_list.append([m1+1,n1-1])
                        else:
                            all_moves_list.append([m1 + 1, n1 - 1])
                except IndexError:
                    print("index error")
        print("all moves list: ",all_moves_list)
        
        if all_moves_list != None:
            print("now going to clean up")
            return self.list_clean_up(all_moves_list)
    
    def move(self,m1,n1,m2,n2,board,board_class):
        en_passant_valid = False
        if board_class.en_passant_valid(m1,n1,self.colour) == True:
            en_passant_valid = True
        if self.checkValid(m1,n1,m2,n2,board) == True:
            print("move is valid")
            return True
        else:
            if self.validKill(m1,n1,m2,n2,board,en_passant_valid) == True:
                return True
            else:
                print("move doesn't appear to be valid at all.")
                return False
            
    def get_points(cls):
        return points
    
class Bishop(Piece):
    points = 3
    
    def __init__(self,colour,num):
        super().__init__(colour)
        self.colour = colour
        self.num = num
        
        
    @classmethod
    def example(cls):
        pass
    
    def list_clean_up(self,all_moves_list):
        new_moves_list = []
        for i in range(0,len(all_moves_list) - 1):
            print(i)
            print("checking {}".format(all_moves_list[i]))
            if all_moves_list[i][0] < 0 or all_moves_list[i][1] < 0:
                print("deleting {}".format(all_moves_list[i]))
                #del all_moves_list[i]
            else:
                new_moves_list.append(all_moves_list[i])
        return new_moves_list
    
    def validKill(self,m1,n1,m2,n2,board):
        valid_kill = False
        if self.colour == "white" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "b":
                valid_kill = True
                        
                        
        elif self.colour == "black" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "w":
                valid_kill = True
                
                
        if valid_kill == True:
            print("killing piece",board[m2][n2])
            
        return valid_kill
    
    def no_jumps(self,m1,n1,m2,n2,board,i,state):        
        for x in range(1,i):
            if state == 1:
                print("checking",m1+x,n1+x)
                if board[m1+x][n1+x] != " ":
                    print(m1+x,n1+x,"false at state 1")
                    return False
            elif state == 2:
                print("checking",m1+x,n1-x)
                if board[m1+x][n1-x] != " ":
                    print(m1+x,n1-x,"false at state 2")
                    return False
            elif state == 3:
                print("checking",m1-x,n1+x)
                if board[m1-x][n1+x] != " ":
                    print(m1-x,n1+x,"false at state 3")
                    return False
            else:
                print("checking",m1-x,n1-x)
                if board[m1-x][n1-x] != " ":
                    print(m1-x,n1-x,"false at state 4")
                    return False
        return True

    def all_moves(self,m1,n1,board):
        all_moves_list = []
        
        for r in range(1,8):
            try:
                if board[m1+r][n1+r] == " " and self.no_jumps(m1,n1,m1+r,n1+r,board,r,1) == True:
                    all_moves_list.append([m1+r,n1+r])
                elif (str(board[m1+r][n1+r])[0] == "b" and self.colour == "white") or (str(board[m1+r][n1+r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1+r,n1+r,board,r,1) == True:
                    all_moves_list.append([m1+r,n1+r])
            except IndexError:
                print("index out of range")
            try:
                if board[m1+r][n1-r] == " " and self.no_jumps(m1,n1,m1+r,n1-r,board,r,2) == True:
                    all_moves_list.append([m1+r,n1-r])
                elif (str(board[m1+r][n1-r])[0] == "b" and self.colour == "white") or (str(board[m1+r][n1-r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1+r,n1-r,board,r,2) == True:
                    all_moves_list.append([m1+r,n1-r])
            except IndexError:
                print("index out of range")
            try:
                if board[m1 - r][n1 + r] == " " and self.no_jumps(m1,n1,m1-r,n1+r,board,r,3) == True:
                    all_moves_list.append([m1-r,n1+r])
                elif (str(board[m1-r][n1+r])[0] == "b" and self.colour == "white") or (str(board[m1-r][n1+r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1-r,n1+r,board,r,3) == True:
                    all_moves_list.append([m1-r,n1+r])
            except IndexError:
                print("index out of range")
            try:
                if board[m1-r][n1-r] == " " and self.no_jumps(m1,n1,m1-r,n1-r,board,r,4) == True:
                    all_moves_list.append([m1-r,n1-r])
                elif (str(board[m1-r][n1-r])[0] == "b" and self.colour == "white") or (str(board[m1-r][n1-r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1-r,n1-r,board,r,4) == True:
                    all_moves_list.append([m1-r,n1-r])
            except IndexError:
                print("index out of range")
        #print(all_moves_list)
        
        if all_moves_list != None:
            return self.list_clean_up(all_moves_list)
    
    def checkValid(self,m1,n1,m2,n2,board):
        print("checking valid?")
        valid = False
            
        for i in range(0,8):
            if m1 + i == m2 and n1 + i == n2:
                state = 1
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
            elif m1 + i == m2 and n1 - i == n2:
                state = 2
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
            elif m1 - i == m2 and n1 + i == n2:
                state = 3
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
            elif m1 - i == m2 and n1 - i == n2:
                state = 4
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
        return valid
            
    
    def move(self,m1,n1,m2,n2,board):
        print("made it here with bishop")
        if self.checkValid(m1,n1,m2,n2,board) == True:
            print("checked for validity")
            if self.validKill(m1,n1,m2,n2,board) == True:
                print("valid move with killing")
                return True
            else:
                print("valid move without killing")
                return True
        else:
            return False
                
    def get_points(cls):
        return points
    
class Knight(Piece):
    points = 3
    
    def __init__(self,colour,num):
        super().__init__(colour)
        self.colour = colour
        self.num = num
        
    @classmethod
    def example(cls):
        pass
    
    def list_clean_up(self,all_moves_list):
        new_moves_list = []
        for i in range(0,len(all_moves_list) - 1):
            print(i)
            print("checking {}".format(all_moves_list[i]))
            if all_moves_list[i][0] < 0 or all_moves_list[i][1] < 0:
                print("deleting {}".format(all_moves_list[i]))
                #del all_moves_list[i]
            else:
                new_moves_list.append(all_moves_list[i])
        return new_moves_list
    
    #GENERATING ALL MOVES INCLUDCES NEGATIVE MOVE INDICES

    def all_moves(self,m1,n1,board):
        all_moves_list = []
        print("SELF COLOUR IS",self.colour)
        try:
            if board[m1+2][n1+1] == " ":
                all_moves_list.append([m1+2,n1+1])
                print(board[m1+2][n1+1],"was valid without killing")
            elif (str(board[m1+2][n1+1])[0] == "b" and self.colour == "black") or (str(board[m1+2][n1+1])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1+2,n1+1])
            elif (str(board[m1+2][n1+1])[0] == "b" and self.colour == "white") or (str(board[m1+2][n1+1])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1+2,n1+1])
                print("a")
        except IndexError:
            print("index out of range")
        try:
            if board[m1 + 2][n1 - 1] == " ":
                all_moves_list.append([m1+2,n1-1])
                print(board[m1+2][n1-1],"was valid without killing")
            elif (str(board[m1+2][n1-1])[0] == "b" and self.colour == "black") or (str(board[m1+2][n1-1])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1+2,n1-1])
            elif (str(board[m1+2][n1-1])[0] == "b" and self.colour == "white") or (str(board[m1+2][n1-1])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1+2,n1-1])
                print("a")
        except IndexError:
            print("index out of range")
        try:
            if board[m1 - 2][n1 + 1] == " ":
                all_moves_list.append([m1-2,n1+1])
                print(board[m1-2][n1+1],"was valid without killing")
            elif (str(board[m1-2][n1+1])[0] == "b" and self.colour == "black") or (str(board[m1-2][n1+1])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1-2,n1+1])
            elif (str(board[m1-2][n1+1])[0] == "b" and self.colour == "white") or (str(board[m1-2][n1+1])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1-2,n1+1])
                print("a")
        except IndexError:
            print("index out of range")
        try:
            if board[m1 - 2][n1 - 1] == " ":
                all_moves_list.append([m1-2,n1-1])
                print(board[m1-2][n1-1],"was valid without killing")
            elif (str(board[m1-2][n1-1])[0] == "b" and self.colour == "black") or (str(board[m1-2][n1-1])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1-2,n1-1])
            elif (str(board[m1-2][n1-1])[0] == "b" and self.colour == "white") or (str(board[m1-2][n1-1])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1-2,n1-1])
                print("a")
        except IndexError:
            print("index out of range")
        try: 
            if board[m1+1][n1+2] == " ":
                all_moves_list.append([m1+1,n1+2])
                print(board[m1+1][n1+2],"was valid without killing")
            elif (str(board[m1+1][n1+2])[0] == "b" and self.colour == "black") or (str(board[m1+1][n1+2])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1+1,n1+2])
            elif (str(board[m1+1][n1+2])[0] == "b" and self.colour == "white") or (str(board[m1+1][n1+2])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1+1,n1+2])
                print("a")
        except IndexError:
            print("index out of range")
        try:
            if board[m1+1][n1-2] == " ":
                all_moves_list.append([m1+1,n1-2])
                print(board[m1+1][n1-2],"was valid without killing")
            elif (str(board[m1+1][n1-2])[0] == "b" and self.colour == "black") or (str(board[m1+1][n1-2])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1+1,n1-2])
            elif (str(board[m1+1][n1-2])[0] == "b" and self.colour == "white") or (str(board[m1+1][n1-2])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1+1,n1-2])
                print("a")
        except IndexError:
            print("index out of range")
        try:
            if board[m1 - 1][n1 + 2] == " ":
                all_moves_list.append([m1-1,n1+2])
                print(board[m1-1][n1+2],"was valid without killing")
            elif (str(board[m1-1][n1+2])[0] == "b" and self.colour == "black") or (str(board[m1-1][n1+2])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1-1,n1+2])
            elif (str(board[m1-1][n1+2])[0] == "b" and self.colour == "white") or (str(board[m1-1][n1+2])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1-1,n1+2])
                print("a")
        except IndexError:
            print("index out of range")
        try:
            if board[m1 - 1][n1 - 2] == " ":
                all_moves_list.append([m1-1,n1-2])
                print(board[m1-1][n1-2],"was valid without killing")
            elif (str(board[m1-1][n1-2])[0] == "b" and self.colour == "black") or (str(board[m1-1][n1-2])[0] == "w" and self.colour == "white"):
                print("that's a friendly piece")
                #all_moves_list.append([m1-1,n1-2])
            elif (str(board[m1-1][n1-2])[0] == "b" and self.colour == "white") or (str(board[m1-1][n1-2])[0] == "w" and self.colour == "black"):
                all_moves_list.append([m1-1,n1-2])
                print("a")
        except IndexError:
            print("index out of range")
        print("all moves list for knight: ",all_moves_list)
        
        if all_moves_list != None:
            return self.list_clean_up(all_moves_list)
                
    def validKill(self,m1,n1,m2,n2,board):
        valid_kill = False
        if self.colour == "white" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "b":
                valid_kill = True
                    
        elif self.colour == "black" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "w":
                valid_kill = True
                
        print("Killing piece",board[m2][n2])
        return valid_kill

                
    def checkValid(self,m1,n1,m2,n2):
        valid = False
        if m1 + 2 == m2 and n1 + 1 == n2:
            valid = True
        elif m1 + 2 == m2 and n1 - 1 == n2:
            valid = True
        elif m1 - 2 == m2 and n1 + 1 == n2:
            valid = True
        elif m1 - 2 == m2 and n1 - 1 == n2:
            valid = True
        elif m1 + 1 == m2 and n1 + 2 == n2:
            valid = True
        elif m1 + 1 == m2 and n1 - 2 == n2:
            valid = True 
        elif m1 - 1 == m2 and n1 + 2 == n2:
            valid = True
        elif m1 - 1 == m2 and n1 - 2 == n2:
            valid = True 
        
        return valid  
        
    
    def move(self,m1,n1,m2,n2,board):
        if self.checkValid(m1,n1,m2,n2) == True:
            if self.validKill(m1,n1,m2,n2,board) == True:
                print("valid move with killing")
                return True
            else:
                print("valid move without killing")
                return True
        else:
            return False
    def get_points(cls):
        return points
    
class King(Piece):
    
    def __init__(self,colour):
        super().__init__(colour)
        self.colour = colour
        self.checkmate = False
        
    @classmethod
    def example(cls):
        pass
        
    def list_clean_up(self,all_moves_list):
        new_moves_list = []
        for i in range(0,len(all_moves_list) - 1):
            print(i)
            print("checking {}".format(all_moves_list[i]))
            if all_moves_list[i][0] < 0 or all_moves_list[i][1] < 0:
                print("deleting {}".format(all_moves_list[i]))
                #del all_moves_list[i]
            else:
                new_moves_list.append(all_moves_list[i])
        return new_moves_list
    
    def all_moves(self,colour,num,boardie,board):
        moves = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                #to see if it is black's or white's turn
                turn = str(board[r][c])[0]
                if (turn == "w" and board.moves % 2 == 0) or (turn == "b" and board.moves % 2 == 1):
                    piece = self.board[r][c][1]
        
        if moves != None:
            return self.list_clean_up(moves)
        
    def is_check(self,m1,n1,m2,n2,board):
        if board.moves % 2 == 0:
            oppMoves = [] #get all moves for opponent's pieces to see if player's king in check
            for move in oppMoves:
                break
                
    
    def checkValid(self,m1,n1,m2,n2,board):
        if self.is_check(m1,n1,m2,n2,board) == True:
            if m1 == m2 + 1 and n1 == n2:
                return True
            elif m1 == m2 - 1 and n1 == n2:
                return True
            elif m1 == m2 + 1 and n1 == n2 + 1:
                return True
            elif m1 == m2 - 1 and n1 == n2 - 1:
                return True
            elif m1 == m2 and n1 == n2 + 1:
                return True
            elif m1 == m2 and n1 == n2 - 1:
                return True
            else:
                return False
    #can only move when in check
    #can only move in a way that kills a piece if necessary
    #one square at a time otherwise
    
    
    def move(self,m1,n1,m2,n2,board,big_board):
        if self.checkValid(m1,n1,m2,n2,big_board) == True:
            if self.colour == "white":
                self._w_king_location = (m2, n2)
            elif self.colour == "black":
                self._b_king_location = (m2, n2)
            #if self.validKill(m1,n1,m2,n2,big_board) == True:
             #   return True
            return True

        
    def castling(self):
        pass
        
class Queen(Piece):
    points = 9
    
    def __init__(self,colour):
        super().__init__(colour)
        self.colour = colour
        
    @classmethod
    def example(cls):
        pass
    def list_clean_up(self,all_moves_list):
        new_moves_list = []
        for i in range(0,len(all_moves_list) - 1):
            print(i)
            print("checking {}".format(all_moves_list[i]))
            if all_moves_list[i][0] < 0 or all_moves_list[i][1] < 0:
                print("deleting {}".format(all_moves_list[i]))
                #del all_moves_list[i]
            else:
                new_moves_list.append(all_moves_list[i])
        return new_moves_list
    
    def no_jumps(self,m1,n1,m2,n2,board,i,state):        
        for x in range(1,i+1):
            if state == 1:
                if board[m1+x][n1+x] != " ":
                    return False
            elif state == 2:
                if board[m1+x][n1-x] != " ":
                    return False
            elif state == 3:
                if board[m1-x][n1+x] != " ":
                    return False
            elif state == 4:
                if board[m1-x][n1-x] != " ":
                    return False
            elif state == 5:
                if board[m1+x][n1] != " ":
                    return False
            elif state == 6:
                if board[m1-x][n1] != " ":
                    return False
            elif state == 7:
                if board[m1][n1+x] != " ":
                    return False
            elif state == 8:
                if board[m1][n1-x] != " ":
                    return False
                
        return True
    def all_moves(self,m1,n1,board):
        all_moves_list = []
        
        for r in range(1,8):
            try:
                if board[m1+r][n1+r] == " " and self.no_jumps(m1,n1,m1+r,n1+r,board,r,1) == True:
                    all_moves_list.append([m1+r,n1+r])
                elif (str(board[m1+r][n1+r])[0] == "b" and self.colour == "white") or (str(board[m1+r][n1+r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1+r,n1+r,board,r,1) == True:
                    all_moves_list.append([m1+r,n1+r])
            except IndexError:
                print("index out of range")
            try:
                if board[m1+r][n1-r] == " " and self.no_jumps(m1,n1,m1+r,n1-r,board,r,2) == True:
                    all_moves_list.append([m1+r,n1-r])
                elif (str(board[m1+r][n1-r])[0] == "b" and self.colour == "white") or (str(board[m1+r][n1-r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1+r,n1-r,board,r,2) == True:
                    all_moves_list.append([m1+r,n1-r])
            except IndexError:
                print("index out of range")
            try:
                if board[m1 - r][n1 + r] == " " and self.no_jumps(m1,n1,m1-r,n1+r,board,r,3) == True:
                    all_moves_list.append([m1-r,n1+r])
                elif (str(board[m1-r][n1+r])[0] == "b" and self.colour == "white") or (str(board[m1-r][n1+r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1-r,n1+r,board,r,3) == True:
                    all_moves_list.append([m1-r,n1+r])
            except IndexError:
                print("index out of range")
            try:
                if board[m1-r][n1-r] == " " and self.no_jumps(m1,n1,m1-r,n1-r,board,r,4) == True:
                    all_moves_list.append([m1-r,n1-r])
                elif (str(board[m1-r][n1-r])[0] == "b" and self.colour == "white") or (str(board[m1-r][n1-r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1-r,n1-r,board,r,4) == True:
                    all_moves_list.append([m1-r,n1-r])
                    
            except IndexError:
                print("index out of range")
            
            for r in range(1,8):
                try:
                    if board[m1+r][n1] == " " and self.no_jumps(m1,n1,m1+r,n1,board,r,5) == True:
                        all_moves_list.append([m1+r,n1])
                    elif (str(board[m1+r][n1])[0] == "b" and self.colour == "white") or (str(board[m1+r][n1])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1+r,n1,board,r,5) == True:
                        all_moves_list.append([m1+r,n1])
                except IndexError:
                    print("index out of range")
                try:
                    if board[m1][n1-r] == " " and self.no_jumps(m1,n1,m1,n1-r,board,r,8) == True:
                        all_moves_list.append([m1+r,n1-r])
                    elif (str(board[m1][n1-r])[0] == "b" and self.colour == "white") or (str(board[m1][n1-r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1,n1-r,board,r,8) == True:
                        all_moves_list.append([m1,n1-r])
                except IndexError:
                    print("index out of range")
                try:   
                    if board[m1][n1 + r] == " " and self.no_jumps(m1,n1,m1,n1+r,board,r,7) == True:
                        all_moves_list.append([m1,n1+r])
                    elif (str(board[m1][n1+r])[0] == "b" and self.colour == "white") or (str(board[m1][n1+r])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1,n1-r,board,r,6) == True:
                        all_moves_list.append([m1,n1+r])
                except IndexError:
                    print("index out of range")
                try:
                    if board[m1-r][n1] == " " and self.no_jumps(m1,n1,m1-r,n1,board,r,6) == True:
                        all_moves_list.append([m1-r,n1])
                    elif (str(board[m1-r][n1])[0] == "b" and self.colour == "white") or (str(board[m1-r][n1])[0] == "w" and self.colour == "black") and self.no_jumps(m1,n1,m1-r,n1,board,r,6) == True:
                        all_moves_list.append([m1-r,n1])
                        
                except IndexError:
                    print("index out of range")
        print("all moves list for queen: ",all_moves_list)          
        if all_moves_list != None:
            return self.list_clean_up(all_moves_list)
        
        
    def validKill(self,m1,n1,m2,n2,board):
        valid_kill = False
        if self.colour == "white" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "b":
                valid_kill = True
                    
        elif self.colour == "black" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "w":
                valid_kill = True
                
        print("Killing piece",board[m2][n2])
        return valid_kill
    
    def checkValid(self,m1,n1,m2,n2,board):
        #moving diagonally
        valid = False
        for i in range(0,8):
            if m1 + i == m2 and n1 + i == n2:
                state = 1
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
            elif m1 + i == m2 and n1 - i == n2:
                state = 2
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
            elif m1 - i == m2 and n1 + i == n2:
                state = 3
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
            elif m1 - i == m2 and n1 - i == n2:
                state = 4
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
        #moving normally
        for j in range(0,8):
            if m1 + j == m2 and n1 == n2:
                state = 5
                if self.no_jumps(m1,n1,m2,n2,board,j,state) == True:
                    valid = True
            elif m1 - j == m2 and n1 == n2:
                state = 6
                if self.no_jumps(m1,n1,m2,n2,board,j,state) == True:
                    valid = True
            elif m1 == m2 and n1 + j == n2:
                state = 7
                if self.no_jumps(m1,n1,m2,n2,board,j,state) == True:
                    valid = True
            elif m1 == m2 and n1 - j == n2:
                state = 8
                if self.no_jumps(m1,n1,m2,n2,board,i,state) == True:
                    valid = True
                
        return valid   
                
                
                
    def move(self,m1,n1,m2,n2,board):
        if self.checkValid(m1,n1,m2,n2,board) == True:
            if self.validKill(m1,n1,m2,n2,board) == True:
                return True
            else:
                print("valid without killing")
                return True
        else:
            return False
    def get_points(cls):
        return points
    
class Rook(Piece):
    points = 5
    
    def __init__(self,colour,num):
        super().__init__(colour)
        self.colour = colour
        self.num = num
        
    @classmethod
    def example(cls):
        pass
    
    def list_clean_up(self,all_moves_list):
        new_moves_list = []
        for i in range(0,len(all_moves_list) - 1):
            print(i)
            print("checking {}".format(all_moves_list[i]))
            if all_moves_list[i][0] < 0 or all_moves_list[i][1] < 0:
                print("deleting {}".format(all_moves_list[i]))
                #del all_moves_list[i]
            else:
                new_moves_list.append(all_moves_list[i])
        return new_moves_list
    
    def validKill(self,m1,n1,m2,n2,board):
        valid_kill = False
        if self.colour == "white" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "b":
                valid_kill = True                        
                        
        elif self.colour == "black" and board[m2][n2] != " ":
            if str(board[m2][n2])[0] == "w":
               valid_kill = True
               
        print("killing piece",board[m2][n2])
        return valid_kill
    
    #this function isn't working
    def no_jumps(self,m1,n1,m2,n2,board,a,state):
        print(board)
        for x in range(1,a+1):
            if state == 1:
                print("this is:",board[m1+x][n1])
                if board[m1+x][n1] != " ":
                    print("failed at state 1")
                    return False
            elif state == 2:
                print("this is:",board[m1][n1+x])
                if board[m1][n1+x] != " ":
                    print("failed at state 2")
                    return False
            elif state == 3:
                print("this is:",board[m1-x][n1])
                if board[m1-x][n1] != " ":
                    print("failed at state 3")
                    return False
            elif state == 4:
                print("this is:",board[m1][n1-x])
                if board[m1][n1-x] != " ":
                    print("failed at state 4")
                    return False
        return True
        #remove repeats from the list, remove negative pairs of
    def all_moves(self,m1,n1,board):
        all_moves_list = []
        
        for r in range(1,8):
            try:
                print("for state 1: {},r is {} ".format(board[m1+r][n1],r))
                if board[m1+r][n1] == " " and self.no_jumps(m1,n1,m1+r,n1,board,r,1) == True:
                    all_moves_list.append([m1+r,n1])
                elif ((str(board[m1+r][n1])[0] == "b" and self.colour == "white") or (str(board[m1+r][n1])[0] == "w" and self.colour == "black")) and self.no_jumps(m1,n1,m1+r,n1,board,r,1) == True:
                    all_moves_list.append([m1+r,n1])
            except IndexError:
                print("index out of range")
            try:
                print("for state 4: {},r is {} ".format(board[m1][n1-r],r))
                if board[m1][n1-r] == " " and self.no_jumps(m1,n1,m1,n1-r,board,r,4) == True:
                    all_moves_list.append([m1,n1-r])
                elif ((str(board[m1][n1-r])[0] == "b" and self.colour == "white") or (str(board[m1][n1-r])[0] == "w" and self.colour == "black")) and self.no_jumps(m1,n1,m1,n1-r,board,r,4) == True:
                    all_moves_list.append([m1,n1-r])
            except IndexError:
                print("index out of range")
            try:
                print("for state 2: {},r is {} ".format(board[m1][n1+r],r))
                if board[m1][n1 + r] == " " and self.no_jumps(m1,n1,m1,n1+r,board,r,2) == True:
                    all_moves_list.append([m1,n1+r])
                elif ((str(board[m1][n1+r])[0] == "b" and self.colour == "white") or (str(board[m1][n1+r])[0] == "w" and self.colour == "black")) and self.no_jumps(m1,n1,m1,n1+r,board,r,2) == True:
                    all_moves_list.append([m1,n1+r])
            except IndexError:
                print("index out of range")
            try:
                print("for state 3: {},r is {} ".format(board[m1-r][n1],r))
                if board[m1-r][n1] == " " and self.no_jumps(m1,n1,m1-r,n1,board,r,3) == True:
                    all_moves_list.append([m1-r,n1])
                if ((str(board[m1-r][n1])[0] == "b" and self.colour == "white") or (str(board[m1-r][n1])[0] == "w" and self.colour == "black")) and self.no_jumps(m1,n1,m1-r,n1,board,r,3) == True:
                    all_moves_list.append([m1-r,n1])
                    
            except IndexError:
                print("index out of range")
        print("all moves for rook:",all_moves_list)
        if all_moves_list != None:
            return self.list_clean_up(all_moves_list)
        
    def checkValid(self,m1,n1,m2,n2,board):
        valid = False
        for a in range(0,8):
            if m1 + a == m2 and n1 == n2:
                print("state 1")
                state = 1
                if self.no_jumps(m1,n1,m2,n2,board,a,state) == True:
                    valid = True
            elif m1 == m2 and n1 + a == n2:
                state = 2
                print("state 2")
                if self.no_jumps(m1,n1,m2,n2,board,a,state) == True:
                    valid = True
            elif m1 - a == m2 and n1 == n2:
                state = 3
                print("state 3")
                if self.no_jumps(m1,n1,m2,n2,board,a,state) == True:
                    valid = True
            elif m1 == m2 and n1 - a == n2:
                state = 4
                print("state 4")
                if self.no_jumps(m1,n1,m2,n2,board,a,state) == True:
                    valid = True
        return valid 

    def move(self,m1,n1,m2,n2,board):
        if self.checkValid(m1,n1,m2,n2,board) == True:
            if self.validKill(m1,n1,m2,n2,board) == True:
                print("valid move with killing")
                return True
            else:
                print("valid move")
                return True
        else:
            return False
            
    
    def castling(self):
        pass 
    def get_points(cls):
        return points