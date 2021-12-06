import numpy as np
import sys
import tiledb


def check_and_create(filename, dims, attr_name, dtype):
    if tiledb.object_type(filename) != "array":
        create_array(filename, dims, attr_name, dtype)


def create_array(filename, dims, attr_name, dtype):
    # The array will be 4x4 with dimensions "rows" and "cols", with domain [1,4] and space tiles 2x2.
    dom = tiledb.Domain(
        tiledb.Dim(name="x", domain=(0, dims[0] - 1), tile=dims[0], dtype=np.int32),
        tiledb.Dim(name="y", domain=(0, dims[1] - 1), tile=dims[1], dtype=np.int32),
        tiledb.Dim(name="z", domain=(0, dims[2] - 1), tile=1, dtype=np.int32)
    )


    attr = tiledb.Attr(dtype=np.dtype("i4, i4, i4"))
    # tiledb.Attr(name=attr, dtype=dtype)
    # The array will be dense with a single attribute "a" so each (i,j) cell can store an integer.
    schema = tiledb.ArraySchema(
        domain=dom, sparse=False, attrs=[attr]
    )

    # Create the (empty) array on disk.
    tiledb.Array.create(filename, schema)
    with tiledb.open(filename) as A:
        print(A[:].shape)


def write_array(grid_position, filename, data):
    size = data.shape
    positions = [size[0] * grid_position[0], size[1] * grid_position[1], grid_position[2]]
    with tiledb.open(filename, mode="w") as A:
        A[positions[0]:positions[0] + size[0], positions[1]:positions[1] + size[1],
        positions[2]:positions[2]+1] = data
