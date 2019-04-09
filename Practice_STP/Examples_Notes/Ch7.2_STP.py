# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 7.2 pg 107 - More Loops
# hashtagallison - Practice 2019-04-08
#-------------------------------------------


        # TIP---> You can user the built-in "range" function to create a sequence of integers,
        #         and use a for-loop to iterate through them. 
        #       > The "range" function takes two parameters (sequence start and sequence stop)
        #           - excludes the stop parameter in the return.

#-------------------------------------------
# EXAMPLE: pg 108 
#-------------------------------------------

        # TIP---> Programmers often name the variable "i" used to iterate through a list 

for i in range(1, 11):
    print(i)

#-------------------------------------------
# EXAMPLE: pg 108-109 
#-------------------------------------------

        # TIP---> A while-loop executes code as long as an expression evaluates to "True"
        #       > If you define a while loop with an expression that is always True, the loop will run forever.
        #           - This is called an infinite loop

x = 10

while x > 0:
    print('{}'.format(x))
    x -= 1

print("Happy New Year!")

#-------------------------------------------
# EXAMPLE: pg 109-110
#-------------------------------------------

        # TIP---> You can use a break-statement to terminate a loop.
        #       > As soon as Python hits the break statement, the loop ends.

# Will run 100 times:
#for i in range(0, 100):
#    print(i)

# Will only run once because of break statement
for i in range(0, 100):
    print(i)
    break

#-------------------------------------------
# EXAMPLE: pg 110
#-------------------------------------------

        # TIP---> You can use a while-loop and the break keywork to write a program
        #         that keeps asking the user for input until they type "q" to quit.

qs = [
    "What is your name?",
    "What is your fav. color?",
    "What is your quest?"
    ] 

n = 0
while True:
    print ("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3 # allows user to cycle indefinitely through every item on the list

#-------------------------------------------
# EXAMPLE: pg 111-112
#-------------------------------------------

        # TIP---> You can use a continue-statement to stop the current iteration of loop
        #         and move on to the next iteration.
        #       > You may achieve the same result by using a while-loop & continue-statement

# Skip number 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

#-------------------------------------------
# EXAMPLE: pg 112-113
#-------------------------------------------

        # TIP---> There is no limit to the number of loops you can have inside other loops.
        #           - However, you DO want to limit this.
        #       > When you have a nested loop, the inner loop iterates through its iterable once
        #         for each time around the outer loop. 

for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

#-------------------------------------------
# EXAMPLE: pg 113
#-------------------------------------------

        # TIP---> You can use two for-loops to add each number in a list to all the numbers
        #         in another list.

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

#-------------------------------------------
# EXAMPLE: pg 113-114
#-------------------------------------------

        # TIP---> You can nest a for-loop inside a while-loop and vice versa.

while input('y or n?') != 'n':
    for i in range(1, 6):
        print(i)

