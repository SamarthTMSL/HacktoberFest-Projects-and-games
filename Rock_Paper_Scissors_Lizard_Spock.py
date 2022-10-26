import random

computer = random.choice(['r', 's', 'p', 'l', 'sp'])

def play():
    user = input(" Choose : 'r' for rock, 's' for scissors, 'p' for paper, 'l' for lizard, 'sp' for spock : ")

    if user == computer:
        return 'Game tied'
        # r>s, s>p, p>r, r>l l>sp, sp>s, s>l, l>p, p>sp, sp>r
    
    if is_win(user,computer):
        return 'You won :)'
    
    if is_win(computer,user):
        return 'You lost :('

    return 'Enter valid choice please.'

def is_win(player,opponent):
    #returns true when player wins
    # r>s, s>p, p>r, r>l l>sp, sp>s, s>l, l>p, p>sp, sp>r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 'l') \
        or (player == 'l' and opponent == 'sp') or (player == 'sp' and opponent == 's') or (player == 's' and opponent == 'l') or (player == 'l' and opponent == 'p')\
        or (player == 'p' and opponent == 'sp') or (player == 'sp' and opponent == 'r'):
        return True

print(play())
print(f'The computer chose {computer}')