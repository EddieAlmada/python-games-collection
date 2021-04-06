# -*- coding: utf-8 -*-
"""
A Simple Project
10/27/2020
"""

# Board Creation 
def con4 (aField):
    for r in range (11): #0 1 2 3 4 5 6 7 8 9 10 
        if r%2 == 0: #0 2 4 6 8 10 
            newR = int(r/2) #0 1 2 3 4 5 
            for c in range (13): 
                if c%2 == 0: #0 2 4 6 8 10 12 
                    newC = int(c/2) # 0 1 2 3 4 5 6 
                    if c != 12:
                        print(aField[newC][newR],end="")
                    else:
                        print(aField[newC][newR])
                else:
                    print("|", end = "")
        else:
                print("-" * 13)
        
# Players input
Player = 1
Counter = [0, 0, 0, 0, 0, 0, 0]
Field = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],
         [" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],
         [" "," "," "," "," "," "]]
DRow = -1
Win = False
con4(Field)
while(Win == False):
    print("Players turn: ",Player)
    
    
#Assigment 11, Error handling
    try:   #This part of the code enters when the player type a string value o simply clicked enter
        MColumn = int(input("Please enter column to play: \n"))
    except:
        MColumn = 100
        print("You entered a value error")    

    try: #This part of the code enters when the player tries to place a move in a row that doesn't exists
        MColumn -= 1
        DRow = -1
        c = -1
        if Player == 1:
           if MColumn < 7 and MColumn > -1:
                if Field [MColumn][DRow] != " ":
                    DRow -= 1 * Counter [MColumn]
                    Field [MColumn][DRow] = "X"
                    Player = 2
                    Counter [MColumn] += 1
                else:
                    Field [MColumn][DRow] = "X"
                    Player = 2
                    Counter [MColumn] += 1
                    Player = 2
        else:
            if MColumn < 7 and MColumn > -1:
                if Field [MColumn][DRow] != " ":
                    DRow -= 1 * Counter [MColumn]
                    Field [MColumn][DRow] = "O"
                    Player = 1
                    Counter [MColumn] += 1
                else:
                    Field [MColumn][DRow] = "O"
                    Player = 1
                    Counter [MColumn] += 1
        for i in range(7): # 0 1 2 3 4 5 6
            for j in range(3):
                k = j + 1
                l = j + 2
                n = j + 3
                if Field [i][j] == "X" and Field [i][k] == "X" and Field [i][l] == "X" and Field [i][n] == "X" :
                    print ("Player 1 WIN")
                    Win = True
        for i in range(7):
            for j in range(3):
                k = j + 1
                l = j + 2
                n = j + 3
                if Field [i][j] == "O" and Field [i][k] == "O" and Field [i][l] == "O" and Field [i][n] == "O" :
                    print ("Player 2 WIN")
                    Win = True
        for j in range(6):
            for i in range(4):
                k = i + 1
                l = i + 2
                n = i + 3
                if Field [i][j] == "X" and Field [k][j] == "X" and Field [l][j] == "X" and Field [n][j] == "X" :
                    print ("Player 1 WIN")
                    Win = True
        for j in range(6):
            for i in range(4):
                k = i + 1
                l = i + 2
                n = i + 3
                if Field [i][j] == "O" and Field [k][j] == "O" and Field [l][j] == "O" and Field [n][j] == "O" :
                    print ("Player 2 WIN")
                    Win = True
    # X diagonal condition
        for i in range(3): # 0 1 2 3 Column
            k = i + 1 # 1 2 3 4
            l = i + 2 # 2 3 4 5
            n = i + 3 # 3 4 5 6
            if Field [i][i] == "X" and Field [k][k] == "X" and Field [l][l] == "X" and Field [n][n] == "X" :
                print ("Player 1 WIN")
                Win = True
        for i in range(2): # 0 1 2
            k = i + 1 # 1 2 3 
            l = i + 2 # 2 3 4 
            n = i + 3 # 3 4 5 
            if Field [i][i+1] == "X" and Field [k][k+1] == "X" and Field [l][l+1] == "X" and Field [n][n+1] == "X" :
                print ("Player 1 WIN")
                Win = True
        if Field [0][2] == "X" and Field [1][3] == "X" and Field [2][4] == "X" and Field [3][5] == "X" :
                print ("Player 1 WIN")
                Win = True
        for i in range(3): # 0 1 2
            k = i + 1 # 1 2 3 
            l = i + 2 # 2 3 4 
            n = i + 3 # 3 4 5 
            if Field [i+1][i] == "X" and Field [k+1][k] == "X" and Field [l+1][l] == "X" and Field [n+1][n] == "X" :
                print ("Player 1 WIN")
                Win = True
        for i in range(2): # 0 1 2
            k = i + 1 # 1 2 3 
            l = i + 2 # 2 3 4 
            n = i + 3 # 3 4 5 
            if Field [i+2][i] == "X" and Field [k+2][k] == "X" and Field [l+2][l] == "X" and Field [n+2][n] == "X" :
                print ("Player 1 WIN")
                Win = True       
        if Field [3][0] == "X" and Field [4][1] == "X" and Field [5][2] == "X" and Field [6][3] == "X" :
                print ("Player 1 WIN")
                Win = True
    # O diagonal condition
        for i in range(3): # 0 1 2 3 Column
            k = i + 1 # 1 2 3 4
            l = i + 2 # 2 3 4 5
            n = i + 3 # 3 4 5 6
            if Field [i][i] == "O" and Field [k][k] == "O" and Field [l][l] == "O" and Field [n][n] == "O" :
                print ("Player 2 WIN")
                Win = True
        for i in range(2): # 0 1 2
            k = i + 1 # 1 2 3 
            l = i + 2 # 2 3 4 
            n = i + 3 # 3 4 5 
            if Field [i][i+1] == "O" and Field [k][k+1] == "O" and Field [l][l+1] == "O" and Field [n][n+1] == "O" :
                print ("Player 2 WIN")
                Win = True
        if Field [0][2] == "O" and Field [1][3] == "O" and Field [2][4] == "O" and Field [3][5] == "O" :
                print ("Player 2 WIN")
                Win = True
        for i in range(3): # 0 1 2
            k = i + 1 # 1 2 3 
            l = i + 2 # 2 3 4 
            n = i + 3 # 3 4 5 
            if Field [i+1][i] == "O" and Field [k+1][k] == "O" and Field [l+1][l] == "O" and Field [n+1][n] == "O" :
                print ("Player 2 WIN")
                Win = True
        for i in range(2): # 0 1 2
            k = i + 1 # 1 2 3 
            l = i + 2 # 2 3 4 
            n = i + 3 # 3 4 5 
            if Field [i+2][i] == "O" and Field [k+2][k] == "O" and Field [l+2][l] == "O" and Field [n+2][n] == "O" :
                print ("Player 2 WIN")
                Win = True       
        if Field [3][0] == "O" and Field [4][1] == "O" and Field [5][2] == "O" and Field [6][3] == "O" :
                print ("Player 2 WIN")
                Win = True
    # X diagonal condition (INVERTED)
        for i in range(6,3,-1): # 6 5 4 Column
            if i == 6:
                if Field [6][0] == "X" and Field [5][1] == "X" and Field [4][2] == "X" and Field [3][3] == "X" :
                   print ("Player 1 WIN")
                   Win = True
            elif i == 5:
                if Field [5][1] == "X" and Field [4][2] == "X" and Field [3][3] == "X" and Field [2][4] == "X" :
                    print ("Player 1 WIN")
                    Win = True
            else:
                if Field [4][2] == "X" and Field [3][3] == "X" and Field [2][4] == "X" and Field [1][5] == "X" :
                    print ("Player 1 WIN")
                    Win = True
        for i in range(6,4,-1):
            if i == 6:
                if Field [6][1] == "X" and Field [5][2] == "X" and Field [4][3] == "X" and Field [3][4] == "X" :
                    print ("Player 1 WIN")
                    Win = True
            else:
                if Field [5][2] == "X" and Field [4][3] == "X" and Field [3][4] == "X" and Field [2][5] == "X" :
                    print ("Player 1 WIN")
                    Win = True            
        if Field [6][2] == "X" and Field [5][3] == "X" and Field [4][4] == "X" and Field [3][5] == "X" :
                print ("Player 1 WIN")
                Win = True
        for i in range(5,2,-1): # 5 4 3 
            if i == 5:
                if Field [5][0] == "X" and Field [4][1] == "X" and Field [3][2] == "X" and Field [2][3] == "X" :
                    print ("Player 1 WIN")
                    Win = True
            elif i == 4:
                if Field [4][1] == "X" and Field [3][2] == "X" and Field [2][3] == "X" and Field [1][4] == "X" :
                    print ("Player 1 WIN")
                    Win = True
            else:
                if Field [3][2] == "X" and Field [2][3] == "X" and Field [1][4] == "X" and Field [0][5] == "X" :
                    print ("Player 1 WIN")
                    Win = True
        for i in range(4,2,-1): # 4 3
            if i == 4:
                if Field [4][0] == "X" and Field [3][1] == "X" and Field [2][2] == "X" and Field [1][3] == "X" :
                    print ("Player 1 WIN")
                    Win = True 
            else:
                if Field [3][1] == "X" and Field [2][2] == "X" and Field [1][3] == "X" and Field [0][4] == "X" :
                    print ("Player 1 WIN")
                    Win = True      
        if Field [3][0] == "X" and Field [2][1] == "X" and Field [1][2] == "X" and Field [0][3] == "X" :
                print ("Player 1 WIN")
                Win = True     
    # O diagonal condition (INVERTED)
        for i in range(6,3,-1): # 6 5 4 Column
            if i == 6:
                if Field [6][0] == "O" and Field [5][1] == "O" and Field [4][2] == "O" and Field [3][3] == "O" :
                   print ("Player 2 WIN")
                   Win = True
            elif i == 5:
                if Field [5][1] == "O" and Field [4][2] == "O" and Field [3][3] == "O" and Field [2][4] == "O" :
                    print ("Player 2 WIN")
                    Win = True
            else:
                if Field [4][2] == "O" and Field [3][3] == "O" and Field [2][4] == "O" and Field [1][5] == "O" :
                    print ("Player 2 WIN")
                    Win = True
        for i in range(6,4,-1):
            if i == 6:
                if Field [6][1] == "O" and Field [5][2] == "O" and Field [4][3] == "O" and Field [3][4] == "O" :
                    print ("Player 2 WIN")
                    Win = True
            else:
                if Field [5][2] == "O" and Field [4][3] == "O" and Field [3][4] == "O" and Field [2][5] == "O" :
                    print ("Player 2 WIN")
                    Win = True            
        if Field [6][2] == "O" and Field [5][3] == "O" and Field [4][4] == "O" and Field [3][5] == "O" :
                print ("Player 2 WIN")
                Win = True
        for i in range(5,2,-1): # 5 4 3 
            if i == 5:
                if Field [5][0] == "O" and Field [4][1] == "O" and Field [3][2] == "O" and Field [2][3] == "O" :
                    print ("Player 2 WIN")
                    Win = True
            elif i == 4:
                if Field [4][1] == "O" and Field [3][2] == "O" and Field [2][3] == "O" and Field [1][4] == "O" :
                    print ("Player 2 WIN")
                    Win = True
            else:
                if Field [3][2] == "O" and Field [2][3] == "O" and Field [1][4] == "O" and Field [0][5] == "O" :
                    print ("Player 2 WIN")
                    Win = True
        for i in range(4,2,-1): # 4 3
            if i == 4:
                if Field [4][0] == "O" and Field [3][1] == "O" and Field [2][2] == "O" and Field [1][3] == "O" :
                    print ("Player 2 WIN")
                    Win = True 
            else:
                if Field [3][1] == "O" and Field [2][2] == "O" and Field [1][3] == "O" and Field [0][4] == "O" :
                    print ("Player 2 WIN")
                    Win = True      
        if Field [3][0] == "O" and Field [2][1] == "O" and Field [1][2] == "O" and Field [0][3] == "O" :
                print ("Player 2 WIN")
                Win = True   
            
        con4(Field)
       
    except: 
        MColumn = 100
        print('Column full')
        con4(Field)
    
      
    
  