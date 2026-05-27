#Boris
#Create a code that prints even numbers up to a number from any given number
def even_numbers():
    number=int(input("Give any number: "))
    for number in range (0, number+1, 2):
        print(number)
even_numbers()
