import time

import matplotlib.pyplot as plt

from lib.file_utils import *
from lib.img_utils import *
from lib.zarr_utils import *
from params import *
import numpy as np

# Params
delete_output = True
file_name = OUTPUT_ZARR
threads = 10

image = plt.imread(IMG_PATH)
image = image[:, :400]
data = np.asarray(image).reshape((image.shape[0], image.shape[1], 1))
print("shape2: " + str(data.shape))
block_size = [128, 128, 128]
# block_size = [data.shape[0]*2, data.shape[1]*3, 1]
# block_size = [20,20,20]
strblock = "_".join([str(b) for b in block_size])
print(strblock)
#
# all_replication = [[3, 3, 3], [10, 10, 10], [30, 30, 30], [50, 50, 50], [100, 100, 100], [200, 200, 200],
#                    [500, 500, 500]]
all_replication = [[2, 2, 130]]


def processAll():
    start = time.time()
    total = 0
    for i in range(replication[0]):
        for j in range(replication[1]):
            for k in range(replication[2]):
                log = open(output_log, "a")
                write_array([i, j, k], filename=file_name, data=data)
                msg = str(total) + ";" + str(time.time() - start)
                total = total + 1
                print(msg)
                log.write(msg + "\n")
                start = time.time()
                log.close()
                # if total > 1000:
                #     return

    return


for x in range(len(all_replication)):

    print("started " + str(x))
    repstr = "_".join([str(b) for b in all_replication[x]])
    output_log = "output_log/zarr_v1_" + strblock + "_th1_rep_" + repstr + "__" + str(x) + ".csv"
    print(output_log)
    replication = all_replication[x]
    print("replication: " + str(replication))
    if delete_output:
        check_and_delete_folder(file_name)

    img = plt.imread(IMG_PATH)
    log = open(output_log, "a")
    size = get_size(img.shape, replication)
    log.write("replications;" + str(replication) + "\n")
    log.write("size;" + str(size) + "\n")
    log.write("block size;" + str(block_size) + "\n")
    start = time.time()
    log.write("start;" + str(start) + "\n")
    create_array(file_name, size, block_size)

    log.write("creation;" + str(time.time() - start) + "\n")

    log.write("create;" + str(time.time()) + "\n")
    print("file created")
    log.close()
    processAll()
    log = open(output_log, "a")
    log.write("done;" + str(time.time()) + "\n")
    log.write("size;" + str(get_folder_size(file_name)) + "\n")
    print("done!")
    if delete_output:
        check_and_delete_folder(file_name)
    log.close()
# print("--- %s seconds ---" % (time.time() - start_time))
