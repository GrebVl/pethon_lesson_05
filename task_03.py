# Создайте программу для игры в ""Крестики-нолики"".
import random


def player_turn(list_, num_user):
    print(f'Ход игрока {num_user}')
    x, y = map(int, input('Введите кординату X и Y через пробел(пример: 2 2): ').split(' '))
    for i in range(len(list_)):
        if list_us[i] == (x,y) and num_user == 1:
            list_us[i] = '  X   '
            break
        elif list_us[i] == (x,y) and num_user == 2:
            list_us[i] = '  0   '
            break
    return list_


def game_over(list_):
    if list_[0] == list_[1] == list_[2]\
            or list_[3] == list_[4] == list_[5]\
            or list_[6] == list_[7] == list_[8]:
        print('\n'
              'Конец игры\n'
              '')
        return True
    elif list_[0] == list_[3] == list_[6] \
            or list_[1] == list_[4] == list_[7] \
            or list_[2] == list_[5] == list_[8]:
        print('\n'
              'Конец игры\n'
              '')
        return True
    elif list_[0] == list_[4] == list_[8] \
            or list_[2] == list_[4] == list_[6]:
        print('\n'
              'Конец игры\n'
              '')
        return True


def tic_tac_toe(list_):
    print(
         '     |  1   |   2  |   3   \t\n'
          f'  1  |{list_[0]}|{list_[1]}|{list_[2]}\n'
          f'-----|------|------|--------\t\n'
          f'  2  |{list_[3]}|{list_[4]}|{list_[5]}\n'
          f'-----|------|------|--------\t\n'
          f'  3  |{list_[6]}|{list_[7]}|{list_[8]}\n'
)


list_us = [(1,1), (1,2), (1,3),
         (2,1), (2,2), (2,3),
         (3,1), (3,2), (3,3)]

tic_tac_toe(list_us)
count = 9
num_us = random.randrange(1, 3)

while count != 0 and count > 0:
    if num_us == 1:
        list_us = player_turn(list_us, num_us)
        tic_tac_toe(list_us)
        num_us = 2
        count -= 1
        if game_over(list_us) == True:
            count = 0
            break
    elif num_us == 2:
        list_us = player_turn(list_us, num_us)
        tic_tac_toe(list_us)
        num_us = 1
        count -= 1
        if game_over(list_us) == True:
            count = 0
            break
