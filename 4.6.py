def computepay(hours,rate):


    if (hours > 40):
        newRate = rate * 1.5
        pay = (rate * 40) + (newRate * (hours - 40))
        return pay

    else:
        pay = hours * rate
        return pay



x = computepay(45,10)
print (x)
