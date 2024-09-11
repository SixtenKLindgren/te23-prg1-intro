from random import randint
p1score = 0
p2score = 0
while p1score < 2 and p2score < 2:  
    p1dice = randint(1, 6)
    p2dice = randint(1, 6)
    if not p1dice == p2dice :
        if p1dice > p2dice :
            p1score = p1score + 1
            print(f"Player 1 wins with a roll of: {p1dice}")
        else :
            p2score = p2score + 1
            print(f"Player 2 wins with a roll of: {p2dice}")
    else : 
        print(f"Both players rolled: {p1dice}")
        p1score = p1score + 1
        p2score = p2score + 1
    print(f"The score is {p1score}, {p2score}")
if p1score == 2 :
    print("Player 1 wins!")
else : 
    print("Player 2 wins!")


    
    


