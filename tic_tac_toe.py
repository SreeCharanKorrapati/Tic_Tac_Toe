#multiplayer and singleplayer
import random
board = [" - "
,
" - "
,
" - "
,
" - "
,
" - "
,
" - "
,
" - "
,
" - "
,
" - "]
currentPlayer =
" X "
winner = None
gameRunning = True
#printing the game board
def printBoard(board):
print(board[0] + " | " + board[1] + " | " + board[2])
print("---------------")
print(board[3] + " | " + board[4] + " | " + board[5])
print("---------------")
print(board[6] + " | " + board[7] + " | " + board[8])
THE CODE:
#take player input
def playerInput(board):
inp = int(input("\nEnter a number between 1-9:"))
if inp >= 1 and inp <= 9 and board[inp-1] ==
" - ":
board[inp-1] = currentPlayer
else:
print("\n---- Enter a valid Number ----\n")
inp = int(input("\nEnter a number between 1-9:"))
if inp >= 1 and inp <= 9 and board[inp-1] ==
" - ":
board[inp-1] = currentPlayer
#check for win or tie
def checkHorizontal(board):
global winner
if board[0] == board[1] == board[2] and board[0] !=
" - ":
winner = board[0]
return True
elif board[3] == board[4] == board[5] and board[3] !=
" - ":
winner = board[3]
return True
elif board[6] == board[7] == board[8] and board[6] !=
" - ":
winner = board[6]
return True
def checkTie(board):
global gameRunning
global winner
if winner == None:
if " - " not in board:
printBoard(board)
print("\n---- Its's a Tie ----\n")
winner ==
" - "
gameRunning = False
def checkWin():
global gameRunning
global winner
if winner == None:
if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
printBoard(board)
print(f"\n---- The Winner is {winner} ----\n")
gameRunning = False
#switch the player
def switchPlayer():
global currentPlayer
if currentPlayer ==
" X ":
currentPlayer =
" O "
else:
currentPlayer =
" X "
#computer
def computer(board):
while currentPlayer ==
" O ":
position = random.randint(0,8)
if board[position] ==
" - ":
board[position] =
" O "
switchPlayer()
print("----1.Single player----")
print("-----2.Multiplayer-----")
n=int(input("Enter the number: "))
if n==1:
while gameRunning:
printBoard(board)
playerInput(board)
checkWin()
checkTie(board)
switchPlayer()
computer(board)
checkWin()
checkTie(board)
elif n==2:
while gameRunning:
printBoard(board)
playerInput(board)
checkWin()
checkTie(board)
switchPlayer()
else:
print("----Enter a valid Number!----")