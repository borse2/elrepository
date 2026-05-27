#Pairty
#PRogram prompts the user for a number and prints whether that number is even or odd
#Initializing
#Functions
def main():
    number=int(input("State ANY number"))
    #Evaluate whether number if even or odd
    if is_even(number):
        print("Even")
    else:
        print("Odd")
#Function should return true if x is even, false if odd
#x is an integer
def is_even(x):
    if x % 2==0:
        return True
    elif x % 2==1:
        return False

main()

