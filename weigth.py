import random
import math 

initialValue = 0 
minimumValue = 0
maxDistance = 0
probability = 0
weigthing = 0
count = 0
weigthingMethod = '*'

def simple(value):
    if weigthingMethod == '*':
        value *= weigthing
    elif weigthingMethod == '-':
        value -= weigthing
    return value

def  choice(value):
    global count
    if weigthingMethod == '*':
        value *= weigthing
    if weigthingMethod == '-':
        value -= weigthing
    if weigthingMethod == 'sin':
        amplitud = 1/2
        longitud = 7/1
        offset = 0
        value -= math.sin( count / longitud ) * amplitud
        count+= 0.1
    return value

def distance(value):
    diff = abs(minimumValue - value)
    if diff <= maxDistance:
        p = random.random()
        if p <= probability:
            value = initialValue
    else:
        value = simple(value)
    return value
    