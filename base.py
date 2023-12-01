from queue import Queue

def base(matrix, point, initialValue, minimumValue, differenceThreshold, weigthingMethod, sortingMethod):
    min = initialValue
    max = initialValue
    rows = len(matrix)
    columns = len(matrix[0])
    radius = 1
    stack = []
    queue = Queue()
    queue.put(point)
    stack.append(queue)
    insertMethod = queue.put
    while len(stack) > 0:
        currentQueue = stack.pop()
        while not currentQueue.empty():
            currentPoint = currentQueue.get()
            currentPoint[0] = weigthingMethod(currentPoint[0])
            if currentPoint[0] >= minimumValue:
                if currentPoint[0] < min:
                    min = currentPoint[0]
                if currentPoint[0] > max:
                    max = currentPoint[0]
                if 0 <= currentPoint[1] < rows - radius:
                    if 0 <= currentPoint[2] < columns - radius:
                        neighborUp =    [ currentPoint[0],  currentPoint[1]-radius, currentPoint[2]           ]
                        neighborRight = [ currentPoint[0],  currentPoint[1],        currentPoint[2]+radius    ]
                        neighborDown =  [ currentPoint[0],  currentPoint[1]+radius, currentPoint[2]           ]
                        neighborLeft =  [ currentPoint[0],  currentPoint[1],        currentPoint[2]-radius    ]
                        neighbors =     [ neighborUp,  neighborRight, neighborDown,  neighborLeft] #nu
                        neighbors = sortingMethod(neighbors)
                        newQueue = Queue()
                        for neighbor in neighbors:
                            if neighbor == None:
                                continue
                            currentNeighbor = neighbor
                            matrixValue = matrix[currentNeighbor[1]][currentNeighbor[2]]
                            if matrixValue == 0:
                                matrix[currentNeighbor[1]][currentNeighbor[2]] = currentNeighbor[0]
                                newQueue.put(neighbor)
                            else:
                                neighborValue = currentNeighbor[0]
                                sum = abs(neighborValue) + abs(matrixValue)
                                neighborValue /= sum
                                matrixValue /= sum
                                diff = neighborValue - matrixValue
                                if diff >= differenceThreshold:
                                    matrix[currentNeighbor[1]][currentNeighbor[2]] = currentNeighbor[0]
                                    newQueue.put(neighbor)
                        if not newQueue.empty():
                            stack.append(newQueue)
    return (min, max)