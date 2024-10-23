import random

saker = ["Penna", "Bok", "Ring"]
validchoice = ["1","2","3","4"]
while True :
    choice = input("Vad vill du göra?\n[1] Print\n[2] Avsluta\n[3] Lägg till sak\n[4] Random sak\n")
    if choice in validchoice :
        if choice == "1" :
            for i in saker :
                print(i)
        if choice == "2" :
            break
        if choice == "3" :
            sak = input("Vilken sak vill du lägga till?\n")
            saker.append(sak.capitalize())
        if choice == "4" :
            print(saker[random.randint(len(saker))])
    else :
        print("Jag fattar inte")