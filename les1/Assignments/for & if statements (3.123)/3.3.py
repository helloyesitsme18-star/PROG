maandnum = int(input('Typ een maandnummer: '))
if maandnum >= 1 and maandnum <= 2 or maandnum == 12:
    print('Het is de winter .')
elif maandnum >= 3 and maandnum <= 5:
    print('Het is de lente.')
elif maandnum >= 6 and maandnum <= 8:
    print('Het is de zomer.')
elif 11 >= maandnum >= 9: #!!!
    print('Het is de herfst.')
else:
    print('ongeldig')
