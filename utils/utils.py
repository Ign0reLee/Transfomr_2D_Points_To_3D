import os
import numpy as np

def Load_Data(path):
    """
    Load Data and make it type float
    Load file must be formed like (Number, x, y) or (Number, x, y, z)
    
    path   : string, path you want.
    return : numpy array, all points of file dtype=float32
    """
    
    line = []
    
    with open(path, 'r') as f:
        lines = f.readlines()
        for l in lines:
            line.append(l.split()[1:])
        line = np.array(line,dtype=np.float32)
        
    return line
        

def Translation_3D(factor = (0,0,0), old_points = (0,0,0)):
    """
    Translate the points.
    
    factor     : float32, Translate factor you want.
    old_points : float32, The original points
    return     : float32, Translated points
    """
    
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
    """
    Sacling the 3D points.

    factor     : float32, Sacling factor you want.
    old_points : float32, The original points.
    return     : float32, Scaling  points from (0,0,0)
    """
    
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

def Scaling_3D_xy(factor = (1,1,1), old_points = (0,0,0)):
    """
    Sacling the 3D points. but only x and y

    factor     : float32, Sacling factor you want.
    old_points : float32, The original points.
    return     : float32, Scaling  points from (0,0,0)
    """
    sx, sy, sz = factor
    ox, oy, oz = old_points
    
    matrix = np.array([
        [sx, 0,  0, 0],
        [0, sy,  0, 0],
        [0,  0,  1, 0],
        [0,  0,  0, 1]
    ])
    
    old_points = np.array([ox,oy,oz,1])
    new_points = np.matmul(matrix, old_points)
    
    return new_points

