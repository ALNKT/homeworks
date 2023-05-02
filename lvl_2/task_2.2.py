# Задача 2.2.
import datetime


# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.


def quarter_of(month):
    full_name_of_month = datetime.datetime.strptime(str(month), "%m").strftime("%B")
    for months, quarter in [
        ([1, 2, 3], 1),
        ([4, 5, 6], 2),
        ([7, 8, 9], 3),
        ([10, 11, 12], 4)
    ]:
        if month in months:
            return f'Месяц {month} ({full_name_of_month}) является частью {quarter} квартала'


print(quarter_of(int(input('Укажите номер месяца: '))))
