#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print("OS name:", os.name)

    
    # Check for item existence and type
    file_name = "textfile.txt"
    print("Item exists      :", str(path.exists(file_name)))
    print("It is a file     :", str(path.isfile(file_name)))
    print("It is a directory:", str(path.isdir(file_name)))

    
    # Work with file paths
    realpath = path.realpath(file_name)
    print("Item's path         :", realpath)
    print("Item's path and name:", path.split(realpath))

    
    # Get the modification time
    path_gettime = path.getmtime(file_name)
    t = time.ctime(path_gettime)
    fromtimestamp = datetime.datetime.fromtimestamp(path_gettime)
    print("File created at:", t)
    print("File created at:", fromtimestamp)

    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - fromtimestamp
    print("It has been", td, "since de file was modified")
    print("Or,", td.total_seconds(), "seconds")

  
if __name__ == "__main__":
    main()
