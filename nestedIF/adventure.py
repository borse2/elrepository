#Boris
#Create an adventure for a game character
print("Welcome to Evangelion Abridged! Play if you dare! >:)")
fork=input("There's a fork in the road?! Do you want to go left or right?")
if fork=="left":
    father=input("You just reunited with your father, but you realized he abadonded you for 6 or 7 years. Do you embrace him or give him the cold shoulder?")
    if father=="embrace him" and fork=="left":
        print("You earned a cool mech suit AND are oblivous to your fathers evil ways")
    elif father=="cold shoulder" and fork=="left":
        print("He disowns you and he continues on his evil journey, unbeknowst to you")
elif fork=="right":
    classmate=input("You meet a classmate who invites you to join them on a secret adventure. Do you accept or decline?")
    if classmate=="accept" and fork=="right":
        print("You are now tasked with saving humanity from your oblivious father")
    elif classmate=="decline" and fork=="right":
        print("Your classmate calls you a loser and you die because of the 3rd impact")
