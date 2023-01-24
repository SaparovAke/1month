
soglas = 'йцкнгшщзхъфвпрлджчсмтьбqwrtpsdfghjklzxcvbnm'
glas = 'уеыаоэяиюeyuioa'

while True:
    sogl = 0
    gl = 0
    word = input('\nвведите тескт: ').lower()
    k = len(word)
    if word == 'exit' or word == 'выход':
        print('Вы вышли')
        break
    for i in word:
        if i in soglas:
            sogl += 1
        elif i in glas:
            gl += 1
    print(f'Количество букв в слове: {k}\n Количество гласных букв: {gl}\n Количество согланых букв: {sogl}\n'
          f'Согласные {round(sogl / k * 100 ,2)}% \n'
          f'Гласные {round(gl / k * 100 , 2)}% \n')