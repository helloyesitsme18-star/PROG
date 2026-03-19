leeftijd  = int(input('Geef je leeftijd: '))
paspoort = input('Nederlands paspoort: ')


if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, u mag stemmen!')
else:
    print('Helaas, u mag niet stemmen.')


#Wanneer je OR statements gebruikt, duidelijk aanduiden wat de vergelijking is
# if leeftijd > 18 or leeftijd < 60