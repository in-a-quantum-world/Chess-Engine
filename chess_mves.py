#chess moves tree
import random
from chess_classes import chess_board
from chess_player import Player
from chess_mcts import MCTS, Minmaxer
from chess_evaluator import Evaluator
from chess_move_handler import Move_handler
import numpy as np

global evie
evie = Evaluator()
evie.instantiate()
def go_to_mcts(user1,user2,orig_board_class,dummy_board_class,engine_moves_list):
    iterations = 3 #for now, try increasing later
    mcts_classes = []
    mcts_outcomes = []
    new_valid_moves = []
    print("engine mvoes list: ",engine_moves_list)
    for x in (engine_moves_list):
        print("x is", x)

        try:
            if x[0] != None and x[0] != []:
                for y in x[0]:
                    print("y is", y)
                    new_valid_moves.append([y, x[1]])
        except:
            if x[0] != None and x[0] != []:
                for y in x[0]:
                    print("y is", y)
                    new_valid_moves.append([y, x[1]])
    print("the following is the valid moves for engine")
    print(new_valid_moves)
    print("done")
    for x in new_valid_moves:  # all the original parent nodes - represent POSSIBLE wengine moves
        # game_tree.find_tree(user1, user2, board.board, board, board.board, 0, x, moves_list)
        # mcts_class.set_root(x)
        mcts_class = MCTS(x, orig_board_class, dummy_board_class, evie, user1, user2)
        mcts_classes.append(mcts_class)
        mh = Move_handler()
        final_outcome_score = mcts_class.run_mcts(iterations, mh,dummy_board_class)
        mcts_outcomes.append([x,final_outcome_score])
        print(final_outcome_score)

    enum_outcomes = enumerate(mcts_outcomes)
    print(mcts_outcomes)
    print(enum_outcomes)
    temp_outcomes = []
    for z in mcts_outcomes:
        temp_outcomes.append(z[1])
    curr_max = 0
    for x in mcts_outcomes:
        if x[1] > curr_max:
            curr_max = x[1]
            max_outcome = x

    print("max outcome is: ",max_outcome)

    return max_outcome[0][0],max_outcome[0][1]



