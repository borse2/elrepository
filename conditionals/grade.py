#Boris
#Grade
#collects a test score as a number from the user and prints the corresponding letter grade

#Make sure to collect an integer from the user and NOT a string
def reportcard():
    score = int (input("What is your currentgrade in APCSI"))
    if score >=90:
        print("Congrats! You have an A! Keep it up!")
    elif score >=80:
        print("A B is still good! You'll get an A in no time!")
    elif score >=70:
        print("You've got a C.. but at least your passing!")
    elif score >=60:
        print("A D...")
    elif score >=50:
        print ("An F?! UNACCEPTABLE")
reportcard()
