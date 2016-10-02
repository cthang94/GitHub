try:
    hours = int(raw_input("Enter hours: "))
    rate = int(raw_input("Enter rate: "))

    pay = hours * rate
    print("The pay is ", pay)

except:
    print("Please enter an integer")
