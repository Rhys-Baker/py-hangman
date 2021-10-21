# -*- coding: utf-8 -*-
import random
import os
from hangmanData import printHangman
from newWordList import wordlist

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#define word list

misses = 6
difficulty = 1


def drawSplashScreen():
    print("""
    ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
    ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
    ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
    ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
    ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
                                                  © Rhys Baker 2021
    """)


def selectDifficulty():
    print("""
    ╔═════════════════╗
    ║Select Difficulty║
    ║                 ║
    ║   [1] easy      ║
    ║   [2] medium    ║
    ║   [3] hard      ║
    ║                 ║
    ╚═════════════════╝

    """)
    global difficulty
    difficulty = int(input("> "))

def selectWord():
        #select a random word from the wordlist and set up variables
    global selectedWord
    global selectedList
    global wrongLetters
    selectedWord = wordlist[random.randrange(len(wordlist))]
    selectedList = list(selectedWord)
    wrongLetters = []

    global guessedWord
    guessedWord = []

    for x in range(len(selectedList)):
        guessedWord.append("")



def printUnderscores():
    underscores = ""
    for x in range(len(selectedWord)):
        if selectedList[x] != "":
            underscores += "_ "
        else:
            underscores += selectedWord[x] + " "
    print("                            " + underscores)



def guess():
    guess = input("> ")
    if guess in selectedList:
        for x in range(len(selectedList)):
            if selectedList[x] == guess:
                guessedWord[x] = guess
                selectedList[x] = ""
    else:
        wrongLetters.append(guess)



def printWrongLetters():
    print("Wrong Letters:")
    print("              " + ", ".join(wrongLetters))



def winLose():
    if guessedWord == list(selectedWord):
        print("win")
        return 1
    elif len(wrongLetters) >= misses / difficulty:
        print("lose")
        return 2
    else:
        return 0




clear()
drawSplashScreen()
selectDifficulty()

selectWord()
while winLose() == 0:
    clear()
    printHangman(len(wrongLetters * difficulty))
    print("")
    printUnderscores()
    print("")
    printWrongLetters()
    guess()

clear()
if winLose() == 1:
    printHangman(7)
else:
    printHangman(6)
printUnderscores()



