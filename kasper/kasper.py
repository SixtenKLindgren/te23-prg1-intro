count = 0
players = ["Player 1", "Player 2", "Player 3", "Player 4"]
playorder = 0
playdirection = 1
while count < 100 :
    count += 1
    if count%7 == 0 or count%11 == 0 or "7" in str(count) or "11" in str(count) :
        print(players[playorder] + ": Klapp")
        playdirection = playdirection * -1
    else : 
        print(f"{players[playorder]}: {count}")
    if playorder + playdirection > 3 :
        playorder = 0
    elif playorder + playdirection < 0 :
        playorder = 3
    else :
        playorder += playdirection