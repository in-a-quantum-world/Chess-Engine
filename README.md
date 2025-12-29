# Chess-Engine 
**A from-scratch Chess Engine and Gameplay Interface.**

This project features a custom chess engine that integrates traditional search algorithms with modern machine learning techniques. It is designed for both competitive play and as an educational tool for players to analyze their games.

---

## Overview
The engine serves as an AI thought partner for beginner to intermediate players. It provides a robust interface for gameplay while offering technical features such as:
* **Hybrid Search:** Combines Minimax with Monte Carlo Tree Search (MCTS).
* **Advanced Analysis:** FEN notation parsing, SQL-backed game history, and endgame tablebases.
* **Custom Logic:** Move validation, checkmate detection, and board state management built without external chess libraries.

---

## Tech Stack & Implementation
* **Language:** Python
* **GUI:** Pygame (Custom graphical representation and piece loading)
* **Database:** SQLite (Relational storage for user accounts and game history)
* **Logic:** Object-Oriented Programming (OOP) for piece classes and board matrices.

Instead of relying on existing libraries (like `python-chess`), all core mechanics—including valid move generation and terminal state detection—are implemented from the ground up to ensure maximum control over the game tree.

---

## Core Algorithms

### 1. Minimax & Alpha-Beta Pruning
To navigate the vast "decision forest" of chess, the engine employs a **Minimax** algorithm. This zero-sum strategy identifies the move that maximizes the engine's advantage while assuming the opponent will play perfectly to minimize it.



* **Optimization:** **Alpha-Beta Pruning** is used to "cut off" branches that are mathematically proven to be worse than previously explored options, significantly reducing computation time.
* **Succinctness:** In some implementations, the **Negamax** variant is used to handle the evaluation from a single perspective, negating scores for the opponent.

### 2. Monte Carlo Tree Search (MCTS)
Traditional tree searches are limited by the exponential growth of possible moves. To handle this complexity, I have integrated **MCTS** to balance **Exploration vs. Exploitation**.



* **Selection & Expansion:** The engine traverses the tree using the Minimax logic to prioritize high-value nodes.
* **Simulation (Exploitation):** Instead of searching the entire tree, the engine uses a **Pre-trained Transformer** to simulate game outcomes from a specific state, making the evaluation process far more efficient.
* **Back-propagation:** The results of simulations are fed back up the tree to update the value of each move.

---

## Search Strategies Employed

| Strategy | Function |
| :--- | :--- |
| **Depth First Search (DFS)** | Explores each branch to its maximum depth (or a set limit) before backtracking, ensuring memory efficiency. |
| **Cycle Detection** | Chess moves can be repetitive; the search tree identifies and ignores cycles to prevent infinite loops. |
| **Heuristic Evaluation** | Applies mathematical formulae to board variables (piece values, position, king safety) to output a winning probability. |
| **Random Move Gen** | A specialized module used for stress-testing the engine's stability and move-validation accuracy. |

---

## Future Objectives
* Implement more complex heuristic evaluation functions.
* Refine the Transformer's ability to interpret specific "Endgame Tablebase" patterns.
* Enhance the Pygame UI with move suggestions and real-time evaluation bars.alpha-beta algorithm would be optimal for finding the next best move. 
* Depth first search: Conducting a depth first search: this starts at the root of the tree and goes as far as possible along each branch of the tree, before backtracking. Main memory only needs to hold one path from the root to the lead at a time, so the program isn’t memory inefficient as such. 


