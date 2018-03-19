# This code illustrates the passing of parameters to functions and how it is used

# now we compare the two numbers. To do so we will pass the values of a and b to the function numCompare


def numCompare(a,b):
    if a>b:
        return 1
    else:
        return 0

a = int(input("Enter the 1st value\n"))
b = int(input("Enter the 2nd value\n"))


print ("The result of the comparison is "+ str(numCompare(a,b)))         #Function ca
