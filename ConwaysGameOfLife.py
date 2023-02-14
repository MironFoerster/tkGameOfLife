# imports
import tkinter as tk
import numpy as np
import copy as cp


# vars
main = tk.Tk()
imw = tk.PhotoImage(file="white.gif")
imb = tk.PhotoImage(file="black.gif")
imageDict = {0: imb, 1: imw}
simulRunning = 0
simulRunningSwap = 1
stayAliveRule = (2, 3)
getBornRule = (3,)
generCount = 0

# Schieberegler Variablen
runDelay = tk.IntVar()
runDelay.set(1000)
setCellSize = tk.IntVar()
setCellSize.set(1)
setGridSize = tk.IntVar()
setGridSize.set(10)


# functions
def getStayAliveRule():
    global stayAliveRule
    stayAliveRule = stayAliveList.curselection()
    stayAliveLabel["text"] = "...stay alive"+str(stayAliveRule)
    

def getGetBornRule():
    global getBornRule
    getBornRule = getBornList.curselection()
    getBornLabel["text"] = "...get born"+str(getBornRule)


def cellStateSwitch(i, j):
    if cellStates[i][j] == 0:
        change = 1
    else:
        change = -1
        
    cellStates[i][j] += change
    labelList[i][j]["image"] = imageDict[cellStates[i][j]]
    
    for x in -1, 0, 1:
        for y in -1, 0, 1:
            
            if x == 0 and y == 0:
                continue
            else:
                if not (i+x < 0 or j+y < 0):
                    try:
                        cellAliveNeighbours[i+x][j+y] += change
                    except:
                        pass


def update():
    global generCount
    cellStatesCopy = cp.deepcopy(cellStates)
    cellAliveNeighboursCopy = cp.deepcopy(cellAliveNeighbours)
    
    for i in range(gridSize):
        for j in range(gridSize):
                        
            if cellStatesCopy[i][j] == 1 and not (cellAliveNeighboursCopy[i][j] in rules[0]):  # living, that dont keep living
                cellStateSwitch(i, j)

            elif cellStates[i][j] == 0 and cellAliveNeighboursCopy[i][j] in rules[1]:  # death, that will be born
                cellStateSwitch(i, j)
                
    if not (cellStatesCopy == cellStates).all():
        generCount += 1
        generCountLabel["text"] = "Generation Count:"+str(generCount)


def simulCreateNew():
    global labelList, cellStates, cellAliveNeighbours, cellSize, gridSize, rules
    
    cellSize = setCellSize.get()
    gridSize = setGridSize.get()
    rules = (stayAliveRule, getBornRule)
    
    for i in labelList:
        for j in i:
            j.destroy()

    arr = np.zeros((gridSize, gridSize), dtype=int)
    labelList = arr.tolist()

    for i in range(gridSize):
        for j in range(gridSize):
            
            labelList[i][j] = tk.Label(simulGridFrame, image=imb, width=cellSize, height=cellSize)
            labelList[i][j].grid(row=i, column=j)
            labelList[i][j].bind("<Button 1>", lambda event, i=i, j=j: cellStateSwitch(i, j))
            
    cellStates = np.zeros((gridSize, gridSize), dtype=int)
    cellAliveNeighbours = np.zeros((gridSize, gridSize), dtype=int)
    
    
def simulRun():
    if simulRunning:
        update()
        main.after(runDelay.get(), simulRun)
        
        
def simulPlayPause():
    global simulRunning, simulRunningSwap
    simulRunning, simulRunningSwap = simulRunningSwap, simulRunning
    
    if simulRunning == 1:
        simulPlayPauseButton["text"] = "Pause"
    else:
        simulPlayPauseButton["text"] = "Play"
    simulRun()
    
    
def generCountReset():
    global generCount
    generCount = 0
    generCountLabel["text"] = "Generation count:"+str(generCount)

    
def close():
    main.destroy()


# GUI
"""SETTING-FRAME"""
settingFrame = tk.Frame(main)
settingFrame.grid(row=0, column=0)

# RULES_SETTING-FRAME
rulesSettingFrame = tk.Frame(settingFrame)
rulesSettingFrame.grid(row=0, column=0)

