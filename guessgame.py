import random

def numguess(): 
    guess = int(0)
    num = int(random.uniform(1,10))
    guess_history = []
    while guess != num:
        guess = int(input("put your guess here "))
        if guess > num:
            guess_history.append(guess)
            print("your guess is too big")
        if guess < num:
            print("your guess is too small")
            guess_history.append(guess)
        if guess == num:
            print("your right")
    print("incorrect guesses:")
    for i in guess_history: 
        print(i)  
numguess()