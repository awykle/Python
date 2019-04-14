# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 9 pg 123 - Files
# hashtagallison - Practice 2019-04-13
#-------------------------------------------


        # TIP---> The first step to working with a file is to open it with the "open" function
        #       > It takes two parameters: the path of the file (string) and the mode to open the file (string)

#-------------------------------------------
# EXAMPLE: pg 123
#-------------------------------------------

        # TIP---> To avoid problems with your program working on different operating systems, you should use the "os" module
        #          - The path function takes each folder in the file path as a parameter and builds the path for you.
        #       > Working with file paths can be tricky. Visit https://theselftaughtprogrammer.io/filepaths for help.

import os
bob_file = os.path.join("Users", "bob", "st.txt")
print(bob_file)
 
#-------------------------------------------
# EXAMPLE: pg 124
#-------------------------------------------

        # TIP---> The mode you pass to the "open" function
