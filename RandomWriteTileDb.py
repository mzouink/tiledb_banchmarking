from params import *
import time
import matplotlib.pyplot as plt
import numpy as np
from lib import tiledb_utils, img_utils

file_name = OUTPUT_ZARR


size = [1600,1600,180]
block_size = [128, 128, 128]

image = plt.imread(IMG_PATH)

tiledb_utils.check_and_create(file_name, size, block_size, image.dtype)
def readFile(file):
    with open(file) as f:
        lines = f.readlines()
    result = [[int(n) for n in x.replace("\n", "").split(" ")] for x in lines]
    return result


blocks = readFile('result/shuffle_result_blocks.txt')
positions = readFile('result/shuffle_result_positions.txt')

output_log = "output_log/tiledb_shuffle2_randomwrite_128_128_128_1600_1600_180.csv"
log = open(output_log, "a")

for b, p in zip(blocks, positions):
    img_block = img_utils.get_block_image(image,b)
    start = time.time()
    tiledb_utils.write_tile_block(file_name, p, img_block)
    msg = str(time.time() - start)
    log.write(msg + "\n")

log.close()