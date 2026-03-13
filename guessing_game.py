import random

def guessing_game():
    # the random no generated from 1 to 10
    answer = random.randint(1, 10)
    count = 0

    while answer < 10:
        guess = int(input('Guess a number from 1 to 10: '))

        if guess < 1 or guess > 10:
            print('Please enter a number between 1 and 10')
            continue

        if guess == answer:
            print('Correct!')
            break
        elif guess > answer:
            print ('Too high! Guess again')
        else:
            print ('Too low! Guess again')
        
        count += 1

# call function to call the game
guessing_game()
