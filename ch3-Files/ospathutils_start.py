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
    print(os.name)  # For windows it will display 'nt'

    # Check for item existence and type
    print("Item exists:", path.exists("../textfile.txt"))
    print("Item is a file:", path.isfile("../textfile.txt"))
    print("Item is a directory:", path.isdir("../textfile.txt"))

    # Work with file paths
    # Shows the path of the file
    print("Item's path:", path.realpath("../textfile.txt"))
    # Shows the path and name of the file in a tuple
    print("Item's path & name:", path.split(path.realpath("../textfile.txt")))

    # Get the modification time
    t = time.ctime(path.getmtime("../textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("../textfile.txt")))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - \
        datetime.datetime.fromtimestamp(path.getmtime("../textfile.txt"))
    print("It has been", td, "since the file was modified")
    print("Or,", td.total_seconds(), "seconds")


if __name__ == "__main__":
    main()
