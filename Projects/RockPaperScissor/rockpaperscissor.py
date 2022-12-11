from ast import Return
import random
from commonmark import ReStructuredTextRenderer

from regex import P

def play():
    user = input("What's your choice? 'r' for rock,'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"


def is_win(player, opponent):
    # return True if player winds
    # r > s, s > p, p > r

    if (player == "r" and opponent == "s") \
        or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True


outcome = play()

print(outcome)