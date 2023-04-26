from random import randint, choice


Rule = 'What number is missing in the progression?'
def game():
    progression = []
    number = ''
    len_progression = randint(5, 10)
    for i in range(randint(1, 60), 100, randint(1, 10)):
        progression.append(i)
        if len(progression) == len_progression:
            break
    missing_number = choice(progression)
    for i in progression:
        if i == missing_number:
            correct_answer = i
            i = '..'
        number += f' {i}'
        number = number.strip()
    return number, str(correct_answer)