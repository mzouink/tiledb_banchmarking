import numpy as np
import sys
import tiledb
import matplotlib.pyplot as plt
from lib.tiledb_utils import *
from lib.img_utils import *

file_name = "../output/hello"
attr = "image"

replication = [3, 3, 3]

img = plt.imread('img/DrosophilaWing.tif')

check_and_create(file_name, get_size(img.shape, replication), attr, img.dtype)

for i in range(replication[0]):
    for j in range(replication[1]):
        for k in range(replication[2]):
            write_array([i, j, k], filename=file_name, data=img)
