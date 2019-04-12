# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 8 pg 121 - Challenges
# hashtagallison - Practice 2019-04-11
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 8: CHALLENGES
#               - Official Answer Key: http://tinyurl.com/hlnsdot  (Don't look until you try for yourself!!)
#-------------------------------------------


#1. Call a different function from the statistics module.

# More about the statistics module: https://docs.python.org/3/library/statistics.html#module-statistics

import statistics

group = [1, 22, 333, 4444, 55555]

pdev = statistics.pstdev(group) # population standard deviation of data

print(pdev)

#2. Create a module named cubed with a function that takes a number as a parameter, and returns the number cubed.
#   Import and call the function from another module.

# See the other files in the folder for the result.