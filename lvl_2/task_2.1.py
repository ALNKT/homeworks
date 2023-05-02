# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    min_number = float('inf')
    for i_num in arr:
        if i_num < min_number:
            min_number = i_num
    print(f'min = {min_number}')


def maximum(arr):
    max_number = float('-inf')
    for i_num in arr:
        if i_num > max_number:
            max_number = i_num
    print(f'max = {max_number}')


minimum([4, 6, 2, 1, 9, 63, -134, 566])
maximum([4, 6, 2, 1, 9, 63, -134, 566])
