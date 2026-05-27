#Create a program that runs 99 bottles until there are no more bottles
#Boris
bottles=100
while bottles>1:
    print(str(bottles)+ " bottles of milk on the wall")
    print(str(bottles)+ " bottles of milk on the wall")
    bottles=bottles-1
    print(str(bottles)+" bottles of milk on the wall")
    if bottles==1:
        print("One bottle of milk on the wall. One bottle of milk on the wall. Take it done pass it around")
        bottles=bottles-1
    if bottles==0:
        print("No more bottles of milk on the wall. Boo Hoo!")
        break
