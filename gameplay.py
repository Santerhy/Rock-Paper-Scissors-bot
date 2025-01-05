import random
from enum import Enum

class Hands(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def RandomHand():
        r = random.randrange(0,3)
        if r == 0:
            return Hands.ROCK
        elif r == 1:
            return Hands.PAPER
        else:
            return Hands.SCISSORS

    def IntToEnum(i):
        if i == 1:
            return Hands.ROCK
        elif i == 2:
            return Hands.PAPER
        else:
            return Hands.SCISSORS


def CheckWinner(playerChoice, botChoice):
    if playerChoice == botChoice:
        return 0
    
    if (botChoice + 1) % 3 == playerChoice % 3:
        return 1

    return -1