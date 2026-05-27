#Boris
#Make a code that recommends drinks based on user input
def coffeerecs():
    print("Welcome to Python Cafe! What can we get started for you today?")
    temperature=input("What can we do for you? Hot or Cold?")
    if temperature=="hot":
        sweetness=input("Now, would that be sweet or bitter?")
        if temperature=="hot" and sweetness=="sweet":
            print("Then I'll gladly recommend the hot chocolate for you today!")
        elif temperature=="hot" and sweetness=="bitter":
            print("Then I'll gladly recommend the cold brew for you today!")


    elif temperature=="cold":
        sweetness=input("Now would that be sweet or bitter?")
        if temperature=="cold" and sweetness=="sweet":
            print("Then I'll gladly recommend the iced latte for you today!")
        elif temperature=="cold" and sweetness=="bitter":
            print("Then I'll gladly recommend the cold brew for you today!")
coffeerecs()
