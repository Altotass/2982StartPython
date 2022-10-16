# 5. Реализуйте алгоритм перемешивания списка

list1 = [6, 2, 7, 4, 5]
print(list1)
list2 = list1
for i in range(len(list1)): 
    for j in range(len(list1) - 1): 
        if list2[j] > list2[j + 1]: 
            temp = list2[j] 
            list2[j] = list2[j + 1] 
            list2[j + 1] = temp 
print(list2)