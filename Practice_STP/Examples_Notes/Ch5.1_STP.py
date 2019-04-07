# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 5.1 pg 67 - Containers - Lists
# hashtagallison - Practice 2019-04-06
#-------------------------------------------


        # TIP---> Containers allow you to store objects, like filing cabnets
        #           - Commonly used containers: lists, tuples, and dictionaries

#-------------------------------------------
# EXAMPLE: pg 67
#-------------------------------------------

        # TIP---> Methods are functions closely associated with a given tupe of data
        #           - They execute code and may return a result just like a function
        #           - You call a method on an object and may pass parameters

"Hello".upper()

"Hello".replace("o", "@")

#-------------------------------------------
# EXAMPLE: pg 67-68
#-------------------------------------------

        # TIP---> A list is a container that stores objects in a certain order.
        #       > Python starts counting at 0
        #       > There are two ways of creating a list:

# Creating a list with list()
fruit = list()
print(fruit)

# Creating a list with brackets:
fruit = []
print(fruit)

        # TIP---> You can create a list with items already in it by using [], and places each item within the brackets separated by commas
        #       > Lists store items in order (unless you change the order)

fruit = ["Apple", "Orange", "Pear"]
print(fruit)

#-------------------------------------------
# EXAMPLE: pg 69
#-------------------------------------------

        # TIP---> Add a new item to a list using the "append" method
        #       > Append always adds the item to the end of the list

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
print(fruit)

#-------------------------------------------
# EXAMPLE: pg 69
#-------------------------------------------

        # TIP---> Lists may store any data type

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

#-------------------------------------------
# EXAMPLE: pg 69
#-------------------------------------------

        # TIP---> Strings, lists and tuples are iterable, meaning that you may access each item using a loop
        #       > Objects that are iterable are called iterables
        #       > Each item in an iterable has an index that represents the item's position in the iterable
        #       > The first item on a list has an index of 0

# In the following example: 
# "Apple" has an index of 0
# "Orange" has an index of 1
# "Pear" has an index of 2

fruit = ["Apple", "Orange", "Pear"]

#-------------------------------------------
# EXAMPLE: pg 70
#-------------------------------------------

        # TIP---> You may retrieve an item with its index
        #       > If you try to access an index that doesn't exist, you'll get an exception: IndexError

fruit = ["Apple", "Orange", "Pear"]
print(fruit[0])
print(fruit[1])
print(fruit[2])

#-------------------------------------------
# EXAMPLE: pg 70
#-------------------------------------------

        # TIP---> Lists are mutable, which means you may add or remove objects from the container

colors =["blue", "green", "yellow"]
print(colors)
colors[2] = "red"
print(colors)

#-------------------------------------------
# EXAMPLE: pg 71
#-------------------------------------------

        # TIP---> You may remove the last item from a list using the method pop
        #       > You cannot use pop to empty a list - you will raise an exception

colors = ["blue", "green", "yellow"]
print(colors)
item = colors.pop()
print(item)
print(colors)

#-------------------------------------------
# EXAMPLE: pg 71
#-------------------------------------------

        # TIP---> You can combine two lists with the addition operator

colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
print(colors1 + colors2)

#-------------------------------------------
# EXAMPLE: pg 71-72
#-------------------------------------------

        # TIP---> You can check if an item is in a list with the keyword "in" or "not in"

colors = ["blue", "green", "yellow"]
print("green" in colors)
print("black" not in colors)

#-------------------------------------------
# EXAMPLE: pg 72
#-------------------------------------------

        # TIP---> You can get the size of a list (count) with the "len" function

print(len(colors))

#-------------------------------------------
# EXAMPLE: pg 72
#-------------------------------------------

# Guess a color program
colors = ["purple",
          "orange",
          "green"]

guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")