# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)


import random


class Matrix:

    def __init__(self, count_columns=None, count_rows=None, number=None):
        self.count_columns = count_columns
        self.count_rows = count_rows
        self.number = self.__check_number(number)
        self.__matrix = self.__get_matrix()

    @staticmethod
    def __check_number(number):
        if not number or 1 <= number <= float('inf'):
            return number
        try:
            raise ValueError
        except ValueError:
            print('Значение "number" должно быть больше 1!')

    def __get_matrix(self):
        if not self.count_columns:
            self.count_columns = random.randint(1, 20)
        if not self.count_rows:
            self.count_rows = random.randint(1, 20)
        return [[self.number for _ in range(self.count_columns)] for _ in range(self.count_rows)]

    def set_new_number(self, new_number):
        self.number = new_number
        self.__matrix = self.__get_matrix()

    def change_current_number(self, number_of_row, number_of_column, number):
        number = self.__check_number(number)
        try:
            self.__matrix[number_of_row - 1][number_of_column - 1] = number
        except IndexError as exc:
            print('Неверный номер строки/столбца:', exc)

    def counts_number_columns_and_rows(self):
        return f'Кол-во строк: {self.count_rows}, кол-во колонок: {self.count_columns}'

    def __str__(self):
        return '\n'.join([''.join(['%s\t' % i for i in row]) for row in self.__matrix])


my_matrix = Matrix(count_columns=4, count_rows=3, number=35)
print(my_matrix, end='\n\n')

my_matrix.set_new_number(3)
print(my_matrix, end='\n\n')

my_matrix.change_current_number(number_of_row=3, number_of_column=3, number=41)
print(my_matrix, end='\n\n')

print(my_matrix.counts_number_columns_and_rows())
