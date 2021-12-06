import time
import matplotlib.pyplot as plt
from lib.img_utils import *
from lib.tiledb_utils import *
from lib.file_utils import *
from params import *

# Params
delete_output = True
file_name = OUTPUT_TILEDB

all_replication = [[3, 3, 3], [10, 10, 10], [30, 30, 30], [50, 50, 50], [100, 100, 100], [200, 200, 200]]

for i in range(len(all_replication)):
    print("started " + str(i))
    output_log = "output_log/tiledb_v1_th1_" + str(i) + ".txt"
    replication = all_replication[i]
    print("replication: " + str(replication))
    if delete_output:
        check_and_delete_folder(file_name)

    img = plt.imread(IMG_PATH)
    log = open(output_log, "a")
    size = get_size(img.shape, replication)
    log.write("replications:" + str(replication) + "\n")
    log.write("size:" + str(size) + "\n")
    log.write("start:" + str(time.time()) + "\n")
    check_and_create(file_name, size,img.dtype)
    log.write("create:" + str(time.time()) + "\n")
    print("file created")
    for i in range(replication[0]):
        for j in range(replication[1]):
            for k in range(replication[2]):
                write_array([i, j, k], filename=file_name, data=img)
                log.write("newblock:" + str(time.time()) + "\n")
                print("block " + str([i, j, k]) + " written")

    log.write("done:" + str(time.time()) + "\n")
    log.write("size:" + str(get_folder_size(file_name)) + "\n")

    if delete_output:
        check_and_delete_folder(file_name)
    log.close()
# print("--- %s seconds ---" % (time.time() - start_time))
