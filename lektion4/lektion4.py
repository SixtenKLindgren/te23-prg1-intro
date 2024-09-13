import random
class card :
    def __init__(self, number, suit) :
        self.number = number
        self.suit = suit
# gör deck listan human readable
    def __repr__(self) :
        return f"{self.number} of {self.suit}"
# ger varje kort sitt värde och ger gubbar värdet av 10 (värdet för ess inte implementerat)
    def value(self) :
        if self.number > 10 :
            return 10
        else :
            return self.number
         
suits = ["hearts", "spades", "diamonds", "clubs"]
# skapar en lista: deck som har alla kort i sig
deck = [card(number, suit) for number in range(1, 14) for suit in suits] 


# lägg till valet om dom vill stanna eller hita

dealer = random.sample(deck, 2)
player = random.sample(deck, 2)
playertotal = sum(card.value() for card in player)
dealertotal = sum(card.value() for card in dealer)

print(f"Your hand is {player} which gives a total of {playertotal}")
print(f"Dealers hand is {dealer} which gives a total of {dealertotal}")

action = input("Hit or stand?")
if action == "hit" :
    player.append(random.choice(deck))
    print(f"Yours: {player}, total: {playertotal}")
    if playertotal > 21 :
        print("You bust")
if dealertotal < 17 :
    dealer.append(random.choice(deck))