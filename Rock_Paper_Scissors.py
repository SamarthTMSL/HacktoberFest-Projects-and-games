def function():
    if (c1 == "R" and b1 == "P") or (c1 == "P" and b1 == "S") or (c1 == "S" and b1 == "R"):
        return True
    elif (c1 == "R" and b1 == "S") or (c1 == "P" and b1 == "R") or (c1 == "S" and b1 == "P"):
        return False
    elif (c1 == "R" and b1 == "R") or (c1 == "P" and b1 == "P") or (c1 == "S" and b1 == "S"):
        return None
    else:
        f = "You can only choose between given options"
        return f


while True:
    def values(b, c):
        my_dict = {
            "R": "Rock",
            "P": "Paper",
            "S": "Scissors"
        }
        if b in my_dict:
            print(f"You chose {my_dict[b]}")
            print(f"Computer chose {my_dict[c]}")
        else:
            print("You can only choose between given options")


    b1 = str.title(input("""
    Type R for Rock
    Type P for Paper
    Type S for Scissors
    If you want to quit type Q
    """))
    import random
    a = random.randint(1, 3)
    if b1 == 'Q':
        print("""You Quit!
Start Over
        """)
        break
    if a == 1:
        c1 = "R"
        function()
        values(b1, c1)
    elif a == 2:
        c1 = "P"
        function()
        values(b1, c1)
    elif a == 3:
        c1 = "S"
        function()
        values(b1, c1)
    s = function()
    if s is True:
        r = "You Won"
        print(r)
    elif s is False:
        r = "You Lose"
        print(r)
    elif s is None:
        r = "It's a tie"
        print(r)
