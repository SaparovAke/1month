
# numbers.remove() - .remove(удаляет полностью)

# Структуры данных: списки, срезы, кортежи.
# list - список
# tuple - кортеж

# objects = (2, True, 'python', 4.6)
# objects += (56, '57', 34)
# objects = list(objects)
# objects.append(345)

# objects = tuple(objects)

# print(objects)
#
# print(type(objects))


# words = list(enumerate(words))

# print(numbers)
# numbers = list(range(1, 6))
# numbers = [i*i for i in range(1, 6) if i < 4]
# print(numbers)

# words = [55, 23.8, True, False, 2, 34, 12, 5]
# words = ['python', 'geektech', 'bishkek']
# new_copy = words.copy()

# new_copy[0] = 33

# print(id(words), id(new_copy))
# print(new_copy is words)
# print(new_copy == words)
#
# print(f'{words=}')
# print(f'{new_copy=}')





# # words.sort(key=len)
# # words.sort()
# words.reverse()
#
# new = words[::-1]
# print(new)

"""добавление"""
# words.append(100)
# words.insert(0, 'geektech')
# words.extend('oop')
# words += 'oop'

"""удаление"""
# words.remove(55)
# a = words.pop(2)
# del words[1:]
# print(a)

"""изменение"""
# words[1] = False
# words[0], words[3] = words[3], words[0]
# words.insert(2, words.pop(0))


# print(words)


# print(type(words))
