import numpy as np


def get_size(dim, replication):
    result = []
    for i in range(len(dim)):
        result.append(dim[i] * replication[i])
    if len(dim) < len(replication):
        result.append(replication[2])
    return result
