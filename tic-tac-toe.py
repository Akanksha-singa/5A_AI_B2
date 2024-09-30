import random
print("Akanksha Singa")
print("1BM22CS027")
# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_full():
    return all(cell != ' ' for row in board for cell in row)

def find_best_move(player):
    # Check for winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if check_winner() == player:
                    return (i, j)  # Winning move
                board[i][j] = ' '  # Undo the move

    # Check for blocking moves
    opponent = 'X' if player == 'O' else 'O'
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = opponent
                if check_winner() == opponent:
                    board[i][j] = ' '  # Undo the move
                    return (i, j)  # Block opponent's winning move
                board[i][j] = ' '  # Undo the move

    return None  # No immediate winning or blocking move

def random_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else None

# Main game loop
while True:
    print_board()
    
    # User's turn
    row, col = map(int, input("Enter your move (row and column): ").split())
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = 'X'  # User's move
    else:
        print("Invalid move. Try again.")
        continue

    if check_winner() or is_full():
        break

    # AI's turn
    ai_move = find_best_move('O')  # Check for winning move
    if ai_move is None:
        ai_move = find_best_move('X')  # Check for blocking move
    if ai_move is None:
        ai_move = random_move()  # Make a random move
    
    if ai_move:
        board[ai_move[0]][ai_move[1]] = 'O'  # AI's move

    if check_winner() or is_full():
        break

# Final result
print_board()
winner = check_winner()
if winner == 'X':
    print("You win!")
elif winner == 'O':
    print("AI wins!")
else:
    print("It's a draw!")
