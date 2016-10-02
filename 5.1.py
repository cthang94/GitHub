try:
    counter = 0
    while counter >= 0:
        enterNumber = int(raw_input("Please enter a number: "))
        counter = counter + 1

    if enterNumber == "done":
        print("done!")

except:
    print("Not a number!")
