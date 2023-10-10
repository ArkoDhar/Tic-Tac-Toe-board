# Initialize the empty Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to print the Tic Tac Toe board
def print_board():
    print(" | ".join(board[:3]))
    print("-" * 9)
    print(" | ".join(board[3:6]))
    print("-" * 9)
    print(" | ".join(board[6:]))

# Function to check if a player has won
def check_win(player):
    # Check rows, columns, and diagonals
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full (a tie)
def check_tie():
    return " " not in board

# Main game loop
current_player = "X"
while True:
    print_board()
    move = input(f"Player {current_player}, enter your move (1-9): ")

    # Validate the input
    if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move) - 1] != " ":
        print("Invalid move. Try again.")
        continue

    # Update the board with the player's move
    board[int(move) - 1] = current_player

    # Check if the current player has won
    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins! Congratulations!")
        break

    # Check for a tie (board full)
    if check_tie():
        print_board()
        print("It's a tie! Game over.")
        break

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"
