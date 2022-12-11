import random
from nltk.corpus import words
#from words import words
import string

def get_valid_word(words):
    words = words.words()
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = len(word) + 1

    while word_letters and lives:
        # letters used
        print("You've used these letters: {}".format(' '.join(used_letters)))
        print("Lives remaining {}".format(lives))

        # what current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: {}".format(' '.join(word_list)))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You've already used that letter!!!")
        else:
            print("Invalid character. Please try again")
        print()
    if not lives:
        print("You lost!!. Word was {}".format(word))
    else:
        print("You've guessed the word correctly {}".format(word))

hangman()
# print(words)