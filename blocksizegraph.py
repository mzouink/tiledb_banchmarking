from params import *
import time
import matplotlib.pyplot as plt
import numpy as np

file_name = OUTPUT_ZARR

def readFile(file):
    with open(file) as f:
        lines = f.readlines()
    result = [[int(n) for n in x.replace("\n", "").split(" ")] for x in lines]
    return result


blocks = readFile('result/shuffle_result_blocks.txt')
positions = readFile('result/shuffle_result_positions.txt')

output_log = "output_log/shuffle_blocksize.csv"
log = open(output_log, "a")

for b, p in zip(blocks, positions):
    size = b[0]*b[1]*b[2]
    log.write(str(size) + "\n")

log.close()