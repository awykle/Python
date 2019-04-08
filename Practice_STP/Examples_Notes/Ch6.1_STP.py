# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 6.1 pg 87 - String Manipulation
# hashtagallison - Practice 2019-04-08
#-------------------------------------------



#-------------------------------------------
# EXAMPLE: pg 87
#-------------------------------------------

        # TIP---> If you have a string that spans more than one line, you must put it in triple quotes (""")

print(
"""line one
line two
line three"""
)

#-------------------------------------------
# EXAMPLE: pg 87-88
#-------------------------------------------

        # TIP---> Strings, like lists and tuples are iterable.
        #       > You may look up each character in a string using an index
        #       > The first character in a string starts at 0 (incremented by 1)
        #       > If you try to look up a character past the last index, it will raise an exception:\
        #           - IndexError

author = "Kafta"

print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

#-------------------------------------------
# EXAMPLE: pg 88-89
#-------------------------------------------

        # TIP---> You may also look up using a negative index.
        #       > This would look up items in an iterable from right to left
        #           - starting with the last character
        #       > Start with [-1] to look up the last item.

author = "Kafka"

print(author[-1])
print(author[-2])
print(author[-3])
print(author[-4])
print(author[-5])

#-------------------------------------------
# EXAMPLE: pg 89
#-------------------------------------------

        # TIP---> Strings are immutable (you cannot change the characters in a string)
        #       > If you want to change the characters in a string, you must create a new string.

ff = "F. Fitzgerald"
ff = "F. Scott Fitzgerald"

print(ff)

#-------------------------------------------
# EXAMPLE: pg 89-90
#-------------------------------------------

        # TIP---> Concatenation:
        #           - You can add two (or more) strings together using the addition operator.

print("cat" + "in" + "hat") 

print("cat" + " in" + " the" + " hat")


#-------------------------------------------
# EXAMPLE: pg 90
#-------------------------------------------

        # TIP---> You can multiply a string by a number with the multiplication operator:

print("Sawyer" * 3)

#-------------------------------------------
# EXAMPLE: pg 90-91
#-------------------------------------------

        # TIP---> You can change every character in a string to uppercase by calling the "upper" method
        #       > You may change every character to lowercase by calling the "lower" method
        #       > You can capitalize the first letter of a sentence by calling the "capitalize" method on a string

print("We hold these truths...".upper())

print("SO IT GOES.".lower())

print("four score and...".capitalize())

#-------------------------------------------
# EXAMPLE: pg 91-92
#-------------------------------------------

        # TIP---> You can create a new string using the format method.
        #           - this looks for occurrances of {} in a string and replaces them with the parameters you pass in.
        #       > You may also pass a variable as a parameter.
        #       > You may do this more than once in the same string.

print("William {}".format("Faulkner"))

last = "Faulkner"

print("William {}".format(last))

author = "William Faulkner"
year_born = "1897"

print("{} was born in {}.".format(author, year_born))

#-------------------------------------------
# EXAMPLE: pg 92
#-------------------------------------------

        # TIP---> The format method is useful if you are creating a string from user input

n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter an adj:")
n2 = input("Enter a noun:")

r = """The {} {} the {} {}
    """.format(
        n1,
        v,
        adj,
        n2
        )

print(r)