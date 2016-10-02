try:
    outstandingBalance = float(raw_input("Please enter your outstanding balance: "))
    annualInterestRate = float(raw_input("Please enter the annual credit card interest rate as a decimal: "))
    minimumMonthlyPaymentRate = float(raw_input("Please enter the minimum monthly payment rate as a decimal: "))
    month = 0
    while month < 13:
        minimumMonthlyPayment = (minimumMonthlyPaymentRate * outstandingBalance)
        interestPaid = (annualInterestRate / 12 * outstandingBalance)
        principalPaid = (minimumMonthlyPayment - interestPaid)
        outstandingBalance = (outstandingBalance - principalPaid)
        
        print("Month: ", month)
        print("Minimum monthly payment: ", minimumMonthlyPayment)
        print("Principal paid: ", principalPaid)
        print("Remaining balance: ", outstandingBalance)
        month = month + 1

except:
    print("Not a number!")

