# Calvin Thang
# Final Exam

# purpose of 1 is to accept an argument and print a string
# define function as summer with parameter of a
def summer(a):
    # set counter container to 0
    counter = 0

    # execute if the counter's value is less than 3
    while counter < 3:
        # output value container
        a = 'Summer is almost here!'
        # print statement for value a
        print (a)
        # counter increments by 1
        counter += 1

# call the function 3 times
summer(3)

# purpose of 2 is to read a file line by line and put into a list
# define function as partTwo with no parameters
def partTwo():
    
    # set variable openf to contain the textfile
    openf = open("sortOfWhite.txt", "r")
    # create an empty list
    emptyList = []
    # set a counter to 0
    counter = 0

    # for every line in the variable openf
    for line in openf:
        # set the variable delimiter to contain the string '#'
        delimiter = '#'
        # remove '#' from every line
        a = line.strip(delimiter)
        # remove '\n' from every line
        b = a.strip('\n')
        # append the contents of the b variable to the emptyList list
        emptyList.append(b)
    # print the updated list
    print (emptyList)

# execute function partTwo
partTwo()

# purpose of 3 is to read a file line by line and create a dictionary with color name as key and hex value as the value
# define function as partThree with no parameters
def partThree():
    # set variable openf to open contents of the file sortOfWhite.txt
    openf = open("sortOfWhite.txt", "r")
    # create an empty list called emptyList
    emptyList = []
    # create a dictionary
    dictionary = dict()
    counter = 0

    # for every line in the file
    for line in openf:
        # set the variable delimiter to '#'
        delimiter = '#'
        # remove the '#'
        a = line.strip(delimiter)
        # remove the '\n'
        b = a.strip('\n')
        c = b.split()
        print (c)

    # i would iterate through emptyList and then add into the dictionary with the color name as key and hex value as the value
# execute function partThree
partThree()
