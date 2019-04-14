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

        # TIP---> The mode you pass to the "open" function determines the actions you may perform:
        #           - "r" opens a file for read only
        #           - "w" opens a file for writing only.
        #               * Overwrites the file if the file exists.
        #               * If the file does not exist, creates a new file for writing.
        #           - "w+" opens a file for reading and writing only.
        #               * Overwrites the file if the file exists.
        #               * If the file does not exist, creates a new file for reading and writing.
        #       > The open function return a file object, which you can use to read/write to the file
        #       > You use the "write" method on the file to write and "close" method to close the file.
        #           - If you use "open" you must use "close" to close the file.
        #           - forgetting to close a file may cause problems in the program later.

st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

#-------------------------------------------
# EXAMPLE: pg 124-125
#-------------------------------------------

        # TIP---> Using a with-statement is the preferred syntax for opening files,
        #         this prevents you from having to remember to close them.
        #           - While using this syntax, the file is automatically closed after the suite in your code executes.
        #       > As long as you are inside the with-statement, you may access the file object (f)
        #           - the file is closed after the with-statement is finished running.
        #       > Remember that a with-statement is a compound statement with an action that automatically occurs
        #         when Python leaves it.

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

#-------------------------------------------
# EXAMPLE: pg 125-126
#-------------------------------------------

        # TIP---> If you want to read the file, you pass in "r" as the second parameter to "open".
        #       > Next, you call the "read" method on your file object (f), which returns an iterable
        #         containing each line of the file.

with open("st.txt", "r") as f:
    print(f.read())

        # TIP---> You may only call "read" on a file ONCE (without closing and reopening it),
        #         therefore, you should save the file contents in a variable or container if you need to use it later.

my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)

#-------------------------------------------
# EXAMPLE: pg 126-127
#-------------------------------------------

        # TIP---> CSV = Comma Separated Values
        #       > Often used by programs such as Excel.
        #           - Each item separated by a comma represents a cell
        #           - Each line represents a row.
        #       > A delimiter is a symbol (like a comma) used to sparate data.
        #       > When you use a with-statement to open a CSV file, you must use a "csv" module to convert the file
        #           - The "writer" method accepts a file object with a delimeter
        #           - This returns a csv object with a method called "writerow"
        #       > The "writerow" method accepts a list as a parameter, which may be used to write to a CSV file.
        #           - Every item on the list will be written to the CSV file
        #           - The "writerow" method only creates one row (you must call it twice to create two rows)

import csv

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])

#-------------------------------------------
# EXAMPLE: pg 127-128
#-------------------------------------------

        # TIP---> You can also use the "csv" module to read the contents from a file.
        #           - Use the "r" parameter and specify the delimiter.
        #       > You can iterate through the csv object using a loop.
        #           - Each time around the loop, the join method adds a comma between each piece of data
        #               * This preserves the original format of the CSV file.

import csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))