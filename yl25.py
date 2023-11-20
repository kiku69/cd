dictionary = {
    "eesnimi": "Kristofer",
    "perenimi": "Mere",
    "sünniaasta": 2007,
    "elukoht": "Saaremaa",
    "lemmik_magustoit": "jäätis",
}

print(dictionary.get("elukoht"))
print(dictionary["elukoht"])

dictionary["lemmik_magustoit"] = "šokolaad"

for key in dictionary:
    print(key)

for value in dictionary.values():
    print(value)

if "isikukood" in dictionary:
    print("Isikukood on olemas")
else:
    print("isikukoodi pole")

print(len(dictionary))

dictionary["height"] = "187cm"
del dictionary["birth_year"]

dictionary.clear()
