import random

import string  # Import the string module for uppercase letters

# ... (rest of the code remains the same)

def print_board(board):
    num_rows = len(board)
    num_cols = len(board[0])
    
    # Print column labels
    col_labels = " ".join(string.ascii_uppercase[:num_cols])
    print(f"  {col_labels}")
    
    for i, row in enumerate(board):
        row_str = " ".join(row)
        print(f"{i} {row_str}")

def is_winner(board, row, col, player):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dr, dc in directions:
        count = 1
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == player:
            count += 1
            r, c = r + dr, c + dc
        
        r, c = row - dr, col - dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == player:
            count += 1
            r, c = r - dr, c - dc
        
        if count >= 5:
            return True
            
    return False

def is_full(board):
    for row in board:
        if "." in row:
            return False
    return True

def player_move(board, player):
    while True:
        try:
            move = input("Enter your move (e.g., A3): ").upper()
            col, row = ord(move[0]) - ord('A'), int(move[1:])
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == ".":
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError, KeyError):
            print("Invalid input. Try again.")

def computer_move(board, player):
    empty_cells = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ".":
                empty_cells.append((row, col))
    
    # Check for winning move
    for row, col in empty_cells:
        board[row][col] = player
        if is_winner(board, row, col, player):
            return row, col
        board[row][col] = "."
    
    # Check for blocking opponent's winning move
    opponent = "O" if player == "X" else "X"
    for row, col in empty_cells:
        board[row][col] = opponent
        if is_winner(board, row, col, opponent):
            return row, col
        board[row][col] = "."
    
    # Random move
    return random.choice(empty_cells)

def play_gomoku():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    board = [["." for _ in range(cols)] for _ in range(rows)]
    players = ["X", "O"]
    current_turn = 0
    
    print("Welcome to Gomoku!")
    
    while True:
        print_board(board)
        player = players[current_turn]
        print(f"Player {player}'s turn.")
        
        if player == "X":
            player_move(board, player)
            row, col = None, None  # Initialize for later use
        else:
            row, col = computer_move(board, player)
            board[row][col] = player
        
        if row is not None and is_winner(board, row, col, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_turn = 1 - current_turn

if __name__ == "__main__":
    play_gomoku()