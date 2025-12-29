class Move_handler():

    def __init__(self):
        self._move_history = []
        self._pgn_moves = ""
        self._white_moves_history = []
        self._black_moves_history = []

        # converting to algebraic chess notation
        self.conversions1 = {0: "a",
                             1: "b",
                             2: "c",
                             3: "d",
                             4: "e",
                             5: "f",
                             6: "g",
                             7: "h"}

        self.conversions2 = {0: 8,
                             1: 7,
                             2: 6,
                             3: 5,
                             4: 4,
                             5: 3,
                             6: 2,
                             7: 1}

    def pgn_notation(self, m1, n1, m2, n2, piece, move_no):
        new_piece = ""
        new_start = str(self.conversions1.get(n1)) + str(self.conversions2.get(m1))
        new_end = str(self.conversions1.get(n2)) + str(self.conversions2.get(m2))

        if piece[0] == "b":
            if piece[1] == "p":
                new_piece = ""
            new_piece = str(piece[1]).upper()
        else:
            new_piece = str(piece[1])

        self.pgn = str(move_no) + "." + str(new_piece + new_start + new_end + " ")
        print("self.pgn is", self.pgn)
        self._pgn_moves += self.pgn
        return self._pgn_moves
    def get_pgn(self):
        return self.pgn

    def inidiv_move(self, move, current_board, piece, killed):
        board_fen = self.fen_conversions(move, piece, killed)

    def game_outcome(self, player, board, game):
        pass

    def add_to_history(self, player_colour, num, m1, n1, m2, n2):
        new_start = str(self.conversions1.get(m1)) + str(self.conversions2.get(n1))
        new_end = str(self.conversions1.get(m2)) + str(self.conversions2.get(n2))

        if player_colour == "white":
            self._white_moves_history.append([num, new_start, new_end])
            # player.add_history(self._white_moves_history)
        elif player_colour == "black":
            self._black_moves_history.append([num, new_start, new_end])
            # player.add_history(self._black_moves_history)

    def fen_conversion(self,orig_board,curr_colour,castling_rights,en_passant,halfmove_clock,fullmove_number):
        print("here")
        self.__this_board = [["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""]]
        first_board = orig_board
        self.colour = curr_colour[0]
        self.castling_rights = castling_rights
        self.en_passant = en_passant
        self.fullmove_number = fullmove_number
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        slash = "/"
        w_piece = ["B", "Q", "P", "R", "N", "K"]
        starting = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        b_piece = ["b", "q", "p", "r", "n", "k"]
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        slash = "/"
        # default castling, en passant
        # two dashes means: no castling permissions, possibility of en passant capture
        # if en passant is possible - include target square
        # if castling is possible - include K or Q, or k or q (king or queen side)
        default = "- - 0 1"
        fen_rows = []
        for x in range(8):
            for y in range(8):
                if first_board[x][y] != " " and first_board[x][y] != "" and first_board[x][y] != " ":
                    if str(first_board[x][y])[0] == "w":
                        p = str(first_board[x][y])[1]
                        p = p.upper()
                        self.__this_board[x][y] = p
                    else:
                        print(first_board[x][y])
                        p = str(first_board[x][y])[1].lower()
                        self.__this_board[x][y] = p
        print("this board is: ",self.__this_board)
        fen_rows = []
        for rank in self.__this_board:  # rank is each of the 8 rows of the board matrix
            empty = 0
            fen_rank = ""
            count = 0
            for square in rank:
                if square == ' ' or square == "" or square == " ":
                    empty += 1
                else:
                    if empty > 0:
                        fen_rank += str(empty)
                        empty = 0
                    try:
                        if fen_rank[len(fen_rank) -1].isdigit() == True:
                            count += int(fen_rank[len(fen_rank) -1])
                        else:
                            count += 1
                        fen_rank += square
                    except:
                        fen_rank += square
                        print("error")

            if empty > 0:
                fen_rank += str(empty)
            """
            if count < 8:
                print(fen_rank,count)
                to_add = 8 - count
                fen_rank += str(to_add)
                count += to_add
                print(fen_rank,count)
            """
            fen_rows.append(fen_rank)

        # Join to form the FEN string
        fen_string = f"{'/'.join(fen_rows)} {curr_colour} {castling_rights} {en_passant} {halfmove_clock} {fullmove_number}"
        print("Generated FEN:", fen_string)

        return fen_string

    #return f"{slash.join(fen_rows)} {self.colour} {self.castling_rights} {"-"} {"0"} {self.fullmove_number}" #using BNF syntax style production rule to join all the parts together

    def fen_conversions_invalid(self, board):
        fen_string = ""
        if board == 0:
            fen_string = starting
        else:
            for x in range(8):
                substring = ""
                for y in range(8):
                    if board[x][y] != " ":
                        if str(board[x][y])[0] == "w":
                            p = str(board[x][y])[1]
                        else:
                            print(board[x][y])
                            p = str(board[x][y])[1].lower()
                        substring += str(y + 1) + p
                if x != 7:
                    if substring == "":
                        substring = "8"
                    fen_string += substring + slash
                else:
                    if substring == "":
                        substring = "8"
                    fen_string += substring
        additional = ""
        if mode == "beginner":
            additional = default
        else:
            print("need to add castling permissions, en passant possiblity")
        fen_string += " " + curr_player
        fen_string += additional

        return fen_string

    def get_all_moves(self, m1, n1, board, piece, player):
        valid_moves = player.get_all_valid_moves(m1, n1, board, piece)
        print("valid moves from this move: ", valid_moves)

    def add_move_to_db(self, old_loc, new_loc, piece, board, killed, player):
        #fen_board = self.fen_conversion(board,curr_colour,castling_rights,en_passant=None,halfmove_clock=None,fullmove_number)
        m1 = old_loc[0]
        n1 = old_loc[1]
        m2 = new_loc[0]
        n2 = new_loc[1]
        san = self.pgn_notation(m1, n1, m2, n2, piece)

