"""
Battleship Project
Name:Pravallika
Roll No:
"""
from random import randint
import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["cellsize"]=50
    data["numships"]=5
    data["Computerboard"]=[[]]
    data["Userboard"]=[[]]
    data["Computerboard"]=emptyGrid(data["rows"],data["cols"])
    data["Userboard"]=emptyGrid(data["rows"],data["cols"])
    data["Computerboard"]=addShips(data["Computerboard"],data["numships"])
    data["TemporaryShip"]=[]
    data["noofshipsadded"]=0
    return



'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["Userboard"],True)
    drawGrid(data,compCanvas,data["Computerboard"],True)
    drawShip(data,userCanvas,data["TemporaryShip"])

    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    


    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid=[]
    for i in range(rows):
        l1 = []
        for j in range(cols):
            l1.append(EMPTY_UNCLICKED)
        grid.append(l1)
    return grid





'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
        rows=randint(1,8)
        cols=randint(1,8)
        fordirection=randint(0,1)
        if(fordirection==1):
            a=[]
            for i in range(rows-1,rows+2,1):
                a.append([i,cols])
        else:
            a=[]
            for i in range(cols-1,cols+2,1):
                a.append([rows,i])
        return a



'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
     for i in range(len(ship)):
        if grid[ship[i][0]][ship[i][1]]!=EMPTY_UNCLICKED:
             return False
     return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0
    while count<numShips:
        ship=createShip()
        if checkShip(grid,ship)==True:
            for i in range(len(ship)):
                grid[ship[i][0]][ship[i][1]]=SHIP_UNCLICKED
            count +=1
    return grid

'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(0,data["rows"],1):
        for j in range(0,data["cols"],1):
                if(grid[i][j]==SHIP_UNCLICKED):
                    boardcolour='yellow'
                else:
                    boardcolour='blue'
                x1=data["cellsize"]*j
                y1=data["cellsize"]*i
                x2=x1+data["cellsize"]
                y2=y1+data["cellsize"]
                canvas.create_rectangle(x1,y1,x2,y2,outline='black',fill=boardcolour)
    return

### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    col=ship[0][1]
    for i in range(len(ship)):
        if(ship[i][1]!=col):
            return False 
    row=[]
    for i in range(len(ship)):
        row.append(ship[i][0])
    row.sort()
    for i in range(len(row)-1):
        if 1+row[i]!=row[i+1]:
            return False
    return True
  
    



'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    return



'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    return




'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    
        
        return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    return

    


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    


    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    for i in range(row+1):
        for j in range(col+1):
            if(board[i][j]==SHIP_UNCLICKED):
                board[i][j]=SHIP_CLICKED
            if(board[i][j]==EMPTY_UNCLICKED):
                board[i][j]=EMPTY_CLICKED
    return
    

 


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
  #  test.test()
    test.testIsVertical()   
    # Finally, run the simulation to test it manually ##
   # runSimulation(500, 500)
