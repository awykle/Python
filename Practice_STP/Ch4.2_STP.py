# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 4.2 pg 61 - Exception Error Handling
# hashtagallison - Practice 2019-04-05
#-------------------------------------------


#-------------------------------------------
# EXAMPLE: pg 61
#-------------------------------------------

        # TIP---> Remember to consider how the wrong user input may cause an error

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
print(a / b)

#-------------------------------------------
# EXAMPLE: pg 62
#-------------------------------------------

        # TIP---> The keywords "try" and "except" are used for exception handling
        #       > See a list of built-in Python exceptions here:
        #       > https://www.tutorialspoint.com/python/standard_exceptions.htm

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")

#-------------------------------------------
# EXAMPLE: pg 63-64
#-------------------------------------------

        # TIP---> Use input validation with the try and except keywords
        #       > Don't use variables defined in a try statement within an except statement
        #           - This would result in the variable being undefined (out of scope)

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError,
        ValueError):
    print("Invalid input.")

#-------------------------------------------
# EXAMPLE: pg 64
#-------------------------------------------

        # TIP---> Docstrings explain what a function does, and documents what kinds of parameters it takes
        #       > It is good practice to include a docstring when writing a function.

def add(x, y):
    """
    Returns x + y. <---Explain what the function does
    :param x: int. <---List parameters and types
    :param y: int.
    :return: int sum of x and y. <---List what the function returns, prints, etc.
    """
    return x + y

#-------------------------------------------
# EXAMPLE: pg 65
#-------------------------------------------

        # TIP---> Only use a variable when needed to keep clean code

# Unnecessary use of variable:
x = 100
print(x)

# Instead, pass the integer directly to the print function
print(100)