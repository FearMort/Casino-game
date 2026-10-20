import random
choices = ["Black","White"]
TotalAmount = float(input("Enter your total amount : "))
while TotalAmount > 0:
    GamblingAmount = float(input("Enter the amount of money you are gambling : "))
    GamblerChoice = input("Black or White?")
    MachineChoice = random.choice(choices)
    if GamblingAmount > TotalAmount:
        print("You dont have enough money")
    elif GamblerChoice == MachineChoice:
        TotalAmount = TotalAmount + GamblingAmount
        print("Your Choice was correct! You won ",GamblingAmount," $" )
        
    else:
        print("Your choice was incorrect, you lost: ", GamblingAmount)
        TotalAmount = TotalAmount - GamblingAmount
    print("your total is now : ",TotalAmount)