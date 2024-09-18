import random
from termcolor import colored
class card :
    def __init__(self, number, suit) :
        self.number = number
        self.suit = suit
# Gör deck listan human readable
    def __repr__(self) :
        return f"{self.number} of {self.suit}"
# Ger varje kort sitt värde, ger gubbar värdet av 10 och ess får sitt värde beroende på handens total
    def value(self, who) :
        if self.number == "Ace":
            if who == "first" :
                return 11
            if who == "dealer" :
                if dealertotal > 10 :
                    return 1
                else :
                    return 11
            if who == "player" :
                if playertotal > 10 :
                    return 1
                else :
                    return 11
        if self.number in ["Jack", "Queen", "King"] :
            return 10
        else :
            return self.number
         
suits = [colored("hearts ♥", "red"), colored("spades ♠", "black"), colored("diamonds ♦", "red"), colored("clubs ♣", "black")]
# Skapar en lista: deck som har alla kort i sig
deck = [card(number, suit) for number in ["Ace", 2, 3, 4, 5, 6, 7, 8, 9 , 10, "Jack", "Queen", "King"] for suit in suits] 

# Skapar dealers och spelarens hand
stood = 0
dealer = random.sample(deck, 2)
player = random.sample(deck, 2)
playertotal = sum(card.value("first") for card in player)
dealertotal = sum(card.value("first") for card in dealer)

print(f"Your hand is {player} Total: {playertotal}")
print(f"Dealers hand is {dealer} Total: {dealertotal}")

while True :
    if dealertotal == 21 or playertotal == 21 :
        break
# Ser till att man skriver en korrekt action (hit eller stand)
    while True and stood == 0 : 
        action = input("Hit or stand? ").lower()        
        if action in ["hit", "stand", "h", "s"] :
            break
        else :
            print("Thats not a valid answer please enter hit, stand, h or s")

# Utför aktionen som spelar säger (hit eller stand)
    if action in ["hit", "h"] :
        player.append(random.choice(deck))
        playertotal = sum(card.value("player") for card in player)
        print(f"Your new hand is: {player} Total: {playertotal}")
    elif action in ["stand", "s"]:
        print(f"You stand. Your hand is {player} Total: {playertotal}")
        stood = 1
        if dealertotal > 16 :
            break
    
    if playertotal > 21 :
        print("You bust")
        break

# Bestämmer om dealer ska hitta och hittar om den ska det
    if dealertotal < 17 :
        dealer.append(random.choice(deck))
        dealertotal = sum(card.value("dealer") for card in dealer)
        print(f"The dealer hits and its new hand is {dealer} Total: {dealertotal}")
        if dealertotal > 21 :
            print("The dealer busts")
            break
    else :
        print(f"The dealer stands. Its hand is: {dealer} Total: {dealertotal}")


# printar en vem som har vunnit
if dealertotal == playertotal :
    print("Its a tie")
elif playertotal == 21 :
    print(colored("Blackjack! You win", "green"))
elif playertotal > dealertotal and playertotal < 22 or dealertotal > 21 :
    print(colored("You win", "green"))
else :
    print(colored("You lose", "red"))