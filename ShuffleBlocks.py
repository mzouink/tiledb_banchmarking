from params import *
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import shuffle


def readFile(file):
    with open(file) as f:
        lines = f.readlines()
    result = [[int(n) for n in x.replace("\n", "").split(" ")] for x in lines]
    return result


blocks = readFile('result/result_blocks.txt')
positions = readFile('result/result_positions.txt')


def writeFile(file,x):
    file = open(file, 'w')
    for l in x:
        print(l)
        file.write(" ".join([str(n) for n in l])+"\n")
    file.close()

result_blocks, result_positions = shuffle(blocks, positions, random_state=0)

writeFile('result/shuffle_result_blocks.txt', result_blocks)
writeFile('result/shuffle_result_positions.txt', result_positions)