import os, random
#import sklearn
import numpy as np
from math import inf as infinity

def  minimax(board, depth, Player):

	if player == "x":
		best = [-1, -1, -infinity]
	else:
		best = [-1, -1, +infinity]




def printBoard():
    for i in range (3):
        print ("  - "*3)
        for j in range (3):
            print ("|", end = " ")
            print (board[i][j], end = " ")
        print ("|")
    print ("  - "*3)

def setboard():
    b = []
    for i in range (3):
        b.append([".", ".", "."])
    return b

def checkWin(board):
    #checking rows
    for i in range (3):
        s = board [i][0] + board [i][1] + board [i][2]
        if s == "o"*3 or s == "x"*3:
            return True

    #checking columns
    for i in range (3):
        s = board [0][i] + board [1][i] + board [2][i]
        if s == "o"*3 or s == "x"*3:
            return True

    #checking horizontals
    s=board [0][0] + board [1][1] + board [2][2]
    if s == "o"*3 or s == "x"*3:
        return True
    s=board [0][2] + board [1][1] + board [2][0]
    if s == "o"*3 or s == "x"*3:
        return True

    #else return false
    return False

def askForInput():
    row = input("Enter Row: ")
    col = input("Enter Col: ")

    while (int(row) > 2 or int(col) > 2):
    	print("\nIndex out of range. Please try again.\n")
    	row = input("Enter Row: ")
    	col = input("Enter Col: ")
    board[int(row)][int(col)] = player
    moveList[row+col] = player

def think():
    k = random.choice(list(moveList.keys()))
    p = moveList.get(k)
    while p!= "":
        k = random.choice(list(moveList.keys()))
        p = moveList.get(k)

    m = [int(k[0]),int(k[1])]
    board[m[0]][m[1]] = player
    moveList[k] = player


board = setboard()
moveList = {
            "00":"",
            "01":"",
            "02":"",
            "10":"",
            "11":"",
            "12":"",
            "20":"",
            "21":"",
            "22":""
            }

win = False
moves = 0
players = ["o","x"]
winner = ""

os.system("clear")
printBoard()

output = open("data.csv", "a+")

while not (win or moves==9):
    player = players[moves%2]
    
    if player == "o":
        think()
    else:
        think()

    os.system("clear")
    printBoard()

    win = checkWin(board)
    if win == True:
        print (player," won")
        winner = player

    moves+=1
    if moves == 9:
        winner = "d"
    
    board_string = ""
    for i in range (3):
        for j in range (3):
             board_string += board[i][j] + ","

    output.write(str(moves)+","+ board_string +winner+"\n")


