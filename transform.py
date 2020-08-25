import os, glob
import argparse

import numpy as np

from tqdm import tqdm
from _utils import *

# Define Parser
parser = argparse.ArgumentParser()
parser.add_argument("--path_2d", help = "2D Points Directory path")
parser.add_argument("--path_3d", help = "3D Points Directory path")
parser.add_argument("--translate", default=30,help = "3D Points Directory path")
parser.add_argument("--left", default =(93,105), help="For Scaling Factor compute left")
parser.add_argument("--right", default=(105,117), help="For Scaling Factor compute right")
args = parser.parse_args()

# Make Variable
path2d = args.path_2d
path3d = args.path_3d
translate_factor = args.translate
left = args.left
right =  args.right

# Check the Path
if not os.path.exists(path2d):
     raise Exception("2D Points path not exists!")
if not os.path.exists(path3d):
     raise Exception("3D Points path not exists!")

# Load Data
path2d = glob.glob(os.path,join(path2d, "*"))
path3d =  glob.glob(os.path.join(path3d, "*"))[0]
trans = Transformer(path3d, translate_factor, left, right)


# Main Start
for path in tqdm(path2d, desc="Scaling 3D Points Now.."):
    points = trans.trans(path)