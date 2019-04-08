# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 5 pg 85 - Challenges
# hashtagallison - Practice 2019-04-07
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 5: CHALLENGES
#               - Official Answer Key: http://http://tinyurl.com/z54w9cb  (Don't look until you try for yourself!!)
#-------------------------------------------


#1. Create a list of your favorite musicians.

artists = [
    "Portugal. The Man",
    "half∙alive",
    "Miike Snow"
    ]

#2. Create a list of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited.

old_stomping_grounds = []

detroit = (42.3314, 83.0458),
houston = (29.7604, 95.3698),
orlando = (28.5383, 81.3792)

old_stomping_grounds.append(detroit)
old_stomping_grounds.append(houston)
old_stomping_grounds.append(orlando)

print(old_stomping_grounds)

#3. Create a dictionary that contains different attributes about you: height, favorite color, favorite author, etc.

aboutme = {
    "height": "5ft 4in",
    "favorite color": "pink",
    "favorite author": "Cory Althoff"
    }

print(aboutme)

#4. Write a program that lets the user ask your height, favorite color, or favorite author, and returns the result from the dictionary you created in the previous challenge. 

print(
    """
    Ask a question about me.
    (1) How tall are you?
    (2) What is your favorite color?
    (3) Who is your favorite author?
    """
    )
q = input("Pick a number:")

if q == "1":
    print("I am " + aboutme["height"] + " tall.")
elif q == "2":
    print("My favorite color is " + aboutme["favorite color"] + ".")
elif q == "3":
    print("My favorite author is " + aboutme["favorite author"] + "! He taught me Python!")
else:
    print("Must choose question 1, 2, or 3. Enter the number only.")


#5. Create a dictionary mapping your favorite musicians to a list of your favorite songs by them.

songs = [
    "Live in the Moment",
    "still feel.",
    "Genghis Khan"
    ]

playlist = {
    artists[0]: songs[0],
    artists[1]: songs[1],   
    artists[2]: songs[2],  
    }

print(playlist)

#6. Lists, tuples, and dictionaries are just a few of the containers built into Python. Research Python sets (a type of container). When would you use a set?

print("""
    A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. 
    Python’s set class represents the mathematical notion of a set. The major advantage of using a set, as opposed to a list, 
    is that it has a highly optimized method for checking whether a specific element is contained in the set. 
    This is based on a data structure known as a hash table.

    Frozen Sets Frozen sets are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.

    ^^^Source: https://www.geeksforgeeks.org/sets-in-python/

    Documentation: https://docs.python.org/2/library/stdtypes.html#set
    """)