# Chess Engine & GUI: Technical Analysis and Objectives

## Project Modularisation and Decomposition

The project is decomposed into several modular components to ensure separation of concerns between the GUI, game logic, and AI engine.

---

### Core Game Files
* **`chess_main.py`** (Main Entry Point)
    * **GUI:** Implements the graphical board and piece rendering using `pygame`.
    * **Instantiation:** Manages the board matrix, engine, and tree data structures.
    * **Game Loop:** Handles continuous execution, move history updates, and termination conditions (Checkmate/Quit).
* **`chess_player.py`**
    * **Player Class:** Uses aggregation/association to control piece objects.
    * **Validation:** Verifies "Check" status and move legality.
    * **Move History Stack:** Implements a standard Stack (`push`, `pop`, `peek`) to store game progression.
* **`chess_classes.py`**
    * Defines individual classes for each piece with specific movement and legal-move generation logic.
* **`chess_moves.py`**
    * **Tree & Branch Classes:** Manages the search tree and child node generation.
    * **Simulation Tools:** utilises "Dummy Users" and "Dummy Boards" to calculate legal moves without affecting the live state.
    * **Notation Handler:** Converts board states to **FEN**, **SAN**, and **PGN**.

### AI and Search Engine
* **`chess_engine.py`**
    * **Algorithm:** Integrates **Monte Carlo Tree Search (MCTS)** with **Minimax** and **Alpha-Beta Pruning**.
    * **Workflow:** Performs Selection, Depth-First Traversal, and Evaluation via the Neural Network.
* **`chess_mcts.py`**: Contains the MCTS class and tree data structure with encapsulated methods.
* **`chess_ann.py`**: Implements a Neural Network (initially procedural, later OOP) to evaluate winning probabilities (0.0 to 1.0) based on board states.
* **`chess_random_moves.py`**: A baseline AI that returns legal random moves for testing.

### Data & Resources
* **`databases_for_chess.py`**: Handles local `sqlite3` integration for player profiles and game history.
* **`chess_table_bases.py`**: Matrix-based evaluation tables for individual pieces.
* **`chess_images/`**: Folder containing asset files for piece rendering.

---

## Project Objectives

### 1. Board Logic & GUI Mechanics
* **Matrix Representation:** Maintain an 8x8 matrix to track pieces and board states.
* **Pygame Interface:** * Map mouse pointer $(x, y)$ coordinates to matrix indices via mathematical mapping.
    * Implement "Two-Click" move logic: Select piece $\rightarrow$ Select target.
* **Standard Rule Implementation:**
    * **Special Moves:** Validation for **Castling** (tracking King/Rook movement) and **En Passant**.
    * **Termination:** Detection of Check, Checkmate, the **50-move rule**, and **Insufficient Material** draws.
* **Capture System:** Remove captured pieces from the grid, update player scores, and log the event.

### 2. Move Validation Architecture
* **Mathematical Mappings:**
    * **Sliding Pieces (Rook/Bishop/Queen):** Check for path obstructions in the matrix.
    * **Knights:** Map specific relative indices ($m \pm 2, n \pm 1$).
    * **Pawns:** Validate 2-square opening moves and diagonal capture logic.
* **Legal Move Generator:** Take any board state and generate a list of all valid moves to prevent illegal user input.

### 3. AI Engine & Evaluation
* **Search Optimization:** * Implement **Minimax** recursion with **Alpha-Beta Pruning** to minimize search time.
    * Use **MCTS** for simulation and expansion of the game tree.
* **Heuristic Evaluation:**
    * **Piece-Square Tables:** Use position-based weights to encourage center control.
    * **Stockfish API:** Integrate external engine evaluations via `async/await` REST API calls for benchmarking and ELO calculation.
* **Neural Evaluation:** Train a **Chess Transformer** on FEN data to identify common openings and optimal endgame strategies.

### 4. Database & User Experience
* **Persistence:** Secure storage for usernames, passwords, and unique Player IDs.
* **Notation Support:** Real-time generation of **Standard Algebraic Notation (SAN)** for the UI and **Portable Game Notation (PGN)** for history logging.
* **Profile Tracking:** Display user stats including games played, win rate, and an estimated ELO rating.
