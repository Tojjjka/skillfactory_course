playing_field =  [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

dict_of_moves = {1: (0,0) , 2: (0,1), 3: (0,2), 4: (1,0),
                 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}


def print_playing_field():
    print(playing_field[0][0], end=" ")
    print(playing_field[0][1], end=" ")
    print(playing_field[0][2])

    print(playing_field[1][0], end=" ")
    print(playing_field[1][1], end=" ")
    print(playing_field[1][2])

    print(playing_field[2][0], end=" ")
    print(playing_field[2][1], end=" ")
    print(playing_field[2][2])


def check_for_player_win(list: list) -> str:
    win = ''
    if playing_field[0][0] == 'X' and playing_field[0][1] == 'X' and playing_field[0][2] == 'X':
        win = player1
    if playing_field[1][0] == 'X' and playing_field[1][1] == 'X' and playing_field[1][2] == 'X':
        win = player1
    if playing_field[2][0] == 'X' and playing_field[2][1] == 'X' and playing_field[2][2] == 'X':
        win = player1
    if playing_field[0][0] == 'X' and playing_field[1][1] == 'X' and playing_field[2][2] == 'X':
        win = player1
    if playing_field[0][2] == 'X' and playing_field[1][1] == 'X' and playing_field[2][0] == 'X':
        win = player1
    if playing_field[0][0] == 'X' and playing_field[1][0] == 'X' and playing_field[2][0] == 'X':
        win = player1
    if playing_field[0][1] == 'X' and playing_field[1][1] == 'X' and playing_field[2][1] == 'X':
        win = player1
    if playing_field[0][2] == 'X' and playing_field[1][2] == 'X' and playing_field[2][2] == 'X':
        win = player1
    if playing_field[0][0] == 'O' and playing_field[0][1] == 'O' and playing_field[0][2] == 'O':
        win = player2
    if playing_field[1][0] == 'O' and playing_field[1][1] == 'O' and playing_field[1][2] == 'O':
        win = player2
    if playing_field[2][0] == 'O' and playing_field[2][1] == 'O' and playing_field[2][2] == 'O':
        win = player2
    if playing_field[0][0] == 'O' and playing_field[1][1] == 'O' and playing_field[2][2] == 'O':
        win = player2
    if playing_field[0][2] == 'O' and playing_field[1][1] == 'O' and playing_field[2][0] == 'O':
        win = player2
    if playing_field[0][0] == 'O' and playing_field[1][0] == 'O' and playing_field[2][0] == 'O':
        win = player2
    if playing_field[0][1] == 'O' and playing_field[1][1] == 'O' and playing_field[2][1] == 'O':
        win = player2
    if playing_field[0][2] == 'O' and playing_field[1][2] == 'O' and playing_field[2][2] == 'O':
        win = player2
    return win


def player_move(symbol: str, move: int):
    k, v = dict_of_moves[move]
    playing_field[k][v] = symbol

def check_progress(text: str) -> int:
    while True:
        check = input(f'{text} сделайте ход: \n')
        if check.isdigit():
            check = int(check)
            k, v = dict_of_moves[check]
            if playing_field[k][v] != 'X' and playing_field[k][v] != 'O':
                return check
            else:
                print('\t\t\t!!!Это поле уже занято!!!\n\t\t\t\tПовторите попытку!')
                print_playing_field()
        else:
            print(f'{text} ввод осуществляется цифрой!')


player1 = input('Player1 - введите ваше имя: ')
player2 = input('Player2 - введите ваше имя: ')
game = False
player = True
steps_to_loss = 0

while game == False:
    print_playing_field()
    if player == True:
        symbol = 'X'
        move = check_progress(player1)
        steps_to_loss += 1
    else:
        symbol = 'O'
        move = check_progress(player2)
        steps_to_loss += 1
    player_move(symbol,move)
    win = check_for_player_win(playing_field)
    if win != '':
        game = True
        print(f'\t\t\t\tПобедил {win}!!!!')
        break
    else:
        game = False
    if steps_to_loss == 9:
        print('Ничья, свободных ходов больше нет!')
        break
    print(f'ходов до проигрыша{steps_to_loss}')
    player = not(player)






