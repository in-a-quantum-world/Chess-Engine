# Chess-Engine
Chess Engine and game-play interface made from scratch. Engine combines use of minmax algorithm with Monte Carlo Tree Search. Extra features include: endgame table bases (and analysis), FEN notation and parsing for board representation, SQL and aggregation, tree traversal, random moves generator (for testing)

# 1 - Project Outline
My idea is to create a chess game that is played by a user against an AI-assisted chess engine. This project will be aimed at beginner to intermediate chess players who are already well aware of rules and strategies of the game, so they can play against the engine, however it will also be designed to provide additional tips or reminders to players. The game should be played by a user against a chess engine. 

# 2 - My proposed solution
Firstly I will first create the prerequisites for a chess game, which is the board and pieces. I will create the graphical user interface for the game using Pygame and create classes for each piece type and load their corresponding images using requests. Instead of using the chess library available for Python, I will try to create functions for checking valid moves myself. This game would be presented as an app. 

The current approach is to first create the chess board and the general game structure before focusing on the game tree and Machine Learning algorithms. Many examples online use the chess library in python which contains many built in methods to abstract the process such as a single method to check for a checkmate. Those that do not use this library create classes for each chess piece and define rules and create functions for checking if a move is valid or for a checkmate. 
My aim is to then create a chess engine that can play this chess game against the user – instead of 2 users playing against each other, one user can play the game, and its opponent will be the chess engine. 

I will initially create a game tree which stores next possible moves for a chess piece on the board, taking into consideration other pieces and chess rules. I then plan on creating an evaluation function which will apply mathematical formulae to the variables associated with a branch of the game tree, to calculate the probability of winning, outputting a number within a certain range. 

A minmax algorithm uses a depth first traversal technique to locate the move that leads to the best outcome (the highest outcome of the evaluation function) - this algorithm finds the most efficient way to have the maximum chance of winning, minimising the chances of losing. I will then use alpha-beta pruning to optimise this by reducing the number of branches of the tree that the algorithm traverses. 

*Where neural networks come in is through further optimising the minimax algorithms* – as there are so many possible outcomes following a single move in chess, it would be impossible to store all of them in a tree (and it would take too long for the program to execute as well). It requires a large amount of data to be stored in a tree data structure and processed. The depth of this tree as a result is very large, thus the program can take a long time to successfully run, so it is not very efficient. The combination of the minmax algorithm and neural networks is called a Monte Carlo Tree Search (MCTS), often used to represent the outcomes of more complicated games. 

I plan to use a pre-trained transformer structure which I will incorporate into the MCTS. This transformer would be able to interpret chess-based statistics including evaluation metrics (which I will create functions for) and is pre-trained, so would not need to undergo special training processes. I will make sure that data fed into this transformer is of a similar format to the type it was trained upon. 


# 3 - Monte Carlo Tree Search
This is a series of algorithms that are reputed at allowing programs to make complex choices based upon many input variables, such as making the next move in a chess game. The Monte Carlo Tree Search incorporates methods from classic tree searching algorithms (eg minmax) and elements from reinforcement learning (a type of machine learning). 
The MCTS algorithm involves a technique known as **‘exploration-exploitation trade off’** which continues to search for the best solution even after what may be thought of as the best solution has already been found. The MCTS algorithm combines two very useful techniques and provides the perfect balance between them: exploitation and exploration. Exploration is exploring many branches of the tree to search for optimal solutions, whereas exploitation will reject searching through a certain tree branch based on its predicted value. 

The **exploration** part of the MCTS algorithm can be performed the minmax algorithm and other similar tree searching algorithms. However these can be incredibly time consuming thus inefficient, which is why exploitation is needed. Alpha-beta pruning is a technique for exploitation but is not very efficient. This is where the idea of neural networks comes in. 
*The MCTS will only search a few layers deep into the tree, prioritising certain branches, and simulates an outcome rather than searching the entire tree, making it a lot more time and space efficient.*


# 4 - Tree Searching Algorithms I employed
* Search tree: A tree is not supposed to have cycles, but due to the nature of chess, some moves can be repeated and so the tree may contain cycles. Cycles are usually not searched twice. 
* Minmax algorithm: This is used to determine the score in a zero-sum game after a certain number of moves have taken place. This algorithm chooses which move to play next by assessing the value to the player that maximises success and minimises failure (hence ‘minmax’) and playing the next move accordingly. 
* Negamax algorithm – An alternative to the minmax algorithm, the only difference being that the evaluation of a position is equal to the negative of the evaluation of a position from the opponent’s point of view. So rather than assessing each possible move for both players, this can be done just for one player, and negated for the other. 
* Alpha-beta adjustment: Most searching algorithms in chess will use a version of an alpha-beta algorithm to search the tree in a depth first manner. This will enable it to assess the value of the end result rather than going from top down, as a traditional minmax algorithm would do. A minmax algorithm combined with an alpha-beta algorithm would be optimal for finding the next best move. 
* Depth first search: Conducting a depth first search: this starts at the root of the tree and goes as far as possible along each branch of the tree, before backtracking. Main memory only needs to hold one path from the root to the lead at a time, so the program isn’t memory inefficient as such. 


