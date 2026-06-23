'''
Tic Tac Toe Game
Author: Christopher
This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players to take turns marking spaces on a 3x3 grid, with the goal of getting three of their markers in a row (horizontally, vertically, or diagonally) before their opponent does. The game also checks for a draw if all spaces are filled without a winner.
features:
- Two player gameplay
- Input validation 
- Win detection
- Draw detection
- Replay option
'''
import random
def intro():
    print('Welcome to Tic Tac Toe')
def start():
    game = 'enter'
    while game not in ['Yes', 'No']:
        game = input('Select Yes or No to start the game: ')
        if game not in ['Yes', 'No']:
            print('Try again')
    if game == 'Yes':
        return True
    else:
        return False
def display_board(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
def player_marker():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Select a marker (X. O): ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O', 'X')
def place_marker(board,marker,position):
    board[position - 1] = marker
def win_check(board, mark):
    return ((board[0] == board[1] == board[2] == mark)or
            (board[3] == board[4] == board[5] == mark)or
            (board[6] == board[7] == board[8] == mark)or
            (board[0] == board[3] == board[6] == mark)or
            (board[1] == board[4] == board[7] == mark)or
            (board[2] == board[5] == board[8] == mark)or
            (board[0] == board[4] == board[8] == mark)or
            (board[2] == board[4] == board[6] == mark))
def space_check(board, position):
    return board[position] == ' '
def full_board(board):
    return ' ' not in board
def player_input(board, marker):
    position = int(input('Choose a side (1-9): '))
    if space_check(board, position - 1):
        place_marker(board,marker,position)
    else:
        print('Choose another side')
        player_input(board, marker)
def replay(): 
    game_on = 'wrong'
    while game_on not in ['Yes', 'No']:
        game_on = input('Would you like to play again (Yes or No): ')
        if game_on not in ['Yes', 'No']:
            print('Select Yes or No')
    return game_on == 'Yes'
# -------------------------------------------GameLoop--------------------------------------------------
intro()
while True:
    board = [' '] * 9
    game_on = start()
    if not game_on:
        print('Game Exited')
        break
    player1_marker, player2_marker = player_marker()
    turn = random.choice(['Christopher','Calypso'])
    print(turn + ' will go first')
    
    
    while game_on:
        display_board(board)
        if turn == 'Christopher':
            player_input(board,player1_marker)
            if win_check(board,player1_marker):
                display_board(board)
                print('Christopher has won!!!')
                game_on = False
            elif full_board(board):
                display_board(board)
                print('Tie Game')
                game_on = False
            else:
                turn = 'Calypso'
        else:
            player_input(board,player2_marker)
            if win_check(board,player2_marker):
                display_board(board)
                print('Calypso has won!!!')
                game_on = False
            elif full_board(board):
                display_board(board)
                print('Tie Game')
                game_on = False
            else:
                turn = 'Christopher'
    if not replay():
        print('Thanks for playing')
        break