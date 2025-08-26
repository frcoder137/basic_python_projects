import random
import emoji

choices = ['r', 'p', 's']

print("Rock Paper Scissors")

user = input(">> ")
computer = random.choice(choices)

emoji_list = {'r': emoji.emojize(":raised_fist:"), 'p': emoji.emojize(":raised_hand:"), 's': emoji.emojize(":victory_hand:")}

print("user: ", emoji_list.get(user))
print("computer: ", emoji_list.get(computer))

def win(user, computer):
    status = ''
    if user == 'r':
        if computer == 's':
            status = 'win'
        elif computer == 'p':
            status = 'lose'
        elif computer == 'r':
            status = 'tie'
    elif user == 'p':
        if computer == 's':
            status = 'lose'
        elif computer == 'p':
            status = 'tie'
        elif computer == 'r':
            status = 'win'
    elif user == 's':
        if computer == 'p':
            status = 'win'
        elif computer == 's':
            status = 'tie'
        elif computer == 'r':
            status = 'lose'

    return status

print(win(user, computer))