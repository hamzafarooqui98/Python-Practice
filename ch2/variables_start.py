# 
# Example file for variables
#

#Declare a variable and initialize it
f=0
print(f)



# re-declaring the variable works
f="abc"
print(f)


# # ERROR: variables of different types cannot be combined
print("this is a string " + str(123)) 


 # Global vs. local variables in functions
# To run the code below comment out all the code above (except f=0) to run it:
def someFunction():
    global f # if u want to use a global variable
    f= "def"
    print(f)

someFunction()
print(f)

del f  # U can undefine the variables in real time by usinf "del statement"
print(f)