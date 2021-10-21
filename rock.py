import random 

def play():
    user = input("What's your choice? Select 'r' for Rock, 'p' for Paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Tie Game..."

    if is_winner(user, computer):
        return "You win!"
    
    return "You lose!"

def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True

print(play())