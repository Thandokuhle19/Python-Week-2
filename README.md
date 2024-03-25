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
~ So, instead of keeping it in the constructor, we define it a static variable outside of the constructor.
~ Meaning it will still have the same four legs, thus legs attribute can be accessed directly on the class itself .
~ The variables are called "static" because they do not change with each instance. They are used to hold constants or fundamental business logic.
~ Eg, class Dog:
          legs = 4
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark !')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)

~ Static variables can change. To prevent this, programmers add underscore before the variable name. 
~ This shows that the variabe should not be changed directly, and a "getter" method should be used.
~ Getters are used 

# Instance and Static methods


_Inheritance:_
# Class inheritance
~ It is possible to inherit all the methods and attributes of another class, in the programming world.
~ Original class is the parent class, whereas the new class that extends is known as the child class.
~ Inheritance gets processed automatically when the child class is created.
~ Eg,  we have a dog class and a chihuahua class that needs to be created that inherits from the dog class. We do this by writing it like: "class Chihuahua(dog):" and include "pass" for now (to not have a an error), which creates a new class.
~ A chihuahua instance can then be created using all the methods and attributes of the parent dog class.
~ But, if the child class defines an attribute or method that is the same as the parent class, the parents version will be overwritten by the child's version.

# Extending Built-in Classes
~ Creating a new list can be done by representing it as "list" and even though it appears as a function. "list" is actually a class. 
~ We thus create a unique list class by extending the list class.
~ The unique list class inherits from the list class and therefore overrides the append function.
~ It will then return the item once it has checked the new function and if the item is already in the list.
~ The parent class will be called by the original append function in the parent class. We won't use the self.append because it will cause infinite recursion or an endless loop.
~ We do this by using the "super" function, which access the underlying instance of the parent class, and will be called super.append.
~ For the new class to be testedm we create a new instance of the unique list and append some items to it, and therefore print the list to see that it only records unique items.

_Handling Errors and Exceptions:_
~ Problems occur in python, and these problems are referred to as erros, while others times are called exceptions.
~ Exceptions stem from a class called the base exception, which in turn extends the base exception class.
~ Eg, when we divide by zero, an error occurs and this is a type of arithmetic error, which is a type of exception, which in turn extends the base exception class.
~ The base exception call provides useful and powerful properties to exceptions.
~ For instance, we take the division error, we can try to find in which file did it occur.
~ By finding this error, we can also find th specific line of where the error occured.
~ But now, if we place 1/10 into a function called "causeError" and then call this function, the stack becomes more defined.
~ We can analyse the original location of the function call and where within that function that error was triggered.
~ This entire traceback is known as a stack trace.
~ It is important to write clear cod and pay attention to your program's structure to avoid excessive debugging difficulties.

# Try/Except
~ Eg, we add 1/10 and then except. 
~ We are going to except as e, so e is going to be our variable.
~ This is a zero division error, we caught this exception and it will not be raised anymore. It is simply a class, it has attributes, you can create them, and they can be returned.
~ Eg, try:
         1/10
        except Exception as e:
            print(type(e))
will show <class 'ZeroDivisionError'>

_Managing and Handling Exceptions:_
~ For example, if we do not care about getting the specific instance of the exception, and we want to print something, we do not have to have the as e in order to catch an exception.
# Finally 
~ If you take the Try/Except block and add a finally to it, this will always executes and gets printed out.
~ Finally statements always execute no matter what happens inside this try block, no need for except statements. 
~ This error is thrown, but will still be printed out. Even if no exception is raised at all, that still executes.
~ This is used when timing how long a function takes to execute. So, if we import the time class, import time, this can be used to actually time our function.
~ 
