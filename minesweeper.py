#Kevin Zhang
#101147715

import random

GRID_SIZE = 10

def placeMines():
    '''This function creates a 2D list with randomly placed mines
    marked with 'x' '''

    grid = []
    for _ in range(GRID_SIZE):
        row = []
        for _ in range(GRID_SIZE): #fills row 
            mine = random.randint(1,10)#10% chance
            if mine == 1: 
                row.append("x")
            else:
                row.append("")
        grid.append(row)#add row to grid
    return grid

def makeBoard():
    '''This function creates the gameboard for the player and fills it 
    with '#' to represent a tile'''

    gameBoard = []
    for _ in range(GRID_SIZE):
        row = []
        for _ in range(GRID_SIZE):
            row.append("#")
        gameBoard.append(row)
    return gameBoard

def showBoard(gameBoard):
    '''This function displays the gameboard to the player'''

    #create the top row of numbers
    columnLabels = " |"
    upperLine = "--"
    for i in range(len(gameBoard)):
        columnLabels+=str(i)
        upperLine+="-"
    print(columnLabels)
    print(upperLine)

    #display the board
    for i in range(len(gameBoard)):
        showRow = str(i) + "|"
        for j in range(len(gameBoard)):
            showRow+=gameBoard[i][j]
        print(showRow)

def countHiddenCells(gameBoard):
    '''This function counts all entries in the gameboard marked
    with a '#' '''

    numOfHiddenCells = 0
    for e in gameBoard:
        for f in e:
            if f == "#":
                numOfHiddenCells+=1
    return numOfHiddenCells

def countAllMines(grid):
    '''This function counts all entries marked with 'x' in the grid'''

    numMines = 0
    for e in grid:
        for f in e:
            if f == "x":
                numMines+=1
    return numMines

def isMineAt(grid,row,col):
    '''This function determines if a specific entry contains a mine'''

    if grid[row][col] == "x":
        return True
    return False

def countAdjacentMines(grid,row,col):
    '''This function counts all the mines adjacent to a specific
    entry'''

    adjacentMines = 0

    #ensures the program does not go out of index
    rowStart = -1
    rowEnd = 2
    colStart = -1
    colEnd = 2
    if row == 0:
        rowStart = 0
    elif row == GRID_SIZE-1:
        rowEnd = 1
    if col == 0:
        colStart = 0
    elif col == GRID_SIZE-1:
        colEnd = 1

    for i in range(rowStart,rowEnd):
        for j in range(colStart,colEnd):
            if grid[row+i][col+j]:
                adjacentMines+=1
    return adjacentMines

def reveal(gameBoard,grid,row,col):
    '''This recursive function reveals all tiles where there are no adjacent 
    mines until it reveals a tile with adjacent mines.'''

    if int(row) < 0 or int(row) > GRID_SIZE-1 or \
        int(col) < 0 or int(col) > GRID_SIZE-1: #input is off the grid
        return
    if gameBoard[row][col] == " ": #tile has already been checked
        return

    mines = countAdjacentMines(grid,row,col)
    if mines > 0: #has adjacent mines
        gameBoard[row][col] = str(mines)
    else: #no adjacent mines
        gameBoard[row][col] = " "
        reveal(gameBoard,grid,row,col-1)
        reveal(gameBoard,grid,row,col+1)
        reveal(gameBoard,grid,row-1,col)
        reveal(gameBoard,grid,row+1,col)

def revealAllMines(gameBoard,grid):
    '''This function reveals all tiles in the grid with an 'x'.
    It then replaces the corrisponding tile in the gameboard with 'X' '''

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "x":
                gameBoard[i][j] = "X"

def validMove(move):
    '''This function ensure that the player enters a valid input'''

    if len(move) < 3: #input is too small
        return False
    if move.count(",") != 1: #input does not contain only one ','
        return False
    row,col = move.split(",")
    if not(row.isnumeric() and col.isnumeric): #input is not a number
        return False
    if int(row) < 0 or int(row) > GRID_SIZE-1 or \
        int(col) < 0 or int(col) > GRID_SIZE-1: #too big or too small for grid
        return False
    else:
        return True

def main():
    '''This is the main game function which runs the game'''

    #initialize game
    grid = placeMines()
    gameBoard = makeBoard()
    gameOver = False

    while not gameOver:
        showBoard(gameBoard)

        #get and manage input
        move = input("Select a cell (row,col) > ")
        while not validMove(move):
            move = input("Select a cell (row,col) > ")
        row,col = move.split(",")
        row = int(row)
        col = int(col)

        #checks if the user hit a mine
        if isMineAt(grid,row,col):
            gameOver = True
            revealAllMines(gameBoard,grid)
            showBoard(gameBoard)
            print("GAME OVER!")    
        else:
            reveal(gameBoard,grid,row,col)
        
        #checks if the user won the game
        if countHiddenCells(gameBoard) == countAllMines(grid) or countAllMines == 0:
            showBoard(gameBoard)
            gameOver = True
            print("You Win!!")

main()