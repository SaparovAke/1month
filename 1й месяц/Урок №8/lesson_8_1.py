# Работа с файлами.
# w - write запись, перезапись
# a - add дозапись
# x - безопасный режим создания файла

from datetime import datetime
import time
# start = datetime.now()
# print(start)
# time.sleep(5)
#
# end = datetime.now() - start
# print(end.seconds)

# 16, 31, 50, 70, 99, 98, 85, 84, 81, 79, 71, 77, 73, 74, 76
# 50, 25, 36, 30, 27




# answers = []
#
#
# with open('results.txt', 'r') as file:
#     for line in file.readlines():
#         name = line.split()[0]
#         seconds = line.split()[-2]
#         status = line.split()[-1]
#         answers.append(
#             {'name': name, 'seconds': seconds, 'status': status}
#         )
#
# for i in answers:
#     print(i if i['status'] == 'неправильно' else '')



# with open('results.txt', 'w') as file:
#     file.write('')
#
# from random import randint, choice
# students = [2, 3, 4, 6, 9, 10, 11, 13, 12, 7]
#
# while len(students) != 0:
#     first = randint(2, 10)
#     second = randint(11, 101)
#     student_id = choice(students)
#     name = input(f'name: {student_id}').title()
#     start = datetime.now()
#     user_answer = int(input(f"сколько будет {first} * {second} = "))
#     end = datetime.now() - start
#     right_answer = first * second
#
#     if user_answer == right_answer:
#         print(True)
#         with open('results.txt', 'a') as file:
#             file.write(
#                 f"{name} {first} * {second} = {user_answer} ({right_answer})"
#                 f" {end.seconds} правильно\n"
#             )
#     else:
#         print(False, right_answer)
#         with open('results.txt', 'a') as file:
#             file.write(
#                 f"{name} {first} * {second} = {user_answer} ({right_answer})"
#                 f" {end.seconds} неправильно\n"
#             )
#     students.remove(student_id)


# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан!')
# file.close()

# with open('file.txt', 'a') as file:
#     file.write('\n2222')

# with open('file.txt', 'x') as file:
#     file.write('123123123')

# from time import sleep as ukta
#
# with open('file.txt', 'r') as file:
#     for i in file.read().split():
#         ukta(1)
#         print(i, end=' ')

    # print(file.readlines()[3])
    # print(file.readline())
    # print(file.readline())
    # print(file.read())






low = 0
high = 100
mid = (low + high) // 2
i = 0
with open('results.txt', 'w', encoding='UTF-8') as file:
    file.write('Угадай цифру\n')

while True:
    print(f"Вы загадали {mid}?")
    user_answer = input(" 'Да' или '<' или '>': ")
    i += 1
    if user_answer.lower() == 'да':
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Попытки: {i}\n")
            file.write(f"Ваше число: {mid}\n")
            file.write(f'Программа завершила задачу:>')
            print("Программа завершено!")
            break
    elif user_answer == '>':
        low = mid
        mid = (low + high) // 2
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Предположение программы: '{mid}' >= Число\n")
    elif user_answer == '<':
        high = mid
        mid = (low + high) // 2
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Предположение программы: '{mid}' <= Число\n")

    else:
        print('Попробуйте еще раз:>')