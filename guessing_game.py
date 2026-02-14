import random

def guessing_game():
    # the random no generated from 1 to 10
    answer = random.randint(1,10)
    count = 0
    while answer:
        gues = int(input('Guess a number from 1 to 10: '))
        if gues < 1 or gues > 10:
            print('Please enter a number between 1 and 10')
            continue
        if gues > answer:
            print ('Too high! Guess again')
        if gues < answer:
            print ('Too low! Guess again')
        if gues == answer:
            print ('Correct!')
            break
        
        count += 1

#call function to call the game
guessing_game()
