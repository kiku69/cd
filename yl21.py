import random
num = random.randint(1, 100)
quess = None

while quess != num:
    quess = input("Arva number 1-100: ")
    quess = int(quess)

    if quess == num:
        print("Õige JAAA")
    elif quess > num:
        print("On liiga suur")
    else:
        print("ON liiga väike")
