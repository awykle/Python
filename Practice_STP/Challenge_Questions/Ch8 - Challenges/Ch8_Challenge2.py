# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 8 pg 121 - Challenge #2
# hashtagallison - Practice 2019-04-11
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 8: CHALLENGES - Question #2
#               - Official Answer Key: http://tinyurl.com/hlnsdot  (Don't look until you try for yourself!!)
#-------------------------------------------


#2. Create a module named cubed with a function that takes a number as a parameter, and returns the number cubed.
#   Import and call the function from another module.


import cubed

while True:
    x = input("Base number to cube: ") 

    if x == "q":
        print("END.")
        break

    else:
        print("--------------------")
        cubed.default(x)

    print("-------------------- Type 'q' to quit")
