import bot
import gameplay



while True:
    i = int(input("'1' = rock, '2' = paper, '3' = scissors. 0 = quit "))
    if i == 0:
        break

    playerHand = gameplay.Hands.IntToEnum(i)
    botHand = bot.GetMove()

    winner = gameplay.CheckWinner(playerHand, botHand)

    if winner == 0:
        print(f"You chose {playerHand.name}, bot chose {botHand.name}. Tie")
    elif winner == 1:
        print(f"You chose {playerHand.name}, bot chose {botHand.name}. You won!")
    elif winner == -1:
        print(f"You chose {playerHand.name}, bot chose {botHand.name}. Bot won")