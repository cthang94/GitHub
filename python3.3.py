def testingScore():
    try:
        score = float(input("Please enter your score between 0 and 1.0: "))

        if (score >= .9 and score <= 1.0):
            print("Your score is a A!")

        elif (score >= .8 and score < .9):
            print("Your score is a B!")

        elif  (score >= .7 and score < .8):
            print("Your score is a C!")

        elif (score >= .6 and score < .7):
            print("Your score is a D!")

        else:
            print("Your score is a F! You suck!")

    except:
        print("Wrong input! Please try again.")
        testingScore()

testingScore()
        
