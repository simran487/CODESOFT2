# CODESOFT2

**Tic Tac Toe with Unbeatable AI**

This project implements a Tic Tac Toe game with a graphical user interface (GUI) using Python's tkinter library. The AI player is unbeatable, utilizing the Minimax algorithm with Alpha-Beta Pruning to make optimal moves.



**Features**

Player vs AI mode
Unbeatable AI using the Minimax algorithm with Alpha-Beta Pruning
Graphical interface using tkinter
Buttons to reset the game and close the application



**Prerequisites**

Python 3.x
tkinter (usually included with standard Python distributions)



**Core Functions**

check_winner(board): Checks if there is a winner on the board.
is_draw(board): Checks if the game is a draw.
minimax(board, depth, alpha, beta, is_maximizing): Implements the Minimax algorithm with Alpha-Beta Pruning.
best_move(board): Determines the best move for the AI.
reset_board(): Resets the game board.
update_buttons(): Updates the GUI buttons to reflect the current state of the board.
click(row, col): Handles player moves and alternates turns between the player and AI.
ai_move(): Executes the AI move.
disable_buttons(): Disables all buttons once the game is over.
close_game(): Closes the application.



**Running the Game**

The game starts with the player ('X') making the first move.
Click on a cell to place your mark.
The AI ('O') will make its move automatically after you.
The result of the game (win/loss/draw) will be displayed at the bottom.
Use the "Reset" button to start a new game.
Use the "Close" button to exit the application.
