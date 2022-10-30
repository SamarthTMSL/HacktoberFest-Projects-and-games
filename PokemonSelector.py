import random

def pokeball():
    return random.choice(["ChariZard", "Zekrom", "Bulbasaur", "Wartortle", "Abomasnow", "Arceus"])

p = pokeball()
n=input("Enter your name: ")
print("Congratulations!!", n,"\nYou got: ")
print(p, "as your partner pokemon!")
