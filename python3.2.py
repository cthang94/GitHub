


def chapter3exercise3point2():
    try:
        hours = int(input("Please enter the hours: "))
        rate = int(input("Please enter the rate: "))
        pay = hours * rate

        if (hours == str or rate == str):
            print("Invalid input, please enter a numeric input")
            chapter3exercise3point2()

        else:
            print("The pay is... ", pay)

    except:
        print("Invalid input, please enter a numeric input")
        chapter3exercise3point2()

    
chapter3exercise3point2()
