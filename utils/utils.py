import os
import numpy as np

def Load_Data(path):
    
    line = []
    
    with open(path, 'r') as f:
        lines = f.readlines()
        for l in lines:
            line.append(l.split()[1:])
        line = np.array(line,dtype=np.float32)
        
    return line
        

def Translation_3D(factor = (0,0,0), old_points = (0,0,0)):
    
    tx, ty, tz = factor
    ox, oy, oz = old_points
    
    matrix = np.array([
        [1,0,0,tx],
        [0,1,0,ty],
        [0,0,1,tz],
        [0,0,0, 1]
    ])
    
    old_points = np.array([ox,oy,oz,1])
    new_points = np.matmul(matrix, old_points)
    
    return new_points

def Scaling_3D(factor = (1,1,1), old_points = (0,0,0)):
    
    sx, sy, sz = factor
    ox, oy, oz = old_points
    
    matrix = np.array([
        [sx, 0,  0, 0],
        [0, sy,  0, 0],
        [0,  0, sz, 0],
        [0,  0,  0, 1]
    ])
    
    old_points = np.array([ox,oy,oz,1])
    new_points = np.matmul(matrix, old_points)
    
    return new_points
