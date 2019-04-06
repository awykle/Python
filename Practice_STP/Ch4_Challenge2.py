# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 4 pg 66 - Challenges
# hashtagallison - Practice 2019-04-06
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 4: CHALLENGES
#               - Official Answer Key: http://tinyurl.com/hkzgqrv  (Don't look until you try for yourself!!)
#-------------------------------------------


#1. Write a function that takes a number as an input and returns that number squared.

def square():
    """
    Returns x ** 2
    :param x: float. 
    :return: float square of x.
    """
    try:
        x = input("Number to square: ")
        x = float(x)
        x_squared = x ** 2
        return(x_squared)
    except(ValueError):
        print("Error: May only square a real number.")
print(square())


#2. Create a function that accepts a string as a parameter and prints it.

def message():
    """
    Prints an input message
    :param x: str.
    :print: the string x
    """
    x = input("Type message here:")
    print(x)  
message()


#3. Write a function that takes three required parameters and two optional parameters.

def total_sum(a,b,c,d=0,e=0):
    """
    Sums three to five floats
    :param a: float.
    :param b: float.
    :param c: float.
    :param d: float.
    :param e: float.
    :return: float sum of a, b, c, d, and e.
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        abcde_sum = a + b + c + d + e
        return(abcde_sum)
    except(ValueError):
        print("Error: Must be a real number.")

num4 = 10

print(
    total_sum(
        input("first number:"),
        input("second number:"),
        input("third number:"),
        num4)
    )

#4. Write a program with two funtions. 
#   The first function should take an integer as a parameter and return the result of the integer divided by 2. 
#   The second function should take an integer as a parameter and return the result of the integer multiplied by 4. 
#   Call the first function, save the result as a variable, and pass it as a parameter to the second function.

def half(p=0):
    if(p >= 0):
        try:
            p = int(p)
            halfP = p / 2
            return(halfP)
        except(ValueError):
            print("Number must be a whole integer.")
    else:
        print("Must be a positive number.")

def times_4(f=0):
    f = int(f)
    fourF = f * 4
    return(fourF)

def times_2(f=0):
    f = int(f)
    fourF = f * 4
    return(fourF)

tables = input("How many tables are there?")
try:
    tables = int(tables)
except(ValueError):
    print("Number must be a whole integer.")

half_tables = half(tables)

chairs = times_4(half_tables)

print("Since we are only using half the tables, we will need a total of " + str(chairs) + " chairs.")

#5. Write a function that converts a string to a float and returns the result.
#   Use exception handling to catch the exception that could occur.

def string_to_float(s):
    try:
        s = float(s)
        return(s)
    except(ValueError):
        print("string must contain a value that may convert to a float")

print(string_to_float(input("Type a float here:")))

#6. Add a docstring to all of the functions that you wrote in challenges 1-5.

print("Done!")
