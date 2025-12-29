# AI Search Logic & Evaluation Metrics

This section explains the advanced search optimizations and the multi-layered evaluation methodology used to determine the "best" move.

---

## Search Optimization

### 1. Alpha-Beta Pruning & Negamax
The engine implements **Alpha-Beta Pruning** within a **Negamax** framework. Negamax is a variant of Minimax that simplifies the code by taking advantage of the zero-sum nature of chess: $max(a, b) = -min(-a, -b)$.

* **Logic:** The algorithm maintains two bounds: **Alpha** ($\alpha$), the minimum score the maximizing player is assured of, and **Beta** ($\beta$), the maximum score the minimizing player is assured of.
* **Pruning Condition:** If a branch is found where $\alpha \geq \beta$, that branch is "pruned" (discarded) because the opponent has already found a better alternative elsewhere.
* **Termination:** Searching stops immediately if a terminal state (Checkmate) is identified or if the evaluation falls below a critical threshold (e.g., 50% win probability).



---

## Neural Network & Transformer Architecture

### Role of the Transformer
Unlike traditional engines that use handcrafted features, this engine uses a **Transformer-based Neural Network** to predict game outcomes directly from the board state.
* **Input Encoding:** The board is converted into an $8 \times 8 \times 12$ NumPy matrix (representing 12 piece types across 64 squares).
* **Recurrent Learning:** The model utilizes historical game data to understand the "flow" of the game, helping it identify common openings and endgame patterns.
* **Simplification:** By predicting a game’s result early, the transformer allows the **Monte Carlo Tree Search (MCTS)** to prioritize high-value branches, drastically reducing the required search depth.

### Model Layers
The model follows a **Sequential Architecture**:
1.  **Convolutional Layers:** Detect spatial patterns (e.g., pawn chains, king safety).
2.  **Flatten & Dense Layers:** Process these features into abstract strategic concepts.
3.  **Softmax Output:** Produces a probability distribution over the likelihood of a Win, Loss, or Draw.

---

## Detailed Evaluation Methods

The engine combines static heuristics with real-time API data to produce a final "Score."

### 1. Stockfish API Metrics
When using the Stockfish integration, the engine processes the following metrics via a REST API:
* **Eval (Centipawns):** A "Centipawn" is $1/100th$ of a pawn. 
    * `+100` means White is ahead by 1 pawn.
    * `+300` suggests an advantage equivalent to a Minor Piece (Bishop/Knight).
* **WinChance:** A normalized percentage (0% to 100%) representing the statistical probability of victory based on millions of master-level games.
* **Centipawn Loss:** Measured during game analysis to calculate the "accuracy" of human moves compared to the engine's top choice.

### 2. Piece-Square Tables (PST)
To ensure the AI understands positional value (not just material count), every piece has a 64-entry matrix.
* **Example:** A Knight has a higher score in the center (e.g., `+20`) than in a corner (e.g., `-10`), encouraging the AI to "develop" its pieces toward the middle of the board.
* **Phase Weighting:** Tables are updated dynamically; for instance, the King's PST shifts from "Defensive/Corner" in the mid-game to "Aggressive/Center" in the endgame.



### 3. Shortest Path & Vectors
The engine treats moves as **Vectors**. For endgames, it uses a shortest-path recursive search to find the most efficient route to checkmate, treating each legal move as a coordinate shift in the $8 \times 8$ matrix.

---

##  Data Processing Workflow
1.  **Read PGN:** Load raw game data from Lichess.org.
2.  **FEN Mapping:** Convert current state to **Forsyth–Edwards Notation** using BNF syntax.
3.  **Matrix Transformation:** Convert FEN into a 3D NumPy array for the Neural Network.
4.  **Inference:** Fetch Stockfish evaluation or use the local Transformer to score the position.
5.  **Pruning:** Use the score to prune the MCTS tree and execute the move.
