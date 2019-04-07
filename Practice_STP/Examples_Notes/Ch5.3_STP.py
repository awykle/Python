# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 5.3 pg 76 - Containers - Dictionaries
# hashtagallison - Practice 2019-04-07
#-------------------------------------------


        # TIP---> Dictionaries are another built-in container for storing objects. 
        #       > They are used to link one object (called a key) to another object (called a value)
        #       > Linking one object to another is called mapping, this creates a key-value pair.
        #       > Add key-value pairs to a dictionary, then you can look up a key to gets its value.
        #           - You CANNOT use a value to look up a key
        #       > Dictionaries are mutable (you can add new key-value pairs)
        #           - Dictionary values may be are mutable
        #           - Dictionary keys must be immutable
        #               > A string or tuple can be a dictionary key (a list or dictory CANNOT be a key) 
        #       > They do not store objects in a specific order.
        #       > Example: storing demographic information about someone
        #       > Dictionaries are represented with curly brackets



#-------------------------------------------
# EXAMPLE: pg 76-77
#-------------------------------------------
        
        # TIP---> There are two syntaxes for creating dictionaries:

# First way to define a new dictionary:
my_dict = dict()
print(my_dict)

# Another way to define a new dictionary:
my_dict = {}
print(my_dict)

#-------------------------------------------
# EXAMPLE: pg 76-77
#-------------------------------------------
        
        # TIP---> Add key pairs with the key separated by the value using a colon
        #       > Use a comma to separate each key-value pair

fruits = {
    "Apple": "Red",
    "Banana": "Yellow",
    }

print(fruits)

        # TIP---> Remember that the output is an arbitrary order: the order is not stored

#-------------------------------------------
# EXAMPLE: pg 76-78
#-------------------------------------------
        
        # TIP---> Dictionaries are mutable (you can add key-value pairs)

facts = dict()

# Add a value
facts["code"] = "fun"

# Look up a key
print(facts["code"])

# Add a value
facts["Bill"] = "Gates"

# Look up a key
print(facts["Bill"])

# Add a value
facts["founded"] = 1776

# Looks up a key
print(facts["founded"])

#-------------------------------------------
# EXAMPLE: pg 78-79
#-------------------------------------------
        
        # TIP---> Use the "in" or "not in" keywords to check if a key is in a dictionary
        #       > You CANNOT use the above keywords to check if a value is in a dictionary
        #       > If you try to access a key that isn't in a dictionary, Python will raise an exception

bill = dict({
    "Bill Gates": "charitable"
    })

print("Bill Gates" in bill)

print("Bill Doors" not in bill)

#-------------------------------------------
# EXAMPLE: pg 79
#-------------------------------------------
        
        # TIP---> You can delete a key-value pair from a dictionary with the keyword "del"

books = {
    "Dracula": "Stoker",
    "1984": "Orwell",
    "The Trial": "Kafka"
    }

del books["The Trial"]

print(books)

#-------------------------------------------
# EXAMPLE: pg 80
#-------------------------------------------
        
        # TIP---> Here is an example of a program using a dictionary

rhymes = {
    "1": "fun",
    "2": "blue",
    "3": "me",
    "4": "floor",
    "5": "live"
    }

n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")