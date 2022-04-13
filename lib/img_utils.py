import numpy as np


def get_size(dim, replication):
    result = []
    for i in range(len(dim)):
        result.append(dim[i] * replication[i])
    if len(dim) < len(replication):
        result.append(replication[2])
    return result

def get_block_image(image,blocksize):
    img = image.copy()

    for i in range(2):
        while(img.shape[i]/blocksize[i]< 1):
            img = np.repeat(img, 2, axis=i)
    img = img[:blocksize[0],:blocksize[1]]

    img = np.dstack([img]*blocksize[2])

    return img

