## File Structure and Descriptions

This section outlines the modular structure of the chess program, detailing the responsibilities and interactions of each component.


### 1. `chess_main.py`
The entry point of the application, handling the core logic and user interface.
* **GUI Representation:** Uses `pygame` to create the graphical board and piece renderings via dedicated functions.
* **Object Instantiation:** Orchestrates the initialization of:
    * The chess board matrix.
    * Piece objects.
    * The chess engine and tree data structures.
* **Database Integration:** Imports modules for managing player details and game history.
* **Game Loop:**
    * Manages continuous execution until stopping conditions (e.g., checkmate or user quit) are met.
    * Triggers move functions and updates the **Move History Stack**.

### 2. `chess_player.py`
Defines the `Player` class and the mechanics of user interaction.
* **Aggregation/Association:** Instantiates specific objects for each piece type within the class to allow direct control.
* **Validation & Logic:**
    * Verifies "Check" status.
    * Validates move legality before execution.
* **Move History Stack:**
    * Implemented as a standard **Stack** data structure.
    * Includes methods: `push()`, `pop()`, `is_full()`, `is_empty()`, and `peek()`.
    * Stores game progression for both the user and the AI.

### 3. `chess_mcts.py`
Contains the **Monte Carlo Tree Search (MCTS)** implementation.
* **Data Structure:** Houses the tree structure and its associated methods.
* **Encapsulation:** Ensures tree operations are handled internally to maintain data integrity.

### 4. `chess_ann.py`
Dedicated to the **Artificial Neural Network (ANN)** for game state evaluation.
* **Neural Network Model:** * Trained on test data to simulate game endings based on board matrix inputs.
    * **Development Flow:** Initially developed procedurally for efficiency testing, then refactored into an **Object-Oriented (OOP)** paradigm for production.
* **Evaluation Functions:** Assesses winning probabilities by analyzing the board matrix and move history.

### 5. `chess_random_moves.py`
A baseline AI component for non-deterministic responses.
* **Functionality:** Returns a legal random move in response to user play.
* **Initialization:** Instantiates all required piece classes (e.g., 8 pawns, 2 knights).
* **Move Generation:** Analyzes the current board state to identify all legal moves for every piece.

### 6. `chess_pygame_random_moves_ai.py`
A specialized execution file for testing the random move generator.
* Acts as an alternative `main.py` to test the interaction between the GUI, the board, and the random AI agent.

### 7. `chess_moves.py`
Manages the complex logic of move generation and tree branching.
* **Tree Class & Subclasses:** * Includes the `TreeBranch` class.
    * Generates child nodes and links the tree to MCTS, Minimax, and Alpha-Beta Pruning processes.
* **Dummy Objects:** * Instantiates **"Dummy Users"** and **"Dummy Boards"** to simulate and find legal moves without affecting the actual game state.
* **Move Handler Class:** * Acts as an intermediary between the Player and Chess classes.
    * **Notation Conversions:** * Current state to **FEN** string.
        * Moves to **Standard Algebraic Notation (SAN)** using BNF syntax rules.
        * Board states to **Portable Game Notation (PGN)**.

### 8. `chess_engine.py`
The logic core that integrates the search algorithms and the neural network.
* **Engine Class:** Methods handle the orchestration of `chess_mcts` and `chess_ann`.
* **Search Process:**
    1. **Selection:** Creates the game tree and sets the current state as the root.
    2. **Traversal:** Performs **Depth-First Search (DFS)** and **In-Order Traversal** to explore child nodes.
    3. **Simulation/Evaluation:** Passes the board matrix to the ANN to return a winning probability (0.0 to 1.0).
    4. **Optimization:** Utilizes **Minimax** and **Alpha-Beta Pruning** to eliminate low-probability branches by adjusting depth levels.

### 9. `databases_for_chess.py`
Handles persistent data storage using the `sqlite3` module.
* **Database Management:** Uses local storage (no server required).
* **OOP Integration:** Database tables are contained within classes with methods for viewing and updating records.

### 10. `chess_classes.py`
Defines the blueprint for all chess pieces.
* **Individual Piece Classes:** Contains methods for specific movement logic.
* **Validation Logic:** Includes a separate, modular function for move validation called within each piece's `move` method.

### 11. `chess_table_bases.py`
Provides optimized evaluation metrics.
* Uses matrix-based values to aid the engine in assessing move quality based on piece type and the current stage of the game.

---

## Folders
* **`chess_images/`**: Contains PNG files for all chess pieces used by `chess_main.py` for the graphical interface.


