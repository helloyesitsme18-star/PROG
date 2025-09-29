getal = -1
som = 0
teller = 0

while getal != 0:
    getal = int(input('Geef een getal: '))
    if getal == 0:
        break
    som += getal
    teller += 1

print(f'Er zijn {teller} getallen ingevuld, de som is: {som}')