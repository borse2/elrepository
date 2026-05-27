#Boris
#Movie Theater
#functions
def theater():
    age=input("How old are you?")
    print (age)
    if int(age) >=18:
        print("You watch any movie you'd like!")
    elif int(age) <13:
        print("Sorry! You can only watch movies rated PG or lower")
    else:
        print("You can't watch rated-R yet, BUT you can watch PG-13 or lower!")
#Main
theater()
