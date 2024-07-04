grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в список и сортируем по алфавиту
students_list = sorted(students)

# Создаем пустой словарь для хранения средних оценок
average_grades = {}

# Заполняем словарь
for i, student in enumerate(students_list):
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    average_grades[student] = average_grade


print(average_grades)




