import random


def play():
    user = input(
        "What's your choice? (r) for rock, (p) for paper or (s) for scissors: "
    )
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tire"

    # r>s, s>p, p>r
    if isWin(user, computer):
        return f"You won! {user} beats {computer}"
    return f"You lost {computer} beats {user}"


def isWin(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())