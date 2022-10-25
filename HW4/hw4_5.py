# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w') as file:
    file.write('3*x^3 + 5*x^5')
    file.close()
with open('poly_2.txt', 'w') as file:
    file.write('4*x^4 + 6*x^6')
    file.close()

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    x = poly_1.split()
with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    y = poly_2.split()
    file.close()
print(f'{x} + {y}')
with open('sum_poly.txt', 'w') as file:
    file.write(f'{x} + {y} = 0')
    file.close()