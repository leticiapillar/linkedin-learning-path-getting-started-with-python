# Calculate the total size of files in a directory in bytes

import os
from os import path

def generate_files():
    dir_name = "deps/"
    files_name = ["file1.txt", "file2.txt", "file3.txt"]
    if path.exists(dir_name) == False:
        os.makedirs(dir_name)
    for fname in files_name:
        file_name = dir_name + fname
        if path.exists(file_name) == False:
            file = open(file_name, "w+")
            file.write(f"Write on line in a file {fname}")
            file.close()

def file_info():
    # Your code goes here.
    dir_name = "deps/"
    size = 0
    for fname in os.listdir(dir_name):
        # print(fname, path.isfile(dir_name+fname))
        if path.isfile(dir_name+fname) and fname.endswith(".txt"):
            size += path.getsize(dir_name+fname)
    return size

def main():
    generate_files()
    size = file_info()
    print("Total size:", size)


if __name__ == "__main__":
    main()