rulesIntroLabel = tk.Label(rulesSettingFrame, text="At which neighbourcount a cell is to...")
rulesIntroLabel.grid(row=0, column=0, columnspan=2)


# STAY_ALIVE_RULES-FRAME
stayAliveRulesFrame = tk.Frame(rulesSettingFrame)
stayAliveRulesFrame.grid(row=1, column=0)

# S_A_R_F-Widgets
stayAliveLabel = tk.Label(stayAliveRulesFrame, text="...stay alive"+str(stayAliveRule))
stayAliveLabel.grid(row=0, column=0)

stayAliveList = tk.Listbox(stayAliveRulesFrame, height=0, selectmode="multiple")
for i in range(9):
    stayAliveList.insert("end", i)
stayAliveList.grid(row=1, column=0)

setStayAliveButton = tk.Button(stayAliveRulesFrame, text="Ok", command=getStayAliveRule)
setStayAliveButton.grid(row=2, column=0)


# GET_BORN_RULES-FRAME
getBornRulesFrame = tk.Frame(rulesSettingFrame)
getBornRulesFrame.grid(row=1, column=1)

# G_B_R_F-Widgets
getBornLabel = tk.Label(getBornRulesFrame, text="...get born"+str(getBornRule))
getBornLabel.grid(row=0, column=0)

getBornList = tk.Listbox(getBornRulesFrame, height=0, selectmode="multiple")
for i in range(9):
    getBornList.insert("end", i)
getBornList.grid(row=1, column=0)

setGetBornButton = tk.Button(getBornRulesFrame, text="Ok", command=getGetBornRule)
setGetBornButton.grid(row=2, column=0)


# SIZE_SETTING-FRAME
sizeSettingFrame = tk.Frame(settingFrame)
sizeSettingFrame.grid(row=0, column=1)

# S_S_F-Widgets
gridSizeScale = tk.Scale(sizeSettingFrame, variable=setGridSize, label="Grid size (cells):", width=10, length=100, orient="horizontal", from_=10, to=150, resolution=10)
gridSizeScale.grid(row=0, column=0)

cellSizeScale = tk.Scale(sizeSettingFrame, variable=setCellSize, label="Cell size (pixels):", width=10, length=100, orient="horizontal", from_=1, to=10, resolution=1)
cellSizeScale.grid(row=1, column=0)


# Trennung
divider = tk.Label(main, text=80*"-")
divider.grid(row=1, column=0)

"""SIMUL-FRAME"""
simulFrame = tk.Frame(main)
simulFrame.grid(row=2, column=0)


# SIMUL_GRID-FRAME
simulGridFrame = tk.Frame(simulFrame)
simulGridFrame.grid(row=0, column=0)

# S_G_F-Widgets
arr = np.zeros((1, 1), dtype=int)
labelList = arr.tolist()
labelList[0][0] = tk.Label(simulGridFrame, text="<EmptySimulation>")
labelList[0][0].grid(row=0, column=0)


# SIMUL_CONTROL-FRAME
simulControlFrame = tk.Frame(simulFrame)
simulControlFrame.grid(row=0, column=1)

# S_C_F-Widgets
simulCreateNewButton = tk.Button(simulControlFrame, text="Create new simulation", command=simulCreateNew)
simulCreateNewButton.grid(row=0, column=0, columnspan=2)

updateButton = tk.Button(simulControlFrame, text="Update one generation", command=update)
updateButton.grid(row=3, column=1)

simulRunDelayScale = tk.Scale(simulControlFrame, label="Run delay (ms):", variable=runDelay, width="10", length="100", orient="horizontal", from_=10, to=1000, resolution=10)
simulRunDelayScale.grid(row=2, column=0)

simulPlayPauseButton = tk.Button(simulControlFrame, text="Play", command=simulPlayPause)
simulPlayPauseButton.grid(row=3, column=0)

generCountLabel = tk.Label(simulControlFrame, text="Generation count:"+str(generCount))
generCountLabel.grid(row=4, column=0, columnspan=2)

generCountResetButton = tk.Button(simulControlFrame, text="Reset generation count", command=generCountReset)
generCountResetButton.grid(row=5, column=0, columnspan=2)

# Close
closeButton = tk.Button(main, text="Close", command=close)
closeButton.grid(row=4, column=0)

main.mainloop()
