from random import randint


Rule = 'Find the greatest common divisor of given numbers.'


def game():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    number = f'{number_1} {number_2}'
# т.к. number_1 сначла становится большим, а после деление становится остатком
# значит проверяем его на равенство 0
    while number_1 != 0:
        number_1, number_2 = max(number_1, number_2), min(number_1, number_2)
        number_1 = number_1 % number_2
    correct_answer = number_2
    return number, str(correct_answer)
