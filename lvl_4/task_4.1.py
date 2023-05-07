# Задача 4.1.
# Домашнее задание на SQL
import sqlite3

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


with sqlite3.connect('teatchers.db') as connection:
    cursor_for_create = connection.cursor()

    cursor_for_create.execute("""
    CREATE TABLE IF NOT EXISTS `students`(
    `Student_Id` INTEGER,
    `Student_Name` CHAR(128),
    `School_Id` INTEGER,
    FOREIGN KEY(`School_Id`) REFERENCES `School`(`id`),
    PRIMARY KEY (`Student_Id`))
    """)

data_for_insert_into_table = [
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4),
]

sql_request = """
INSERT OR REPLACE INTO `students` VALUES (?, ?, ?)
"""

with sqlite3.connect('teatchers.db') as conn:
    cursor_for_insert = conn.cursor()
    cursor_for_insert.executemany(sql_request, data_for_insert_into_table)


def get_info_about_student_and_school(student_ID: int):
    with sqlite3.connect('teatchers.db') as connect:
        cursor = connect.cursor()
        data_of_student = cursor.execute("""
        SELECT st.Student_Id, st.Student_Name, st.School_Id, sch.School_Name FROM `students` 'st' 
        JOIN `School` 'sch' ON st.School_Id = sch.School_Id
        WHERE st.Student_Id = {ID}
        """.format(ID=student_ID)).fetchall()

    format_of_output = (
        'ID Студента',
        'Имя студента',
        'ID школы',
        'Название школы'
    )
    data_of_student_for_output = dict(zip(format_of_output, data_of_student[0]))
    for key, value in data_of_student_for_output.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    student_id = 201
    get_info_about_student_and_school(student_id)
