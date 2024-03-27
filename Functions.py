#creating our own custom functions
#parameters: input that you define for your function
#arguemt: actual value for the given parameter

def greet(first_name, last_name): #we are passin two parameters
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

greet("Thando", "Mandondo") #we call the function, and they have two arguments

print("\n")

#Two types of functions: 1, performs a task and 2, returns a value
#The functions below represent the two functions
def get_greet(first_name, last_name):
    return f"Hi {first_name} {last_name}" #used a return to return the value from the get_greet function

#because it returns a value, we store the value in a seperate variable
message = get_greet("Thando", "Mandondo")
print(message)

print("\n")

#create a function that will increment a number by a given value
def increment(number,by):
    return number + by

result = increment(2,1)
print(result) #the function will first call the increment function, get the result
#and it will temporary store it for us and then it will pass that variable

#functions that pass a variable number of arguments
#multiply function only takes two parameters thus won't have as many arguments
#to solve this, we use a plural name to indicate the collection of arguments

print("\n")

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


result = multiply(2,3,4,5)
print(result)

print("\n")


#**args - use the function to save arguments about this user
def save_user(**user):
    print(user) #to print out the whole dictionary
    print(user["name"]) #when we want to access our value keys only, we use square brackets, in this case its name only

save_user(id=1, name="Thando", age=21) #adding keyword arguments and passing three keyword arguments

print("\n")


#we have process called scope which is a region of the code where a variable is defined
#message = "a" #when we move the message variable outside the function, they are called global variables
# meaning they are accessible anywhere and in any functions
def greet(name): #scope of the variable is the greet function and it only exists inside of this function
    message = "a" #we call these variables locals because they only exist in that function and no where else

def send_email(name):
    message = "b"

greet("Thando")
print(message)
#the message variables are different from each other and are seperate

#have a fizzbuzz function