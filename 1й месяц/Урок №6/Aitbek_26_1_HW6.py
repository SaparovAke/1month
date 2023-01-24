

def number(n):
    if type(n) == int:
        if n % 2 == 0:
            return True
        else:
            return False
    else:
        return None
print(number("fsad"))


def litercy(sentences):

    if sentences[0].istitle and sentences[-1] == ".":
        return sentences
    else:
        return "Предложение не правильно написанно." \
               "\nНапишите с заглавной буквы и в окончании с точкой '.'"

print(litercy("Салам с Бишкека."))



def average(*args):
    return int(sum(args) // len(args))

print(average(4, 6, 20))


def rest_number(lst, number = 0):
    a = [abs(i - number) for i in lst]
    b = a.index(min(a))
    return f'{lst}, {number} == {lst[b]}'

print(rest_number([1.2, 5, 25, 65, 100], 45))