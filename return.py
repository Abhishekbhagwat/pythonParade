'''this code illustrates how the return statement is used. An important point to note is that only one value can be returned by a
function'''

def maximum(x,y):
    if x>y:
        return (x)
    elif x==y:
        return ("x equals y")
    else:
        return (y)

x = int(input("Enter the 1st value\n"))
y = int(input("Enter the 2nd value\n"))

print ("The maximum value is "+str(maximum(x,y)))



'''Note how the function returns only the largest value. It cannot return multiple values. A very unique case of a string being
returned is shown in the above function. After the return statement has been executed the control flow comes out of the function
and returns to the main function'''
