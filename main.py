import numpy as np
import cv2
import matplotlib.pyplot as plt 
import insertion
import weigth
import alg
import base

weigth.weigthingMethod = '-'
weigth.weigthing = 0.3 #chi
weigth.probability = 0.01
weigth.maxDistance = 1 # sigma
weigth.minimumValue = 10 # kappa
weigth.initialValue = 500 # epsilon

matrix = []
dimension = 500
rows, columns = dimension, dimension # row = beta; column = gamma
matrix = np.zeros((rows, columns))

point = []
iSpawn, jSpawn = rows//2, columns//2
point = [weigth.initialValue, iSpawn, jSpawn]

matrix[point[1]][point[2]] = point[0]

min, max = alg.lifo(
    matrix, 
    point, 
    initialValue = weigth.initialValue, 
    minimumValue = weigth.minimumValue,
    differenceThreshold = 1, # lambda
    weigthingMethod = weigth.simple, 
    sortingMethod = insertion.sequential
)

c = min + (max - min) * 0.009
# _, matrix = cv2.threshold(matrix, c, 255, cv2.THRESH_BINARY)

plt.imshow(matrix)
plt.colorbar()
plt.show() 


# fig, ax = plt.subplots()
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         value = matrix[i, j]
#         ax.text(j, i, value, ha='center', va='center', color='black')
# ax.invert_yaxis()
# plt.show()