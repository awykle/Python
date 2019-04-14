# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 7 pg 114 - Challenges
# hashtagallison - Practice 2019-04-08
#-------------------------------------------

#-------------------------------------------
#       CHAPTER 7: CHALLENGES
#               - Official Answer Key: http://tinyurl.com/z2m2ll5  (Don't look until you try for yourself!!)
#-------------------------------------------


#1. Print each item in the following list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"].

hbo = [
    "The Walking Dead", 
    "Entourage", 
    "The Sopranos", 
    "The Vampire Diaries"
    ]

for recommend in hbo:
    print(recommend)


#2. Print all the numbers from 25 to 50.

for i in range(25,51):
    print(i)


#3. Print each item in the list from the first challenge and their indexes.

i = 0
for recommend in hbo:
    print(str(i) + " - " + recommend)
    i += 1

#4. Write a program with an infinite loop (with the option to type q to quit) and a list of numbers. Each time through
#   the loop, ask the user to guess a number on the list and tell them whether or not they guessed correctly.

secret_nums = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]
wins = 0
fails = 0
guesses = []
cracked = []

print("\n----------------------------------------")
print("       NEW GAME -- CRACK THE CODE")
print("----------------------------------------\n")

while True:
    print("Type 'q' to quit")
    print("Type 'c' to start over (clears wins/fails/guesses)")
    print("Type 'g' to see your guesses so far")
    print("\n----------------------------------------")
    guess = input("\nGuess the secret numbers between 1 and 999999999: ")
    try:
        if guess == "c":
            wins = 0
            fails = 0
            guesses = []
            cracked = []
            print("\n----------------------------------------")
            print("       NEW GAME -- CRACK THE CODE")
            print("  Stats and guesses have been cleared.")
            print("----------------------------------------\n")
        elif guess == "g":
            print("\n----------------------------------------")
            print("You guessed " + str(wins) + "/9 numbers!" )
            print(str(fails) + " failed attempts.\n")
            print("Secret numbers discovered so far:")
            print(cracked)
            print("List of failed guesses so far:")
            print(guesses)
            print("----------------------------------------\n")
        elif guess == "q":
            wins = 0
            fails = 0
            guesses = []
            cracked = []
            print("\n----------------------------------------")
            print("Stats and guesses have been cleared. \nGAME ENDED.")
            print("----------------------------------------\n")
            break
        elif wins == 9:
            print("\n----------------------------------------")
            print("Great job! You guessed ALL the secret numbers!")
            print(str(fails) + " failed attempts.")
            print(secret_nums)
            print("----------------------------------------\n")
        elif int(guess) in guesses:
            print("\n----------------------------------------")
            print("\nYou already guessed that number, try again.\n")
            print("----------------------------------------\n")
        elif int(guess) in secret_nums:
            wins += 1
            cracked.append(int(guess))
            if wins == 9:
                print("\n----------------------------------------")
                print("----------------------------------------")
                print("----------------------------------------")
                print("!!!!!!!!!!!!!!!Great job!!!!!!!!!!!!!!!!")
                print("You guessed ALL the secret numbers!")
                print(str(fails) + " failed attempts.")
                print(secret_nums)
                print("----------------------------------------")
                print("----------------------------------------")
                print("----------------------------------------\n")
            else:
                print("\n----------------------------------------")
                print("----------------------------------------")
                print("----------------------------------------")
                print("\nGreat job!!! You guessed a number!!!!!!!")
                print("You guessed " + str(wins) + "/9 numbers!" )
                print(str(fails) + " failed attempts.\n")
                print("----------------------------------------")
                print(cracked)
                print("----------------------------------------")
                print("----------------------------------------\n")
        elif float(guess) % 1 != 0:
            print("\n----------------------------------------")
            print("\nMust be a whole number\n")
            print("----------------------------------------\n")
        elif int(guess) > 999999999 or int(guess) < 1:
            print("\n----------------------------------------")
            print("\nMust be between 1 and 999999999.\n")
            print("----------------------------------------\n")
        elif int(guess) < 999999999 and int(guess) > 1:
            fails += 1
            print("\n----------------------------------------")
            print("----------------------------------------")
            print("\nI'm sorry, that is not one of the secret numbers.")
            print("You guessed " + str(wins) + "/9 numbers!" )
            print(str(fails) + " failed attempts.\n")
            print("----------------------------------------")
            print("----------------------------------------\n")
            guesses.append(int(guess))
        else:
            print("\n----------------------------------------")
            print("\nError, Must be a valid number. Try again.\n")
            print("----------------------------------------\n")
    except(ValueError):
        print("\n----------------------------------------")
        print("\nError, Must be a valid number. Try again.\n")
        print("----------------------------------------\n")

#5. Multiply all the numbers in the list [8, 19, 148, 4] will all the numbers in the list [9, 1, 33, 83], and append
#   each result to a third list.

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
product = []

for i in list1:
    for j in list2:
        product.append(i * j)

print(product)
