# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 6.2 pg 92 - More String Manipulation
# hashtagallison - Practice 2019-04-08
#-------------------------------------------



#-------------------------------------------
# EXAMPLE: pg 92-93
#-------------------------------------------

        # TIP---> You can use the "split" method to spearate one string into two or more strings.
        #       > Specify the parameter that you would like to use for splitting (such as ".")

print("Hello. Yes!".split("."))

#-------------------------------------------
# EXAMPLE: pg 93-94
#-------------------------------------------

        # TIP---> The "join" method lets you add new characters between every character in a string.
        #       > You can turn a list of strings into a single string by calling the "join" method on an empty string and passing in the list as a parameter 

first_three = "abc"
result = "+".join(first_three)

print(result)

words= ["The",
        "fox",
        "jumped",
        "over",
        "the",
        "fence",
        "."
       ]

one = "".join(words)

print(one)

#using join to separate each word with a space (note the space printed before the period on the output)

one = " ".join(words)

print(one)

#-------------------------------------------
# EXAMPLE: pg 94
#-------------------------------------------

        # TIP---> You can use the "strip" method to remove leading and trailing whitespace from a string.

s = "   The     "
s = s.strip()

print(s)

#-------------------------------------------
# EXAMPLE: pg 94-95
#-------------------------------------------

        # TIP---> The "replace" method replaces every occurrence of a string with another string.
        #       > First parameter is the string to replace, the second parameter is what it will be replaced with.

equ = "All animals are equal."
equ = equ.replace("a", "@")

print(equ)

#-------------------------------------------
# EXAMPLE: pg 95
#-------------------------------------------

        # TIP---> You can get the index of the first occurance of a character in a string with the "index" method.
        #       > Pass the character that you are looking for as a parameter.
        #       > Python raises an exception if the index method does not match. (ValueError)

print("animals".index("m"))

# Using exception handling if unsure there will be a match

try: print("animals".index("z"))
except:
    print("Not found.")

#-------------------------------------------
# EXAMPLE: pg 96
#-------------------------------------------

        # TIP---> The "in" and "not in" keywords check if a string is in another string
        #       > Returns either True or False

print("Cat" in "Cat in the hat.")

print("Bat" in "Cat in the hat.")

print("Potter" not in "Harry")

#-------------------------------------------
# EXAMPLE: pg 96-97
#-------------------------------------------

        # TIP---> If you use quotes inside of a string, you will get a syntax error (InvalidSyntax)
        #       > You may fix this error by prefacing the quotes with backslashes \
        #       > Escaping a string means putting a symbol in front of a character that normally has a special
        #         meaning in Python. It lets Python know that, in the instance, the quote is meant to represent a character.

print("She said \"Surely.\"")

print('She said \"Surely.\"')

# You do NOT need to escape single quotes within double quotes.

print("She said 'Surely.'")

# You can put double quotes inside of single quotes (instead of escaping with a \)

print('She said "Surely."')

#-------------------------------------------
# EXAMPLE: pg 98
#-------------------------------------------

        # TIP---> Putting "\n" inside of a string represents a new line.

print("line1\nline2\nline3")

#-------------------------------------------
# EXAMPLE: pg 98-100
#-------------------------------------------

        # TIP---> Slicing is a way to return a new iterable from a subset pf the items in another iterable.
        #       > You want to include the index to STOP slicing at, which means +1 of the last index you want returned. 

# Slicing a list:

fict = ["Tolstoy",
        "Camus",
        "Orwell",
        "Huxley",
        "Austin"]

print(fict[0:3])

# Slicing a string:

ivan = "In place of death there was light."

print(ivan[0:17])
print(ivan[17:33])

        # TIP---> If your start index was zero, you can leave the start index empty
        #       > If your end index is the index of the iterable, you can leave the end index empty
        #       > Leaving both the start and end index empty, returns the original iterable

print(ivan[:17])

print(ivan[17:])

print(ivan[:])