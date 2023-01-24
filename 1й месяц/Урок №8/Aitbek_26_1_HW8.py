
mini = 0
maxi = 100
mid = (mini + maxi) // 2
i = 0

with open("results.txt", "w", encoding="UTF-8") as file:
        file.write('Программа угадай число\n')

while True:
        print(f"Ваше число это {mid}?")
        user = input('Да, больше ">" или меньше "<"').lower()
        i += 1
        if user == 'да':
                with open('results.txt', 'a', encoding='UTF-8') as file:
                        file.write(f'Количество попыток {i}\n')
                        file.write(f'Ваше число {mid}\n')
                        print('Программа завершено')
                break
        elif user == '<':
                maxi = mid
                mid = (mini + maxi) // 2
                with open('results.txt', 'a', encoding='UTF-8') as file:
                        file.write(f'Предпологаемое число: {mid}\n')
        elif user == '>':
                mini = mid
                mid = (mini + maxi) // 2
                with open('results.txt', 'a', encoding='UTF-8') as file:
                        file.write(f'Предпологаемое число: {mid}\n')
        else:
                print('Вы не правильно ввели, попробуйте снова')



