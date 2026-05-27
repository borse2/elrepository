import random
secret_number=random.randint(1,100)
attempt=0
high=100
low=1
def linear_search():
    global attempt
    global secret_number
    for guess in range(1,101):
        if guess==secret_number:
            print(f"Your number is: {guess}")
            break
        else:
            attempt=attempt+1
    print(f"It took me {attempt} guesses to find the secret number")



def binary_search():
    global high
    global low
    global secret_number
    global attempt
    found=False
    while found==False:
        mid=(low+high)//2
        if secret_number==mid:
            print(f"Your number is: {secret_number}")
            found==True
            print(f"It took me {attempt} guesses to find the secret number")
            break
        elif mid<secret_number:
            low=mid+1
            attempt=attempt+1
        elif mid>secret_number:
            high=mid-1
            attempt=attempt+1


binary_search()
