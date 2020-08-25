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

def Slice_Points(slice_factor =(0,1), points=np.array([2,3])):
    start, end = slice_factor
    return points[start:end]

def Calc_Sacling_Factor(left2d, right2d, left3d, right3d):
    
    left_max2d, _        = np.argmax(left2d,axis=0)
    left_max3d, _, _,  _ = np.argmax(left3d,axis=0)
    
    right_min2d, _       = np.argmin(right2d,axis=0)
    right_min3d, _, _, _ = np.argmin(right3d,axis=0)
    
    sub2d = left2d[left_max2d] - right2d[right_min2d]
    sub3d = left3d[left_max3d] - right3d[right_min3d]
    
    dist2d = np.sqrt(np.sum(np.square(sub2d)))
    dist3d = np.sqrt(np.sum(np.square(sub3d)))
    print(dist2d)
    print(dist3d)
    
    return dist2d/dist3d
        

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

    

def Scaling_3D(factor = (1,1,1), old_points = (0,0,0,0)):
    """
    Sacling the 3D points.

    factor     : float32, Sacling factor you want.
    old_points : float32, The original points.
    return     : float32, Scaling  points from (0,0,0)
    """
    
    sx, sy, sz = factor
    ox, oy, oz,_ = old_points
    
    matrix = np.array([
        [sx, 0,  0, 0],
        [0, sy,  0, 0],
        [0,  0, sz, 0],
        [0,  0,  0, 1]
    ])
    
    old_points = np.array([ox,oy,oz,1])
    new_points = np.matmul(matrix, old_points)
    
    return new_points[:-1]

def Scaling_3D_xy(factor = (1,1,1), old_points = (0,0,0,0)):
    """
    Sacling the 3D points. but only x and y

    factor     : float32, Sacling factor you want.
    old_points : float32, The original points.
    return     : float32, Scaling  points from (0,0,0)
    """
    sx, sy, sz = factor
    ox, oy, oz, _ = old_points
    
    matrix = np.array([
        [sx, 0,  0, 0],
        [0, sy,  0, 0],
        [0,  0,  1, 0],
        [0,  0,  0, 1]
    ])
    
    old_points = np.array([ox,oy,oz,1])
    new_points = np.matmul(matrix, old_points)
    
    return new_points[:-1]

