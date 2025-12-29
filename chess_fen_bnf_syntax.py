w_piece = ["b","q","p","r","n","k"]
nums = [1,2,3,4,5,6,7,8]
slash = "/"
b_piece = ["B","Q","P","R","N","K"]
starting = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

"""
<EPD> ::=  <Piece Placement>
       ' ' <Side to move>
       ' ' <Castling ability>
       ' ' <En passant target square>
      {' ' <operation>}
      
      
<Piece Placement> ::= <rank8>'/'<rank7>'/'<rank6>'/'<rank5>'/'<rank4>'/'<rank3>'/'<rank2>'/'<rank1>
<ranki>       ::= [<digit17>]<piece> {[<digit17>]<piece>} [<digit17>] | '8'
<piece>       ::= <white Piece> | <black Piece>
<digit17>     ::= '1' | '2' | '3' | '4' | '5' | '6' | '7'
<white Piece> ::= 'P' | 'N' | 'B' | 'R' | 'Q' | 'K'
<black Piece> ::= 'p' | 'n' | 'b' | 'r' | 'q' | 'k'

<Side to move> ::= {'w' | 'b'}

<Castling ability> ::= '-' | ['K'] ['Q'] ['k'] ['q'] (1..4)
"""
def fen_extras(board,piece,killed,curr_player):
    s = ""
    if curr_player.colour == "white":
        s = "b"
    else:
        s = "w"

def fen_adding(board,fen_string):
    superstring = ""
    substring = ""
    count = 0
    
    for char in fen_string:
        if char != "/":
            try:
                alpha = int(char)
                count += alpha
            except:
                count += 1
            finally:
                if count > 8:
                    if len(substring) <= 16:
                        subsubstring = ""
                        count2 = 0
                        letter_count = 0
                        consec_letters = 0
                        for c in substring:
                            if str(c) != c:
                                count2 += c
                                #if substring
                            else:
                                letter_count += 1
                                
                    substring += char
            
        else:
            superstring += substring
            substring = ""
            count = 0
    return superstring
def fen_adding2(board,fen_string):
    superstring = ""
    substring = ""
    count = 0
    for char in fen_string:
        if char != "/":
            try:
                alpha = int(char)
                count += alpha
            except:
                alpha = char
                count += 1
            finally:
                if count > 8:
                    substring2 = ""
                    for x in range(len(substring)):
                        for y in range(x,len(substring)):

                            subsub = substring[x:y]
                            subsub2 = subsub
                            for i in range(len(subsub)):
                                try:
                                    if subsub2[i].isnumeric() == True and subsub2[i+2].isnumeric() == True:
                                        subsub2 -= (subsub[i+2])
                                except:
                                    print("nah")
                        substring2 += (subsub2)
                    substring = substring2
                else:
                    substring += char
        superstring+= substring
    return superstring
def fen_conversion(board,mode,moves,curr_player):
    #decalre an acceptable format too
    w_piece = ["b","q","p","r","n","k"]
    nums = [1,2,3,4,5,6,7,8]
    slash = "/"
    #default castling, en passant
    #two dashes means: no castling permissions, possibility of en passant capture
    #if en passant is possible - include target square
    #if castling is possible - include K or Q, or k or q (king or queen side)
    default = "- - 0 1"
    b_piece = ["B","Q","P","R","N","K"]
    starting = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    fen_string = ""
    if moves == 0:
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
                    substring += p
                elif str(board[x][y])[0] == " ":
                    p = y+1
                    substring += str(p)
            if x != 7:
                #COUNT PARAMETER NEEDED TO COUNT HOW MUCH IS ALREADY IN STRING
                if substring == "12345678":
                    substring = "8"
                elif "1234" in substring:
                    substring = substring.replace("1234", "4")
                elif "123" in substring and "5678" in substring:
                    substring = substring.replace("5678","6")
                    substring = substring.replace("123", "1")
                elif "5678" in substring:
                    substring = substring.replace("5678","4")
                elif "678" in substring:
                    substring = substring.replace("678","1")
                elif "456" in substring:
                    substring = substring.replace("456","3")
                elif "234" in substring:
                    substring = substring.replace("234", "2")
                elif "456" in substring:
                    substring = substring.replace("456","3")
                else:
                    subsub = substring
                    """
                    for x in range(8):
                        for y in range(x,8):
                            try:
                                if subsub[x:y].isnumeric() == True:
                                    print("subsub is numeric and: ",subsub[x:y])

                                    minisub = subsub[y-1]
                                    print("minisub is: ",minisub)
                                    subsub.append(minisub)
                                    print("subsub is now: ",subsub)
                            except:
                                print("there was an exception")
                                break
                    substring = subsub
                """
                fen_string += substring + slash
            else:
                if substring == "":
                    substring = 8


                fen_string += substring
    additional = ""
    if mode == "beginner":
        additional = default
    else:
        print("need to add castling permissions, en passant possiblity")
    fen_string += " " + curr_player
    fen_string += additional
    
    return fen_string
   
board = [['bR1', 'bN1', 'bB1', 'bQ', 'bK', 'bB2', 'bN2', 'bR2'], ['bp1', ' ', ' ', ' ', 'bp5', 'bp6', 'bp7', 'bp8'], [' ', ' ', ' ', 'bp4', ' ', ' ', ' ', ' '], [' ', 'bp2', 'bp3', 'wp4', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'wp5', ' ', ' ', ' '], ['wp1', 'wp2', 'wp3', ' ', ' ', 'wp6', 'wp7', 'wp8'], ['wR1', 'wN1', 'wB1', 'wQ', 'wK', 'wB2', 'wN2', 'wR2']]

mode = "beginner"
curr_player = "w"
fen_string = fen_conversion(board,mode,3,curr_player)
print("fen string is: ",fen_string)
#print(fen_adding2(board,fen_string))

superstring = ""
substring = ""
count = 0

for char in fen_string:
    if char != "/":
        try:
            alpha = int(char)
            count += alpha
        except:
            count += 1
