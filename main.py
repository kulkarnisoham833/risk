
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
    ret.append(random.randint(1,6))
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
      a = int(input(f"You currently have {armies} arm{'y' if armies == 1 else 'ies'} remaining. How many will you place? "))
      if a <= 0 or a > armies:
        raise ValueError("Too many or too few armies requested.")
      r = int(input(f"Enter row number (0 to {len(b) - 1}): "))
      c = int(input(f"Enter col number (0 to {len(b[0]) - 1}): "))
      if b[r][c][int(not playerNum)] > 0:
        raise ValueError()
      # make sure inputs are valid
      b[r]
      b[0][c]
      armies -= a
    except:
      print("Invalid input / You cannot place armies in opponent territories.")
      continue
    
    placeArmies(a, r, c, playerNum, b) # Inputs are valid
    printBoard(b)

def placeArmies(armies, row, col, playerNum, b):
  b[row][col][playerNum] += armies

def countTerritories(playerNum, b):
  c = 0
  for i in range(len(b)):
    for j in range(len(b[0])):
      if b[i][j][playerNum] > 0: #Acc to PlaceArmyPrompt, b[i][j][not playerNum] shold be zero
        c += 1
  return c
  
def attack(sourcePlayer, b):
  printBoard(b)
  while True:
    try:
      print("Where will you attack from?")
      r = int(input(f"Enter row number (0 to {len(b) - 1}): "))
      c = int(input(f"Enter col number (0 to {len(b[0]) - 1}): "))
      if b[r][c][not sourcePlayer] > 0 or b[r][c][sourcePlayer] <= 1:
        raise ValueError()
      # make sure inputs are valid
      b[r]
      b[0][c]
      break
    except:
      print("Invalid input. You cannot attack from opponent territories or territories with less than or equal to one army.")
      continue
  while True:
    try:
      print("What will you attack? It is at most one unit away from your source attack in either or both directions.")
      rA = int(input(f"Enter row number (0 to {len(b) - 1}): "))
      cA = int(input(f"Enter col number (0 to {len(b[0]) - 1}): "))
      
      if b[rA][cA][sourcePlayer] > 0 or not(abs(rA - r) <= 1 and abs(cA - c) <= 1):
        raise ValueError()
      # make sure inputs are valid
      b[rA]
      b[0][cA]
      break
    except:
      print("Invalid input. You can't attack yourself.")
      continue
    
  while True: # How many armies will you take
    try:
      upto = min(b[r][c][sourcePlayer] - 1, 3)
      armiesMoving = int(input(f"You may take up to {upto} armies. How many will you take? "))
      if armiesMoving > upto:
        raise ValueError()
      break
    except:
      print("Invalid input. Enter the right number of armies.")
  b[r][c][sourcePlayer] -= armiesMoving
  b[rA][cA][sourcePlayer] += armiesMoving
  print(f"Player {sourcePlayer + 1} is invading player {int(not sourcePlayer) + 1} with {armiesMoving} troops at row {rA} col {rB}!")
  printBoard(b) #TODO: get it to bold the cell in question
  
  #Run the attack
  red = sorted(diceRoll(armiesMoving)) #An array of randints 1 to 6
  defenders = b[rA][cA][not sourcePlayer]
  white = sorted(diceRoll(max(defenders, 2)))
  while min(len(white),len(red)) > 0:
    if white[i] >= red[i]: # red loses
      red.pop(i)
      stat = input(f"Player {sourcePlayer} loses. There are now {len(red)} attackers and {len(white)} defenders. Keep attacking (Y/N)? ")
      if stat == "N": break
    else:
      white.pop(i)
      stat = input(f"Player {not sourcePlayer} loses. There are now {len(red)} attackers and {len(white)} defenders. Keep attacking (Y/N)? ")
      if stat == "N": break
  if len(white) <= 0:
    

  


Board = initBoard()

# 1. Who goes first?
currPlayer = -1
tmp = diceRoll(2)
while tmp[0] == tmp[1]:
  tmp = diceRoll(2)
currPlayer = 0 if tmp[0] > tmp[1] else 1 # False is the first player, True is the second player

tmp = 1
while tmp > 0: # Place all the troops
  placeArmyPrompt(1, currPlayer, Board)
  currPlayer = not currPlayer
  placeArmyPrompt(1, currPlayer, Board)
  tmp -= 1
  currPlayer = not currPlayer

gameWin = False
# Turns
while not gameWin:
  # for every 3 territories you control, you gain one troop
  # TODO: Continent support. Also secret mission support
  placeArmyPrompt(max(countTerritories(currPlayer, Board) // 3, 3), currPlayer, Board)
  attack(currPlayer, Board)
  currPlayer = not currPlayer

  



