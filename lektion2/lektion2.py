import random
money = 1000
while money > 0:
    bet = input("Bet?: ")
    bet = int(bet)
    if bet < money:
        dice = random.randint(1,6)
        print (f"You rolled {dice}")
        if dice > 3:
            money = money + bet
            print (f"You won {bet}!")
        else: 
            money = money - bet
            print (f"You lost {bet}")
        print (f"You now have {money}")
    else:
        print("You can't afford that")