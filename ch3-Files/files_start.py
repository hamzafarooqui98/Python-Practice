#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():
    # Open a file for writing (also overwrites) and create it if it doesn't exist
    # myfile = open("textfile.txt", "w")  # '+' sign is used to create the file

    # Open the file for appending text to the end
    # myfile = open("textfile.txt", "a+")

    # # write some lines of data to the file
    # for i in range(10):
    #     myfile.write("This is some Text \n")

    # # close the file when done
    # myfile.close()

    # Open the file back up and read the whole content of the file   P.S: For Read u don't have to close the file
    myfile = open("../textfile.txt", "r")  # r means read
    if myfile.mode == 'r':
        # contents = myfile.read()
        # print(contents)
        fl = myfile.readlines()  # It converts the all the line contents in a list
        print(fl)
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()
