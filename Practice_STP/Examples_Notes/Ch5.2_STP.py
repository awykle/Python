# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 5.2 pg 73 - Containers - Tuples
# hashtagallison - Practice 2019-04-06
#-------------------------------------------


        # TIP---> A tuple is a container that stores objects in a specific order.
        #       > Unlike lists, tuples are immutable (their contents cannot change)
        #       > You can NOT modify, add, or remove items in a tuple
        #       > If you try to add new items to a tuple, it will raise an exception (TypeError)
        #       > Although, not flexible, tuples are useful if you know the values will not change
        #           and you want to ensure that other parts of the program won't change them.
        #           - Example: Geographic coordinates (lat/long)
        #       > Tuples may be used as keys in dictionaries (lists may not)

#-------------------------------------------
# EXAMPLE: pg 73
#-------------------------------------------
        
        # TIP---> Tuples are represented with (), there are two ways to define a tuple:
       
# First way to create a tuple:
my_tuple = tuple()
print(my_tuple)

# Another way to create a tuple:
my_tuple = ()
print(my_tuple)

#-------------------------------------------
# EXAMPLE: pg 73-74
#-------------------------------------------

        # TIP---> To add objects to a tuple, create one with () each item you want to add, separating them with commas

rndm = ("M. Jackson", 1958, True)
print(rndm)

        # TIP---> Even if the tuple only has one item you still need to put a comma after it
        #           - this differentiates it from a number in parentheses to denote it's position in order of operations

# This is a tuple
print(("self_taught",))

# This is not a tuple
print((9) + 1)

#-------------------------------------------
# EXAMPLE: pg 74
#-------------------------------------------

        # TIP---> You can get get items from a tuple the same way from a list
        #           - Reference it from an index
        #       > Remember that indexing starts at 0

dys = ("1984",
       "Brave New World",
       "Fahrenheit 451")

print(dys[2])

#-------------------------------------------
# EXAMPLE: pg 75
#-------------------------------------------

        # TIP---> You can check if an item is in a tuple using the keyword "in" or "not in"

dys = ("1984",
       "Brave New World",
       "Fahrenheit 451")

print("1984" in dys)
print("Handmaid's Tale" not in dys)

