maandnr = int(input('Voer hier een maandnummer in: '))

if 3 <= maandnr <= 5:
    print(f'lente')
elif 6 <= maandnr <= 8:
    print(f'zomer')
elif 9 <= maandnr <= 11:
    print(f'herfst')
elif maandnr in (12, 1, 2):
    print(f'winter')
else:
    print(f'Ongeldige invoer')