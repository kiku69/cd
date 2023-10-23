a = float(input("sisesta esimese külje pikkus:"))
b = float(input("sisesta teise külje pikkus:"))
c = float(input("sisesta kolmanda külje pikkus:"))
if a + b > c and c + b > a and c + a > b:
    if a == b and b == c and c == a:
    
        print("kolmnurk on võrdkülgne")
    elif a == b or b == c or c == a:
        print("kolmnurk on võrdhaarne")
    else:
        print("kolmnurk on erikülgne")
else:
    print("ei eksisteeri")
