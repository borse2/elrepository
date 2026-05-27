def main():
    print("Welcome to your brand new calculator that can only preform addition, subtraction, division, or multiplication.")
    x=int(input("Please give me a number "))
    y=int(input("Please give me another number "))
    operator=input("Which operator would you like to use today? Addition/Multiplication/Subtraction/Division ")
    if operator=="Addition":
        print(calc_sum(x,y))
    elif operator=="Subtraction":
        print(calc_sub(x,y))
    elif operator=="Multiplication":
        print(calc_mult(x,y))
    elif operator=="Division":
        print(calc_div(x,y))

def calc_sum(x,y):
    addition=x+y
    return addition
def calc_sub(x,y):
    subtraction=x-y
    return subtraction
def calc_div(x,y):
    division=x/y
    return division
def calc_mult(x,y):
    multiplication=x*y
    return multiplication

main()
