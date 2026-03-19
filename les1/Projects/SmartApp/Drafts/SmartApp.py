def Fahrenheit(temp_celsius):
    return temp_celsius * 1.8 + 32

def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    return temp_celsius - (luchtvochtigheid / 100) * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    temp_gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if temp_gevoel < 0 and windsnelheid > 10:
        return (f'Het is heel koud en het stormt! Verwarming helemaal aan!')
    elif temp_gevoel < 0 and windsnelheid <= 10:
        return (f'Het is behoorlijk koud! Verwarming aan op de benedenverdieping!')
    elif 0 <= temp_gevoel < 10 and windsnelheid > 12:
        return (f'Het is best koud en het waait; verwarming aan en roosters dicht!')
    elif 0 <= temp_gevoel < 10 and windsnelheid < 12:
        return (f'Het is een beetje koud, elektrische kachel op de benedenverdieping aan!')
    elif 10 <= temp_gevoel < 22:
        return (f'Heerlijk weer, niet te koud of te warm.')
    else:
        return(f'Warm! Airco aan!')

def weerstation():
    temp_celsius_hist = []  # lijst om gem.temp te op te slaan


    for dag in range(1,8):

#Temperatuur
        while True:
            temp_1 = input(f'Hoeveel graden is het op dag {dag}? (°C): ')
            if temp_1 == '':
                print("Leeg vak, het programma stopt nu.")
                return
            try:
                temp_celsius = float(temp_1)
                break

            except ValueError:
                print('Probeer opnieuw, onjuist type invoer')

#Windsnelheid
        while True:
            wind = input (f'Wat is de windsnelheid op dag {dag}? (m/s): ')
            if wind == '':
                print("Leeg vak, het programma stopt nu.")
                return
            try:
                windsnelheid = float(wind)
                break
            except ValueError:
                print('Probeer opnieuw, onjuist type invoer')

#Luchtvochtigheid
        while True:
            vochtigheid = input (f'Wat is de luchtvochtigheid op dag {dag}? (%): ')
            if vochtigheid == '':
                print("Leeg vak, het programma stopt nu.")
                return
            try:
                luchtvochtigheid = float(vochtigheid)
                if luchtvochtigheid < 0 or luchtvochtigheid > 100:
                    print('Invoer moet tussen 0-100 liggen, probeer nogmaals.')
                    continue
                break
            except ValueError:
                print('Probeer opnieuw, onjuist type invoer')


        temp_celsius_hist.append(temp_celsius)
        gem_temp = sum(temp_celsius_hist) / len(temp_celsius_hist)
        print(f'Het is {temp_celsius:.1f}C en {Fahrenheit(temp_celsius):.1f}F')
        print(weerrapport(temp_celsius, windsnelheid, luchtvochtigheid))
        print(f'De gemiddelde temperatuur is vandaag {gem_temp:.1f}C')
        print("=======================================================================")

def aantal_dagen(inputFile):

    try:
        with open(inputFile) as bestand:
            regels = bestand.readlines()
            dagen = len(regels) - 1
            return dagen

    except FileNotFoundError:  #Als het deze foutmelding geeft crasht het bestand niet hierdoor en returnt hij -1
        print('Geen bestand gevonden.')
        return -1

def auto_bereken(inputFile, outputFile):

    with open(inputFile, 'r') as bestand1:
        regel = bestand1.readlines()[1:] #slaat de headerregel over dmv indexeren

    with open(outputFile, 'w') as bestand2:
        for dag in regel:
            data = dag.strip().split()

            datum = data[0]
            numPeople = int(data[1])
            tempSetpoint = float(data[2])
            tempOutside= float(data[3])
            precip = float(data[4])

            cv_stand = -1

            cvketel = tempSetpoint - tempOutside
            if cvketel >= 20:
                cv_stand = 100
            elif 10 <= cvketel < 20:
                cv_stand = 50
            elif cvketel < 10:
                cv_stand = 0

            ventilatie = numPeople + 1
            if ventilatie > 4:
                ventilatie = 4


            if precip < 3:
                bewatering = True
            elif precip >= 3:
                bewatering = False

            bestand2.write(f'{datum};{cv_stand};{ventilatie};{bewatering}\n')


def overwrite_settings(outputFile):
    try:
        with open(outputFile, 'r') as bestand:
            regels = bestand.readlines()

    except FileNotFoundError:
        print("Het bestand bestaat nog niet. Voer eerst optie 2 uit om het bestand aan te maken.")
        return -1

    user_datum = input('Voer een datum in (dd-mm-yyyy): ')
    print('1. CV Ketel instellen\n2. Ventilatie instellen\n 3. Bewatering instellen')
    keuze_menu = input('Maak uw keuze: ')
    aanpassing = input('Geef een nieuwe waarde op: ')


    nieuw = []
    datum_ok = False

    for dag in regels:
        data = dag.strip().split(';')
        datum = data[0]

        if datum == user_datum:
            datum_ok = True

            if keuze_menu == '1':
                try:
                    waarde = int(aanpassing)
                    if 0 <= waarde <= 100:
                        data[1] = str(waarde)
                    else:
                        return -3
                except ValueError:
                    return -3

            elif keuze_menu == '2':
                try:
                    waarde = int(aanpassing)
                    if 0 <= waarde <= 4:
                        data[2] = str(waarde)
                    else:
                        return -3
                except ValueError:
                    return -3

            elif keuze_menu == '3':
                if aanpassing == '0':
                    data[3] = False
                if aanpassing == '1':
                    data[3] = True
                else:
                    return -3
        nieuw.append(';'.join(data) + '\n')

    if not datum_ok:
        return -1

    with open(outputFile, 'w') as bestand:
        bestand.writelines(nieuw)

    return 0


def smart_app_controller():
    inputFile = 'inputFile.txt'
    outputFile = 'outputFile.txt'

    print("Welkom bij de Smart App Controller!")
    print("Dit programma heeft de volgende opties:")
    print("1. Aantal dagen tellen in het inputbestand")
    print("2. Automatisch actuatorinstellingen berekenen")
    print("3. Instellingen handmatig overschrijven")
    print("4. Programma afsluiten")

    keuze = input("Maak uw keuze (1-4): ")

    if keuze == '1':
        resultaat = aantal_dagen(inputFile)
        if resultaat == -1:
            print("Het bestand kon niet worden gevonden.")
        else:
            print(f"Aantal dagen in het bestand: {resultaat}")

    elif keuze == '2':
        auto_bereken(inputFile, outputFile)
        print("Automatische berekening voltooid. Resultaat opgeslagen in outputFile.txt.")

    elif keuze == '3':
        resultaat = overwrite_settings(outputFile)
        if resultaat == 0:
            print("Instelling succesvol aangepast.")
        elif resultaat == -1:
            print("Datum niet gevonden in bestand.")
        elif resultaat == -3:
            print("Ongeldige invoer of systeemkeuze.")

    elif keuze == '4':
        print("Programma afgesloten.")

    else:
        print("Ongeldige keuze. Probeer opnieuw.")
smart_app_controller()









