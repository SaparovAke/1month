# Функции, аргументы: *args, **kwargs.
# def - definition (определение)
# DRY - don't repeat yourself


""" ДОП ЗАДАНИЕ
Создать четвёртую команду для вывода среднего значения оценки."""

students_rates = {
    'iskhak': 2,
    'jyrgal': 3,
    'aitbek': 3
}


def find_student(name):
    # return True if name in students_rates.keys() else False
    if name in students_rates.keys():
        return True
    return False


def add(name: str, rate: int):
    if not find_student(name):
        if 5 >= rate >= 1:
            students_rates[name] = rate
        else:
            print('оценка от 1 до 5!')
    else:
        print(f'{name} уже есть!')


def delete(name):
    if find_student(name):
        del students_rates[name]
    else:
        print(f'{name} не существует!')


def edit(name, new_name):
    if find_student(name):
        students_rates[new_name] = students_rates.pop(name)


while True:
    print(students_rates)
    command = input(f'1) add\n'
                    f'2) edit\n'
                    f'3) delete\n')
    if command == '1':
        add(name=input('name to add: '), rate=int(input('rate: ')))
    elif command == '2':
        edit(name=input('old name: '), new_name=input('new name: '))
    elif command == '3':
        delete(name=input('name for delete: '))
    else:
        print('выбирайте из списка!')




# def menu(**kwargs):
#     return sum(kwargs.values())
#
# print(menu(a=1, b=2, drink=145))

# def plus(a, *args, b=1):
#     print(a, b, args)
#     return sum(args) / a
#
# print(plus(2, 3, 7, 1, 8, 89, 12))



# def min1(seq):
#     return sorted(seq)[-1]
#
# print(min1([2, 6, 1, 7, 8]))

# print(min([1, 4, 5, 7, 0.5]))
# print(max([1, 4, 5, 7, 0.5]))



# def len1(seq):
#     counter = 0
#     for _ in seq:
#         counter += 1
#     return counter
#
#
# print(len1('geektech') + 5)
# print(len('geektech') + 5)


# def greet(name, surname='unknown'):  # name - обязательный позиционный параметр
#     print(f'name: {name}, surname: {surname}')

# greet(name=input('укажите имя: '), surname=input('фамилия: '))
# greet('samat', 'aliev')  # samat - обязательный позиционный аргумент
# greet('jyrgal', 'alymbekov')
# greet(surname='timurova', name='bermet')  # именованные аргументы (keyword arguments)


# def get_area(width: int, length: int) -> int:
#     """
#     Принимает ширину и длину, возвращает площадь.
#     """
#     print(width, length)
#     return width * length
#
# print(get_area.__doc__)
# # print(help(str))
#
# square_2 = get_area(6, 8)
# square_hall = get_area(8.5, 20)
# print(square_2 + square_hall, sep='\n')

# width = 6
# length = 8
# square_2 = width * length
# print(square_2)
#
# width = 8.5
# length = 20
# square_hall = width * length
# print(square_hall)
