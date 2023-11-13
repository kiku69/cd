name = input("palun sisestage oma nimi: ")
print("tere", name)

area = input("palun sisestage elukoht: ")
if "saaremaa" in area.lower():
    print("tere saarlane")

age = input("palun sisestage oma vanus: ")
if age < 17:
    print("sa oled liiga noor")
elif age == 18:
    print("palju õnne, sa oled täisealine!")
else:
    print("sa võid autot juhtida")