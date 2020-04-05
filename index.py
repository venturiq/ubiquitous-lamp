import random
import ssp
rps = ['Rock', 'Paper', 'Scissors']
again = True
player1 = random.choice(rps)
player2 = random.choice(rps)

while(again == True):
    i = input("Do you want to play again? y/n: ")
    if(i == 'y'):
        ssp.winner(player1, player2)
    if(i == 'n'):
        again = False
        break
