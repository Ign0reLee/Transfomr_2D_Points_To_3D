import os, glob
import argparse
import time

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
parser.add_argument("--os", default="u", help="For windows users, This is just using for path separator")
args = parser.parse_args()

# Make Variable
path2d = args.path_2d
path3d = args.path_3d
translate_factor = args.translate
left = args.left
right =  args.right

if args.os == "u":
    separator = "/"
elif args.os =="w":
    separator = "\\"
else:
    raise Exception("Please input right your OS enviroment, if mac user's it does not supported yet!")

# Check the Path
if not os.path.exists(path2d):
     raise Exception("2D Points path not exists!")
if not os.path.exists(path3d):
     raise Exception("3D Points path not exists!")

# Load Data
path2d = glob.glob(os.path.join(path2d, "*"))
path3d =  glob.glob(os.path.join(path3d, "*"))[0]
trans = Transformer(path3d, translate_factor, left, right)


# Main Start

print("Sacling Start...")
start = time.time()
for path in tqdm(path2d, desc="Scaling 3D Points Now.."):
    points = trans.trans(path)
    name = path.split(separator)[-1].replace(".txt", ".csv")
    make_csv(points,name)

print("Scaling End..")
print("End Time : %.3f second"%(time.time() - start))