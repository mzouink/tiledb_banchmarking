import numpy as np
import tiledb


def check_and_create(filename, dims,blocksize, dtype):
    if tiledb.object_type(filename) != "array":
        create_array(filename, dims,blocksize,dtype)


def create_array(filename, dims,blocksize,dtype):
    dom = tiledb.Domain(
        tiledb.Dim(name="x", domain=(0, dims[0] - 1), tile=blocksize[0], dtype=np.int32),
        tiledb.Dim(name="y", domain=(0, dims[1] - 1), tile=blocksize[1], dtype=np.int32),
        tiledb.Dim(name="z", domain=(0, dims[2] - 1), tile=blocksize[2], dtype=np.int32)
    )

    attr = tiledb.Attr(dtype=dtype)
    # tiledb.Attr(name=attr, dtype=dtype)
    schema = tiledb.ArraySchema(
        domain=dom, sparse=False, attrs=[attr]
    )

    # Create the (empty) array on disk.
    tiledb.Array.create(filename, schema)


def write_array(grid_position, filename, data):
    size = data.shape
    positions = [size[0] * grid_position[0], size[1] * grid_position[1], grid_position[2]]
    # DenseArray
    with tiledb.DenseArray(filename, mode="w") as A:
        A[positions[0]:positions[0] + size[0], positions[1]:positions[1] + size[1],
        positions[2]:positions[2] + 1] = data
