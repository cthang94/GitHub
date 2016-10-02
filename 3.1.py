def computation():
    hours = int(raw_input("Enter hours: "))
    rate = int(raw_input("Enter rate: "))

    if (hours > 40):
        newRate = rate * 1.5
        pay = (rate * 40) + (newRate * (hours - 40))
        print("The pay is: ", pay)

computation()

