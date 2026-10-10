
def display_board(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('  _  |  _  |  _  ')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('  _  |  _  |  _  ')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('  _  |  _  |  _  ') 

def get_player_move(board, player):
    
    while True:    
        user_input = (input("Choose the number for your move {}.".format(player)))
        if user_input.isdigit():
            move = int(user_input)
            if move in range(1, 10) and board[move] == " ":
                return move 
        print("Invalid move, cell is occupied or not in 1-9. Try again!")

def check_win(board, mark):
    horizontal = (board[7] == board[8] == board[9] == mark) or \
    (board[4] == board[5] == board[6] == mark) or \
    (board[1] == board[2] == board[3] == mark)
    vertical = (board[7] == board[4] == board[1] == mark) or \
    (board[8] == board[5] == board[2] == mark) or \
    (board[9] == board[6] == board[3] == mark)
    diagonal = (board[7] == board[5] == board[3] == mark) or \
    (board[9] == board[5] == board[1] == mark)
    return horizontal or vertical or diagonal

def is_board_full(board):
    return " " not in board[1:]

print("Let's play Tic-Tac-Toe!")

def play_game():
    board = [' '] * 10
    current_player = "X"
    while True:
        display_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! {current_player} is the winner!")
            break
        if is_board_full(board):
            display_board(board)
            print("The game is a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()