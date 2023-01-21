import random

def hangman(word):
    # Initializing variables
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("\n")
    print("Welcome to Hangman")
    print("\n")
    print("Possible words are: ", words)
    print("\n")
    # Game Loop
    while wrong < len(stages) - 1:
        msg = "Guess a letter: "
        print("\n")
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    # Game Over
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! The word was {}.".format(word))

words = ['python', 'java', 'javascript', 'computer', 'hacker', 'painting', 'javascript']
hangman(random.choice(words))
