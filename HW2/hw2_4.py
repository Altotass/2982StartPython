# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#    Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random
N = int(input('Ввести целое число ')) 
my_list = range(0, N)
value_list = [random.randint(-N, N) for _ in my_list]
print(value_list)
with open('1.txt', 'w') as file:
    for i in value_list:
            file.write(str(i)+'\n')
x = int(input('Введите позицию первого элемента: '))
y = int(input('Введите позицию второго элемента: '))
mult = 0
with open('1.txt', 'r') as file:
    for i in range(N):
        mult = value_list[x - 1]*value_list[y - 1]
    print(f'Произведение элементов: {value_list[x - 1]} * {value_list[y - 1]} =', mult)