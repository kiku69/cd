def upc(a):
    a = str(a)
    counter = 0
    checkerneg = 0
    checkerpos = 0
    if len(a) < 11:
        a = ("0")*(11-len(a))+a
    for n in a:
        if counter % 2 == 0:
            checkerneg += int(n)
        else:
            checkerpos += int(n)
        counter += 1
    M = ((checkerneg*3)+checkerpos) % 10
    if M != 0:
        return 10 - M
    else:
        return 0
