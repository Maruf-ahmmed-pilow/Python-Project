import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess>random_number:
            print(f'Sorry, {guess} is too high from the random number.')
        elif guess<random_number:
            print(f'Sorry, {guess} is too low from the rangom number.')
            
    print(f'Yay, congrats you have guessed the number, {random_number} correctly!')
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess =  random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
            
        feedback = input(f'is {guess} too high (H) too low (L) or correct(C)??').lower()
        
        if feedback == 'h':
            high = guess-1
            
        if feedback == 'l':
            low = guess +1
            
    print('yay ! the computer guessed your number, {guess}, correctly!')

guess(10)