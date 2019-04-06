# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 0 pg 0 - Challenges
# hashtagallison - Practice 2019-00-00
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 0: CHALLENGES
#               - Official Answer Key: http://  (Don't look until you try for yourself!!)
#-------------------------------------------


#1. Print three different strings.

print("Hello, World!")
print("This is my first challenge.")
print("Everyone loves tacos, right?")


#2. Write a program that prints a message if a variable is less than 10, and different messages if the variable is greater than or equal to 10.

tacos = 100

if tacos < 10 and tacos > 0:
    print("We need more tacos!")
elif tacos == 0:
    print("Who ate all the tacos?")
elif tacos == 10:
    print("10 tacos!!!!!!!!!!!!!!")
elif tacos > 10:
    print("There are so many tacos! I am so happy :)")
else:
    print("What about the tacos? The world is ending...")

#3. Write a program that prints a message if a vairable is less than or equal to 10, another message if the variable is greater than 10 but less than or equal to 25, and another message if the varaible is greater than 25. 

people = 3

if people <= 10 and people > 0:
    print("You get a taco, and you get a taco, and YOU get a taco!")
elif people > 10 and people < 25:
    print("It's a taco fiesta!")
elif people > 25:
    print("Not enough tacos, fend for yourself!")
else:
    print("Something's not right...how many people are here for tacos?")

#4. Create a program that dividestwo variables and prints the remainder.

print("Tacos per person:")
print(tacos // people)
print("Extra tacos:")
print(tacos % people)

#5. Create a program that takes two variables, divides tham, and prints the quotient.

sauce = 325

print("You may use exactly " + str(sauce / tacos) + " sauce packets per taco.")

#6. Write a program with a variable "age" assigned to an integer that prints different strings depending on what integer "age" is.

age = 30
if age >= 21:
    print("Have a margarita with your tacos!")
elif age < 21 and age >= 12:
    print("Have a Mexican Soda with your tacos!")
elif age < 12:
    print("Have a juice box with your tacos!")
else:
    print("Wait, how old did you say you are?")

 