
import numpy
import pandas
from chess_mat_determinant import det,mat_for_bishops,mat_for_pawns
from path_to_checkmate import find_sol, get_sol
import aiohttp
import asyncio
from chess_move_handler import Move_handler as mh
import numpy as np
import nest_asyncio
nest_asyncio.apply()


#retrieves API response
#converts from JSON (parsing)
async def post(data):
    url = "https://chess-api.com/v1"
    headers = {"Content-Type": "application/json"}

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.post(url, json=data, headers=headers) as response:
            return await response.json()


#asynchronous function for calling
async def main(fen_string):
    print("at main for api call")
    #fen data needs to be used for request
    #exemplar FEN strings of correct format
    fen_string1 = {"fen": "8/1P1R4/n1r2B2/3Pp3/1k4P1/6K1/Bppr1P2/2q5 w - - 0 1"}
    fen_string4 = {"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1"}
    fen_string2 = {"fen": "5k1r/2q3p1/p3p2p/1B3p1Q/n4P2/6P1/bbP2N1P/1K1RR3 w - - 0 1"}
    fen_string3 = {"fen": "7N/1b4RN/7k/6b1/KBp4p/5q2/6Q1/7n w - - 0 1"}
    fen_string5 = {"fen": "RNBQKB1R/P1PPPPPP/5N2/1P6/4p3/n7/1ppppppp/r1bqkbnr w - - 0 1"}
    response = await post(fen_string) #performing POST function (REST API)
    print(response)
    #length = len(list(response))
    #obtaining the most important parts of repsonse
    try:
        eval = response["eval"]
        winChance = response["winChance"]
        mate = response["mate"]
        centipawns = response["centipawns"]
        print("eval is",eval)
        print("win chance is",winChance)
        print("mate is",mate)
        print("centipawns is",centipawns)
        return eval, winChance, mate, centipawns
    except:
        return 0,0,0,0

