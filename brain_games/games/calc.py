from random import randint, choice


Rule = 'What is the result of the expression?'


def game():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    operation = choice('+-*')
    number = f'{number_1} {operation} {number_2}'
    if operation == '+':
        correct_answer = str(number_1 + number_2)
    elif operation == '-':
        correct_answer = str(number_1 - number_2)
    elif operation == '*':
        correct_answer = str(number_1 * number_2)
    return number, correct_answer
