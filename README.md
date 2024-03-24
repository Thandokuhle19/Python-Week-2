# Python-Week-2
_Anatomy of a Function:_
Programs involve systems, tasks, objects, and interacting components, thus programmers need to think of designig programs rather than just following instructions.
For this reason, the basic unit of a program is a function.
Without functions, a program lacks functionality. 
# Functions:
~ Composed of a name and parameters, which are symbolised by the 'def' statement.
~ 
# Named Parameters:
~
*args:
~ There is a rule when using keywords in Python, and that is they must come after the positional arguments.
~ The order for the first two arguments is important and cannot be changed. But, after these mandatory arguments, they keyword arguments can be in any order.
~ To allow users to pass in any number of variables, use the asterisk (*) symbol before the argument name to create a pointer to the inputted variables(like this: *args).
~ 
**kwargs:
~ We use kwargs method to handle keyword arguments. Kwargs is short for keyword arguments.
~ Keyword arguments are now stored as a dictionay instead of a tuple. 
~ Dictionary is a more appropriate data structure for referencing keywords, since keyword arguments have keys and values and can be passed in order.


_Variables and Scope:_
This part focuses on how gloabl and local variables interact.
Function Scope:
~ In the previous section, we had discussed that *args and *kwargs, which were used to print out the arguments passed into a function.
~ This allowed us to see a tuple and dictionary of the passed arguemens
~ A method called "locals" (locals())function allows us to access all the variables within a Python function without any asterisks.
~ For example we will use the locals functions to print the output. So, let's call perform operation with the arguments one and two and specify that the operation is multiplication.
~ locals() are only accessible locally within the function. These variables can be defined by any name within the function definition, and it will only be avaialable anywhere within that function.
~ Hence we do not reference a variable outside its scope because it will result to an error.
~ local varibles are definied inside the function and global variables are defined outside a function.
~ globals() are built-in functions that enables us to retrieve all these variables.
~ Global and Local scope: 

_Functions as Variables:_
# Variables as functions
~ Both variables and functions both have names and data associated with them.
~ But, for functions, the data includes inofrmation about required parameters and lines of instructions to be executed.

# Viewing Function Data with _code_
~ "code" attribute of Python function objects can be used to confirm that functions are just variables in Python. 
~ Functions are not unique in Python, they are variables associated with some data.

# Text Processing in Python
~ There are two text processing operations, and a functions that can make the text lowercase, remove punctuations, new lines, and words that are three characters or less.
~ Can remove long words.
~ Calling these functions in a list, we can change the order or decided which function to apply.

# Lambda Functions
~ We represent a function without giving it a variable name.
~ 5 or 2 + 3 can be written without assigning it to a variable, a small function can be defined by using the lambda keyword.
~ Eg, x: x + 3 is a lambda function that takes a sinle parameter x and returns x + 3. There won't be a need to return keyword in lambda functions.
~ Lambda functions can be helpful in a sense that you will need to pass a function as an argument to another Python function.
~ Lambda functions are convenient for writing small functions that you need while writing code.

_Anatomy of a Class:_
# Instance Attributes
~ As much as there can be confusion, we can gather an example of a class created: the dog class. This class has two instance attributes, which is name and legs. These are the attributes that every instance of a dog class does possess.
~ However, when we create a new instance, such as "Rover", we can print its name and legs by using "my_dog.name" and "my_dog.legs".
~ Eg: class Dog:
    def __init__(self,name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark !')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
~ If we try to access "dogs.legs", we will get an error, and we cannot modify the value of legs.

# Static Attributes
~ 
