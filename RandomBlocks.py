import os
import matplotlib.pyplot as plt
import random
import numpy as np

from params import IMG_PATH


def getRandomBlock(max):
    return np.asarray([[random.randint(int(max[0] / 2), max[0]), random.randint(int(max[1] / 2), max[1]),
                       random.randint(int(max[2] / 2), max[2])]])


def getRandomPosition(bsize, size):
    return np.asarray([[random.randint(0, size[0] - bsize[0]), random.randint(0, size[1] - bsize[1]),
                        random.randint(0, size[2] - bsize[2])]])

def writeFile(file,x):
    file = open(file, 'w')
    for l in x:
        print(l)
        file.write(" ".join([str(n) for n in l])+"\n")
    file.close()

maxs = [[30, 30, 30], [150, 150, 150], [300, 300, 150]]
replucations = [2, 2, 180]

img = plt.imread(IMG_PATH)
img = img[:, :300]

size = np.asarray([img.shape[0] * replucations[0], img.shape[1] * replucations[1], replucations[2]])

result_positions = np.empty((0, 3), np.int8)
result_blocks = np.empty((0, 3), np.int8)

for i in range(3):
    for j in range(300):
        block = getRandomBlock(maxs[i])
        pos = getRandomPosition(block[0], size)
        result_blocks = np.append(result_blocks, block, axis=0)
        result_positions = np.append(result_positions, pos, axis=0)

# print(result_blocks)
# print(result_positions)
writeFile('result/result_blocks.txt', result_blocks)
writeFile('result/result_positions.txt', result_positions)
