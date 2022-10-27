import random

def hangman():
    random_words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","accept","acceptable","accessible","accidental","account","accurate","achiever","acid","acidic","acoustic","acoustics","acrid","act"]
    word = random.choice(random_words)
    turns = 10
    guessmade = ''
    valid_entry = 'abcdefghijklmnopqrstuvwxyz'

    while len(word) > 0 and turns > 0:
        main_word = ''

        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + '_ '
        if main_word == word:
            print(word)
            print("You won!!!")
            break
        
        print('Guess the word: ', main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print('Enter valid letter please:')
            guess = input()
        
        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print('-----------------')
            if turns == 8:
                print("8 turns left")
                print('-----------------')
                print('     o     ')
            if turns == 7:
                print("7 turns left")
                print('-----------------')
                print('     o     ')
                print('     |     ')
            if turns == 6:
                print("6 turns left")
                print('-----------------')
                print('     o     ')
                print('     |     ')
                print('    /      ')
            if turns == 5:
                print("5 turns left")
                print('-----------------')
                print('     o     ')
                print('     |     ')
                print('    / \    ')
            if turns == 4:
                print("4 turns left")
                print('-----------------')
                print('    \o     ')
                print('     |     ')
                print('    / \    ')
            if turns == 3:
                print("3 turns left")
                print('-----------------')
                print('    \o/    ')
                print('     |     ')
                print('    / \    ')
            if turns == 2:
                print("2 turns left")
                print('-----------------')
                print('    \o/  | ')
                print('     |     ')
                print('    / \    ')
            if turns == 1:
                print("1 turn left")
                print('-----------------')
                print('    \o/__| ')
                print('     |     ')
                print('    / \    ')
            if turns == 0:
                print("You loose :(")
                print("You let an innocent man die! ")
                print('-----------------')
                print('     o__| ')
                print('    /|\     ')
                print('    / \    ')
                break

name = input("Enter your name: ")
print('Welcome ', name , '!')
print('----------------------')
print('Try to guess a word in 10 lives available ->')
hangman()