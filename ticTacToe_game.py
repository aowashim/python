def display_board(board):
    print(f'     |     |    \n  {board[0]}  |  {board[1]}  |  {board[2]}  \n     |     |    ')
    print('-----------------')
    print(f'     |     |    \n  {board[3]}  |  {board[4]}  |  {board[5]}  \n     |     |    ')
    print('-----------------')
    print(f'     |     |    \n  {board[6]}  |  {board[7]}  |  {board[8]}  \n     |     |    ')
    
def whose_turn():
    rn = random.randint(1,2)
    if rn == 1:
        print("Player1 will choose first.")
    else:
        print("Player2 will choose first.")
    return rn

def choose_xo():
    player_info['player1'] = input("Player1 : Do you want be 'X' or 'O' ? ").upper()
    if player_info['player1'] == 'X':
        player_info['player2'] = 'O'
    else:
        player_info['player2'] = 'X'
        
def winner(board):
    ch = ''
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X'):
        return 'X'
    elif (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X'):
        return 'X'
    elif (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X'):
        return 'X'
    elif (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        return 'X'
    elif (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
        return 'O'
    elif (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O'):
        return 'O'
    elif (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return 'O'
    elif (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return 'O'
    
def player_input():
    choose_xo()
    pl_no = whose_turn()
    flag1 = ''
    count = 0
    while count != 9:
        pos = int(input('Choose your position betweeen (1-9) : '))
        if pl_no == 1:
            if board_lst[pos-1] != ' ':
                continue
            else:
                board_lst[pos-1] = player_info['player1']
                pl_no = 2
        elif pl_no == 2:
            if board_lst[pos-1] != ' ':
                continue
            else:
                board_lst[pos-1] = player_info['player2']
                pl_no = 1
        clear_output()
        count += 1
        display_board(board_lst)
        flag1 = winner(board_lst)
        if flag1 == 'X' or flag1 == 'O':
            return flag1

import random
from IPython.display import clear_output
board_lst = [' ']
player_info = {'player1':'','player2':''}
print("Welcome to Tic Tac Toe!")
yn = input("Are you ready to play? Enter 'Y' or 'N' : ").upper()
while yn == 'Y':
    board_lst = [' ']*9
    player_info = {'player1':'','player2':''}
    flag = player_input()
    if flag == 'X':
        if player_info['player1'] == 'X':
            print("Player1 is the Winner!")
        else:
            print("Player2 is the Winner!")
    elif flag == 'O':
        if player_info['player1'] == 'O':
            print("Player1 is the Winner!")
        else:
            print("Player2 is the Winner!")
    else:
        print("Match drawn!")
    yn = input("Do you want to play again? Enter 'Y' or 'N' : ").upper()