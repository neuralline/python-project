import random


def guessUser(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < randomNumber:
            print("Sorry, guess again. Too low")
        elif guess > randomNumber:
            print("Sorry, guess again. Too high")

    print(f"Yay, congrats. you have guessed the number {randomNumber}")


def guessComputer(x):
    low = 0
    high = x
    feedback = ""
    print(f"I'm gonna guess the number you have in mind from 1 to {x}")
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} correct (c), too low (l) or too high (h)? "
        ).lower()
        if feedback == "l":
            low = guess - 1
        elif feedback == "h":
            high = guess + 1

    print("great playing with you")


guessComputer(10)