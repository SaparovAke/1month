# Структуры данных: словари, множества.
# {key: value}
# dict - dictionary (словарь)
# set - множество

# from random import choice
# from time import sleep
#
# students = [2, 3, 5, 14, 7, 8, 9, 10, 11, 13, 19]
# answers = {}
#
# while len(students) != 0:
#     print(students)
#     student_id = choice(students)
#     name = input(f'имя студента под номером {student_id}: ').title()
#     timer = 20
#     while timer != 0:
#         sleep(1)
#         print(timer)
#         timer -= 1
#     rate = int(input(f'оценка для {name}: '))
#     answers[name] = rate
#     students.remove(student_id)
#
# for name, rate in answers.items():
#     print(f'{name}: {rate}')
#
# print(sum(answers.values()) / len(answers))







# word = 'инвентаризация'
# word = set(word)
# print(word)

# plov = {"рис", "морковь", "мясо"}
# manty = {"тесто", "мясо", "лук"}
#
# plov.add('чеснок')
# plov.update(['лук', "перец"])
# plov.remove("перец")
# print(plov)

# print(plov.difference(manty))
# print(plov - manty)
#
# print(plov.intersection(manty))
# print(plov & manty)
#
# print(plov.union(manty))
# print(plov | manty)
#
#
# print(plov.symmetric_difference(manty))
# print(plov ^ manty)


# numbers = {1, 2, 3, 3, 1, 2, 4}
# numbers2 = [1, 2, 3, 3, 1, 2, 4]
#
# print(type(numbers))
# print(numbers)
# print(numbers2)


# regions = ['chuy', 'osh', 'talas', 'batken', 'y-k', 'jalal-abad', 'naryn']
# data = {i: int(input(f'сколько градусов в {i}')) for i in regions}
# print(f"средняя температура по КР {round(sum(data.values()) / len(data), 2)}")

# new = dict(name='alina', age='20', country='kg')
# new = dict([[2, 'q'], ['w', 'e'], ['r', 't']])
# new = dict(enumerate('python'))
# print(new)


# numbers = [i*i for i in range(1, 6)]
# numbers2 = {i: i*i for i in range(1, 6)}
#
# print(numbers)
# print(numbers2)

# student = {
#     'name': 'Ishak',
#     'age': 16,
#     'hobby': ['бег', "плавание", "шахматы"],
#     'married': False
# }
#
# for key, value in student.items():
#     print(f'{key} >> {value}')

# for i in student:
#     print(f'{i}: {student[i]}')

# print(student.keys())
# print(student.values())
# print(student.items())


# print(student['nam'])
# print(student.get('name', 'такого ключа нет!'))


"""add"""
# student['height'] = 1.71
# student['hobby'].append('football')
# student.update(new)

"""edit"""
# student['married'] = True
# student['age'] += 1
# student['hobby'][0] = 'programming'

"""delete"""
# del student['hobby'][1]
# del student['married']
# deleted = student.pop('hobby')
# print(deleted)

# print(type(student))
