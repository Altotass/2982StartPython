# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('Введите натуральную степень k = '))
koef = [randint(0,100) for i in range(k)]+[randint(1,100)]
result = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koef ) if j][::-1])
print(result)
result = result.replace('x^1+', 'x+')
result = result.replace('x^0', '')
result += ('','1')[result[-1] == '+']
result = (result, result[:-2])[result[-2:]=='^1']
print(result + ' = 0')
with open('3.txt', 'w') as file:
    file.write(result + ' = 0')
    file.close()