# 1. Создайте программу для игры с конфетами человек против человека.    
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?    
#     a) Добавьте игру против бота    
#     b) Подумайте как наделить бота "интеллектом"    

from random import randint
one = 'Игрок 1'
two = 'Игрок 2'
y = candy = 100
max = 28

count = 0
x = randint(1, 2)

if x == 1:
    player1 = one
    player2 = two
else:
    player1 = two
    player2 = one
print(f'{player1} - ходит первым!')

while y > 0:
    if count == 0:
        numb = int(input(f'\nТвой ход {player1} = '))
        if numb > y or numb > max:
            numb = int(input(f'можно взять только {max} конфет: '))
        y = y - numb
    if y > 0:
        print(f'осталось {y}')
        count = 1

    if count == 1:
        numb = int(input(f'\nТвой ход {player2} = '))
        if numb > y or numb > max:
            numb = int(input(f'можно взять только {max} конфет: '))
        y = y - numb
    if y > 0:
        print(f'осталось {y}')
        count = 0
if count == 1:
    print(f'{one} ПОБЕДИЛ')
if count == 0:
    print(f'{two} ПОБЕДИЛ')

exit()
from random import randint
y = candy = 150
max = 28
one = 'Игрок'
two = 'Компьютер'
players = [one, two]
start = randint(-1, 0)
print(start)
print(f'{players[start + 1]} ходит первым !')

while y > 0:
    start += 1
    if players[start % 2] == 'Компьютер':
        print(f'Ходит {players[start % 2]} \nНа кону {y}: ')

        if y < 29:
            numb = y
        else:
            delet = y // 28
            numb = y - ((delet * max) + 1)
            if numb == -1:
                numb = max - 1
            if numb == 0:
                numb = max
        while numb > 28 or numb < 1:
            numb = randint(1,28)
        print(numb)
    else:
        numb = int(input(f'Ходит, {players[start % 2]} \nНа кону {y}:  '))
        while numb > max or numb > y:
            numb = int(input(f'можно взять только {max} конфет: '))
    y = y - numb
print(f'На кону осталось {y} \nПобедил {players[start % 2]}')