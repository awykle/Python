# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 4.1 pg 48 - Functions
# hashtagallison - Practice 2019-04-05
#-------------------------------------------


#-------------------------------------------
# EXAMPLE: pg 48-49
#-------------------------------------------

        # TIP---> By convention, you should never use capital letters in a function name, and words should be separated by underscores: like_this

def f(x):
    return x * 2

result = f(2)
print(result)


#-------------------------------------------
# EXAMPLE: pg 50
#-------------------------------------------

        # TIP---> You can save the result of a function in a variable, whenever you need to use that result later.

def f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")

#-------------------------------------------
# EXAMPLE: pg 50
#-------------------------------------------

        # TIP---> To define a function with no parameters, leave the parentheses empty when defining the function.
        #       > To define multiple parameters, separate parameters with a comma.

def f():
    return 1 + 1

result = f()
print(result)


def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)


#-------------------------------------------
# EXAMPLE: pg 51
#-------------------------------------------

        # TIP---> A function does not need to have a return statement.
        #       > If a function doesn't have a return, it returns "None"

def f():
    z = 1 + 1

result = f()
print(result)


#-------------------------------------------
# EXAMPLE: pg 51-53
#-------------------------------------------

        # TIP---> Built-in functions are included in a library when Python is installed
        #       > Example: print function

# length of an object
print(len("Monty"))
print(len("Python"))

# convert to string object
print(str(100))

#convert to integer object
print(int("1"))

#convert to floating-point number object
print(float(100))

        # TIP---> Remember that the parameter you pass must be able to convert

print(int("110"))
print(int(20.54))

print(float("16.4"))
print(float(99))

#-------------------------------------------
# EXAMPLE: pg 53-54
#-------------------------------------------

        # TIP---> input() is a built-in function that collects information from the user of the program
        #       > This allows you to save the users' responses as variables to use later
        #       > The input() function collects the data as a string, so it may need to be converted

age = input("Enter your age")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")

#-------------------------------------------
# EXAMPLE: pg 54-56
#-------------------------------------------

def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(2)
even_odd(3)


        # TIP---> Functions are useful because they allow you to reuse functionality (write less code)
        #       > Try to use functions to consolidate tasks that would otherwise need to be repeated

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd()
even_odd()
even_odd()

#-------------------------------------------
# EXAMPLE: pg 56-57
#-------------------------------------------

        # TIP---> optional parameters are defined with a default value

def f(x=2):
    return x ** x

print(f())
print(f(4))

        # TIP---> You can define a function with BOTH optional and required parameters
        #       > You MUST define ALL required parameters before the optional ones

def add_it(x, y=10):
    return x + y

result = add_it(2)
print(result)

#-------------------------------------------
# EXAMPLE: pg 58-59
#-------------------------------------------

# Global variables with global scope:
x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

        # TIP---> If you define variables inside of a function, you may only read or write to them from withing the function
        #       > If you try to call them outside of the function, you will get an exception error

# Local variables with local scope to function f()
def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)

f()

#-------------------------------------------
# EXAMPLE: pg 60
#-------------------------------------------

        # TIP---> You can read/write to a global variable from anywhere
        #       > To write to a global variable from a local scope, you MUST define it as global

x = 100

def f():
    global x
    x += 1
    print(x)

f()