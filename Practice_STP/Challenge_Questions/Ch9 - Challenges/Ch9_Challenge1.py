# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 9 pg 129 - Challenges
# hashtagallison - Practice 2019-04-14
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 9: CHALLENGES
#               - Official Answer Key: http://tinyurl.com/hll6t3q  (Don't look until you try for yourself!!)
#-------------------------------------------


#1. Find a file on your computer and print its contents using Python.

import os

dontquit = []

# This is a local path on allis computer
# Must include "C:\\" with double back slashes or it will not print correctly.
#dontquit_path = "C:\\" + os.path.join("Users", "allis", "Documents", "programming", "dontquit.txt")

# This is for a file within this repo
dontquit_path = "dontquit.txt"

print(dontquit_path + "\n")

with open(dontquit_path, "r") as f:
    dontquit.append(f.read())

# Must print by index to have proper formatting.
print(dontquit[0])

# Writes to file:
#with open("dontquit.txt", "w") as f:
#    f.write(dontquit[0])


#2. Write a program that asks a user a question, and saves their answer to a file.

with open("question.txt", "w") as f:
    q1 = input("What is your favorite programming language?")
    f.write(q1)


#3. Take items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant",
#   "Inception"], ["Training Day", "Man on Fire", "Flight"]] and write them to a CSV file.
#       - The data in each list should be a row in the file, with each item in the list separated by a comma.

import csv

cruise = ["Top Gun", "Risky Business", "Minority Report"]
dicaprio = ["Titanic", "The Revenant", "Inception"]
washington = ["Training Day", "Man on Fire", "Flight"]

with open("actors.csv", "w", newline='') as f:
    w = csv.writer(f, 
                   delimiter=",")
    w.writerow(cruise)
    w.writerow(dicaprio)
    w.writerow(washington)




