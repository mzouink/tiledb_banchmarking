
from params import *
import time
import matplotlib.pyplot as plt
import numpy as np
from lib.zarr_utils import *

file_name = OUTPUT_ZARR

def readFile(file):
    with open(file) as f:
        lines = f.readlines()
    result = [[int(n) for n in x.replace("\n", "").split(" ")] for x in lines]
    return result


blocks = readFile('result/result_blocks.txt')
positions = readFile('result/result_positions.txt')

output_log = "output_log/zarr_v6_Dense_read_noOutput.csv"
log = open(output_log, "a")

for b, p in zip(blocks, positions):
    start = time.time()
    read_zarr_block(file_name, p, b)
    # print(blockdata)
    msg = str(time.time() - start)
    log.write(msg + "\n")

log.close()
#
# file_name = OUTPUT_ZARR
# z = zarr.open(file_name, smode='r')
# print(z.shape)
# # write_array([i, j, k], filename=file_name, data=data)
#
# x = z[:,:,4]
# plt.imshow(np.reshape(x,(x.shape[0],x.shape[1])),cmap="gray")
# plt.show()
