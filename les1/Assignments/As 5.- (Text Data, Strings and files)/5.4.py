import datetime
#print(s, naam)

bestand = open('oefening_5_4_hardlopers.txt', 'a')
print('Typ \'stop\' om het programma de stoppen')
while True:
    naam = input('\nWat is de naam van de hardloper: ')
    if naam == 'stop':
        bestand.close()
        break
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")

    bestand.write(f'{s}, {naam}\n')



