import time
n=18
number_of_guesses=1
print("Enter your name: ")
x=input()
x=x.capitalize()
print("Hello", x)
print("Number of guesses is limited to only 5 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("You enter less number please input greater number\n")
    elif guess_number>18:
        print("You enter greater number please input smaller number\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"No. of guesses he took to finish")
        break
    print(5-number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>5):
    time.sleep(2)
    print("Game Over")
