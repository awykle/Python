# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 7, Q4 pg 114 - Challenges
# hashtagallison - Practice 2019-04-10
#-------------------------------------------

#-------------------------------------------
# The program was created to resolve prompt #4 in chapter 7 challenges.
# Used syntax examples from chapters 3-7 as reference.
# Did not access "answer key" for challenge until after resolved.
#-------------------------------------------

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
    guess = input("\nGuess a secret numbers between 1 and 999999999: ")
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
            print("Secret numbers discovered so far:")
            print(cracked)
            print("\n" + str(fails) + " failed attempts.\n")
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
                print("!!!!!!!!!!!!!!!GREAT JOB!!!!!!!!!!!!!!!!")
                print("You guessed ALL the secret numbers!")
                print(str(fails) + " failed attempts.")
                print("The secret code has been revealed:")
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
                print(cracked)
                print("----------------------------------------")                
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



