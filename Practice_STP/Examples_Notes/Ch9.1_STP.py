# https://www.theselftaughtprogrammer.io
# Cory Althoff - The Self-taught Programmer
# Chapter 9 pg 131 - Bringing It All Together - Hangman Game
# hashtagallison - Practice 2019-04-14
#-------------------------------------------

def hangman(word):
    wrong = 0
    stages = ["",
              "_________         ",
              "|                 ",
              "|         |       ",
              "|         O       ",
              "|        /|\      ",
              "|        / \      ",
              "|                 ",
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print("\n".join(stages[0: e]))
        if "__" not in KeyboardInterrupt:
            print("You win!")
            print(" ".join(board))
            win = True
            break
        if not win:
            print("\n".join(stages[0:wrong]))
            print("You lose! It was {}.".format(word))

hangman("cat")
