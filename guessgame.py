import random

def numguess(): 
    guess = int(0)
    num = int(random.uniform(1,10))

    while guess != num:
        guess = int(input("put your guess here "))
        guess_history = []
        guess_history.append(guess)
        if guess > num:
            print("your guess is too big")
        if guess < num:
            print("your guess is too small")
        if guess == num:
            print("your right")
    for i in range(1, len(guess_history)):
        print(guess_history)
numguess()