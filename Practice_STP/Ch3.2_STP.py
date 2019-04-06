# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 3.2 pg 35 - Statements
# hashtagallison - Practice 2019-04-05
#-------------------------------------------

        # TIP---> Conditional statements: if, elif, else
        #       > Control structure: a block of code that makes decisions by analyzing
        #           the values of of variables. Executes additonal code conditionally.

#-------------------------------------------
# EXAMPLE: pg 36-38
#-------------------------------------------


home = "America"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

home = "Canada"
if home == "America":
    print("Hello, America")
else:
    print("Hello, World!")

        # TIP---> You can have multiple if statements in a row
        #       > Code will only be executed if its expression evaluates to True
        #       > You may nest an if statement inside of another if statement

x = 2
if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")

x = 10
y = 11

# Both if statements must evaluate to True to print
if x == 10:
    if y == 11:
        print(x + y)


#-------------------------------------------
# EXAMPLE: pg 38
#-------------------------------------------

        # TIP---> elif-statements: (else-if) may be added indefinitely to if-else statements

home = "Thailand"
if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")

home = "Mars"
if home == "America":
    print("Hello, America!")
elif home == "Canada":
    print("Hello, Canada!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "Mexico":
    print("Hello, Mexico!")
else:
    print("Hello, World!")


#-------------------------------------------
# EXAMPLE: pg
#-------------------------------------------

        # TIP---> you may have multiple if and elif-statements in a row

x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("I don't know!")

if x == 100:
    print("x is 100!")

if x % 2 == 0:
    print("x is even!")
else:
    print("x is odd!")

        # TIP---> The above example is made up of three compound statements.
        #       > The first compound statement has 3 clauses.
        #       > The second compound statement has one clause.
        #       > The third compound statement has 2 clauses.
        #       > Note that spaces between statements help make the code more readable, and are ignored.



