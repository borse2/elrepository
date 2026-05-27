balance=200
money=input("Welcome to the ATM. What would you like to do? Check/Withdraw/Deposit ")
def check():
    global money
    global balance
    if money=="Check":
        print("You have " + str(balance) + " dollars")
def withdraw():
    global money
    global balance
    if money=="Withdraw":
        subtract=input("How much would you like to withdraw? ")
        if int(subtract)>balance:
            print("Insufficient funds")
        else:
            print("You have withdrawn  " + str(int(subtract)) + " dollars")
            balance=balance-int(subtract)
            print("You now have " + str(balance) + " dollars")
def deposit():
    global money
    global balance
    if money=="Deposit":
        addition=input("How much would you like to deposit? ")
        balance=balance+addition
        print("You have depositied__________ dollars")

check()
withdraw()
deposit()

