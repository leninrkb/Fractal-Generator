import random 
import math

mod = 4
increments = 1
current = 1
m1, m2, m3, m4 = 1, 2, 3, 4
lastdef = None


def next(current, increments, mod):
    current = (current % mod) + increments
    return current

def stochastic(points):
    random.shuffle(points)
    return points
    
def probability(points):
    p = random.random()
    if p < 0.1:
        return down(points)
    if p < 0.2:
        return right(points)
    if p < 0.6:
        return left(points)
    if p <= 1:
        return up(points)

def sequential_sequential(points):
    global current, m1, m2, m3, m4
    points_ = None
    if current == m1:
        points_ = down(points)
    elif current == m2:
        points_ = up(points)
    elif current == m3:
        points_ = left(points)
    elif current == m4:
        points_ = right(points)
    if current == 4:
        m1 = next(m1, increments, mod)
        m2 = next(m2, increments, mod)
        m3 = next(m3, increments, mod)
        m4 = next(m4, increments, mod)
    current = next(current, increments, mod)
    return points_
    
def sequential(points):
    global current
    current = next(current, increments, mod)
    if current == 2:
        return down(points)
    if current == 3:
        return up(points)
    if current == 4:
        return left(points)
    if current == 1:
        return right(points)

def half_sequential(points):
    global current
    current = next(current, increments, mod)
    if current == 1:
        return up_clockwise(points)
    if current == 2:
        return down_clockwise(points)
    if current == 3:
        return right_clockwise(points)
    if current == 4:
        return left_clockwise(points)
    
def exagon_clockwise(points):
    global current
    current = next(current, increments, mod)
    if current == 1:
        return  up_clockwise(points)
    if current == 2:
        return right_clockwise(points)
    if current == 3:
        return down_clockwise(points)
    if current == 4:
        return left_clockwise(points)
        
def up(points):
    A, B, C, D = points
    points = [
        C, B, D, A
    ]
    return points
    
def right(points):
    A, B, C, D = points
    points = [
        D, A, C, B
    ]
    return points

def down(points):
    A, B, C, D = points
    points = [
        A, D, B, C
    ]
    return points

def left(points):
    A, B, C, D = points
    points = [
        B, C, A, D
    ]
    return points

def up_clockwise(points):
    A, B, C, D = points
    points = [
        B, C, D, A
    ]
    return points

def right_clockwise(points):
    A, B, C, D = points
    points = [
        C, D, A, B
    ]
    return points

def down_clockwise(points):
    A, B, C, D = points
    points = [
        D, A, B, 
 C   ]
    return points

def left_clockwise(points):
    A, B, C, D = points
    points = [
        A, B, C, D
    ]
    return points