class Tree():
    def __init__(self,boardie,dummy_board):
        self._game_tree = []
        self._board_board = boardie

    def make_dummy_users(self):
        self.__dummy_user1 = Player("white")
        #player 2 will be the engine
        self.__dummy_user2 = Player("black")
        self.__dummy_user1.inst_moves_history()
        self.__dummy_user2.inst_moves_history()

        self.__dummy_handler = Move_handler()

    def find_tree(user1,user2,board_inital,board,boardie,curr_depth,move,moves_list):
        max_depth = 3
        self.__dummy_board = chess_board()
        self.__dummy_board.new_board(boardie)
        
        print("FINAL MOVES LIST IS: ",final_moves_list)
        #engine_moves_list = user2.find_all_moves(boardie,board)
        temp_list = moves_list
        #children = []
        if temp_list != [] or temp_list != None:
            for x in temp_list:
                
                print("visiting a new x now")
                current_child = []
                print("x is",x)
                count = 0
                for y in range(len(x)):
                    count += 1
                dummy_piece = x[1]
                print("dummy piece is",dummy_piece)
                m1,n1 = self.__dummy_board.get_pos(str(dummy_piece))
                print("count is",count)
                
                if count > 1:
                    for z in range(0,count-1):
                        print("current count is",z)
                        try:
                            m2 = x[0][z][0]
                            n2 = x[0][z][1]
                            
                        except IndexError:
                            m2 = x[0][z][0][0]
                            n2 = x[0][z][0][1]
                        curr_depth += 1
                        
                        if curr_depth > (max_depth):
                            if curr_depth % 2 == 0:
                                next_moves = self.__dummy_user2.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                            else:
                                next_moves = self.__dummy_user1.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                            return next_moves
                        else:
                            print("FINDING NEXT MOVES")
                            self.__dummy_board.update_board(m2,n2,dummy_piece)
                            self.__dummy_board.update_board(m1,n1," ")
                            if curr_depth % 2 == 0:
                                next_moves = self.__dummy_user2.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                            else:
                                next_moves = self.__dummy_user1.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                            current_child = [next_moves,dummy_piece]
                            print("current child is {}".format([current_child,breadth]))
              
                else:
                    m2 = [0][1][0]
                    n2 = [0][1][1]
                    
                print("m1 {}, n1 {}, m2 {}, n2 {}".format(m1,n1,m2,n2))
                curr_depth += 1
                if curr_depth > (max_depth):
                    if curr_depth % 2 == 0:
                        next_moves = self.__dummy_user2.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                    else:
                        next_moves = self.__dummy_user1.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                    return next_moves
                else:
                    print("FINDING NEXT MOVES")
                    #updating dummy board to make the move
                    self.__dummy_board.update_board(m2,n2,dummy_piece)
                    self.__dummy_board.update_board(m1,n1," ")
                    if curr_depth % 2 == 0:
                        next_moves = self.__dummy_user2.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                    else:
                        next_moves = self.__dummy_user1.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
                        current_child = [next_moves,dummy_piece]
                    print("current child is {}".format([current_child,breadth]))
                        
                    children.append(current_child)
                    breadth += 1
                    try:
                        victim_piece = current_child[0][0][1]
                        temp_list.remove(x)
                        self.find_tree(user1,user2,self.__dummy_board.board,self.__dummy_board,breadth,final_moves_list,temp_list,children,antichildren)
                    except IndexError:
                        print("list index out of range")
                        continue
                        next_moves = [[[]]]
                    #temp_list.remove(x)
                    
                    self.__dummy_board.update_moves()
                    self.__dummy_board.update_board()
                    
                    return next_moves

    class Tree_branch():
        def __init__(self,boardie,board,k,engine_moves_list):
            self.__dummy_boardie = boardie
            self.__dummy_board = chess_board()
            self.__dummy_board.new_board(boardie)
            self.__moves_list = engine_moves_list
            self.__root = k
            print("root is: ",self.__root)
            self.__leaf_node = False
            self.__dummy_handler = Move_handler()
        def make_dummy_users(self):
            self.__dummy_user1 = Player("white")
            #player 2 will have to be the engine
            self.__dummy_user2 = Player("black")
            self.__dummy_user1.inst_moves_history()
            self.__dummy_user2.inst_moves_history()
        def is_fully_expanded(self):
            return False
        def add_eval(self,move,tree):
            pass
        #add eval so it can be turned into a different tree that has the normalised evaluated value of each move
        #USE THE NODE CLASS TO INSTANTIATE NODES FOR ALL THE DIFFERENT PARTS OF THE TREE        
        class Node():
            def __init__(self,node,board):
                self.__node = node
                self.__leaf_node = True
            @property
            def children(self):
                pass
            
            def is_fully_expanded(self):
                return self.__leaf_node
            
            def get_visit_num(self):
                pass
            
            def is_root(self):
                #return true or false. check if root node
                pass 
        def get_board(self):
            return self.__dummy_board
        #PARAMETER NEEDED FOR THE BOARD THAT WILL BE USED BECAUSE YOU CANT JUST KEEP MAKING NEW ONES

        def generate_children(self,user1,user2,breadth,final_moves_list,tree,children,antichildren,large,root,board,boardie):
            max_breadth = 5
            temp_list = root
            print("templist is",temp_list)
            print("CURRENT BREADTH IS: ",breadth)
            
            #this needs to be appended
            for x in temp_list[0]:
                tree.append(x)
                print("visiting a new x now, which is ",x)
                current_child = []
                current_antichild = []
                dummy_piece = temp_list[1]
                print("dummy piece is: ",dummy_piece)
                
                self.__dummy_board_extra = board
                self.__dummy_board_extra.new_board(boardie)
                """
                count = 0
                for y in range(len(x)):
                    count += 1
                
                dummy_piece = self.__root[1]
                
                print("dummy piece is",dummy_piece)
            
                m1,n1 = self.__dummy_board.get_pos(str(dummy_piece))
                print("count is",count)
                
                for z in range(0,count-1):
                    print("current count is",z)
                    try:
                        m2 = x[z][0]
                        n2 = x[z][1]
                        
                    except IndexError:
                        m2 = x[0][z][0]
                        n2 = x[0][z][1]
                """
                m2 = x[0]
                n2 = x[1]
                m1,n1 = self.__dummy_board_extra.get_pos(str(dummy_piece))
                print("m1 {}, n1 {}, m2 {}, n2 {}".format(m1,n1,m2,n2))

                #rollout
                print("FINDING NEXT MOVES")
                temp_list[0].remove(x)
                if breadth % 2 == 0:
                    next_moves = [self.__dummy_user2.get_all_valid_moves(m2,n2,self.__dummy_board_extra.board,dummy_piece),dummy_piece]
                else:
                    next_moves = [
                        self.__dummy_user1.get_all_valid_moves(m2, n2, self.__dummy_board_extra.board, dummy_piece),dummy_piece]
                current_child = next_moves,dummy_piece,breadth
                print("current child is {}".format(current_child))
                print("NEXT MOVEs: ",next_moves)
                #make the move for current child, instantiate new dummy board???

                children.append(current_child)
                breadth += 1
                if breadth <= max_breadth:
                    try:
                        victim_piece = current_child[0][0][1]
                        try:
                            temp_list.remove(x)
                        except:
                            print("ok")
                        print("breadth is",breadth)
                        for j in next_moves[0]:
                            root = [j],dummy_piece
                            print("the root is now: ",root)
                            #DIFFERENT BOARDS PASSED TO THE GENERATOR
                            self.__dummy_board_extra.update_board(m2,n2,dummy_piece)
                            self.__dummy_board_extra.update_board(m1,n1," ")
                            print("updated board is: ",self.__dummy_board_extra.board)
                            #getting the right boards generated
                            if breadth < max_breadth:
                                ans = self.generate_children(user1,user2,breadth,final_moves_list,tree[1],children,antichildren,large,root,self.__dummy_board_extra,self.__dummy_board_extra.board)
                            elif breadth == max_breadth:
                                #evie.store_everything(self.__dummy_board_extra, str(user1.colour())[0],"-","-")
                                ans = self.generate_children(user1,user2,breadth,final_moves_list,tree[1],children,antichildren,large,root,board,boardie)
                            #this is super wrong
                            j[1] = ans
                            print("ans is: ",ans)
                    except IndexError:
                        print("list index out of range")
                        continue
                        next_moves = [[[]]]
                    return ans
                else:
                    print("it's over!!")
                    return children
                    break
                    
                    #temp_list.remove(x)
                """
                self.__dummy_board.update_moves()
                self.__dummy_board.update_board()
                """
            #after depth is greater than 1 you need to commit to the new board
            """
            self.__dummy_board.update_board(m2,n2,dummy_piece)
            self.__dummy_board.update_board(m1,n1," ")
            next_moves = self.__dummy_user2.get_all_valid_moves(m2,n2,self.__dummy_board.board,dummy_piece)
            """

            print("CHILDREN HAVE BEEN GENERATED")
            print(children)
            print("tree stuff: ")
            print(tree)
            self.__children = children
            #return next_moves
            return children,tree

    def make_branch(self,user1,user2,boardie,board,k,engine_moves_list,large):
        print("making a branch")
        mm = Minmaxer()
        moves_num = board.moves
        #mm.get_minmax(k, user1,user2,board,boardie,boardie,0,0,engine_moves_list,5,moves_num,alpha = -370,beta = 370,max_score=-3700,min_score=3700)
        self.branch = self.Tree_branch(boardie,board,k,engine_moves_list)
        children = []
        antichildren = []
        board = self.branch.get_board()
        self.branch.make_dummy_users()
        self.__tree = []
        print("getting children")
        branch, children = self.branch.generate_children(user1,user2,0,engine_moves_list,self.__tree,children,antichildren,large,k,board,boardie)
        print("children is",children)
        return branch
        #node of a branch of a tree

    def find_depth(self,sub_tree):
        #Recursively finds the maximum depth of a nested list
        if not isinstance(sub_tree, list):
            return 0
        if not sub_tree:  #if its a character
            return 1
        return 1 + max(self.find_depth(i) for i in sub_tree)

    def depth_first_traversal(self,tree):
        #part = np.array(tree)
        #print("here")
        l = self.find_depth(tree)
        #print("depth currently is: ",l)
        if l == 1:
            #print("tree is, well subtree", tree)
            return tree
        elif l == 0:
            #print("tree was a piece?", tree)
            return tree
        for x in tree:
            self.depth_first_traversal(x)

