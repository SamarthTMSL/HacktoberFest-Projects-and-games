import random

roll_once_more = "y"

print("THIS WILL GIVE YOU A SIMULATION FOR DOUBLE DICE ROLL\n")

while roll_once_more == "y":

    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)

    print("YOUR ROLL IS:\n")

    print(roll_1,"  ",roll_2,"\n")

    roll_once_more = input("Do you wish to roll again?(y/n) : ")
