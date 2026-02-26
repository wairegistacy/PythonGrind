import random
def gues_even_no():
    even_answer = random.randrange(2, 11, 2)
    count = 0
    while True:
        gues = int(input('Guess an even number between 1 and 10: '))
        if gues%2 != 0:
            print('Not an even number')
            continue
        if gues < even_answer:
            print('Too low! Guess again')
        if gues > even_answer:
            print('Too high! Guess again')
        if gues == even_answer:
            print('Correct answer')
            break

        count += 1

gues_even_no()
