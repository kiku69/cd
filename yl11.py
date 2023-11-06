sisend = input("Sisesta string: ")

puhastatud_sisend = sisend.strip()

if len(puhastatud_sisend) >= 7 and len(puhastatud_sisend) % 2 != 0:

    keskmine_indeks = len(puhastatud_sisend) // 2
    kolm_keskmine = puhastatud_sisend[keskmine_indeks - 1:keskmine_indeks + 2]
    
    print("Kolm keskmist sümbolit on:", kolm_keskmine)
else:
    print("Sisestatud string ei vasta nõuetele.")
