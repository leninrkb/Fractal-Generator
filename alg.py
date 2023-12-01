from queue import Queue
import random 

def do_something(insertMethod, weigthingMethod, sortingMethod, matrix, currentPoint, min, max, minimumValue, rows, columns, radius, differenceThreshold):
    currentPoint[0] = weigthingMethod(currentPoint[0])
    if currentPoint[0] >= minimumValue:
        if currentPoint[0] < min:
            min = currentPoint[0]
        if currentPoint[0] > max:
            max = currentPoint[0]
        if 0 <= currentPoint[1] < rows - radius:
            if 0 <= currentPoint[2] < columns - radius:
                neighbors = get_neighbors(currentPoint, radius)
                neighbors = sortingMethod(neighbors)
                process_neighbors(insertMethod, neighbors, matrix, differenceThreshold)
    return(min, max)
    

def get_neighbors(currentPoint, radius):
    neighborUp =    [ currentPoint[0],  currentPoint[1]-radius, currentPoint[2]           ]
    neighborRight = [ currentPoint[0],  currentPoint[1],        currentPoint[2]+radius    ]
    neighborDown =  [ currentPoint[0],  currentPoint[1]+radius, currentPoint[2]           ]
    neighborLeft =  [ currentPoint[0],  currentPoint[1],        currentPoint[2]-radius    ]
    neighbors =     [ neighborUp,   neighborRight,  neighborDown,   neighborLeft]
    return neighbors

def process_neighbors(insertMethod, neighbors, matrix, differenceThreshold):
    for neighbor in neighbors:
        if neighbor == None:
            continue
        currentNeighbor = neighbor
        matrixValue = matrix[currentNeighbor[1]][currentNeighbor[2]]
        if matrixValue == 0:
            matrix[currentNeighbor[1]][currentNeighbor[2]] = currentNeighbor[0]
            insertMethod(neighbor)
        else:
            neighborValue = currentNeighbor[0]
            sum = abs(neighborValue) + abs(matrixValue)
            neighborValue /= sum
            matrixValue /= sum
            diff = neighborValue - matrixValue
            if diff >= differenceThreshold:
                matrix[currentNeighbor[1]][currentNeighbor[2]] = currentNeighbor[0]
                insertMethod(neighbor)


def lifo(matrix, point, initialValue, minimumValue, differenceThreshold, weigthingMethod, sortingMethod):
    min = initialValue
    max = initialValue
    rows = len(matrix)
    columns = len(matrix[0])
    radius = 1
    stack = []
    stack.append(point)
    while len(stack) > 0:
        currentPoint = stack.pop()
        min, max = do_something(stack.append, weigthingMethod, sortingMethod, matrix, currentPoint, min, max, minimumValue, rows, columns, radius, differenceThreshold)       
    return (min, max)

def fifo_lifo(matrix, point, initialValue, minimumValue, differenceThreshold, weigthingMethod, sortingMethod):
    min = initialValue
    max = initialValue
    rows = len(matrix)
    columns = len(matrix[0])
    radius = 1
    stack = []
    stack.append(point)
    queue = Queue()
    queue.put(stack)
    while not queue.empty():
        currentStack = queue.get()
        newStack = []
        while len(currentStack) > 0:
            currentPoint = currentStack.pop()
            min, max = do_something(newStack.append, weigthingMethod, sortingMethod, matrix, currentPoint, min, max, minimumValue, rows, columns, radius, differenceThreshold)       
        if len(newStack) > 0:
            queue.put(newStack)
    return (min, max)


def lifo_fifo(matrix, point, initialValue, minimumValue, differenceThreshold, weigthingMethod, sortingMethod):
    min = initialValue
    max = initialValue
    rows = len(matrix)
    columns = len(matrix[0])
    radius = 1
    queue = Queue()
    queue.put(point)
    stack = []
    stack.append(queue)
    while len(stack) > 0:
        currentQueue = stack.pop()
        newQueue = Queue()
        while not currentQueue.empty():
            currentPoint = currentQueue.get()
            min, max = do_something(newQueue.put, weigthingMethod, sortingMethod, matrix, currentPoint, min, max, minimumValue, rows, columns, radius, differenceThreshold)       
            if not newQueue.empty():
                stack.append(newQueue)
    return (min, max)