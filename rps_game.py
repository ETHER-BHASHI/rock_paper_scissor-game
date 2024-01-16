import random


def play():
    user=input("CHOOSE YOUR OPTION : 'r' for rock,'p' for paper, and 's' for scissor\n").lower()
    comp=random.choice(['rock','paper','scissor'])
    print(f"Computers choce is {comp}")
    if user==comp:
        return "tie \nmoyeee moyyeee"
    if is_win(user, comp):
        print(f"")
        return "YOU WON! :)"
    return "YOU LOST ! :( "
    
    
def is_win(player, opponent):
    #r>s,s>p,p>r
    if (player=='rock' and opponent=='scissor') or (player=='scissor' and opponent=='paper') or (player=='paper' and opponent=='rock'):
        return True
    
    
print(play())