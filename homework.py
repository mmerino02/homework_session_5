print("This program will calculate your net income based on your gross income")
print(" ")
try:
    gross = int(input("What is your gross income? "))
    children = int(input("How many children do you have? "))
    print(" ")
except ValueError:
    print("one of the numbers was not valid")
except NameError:
    print("Sorry the program is lacking. Please come back later.")

else:
    if gross < 1000:
        net1 = gross-((gross*0.10)+((gross*0.01)*children))
        print(net1, "is your net income")
    elif gross < 2000:
        net2 = gross-((gross*0.12)+((gross*0.01)*children))
        print(net2, "is your net income")
    elif gross < 4000:
        net3 = gross-((gross*0.14)+((gross*0.005)*children))
        print(net3, "is your net income")
    else:
        net4 = gross - ((gross * 0.18)+((gross*0.005)*children))
        print(net4, "is your net income")
