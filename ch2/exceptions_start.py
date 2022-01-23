#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x= 10 / 0

# TODO: Exceptions provide a way of catching errors and then handling them in
# a separate section of the code to group them together
# try:
#     x = 10 / 0
# except:
#     print("That is wrong")


# TODO: You can also catch specific exceptions
try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
    print(e)  # Output: "division by zero"
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally:                 # finally contains code that always executes regardless of an error occured
    #   0and u can also use to clean up any resources that u have allocated such an open files
    print("This code always runs")
