# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
def player_turn(num_user, candies):
    print(f'Ход игрока {num_user}')
    count_ = 1
    while count_ == 1:
        user_ = str(input('Введите число от 1 до 28: '))
        if user_.isdigit() == True:
            user_ = int(user_)
            if user_ <= 0 or user_ > 28:
                count = 1
                print(f'Указанное значение {user_} не находится в диапозоне от 1 до 28')
            elif user_ > candies:
                print(f'Указанное значение {user_} привышает количество конфет {candies}')
            elif user_ >= 1 and user_ <= 28:
                break
        elif user_.isdigit() == False:
            count = 1
            print(f'Указанное значение {user_} является строкой,\n'
                  f' введите числовой форме в диапозон от 1 до 28')
    candies -= user_
    return candies

def game_over(num_user, candies):
    print('\n'
          'Конец игры\n'
          '')
    if candies == 0 and num_user == 2:
        print('Проиграл игрок 2\n'
              'Победил игрок 1\n'
              f'количество раундов: {round}')
    elif candies == 0 and num_user == 1:
        print('Проиграл игрок 1\n'
              'Победил игрок 2\n'
              f'количество раундов: {round}')


numbers_candies = 2021
round = 1
print(
    'На столе лежит 2021 конфета.\n'
    'Играют два игрока делая ход друг после друга.\n'
    'Первый ход определяется жеребьёвкой.\n'
    'За один ход можно забрать не более чем 28 конфет.\n'
    'Все конфеты оппонента достаются сделавшему последний ход.'
)
num_us = random.randrange(1, 3)

while numbers_candies != 0 and numbers_candies > 0:
    print(f'раунд {round}')
    print(f'На столе лежит {numbers_candies} конфета.')
    if num_us == 1:
        numbers_candies = player_turn(num_us, numbers_candies)
        num_us = 2
        round += 1
    elif num_us == 2:
        numbers_candies = player_turn(num_us, numbers_candies)
        num_us = 1
        round += 1

game_over(num_us, numbers_candies)