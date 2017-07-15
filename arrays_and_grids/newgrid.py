# connor bailes

from grid import Grid
import random


def loadGrid():

    rows = int(raw_input("How many rows? "))
    columns = int(raw_input("How many colums? "))
    
    newGrid = Grid(rows, columns, random.randint(1, 10))
    
    

    for i in xrange(rows):
        for j in xrange(columns):
            rand = random.randint(1,10)
            newGrid[i:j] = rand
            
        
    print newGrid

loadGrid()
