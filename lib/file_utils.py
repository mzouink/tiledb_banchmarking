import os
import shutil


def check_and_delete_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("File deleted!")


def get_folder_size(path):
    size = 0
    for ele in os.scandir(path):
        size += os.stat(ele).st_size
    return size
