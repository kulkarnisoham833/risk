
import random

# RISK

# 5x5 array of territories marked A through Y
# Game is played with 2 players: you (0) against the computer (1)
# each player receives 30 troops and places 1 on empty territories until all territories are claimed
# Create the game loop: iterate until the game is won.
#  https://www.wikihow.com/Play-Risk

# Only one person should have troops on a territory at a time: use color to express this, not a pair where one is zero


def diceRoll(n):
  ret = []
  for i in range(n):
    ret.append(random.randint(1,4))
  return ret

def initBoard(w = 5, h = 5):
  return [[[0, 0] for x in range(w)] for y in range(h)]
  
def printBoard(b):
  print("\n" + " "*5, end="")
  for i in range(len(b[0])):
    tmp = str(i)

    print(tmp, end=" "*(9-len(tmp)))
  print("\n")
  for i in range(len(b)):
    tmp = str(i) + ":"
    print(tmp, end=" "*(5-len(tmp))) #always 5 chars

    for j in range(len(b[i])):
      p = str(b[i][j][0]) + "," + str(b[i][j][1])
      print(p, end=" "*(4+(5-len(p))))
    print("\n")

def placeArmyPrompt(armies, playerNum, b):
  # Show the board with coords
  # Tell how many armies they can place. Ask for how many and where to place with a confirmation step until they place all their armies
  print(f"You are player {playerNum+1}.")
  print(f"You may place {armies} arm{'y' if armies == 1 else 'ies'} on this turn.")
  while armies > 0:
    printBoard(b)
    try:
      tmp = int(input(f"You currently have {armies} arm{'y' if armies == 1 else 'ies'} remaining. How many will you place? "))
      if tmp <= 0 or tmp > armies:
        raise ValueError("Too many or too few armies requested.")
      a = tmp
      armies -= a
    except:
      print("Invalid input.")
      continue

    try:
      r = int(input(f"Enter row number (0 to {len(b) - 1}): "))
      c = int(input(f"Enter col number (0 to {len(b[0]) - 1}): "))
      if b[r][c][int(not playerNum)] > 0:
        raise ValueError()
      # make sure inputs are valid
      b[r]
      b[0][c]
    except:
      print("Invalid input / You can only place armies in empty territories.")
      continue
    
    placeArmies(a, r, c, playerNum, b) # Inputs are valid
    printBoard(b)

def placeArmies(armies, row, col, playerNum, b):
  
  b[row][col][playerNum] += armies

  

Board = initBoard()

# 1. Who goes first?
currPlayer = -1
tmp = diceRoll(2)
while tmp[0] == tmp[1]:
  tmp = diceRoll(2)
currPlayer = 0 if tmp[0] > tmp[1] else 1 # False is the first player, True is the second player

tmp = 40
while tmp > 0: # Place all the troops
  placeArmyPrompt(1, currPlayer, Board)
  currPlayer = not currPlayer
  placeArmyPrompt(1, currPlayer, Board)
  tmp -= 1


