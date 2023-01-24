# .range это для выведение от 0 до скольки то например(0, до 1000, 2) 2 индекс это есть шаг


# with open("results.txt", "a", encoding="UTF-8") as file:
#     low = 0
#     high = 100
#     mid = (low + high) // 2
#     i = 0
#     while True:
#         print(f"Ваше число это {mid}?")
#         user_answer = input("Да, > или < : ").lower()
#         if user_answer == "да":
#             i =+ 1
#             break
#         file.write(f"Попытки {i}")
#         file.write(f"Ваше число{mid}")



#
# signal = input('введите цвет светафора:')
#
# if signal == 'red' or signal == 'yellow':
#     print('stop')
# elif signal == 'green':
#     print('go')
# else:
#     print('осмотрись!!!')
#     situation = input('опишите ситуацию')
#     if situation == 'off':
#         print('смотри налево')
#     elif situation == 'police':
#         print('жди знака гаишника')

# time = int(input('введите время: '))
#
# if time >= 6 and time <= 11:
#     print('good morning')
#
# elif time >= 12 and time <= 17:
#     print('good aftenoon')
#
# elif time >= 18 and time <= 24:
#     print('good evening')
#
# elif time >= 00 and time <= 5:
#     print('good night')
#
# else:
#     print('не правильно ввели время !!!')
#
# password = input('введите пароль: ')
#
# if len(password) >= 8 and not password.isalpha() and not password.isnumeric():
#     print('ваш пароль подойдёт')
# else:
#     print('no')


# for and while читаем так (когда)

# Не равно (!=)
# Проверяет, не равно ли значение слева правому. Оператор <> выполняет ту же задачу,
# но его убрали в Python 3. Когда условие выполнено, возвращается True . В противном случае — False .

# .append добавляет в список
# .isdigit() возвращает True, если все символы является цифрами. Если нет то возвращается False


# bishkek = float((input('Напишите температуру Бишкека: ')))
# osh = float((input('Напишите температуру Оша: ')))
# naryn = float((input('Напишите температуру Нарын: ')))
# batken = float((input('Напишите температуру Баткен: ')))
# ik = float((input('Напишите температуру ИК: ')))
# talas = float((input('Напишите температуру Талас: ')))
# jalal_abad = float((input('Напишите температуру Жалал-Абада: ')))
#
# sum_ob = bishkek + batken + naryn + ik + osh + talas + jalal_abad
#
# print(f"Средний показатель температуры воздуха по КР на сегодня {round(sum_ob // 7, 1)} °C.")
#
# soglas = "qwrtpsdfghjklzxcvbnmйцкнгшщзхъфвпрлджчсмтьб"
# glas = "eyuioaуеаоэяи"
#
# while True:
#     sogl = 0
#     gl = 0
#     word = input("Напишите слово: ")
#     k = len(word)
#     if word == "exit" or word == "выход":
#         print("Программа вышла")
#         break
#     for i in word:
#         if i in soglas:
#             sogl += 1
#         elif i in glas:
#             gl += 1
#     print(f"Слово: {word}\n"
#           f"Количество букв: {k}\n"
#           f"Количество согласных букв: {sogl}\n"
#           f"Количество гласных букв: {gl}\n"
#           f"Гласные и согласные в процентах: {round(gl / k * 100, 2)} % / {round(sogl / k * 100, 2)} %")
#
#

















