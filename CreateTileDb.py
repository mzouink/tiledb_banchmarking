import time

import matplotlib.pyplot as plt
from lib import tiledb_utils,img_utils,zarr_utils
from params import *

# Params
delete_output = True
file_name = OUTPUT_TILEDB
threads = 10

img = plt.imread(IMG_PATH)
img = img[:, :300]
# block_size = [img.shape[0]*2, img.shape[1]*3, 1]
block_size = [128, 128, 128]
strblock = "_".join([str(b) for b in block_size])
print(block_size)
#
# all_replication = [[3, 3, 3], [10, 10, 10], [30, 30, 30], [50, 50, 50], [100, 100, 100], [200, 200, 200],
#                    [500, 500, 500]]
all_replication = [[2, 2, 180]]

def processAll():
    start = time.time()
    total = 0
    for i in range(replication[0]):
        for j in range(replication[1]):
            for k in range(replication[2]):
                tiledb_utils.write_array([i, j, k], filename=file_name, data=img)
                msg = str(total) + "-newblock;" + str(time.time() - start)
                total += 1
                print(msg)
                log.write(msg + "\n")
                start = time.time()
                if total > 1000:
                    return

    return
for x in range(len(all_replication)):

    print("started " + str(x))
    repstr = "_".join([str(b) for b in all_replication[x]])
    output_log = "output_log/tiledb_v6_Dense_" + strblock + "_th1_rep_" + repstr + "_" + str(x) + ".csv"
    print(output_log)
    replication = all_replication[x]
    print("replication: " + str(replication))
    if delete_output:
        tiledb_utils.check_and_delete_folder(file_name)

    img = plt.imread(IMG_PATH)
    log = open(output_log, "a")
    size = tiledb_utils.get_size(img.shape, replication)
    log.write("replications;" + str(replication) + "\n")
    log.write("size;" + str(size) + "\n")
    log.write("block size:" + str(block_size) + "\n")
    start = time.time()
    log.write("start;" + str(start) + "\n")
    tiledb_utils.check_and_create(file_name, size, block_size, img.dtype)

    log.write("creation;" + str(time.time() - start) + "\n")

    log.write("create;" + str(time.time()) + "\n")
    print("file created")
    processAll()

    log.write("done;" + str(time.time()) + "\n")
    log.write("size;" + str(tiledb_utils.get_folder_size(file_name)) + "\n")
    print("done!")
    # if delete_output:
    #     check_and_delete_folder(file_name)
    # log.close()
# print("--- %s seconds ---" % (time.time() - start_time))
