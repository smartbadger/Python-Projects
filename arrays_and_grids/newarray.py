#Connor Bailes

from arrays import Array
import random

def createArray():

    arraySize = int(raw_input("Enter Size"))
    userStartRange = int(raw_input("Enter Start"))
    userStopRange = int(raw_input("Enter Stop"))

    newArray = Array(arraySize)
    
    for i in xrange(arraySize):
        rand = random.randint(userStartRange, userStopRange)
        newArray[i] = rand
    print newArray

createArray()
