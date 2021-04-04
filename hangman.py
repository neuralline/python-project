import random
from words import words
import string


def gerValidWord(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = gerValidWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()  #  What the user has guessed

    lives = 6

    # getting user input
    while len(wordLetters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd]) ==> 'a b cd
        print(
            "You have",
            lives,
            "lives left and used these letters: ",
            "".join(usedLetters),
        )

        # what current word is (ie W - R D)
        word_list = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                print("")
            else:
                lives = lives - 1
                print("Letter is not in word.")

        elif userLetter in usedLetters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # gets here when len(wordLetters) == 0 OR when lives == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("YAY! You guessed the word", " ".join(word), "!!")


hangman()
