# this code illustrates the difference between global and local variables and shows how to resolve its scope

x = 50                              #Global variable x = 50

def func(x):
    x = 1                           #Local variable x = 1; Compiler doesn't recognise the global value of x = 50
    print ("x is "+ str(x)+" in the function")                #prints value of x = 1

    #control exits from the function. Value of x is restored to 50

func(x)

print ("x is "+str(x)+" outside the function func()")                             #prints value of x = 50
