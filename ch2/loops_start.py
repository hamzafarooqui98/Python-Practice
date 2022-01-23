#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while (x < 5):
        print(x)
        x += 1

    # TODO: define a for loop
    # for z in range(5, 10):  # from 5 to 10(exclusive) loop
    #     print(z)

    # TODO: use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # TODO: use the break and continue statements
    for z in range(5, 10):  # from 5 to 10(exclusive) loop
        # if z == 7:
        #     break
        if z % 2 == 0:
            continue   # Continue statement will go to the next loop without executing the below code
        print(z)

    # TODO: using the enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()
