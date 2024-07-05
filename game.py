import random

bot=['rock','paper','scissor']

b =random.choice(bot)


# take user input outside and pass it to function
user_in = input("Enter R for  rock, P for  paper, S for scissor:")

def user_input(user):
    if user=="R" or user=="r":
        out = "rock"
    elif user=="P" or user=="p":
        out = "paper"  
    elif user=="S" or user=="s":
        out = "scissor"
    else:
        out = "Invalid move"
    # print("Bot choose:",ans) this line is unnecessary
    return out
    
u = user_input(user_in)
print(u)
print(b)
# check for win or lose

def condition(u, b):
    if u==b:
        show = "Draw"
    elif u == "paper" and b == "rock":
        show = "wins"
    elif u == "rock" and b == "scissor":
        show = "wins"   
    elif u == "scissor" and b == "paper":
        show = "wins"
    else:
        show = "lose!"
    return show
    
result = condition(u, b)
print(result)
