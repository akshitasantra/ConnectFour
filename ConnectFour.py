print("Welcome to Connect Four!")
rows, cols = (6, 7)
board = [[" " for i in range(cols)] for j in range(rows)]
def printBoard(board):
rows = ['a', 'b', 'c', 'd', 'e', 'f']
top = '
1
2 3 4 5 6
7
'
row = [[n] for n in range(0, 7)]
row[0][0] = 'f | '
row[1][0] = 'e | '
row[2][0] = 'd | '
row[3][0] = 'c | '
row[4][0] = 'b | '
row[5][0] = 'a | '
print('')
print(' ' + '-' * (len(top) - 3))
for j in range(0, len(rows)):
for i in range(1, 8):
row[j][0] = row[j][0] + str(board[j][i - 1]) + ' | '
print(row[j][0])
print(' ' + '-' * ((len(row[j][0]) - 3)))
print(top)
print('')
def validMove(num):
return num >= 1 or num <= 7 or not str(num).isnumeric()
def addMove(col, letter):
col-=1
if board[0][col] == " ":
for i in range(5, -1, -1):
if board[i][col] == " ":
board[i][col] = letter
break
def winsFor(team):
# check horizontal wins
for i in range(7 - 3):
for j in range(6):
if board[j][i] == team and board[j][i+1] == team and board[j][i+2] == team and
board[j][i+3] == team:
return True
# check for vertical wins
for c in range(7):
for r in range(3):
if board[r][c] == team and board[r+1][c] == team and board[r+2][c] == team and
board[r+3][c] == team:
return True
# check for diagonal right wins
for c in range(7-3):
for r in range(6-3):
if board[r][c] == team and board[r+1][c+1] == team and board[r+2][c+2] == team
and board[r+3][c+3] == team:
return True
# check for diagonal left wins
for c in range(7-4, 7):
for r in range(6-3):
if board[r][c] == team and board[r+1][c-1] == team and board[r+2][c-2] == team and
board[r+3][c-3] == team:
return True
while True:
printBoard(board)
print('To play: enter an integer between 1 to 7 ' + \
'corresponding to each column in the board. ' + \
'Whoever stacks 4 pieces next to each other, ' + \
'either horizontally, vertically or diagonally wins.')
Xinput = int(input("X's choice: "))
print()
while not validMove(Xinput):
print("Not a valid move, please try again")
Xinput = int(input("X's choice: "))
print()
addMove(Xinput, "X")
if winsFor("X"):
print("X wins -- Congratulations!")
printBoard(board)
break
else:
printBoard(board)
Oinput = int(input("O's choice: "))
print()
while not validMove(Oinput):
print("Not a valid move, please try again")
Oinput = int(input("O's choice: "))
print()
addMove(Oinput, "O")
if winsFor("O"):
print("O wins -- Congratulations!")
printBoard(board)
break