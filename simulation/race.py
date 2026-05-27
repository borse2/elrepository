#initialize
import random
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
is_hare_asleep = False #Hare starts Awake
tortoise_wins = 0
hare_wins = 0
# The Simulation Loop
while tortoise_pos < finish_line and hare_pos < finish_line:
    # Tortoise always moves a short distance between 1 - 3 meters at random
    tortoise_pos=tortoise_pos+random.randint(1,3)
    # Hare has a 30% chance of falling a sleep for a turn
    y=random.randint(0,100)
    if y<=30:
        is_hare_asleep==True
    else:
        is_hare_asleep==False


    # If Hare is awake, it will move 1 - 10 meters at random
    if is_hare_asleep==False:
        hare_pos=hare_pos+random.randint(1,10)

    # Print the positions of the Hare and Tortoise after each round
    print(f" 🐇: {hare_pos} meters | 🐢: {tortoise_pos} meters")
# Determine the winner
if tortoise_pos >= finish_line:
    print("🐢 The Tortoise wins! Tortoise Wins: {tortoise_wins}")
    tortoise_wins=tortoise_wins+1
else:
    print("🐇 The Hare wins! Hare Wins: {hare_wins")
    hare_wins=hare_wins+1
