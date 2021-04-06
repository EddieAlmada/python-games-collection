# -*- coding: utf-8 -*-
"""
Project #2

10/11/2020
"""
C = True
print("The game has started")
Word = input("Player 1 enter your word: ")
Game = []
gameOver = False
correct = []
G = []
d = -1
w = 0

while(C == True):
    Verification = input("This is the word you entered: " + Word + ", is it correct?[Y/N]")
    if Verification == "Y" or Verification == "y":
        for i in range(len(Word)):
            Game.append(Word[i])
            correct.append(" ")
            # G.append(" ")
            C = False
    else:
        Word = input("Player 1 enter your word: ")

print(chr(27) + "[2J")

print("The lenght of the word is:", len(Word))
print("   ______")
print("  |      |")
print("  |  ")
print("  |  ")
print("  |  ")
print(" _|____________")

    

while (gameOver == False):
    e = 0
    print("Tarjet word:", correct)
    print("Mistakes made:", G)
    guess = input("Player 2, please entre a guess letter:")
    for i in range(len(Word)): 
        if guess == Game[i]:
            correct[i] = guess
            e += 1
            w +=1
            
    if w == len(Word):
        print("Congratulations you have won!")
        gameOver = True
         
    if e == 0:
        d += 1
        G.append(guess)
        if d == 0:
            print("   ______")
            print("  |      |")
            print("  |      O")
            print("  |    ")
            print("  |    ")
            print(" _|____________")
        if d == 1:
            print("   ______")
            print("  |      |")
            print("  |      O")
            print("  |      | ")
            print("  |       ")
            print(" _|____________")
        if d == 2:
            print("   ______")
            print("  |      |")
            print("  |      O")
            print("  |     /| ")
            print("  |      ")
            print(" _|____________")
        if d == 3:
            print("   ______")
            print("  |      |")
            print("  |      O")
            print("  |     /|\ ")
            print("  |      ")
            print(" _|____________")
        if d == 4:
            print("   ______")
            print("  |      |")
            print("  |      O")
            print("  |     /|\ ")
            print("  |      / ")
            print(" _|____________")
        if d == 5:
            print("   ______")
            print("  |      |")
            print("  |      O")
            print("  |     /|\ ")
            print("  |      /\ ")
            print(" _|____________")
            print("You've lost the game, GAME OVER!")
            gameOver = True
print(Game)



