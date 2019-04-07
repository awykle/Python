# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 5.4 pg 80 - Containers in Containers
# hashtagallison - Practice 2019-04-07
#-------------------------------------------


        # TIP---> You can store containers in containers

#-------------------------------------------
# EXAMPLE: pg 81
#-------------------------------------------
        
        # TIP---> You can store a lists in a list

lists = []

rap = [
    "Kanye West",
    "Jay Z",
    "Eminem",
    "Nas"
    ]

rock = [
    "Bob Dylan",
    "The Beatlels",
    "Led Zeppelin"
    ]

djs = [
    "Zeds Dead",
    "Tiesto"
    ]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

#-------------------------------------------
# EXAMPLE: pg 82
#-------------------------------------------
        
        # TIP---> The above example has three indexes and each index has a list.
        #       > You may access these lists by using the coorisponding index

rap = lists[0]

print(rap)

#-------------------------------------------
# EXAMPLE: pg 82
#-------------------------------------------
        
        # TIP---> If you append a new item to your inne list, 
        #         you will see a change when you print the outer list

rap = lists[0]
rap.append("Kendrick Lamar")

print(rap)
print(lists)

#-------------------------------------------
# EXAMPLE: pg 82-84
#-------------------------------------------
        
        # TIP---> You can store a tuple inside of a list, a list inside a tuple, 
        #         and a dictionary inside of a list or a tuple

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

eights = [
    "Edgar Allan Poe",
    "Charles Dickens"
    ]

nines = [
    "Hemingway",
    "Fitzgerald",
    "Orwell"
    ]

authors = (eights, nines)

print(authors)

bday = {
    "Hemingway": "7.21.1899",
    "Fitzgerald": "9.24.1896"
    }

my_list = [bday]

print(my_list)

my_tuple = (bday,)

print(my_tuple)

#-------------------------------------------
# EXAMPLE: pg 84
#-------------------------------------------
        
        # TIP---> A list, tuple, or dictionary can be a value in a dictionary

ny = {
    "location":(
            40.7128,
            74.0059
            ),

    "celebs": [
        "W. Allen",
        "Jay Z",
        "K. Bacon"
                ],

    "facts": {
        "state": "NY",
        "country": "America"
        }
    }

print(ny)