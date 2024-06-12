import tkinter as tk
import numpy as np

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def minimax(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, -float('inf'), float('inf'), False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def reset_board():
    global board
    board = np.array([[" " for _ in range(3)] for _ in range(3)])
    update_buttons()
    result_label.config(text="")

def update_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j], state=tk.NORMAL if board[i][j] == " " else tk.DISABLED)

def click(row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        winner = check_winner(board)
        if winner:
            update_buttons()
            result_label.config(text=f"Player {winner} wins!")
            disable_buttons()
        elif is_draw(board):
            update_buttons()
            result_label.config(text="It's a draw!")
            disable_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"
            update_buttons()
            if current_player == "O":
                ai_move()

def ai_move():
    global current_player
    row, col = best_move(board)
    board[row][col] = current_player
    winner = check_winner(board)
    if winner:
        update_buttons()
        result_label.config(text=f"Player {winner} wins!")
        disable_buttons()
    elif is_draw(board):
        update_buttons()
        result_label.config(text="It's a draw!")
        disable_buttons()
    else:
        current_player = "O" if current_player == "X" else "X"
        update_buttons()

def disable_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)

def close_game():
    root.destroy()

# Initialize GUI
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
board = np.array([[" " for _ in range(3)] for _ in range(3)])
current_player = "X"

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2,
                                  command=lambda i=i, j=j: click(i, j))
        buttons[i][j].grid(row=i, column=j)

result_label = tk.Label(root, text="", font=('normal', 20))
result_label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", font=('normal', 20), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3)

close_button = tk.Button(root, text="Close", font=('normal', 20), command=close_game)
close_button.grid(row=5, column=0, columnspan=3)

root.mainloop()
