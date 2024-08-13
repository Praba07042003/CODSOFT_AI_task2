import math
import random

# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):
    """Checks if there's a winner."""
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != EMPTY:
            return board[pos[0]]
    return None

def is_full(board):
    """Checks if the board is full."""
    return all(cell != EMPTY for cell in board)

def minimax(board, depth, is_maximizing):
    """The Minimax algorithm."""
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 10 - depth
    elif winner == PLAYER_O:
        return depth - 10
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Finds the best move for the AI."""
    best_move = None
    best_score = -math.inf
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    """Main function to play Tic-Tac-Toe against the AI."""
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        while True:
            try:
                player_move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= player_move < 9 and board[player_move] == EMPTY:
                    board[player_move] = PLAYER_O
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        if check_winner(board) == PLAYER_O:
            print_board(board)
            print("Congratulations, you win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI's move
        ai_move = find_best_move(board)
        board[ai_move] = PLAYER_X
        print(f"AI chooses position {ai_move + 1}.")
        print_board(board)

        if check_winner(board) == PLAYER_X:
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
