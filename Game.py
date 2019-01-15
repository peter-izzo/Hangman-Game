import random

#create stages of the game and starts the "win" mode in false
#board consists of underscores in teh amount of lettes in the word picked

def hangman(word):
    wrong = 0
    stages = ["",
             "_________         ",
             "|                 ",
             "|        |        ",
             "|        0        ",
             "|       /|\       ",
             "|        |        ",
             "|       / \       ",
             "|                 "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

#while loop that runs as long as "wrong" is -1 of stages since stages needs to start at 1 and wrong starts at 0
#as player incorrectly guesses letters, stages increases drawing more of the stick figure
#as player guesses correctly, correctly guessed letters fill the underscores
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter(duplicate letters must be guessed twice): "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        #if there are no more blank underscores, player wins and program breaks
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    #if stickman fully drawn and no more stages available, player loses
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

#word list. Need to add more words at a later date
l = ["cat", "dog", "squirrel", "mouse", "reptar", "dinosaur", "car", "immortal", "sustenance", "hexadecimal", "mangoes"]
#randomly chooses a word from the list
i = random.choice(l)
hangman(i)
