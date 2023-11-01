import random

def play():
    user = input("what's is your choice ? 'r' for rock, 'p' for paper, 's' for scissors : \n ")
    computer = random.choice(['r', 'p', 's'])
    
    
    if user == computer:
        return 'It\'s a tie'
    
    # r > s, s > p, p > r
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, oponent):
    #return true if player wins
    # r > s, s > p, p > r
    
    if (player == 'r' and oponent == 's') or (player) or (player == 'p' and oponent == 'r') or (player == 's' and oponent == 'p'):
        return True
    
print(play())
        