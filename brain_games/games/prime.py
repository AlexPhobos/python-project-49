from random import randint


Rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def game():
    number = randint(1, 100)
    if number == 1:
        correct_answer = 'no'
        return number, correct_answer
    for i in range(2, ((number // 2) + 1)):
        if number % i == 0:
            correct_answer = 'no'
            break
    else:
        correct_answer = 'yes'
    return number, correct_answer