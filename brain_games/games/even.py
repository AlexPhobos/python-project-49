from random import randint


Rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    number = randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
