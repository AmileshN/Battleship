from random import randint 
print("Welcome to Battleship")

board=[]
for x in range(0,5):
  board.append(["O"]*5)

def printboard(board):
  for x in board:
    print (" ".join(x))

def randomrow():
  return randint(0,len(board)-1)
def randomcol():
  return randint(0,len(board)-1)
shiprow=randomrow()
shipcol=randomcol()
turn=0


for x in range(0,4):
  printboard(board)
  guessrow=int(input("Guess what row the ship is in "))
  guesscol=int((input("Guess what column the ship is in ")))

  if guesscol==shipcol and guessrow==shiprow:
    print("hit you win")
    break
  else:
    if guessrow not in range(5) or guesscol not in range(5):
      print("Not in range idiot")
    elif board[guessrow][guesscol]=="X":
      print("already guessed")
    else:
      print("miss")
      board[guessrow][guesscol]="X"
    turn=turn+1
    printboard(board)

