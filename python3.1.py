hours = int(input("Please enter hours: "))
rate = int(input("Please enter the rate: "))

if (hours > 40):
    newRate = int(rate * 1.5)
    pay = newRate * hours
    pay = str(pay)
    print("The pay is... ", pay)

else:
    pay2 = hours * rate
    pay2 = str(pay2)
    print("The pay is... ", pay2)

