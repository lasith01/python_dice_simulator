import random

print("Welcome to Rolling Dice Simulator")

while True:
    choice = input("Want to roll the dice? (y/n)")
    if choice.lower() != 'y':
        break

    num = random.randint(1, 6)

    if num==1:
        print("---------------")
        print("               ")
        print("       0       ")
        print("               ")
        print("---------------")

    elif num==2:
        print("---------------")
        print("               ")
        print("      0  0     ")
        print("               ")
        print("---------------")

    elif num==3:
        print("---------------")
        print("               ")
        print("    0  0  0    ")
        print("               ")
        print("---------------")

    elif num==4:
        print("---------------")
        print("               ")
        print("    0  0  0    ")
        print("       0       ")
        print("---------------")

    elif num==5:
        print("---------------")
        print("               ")
        print("      0 0 0    ")
        print("       0 0     ")
        print("---------------")

    else :
        print("---------------")
        print("               ")
        print("    0  0  0    ")
        print("    0  0  0    ")
        print("---------------")

