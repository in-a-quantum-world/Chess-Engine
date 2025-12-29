import random
import math

import chess
from chess_evaluator import Evaluator as ev, Evaluator
import asyncio
import time
from chess_classes import chess_board
#mcts in python

# get the board state stuff working
# do that within the board class

global evie
evie = Evaluator()
evie.instantiate()
class Minmaxer():
    def __init_(self):
        pass
    def return_depth(self, depth):
        return self.__depth1

    def get_opp_moves(self, user1, board, board_state):
        opp_moves = user1.all_moves(board_state)
        return opp_moves

    # use a depth first traversal method to go down the depth
    def depth_first_traversal(self, tree, board_state, board_class, orig_board_state):
        # part = np.array(tree)
        # print("here")

        l = self.find_depth(tree)
        # print("depth currently is: ",l)
        if l == 1:
            # print("tree is, well subtree", tree)
            board_class.undo_recent_move()
            return tree
        elif l == 0:
            # print("tree was a piece?", tree)
            return tree
        for x in tree:
            board_state  # make relevant change
            self.depth_first_traversal(x)
    def alpha_beta_pruning(self,alpha,beta,engine_turn,depth,maxScore,minScore):
        self.alpha = alpha
        self.beta = beta
        self.prune = False
        if maxScore != None:
            if maxScore > alpha:
                print("max score is greater than alpha")
                self.alpha = maxScore
            if beta <= alpha:
                print("pruned because beta is less than or equal to alpha:")
                self.prune = True

        elif minScore != None:
            if minScore < beta:
                print("min score is less than beta")
                self.beta = minScorea
            if beta <= alpha:
                print("pruned because beta is less than or equal to alpha:")
                self.prune = True
        return self.alpha,self.beta,self.prune
    def get_negamax_ab(self, board_state, valid_moves, depth, alpha, beta, turnMultiplier):
        if depth == 0:
            return (turn_multiplier * score(board_state))
        if moves % 2 == 0:
            max_score = -3700
            for move in valid_moves:
                board_state.move(move)
                next_moves = board_state.get_valid_moves()
                score = get_negamax_ab(board_state, next_moves, depth - 1, -alpha, -beta, -turnMultiplier)
                if score > max_score:
                    max_score = score
                    if depth == DEPTH:
                        next_move = move
                if max_score < alpha:
                    alpha = max_score
                if alpha >= beta:
                    break
            if max_score != None:
                return max_score

    def get_minmax_with_moves_ready(self):
        pass
    def adjust_list(self,valid_moves):
        new_valid_moves = []

        for x in valid_moves:
            print("x is", x)
            for y in x[0]:
                print("y is", y)
                new_valid_moves.append([y, x[1]])

        return new_valid_moves
    #the minmax algo should also be used for backprop
    def get_minmax(self, curr_root_node,user1, user2, board_class, orig_board_state, curr_board_state, depth, move_num,
                   valid_moves, max_depth, before_move_nums,alpha,beta,max_score,min_score):
        print("valid moves is: ",valid_moves)
        if depth == 0:
            #board_class.new_board(curr_board_state)
            #board_class.undo_recent_move()
            print("depth is zero")
            total_moves = before_move_nums + move_num
            if max_depth % 2 == 0:
                colour = user2.colour()
                dash = "-"
                print("colour is: ",colour)
                castling_rights = board_class.castling_rights(colour)
                this_board = board_class.board
                print("this board is: ",this_board)
                evie.store_everything(this_board, colour, castling_rights, dash, total_moves)
                return evie.score() # because user2 is engine
                #within the same event loop

            else:
                colour = user1.colour()
                dash = "-"
                print("colour is: ",colour)
                castling_rights = board_class.castling_rights(colour)
                this_board = board_class.board
                print("this board is: ",this_board)
                evie.store_everything(this_board,colour,castling_rights,dash,total_moves)
                return evie.score() #score needs to be minimised
        else:
            if move_num % 2 == 0:
                print("MAXIMISING")
                # maximiser
                #max_score = -3700
                for move in valid_moves:  #checking each move within valid moves and conducting minmax on all of those
                    #generating all valid mvoes that can be done following move
                    temp_m1,temp_n1 = board_class.get_pos(move[1])
                    temp_m2 = move[0][0]
                    temp_n2 = move[0][1]
                    dummy_piece = move[1]
                    print(temp_m2,temp_n2,dummy_piece)
                    print("temp m1 and n1 are: {},{}".format(temp_m1, temp_n1))

                    #board_class.update_board(temp_n2, temp_m2, dummy_piece)
                    print(board_class.board)
                    print("board updated")
                    #board_class.update_board(temp_n1, temp_m1, " ")
                    curr_root_node = curr_root_node.add_child(move,board_class.board)
                    next_moves = self.adjust_list(user2.find_all_moves(curr_board_state,board_class))  # find next moves in the tree
                    print("next moves are: ",next_moves)
                    move_num += 1
                    curr_board_state = board_class.board

                    score = self.get_minmax(curr_root_node,user1, user2, board_class, orig_board_state, curr_board_state,
                                            depth - 1, move_num, next_moves, max_depth,before_move_nums,alpha,beta,max_score,min_score)
                    #undoing the move so the board state returns to its previous state
                    #board_class.undo_recent_move()
                    print("move undone")
                    time.sleep(0.5)
                    print("score is: ",score)
                    if max_score !=None and score!=None:
                        if score > max_score:  # if the current score is larger than max score, then max score needs to be reassigned
                            max_score = score
                            if depth == max_depth:

                                best_move = move
                                #return best_move,max_score
                                return max_score
                        print("alpha is {}, beta is {}".format(alpha, beta))
                        alpha,beta,prune = self.alpha_beta_pruning(alpha=alpha, beta=beta,engine_turn=True,depth=depth,maxScore=max_score,minScore=None)
                        if prune == True:
                            break
                    if max_score != None:
                        return max_score

            else:
                print("MINIMISING")
               # min_score = 3700  #needs to be minimised, so originally a large value is set
                for move in valid_moves:
                    # dummy_board.update_board(j[0],j[1],current_piece)
                    print("move is: ",move)
                    temp_m1, temp_n1 = board_class.get_pos(move[1])
                    temp_m2 = move[0][0]
                    temp_n2 = move[0][1]
                    dummy_piece = move[1]
                    print(temp_m2, temp_n2, dummy_piece)
                    print("temp m1 and n1 are: {},{}".format(temp_m1, temp_n1))

                    #board_class.update_board(temp_n2, temp_m2, dummy_piece)
                    curr_root_node = curr_root_node.add_child(move, board_class.board)
                    next_moves = self.adjust_list(user1.all_moves(curr_board_state))  # find next moves in the tree
                    print("next moves are: ", next_moves)
                    move_num += 1
                    curr_board_state = board_class.board
                    #curr_board_state = dummy_board.board
                    score = self.get_minmax(curr_root_node,user1, user2, board_class, orig_board_state, curr_board_state,
                                            depth - 1, move_num, next_moves, max_depth,before_move_nums,alpha,beta,max_score,min_score)
                    #board_class.undo_recent_move()
                    print("score is: ",score)
                    time.sleep(0.5)
                    if min_score != None and score !=None:
                        if score < min_score:
                            min_score = score
                            if depth == max_depth:
                                #board_class.undo_recent_move()
                                best_move = move
                                #return best_move,min_score
                                return min_score

                        alpha,beta,prune = self.alpha_beta_pruning(alpha=alpha, beta=beta, engine_turn=False, depth=depth,maxScore=None,minScore = min_score) #CHECK IF TRUE OR FALSE, FOR PRUNING
                        print("alpha is {}, beta is {}".format(alpha, beta))
                        if prune == True:
                            break
                    if min_score != None:
                        return min_score

    def backprop(self):
        #this was an attempt to do backpropagation on the game tree, where all nodes of the game tree are stored in a singular multidimensional array
        #this attempt is no longer used as I am now conducting the backpropagation dynamically
        max_depth = -4  # max depth should ideally not be larger than 5
        # THIS IS TRYING TO DO BACKPROP WITHIN MINMAX. SEPARATE THESE.
        dummy_board.new_board(curr_board_state)
        if depth == 0:
            end_node_score = score(dummy_board.board)
            return
        elif depth == -4:
            # move handler here
            minmax_handler = Move_handler()
            minmax_handler.fen_conversion_proper()
            # convert to fen
            move_num -= 1
            child_node_score = score(dummy_board.board)
            if score > max_score:
                max_score = score
                next_move = move
            else:
                next_move = None
            depth = -4
            dummy_board.new_board(board3)
            return child_node_score, next_move, self.get_minmax(user1, user2, board_class, orig_board_state, board1, board2,
                                                                board3=None, game_tree=game_tree, depth=depth+1, move=move, move_num=move_num,alpha=-37000,beta=37000)  # go to negative values
        elif depth == -1:
            move_num -= 1
            branch_score1 = score(dummy_board.board)
            dummy_board.new_board(orig_board_state)
            return self.get_minmax(user1, user2, board_class, orig_board_state, board1, board2=None, board3=None, game_tree=game_tree,
                                   depth=depth+1, move=move, move_num=move_num)  # go to negative values

        elif depth == -2:
            move_num -= 1
            branch_score2 = score(dummy_board.board)
            dummy_board.new_board(board1)
            return self.get_minmax(user1, user2, board_class, orig_board_state, board1=None, board2=None, board3=None,
                                   game_tree=game_tree, depth=depth+1, move=move, move_num=move_num)  # go to negative values

        elif depth == -3:
            move_num -= 1
            branch_score3 = score(dummy_board.board)
            dummy_board.new_board(board2)
            return self.get_minmax(user1, user2, board_class, orig_board_state, board1, board2=None, board3=None, game_tree=game_tree,
                                   depth=depth+1, move=move, move_num=move_num)  # go to negative values
