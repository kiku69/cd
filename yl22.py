import random

options = ["kivi", "paber", "käärid"]
r = random.choice(options)

while True:
    a = input("sisesta kivi, paber või käärid: ")
    if a == "x":
        break

    if a == "kivi" and r == "käärid" or a == "paber" and r == "kivi" or a == "käärid" and r == "paber" or a == "kivi" and r == "kivi"
        print("sinu võit")
    elif a == "kivi" and r == "paber" or a == "paber" and r == "käärid" or a == "käärid" and r == "paber"
        print("sinu kaotus")
    else:
        print("viik")
