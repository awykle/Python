# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 3.1 pg 13 - Intro to Programming
# hashtagallison - Practice 2019-04-04
#-------------------------------------------

#-------------------------------------------
# EXAMPLE: pg 13
#-------------------------------------------

for i in range(100):
    print("Hello, World!")

        # TIP---> Indents must be four spaces
        #       > Use three quotes if you have a long line of code extending to another line
        #       > Use a \ to extend code to the next line

#-------------------------------------------
# EXAMPLE: pg 16-17
#-------------------------------------------

print\
    ("""This is a really really
    really really "really long line of
    code.""")

        # TIP---> You can use single or double quotes for strings as long as they match 
        #       > Object with the data type NoneType always have the value None. They are used to represent the absence of value. 

#-------------------------------------------
# EXAMPLE: pg 20
#-------------------------------------------

print(2+2)

print (2-2)

print (4/2)

print(2*2)


        # TIP---> Create a floating number when dividing ints 
        #       > A constant is a value that never changes (such as the number 2 in the example above)
        #       > A variable is assigned using the assignment operator (the = sign)

#-------------------------------------------
# EXAMPLE: pg 21-22
#-------------------------------------------

b = 100
print(b)

x = 100
print(x + b)

x = 200
print(x + b)

#-------------------------------------------
# EXAMPLE: pg 23
#-------------------------------------------

        # TIP---> You may incriment and dedecrement a variable in two ways, below

x = 10
x = x - 1
print(x)

x = 10
x -= 1
print(x)    

x = 10
x += 1
print(x)

#-------------------------------------------
# EXAMPLE: pg 23-24
#-------------------------------------------

hi = "Hello, World!"
print(hi) 

my_float = 2.2
print(my_float)

my_boolean = True
print(my_boolean)

        # TIP---> Rules for variables:
        #           1. Variable names cannot have spaces
        #           2. Variable names may contain letters, numbers, or the underscore symbol
        #           3. You cannot start a variable name with a number
        #           4. You can start a variable with an underscore BUT it has a special meaning (covered later in the course)
        #           5. You cannot use python keywords for variable names
        #               *List of keywords here: http://theselftaughtprogrammer.io/keywords
        #       > There are two types of errors: syntax and exception (non-synatax)
        #               - An example of an exception error is ZeroDivisionError (Occurs if you try to divide by zero)
        #               - Unlike syntax errors, exception errors are NOT necessarily fatal (the program may still be able to run)
        #               - Another common error is IndentationError


#-------------------------------------------
# EXAMPLE: pg 27-28
#-------------------------------------------

        # TIP--->               ARITHMETIC OPERATORS 
        #       -------------------------------------------------------------
        #       Operator: | Meaning:            | Example:    | Evaluates to:
        #       -------------------------------------------------------------
        #           **      Exponent              2 ** 2        4
        #           %       Modulo/Remainder      14 % 4        2
        #           //      Int Div/Floored Quot  13 // 8       1
        #           /       Division              13 / 8        1.625
        #           *       Multiplication        8 * 2         16
        #           -       Subtraction           7 - 1         6
        #           +       Addition              2 + 2         4
        #       -------------------------------------------------------------    


        # TIP---> When you use a modulo on two numbers, if there is no remainder (modulo returns 0), the number is even, otherwise it is odd.

# even
print(12 % 2)

# odd
print(11 % 2)

# division to return the floored quotient as an int
print(14 // 3)

# division to return a floating point 
print(14 / 3)

# exponent
print(2 ** 2)     

#-------------------------------------------
# EXAMPLE: pg 29
#-------------------------------------------

        # TIP---> Order of operations, remember: "Please Excuse My Dear Aunt Sally"

print(2 + 2 * 2)

print((2 + 2) * 2)

#-------------------------------------------
# EXAMPLE: pg 29-32
#-------------------------------------------

        # TIP--->               COMPARISON OPERATORS 
        #       ---------------------------------------------------------------
        #       Operator: | Meaning:              | Example:    | Evaluates to:
        #       ---------------------------------------------------------------
        #           >     Greater than              100 > 2         True
        #           <     Less than                 100 < 10        False
        #           >=    Greater than or equal to  2 <= 2          True
        #           <=    Less than or equal to     1 <= 4          True
        #           ==    Equal                     6 == 9          False
        #           !=    Not Equal                 3 != 2          True
        #       ---------------------------------------------------------------

        # TIP---> Remember that a single = is used to make an assignment NOT the same as ==

print(100 > 10)

print(100 < 10)

print(2 >= 2)

print(2 <= 2)

print(2 == 2)

print(1 == 2)

print(1 != 2)

print(2 != 2)

#-------------------------------------------
# EXAMPLE: pg 32-35
#-------------------------------------------

        # TIP--->               LOGICAL OPERATORS 
        #       ---------------------------------------------------------------
        #       Operator: | Meaning:      | Example:            | Evaluates to:
        #       ---------------------------------------------------------------
        #           and         and         True and True           True
        #           or          or          True or False           True
        #           not         not         not True                False
        #       ---------------------------------------------------------------

print(1 == 1 and 2 == 2)

print(1 == 2 and 2 == 2)

print(1 == 2 and 2 == 1)

print(2 == 1 and 1 == 1)

print(1 == 1 and 10 != 2 and 2 < 10)

print(1 == 1 or 1 == 2)

print(1 == 1 or 2 == 2)

print(1 == 2 or 2 == 1)

print(1 == 1 or 1 == 2 or 1 == 3)


        # TIP---> placing the keyword not in front of an expression will change the result of the evaluation
        #         to the opposite of what it would have otherwise evaluated to.

print(not 1 == 1)

print(not 1 == 2)



