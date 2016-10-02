try:
    def computation(score):
        score = computation()

        if (score >= 0.9):
            print("You have an A!")

        elif (score >= 0.8):
            print("You have a B!")

        elif (score >= 0.7):
            print("You have a C!")

        elif (score >= 0.6):
            print("You have a D!")

        else:
            print("You have an F!")

    computation(0.3)

except:
    print("Invalid!")
