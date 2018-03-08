# pythonParade
The main aim of this repository is to store the content material to be covered in the advanced Python3 workshop conducted by IEEE NTU student branch


The contents which will be covered in this Advanced Python workshop are :
1. Blazing fast recap of the previously done concepts
2. Functions - Declaration and Implementation
3. Recursive functions - Very short introduction and a few examples. Difference between recursion and iteration
4. Data Structures - Declaration and Implementation of the various types of Data Structures like Lists, tuples, dictionary. Elucidation on the primary differences
between them and also a few in built library functions for the manipulation of these structures.
5. Usage of pip - Quick intro into syntax of pip for further installation of frameworks
6. {If time permits} - Basics of Algorithm - Example algorithm of BubbleSort

All the code snippets can be found on my GitHub repository. The link is github.com/abhishekbhagwat/pythonParade 



Functions:
Functions are snippets of code written outside the main function. This is written to reduce the repetition of code. A function can be called multiple times within the
program. The typical Declaration of a function is done in the following manner

```python
def func_name(func_args):
    func_body ```

''' The code is pretty much self explanatory. It uses a keyword def to define the function. The name of the function is func_name and the arguments taken by the function
are func_args '''

eg 1.1

def sayHello():                     #the function sayHello does not require any arguments
    print"Hello World!"

''' Parameters are certain values supplied to the functions so that they can use these values to perform certain actions or operations. These are supplied in the 
parenthesis in the function declaration after the function name'''

eg 1.2

def numCompare(a,b):
    if a>b:
        return 1
    else:
        return 0


''' Scope of a variable - There are essentialy 2 kinds of scope - Local and Global. Local scope means that if a value of a particular variable is modified inside 
the block of a function or such constructs, the global value set does not change. As soon as the control escapes that particular block of execution, the 
value is restored back to the original one '''

eg 1.3

x = 50

def func(x):
    x = 1
    print"x is "+ x

func(x)
print x 

'''Return statement : This particular statement is used to return a certain value from the function. Usually only a single value can be returned. After the return
statement the control comes out of the particular function and the flow of control moves on.'''

eg 1.4

def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return "x equals y"
    else:
        return y

''' Pass : Pass statement is used to indicate an empty block of statements'''

def passExmp():
    pass

'''Using the pass keyword essentially passes over the control to the next line of code'''

DATA Structures

'''Data structures are certain programming constructs which are used to store data in a certain manner. Different programming languages make use of different 
data structures, but Python uses 3 main types of Data structures - LISTS, TUPLES, DICTIONARY'''

''' 1. LISTS - List is a linear data stucture where large amount of data is stored in consecutive memory locations. Initialization of a list is very easy'''

eg 2.1
listName = ['Data 1','Data 2'....'Data n']

'''To access each element of a list to perform certain operation is called as Traversal. Each element of a list has an index which essentially denotes the 
position of that unique element. Index numbering starts from 0. This implies that the very first element of a list has an index of 0. Each element can be accessed
consecutively by using a for loop and the index number as a counter variable.'''

eg 2.2 
fruits = ['Apple','Banana','Orange']

fruits[0] = 'Apple'
fruits[1] = 'Banana'
fruits[2] = 'Orange'

#to access all elements of the list use a for loop in the following way

for fruit in fruits:        #uses a var fruit to check the presence of an element in list   
    print fruit             #prints the element stored in the var fruit

'''another way to do this is to count the number of elements in the list and use a counter variable to iterate over the list. As soon as the counter variable 
crosses the number of elements present in the list, the loop must break'''



