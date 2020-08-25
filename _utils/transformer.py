import os
import numpy as np

from tqdm import tqdm
from .utils import *


class Transformer():

    def __init__(self, path3d, translate,left_values, right_values):
        
        self.points3d      =  self.__load_3d__(path3d, translate)
        self.left_values   =  left_values
        self.rgiht_values  =  right_values
        self.left_3d       =  Slice_Points(left_values, self.points3d)
        self.right_3d      =  Slice_Points(right_values, self.points3d)
        print("End..")

    def __load_3d__(self, path, translate):

        print("Start Load and Translate the 3D points..")

        points = Load_Data(path)
        trans_point = []

        for p in tqdm(points, desc = "3D Point Translate"):
            trans_point.append(Translation_3D((translate, translate, translate), p))
        
        return trans_point
    
    def trans(self, path):

        points   = Load_Data(path)
        left_2d  = Slice_Points(self.left_values, points)
        right_2d = Slice_Points(self.rgiht_values, points)
        factor   = Calc_Sacling_Factor(left_2d, right_2d, self.left_3d. self.right_3d)
        factors  = (factor, factor, factor)

        scaled_points = []
        for p in self.points3d:
            scaled_points.append(Scaling_3D(factors, p))

        return scaled_points
            

