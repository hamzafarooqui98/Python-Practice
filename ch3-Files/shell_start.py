#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("../textfile.txt.bak"):
        # get the path to the file in the current directory
        src = path.realpath("../textfile.txt")

        # let's make a backup copy by appending "bak" to the name
        # dst = src + ".bak"
        # shutil.copy(src, dst)

        # rename the original file
        # chamge the name of the file specifie in 1st argument to the name written on 2nd argument
        # os.rename("../textfile.txt", "newfile.txt")

        # now put things into a ZIP archive
        # root_dir, tail = path.split(src)
        # # first argument is for name of the zip file and 3rd argument is the path where u want to have it
        # shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        # 'with' keyword lets us help us to create a local scope that simplifies working with objects
        with ZipFile("testzip.zip", "w") as newzip:
            # ZipFile() is just like writing a file where the 1st argument is the name of the file and 2nd argument is what u want to do with it
            # In our case it is to write
            # 'newzip variable is used as reference to control ZipFile("testzip.zip", "w")'
            newzip.write("newfile.txt")
            newzip.write("../textfile.txt.bak")


if __name__ == "__main__":
    main()
