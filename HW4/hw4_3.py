# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
x = int(input('Задайте последовательность чисел = '))
lst1 = []
lst2 = []
for i in range(x):
    lst1.append(randint(1, 20))
print(lst1)

for i in range(x):
    if lst1.count(lst1[i]) > 1:
        i += 1
    else:
        lst2.append(lst1[i])
print(lst2)