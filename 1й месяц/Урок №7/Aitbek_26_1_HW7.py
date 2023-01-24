#
# def rest_number(lst, tup=0):
#     return tup, sorted(lst, key=lambda num: abs(tup - num))
#
#
# print(tuple(rest_number([78, 26, 34, 15, 47, 86, 24, 75], 80)))


# def output_by_index(senteces):
#     while True:
#         try:
#             indx = input('Введите индекс: ')
#             if indx == 'exit':
#                 print('Программа завершена')
#                 break
#             print(senteces[int(indx)])
#         except:
#                 print(f'Вводите только числа от 0 до {len(senteces) -1}')
#
# print(output_by_index(['hi', 'happy', 'nothing', True, 45, False,[],()]))

lst = [1, 5, 2.76, 20.22, 6, 4]
new1 = list(map(lambda x: x * 3, lst))
new2 = tuple(filter(lambda x: type(x) == int, lst))
print(new1)
print(new2)
