# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 8.1 pg 117 - Modules
# hashtagallison - Practice 2019-04-11
#-------------------------------------------


        # TIP---> Programs are divided into multiple pieces, called modules
        #       > You may use code from one module in another module.
        #       > Python has built-in modules which contain important functionality
        #       > For a list of available built-in modules go to:
        #           https://docs.python.org/3/py-modindex.html
        #       > You should always import your modules at the top of the file,
        #         this makes it easy to read the code and know which modules are used in the program.

#-------------------------------------------
# EXAMPLE: pg 117-118
#-------------------------------------------

        # TIP---> To use a module, you must first import it. 
        #       > The "pow" funct. from the "math" module raises parameters x by y.

import math

print(math.pow(2, 3))

#-------------------------------------------
# EXAMPLE: pg 118
#-------------------------------------------

        # TIP---> The "random" module has a function called "randint" to generate a random int
        #       >   - The parameters tells it to return at int between both numbers.

import random

i = 10
while i > 0:
    print(random.randint(0,100))
    i -= 1

#-------------------------------------------
# EXAMPLE: pg 118-119
#-------------------------------------------

        # TIP---> The statistics module has functions to calculate the mean, median, and mode

import statistics

nums = [i, 5, 33, 12, 46, 33, 2]

# mean
print(statistics.mean(nums))

# median
print(statistics.median(nums))

# mode
print(statistics.mode(nums))

#-------------------------------------------
# EXAMPLE: pg 119
#-------------------------------------------

        # TIP---> Use the built-in "keyword" module to check if a string is a keyword in Python

import keyword

print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

#-------------------------------------------
# EXAMPLE: pg 119
#-------------------------------------------

        # TIP---> 