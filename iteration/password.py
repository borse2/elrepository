#Boris
#Make a program that keeps asking for a password until the user types in the correct password
password="boberto"
while True:
    security=input("Please enter your password: ")
    if security==password:
        print("Access granted!")
        break
    else:
        reset=input("Incorrect password. Reset your password? Yes or No? ")
        if reset=="Yes" or reset.lower()=="yes":
            email=input("Enter your email address: ")
            print(f"The email has been sent to {email}")
            newpass=input("What would you like your new password to be? ")
            password=newpass
        else:
            print("Try again later")
