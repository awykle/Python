# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 7.1 pg 103 - Loops: for-loops
# hashtagallison - Practice 2019-04-08
#-------------------------------------------


        # TIP---> A loop is a piece of code that continually executes until a condition is satisfied.
        #       > A "for-loop" is a loop used to iterate through an iterable (called iterating)

#-------------------------------------------
# EXAMPLE: pg 103
#-------------------------------------------

        # TIP---> Use a for-loop to iterate through the characters of a string

name = "Ted"

# Each time around the loop, the variable "character" gets assigned an item in the iterable "name"
for character in name:
    print(character)

#-------------------------------------------
# EXAMPLE: pg 104-105
#-------------------------------------------

        # TIP---> Use a for-loop to iterate through the items in a list, tuple, or dictionary.

shows = [
    "GOT",
    "Narcos",
    "Vice"
    ]

for show in shows:
    print(show)

coms = (
    "A. Development",
    "Friends",
    "Always Sunny"
    )

for show in coms:
    print(show)

people ={
    "G. Bluth II": "A. Development",
    "Barney": "HIMYM",
    "Dennis": "Always Sunny"
    }

for character in people:
    print(character)

#-------------------------------------------
# EXAMPLE: pg 105
#-------------------------------------------

        # TIP---> Use for-loops to change the items in a mutable iterable (like a list)
        #       > Keep track of the current item in the list using an "index variable"
        #           - index variables start at 0 and is incremented each time around the loop


tv = [
    "GOT",
    "Narcos",
    "Vice"
    ]

i = 0

for show in tv:
    new = tv[i]    # index variable "i" and is stored in the variable "new"
    new = new.upper()   # calls the upper method on the variable "new"
    tv[i] = new    # replace the current item in the list with the result of the transformation (above)
    i += 1  # incriment the index variable by one to procede to the next item in the loop

print(tv)

#-------------------------------------------
# EXAMPLE: pg 105-106
#-------------------------------------------

        # TIP---> There is a short-cut syntax:
        #       > See below. Instead of iterating through "tv", pass "tv to "enumerate" and iterate through the result.
        #           - this allows the addition of a new variable "i", that keeps track of the current index.

tv = [
    "GOT",
    "Narcos",
    "Vice"
    ]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

#-------------------------------------------
# EXAMPLE: pg 106-107
#-------------------------------------------

        # TIP---> You can use for-loops to move data between mutable iterables.

#two for-loops take strings from two different lists, modify, and put them into a new list

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)