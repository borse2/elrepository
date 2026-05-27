#Boris Adokou
#Rock, Paper, Scissors Game
# A simple implementation of the Rock, Paper, Scissors game.

#initializing
import random
draw=0
win=0
loss=0
played=0
x=random.randint(1,3)
#main
def rps():
    global draw, win, loss, played, x
#----------------------------------------------------------------------------------
    while True:
        if x==1:
            computer="Rock"
        elif x==2:
            computer="Paper"
        else:
            computer="Scissors"
        player=input("Choose Rock, Paper, or Scissors: Rock, Paper, Scissors? ")
        if player not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue
#---------------------------------------------------------------------------------
        if player==computer:
            print("It's a tie!")
            print(f"Both chose {player}.")
            print("---------------------------------------------------------------------")
            draw=draw+1
        elif (player=="Rock" and computer=="Scissors") or (player=="Paper" and computer=="Rock") or (player=="Scissors" and computer=="Paper"):
            print("You win!")
            print(f"{player} beats {computer}.")
            print("---------------------------------------------------------------------")
            win=win+1
        else:
            print("Computer wins!")
            print(f"{computer} beats {player}.")
            print("---------------------------------------------------------------------")
            loss=loss+1
        played=played+1
        print(f"Games played: {played}, Wins: {win}, Losses: {loss}, Draws: {draw}")
#----------------------------------------------------------------------------------
        replay=input("Do you want to play again? (yes/no): ")
        if replay.lower()== "yes":
            continue
        else:
            print("Thanks for playing!")
            break
rps()
