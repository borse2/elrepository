#Boris
#Write a function with 3 integer parameters (a,b,c) that prints the largest of the 3 numbers

#functions
def largest(a,b,c): #abc are the parameters that will cointain integers
#solution goes here
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print (b)
    elif c > a and c > b:
        print (c)

#main
largest(5,3,4)
largest (9,10,5)
largest (1,2,3)
