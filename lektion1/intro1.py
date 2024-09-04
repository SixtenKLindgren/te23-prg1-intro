print("Hej")
namn = input("Vad heter du? ")

print(f"Hej {namn} Välkommen")

print("Hur gammal är du?")

ålder = input("Skriv ditt ålder") 

print(f"Super bra att du är {ålder} år gammal ") 

if int(ålder) >= 15:
    print("Du får köra mopped")
else:
    print("Men du får inte köra mopped")