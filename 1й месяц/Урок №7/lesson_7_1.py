contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]

def create(contacts):
    print("Введите имя контакта:")
    name = input("> ")
    print("Введите телефон контакта:")
    phone = input("> ")
    new_contact = {'name': name, 'phone': phone}
    contacts.append(new_contact)
    print("Контакт добавлен и сохранён")

def edit(contacts):
    print("Введите имя контакта: ")
    name = input("> ")
    for index, contact in enumerate(contacts):
        if contact['name'] == name:
            print("Введите новое имя контакта: ")
            new_name = input("> ")
            print("Введите новый телефон контакта: ")
            new_phone = input("> ")
            contact_update = {
                'name': new_name,
                'phone': new_phone
            }
            contacts[index] = contact_update
            index = -1
            break
    if index == -1:
        print("Контакт изменен")
    else:
        print("Контакт не найден")

def delete():
    name = input('что удалить?')
    for contact in contacts:
        if name == contact["name"]:
            a = contacts.index(contact)
            del contacts[a]
    return contacts

while True:
    for i in contacts:
        print(f'{i}')
    dsf = input('выберите команду\n1)create\n2)edit\n3)delete')
    if dsf =='1':
        (create())
    elif dsf == '2':
        (edit(contacts))
    elif dsf == '3':
        (delete())





# lambda, и работа с исключениями
# lambda arguments: expression
# map, filter
# try:
#     code
# except:
#     message, define smth
# finally:
#     messsage


# word = 'python'
# while True:
#     try:
#         user_index = int(input('index? '))
#         print(word[user_index])
#     except:
#         print('только цифры от 0 до 5')
    # except ValueError:
    #     print('только цифры!')
    # except IndexError:
    #     print('нет такого индекса')


# from random import choice
# from time import sleep
#
# students = [2, 3, 5, 14, 7, 8, 9, 10, 11, 13, 19]
# answers = {}
#
# while len(students) != 0:
#     attempts = 2
#     print(students)
#     student_id = choice(students)
#     name = input(f'имя студента под номером {student_id}: ').title()
#     timer = 5
#     while timer != 0:
#         sleep(1)
#         print(timer)
#         timer -= 1
#     try:
#         while attempts != 0:
#             rate = int(input(f'оценка для {name}: попыток осталось: {attempts}'))
#     except:
#         attempts -= 1
#         print('только числа!')
#         continue
#     answers[name] = rate
#     students.remove(student_id)
#
# for name, rate in answers.items():
#     print(f'{name}: {rate}')
#
# print(sum(answers.values()) / len(answers))





# try:
#     print(int('23'))
# except:
#     print("неверный тип данных")
# finally:
#     print('проверка завершена')

# print('python'[7])
# print(name)


# numbers = list(range(1, 11))
# new = sorted(numbers, key=lambda x: x % 2 == 0, reverse=True)

# new = list(filter(lambda x: x < 5, numbers))
# new = [i for i in numbers if i <= 6]


# new = list(map(lambda x: x * 3, numbers))
# new = [i * 2 for i in numbers]

# print(numbers, new, sep='\n')





# lambda_func = lambda a, b: a + b
#
#
# def def_func(a, b):
#     return a + b
#
# print(type(lambda_func))
# print(type(def_func))
#
# print(lambda_func(2, 3))
# print(def_func(2, 3))


# def up_letter(word):
#     return word.title()
#
#
# def last_up(word):
#     return word[:-1] + word[-1].title()
#
#
# def show_words(func, seq):
#     for i in seq:
#         print(func(i))

# words = ('oop', 'python', 'django')
# show_words(lambda word: word.title(), ('oop', 'python', 'django'))
# show_words(lambda word: word[:-1] + word[-1].title(), words)
# show_words(up_letter, 'python')
# show_words(len, ['geektech', 'kgz', 'bishkek'])
