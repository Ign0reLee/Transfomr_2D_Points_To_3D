import os, glob

import numpy as np
import argparse

from utils import *

# Define Parser
parser = argparse.ArgumentParser()
parser.add_argument("--path_2d", help = "2D Points Directory path")
parser.add_argument("--path_3d", help = "3D Points Directory path")
parser.add_argument("--translate", default=30,help = "3D Points Directory path")
args = parser.parse_args()

# Make Variable
path2d = args.path_2d
path3d = args.path_3d
translate_factor = args.translate

# Check the Path
if not os.path.exists(path2d):
     raise Exception("2D Points path not exists!")
if not os.path.exists(path3d):
     raise Exception("3D Points path not exists!")

