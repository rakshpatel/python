import random
from re import X

from requests_toolbelt import GuessAuth

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and {}: ".format(x)))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print("Congratulations!!!. You have guessed the number {} correctly!!".format(random_number))

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input("Is {} to high (H), too low (L), or correct (C)?? ".format(guess)).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Congratulations!!!. You guesssed the number {} correctly!!".format(guess)) 

print("You are playing a game")
guess(10)
print("Computer is playing a game")
computer_guess(10)