#needed to use this loop originally - no longer needed
"""
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(fen_string))
"""
class Evaluator():
    #has to be instantiated when the game begins
    def __init__(self):
        self.mh = mh() #instantiating move handler
        self.P = 100
        self.N = 320
        self.B = 330
        self.R = 500
        self.Q = 900
        self.K = 20000
    def shortest_path_eval(self,board_state,piece):
        sol_list = []
        for x in range(100):
            sol_list.append(get_sol(board_state,piece)) #gets list

        length = 1000
        for z in range(len(sol_list)):
            if length > len(sol_list[z]):
                length = len(sol_list[z])
                heuristic_sol = sol_list[z]

        tracker = 0
        track_list = []
        for z in range(len(sol_list)):
            curr_score = 0
            current_sol = sol_list[z]
            for a in current_sol:
                x,y = a[0],a[1]
                if piece == "bN1":
                    start = (0, 1)
                    curr_score += self.bntable1.get_simple_score(x,y)
                elif piece == "bN2":
                    start = (0, 6)
                    curr_score += self.bntable2.get_simple_score(x,y)
                elif piece == "bR1":
                    start = (0, 0)
                    return 0
                elif piece == "bR2":
                    start = (0, 7)
                    return 0
                elif piece == "bB1":
                    start = (0, 2)
                    curr_score += self.bbtable1.get_simple_score(x,y)
                elif piece == "bB2":
                    start = (0, 5)
                    curr_score += self.bbtable2.get_simple_score(x,y)
                if piece == "wN1":
                    start = (7, 1)
                    curr_score += self.wntable1.get_simple_score(x,y)
                elif piece == "wN2":
                    start = (7, 6)
                    curr_score += self.wntable2.get_simple_score(x,y)
                elif piece == "wR1":
                    start = (7, 0)
                    return 0
                elif piece == "wR2":
                    start = (7, 7)
                    return 0
                elif piece == "wB1":
                    start = (7, 2)
                    curr_score += self.wbtable1.get_simple_score(x,y)
                elif piece == "wB2":
                    start = (7, 5)
                    curr_score += self.wbtable2.get_simple_score(x,y)
            track_list.append(curr_score)

        max_score = max(track_list)
        ind = track_list.index(max_score)
        return max_score, sol_list[ind]


    def heuristic_eval(self,board_state,move):
        piece = move[2]
        return self.shortest_path_eval(board_state,piece)
    def process_score(self):
        self._total_score = (0.025*self._winChance) + (0.5*self._eval) + (0.0025 * float(self._centipawns))
        #self._total_score = self._eval
        print("total score is",self._total_score)
        return self._total_score
    async def get_api_eval(self,fen_string):
        self._eval,self._winChance,self._mate,self._centipawns = await main(fen_string)
        print("eval is,",self._eval)
        return self.process_score()
    async def get_specific_api_stuff(self,fen_string):
        self._eval, self._winChance, self._mate, self._centipawns = await main(fen_string)
        print("eval is,", self._eval)
        print("win chance is",self._winChance)
        print("mate is",self._mate)
        print("centipawns is",self._centipawns)
        return self._eval,self._winChance,self._mate,self._centipawns
    def score(self):


        fen = self.mh.fen_conversion(board,self.active_colour[0],self.castling_rights,self.en_passant,0,self.full_move_number) #converting to fen notation
        print("fen is",fen)
        fen_string = {"fen": fen}
        eval_score = asyncio.run(self.get_api_eval(fen_string))
        return eval_score
    def store_everything(self,board,player_colour,castling_rights,en_passant_square,move_number):
        print("board is", board)
        print("active colour is", player_colour)
        print("castling rights are", castling_rights)
        print("en passant square is", en_passant_square)
        print("move number is", move_number)
        self.active_colour = player_colour[0]
        if castling_rights == None:
            self.castling_rights = "-"
        else:
            self.castling_rights = castling_rights
        self.en_passant = en_passant_square
        self.half_move_clock = "0"
        self.full_move_number = move_number
    class Queen_Table():
        def __init__(self,colour):
            self.__start_table = [[-20, -10, -10, -5, -5, -10, -10, -20],
             [-10,   0,   0,  0,  0,   0,   0, -10],
             [-10,   0,   5,  5,  5,   5,   0, -10],
              [-5,   0,   5,  5,  5,   5,   0,  -5],
              [-5,   0,   5,  5,  5,   5,   0,  -5],
             [-10,   5,   5,  5,  5,   5,   0, -10],
             [-10,   0,   5,  0,  0,   0,   0, -10],
             [-20, -10, -10,  0,  0, -10, -10, -20]]
            if colour[0] == "b":
                new_table = []
                for x in range(8):
                    new_table.append(self.__start_table[7-x])
                self.__start_table = new_table
            self.__curr_table = self.__start_table
            self.__score = 0
            #self._object = inst
        def get_eval_board(self):
            return self.__curr_table
        def get_simple_score(self,x,y):
            return self.__curr_table[x][y]
        def get_piece_index(self,boardie,piece):
            self.find = piece
            n1,m1 = 0,0
            for x in range(0,8):
                for y in range(0,8):
                    print("x is {}, y is {}".format(x,y))
                    if boardie[x][y] == self.find:
                        print("x is {}, y is {}".format(x,y))
                        return x,y
        def get(self,x,y,move_num):
            val = self.__start_table[x][y]
        def update(self,board_state):
            #compare to current board
            different = []
            for i in range(0,8):
                for j in range(0,8):
                    if board_state[i][j] != board_state[i][j]:
                        different.append([i,j,board_state[i][j]])

        def new_score(self,x2,y2):
            self.__score = self.__score + self.__curr_table[x2][y2]
            return self.__score
        def evaluate(self,piece,board,board_state):
            #moves = board.moves
            x,y = self.get_piece_index(board,piece)
            print("x is {}, y is {}".format(x,y))
            #if moves < 3:
                #print("moves less than 3")
            self.__table = self.update(piece,board,board_state)
            score = mat_for_pawns(x, y, self.get_eval_board())
            return self.new_score(x,y)
    class Pawn_Table():
        def __init__(self,num,colour):
            self.__start_table = [[0,  0,  0,  0,  0,  0,  0,  0], 
               [50, 50, 50, 50, 50, 50, 50, 50], 
               [10, 10, 20, 30, 30, 20, 10, 10], 
               [5,  5, 10, 27, 27, 10,  5,  5],
               [0,  0,  0, 25, 25,  0,  0,  0], 
               [5, -5,-10,  0,  0,-10, -5,  5], 
               [5, 10, 10,-25,-25, 10, 10,  5], 
               [0,  0,  0,  0,  0,  0,  0,  0]]
            if colour[0] == "b":
                new_table = []
                for x in range(8):
                    new_table.append(self.__start_table[7-x])
                self.__start_table = new_table
            self.__curr_table = self.__start_table
            self.__score = 0
            self._num = num
            #self._object = inst
        def get_eval_board(self):
            return self.__curr_table
        def get_simple_score(self,x,y):
            return self.__curr_table[x][y]
        def get_piece_index(self,boardie,piece):
            self.find = piece
            n1,m1 = 0,0
            for x in range(0,8):
                for y in range(0,8):
                    print("x is {}, y is {}".format(x,y))
                    if boardie[x][y] == self.find:
                        print("x is {}, y is {}".format(x,y))
                        return x,y
        def get(self,x,y,move_num):
            val = self.__start_table[x][y]
        def update(self,board_state):
            #pawn piece tbale base needs to be updated given the new board state
            #compare to current board
            different = []
            for i in range(0,8):
                for j in range(0,8):
                    if board_state[i][j] != board_state[i][j]:
                        different.append([i,j,board_state[i][j]])

            #check for valid killing of all dummy pawns after that has been moved
        def new_score(self,x2,y2):
            self.__score = self.__score + self.__curr_table[x2][y2]
            return self.__score
        def evaluate(self,piece,board,board_state):
            #moves = board.moves
            x,y = self.get_piece_index(board,piece)
            print("x is {}, y is {}".format(x,y))
            #if moves < 3:
                #print("moves less than 3")
            self.__table = self.update(piece,board,board_state)
            score = mat_for_pawns(x, y, self.get_eval_board())
            return self.new_score(x,y)

    class Knight_Table():
        def __init__(self,num,colour):

            self.__start_table = [[-50,-40,-30,-30,-30,-30,-40,-50], 
            [-40,-20,  0,  0,  0,  0,-20,-40], 
            [-30,  0, 10, 15, 15, 10,  0,-30], 
            [-30,  5, 15, 20, 20, 15,  5,-30], 
            [-30,  0, 15, 20, 20, 15,  0,-30], 
            [-30,  5, 10, 15, 15, 10,  5,-30], 
            [-40,-20,  0,  5,  5,  0,-20,-40], 
            [-50,-40,-20,-30,-30,-20,-40,-50]]
            self.num = num

        def get(self,x,y,move_num):
            val = self.__start_table[x][y]
        def get_eval_board(self):
            return self.__curr_table
        def get_simple_score(self,x,y):
            return self.__curr_table[x][y]
        def new_score(self, x2, y2):
            self.__score = self.__score + start_table[x2][y2]
            return self.__score
        def get_piece_index(self,boardie,piece):
            self.find = piece
            n1,m1 = 0,0
            for x in range(0,8):
                for y in range(0,8):
                    print("x is {}, y is {}".format(x,y))
                    if boardie[x][y] == self.find:
                        print("x is {}, y is {}".format(x,y))
                        return x,y
        def evaluate(self, piece, board, board_state):
            moves = board.moves
            x, y = self.get_piece_index(board, piece)
            if moves < 3:
                print("moves less than 3")

            else:
                self.__table = self.update(piece, board, board_state)
                score = mat_for_knight(x, y, self.get_eval_board())
                return self.new_score(x, y)
    class Bishop_Table():
        def __init__(self,num,colour):

            self.__start_table = [[-20,-10,-10,-10,-10,-10,-10,-20], 
                                 [-10,  0,  0,  0,  0,  0,  0,-10], 
                                 [-10,  0,  5, 10, 10,  5,  0,-10], 
                                 [-10,  5,  5, 10, 10,  5,  5,-10], 
                                 [-10,  0, 10, 10, 10, 10,  0,-10], 
                                 [-10, 10, 10, 10, 10, 10, 10,-10], 
                                 [-10,  5,  0,  0,  0,  0,  5,-10], 
                                 [-20,-10,-40,-10,-10,-40,-10,-20]]
           #reverse for the other colour
            if colour[0] == "w":
                new_table = []
                for x in range(8):
                    new_table.append(self.__start_table[7-x])
                self.__start_table = new_table
            self.__curr_table = self.__start_table
        def get(self,x,y):
            val = self.__start_table[x][y]
        def get_eval_board(self):
            return self.__curr_table
        def get_simple_score(self,x,y):
            return self.__curr_table[x][y]
        def get_piece_index(self,boardie,piece):
            self.find = piece
            n1,m1 = 0,0
            for x in range(0,8):
                for y in range(0,8):
                    print("x is {}, y is {}".format(x,y))
                    if boardie[x][y] == self.find:
                        print("x is {}, y is {}".format(x,y))
                        return x,y
        def update(self,board_state):
            #pawn piece tbale base needs to be updated given the new board state
            pass
        def new_score(self,x1,y1,x2,y2):
            self.__score = self.__score + start_table[x2][y2]
        def evaluate(self,board,board_state):
            moves = board.moves
            if moves < 3:
                print("moves less than 3")

            else:
                self.__table = self.update(piece, board, board_state)
                score = mat_for_bishop(x, y, self.get_eval_board())
                return self.new_score(x, y)
    #there is no piece table for queens because they are not commonly evaluated
    class King_Start_Table():
        def __init__(self,colour):

            self.__start_table = [[-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-20, -30, -30, -40, -40, -30, -30, -20],
            [-10, -20, -20, -20, -20, -20, -20, -10],  
            [20,  20,   0,   0,   0,   0,  20,  20], 
            [20,  30,  10,   0,   0,  10,  30,  20]]
            if colour[0] == "b":
                new_table = []
                for x in range(0,8):
                    new_table.append(self.__start_table[7-x])
                self.__start_table = new_table
        def get_eval_board(self):
            return self.__curr_table

    class King_End_Table():
        def __init__(self,colour):

            self.__end_table = [[-50,-40,-30,-20,-20,-30,-40,-50], 
            [-30,-20,-10, 0,  0,-10,-20,-30], 
            [-30,-10, 20, 30, 30, 20,-10,-30], 
            [-30,-10, 30, 40, 40, 30,-10,-30], 
            [-30,-10, 30, 40, 40, 30,-10,-30], 
            [-30,-10, 20, 30, 30, 20,-10,-30], 
            [-30,-30,  0,  0,  0, 0,-30,-30], 
            [-50,-30,-30,-30,-30,-30,-30,-50]]
            if colour[0] == "b":
                new_table = []
                for x in range(8):
                    new_table.append(self.__end_table[x][::-1])
                self.__end_table = new_table
        def get_eval_board(self):
            return self.__curr_table
        
    def update_table(self,piece,new_board,new_boardie):
        if piece[1:2] == "N1":
            self.knight1_table.evaluate(piece,new_board,new_boardie)
        elif piece[1:2] == "N2":
            self.knight2_table.evaluate(piece,new_board,new_boardie)
        elif piece[1:2] == "B1":
            self.bishop1_table.evaluate(piece,new_board,new_boardie)
        elif piece[1:2] == "B2":
            self.bishop2_table.evaluate(piece,new_board,new_boardie)
        #continue withthis evaluation stuff 

    def det(self,piece,new_board,new_boardie):
        print("piece is {}".format(piece))
        print(piece[1:3])
        if piece[0] == "b":
            if piece[1:3] == "N1":
                return self.bknight1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "N2":
                return self.bknight2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "B1":
                return self.bbishop1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "B2":
                return self.bbishop2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "R1":
                return self.brook1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "R2":
                return self.brook2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1] == "Q":
                return self.bqtable.evaluate(piece,new_board,new_boardie)
            elif piece[1] == "K":
                if new_board.moves > 20:
                    return self.bk_endtable.evaluate(piece,new_board,new_boardie)
                else:
                    return self.bk_starttable.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p1":
                print("ok")
                return self.bpawn1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p2":
                return self.bpawn2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p3":
                return self.bpawn3_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p4":
                return self.bpawn4_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p5":
                return self.bpawn5_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p6":
                return self.bpawn6_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p7":
                return self.bpawn7_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p8":
                return self.bpawn8_table.evaluate(piece,new_board,new_boardie)
        else:
            if piece[1:3] == "N1":
                return self.wknight1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "N2":
                return self.wknight2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "B1":
                return self.wbishop1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "B2":
                return self.wbishop2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "R1":
                return self.wrook1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "R2":
                return self.wrook2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1] == "Q":
                return self.wqtable.evaluate(piece,new_board,new_boardie) #append the queen evaluatio  method
            elif piece[1:3] == "p1":
                print("ok")
                return self.wpawn1_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p2":
                return self.wpawn2_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p3":
                return self.wpawn3_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p4":
                return self.wpawn4_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p5":
                return self.wpawn5_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p6":
                return self.wpawn6_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p7":
                return self.wpawn7_table.evaluate(piece,new_board,new_boardie)
            elif piece[1:3] == "p8":
                return self.wpawn8_table.evaluate(piece,new_board,new_boardie)
            elif piece[1] == "K":
                if new_board.moves > 20:
                    return self.wk_endtable.evaluate(piece,new_board,new_boardie)
                else:
                    return self.wk_starttable.evaluate(piece,new_board,new_boardie)
    def instantiate(self):
        #not used for rooks
        self.wptable1 = self.Pawn_Table(1,"w")
        self.wptable2 = self.Pawn_Table(2,"w")
        self.wptable3 = self.Pawn_Table(3,"w")
        self.wptable4 = self.Pawn_Table(4,"w")
        self.wptable5 = self.Pawn_Table(5,"w")
        self.wptable6 = self.Pawn_Table(6,"w")
        self.wptable7 = self.Pawn_Table(7,"w")
        self.wptable8 = self.Pawn_Table(8,"w")

        self.wbtable1 = self.Bishop_Table(1,"w")
        self.wbtable2 = self.Bishop_Table(2,"w")
        self.wntable1 = self.Knight_Table(1,"w")
        self.wntable2 = self.Knight_Table(2,"w")
        self.wk_starttable = self.King_Start_Table("w")
        self.wk_endtable = self.King_Start_Table("w")
        self.wqtable = self.Queen_Table("b")

        self.bptable1 = self.Pawn_Table(1,"b")
        self.bptable2 = self.Pawn_Table(2,"b")
        self.bptable3 = self.Pawn_Table(3,"b")
        self.bptable4 = self.Pawn_Table(4,"b")
        self.bptable5 = self.Pawn_Table(5,"b")
        self.bptable6 = self.Pawn_Table(6,"b")
        self.bptable7 = self.Pawn_Table(7,"b")
        self.bptable8 = self.Pawn_Table(8,"b")

        self.bbtable1 = self.Bishop_Table(1,"b")
        self.bbtable2 = self.Bishop_Table(2,"b")
        self.bntable1 = self.Knight_Table(1,"b")
        self.bntable2 = self.Knight_Table(2,"b")
        self.bk_starttable = self.King_Start_Table("b")
        self.bk_endtable = self.King_End_Table("b")
        self.bqtable = self.Queen_Table("b")

evie = Evaluator()
global board
board = [["bR1", "bN1", "bB1", "bQ","bK","bB2"," ","bR2"],
                        ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"],
                        [" "," "," "," "," "," "," ","bN2"],
                        [" "," "," "," "," "," "," "," "],
                        ["wp1"," "," "," ","wp5"," "," "," "],
                        [" "," "," "," "," "," "," "," "],
                        [" ","wp2","wp3","wp4","wB2","wp6","wp7","wp8"],
                        ["wR1", "wN1", "wB1", "wQ","wK"," ","wN2","wR2"]]
evie.instantiate()
#evie.det("wp1")
#print(asyncio.run(evie.score(board,"white","-","-",5))) #within the same event loop