#KEEP WORKING ON THIS
class MCTS():
    # USE THE NODE CLASS TO INSTANTIATE NODES FOR ALL THE DIFFERENT PARTS OF THE TREE
    class Node():

        def __init__(self,val,current_board_state,children,parent):
            self.node = val
            self.board_state = current_board_state
            self.visit_count = 0
            self.children = children
            self.parent = parent
            self.wins = 0
            #self.wins = 0

        def is_fully_expanded(self): #checks if there are no more child nodes
            if len(self.children) == 0:
                return True
            else:
                return False
        def get_parent(self): #check this carefully
            node = self.parent
            while node.parent != None:
                node = self.parent
            return node #returns parent for the node
        def update_value(self):
            pass
        def add_visits(self): #needs to keep track of how many times it has been visited
            self.visit_count += 1
        def add_child(self,val,board_state):
            child = self.__class__(val,board_state,children=[],parent=self)
            self.children.append(child)
            return child #adding the instantiated node as a child of the current node (root node)
        def ucb(self,exploration_weight):
            self.exploration_weight = exploration_weight
            if self.visit_count == 0:
                return float("inf")
            self.exploitation = wins/self.visit_count
            self.exploration = self.exploration_weight
            self.score = self.exploitation + self.exploration
            return self.score
            #returns an optimised score based off of these parameters
        def best_child(self,exploration_weight):
            #exploration_weight = 0.5 #using the exploration exploitation trade off strategy
            best = max(self.children, key=lambda c: c.ucb(exploration_weight)) #finding the child node with the maximum evaluation score using the UCB formula
            print("best val and wins are: ",best.node,best.wins)
            return best.node,best.wins

    def __init__(self,root_val,orig_board_class,board_class,evaluator,user1,user2):
        self.board_class = orig_board_class #this could cause an error as you are passing the instantiated object
        self.move_num = board_class.moves
        self.val = root_val
        self.root = self.Node(root_val,board_class.board,children=[],parent=None)
        self.user1 = user1
        self.user2 = user2
        self.dummy_board = chess_board()
        self.dummy_board.new_board(board_class.board)
        self.first_board_state = board_class.board
        self.minmax = Minmaxer()
        #self.valid_moves = valid_moves
        # fix the node children thing later

    def search(self,tree):
        #used to hold all of the nodes (parent nodes)
        pass
    """
    def make_node(self,current_board_state,children):
        self.curr_node = self.Node(val,current_board_state,children)
    """
    def adding_children(self,max_depth): #RECURSIVE
        pass
        #use depth first traversal strategies to keep adding children
    def find_depth(self,sub_tree):
        #Recursively finds the maximum depth of a nested list
        if not isinstance(sub_tree, list):
            return 0
        if not sub_tree:  #if its a character
            return 1
        return 1 + max(self.find_depth(i) for i in sub_tree)

    def depth_first_traversal(self,tree):
        l = self.find_depth(tree)
        #print("depth currently is: ",l)
        if l == 1:
            #tree is a subtree
            return tree
        elif l == 0:
            #tree was a piece
            return tree
        for x in tree:
            self.depth_first_traversal(x)

    def expansion(self,node,move_handler):
        #generate all legal moves from a root move
        pass
    def backprop(self, node, result):
        while node is not None: #checking that it has children so it can be visited
            node.add_visits()
            node.wins += result #adding backprop score
            #result = -result
            node = node.parent

    def best_child(self, result):
        return self.node.best_child()

    def simulate(self,max_depth,current_node):
        #this simulation is also doing the expansion
        #expansion is generating all the child nodes (part of the minmax algorithm too) and adding these as children to the current node
        print("current node is: ",current_node.node)
        m2 = (current_node.node)[0][0]
        n2 = (current_node.node)[0][1]
        dummy_piece = (current_node.node)[1]
        self.current_board_class.new_board(self.first_board_state)
        print("dummy piece is: ",dummy_piece)
        print("the board is: ",self.dummy_board.board)
        self.current_board_class.better_update(m2, n2, dummy_piece)
        #self.board_class.update_board(m1, n1, " ")
        valid_moves = self.user1.all_moves(self.current_board_class.board) #this forms part of the expansion
        """
        for move in valid_moves:
            temp_m1 = move[0][0]
            temp_n1 = move[0][1]
            temp_m2 = move[1][0]
            temp_n2 = move[1][1]
            dummy_piece = move[2]
            self.board_class.update_board(temp_m2, temp_n2, dummy_piece)
            self.board_class.update_board(temp_m1, temp_n1, " ")
            current_node.add_child(move,self.board_class.board)
            self.board_class.undo_recent_move()
        """
        new_valid_moves = []
        for x in valid_moves:
            for y in x[0]:
                new_valid_moves.append([y, x[1]])
        #self.dummy_board = self.board_class
        #the simulation is purely within the minmax algorithm
        backprop_score =  self.minmax.get_minmax(self.root,self.user1, self.user2, self.current_board_class, self.current_board_class.board, self.first_board_state,1, self.move_num+1,
                   new_valid_moves,max_depth, self.move_num+1,alpha = -370,beta = 370,max_score=-3700,min_score=3700)
        time.sleep(0.8)
        print("finished")
        return backprop_score

    def selection(self):
        current_node = self.root
        while not current_node.is_fully_expanded():
            current_node = current_node.best_child()
        return current_node
    def run_mcts(self,iterations, move_handler,orig_board_class):
        #for q in range(iterations): #the purpose of the iterations is for optimisation
        self.current_board_class = orig_board_class
        current_node = self.root #so this doesn't need to change each time
        #self.expansion(current_node, self.mh) #going down a tree branch #DEPTH FIRST TRAVERSAL NEEDED HERE
        backprop_score = self.simulate(5,current_node) #simulating result by doing minmax
        print("backprop_score is: ",backprop_score)
        self.backprop(current_node, backprop_score) #backprop in order to update all the stats for the parent nodes

        #return self.root.best_child(exploration_weight=1.4),backprop_score #should return best evaluation score - the move itself is not needed
        return backprop_score#,current_node.get_parent()

#valid moves is:  [[[[5, 2], [5, 0]], 'wN1'], [[[5, 7]], 'wN2'], [[[6, 3], [5, 4], [4, 5], [3, 6], [2, 7]], 'wB1'], [[[2, 0]], 'wB2'], [[[6, 3], [1, 3], [0, 3], [6, 3], [1, 3], [0, 3], [6, 3], [1, 3], [0, 3], [6, 3], [1, 3], [0, 3], [6, 3], [1, 3], [0, 3], [6, 3], [1, 3], [0, 3], [6, 3], [1, 3]], 'wQ'], [[[4, 0], [5, 0]], 'wp1'], [[[4, 1], [5, 1]], 'wp2'], [[[4, 2], [5, 2]], 'wp3'], [[[4, 3]], 'wp4'], [[[4, 4], [5, 4]], 'wp5'], [[[4, 5], [5, 5]], 'wp6'], [[[4, 6], [5, 6]], 'wp7'], [[[4, 7], [5, 7]], 'wp8']]

