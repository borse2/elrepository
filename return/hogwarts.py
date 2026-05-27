import random
import time
def main():
  print("Welcome to Hogwarts")
  name=input("What is your name, wizard? ").capitalize()
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("....")
  time.sleep(1)
  print(".....")
  print(house(name))

def house(name):
  x=random.randint(1,4)
  if name=="Harry" or name=="Ron" or name=="Hermione" or x==1:
    return "Welcome to House Gryffindor"
  elif name=="Newt" or name=="Nymphphadora" or name=="Pomona" or x==2:
    return "Welcome to House Hufflepuff"
  elif name=="Luna" or name=="Cho" or name=="Filius" or x==3:
    return "Welcome to House Ravenclaw"
  elif name=="Voldemort" or name=="Draco" or name=="Severus" or x==4:
    return "Welcome to House Syltherin"


main()

while True:
  redo=input("Would you like to be reassessed? Yes or No? ").capitalize()
  if redo=="Yes":
    main()
  elif redo=="No":
    print("Settle in your new home!")
    break
  else:
    print("You've entered something incorrect")

