# Database Design and Implementation

This project utilises a relational database structure managed via the `sqlite3` Python package. The database is designed to handle user authentication, game tracking, and move-by-move history using a normalized schema to ensure data integrity.

---

## Database Architecture

The system uses a relational model to link user profiles to their respective game histories and specific move sequences.

### 1. User Management Tables
* **`chess_users`**: Stores core authentication data.
    * **Fields:** `User ID` (Primary Key), `Date/Time Joined`, `Username`, and `Password` (Hashed).
    * **Logic:** A pre-registration check is performed to ensure usernames are unique before committing to the database.
* **`user_chess_info`**: Stores metadata and performance metrics for the user.
    * **Fields:** `userID` (Primary Key), `username`, `ELO rating`, and `Date Joined`.

### 2. Game & History Tracking
* **`user_game_history`**: Records individual game sessions.
    * **Logic:** Every game is assigned a unique `gameID`. It captures the full history of moves made by both the player and the AI engine.
* **`move_history`**: A granular look at every state of the board.
    * **Fields:** `moveID` (Primary Key), `board_fen_notation`, `move_string`, and `move_san`.
    * **Data Formats:** Stores board states in FEN (Forsyth–Edwards Notation) and moves in SAN (Standard Algebraic Notation).

### 3. Relational Link Tables (Many-to-Many Resolution)
To maintain a clean relational structure and avoid many-to-many conflicts, the following link tables are used:
* **`chess_users_games_link`**: Connects `chess_users` to `user_game_history`.
    * **Primary Key:** Composite (`userID`, `gameID`).
* **`game_move_history_link`**: Connects `user_game_history` to the specific `move_history` entries.
    * **Primary Key:** Composite (`gameID`, `moveID`).

---

## Technical Implementation

### Data Access & Security
* **SQL Integration:** All interactions (Creation, Activation, and Access) are handled via standard SQL queries executed through the `sqlite3` wrapper.
* **Privacy Logic:** The application layer ensures users can only query their own `gameID` records, preventing unauthorized access to other players' histories.
* **Password Security:** While functionality is the priority, the schema supports a **Hashing Algorithm** extension for password storage to follow security best practices.
* **Relational Integrity:** By using **Composite Primary Keys** in the link tables, the database ensures that every move and game is accurately mapped to the correct user without data redundancy.
