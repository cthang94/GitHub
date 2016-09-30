# Calvin Thang
# Homework 2


# set the variable to open the file
try:
    fopen = open("climdata.txt", "r")

except:
    print("Sorry, the file does not exist.")


else:

    # create a dict to store kay value
    info = dict()

    # create a for loop to go through every line in the file
    for line in fopen:

        # skip the line if the program sees Hour (skips first line)
        if "Hour" in line:
            continue
        else:
            
            line = line.translate("F")

            # slice the string from the beginning to the 8th part
            
            time = line[:8]
            # tokenize the line
            line.split
            # slice a part of the string and put it in the variable temp
            temp = line[10:14]
            # a dictionary containing time, temp key value pairs
            info[time] = temp

    # find the greatest number
    for digit in info:
        answer = max(info, key=info.get)

        print("The highest temperature of", info[answer], "fahrenheit happened at", answer)
    
