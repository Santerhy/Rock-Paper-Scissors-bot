import gameplay

#Contains player moves from 3 consecutive games
class Combos:
    def __init__(self, h1, h2, h3):
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.occurance = 1
    
    def CheckForOccurance(self,_h1, _h2, _h3):
        if self.h1 == _h1 and self.h2 == _h2 and self.h3 == _h3:
            self.occurance += 1
            return True
        return False

def GetMove():
    if len(gameplay.games) < 3:
        return gameplay.Hands.RandomHand()
    return EvaluateHands()
    #return gameplay.Hands.RandomHand()

def EvaluateHands():
    possibleCombos = []

    for i in range(2, len(gameplay.games)):

        h1, h2, h3 = gameplay.games[i][1], gameplay.games[i-1][1], gameplay.games[i-2][1]
        if len(possibleCombos) == 0:
            possibleCombos.append(Combos(h1, h2, h3))
        else:
            CheckOccurances(possibleCombos, h1, h2, h3)

    SortCombos(possibleCombos)
    print("==============================")
    #print("PossibleCombos: " + len(possibleCombos))
    for x in range(len(possibleCombos)):
        print(f"\n h1: {possibleCombos[x].h1}, h2: {possibleCombos[x].h2}, h3: {possibleCombos[x].h3}, occurance: {possibleCombos[x].occurance}")
    print("==============================")
    possibleCombos.clear
    return gameplay.Hands.GetWinnerHand(possibleCombos[-1].h1)

def CheckOccurances(arr, h1, h2, h3):
    for j in range(len(arr)):
        if arr[j].CheckForOccurance(h1, h2, h3):
            return
    arr.append(Combos(h1, h2, h3))

def SortCombos(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j].occurance > arr[j+1].occurance:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break