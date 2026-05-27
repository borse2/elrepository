
finished=[]
productivity=["Sweep living room", "Reorganize Desk", "Declutter Living Room", "Study for Gov"]
x=len(finished)
y=len(productivity)
#------------------------------------------------------------------------
while True:
    menu=input("""Lets get productive! What do you want to do to your to-do list?
Add, Remove, Mark, Clear, Exit? """).strip()
#---------------------------------------------------------------------------
    if menu=="Add" or menu.lower()=="add":
        print(productivity)
        add=input("What needs to be added? ").strip()
        if add=="":
            print("Wrong answer, forehead!")
        else:
            productivity.append(add)
            print(f"You have {y} tasks to do")
            print(productivity)

#------------------------------------------------------------------------
    elif menu=="Remove" or menu.lower()=="remove":
        print(productivity)
        remove=input("What needs to be removed? ").strip()
        try:
            productivity.remove(remove)
            finished.append(remove)
            print(f"You have completed {x} tasks")
            print(finished)
        except:
            print("Wrong answer forehead! Try again")
            continue
    #------------------------------------------------------------------------
    elif menu=="Clear" or menu.lower()=="clear":
        productivity.clear()
        print(productivity)
        print("Were you procrastinating again or were you actually productive?")
    #------------------------------------------------------------------------
    elif menu=="Mark" or menu.lower()=="mark":
        print(productivity)
        mark=input("What needs to be marked as done? ").strip()
        try:
            productivity.remove(mark)
            finished.append(mark)
            print(finished)
        except:
            print("Invalid input. Try again, pal")
            continue
        #------------------------------------------------------------------------
    elif menu not in ["Add", "Remove", "Mark", "Clear", "Exit", "add", "remove", "mark", "clear", "exit"]:
        print("Invalid input. Try again buddy")
        continue
    else:
        break

