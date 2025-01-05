import random
from enum import Enum

games = []

class Hands(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def RandomHand():
        r = random.randrange(0,3)
        print("Choosing random hand")
        if r == 0:
            return Hands.ROCK
        elif r == 1:
            return Hands.PAPER
        else:
            return Hands.SCISSORS

    def GetWinnerHand(hand):
        if hand == Hands.ROCK:
            return Hands.PAPER
        if hand == Hands.PAPER:
            return Hands.SCISSORS
        return Hands.ROCK

    def IntToEnum(i):
        if i == 1:
            return Hands.ROCK
        elif i == 2:
            return Hands.PAPER
        else:
            return Hands.SCISSORS


def CheckWinner(playerChoice, botChoice):
    winner = -1
    if playerChoice.value == botChoice.value:
        winner = 0
    
    if (botChoice.value + 1) % 3 == playerChoice.value % 3:
        winner = 1

    games.append([winner, playerChoice, botChoice])
    #print(games)

    return winner