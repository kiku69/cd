letters = ("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
a = input("sisesta sõna").lower()

b=a.count("a") +a.count("e") +a.count("i") +a.count("o") +a.count("u") +a.count("õ") +a.count("ä") +a.count("ö") +a.count("ü")
print(b)

i = 0
for c in a:
    if c in letters:
        i += 1
print(i)
