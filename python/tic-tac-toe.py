import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win or a draw
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Draw'
    return None

# Function for the AI to make a move
def ai_move(board):
    # Check if AI can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_winner(board) == 'O':
                    return
                board[i][j] = ' '

    # Check if the player can win and block
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_winner(board) == 'X':
                    board[i][j] = 'O'
                    return
                board[i][j] = ' '

    # Choose a random empty spot
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    i, j = random.choice(empty_spots)
    board[i][j] = 'O'

# Function for the player to make a move
def player_move(board):
    while True:
        move = input("Enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter two numbers.")
            continue
        i, j = int(move[0]), int(move[1])
        if i not in range(3) or j not in range(3):
            print("Invalid move. Please try again.")
        elif board[i][j] != ' ':
            print("Spot already taken. Please try again.")
        else:
            board[i][j] = 'X'
            break

# Main function to run the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        result = check_winner(board)
        if result:
            break

        ai_move(board)
        print("AI made a move:")
        print_board(board)
        result = check_winner(board)
        if result:
            break

    if result == 'Draw':
        print("It's a draw!")
    else:
        print(f"{result} wins!")

if __name__ == "__main__":
    play_game()
