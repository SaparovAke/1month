
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#
#   while True:
#     word = input('\nвведите слово: ').lower()
#     if word == 'exit':
#         print('exit...')
#         break
#     for i in word:
#         if i in rus:
#             print(eng[rus.index(i)], end='')
#         else:
#             print(rus[eng.index(i)], end='')



# циклы: for, while
# i - iterable, item

# ,birtr
# пуулеуср


# rounds = 5
#
# while rounds > 0:
#     print(rounds)
#     rounds -= 1

# c = 0
# while c < 5:
#     if c == 3:
#         break
#     print('hello', c)
#     c += 1

# cash = 100
# percents = 0.12
# years = 5
#
# for i in range(years):
#     cash += cash * percents
#     print(round(cash, 2))


# for i in range(5):
#     time = int(input('введите время: '))
#     if 6 <= time <= 11:
#         print('good morning')
#     elif time >= 12 and time <= 17:
#         print('good afternoon')
#     elif time >= 18 and time <= 24:
#         print('good evening')
#     else:
#         print('hello')



# for i in range(1, 5):
#     for k in range(1, 4):
#         print(i, k)


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end='-')

# word = 'python'
#
# for letter in word:
#     if letter == 'q':
#         break
#         # continue
#     print(letter)
# else:
#     print('завершили!')
