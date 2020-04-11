"""Modelling a classic Hangman game in English (without hanging though...)."""

import string
import random

ALPHABET_LIST = list(string.ascii_lowercase)
WORDS_TO_GUESS = ["fox",
                  "bear",
                  "koala",
                  "hedgehog",
                  "chimpanzee",
                  "chinchilla"]
RANDOM_WORD = random.choice(WORDS_TO_GUESS)
LETTERS_IN_WORD, LETTERS_NOT_IN_WORD = [], []
BASE = ['_' for letter in list(RANDOM_WORD)]


def guess_the_word():
    """Perform some action based on user input."""

    print(f"\nHere's the word I need you to guess: "
          f"{len(RANDOM_WORD) * ' _'}\n")

    while sorted(LETTERS_IN_WORD) != sorted(RANDOM_WORD):
        user_input = input("\nPlease give a single letter: ").lower()
        if (user_input in ALPHABET_LIST) and (len(user_input) == 1):
            if user_input in RANDOM_WORD:
                find_all_indices = [index for index, value
                                    in enumerate(RANDOM_WORD)
                                    if value == user_input]
                for num in find_all_indices:
                    BASE[num] = user_input
                    LETTERS_IN_WORD.append(user_input)
            else:
                LETTERS_NOT_IN_WORD.append(user_input)
                print(f"Sorry - please try again!"
                      " Here's the list of letters you've"
                      " tried which do not exist in the word:"
                      f"\n{LETTERS_NOT_IN_WORD}")
            print("".join(BASE).capitalize())
        else:
            print(f"'{user_input}' is not a valid value...")
            continue

    print(f"\nYou guessed it! -> "
          f"{RANDOM_WORD.upper()}\nThanks for playing! Stay home & safe! =)")


guess_the_word()
