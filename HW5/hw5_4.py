# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# FFFBBBCCCCTTTTGTTT -> 3F3B4C4T1G3T

with open('RLE_encode.txt', 'w') as data:
    data.write('FFFBBBCCCCTTTTGTTT')
with open('RLE_encode.txt', 'r') as data:
    string = data.readline()
print('Начальная строка : ' + string)

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
    else:        
        encoded_string = encoded_string + str(count) + char
        return encoded_string

def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
        return decoded_string

with open('RLE_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('RLE_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Зашифрованная строка : ' + rle_encode(decoded_string))
print('Расшифрованная строка : ' + decoded_string)