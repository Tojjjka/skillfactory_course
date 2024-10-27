playing_field =  [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

dict_of_moves = {'1': (0,0) , '2': (0,1), '3': (0,2), '4': (1,0),
                 '5': (1,1), '6': (1,2), '7': (2,0), '8': (2,1), '9': (2,2)}


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


def check_for_player_win() -> bool:
    if playing_field[0][0] == playing_field[0][1] == playing_field[0][2]:
        return True
    elif playing_field[1][0] == playing_field[1][1] == playing_field[1][2]:
        return True
    elif playing_field[2][0] == playing_field[2][1] == playing_field[2][2]:
        return True
    elif playing_field[0][0] == playing_field[1][1] == playing_field[2][2]:
        return True
    elif playing_field[0][2] == playing_field[1][1] == playing_field[2][0]:
        return True
    elif playing_field[0][0] == playing_field[1][0] == playing_field[2][0]:
        return True
    elif playing_field[0][1] == playing_field[1][1] == playing_field[2][1]:
        return True
    elif playing_field[0][2] == playing_field[1][2] == playing_field[2][2]:
        return True
    else:
        return False

def make_move(symbol: str, move: int):
    k, v = dict_of_moves[move]
    playing_field[k][v] = symbol

def check_and_accept_player_input(text: str) -> str:
    while True:
        player_move = input(f'{text} сделайте ход: \n')
        if player_move in dict_of_moves.keys():
            k, v = dict_of_moves[player_move]
            if playing_field[k][v] != 'X' and playing_field[k][v] != 'O':
                return player_move
            else:
                print('\t\t\t!!!Это поле уже занято!!!\n\t\t\t\tПовторите попытку!')
                print_playing_field()
        else:
            print('Нельзя сделать такой ход')


player1 = input('Player1 - введите ваше имя: ')
player2 = input('Player2 - введите ваше имя: ')
player = True
steps_to_draw = 0
win = False

while True:
    print_playing_field()
    if player:
        symbol = 'X'
        move = check_and_accept_player_input(player1)
        steps_to_draw += 1
    else:
        symbol = 'O'
        move = check_and_accept_player_input(player2)
        steps_to_draw += 1
    make_move(symbol, move)
    win = check_for_player_win()
    if win:
        if player:
            print(f'\t\t\t\tПобедил {player1}!!!!')
        else:
            print(f'\t\t\t\tПобедил {player2}!!!!')
        break
    if steps_to_draw == 9:
        print('Ничья, свободных ходов больше нет!')
        break
    player = not player



