import time
import matplotlib.pyplot as plt
from lib.img_utils import *
from lib.tiledb_utils import *
from lib.file_utils import *
from params import *
from concurrent.futures import ProcessPoolExecutor


# Params

def run_multi_thread():
    delete_output = True
    file_name = OUTPUT_TILEDB
    threads = 1

    all_replication = [[3, 3, 3], [10, 10, 10], [30, 30, 30], [50, 50, 50], [100, 100, 100], [200, 200, 200]]

    img = plt.imread(IMG_PATH)

    def write_block(block):
        print("Writing:"+str(block))
        write_array(block, filename=file_name, data=img)
        log.write("newblock:" + str(time.time()) + "\n")
        print("block " + str(block) + " written")

    for r in range(len(all_replication)):
        print("started " + str(r))
        output_log = "output_log/tiledb_v2_th10_" + str(r) + ".txt"
        if os.path.exists(output_log):
            os.remove(output_log)
        replication = all_replication[r]
        print("replication: " + str(replication))
        if delete_output:
            check_and_delete_folder(file_name)

        log = open(output_log, "a")
        size = get_size(img.shape, replication)
        log.write("replications:" + str(replication) + "\n")
        log.write("size:" + str(size) + "\n")
        log.write("start:" + str(time.time()) + "\n")
        check_and_create(file_name, size, img.dtype)
        log.write("create:" + str(time.time()) + "\n")
        print("file created")
        start = time.time()
        with ProcessPoolExecutor(max_workers=threads) as executor:
            for i in range(replication[0]):
                for j in range(replication[1]):
                    for k in range(replication[2]):
                        executor.submit(write_block, [i, j, k])

        # print("Task results: ", [t.result() for t in tasks])

        print("Ingestion complete. Duration: ", time.time() - start)
        log.write("done:" + str(time.time()) + "\n")
        log.write("size:" + str(get_folder_size(file_name)) + "\n")

        if delete_output:
            check_and_delete_folder(file_name)
        log.close()
        break


if __name__ == "__main__":
    run_multi_thread()
