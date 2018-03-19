# pythonParade
## Advanced Python3 workshop conducted by IEEE NTU student branch


The **contents** which will be covered in this Advanced Python workshop are :
1. Blazing fast recap of the previously done concepts
2. Functions - Declaration and Implementation
3. Recursive functions - Very short introduction and a few examples. Difference between recursion and iteration
4. Data Structures - Declaration and Implementation of the various types of Data Structures like Lists, tuples, dictionary. Elucidation on the primary differences
between them and also a few in built library functions for the manipulation of these structures.
5. Usage of pip - Quick intro into syntax of pip for further installation of frameworks
6. Creating a script to automate login into NTULearn
All the code snippets can be found on my GitHub repository. The link is github.com/abhishekbhagwat/pythonParade 



## Functions
Functions are snippets of code written outside the main function. This is written to reduce the repetition of code. A function can be called multiple times within the
program. The typical Declaration of a function is done in the following manner

```python
def func_name(func_args):
    func_body
```

    
The code is pretty much self explanatory. It uses a keyword def to define the function. The name of the function is func_name and the arguments taken by the function
are func_args

```python
def sayHello():                     #the function sayHello does not require any arguments
    print ("Hello World!")
```
### Parameters
Parameters are certain values supplied to the functions so that they can use these values to perform certain actions or operations. These are supplied in the 
parenthesis in the function declaration after the function name

```python
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

```

### Scope of a variable
There are essentialy 2 kinds of scope - Local and Global. Local scope means that if a value of a particular variable is modified inside the block of a function or such constructs, the global value set does not change. As soon as the control escapes that particular block of execution, the value is restored back to the original one 

```python
x = 50
def func(x):
    x = 1
    print "x is "+ x
func(x)
print x 
```

### Return statement
This particular statement is used to return a certain value from the function. Usually only a single value can be returned. After the return statement the control comes out of the particular function and the flow of control moves on.

```python
# this code illustrates the difference between global and local variables and shows how to resolve its scope

x = 50                              #Global variable x = 50

def func(x):
    x = 1                           #Local variable x = 1; Compiler doesn't recognise the global value of x = 50
    print ("x is "+ str(x)+" in the function")                #prints value of x = 1

    #control exits from the function. Value of x is restored to 50

func(x)

print ("x is "+str(x)+" outside the function func()")                             #prints value of x = 50

```

### Pass
Pass statement is used to indicate an empty block of statements

```python
def passExmp():
    pass
```

Using the pass keyword essentially passes over the control to the next line of code

## Data Structures

Data structures are certain programming constructs which are used to store data in a certain manner. Different programming languages make use of different 
data structures, but Python uses 3 main types of Data structures - LISTS, TUPLES, DICTIONARY

Due to time constraints I will only be demonstrating about Lists, but the logic can be extended to tuples and dictionaries also.

### Lists
List is a linear data stucture where large amount of data is stored in consecutive memory locations. Initialization of a list is very easy.

```python
listName = ['Data 1','Data 2'....'Data n']
```

To access each element of a list to perform certain operation is called as **Traversal**. Each element of a list has an index which essentially denotes the 
position of that unique element. Index numbering starts from 0. This implies that the very first element of a list has an index of 0. Each element can be accessed consecutively by using a for loop and the index number as a counter variable.

```python
fruits = ['Apple','Banana','Orange']

fruits[0]   #'Apple'
fruits[1]   #'Banana'
fruits[2]   #'Orange'

#to access all elements of the list use a for loop in the following way

for fruit in fruits:        #uses a var fruit to check the presence of an element in list   
    print (fruit)             #prints the element stored in the var fruit

```

Another way to do this is to count the number of elements in the list and use a counter variable to iterate over the list. As soon as the counter variable crosses the number of elements present in the list, the loop must break.

## pip
pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the Python Package Index. Python 2.7.9 and later, and Python 3.4 and later include pip by default. All frameworks and dependencies required by Python can be installed using pip. 
As we are using Python3 we will be using pip3
```
pip3 install package_name
```
To run as administrator or provide privileges
```
sudo pip3 install package_name
```
## Automation of NTULearn Login
Now we will be writing a script to automate the process of signing in into NTULearn using Python and Selenium.

#### Requirements
1.Selenium <br>
2.Chromedriver https://chromedriver.storage.googleapis.com/index.html?path=2.36/<br>
3.Chrome Browser (As it is the most used browser!)<br>

The first step will be to install pip. Fire up a terminal window and type in 
```
pip3 install selenium
```
if required you can also use the sudo flag before pip3. Make sure you have completed this step before going to the next step.

Now click on the link next to Chromedriver to install the Chrome WebDriver package. This allows us to communicate with the browser.

After installing both fire up idle and save the file as automate.py and place it in the directory where Selenium has been installed. Open up automate.py and start editing.

#### Importing the required modules
Modules are certain pre-written files which contain certain code to perform the required function. From the module we import certain functions. Alternatively we could import the entire module itself. Now type in the following code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

#### Creating the credential strings

We now have to store our login credentials in the file. To do this we will make use of strings.

```python 
usernameStr = 'Username'       
passwordStr = 'Password'
```
Copy the above code and paste it into the same file. Replace the text in the ' ' with your username and password

#### Requesting to open Chrome browser

```python
browser = webdriver.Chrome()
browser.get(('https://ntulearn.ntu.edu.sg/webapps/login/'))
```
I have already added the link to NTULearn. This link can be modified into others also.

#### Inspection of elements of the webpage

Open the link for NTULearn login page and right click on the username field and click on inspect element. Observe the id for that particular field. Repeat the same procedure for the password field and the login field. 

```python
username = browser.find_element_by_id('user_id')        #username id is user_id
username.send_keys(usernameStr)                         #this prompt send the data stored in usernameStr to the username field
password = browser.find_element_by_id('password')       #password id is password
password.send_keys(passwordStr)                         #this prompt send the data stored in passwordStr to the password field
```

Now it is the time to click the login button

```python
signInButton = browser.find_element_by_id('entry-login')    #Login button id is entry-login
signInButton.click()                                        #this prompt clicks the button
```

### Adding it all together

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'Username'
passwordStr = 'Password'

browser = webdriver.Chrome()
browser.get(('https://ntulearn.ntu.edu.sg/webapps/login/'))

username = browser.find_element_by_id('user_id')
username.send_keys(usernameStr)
password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('entry-login')
signInButton.click()
```

### Cleaning up and adding it together

Now for the final part. Navigate into the Selenium folder, next click on the webdriver folder. Inside that, click the chrome folder and open the webdriver.py file.

```
Selenium >> webdriver >> chrome >> webdriver.py
```

In this file navigate to this part of the code and replace the executable_path value with the path of the folder.
```python
 def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None):
```
### Finishing up

Now run the code and allow the code to run its magic! Hope y'all can carry away skills from this workshop and had fun. 

# THAT'S ALL FOLKS! 

                
