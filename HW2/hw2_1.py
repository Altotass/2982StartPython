# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.    
#     Пример:    
#     - 6782 -> 23
#     - 0,56 -> 11

x = input('Введите вещественное число х = ')
print(type(x))
sum = 0
for i in x:
    if i != '.' and i != '-' and i != ',':
        sum += int(i)
print(sum)