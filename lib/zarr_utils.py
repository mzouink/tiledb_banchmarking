import zarr


def create_zarr_array(filename, dims, blocksize):
    # print(dims.dtype)
    # print(blocksize.dtype)
    root = zarr.open(filename, shape=dims, chunks=blocksize, mode='w', dtype="i4")


def write_zarr_block(filename, position, data):
    z = zarr.open(filename, smode='w')
    size = data.shape
    print("shape: " + str(size))
    print("position: " + str(position))
    z[position[0]:position[0] + size[0], position[1]:position[1] + size[1], position[2]:position[2] +size[2]] = data


def write_array(grid_position, filename, data):
    z = zarr.open(filename, smode='w')
    size = data.shape
    print("shape: " + str(size))
    positions = [size[0] * grid_position[0], size[1] * grid_position[1], grid_position[2]]
    z[positions[0]:positions[0] + size[0], positions[1]:positions[1] + size[1],
    positions[2]:positions[2] + 1] = data


def read_zarr_block(file, position, block):
    z1 = zarr.open(file, mode='r')
    return z1[position[0]:position[0] + block[0], position[1]:position[1] + block[1],
           position[2]:position[2] + block[2]]
