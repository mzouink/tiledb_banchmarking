import numpy as np
import zarr


def create_array(filename, dims, blocksize):
    # print(dims.dtype)
    # print(blocksize.dtype)
    root = zarr.open(filename, shape=dims, chunks=blocksize, mode='w', dtype="i4")


def write_array(grid_position, filename, data):
    z = zarr.open(filename, smode='w')
    size = data.shape
    print("shape: " + str(size))
    positions = [size[0] * grid_position[0], size[1] * grid_position[1], grid_position[2]]
    z[positions[0]:positions[0] + size[0], positions[1]:positions[1] + size[1],
    positions[2]:positions[2] + 1] = data
